### 采集标准输出
以下为四种采集配置方式。建议只使用一种方法管理日志采集配置：

| 配置方式 | 配置说明 | 场景适用 |
| --- | --- | --- |
| （推荐）CRD-AliyunPipelineConfig | 通过 K8s CRD 管理日志采集配置。 | 适用于需要复杂采集和处理需求以及在 ACK 集群中确保日志与应用版本一致性的场景。 |
| CRD-AliyunLogConfig | 旧版 CRD 管理方式。 | 支持已知场景的旧版管理方式。 需要逐渐迁移到新版本 CRD-AliyunPipelineConfig 以享受更好的扩展性和稳定性。两类 CRD 采集方式对比请参见 [CRD](../../../../sls/documents/use-crd-to-manage-collection-configurations.md) [类型](../../../../sls/documents/use-crd-to-manage-collection-configurations.md) 。 |
| 日志服务控制台 | 图形化界面直接管理，快速部署配置。 | 适合少量采集配置的创建和管理，部分高级功能和自定义需求无法通过实现。 |
| 环境变量 | 通过环境变量快速配置日志参数。 | 进行简单配置调整，不支持复杂处理逻辑，仅支持单行文本日志。可满足以下定制需求： 将多个应用数据采集到同一 Logstore。 将不同应用数据采集到不同的 Project。 |
