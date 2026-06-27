## 注意事项
如果您的实例为[集群架构](../product-overview/cluster-master-replica-instances.md)或[读写分离架构](../product-overview/read-or-write-splitting-instances-1.md)，实例默认会提供Proxy（代理）节点的连接地址，连接方式与连接标准架构的实例相同。
说明
集群架构的实例通过[直连地址](enable-the-direct-connection-mode.md)连接时，连接方式与连接开源Redis Cluster相同。
如果实例开启了[专有网络免密访问](enable-password-free-access.md)，同一专有网络下的客户端程序无需设置密码即可连接实例。
