## How to generate or update the py files for a proto 
```shell
cd retailcore_proto
py -m grpc_tools.protoc --proto_path=./proto --python_out=./py_grpc --pyi_out=./py_grpc --grpc_python_out=./py_grpc ./proto/user.proto
```

### After the file must have been generated, navigate to py_grpc folder and make the following edit

Old [protoName]_pb2_grpc.py as [protoName]__pb2_grpc.py
```python
import user_pb2 as user__pb2
```

New [protoName]_pb2 as [protoName]__pb2
```python
from retailcore_proto.py_grpc import user_pb2 as user__pb2
```

Finally, update the version number in retailcore_proto/__init__.py by increasing using the right semantic naming convention
```python
__version__ = '0.0.x'
```

## Usage of this library
Add the following to your project requirements.txt file
```
git+https://github.com/Prunedge-Dev-Team/retailcore-shared-proto.git@main
```
