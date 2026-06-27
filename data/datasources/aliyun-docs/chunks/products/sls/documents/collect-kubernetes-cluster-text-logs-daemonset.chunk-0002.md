## 采集配置创建流程
[安装](collect-kubernetes-cluster-text-logs-daemonset.md)[LoongCollector](collect-kubernetes-cluster-text-logs-daemonset.md)：通过DaemonSet模式部署LoongCollector，确保集群中每个节点均运行一个采集容器，统一采集该节点上所有容器的日志。
Sidecar模式请参考[采集](collect-k8s-cluster-logs-through-sidecar.md)[Kubernetes Pod](collect-k8s-cluster-logs-through-sidecar.md)[文本日志（Sidecar](collect-k8s-cluster-logs-through-sidecar.md)[模式）](collect-k8s-cluster-logs-through-sidecar.md)。
[创建](collect-kubernetes-cluster-text-logs-daemonset.md)[LogStore](collect-kubernetes-cluster-text-logs-daemonset.md)：用于存储采集日志。
[创建并配置日志采集规则](collect-kubernetes-cluster-text-logs-daemonset.md)
[全局与输入配置](collect-kubernetes-cluster-text-logs-daemonset.md)：定义采集配置的名称及日志采集的来源和范围。
[日志处理与结构化](collect-kubernetes-cluster-text-logs-daemonset.md)：根据日志格式进行处理配置。
多行日志：适用于单条日志跨越多行（如 Java 异常堆栈、Python traceback），需通过行首正则识别每条日志的起始行。
结构化解析：通过配置解析插件（如正则、分隔符、NGINX 模式等）将原始字符串提取为结构化的键值对，便于后续查询与分析。
[日志过滤](collect-kubernetes-cluster-text-logs-daemonset.md)：通过配置采集黑名单和内容过滤规则，筛选有效日志内容，减少冗余数据的传输与存储。
[日志分类](collect-kubernetes-cluster-text-logs-daemonset.md)：通过配置日志主题（Topic）和日志打标灵活区分不同业务、容器或路径来源的日志。
[查询与分析配置](collect-kubernetes-cluster-text-logs-daemonset.md)：系统默认开启全文索引，支持关键词搜索。建议启用字段索引，以便
