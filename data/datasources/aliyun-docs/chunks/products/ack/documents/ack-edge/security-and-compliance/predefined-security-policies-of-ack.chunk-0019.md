### ACKProtectCoreDNS
规则说明：防止kube-system命名空间中CoreDNS相关资源被删除，包括其使用的Deployment、Service和ConfigMap。
重要等级：high。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| min_replicas | int | 定义 CoreDNS Deployment 期望的最小副本数量。 |
