import onnxruntime as rt

sess_providers = rt.get_available_providers()
# sess_providers = [('CUDAExecutionProvider', {
#                 # 'device_id': 0,
#                 'gpu_mem_limit': 4 * 1024 * 1024 * 1024,
#                 # 'arena_extend_strategy': "kNextPowerOfTwo",
#                 # 'cudnn_conv_algo_search': 'EXHAUSTIVE',
#                 'do_copy_in_default_stream': False
#                 }),
#                 'CPUExecutionProvider',]

sess_options = rt.SessionOptions()
# sess_options.inter_op_num_threads = 1
# sess_options.intra_op_num_threads = 1
# sess_options.execution_mode = rt.ExecutionMode.ORT_SEQUENTIAL
# sess_options.graph_optimization_level = rt.GraphOptimizationLevel.ORT_ENABLE_ALL

runsess = rt.InferenceSession("segment.onnx", sess_options, sess_providers)