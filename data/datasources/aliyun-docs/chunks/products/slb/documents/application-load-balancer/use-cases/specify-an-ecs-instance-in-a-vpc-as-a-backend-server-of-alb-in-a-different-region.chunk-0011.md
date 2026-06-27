### 如何使用升级前的ALB实例挂载跨地域VPC内的服务器？
如果您使用升级前的ALB实例，需要按照以下步骤进行操作。使用升级前的ALB实例需要为VPC1、VPC2、转发路由器添加路由，并为ECS实例配置安全组。具体操作，请参见[步骤五：配置路由和安全组](specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region.md)。其余步骤与上文相同，此处不再描述。
使用限制
后端服务器限制
[升级前](../product-overview/supported-regions-and-zones.md)[ALB](../product-overview/supported-regions-and-zones.md)[实例挂载远端](../product-overview/supported-regions-and-zones.md)[IP](../product-overview/supported-regions-and-zones.md)[支持的地域](../product-overview/supported-regions-and-zones.md)。
跨地域挂载的后端服务器仅支持IP类型。
只支持挂载私网IP地址，不支持挂载公网IP地址。
不支持挂载同一个VPC内的ALB、NLB或CLB实例。
ALB与后端服务器间的转发配置限制
支持通过企业版转发路由器或高速通道实现远端IP转发，不支持基础版转发路由器。
如果使用企业版转发路由器，请注意：企业版转发路由器会在用户指定的可用区的交换机实例上创建弹性网卡ENI（Elastic Network Interface），作为VPC实例向企业版转发路由器发送流量的入口。创建VPC实例时，请确保在企业版转发路由器支持的可用区中创建至少一个交换机实例，以便将VPC实例连接至企业版转发路由器。更多信息，请参见[企业版转发路由器支持的地域和可用区](../../../../cen/documents/product-overview/how-transit-routers-work.md)。
一张云企业网中，一个地域只能有一个VPC内的一个或多个ALB实现跨地域挂载服务器。
无法实现同一个地域多个VPC内的ALB使用同一个转发路由器访问后端服务。
无法实现同一个地域多个VPC内的ALB使用多个转发路由器访问同一个后端服务。
ALB与后端服务器的流量仅支持通过系统路由表转发，暂不支持通过VPC自定义路由表转发。
步骤五：配置路由和安全组
为VPC1的系统路由表添加路由条目。
检查VPC1中的系统路由表是否已经有目标网段的路由指向转发路由器VPC1连接，如果没有，则执行如下步骤添加路由条目。
说明
ALB与后端服务的流量仅
