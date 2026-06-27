### GPU计算型实例规格族gn9gc
说明
gn9gc正在邀测中，如需使用，请提交工单申请。
规格族介绍：gn9gc是阿里云推出的第9代高性价比GPU云服务器实例。采用最新一代CIPU 2.0提供云服务能力，采用高主频处理器，并配置适当容量的内存，针对大语言模型生成场景和视频、图像生成场景提供高性价比的实例。同时GPU可以直接提供图形处理能力，支持各类渲染业务需求。
适用场景：
大模型推理：全新一代GPU提供超越8代的全新算力，显存带宽大幅提升，新支持FP4算力全面提升推理性能和性价比。多卡并行推理效率大大提升。
计算：
采用最新的CIPU 2.0云处理器。
第2代CIPU提供更高的云处理算力，提供更强的eRDMA、VPC、EBS组件算力。支持容器（包括但不限于Docker、Clear Container、Pouch等）。
采用全新Blackwell架构专业显卡：
支持OpenGL专业级图形处理功能。
支持RTX、TensorRT等常用加速功能，全新升级支持FP4和PCIe Gen5互联。
GPU主要参数：

| GPU 架构 | GPU 显存 | 计算性能 | 视频编解码能力 | 卡间互联 | 加速 APIs |
| --- | --- | --- | --- | --- | --- |
| NVIDIA Blackwell | 容量： 72 GB 带宽： 1344 GB/s | TF32： 126 TFLOPS FP32： 52 TFLOPS FP16/BF16： 266 TFLOPS FP8/INT8： 530 TFLOPS FP4： 970 TFLOPS RT Core： 196 TFLOPS | 3 * Video Encoder 3 * Video Decoder | PCIe 接口：PCIe Gen5 x16 带宽：128 GB/s，支持 P2P | DX12、OpenGL 4.6、Vulkan 1.3、CUDA 12.8、OpenCL 3.0、DirectCompute |
