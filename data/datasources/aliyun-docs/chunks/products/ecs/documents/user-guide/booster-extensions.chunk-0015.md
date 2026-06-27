### 模型、框架版本及性能提升
在主流GPU实例上进行了openclip和bevformer模型应用优化前后的性能测试，测试环境和优化效果如下
测试环境

| 测试环境 | 说明 |
| --- | --- |
| 操作系统 | 阿里云公共镜像 Ubuntu 22.04、阿里云公共镜像 Ubuntu 24.04 |
| 内核版本 | 5.15.0-144-generic |
| gcc 版本 | 11.4.0 |
| glibc 版本 | 2.35 |
| keentune | 3.2.61 |
| python | 3.10.12 |
| pytorch | 2.7.0a0+ecf3bae40a.nv25.2 |
| nccl | 2.26.2 |
| mmcv-full | 1.7.2 |
| mmdet3d | 1.0.0rc4 |

优化效果

| 实例规格 | 模型 | 训练/推理 | 平均吞吐提升（samples/s） |
| --- | --- | --- | --- |
| ebmgn8v.48xlarge | Bevformer | bevformer_base 训练 | FP32（10%+） FP16（8%+） |
| Openclip | RN50 推理 | 20%+ |  |
| RN50 训练 | 25%+ |  |  |

CPFS FUSE加速效果如下表所示：
CPFS FUSE加速当前仅支持阿里云公共镜像Ubuntu 24.04版本，以下测试数据基于该操作系统版本得出。

| 性能场景分类 | 用例场景 | 性能数据 | 性能提升 | 备注 |
| --- | --- | --- | --- | --- |
| 带宽 | Buffer 读（1M IO） | 40GB/s | 2.5 倍 | 原生 FUSE 约为 15GB/s |
| 带宽 | Buffer 写（1M IO） | 40GB/s | 10 倍 | 原生 FUSE 约为 4GB/s |
| IOPS | Direct 读（4k IO） | 1,000,000 | 2.5 倍 | 原生 FUSE 约为 400,000 |

该文章对您有帮助吗？
反馈
