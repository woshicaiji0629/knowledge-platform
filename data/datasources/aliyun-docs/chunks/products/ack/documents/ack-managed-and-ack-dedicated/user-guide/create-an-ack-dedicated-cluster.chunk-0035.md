有SLS Project或新建一个SLS Project，用于收集集群应用日志。
同时将启用集群API Server审计功能，收集对Kubernetes API的请求以及请求结果。
如需后续启用，请参见[采集](collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)[ACK](collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)[集群容器日志](collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)、[使用集群](../security-and-compliance/work-with-cluster-auditing.md)[API Server](../security-and-compliance/work-with-cluster-auditing.md)[审计功能](../security-and-compliance/work-with-cluster-auditing.md)。
创建 Ingress Dashboard：在SLS控制台创建Ingress Dashboard，可收集Nginx Ingress访问日志，请参见[Nginx Ingress](analyze-and-monitor-the-access-log-of-nginx-ingress.md)[访问日志分析与监控](analyze-and-monitor-the-access-log-of-nginx-ingress.md)。
安装 node-problem-detector 并创建事件中心：在SLS控制台中添加事件中心，实时收集集群中的所有Kubernetes Event，请参见[创建并使用](../../../../sls/documents/create-and-use-an-event-center.md)[K8s](../../../../sls/documents/create-and-use-an-event-center.md)[事件中心](../../../../sls/documents/create-and-use-an-event-center.md)。
云资源及计费说明：[SLS](../../../../sls/documents/billing-overview.md)
集群巡检
启用智能运维的[集群巡检功能](work-with-the-cluster-inspection-feature.md)，定期扫描集群内配额、资源水位、组件版本等
