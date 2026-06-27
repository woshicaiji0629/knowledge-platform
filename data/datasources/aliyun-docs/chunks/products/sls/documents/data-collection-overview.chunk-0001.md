### Kubernetes环境下的采集方案
当企业应用部署在Kubernetes环境下，使用阿里云日志服务进行采集时请参考如下内容：
[Kubernetes](container-log-collection-in-a-kubernetes-cluster.md)[集群容器日志采集](container-log-collection-in-a-kubernetes-cluster.md)：对于应用日志采集有两种方式，支持标准输出与文本日志类型，采集前请阅读[Kubernetes](kubernetes-cluster-container-log-collection-instructions.md)[集群容器日志采集须知](kubernetes-cluster-container-log-collection-instructions.md)。
[通过控制台采集集群容器日志（标准输出/文件）](collect-kubernetes-cluster-text-logs-daemonset.md)：通过控制台手动可视化配置日志采集规则，适合少量集群及测试环境的使用场景。
[通过](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)[Kubernetes CRD](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)[采集集群容器日志（标准输出/文件）](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)：使用CRD自定义资源配置日志采集规则，方便模板化，生产集群优先选择，支持CI/CD自动化的场景。
[采集](use-prometheus-to-collect-kubernetes-metric-data.md)[Kubernetes](use-prometheus-to-collect-kubernetes-metric-data.md)[监控数据(Metric)](use-prometheus-to-collect-kubernetes-metric-data.md)：本文介绍如何在Kubernetes上部署Prometheus，将监控数据采集到日志服务MetricStore中，并将日志服务MetricStore对接到Grafana实现监控数据可视化展示。
[采集](collect-kubernetes-events.md)[Kubernetes](collect-kubernetes-events.md)[事件](
