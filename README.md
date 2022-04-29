# onnx-flask-demo

parallel call a flask server in windows10

## run test
1. ```python service-XXX.py```, to start the server.  
2. ```python call_http_server.py```, run multiple times, simulating parallel calls to the server.  

## problem
when run more then 8 times ```python call_http_server.py```, the memory of GPU will be fill, and the program will be fail
Error information: 
```
onnxruntime.capi.onnxruntime_pybind11_state.RuntimeException: [ONNXRuntimeError] : 6 : RUNTIME_EXCEPTION : Non-zero status code returned while running Clip node.
bfc_arena.cc:342 onnxruntime::BFCArena::AllocateRawInternal Failed to allocate memory for requested buffer of size xxx
```