## 背景信息
[开启直连模式](enable-the-direct-connection-mode.md)时，云数据库 Tair（兼容 Redis）会为该集群中所有数据分片的master节点分配一个虚拟IP（VIP）地址。客户端在首次向直连地址发送请求前会通过DNS服务器解析直连地址，解析结果会是集群中一个随机数据分片的VIP。获取到VIP后，客户端即可通过Redis Cluster协议操作该集群中的数据。下图展示了直连模式下集群的服务架构。
