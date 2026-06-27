## APF限流
说明
APF限流相关指标监控处于灰度发布中。
APF相关指标仅支持1.20及以上版本集群。如需升级，请参见[手动升级集群](update-the-kubernetes-version-of-an-ack-cluster.md)。
APF相关指标大盘还依赖如下组件的升级，请参见[组件监控升级说明](https://help.aliyun.com/zh/prometheus/user-guide/update-monitoring-components)完成升级：
容器集群监控组件：0.06及以上版本。
[ack-arms-prometheus](../../../../arms/documents/prometheus-monitoring/prometheus-monitoring-change-records-2.md)组件：v1.1.31及以上版本。
托管探针：v1.1.31及以上版本。
可观测性展示
功能解析
下表中部分指标按PL、Instance、FS维度进行统计。
PL：Priority Level维度，即根据不同优先级进行统计。
Instance：根据API Server实例维度进行统计。
FS：Flow Schema维度，即根据请求分类进行统计。
关于APF及上述维度的详细信息，请参见[APF](https://kubernetes.io/docs/concepts/cluster-administration/flow-control/)。
