## 使用限制
集群类型：仅支持ACK托管集群Pro版、ACK托管集群基础版、ACK专有集群。
集群版本及操作系统限制：仅支持内核版本大于4.19的Alibaba Cloud Linux、Ubuntu、ContainerOS操作系统。
Alibaba Cloud Linux：集群版本为1.18及以上。
ContainerOS：集群版本为1.24及以上。
Ubuntu：
集群版本为1.30及以上。如需升级集群，请参见[手动升级集群](../../ack-managed-and-ack-dedicated/user-guide/update-the-kubernetes-version-of-an-ack-cluster.md)。
节点初始化时，会关闭操作系统自动升级。
节点初始化时，把/etc/resolv.conf软连接指向到/run/systemd/resolve/stub-resolv.conf，将 DNS服务器指向 DHCP配置。
目前不支持CPFS存储卷、镜像加速插件、安全加固等功能。
