## CRD类型
警告
使用AliyunPipelineConfig，需要日志组件版本最低为0.5.1。
为了便于通过云原生方式管理Logtail采集配置，日志服务定义了两类CRD，它们的能力与区别见下表：

| 类型 | AliyunPipelineConfig（推荐使用） | AliyunLogConfig |
| --- | --- | --- |
| ApiGroup | telemetry.alibabacloud.com/v1alpha1 | log.alibabacloud.com/v1alpha1 |
| CRD 资源名 | ClusterAliyunPipelineConfig | AliyunLogConfig |
| 作用域 | 集群 | 命名空间 |
| 采集配置格式 | 基本等价于日志服务 API 中的 [LogtailPipelineConfig](developer-reference/api-sls-2020-12-30-struct-logtailpipelineconfig.md) | 基本等价于日志服务 API 中的 [LogtailConfig](developer-reference/api-sls-2020-12-30-struct-logtailconfig.md) |
| 跨地域能力 | 支持 | 支持 |
| 跨账号能力 | 支持 | 支持 |
| Webhook 校验参数 | 支持 | 不支持 |
| 配置冲突检测 | 支持 | 日志组件 0.5 以上版本支持 |
| 配置难度 | 较低 | 较高 |
| 配置可观测性 | Status 包含错误详情、更新时间、上次应用成功配置、上次应用成功时间等信息 | Status 包含错误码与错误信息 |

该文章对您有帮助吗？
反馈
