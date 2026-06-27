）。
计算：
采用全新Blackwell架构专业显卡：
支持OpenGL 专业级图形处理功能
支持RTX、TensorRT等常用加速功能，全新升级支持FP4和PCIe Gen5互联。
采用PCIe Switch互联，相比直连CPU方案，其NCCL性能提升36%，多卡分片大模型推理时，性能最大提升9%。
GPU主要参数：

| GPU 架构 | GPU 显存 | 计算性能 | 视频编解码能力 | 卡间互联 | 加速 APIs |
| --- | --- | --- | --- | --- | --- |
| Blackwell | 容量：72 GB 带宽：1344GB/s | TF32: 126 TFLOPS FP32: 52 TFLOPS FP16/BF16: 266 TFLOPS FP8/INT8: 530 TFLOPS FP4: 971 TFLOPS RT core: 196 TFLOPS | 3 * Video Encoder 3 * Video Decoder | PCIe Gen5 x16: 128GB/s 支持 P2P | 支持 DX12、 OpenGL4.6、Vulkan1.3、CUDA12.8、Open CL3.0、DirectCompute |
