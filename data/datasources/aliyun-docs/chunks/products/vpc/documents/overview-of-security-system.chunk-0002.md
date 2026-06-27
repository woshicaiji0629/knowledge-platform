### 安全防护功能
专有网络VPC可以通过以下功能保障云服务的安全性和可靠性。

| 功能 | 描述 |
| --- | --- |
| ECS 安全组 | 安全组是一种虚拟防火墙，具备状态检测和数据包过滤能力，用于在云端划分安全域。通过配置安全组规则，您可以控制安全组内一台或多台 ECS 实例的入流量和出流量。详细信息，请参见 [安全组概述](../../ecs/documents/user-guide/overview-44.md) 。 |
| 网络 ACL | 网络 ACL 是 VPC 中的网络访问控制功能。您可以自定义设置网络 ACL 规则，并将网络 ACL 与交换机绑定，实现对交换机中 ECS 实例的流量的访问控制。详细信息，请参见 [网络](network-acl-overview.md) [ACL](network-acl-overview.md) [概述](network-acl-overview.md) 。 |
| 流日志 | 专有网络 VPC 提供流日志功能，可以记录 VPC 网络中弹性网卡 ENI（Elastic Network Interface）传入和传出的流量信息，帮助您检查访问控制规则、监控网络流量和排查网络故障。详细信息，请参见 [流日志概述](vpc-flow-logs.md) 。 |
| 流量镜像 | VPC 流量镜像功能可以镜像经过弹性网卡 ENI 且符合筛选条件的报文。通过流量镜像功能，您可以复制 VPC 中 ECS 实例的网络流量，然后将复制后的网络流量转发给指定的弹性网卡或私网传统型负载均衡 CLB（Classic Load Balancer）实例，用于内容检查、威胁监控和问题排查等场景。详细信息，请参见 [流量镜像概述](traffic-mirroring-overview.md) 。 |
