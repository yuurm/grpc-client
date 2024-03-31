```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip install grpcio grpcio-tools
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. phonebook.proto
pip install buf
```