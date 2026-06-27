## ACK专有集群
单阿里云账号最大集群数：0（[已停止创建](../ack-managed-and-ack-dedicated/user-guide/create-an-ack-dedicated-cluster.md)）
单集群最大节点池数①：100
单集群最大节点数：
使用Flannel容器网络插件：默认支持200个，最大支持1000个节点
使用Terway容器网络插件：默认支持5,000个，最大支持15,000个节点
单节点最大Pod数②：
使用Flannel容器网络插件：256
使用Terway容器网络插件：单节点Pod限额由节点规格决定。详见[节点](../ack-managed-and-ack-dedicated/user-guide/work-with-terway.md)[Pod](../ack-managed-and-ack-dedicated/user-guide/work-with-terway.md)[限额计算方法](../ack-managed-and-ack-dedicated/user-guide/work-with-terway.md)
配额提升方式：
[到配额平台提交申请](https://quotas.console.aliyun.com/products/csk/quotas)
