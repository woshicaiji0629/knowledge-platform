### 注解说明
通过在原生的Service上添加Annotation实现流量的拓扑配置，相关参数如下所示。

| annotation Key | annotation Value | 说明 |
| --- | --- | --- |
| openyurt.io/topologyKeys | kubernetes.io/hostname | 限制 Service 只能被本节点访问。 |
| openyurt.io/topologyKeys | kubernetes.io/zone 或 openyurt.io/nodepool | 限制 Service 只能被本节点池的节点访问。 ACK Edge 集群 版本如果大于等于 1.18，推荐您使用 openyurt.io/nodepool。 |
| - | - | Service 不做任何拓扑限制。 |
