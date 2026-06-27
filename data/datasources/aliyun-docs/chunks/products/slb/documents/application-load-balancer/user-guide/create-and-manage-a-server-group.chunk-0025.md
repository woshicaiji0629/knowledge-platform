## 添加IPv6后端服务器
当用户需要在服务器组中挂载IPv6类型的后端服务器时，可以将IP协议版本设置为IPv4/v6双栈。
仅服务器类型和IP类型的服务器组支持。
需要服务器组所属VPC已[开启](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#task-2198980)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#task-2198980)[功能](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#task-2198980)。
IP协议版本为IPv4/v6双栈的服务器组，仅支持添加至双栈ALB实例的监听转发规则中。
IP类型服务器组还要求ALB实例为[升级实例](../../product-overview/alb.md)，且仅支持当前VPC网段内的IPv6地址，不支持启用远端IP。
