### GPU计算型弹性裸金属服务器实例规格族ebmgn8ia
该实例目前仅支持海外等部分地域，如有需求，请联系阿里云销售人员。
规格族介绍：ebmgn8ia是阿里云针对搜索推荐、仿真和其他GPU计算稀疏类（平均每颗GPU需要配备比较多的vCPU资源）业务的发展推出的第8代加速计算规格族（弹性裸金属实例规格族），采用最新NVIDIA L20 GPU，每个实例为一台采用了2颗高主频CPU和4个GPU计算卡的裸金属主机。
产品特色及适用场景：
高主频：该产品配置了2颗AMD EPYC™ Genoa 9T34处理器，每颗处理有64个物理核，整机提供256个vCPU，主频高达3.4-3.75GHz。大幅提高CPU单核性能，适用于CAD建模，并提升CAE仿真的前期预处理速度。
稀疏资源配比：平均GPU配置了64 vCPU和384 GiB内存，平均每个GPU的内存带宽达到230 GB/s, 适合高I/O吞吐的GPU计算场景，如广告、搜索、推荐以及传统CAE仿真，部分采用CPU渲染的影视制作等。
采用最新的CIPU 1.0云处理器：
具有解耦计算和存储能力，可以灵活选择所需存储资源。相对于上一代，该实例规格的机器间带宽提升至160 Gbit/s，可以更快地完成数据传输和处理。
CIPU提供裸金属能力，相对于传统虚拟化实例，可以支持GPU实例之间的PCIe P2P通信。
计算：
采用全新NVIDIA L20企业级GPU：
支持vGPU、RTX、TensorRT等常用加速功能。
支持FP8精度，提升计算效率。
NVIDIA L20主要参数：

| GPU 架构 | GPU 显存 | 计算性能 | 视频编解码能力 | 卡间互联 |
| --- | --- | --- | --- | --- |
| NVIDIA Ada Lovelace | 容量： 48 GB 带宽： 864 GB/s | FP64: N/A FP32: 59.3 TFLOPS FP16/BF16: 119 TFLOPS FP8/INT8: 237 TFLOPS | 3 * Video Encoder（+AV1） 3 * Video Decoder 4 * JPEG Decoder | PCIe 接口：PCIe Gen4 x16 带宽：64 GB/s |
