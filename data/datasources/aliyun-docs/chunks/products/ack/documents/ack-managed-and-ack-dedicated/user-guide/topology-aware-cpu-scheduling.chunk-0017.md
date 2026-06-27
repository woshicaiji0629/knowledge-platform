## 生产环境使用建议
可观测性：在启用绑核前后，[接入阿里云](use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md)[Prometheus](use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md)[监控](use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md)，密切关注应用的关键性能指标（如RT、QPS）以及节点的CPU使用率、CPU Throttling等指标，关注绑核带来的性能变化。
分批变更：对于多副本应用，建议采用金丝雀发布或分批更新的方式，逐步启用或停用绑核策略，以控制变更风险。
