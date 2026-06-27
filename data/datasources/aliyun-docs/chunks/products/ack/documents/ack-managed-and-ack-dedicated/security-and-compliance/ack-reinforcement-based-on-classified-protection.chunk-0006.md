## 使用Alibaba Cloud Linux等保2.0三级版
[创建](../user-guide/create-an-ack-managed-cluster-2.md)[ACK](../user-guide/create-an-ack-managed-cluster-2.md)[集群](../user-guide/create-an-ack-managed-cluster-2.md)时，您可以启用等保加固。ACK会为集群自动配置等保加固项，使其满足国家信息安全部发布的《GB/T22239-2019信息安全技术网络安全等级保护基本要求》中对操作系统的等级保护要求。
重要
为满足等保2.0三级版的标准要求，ACK会在等保加固的Alibaba Cloud Linux中默认创建ack_admin、ack_audit、ack_security三个普通用户。
为满足等保2.0三级版的标准要求，等保加固的Alibaba Cloud Linux禁止使用root用户通过SSH登录。您可通过[ECS](https://ecs.console.aliyun.com/)[控制台](https://ecs.console.aliyun.com/)[通过](../../../../ecs/documents/user-guide/log-on-to-an-instance-by-using-vnc.md)[VNC](../../../../ecs/documents/user-guide/log-on-to-an-instance-by-using-vnc.md)[连接实例](../../../../ecs/documents/user-guide/log-on-to-an-instance-by-using-vnc.md)，创建可使用SSH的普通用户。
