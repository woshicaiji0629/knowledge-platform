### 多个集群/环境下日志采集后统一查询分析
比如测试，生产等不同环境集群的日志需要统一进行查询分析，可以有三种方式：
在采集数据时，将数据储存在同一个LogStore，建议通过[通过控制台采集集群容器日志（标准输出/文件）](collect-kubernetes-cluster-text-logs-daemonset.md)添加Tag来区分环境。当需要统一查询时，即可在该LogStore中直接进行查询分析。
在采集数据时，采集到不同的LogStore甚至是不同地域的Project中，当需要统一查询分析时，通过创建虚拟资源[StoreView](cross-logstore-query-and-analysis.md)来关联多个LogStore进行查询。此方式不额外增加存储，但只能查询不能修改，且不支持设置告警进行监控。使用时可通过tag字段判断日志来自哪一个LogStore。
（推荐）在采集数据时，采集到不同的LogStore甚至是不同地域的Project中，当需要统一查询分析时，通过[数据加工](data-processing-new-version-quick-start.md)将选取的数据复制并存储到指定的LogStore中。此方式可对选取的数据进行解析处理后再进行存储，支持设置告警监控，但该功能需要额外收费。
