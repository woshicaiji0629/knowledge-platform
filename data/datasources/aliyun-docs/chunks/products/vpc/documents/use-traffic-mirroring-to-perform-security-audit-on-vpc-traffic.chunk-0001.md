## 前提条件
已创建两个VPC，每个VPC内创建1台ECS实例。
您可以结合业务需求，为ECS1绑定EIP，通过EIP提供公网服务。
ECS2作为镜像目的，绑定EIP访问公网，以部署Suricata。
本文示例中服务器操作系统统一为Alibaba Cloud Linux 3.2104 LTS 64位。
确保ECS2的安全组入方向放开4789端口，允许ECS1封装的UDP协议报文访问ECS2的4789端口，以接收镜像流量。
初次使用流量镜像功能时，根据提示开通流量镜像功能。
镜像源和镜像目的不属于同一个VPC时，需要确保VPC间互通。本文示例通过[VPC](create-and-manage-vpc-peering-connection.md)[对等连接](create-and-manage-vpc-peering-connection.md)连通两个VPC。
已创建阿里云Elasticsearch实例并开启Kibana公网访问，[将本机公网](https://help.aliyun.com/zh/es/user-guide/configure-kibana-public-network-or-private-network#t614906.html)[IP](https://help.aliyun.com/zh/es/user-guide/configure-kibana-public-network-or-private-network#t614906.html)[地址添加到白名单](https://help.aliyun.com/zh/es/user-guide/configure-kibana-public-network-or-private-network#t614906.html)。
