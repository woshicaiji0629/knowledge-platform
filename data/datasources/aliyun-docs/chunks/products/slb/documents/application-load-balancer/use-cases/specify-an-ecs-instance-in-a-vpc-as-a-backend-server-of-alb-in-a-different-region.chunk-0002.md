## 使用限制
说明
自北京时间2025年2月25日00:00:00起，对于新建实例默认使用升级后的ALB，已创建的ALB实例不受影响（提交自助申请创建的实例除外）。具体可参考[应用型负载均衡](../../product-overview/alb.md)[ALB](../../product-overview/alb.md)[实例升级公告](../../product-overview/alb.md)。
本文默认使用ALB升级实例作为示例。如果您使用的是升级前的ALB实例，请参见[升级前](specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region.md)[ALB](specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region.md)[实例操作说明](specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region.md)。
后端服务器限制
跨地域挂载的后端服务器仅支持IP类型。
只支持挂载私网IP地址，不支持挂载公网IP地址。
如果您需要挂载IPv6服务器，添加IP类型服务器组时，需要将IP协议版本设置为IPv4/v6双栈，注意事项如下：
仅当服务器组选择的VPC已[开启](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#task-2198980)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#task-2198980)[功能](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#task-2198980)时，支持将IP协议版本设置为IPv4/v6双栈。
仅支持添加至双栈[ALB](../../product-overview/alb.md)[升级实例](../../product-overview/alb.md)的监听或转发规则中。升级前的ALB实例不支持。
IP协议版本为IPv4/v6双栈时，仅支持添加当前服务器组所在VPC网段内的IPv6地址，不支持启用远端IP。
ALB与后端服务器间的转发配置限制
如果使用企业版转发路由器，请注意：企业版转发路由器会在用户指定的可用区的交换机实例上创建弹性网卡ENI（Elastic Network Interface
