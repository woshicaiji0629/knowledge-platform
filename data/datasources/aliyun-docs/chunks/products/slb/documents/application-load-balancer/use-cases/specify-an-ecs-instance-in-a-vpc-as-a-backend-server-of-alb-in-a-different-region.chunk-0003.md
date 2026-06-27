LB实例不支持。
IP协议版本为IPv4/v6双栈时，仅支持添加当前服务器组所在VPC网段内的IPv6地址，不支持启用远端IP。
ALB与后端服务器间的转发配置限制
如果使用企业版转发路由器，请注意：企业版转发路由器会在用户指定的可用区的交换机实例上创建弹性网卡ENI（Elastic Network Interface），作为VPC实例向企业版转发路由器发送流量的入口。创建VPC实例时，请确保在指定的可用区中创建至少一个交换机实例，以便将VPC实例连接至企业版转发路由器。详情请参见[转发路由器工作原理](../../../../cen/documents/product-overview/how-transit-routers-work.md)。
ALB与后端服务器的流量仅支持通过系统路由表转发，暂不支持通过VPC自定义路由表转发。
