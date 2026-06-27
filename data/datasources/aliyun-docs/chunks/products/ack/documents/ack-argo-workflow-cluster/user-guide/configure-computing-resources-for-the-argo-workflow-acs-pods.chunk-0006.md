### 算力质量（Compute QoS）
不同的算力质量在资源供给上会有所区别，以适应不同的业务场景，ACS当前提供了2种算力质量：

| 算力质量 | 标签 | 特点 | 典型应用场景 |
| --- | --- | --- | --- |
| 默认型 | default | 有一定的算力扰动。 不存在强制的实例驱逐，实例故障通过热迁移或者通知用户触发驱逐完成。 | 微服务应用 Web 应用 计算类任务 |
| BestEffort 型 | best-effort | 有一定的算力扰动。 存在强制的实例抢占和驱逐，驱逐前 5 分钟会有事件通知。 | 大数据计算 音视频转码 批处理任务 |

通过使用Pod上的alibabacloud.com/compute-qos标签指定实例的算力质量。
BestEffort算力质量实例为动态库存，强烈建议在生产环境配置库存优先调度策略，在库存不足时由平台自动切换至默认型。更多信息，请参见[高级配置参数](https://help.aliyun.com/zh/cs/user-guide/custom-resource-priority-scheduling#095649ebeaybl)。
