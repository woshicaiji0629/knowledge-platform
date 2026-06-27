# 使用ALB挂载跨地域VPC内的服务器-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/use-cases/specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region

# 使用ALB挂载跨地域VPC内的服务器
应用型负载均衡 ALB（Application Load Balancer）支持跨地域挂载功能。本文指导您如何使用ALB挂载跨地域VPC内的服务器，实现高效的流量分配和系统优化。
## 场景示例
某电子商务企业主要依托线上平台进行产品销售与推广。通常情况下，该企业在西南1（成都）部署的服务器足以满足日常业务需求。然而，面对重大促销活动期间流量的大幅增长，高并发请求可能会超出西南1（成都）服务器的承载能力。
为解决这一问题，企业可以结合使用ALB IP类型服务器组和云企业网CEN（Cloud Enterprise Network）转发路由器产品，将华东1（杭州）地域的服务器整合到现有网络架构中，以实现资源的快速扩展。跨地域VPC可以通过转发路由器快速实现私网互通，在私网互通的基础上，通过添加ALB IP类型服务器组挂载跨地域的服务器，使ALB将客户端请求同时转发至西南1（成都）和华东1（杭州）的服务器中，提升系统的负载能力和响应速度。
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
如果使用企业版转发路由器，请注意：企业版转发路由器会在用户指定的可用区的交换机实例上创建弹性网卡ENI（Elastic Network Interface），作为VPC实例向企业版转发路由器发送流量的入口。创建VPC实例时，请确保在指定的可用区中创建至少一个交换机实例，以便将VPC实例连接至企业版转发路由器。详情请参见[转发路由器工作原理](../../../../cen/documents/product-overview/how-transit-routers-work.md)。
ALB与后端服务器的流量仅支持通过系统路由表转发，暂不支持通过VPC自定义路由表转发。
## 前提条件
已在西南1（成都）地域创建了[专有网络](../../../../vpc/documents/user-guide/create-and-manage-a-vpc.md)VPC1，在华东1（杭州）地域创建了专有网络VPC2。
VPC1中在可用区A和可用区B下分别部署了交换机VSW1和VSW2。
VPC2中在可用区H和可用区I下分别部署了交换机VSW3和VSW4。
下表为本文的网段规划。如果您需要自行规划网段，请确保要互通的网段之间没有重叠。
单击查看VPC网段。
| 地域 | VPC | 交换机 | 交换机可用区 | 网段规划 |
| --- | --- | --- | --- | --- |
| 西南 1（成都） | VPC1 主网段：172.16.0.0/12 | VSW1 | 可用区 A | 172.16.1.0/24 |
| VSW2 | 可用区 B | 172.16.2.0/24 |  |  |
| 华东 1（杭州） | VPC2 主网段：192.168.0.0/16 | VSW3 | 可用区 H | 192.168.1.0/24 |
| VSW4 | 可用区 I | 192.168.2.0/24 |  |  |
已在VSW1中创建ECS01，在VSW3中创建ECS02，且ECS01和ECS02中均部署了应用服务。
单击查看ECS中测试服务部署命令示例。
ECS01部署命令示例
yum install -y nginx systemctl start nginx.service cd /usr/share/nginx/html/ echo "Hello World ! This is chengdu ECS01." > index.html
ECS02部署命令示例
yum install -y nginx systemctl start nginx.service cd /usr/share/nginx/html/ echo "Hello World ! This is hangzhou ECS02." > index.html
已在VPC1中创建了一个公网[ALB](../user-guide/create-and-manage-alb-instances.md)[实例](../user-guide/create-and-manage-alb-instances.md)。
已[注册域名](https://help.aliyun.com/zh/dws/user-guide/how-to-register-a-domain-name)并完成[备案](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)，且通过自有域名[为](../user-guide/configure-cname-resolution-for-alb.md)[ALB](../user-guide/configure-cname-resolution-for-alb.md)[配置](../user-guide/configure-cname-resolution-for-alb.md)[CNAME](../user-guide/configure-cname-resolution-for-alb.md)[解析](../user-guide/configure-cname-resolution-for-alb.md)。
已创建[云企业网实例](../../../../cen/documents/user-guide/cen-instances-1.md)，并在云企业网实例下的西南1（成都）地域和华东1（杭州）地域分别创建了[转发路由器实例](../../../../cen/documents/user-guide/transit-routers.md)。
## 操作步骤
### 步骤一：创建ALB服务器组
创建IP类型的服务器组，挂载ECS01和跨地域VPC内的ECS02。
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择ALB所属的地域。本文选择西南1（成都）。
在左侧导航栏，选择应用型负载均衡ALB>服务器组。
在服务器组页面，单击创建服务器组，完成以下配置，然后单击创建。
此处仅列出和本文强相关的配置项，其余参数的配置可保持默认值。更多信息，请参见[NLB](../../network-load-balancer/user-guide/create-and-manage-a-server-group.md)[服务器组](../../network-load-balancer/user-guide/create-and-manage-a-server-group.md)。
| 配置 | 说明 |
| --- | --- |
| 服务器组类型 | 需选择 IP 类型 ，后续可通过添加 IP 地址挂载非 VPC 网段内的服务器。 |
| VPC | 选择 VPC1。 |
| 选择后端协议 | 选择 HTTP 。 说明 基础版 ALB 实例的 HTTPS 监听只能选择后端协议是 HTTP 的服务器组。 |
| 选择调度算法 | 使用默认值 加权轮询 ，更多调度算法参考 [负载均衡调度算法介绍](../../product-overview/introduction-to-load-balancing-scheduling-algorithm.md) 。 |
在服务器组创建成功对话框，单击添加后端服务器。
在添加后端服务器面板，添加ECS01的私网IP地址，单击下一步，设置添加的IP地址的端口和权重，然后单击确定。
端口设置需要与后端服务的端口保持一致。本文端口输入80，权重使用默认值。
单击添加IP，添加ECS02的私网IP地址，ECS02的IP地址不在服务器组关联的VPC网段内，需打开远端IP，然后单击下一步，设置添加的IP地址的端口和权重，然后单击确定。本文端口输入80，权重使用默认值。
未开启远端IP时，仅支持输入当前服务器组所在VPC网段内的IP地址。开启远端IP后，支持输入以下网段内的IP地址。
10.0.0.0/8
100.64.0.0/10
172.16.0.0/12
192.168.0.0/16
### 步骤二：为ALB实例配置监听
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择ALB所属的地域。本文选择西南1（成都）。
在实例页面，找到在VPC1中创建的ALB实例，在操作列单击创建监听。
在负载均衡业务配置向导>配置监听页面，完成以下参数配置，其余参数可保持默认值，然后单击下一步。
| 监听配置 | 说明 |
| --- | --- |
| 选择监听协议 | 选择监听 HTTP 协议。 |
| 监听端口 | 输入用来接收请求并向后端服务器进行请求转发的监听端口，端口范围为 1~65535。本文输入 80 。 |
在选择服务器组的下拉框选择IP类型，并选择在步骤一中创建的服务器组，然后单击下一步。
在配置审核配置向导，确认配置信息，单击提交。
### 步骤三：TR连接VPC实例
将VPC1连接至西南1（成都）地域转发路由器，VPC2连接至华东1（杭州）地域转发路由器，通过转发路由器实现VPC1和VPC2跨地域私网互通，确保ALB可以通过转发路由器将客户端请求转发至跨地域VPC内的服务器。
登录[云企业网管理控制台](https://cen.console.aliyun.com/)。
在云企业网实例页面，单击已创建的云企业网实例ID。
在基本信息>转发路由器页签，找到西南1（成都）地域的转发路由器实例，在操作列单击创建网络实例连接。
在连接网络实例页面，配置以下信息，然后单击确定创建，将VPC1连接至西南1（成都）地域转发路由器。
此处仅列出和本文强相关的配置项，其余配置项可保持默认值。更多信息，请参见[使用企业版转发路由器创建](../../../../cen/documents/user-guide/connect-vpcs.md)[VPC](../../../../cen/documents/user-guide/connect-vpcs.md)[连接](../../../../cen/documents/user-guide/connect-vpcs.md)。
| 参数 | 说明 |
| --- | --- |
| 实例类型 | 本文选择 专有网络（VPC） 。 |
| 地域 | 选择要连接的网络实例所在的地域。本文选择 西南 1（成都） 。 |
| 网络实例 | 选择要连接的 VPC 网络实例 ID。本文选择 VPC1。 |
| 交换机 | 从企业版转发路由器支持的可用区中选择交换机实例。本文选择 VSW1 和 VSW2。 |
单击继续创建连接，根据以下信息，将VPC2连接至华东1（杭州）地域转发路由器。
| 参数 | 说明 |
| --- | --- |
| 实例类型 | 选择 专有网络（VPC） 。 |
| 地域 | 选择 华东 1（杭州） 。 |
| 网络实例 | 选择 VPC2。 |
| 交换机 | 选择 VSW3 和 VSW4。 |
### 步骤四：在TR之间创建跨地域连接
转发路由器连接VPC后，需要在不同地域的转发路由器之间创建跨地域连接，才能实现VPC1和VPC2的跨地域私网互通。
登录[云企业网管理控制台](https://cen.console.aliyun.com/)。
在云企业网实例页面，单击已创建的云企业网实例ID。
在基本信息>转发路由器页签，找到西南1（成都）地域的转发路由器实例，在操作列单击创建网络实例连接。
在连接网络实例页面，配置以下信息，然后单击确定创建。
此处仅列出和本文强相关的配置项，其余配置项可保持默认值。更多信息，请参见[使用企业版转发路由器创建跨地域连接](../../../../cen/documents/user-guide/manage-inter-region-connections.md)。
| 配置项 | 说明 |
| --- | --- |
| 实例类型 | 选择 跨地域连接 。 |
| 地域 | 选择要互通的地域。本文选择 西南 1（成都） 。 |
| 对端地域 | 选择要互通的对端地域。本文选择 华东 1（杭州） 。 |
| 带宽分配方式 | 选择 按流量付费 。 针对转发路由器间的跨地域流量，您可使用云数据传输 CDT 降低流量成本，如您未开通该服务建议您查看 [升级至](https://help.aliyun.com/zh/cdt/user-guide/upgrade-to-cdt-billing) [CDT](https://help.aliyun.com/zh/cdt/user-guide/upgrade-to-cdt-billing) [计费](https://help.aliyun.com/zh/cdt/user-guide/upgrade-to-cdt-billing) 开通，仅开通 CDT 不收取任何费用。您也可以根据实际业务情况选择使用带宽包。 |
### 步骤五：结果验证
完成上述配置后，ALB可以成功将客户端请求转发至ECS01和ECS02。
连通性测试
在浏览器中输入域名，例如http://<域名>。多次刷新页面，您可以观察到客户端能正常接收到响应，并且响应的服务器在ECS01和ECS02之间转换。
故障测试
停用ECS01服务，在ECS01中执行systemctl stop nginx.service命令停用应用。
在浏览器中输入域名，例如http://<域名>，客户端发出请求后仍能正常接收到响应，说明已实现跨地域VPC内服务器的负载均衡。
## 常见问题
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
ALB与后端服务的流量仅支持通过系统路由表转发，暂不支持通过VPC自定义路由表转发。
登录[专有网络管理控制台](https://vpcnext.console.aliyun.com/vpc)。
在专有网络页面，单击VPC1的实例ID。
在VPC1详情页面，单击资源管理页签，在路由表下方单击数字链接。
在路由表页面，找到VPC1的系统路由表，并单击路由表ID。
在路由表详情页面，选择路由条目列表>自定义路由条目页签，然后单击添加路由条目。
在添加路由条目面板，配置以下参数，然后单击确定。
| 参数 | 说明 |
| --- | --- |
| 目标网段 | 输入要转发到的目标网段。本文输入 VPC2 所在的网段： 192.168.0.0/16 。 |
| 下一跳类型 | 选择下一跳的类型。本文选择 转发路由器 。 |
| 转发路由器 | 选择具体的转发路由器实例。本文选择 [步骤三](specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region.md) 中的 VPC1 连接。 |
配置回源路由。
查看回源路由。
执行以下步骤，获取ALB实例的回源路由。
登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择实例的所属地域。本文选择西南1（成都）。
在实例页面，单击目标ALB实例ID。
单击实例详情页签，然后在回源路由右侧单击查看。
为VPC2内的系统路由表添加ALB的回源路由。
登录[专有网络管理控制台](https://vpcnext.console.aliyun.com/vpc)。
在专有网络页面，单击VPC2的实例ID。
在VPC详情页面，单击资源管理页签，在路由表下方单击数字链接。
在路由表页面，找到VPC2的系统路由表，并单击路由表ID。
在路由表详情页面，选择路由条目列表>自定义路由条目页签，然后单击添加路由条目。
在添加路由条目面板，配置以下参数，然后单击确定。
| 参数 | 说明 |
| --- | --- |
| 目标网段 | 输入要转发到的目标网段。本文输入 ALB 实例的回源路由。如果回源路由有多条，请重复配置操作， 直到所有回源路由全部配置完。 |
| 下一跳类型 | 选择下一跳的类型。本文选择 转发路由器 。 |
| 转发路由器 | 选择具体的转发路由器实例。本文选择 VPC2 关联的转发路由器。 |
为VPC1关联的转发路由器添加ALB的回源路由。
登录[云企业网管理控制台](https://cen.console.aliyun.com/)。
在云企业网实例页面，单击已创建的云企业网实例ID。
在基本信息>转发路由器页签，找到连接VPC1的转发路由器实例，并单击该目标转发路由器实例ID。
单击转发路由器路由表页签，在页签左侧区域，单击目标路由表ID，在路由表详情页面的路由条目页签下，单击创建路由条目。
在添加路由条目对话框，配置路由条目信息，然后单击确定。
| 配置项 | 说明 |
| --- | --- |
| 路由表 | 系统默认选择当前路由表。 |
| 所属转发路由器 | 系统默认选择当前转发路由器实例。 |
| 目的地址 CIDR | 路由条目的目标网段。本文输入 ALB 实例的回源路由。如果回源路由有多条，请重复配置操作， 直到所有回源路由全部配置完。 |
| 是否为黑洞路由 | 选择 否 。 |
| 下一跳连接 | 选择路由的下一跳连接。本文选择 VPC1 连接。 |
检查后端ECS的防火墙设置。
跨地域访问的报文会以ALB所在 VPC 网段内的 IP 地址作为源地址访问后端服务，请确保后端 ECS 的 iptables 或其他第三方安全软件未屏蔽该网段（本文示例为 172.16.0.0/12），否则将导致跨域访问后端服务失败。
### 同地域的2个VPC创建对等连接后，ALB是否可以挂载这2个VPC内的服务器？
可以。
### ALB通过云企业网CEN实现挂载跨地域VPC内服务器怎么收费？
除了收取[ALB](../product-overview/billing-overview.md)[费用](../product-overview/billing-overview.md)外还会额外产生CEN计费项，具体可参考[云企业网计费说明](../../../../cen/documents/product-overview/billing-rules.md)。
## 相关文档
如果您需要使用ALB挂载同地域IDC内的服务器，请参见[使用](specify-an-on-premises-server-as-a-backend-server-of-alb.md)[ALB](specify-an-on-premises-server-as-a-backend-server-of-alb.md)[挂载同地域](specify-an-on-premises-server-as-a-backend-server-of-alb.md)[IDC](specify-an-on-premises-server-as-a-backend-server-of-alb.md)[服务器](specify-an-on-premises-server-as-a-backend-server-of-alb.md)。
如果您需要使用NLB挂载同地域IDC内服务器或者跨地域VPC内服务器，请参见[使用](../../network-load-balancer/use-cases/add-servers-in-data-centers-to-an-nlb-instance.md)[NLB](../../network-load-balancer/use-cases/add-servers-in-data-centers-to-an-nlb-instance.md)[挂载同地域](../../network-load-balancer/use-cases/add-servers-in-data-centers-to-an-nlb-instance.md)[IDC](../../network-load-balancer/use-cases/add-servers-in-data-centers-to-an-nlb-instance.md)[服务器](../../network-load-balancer/use-cases/add-servers-in-data-centers-to-an-nlb-instance.md)或[使用](../../network-load-balancer/use-cases/use-nlb-and-cen-to-distribute-traffic-across-regions.md)[NLB](../../network-load-balancer/use-cases/use-nlb-and-cen-to-distribute-traffic-across-regions.md)[挂载跨地域](../../network-load-balancer/use-cases/use-nlb-and-cen-to-distribute-traffic-across-regions.md)[VPC](../../network-load-balancer/use-cases/use-nlb-and-cen-to-distribute-traffic-across-regions.md)[内的服务器](../../network-load-balancer/use-cases/use-nlb-and-cen-to-distribute-traffic-across-regions.md)。
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
