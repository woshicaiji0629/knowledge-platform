## 直连模式
直连模式为类似连接原生Redis Cluster的方式连接集群。客户端首次连接时会通过DNS将直连地址解析为一个随机数据分片的虚拟IP（VIP）地址，之后即可通过Redis Cluster协议访问各数据分片。集群架构直连模式同样支持多副本与单节点，但不支持开启读写分离，直连模式的服务架构和说明如下。
集群架构直连模式服务架构（以多副本为例）
说明
直连模式与代理模式的连接方式区别较大，相关注意事项和连接示例请参见[使用直连模式连接实例](../user-guide/use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)。
