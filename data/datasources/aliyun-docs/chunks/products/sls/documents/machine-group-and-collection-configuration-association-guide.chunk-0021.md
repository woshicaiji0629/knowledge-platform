### 如何修改采集配置
为确保日志采集配置稳定可靠，修改操作必须在采集配置的原始创建位置进行。若跨途径修改（如配置由环境变量创建却在控制台调整），采集配置可能在Pod重建、组件更新等运维操作中被原始来源覆盖，引发日志格式异常、采集中断等风险。
以下是各创建方式对应的规范修改方法及关键注意事项：
SLS控制台/CLI/SDK创建：在SLS控制台/CLI/SDK直接修改采集配置。
容器服务控制台/业务容器环境变量创建：调整容器环境变量（如 aliyun_logs_*），参数详见[采集](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)[ACK](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)[集群容器日志](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)。不支持在SLS控制台修改。
环境变量创建采集配置是一种快速接入方式，仅支持基础采集路径配置，无法设置高级参数或处理插件，如需使用高级功能，建议：删除当前容器环境变量与已创建的采集配置 → 改用SLS控制台、SDK、CLI或CRD方式重新创建。
若采集配置通过环境变量方式创建，并曾经在SLS控制台补充过处理插件或高级参数，这些修改可能在Pod重建或组件更新等情况下被原始采集配置覆盖丢失，请尽快迁移。
CRD方式创建：直接编辑对应的CR资源（如 AliyunPipelineConfig），参数详见[AliyunPipelineConfig](kubernetes-cr-parameter-description.md)[参数说明](kubernetes-cr-parameter-description.md)。不支持在SLS控制台修改。
若采集配置通过CRD - AliyunPipelineConfig方式创建，并曾经在SLS控制台修改，所有改动均会在修改后30分钟内被还原，请检查当前采集配置是否符合预期。
若采集配置通过CRD - AliyunLogConfig方式创建，并曾经在SLS控制台修改，这些修改可能在Pod重建或组
