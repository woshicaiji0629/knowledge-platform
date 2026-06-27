### IP类型
未开启远端IP时，仅支持添加当前VPC网段内的IP地址；开启远端IP后，还可添加其他VPC或本地IDC中的IP地址。
说明
自北京时间2025年2月25日00:00:00起，对于新建实例默认使用升级后的ALB，已创建的ALB实例不受影响（提交自助申请创建的实例除外）。具体可参考[应用型负载均衡](../../product-overview/alb.md)[ALB](../../product-overview/alb.md)[实例升级公告](../../product-overview/alb.md)。
使用限制
警告
升级前的ALB实例不支持通过IP类型服务器组挂载同一个VPC内的ALB、NLB或CLB实例。如果需要挂载同VPC下的该类资源，请确保使用ALB升级实例，否则可能会导致服务异常。
升级后
后端服务器限制
只支持挂载私网IP地址，不支持挂载公网IP地址。
IP协议版本为IPv4/v6双栈时，仅支持添加当前服务器组所在VPC网段内的IPv6地址，不支持启用远端IP。
ALB与后端服务器间的转发配置限制
如果使用企业版转发路由器，请注意：企业版转发路由器会在用户指定的可用区的交换机实例上创建弹性网卡ENI（Elastic Network Interface），作为VPC实例向企业版转发路由器发送流量的入口。创建VPC实例时，请确保在指定的可用区中创建至少一个交换机实例，以便将VPC实例连接至企业版转发路由器。详情请参见[转发路由器工作原理](../../../../cen/documents/product-overview/how-transit-routers-work.md)。
ALB与后端服务器的流量仅支持通过系统路由表转发，暂不支持通过VPC自定义路由表转发。
升级前
后端服务器限制
[升级前](../product-overview/supported-regions-and-zones.md)[ALB](../product-overview/supported-regions-and-zones.md)[实例挂载远端](../product-overview/supported-regions-and-zones.md)[IP](../product-overview/supported-regions-and-zones.md)[支持的地域](../product-overview/supported-regions-and-zones.md)。
跨地域挂载的后端服务器仅支持IP类型。
只支持挂载私网IP地址，不支持挂载公网IP地址。
不支持挂载同一个VPC内的ALB、NLB或CLB实例。
ALB与后端服务器间的转发配置限制
支持通过企业版转发路由器或高速通道实现远端IP转发，不支持基础版转发路由器。
如果使用企
