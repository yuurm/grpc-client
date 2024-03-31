import grpc
import phonebook_pb2
import phonebook_pb2_grpc
import tkinter as tk
from tkinter import messagebox

class PhoneBookClient:
    def __init__(self, host='localhost', port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = phonebook_pb2_grpc.PhoneBookServiceStub(self.channel)

    def add_entry(self, first_name, last_name, patronymic, phone_number, note):
        entry = phonebook_pb2.Entry(
            first_name=first_name,
            last_name=last_name,
            patronymic=patronymic,
            phone_number=phone_number,
            note=note
        )
        response = self.stub.AddEntry(entry)
        return response

    def delete_entry(self, phone_number):
        entry = phonebook_pb2.Entry(phone_number=phone_number)
        response = self.stub.DeleteEntry(entry)
        return response

    def search_entry(self, query):
        entry = phonebook_pb2.Entry(phone_number=query)
        entries = self.stub.SearchEntry(entry)
        return entries

    def view_entry(self, phone_number):
        entry = phonebook_pb2.Entry(phone_number=phone_number)
        response = self.stub.ViewEntry(entry)
        return response

class PhoneBookGUI:
    def __init__(self, root):
        self.client = PhoneBookClient()

        self.root = root
        self.root.title("Phone Book")

        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(padx=10, pady=10)

        self.first_name_label = tk.Label(self.entry_frame, text="First Name:")
        self.first_name_label.grid(row=0, column=0, padx=5, pady=5)
        self.first_name_entry = tk.Entry(self.entry_frame)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Add other fields similarly

        self.add_button = tk.Button(self.entry_frame, text="Add Entry", command=self.add_entry)
        self.add_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def add_entry(self):
        first_name = self.first_name_entry.get()
        # Get other fields similarly
        response = self.client.add_entry(first_name, last_name, patronymic, phone_number, note)
        messagebox.showinfo("Info", "Entry added successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneBookGUI(root)
    root.mainloop()
