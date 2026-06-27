### 计算类型（Compute Class）
ACS Pod支持下列算力计算类型：

| 计算类型 | 标签 | 适用场景 |
| --- | --- | --- |
| 通用型（默认） | general-purpose | 满足绝大部分无状态微服务应用 、Java Web 应用、计算类任务等。 |
| 性能型 | performance | 满足性能需求更强的业务场景，如 CPU Based AI/ML 训练和推理、HPC 批处理等。 |
| GPU 型 | gpu | 满足 AI/HPC 等异构计算场景，如 GPU 单卡、多卡推理，GPU 并行计算等。 |
| 高性能网络 GPU 型（gpu-hpn) | gpu-hpn | 满足 AI/HPC 等异构计算场景，如 GPU 分布式训练，分布式推理，GPU 高性能计算等。 |

通过使用Pod上的alibabacloud.com/compute-class标签指定实例的计算类型。下方示例分别演示了四种计算类型的配置方法：
关于ACS Pod计算类型的更多说明，请参见[ACS Pod](https://help.aliyun.com/zh/cs/user-guide/acs-pod-instance-overview)[实例概述](https://help.aliyun.com/zh/cs/user-guide/acs-pod-instance-overview)。
