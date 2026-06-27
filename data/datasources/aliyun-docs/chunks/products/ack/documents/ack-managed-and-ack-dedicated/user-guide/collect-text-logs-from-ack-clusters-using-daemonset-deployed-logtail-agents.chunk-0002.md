## 索引

| 操作步骤 | 操作链接 |
| --- | --- |
| 步骤一：安装日志采集组件 | 在以下两个日志采集组件中选择一个进行安装。 [安装](collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [LoongCollector（推荐）](collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) LoongCollector 是 SLS 推出的新一代采集 Agent，是 Logtail 的升级版。 [安装](collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [Logtail](collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) Logtail 组件是用于采集 Kubernetes 日志的 Agent，支持多种日志类型及标准容器和 Kubernetes 集群的日志数据采集。 |
| 步骤二：创建采集配置 | 根据采集需求选择文本日志或标准输出。 [采集文本日志](collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) 文本日志是由容器内的程序生成并保存到指定目录下的日志文件，适用于需要对指定目录下的日志文件长期分析或故障排查等场景。 [采集标准输出](collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) 标准输出（stdout）是容器内程序在运行时生成的实时日志，适用于程序调试和快速定位问题等场景。 |
| 步骤三：查询分析日志 | 通过控制台进行日志查询与分析。 [查询分析日志](collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [日志默认字段](collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) |
