## 使用限制
双栈支持的地域，请参见[ALB](../user-guide/alb-instance-overview.md)[双栈支持的地域](../user-guide/alb-instance-overview.md)。
使用双栈功能，需要开通VPC可用区中交换机的IPv6功能。
双栈ALB实例支持将IPv4和IPv6的客户端流量转发至IPv4、IPv6的后端服务。详情请参见[ALB](../user-guide/alb-instance-overview.md)[实例概述](../user-guide/alb-instance-overview.md)。
不支持已有的IPv4实例升级为双栈实例，仅支持新建双栈实例。
IP协议版本为IPv4/v6双栈的服务器组，仅支持添加至双栈ALB实例的监听或转发规则中。
