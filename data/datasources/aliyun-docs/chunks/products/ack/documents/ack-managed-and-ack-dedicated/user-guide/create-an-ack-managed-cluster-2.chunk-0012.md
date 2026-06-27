| 参数 | 描述 | 参数组合 |
| --- | --- | --- |
| cluster_type | 集群类型。创建 ACK 托管集群 时，该参数必须配置为 ManagedKubernetes 。 | 创建 ACK 托管集群 Pro 版 "cluster_type": "ManagedKubernetes" "profile": "Default" "cluster_spec": "ack.pro.small" 创建 ACK 托管集群基础版 "cluster_type": "ManagedKubernetes" "profile": "Default" "cluster_spec": "ack.standard" |
| profile | 集群子类型。创建 ACK 托管集群 时，该参数必须配置为 Default 。 |  |
| cluster_spec | 集群规格。 ack.pro.small ：表示创建 ACK 托管集群 Pro 版 。 ack.standard ：表示创建 ACK 托管集群基础版 。 |  |
