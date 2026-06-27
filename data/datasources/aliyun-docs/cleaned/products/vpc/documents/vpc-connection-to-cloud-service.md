# VPC私网访问云服务-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/vpc-connection-to-cloud-service

# VPC私网访问云服务
VPC内的实例访问云服务时（例如访问对象存储OSS），如果通过公网访问，可能会存在数据安全风险、公网网络质量不稳定等问题，同时公网访问也会产生公网流量成本。
为了解决这些问题，阿里云提供了VPC内通过私网访问云服务的能力，确保访问请求保留在阿里云的内网中，从而获得更高的安全性、更稳定的网络性能和更优的成本控制。
本文将介绍两种主流的VPC私网访问方案：网关终端节点和私网连接（PrivateLink）。
## 工作原理
| 网关终端节点 | 私网连接（PrivateLink） |
| --- | --- |
| 网关终端节点可以理解为 VPC 在访问特定云服务时的一个“虚拟网关”。 以 OSS 为例，工作过程如下： 创建网关终端节点时，需要选择 VPC、路由表、要访问的云服务。 网关终端节点完成创建后，系统会自动在选中的路由表里，增加一个自定义路由条目：目标网段为一个系统前缀列表（里面包含 [OSS 在该地域的 VIP 网段](../../oss/documents/user-guide/regions-and-endpoints.md) ），下一跳为创建的网关终端节点。 路由表所绑定的交换机内的 ECS 实例，在访问 OSS 内网域名时，VPC 会将访问请求路由到网关终端节点，并通过阿里云内网直接到达 OSS，无需绕行公网。 | 私网连接（PrivateLink）像是在 VPC 和目标服务之间建立了一条“私密隧道”。 以 OSS 为例，工作过程如下： 使用 PrivateLink 需要先创建接口终端节点。创建接口终端节点时，需要选择 VPC、安全组、可用区与交换机、要访问的云服务。 接口终端节点完成创建后，系统会自动在每个选中的交换机里创建一个拥有私网 IP 的终端节点弹性网卡（ENI），作为访问服务的唯一入口。 ECS 实例在访问终端节点域名时，如果符合安全组规则，所有访问请求都将经过终端节点弹性网卡，并通过阿里云内网直接到达 OSS，无需绕行公网。 |
|  |  |
为了让您更直观地选择，下表总结了两种方案的主要区别：
| 特性 | 网关终端节点 | 私网连接 (PrivateLink) |
| --- | --- | --- |
| 应用场景 | 结合网关终端节点的终端节点策略与 OSS 的 Bucket 授权策略，可以降低未授权访问风险，实现双向鉴权： 源端控制：VPC 侧仅允许该 VPC 访问指定 Bucket，不允许该 VPC 访问其他 Bucket。 目的端控制：OSS 侧仅允许指定 VPC 访问该 Bucket，不允许其他 VPC 访问。 | VPC 通过私网安全访问云服务的标准方案，相比网关终端节点支持更多云服务类型、更多高级能力。 |
| 适用服务类型 | 目前仅适用于对象存储 OSS。 | 适用于 [众多阿里云一方服务](https://help.aliyun.com/zh/privatelink/aliyun-services-that-integrate-with-privatelink#e6d966791d7gc) 以及用户自建服务（含 ISV 提供的服务）。 |
| VPC 侧安全能力 | 仅支持终端节点策略。 | 支持安全组、网络 ACL、终端节点策略。 |
| 组网能力 | 不支持复杂组网。可能存在云服务地址（100.x.x.x 网段）冲突的问题。 | 支持复杂组网。结合 VPC 对等连接/云企业网、高速通道/VPN 网关产品，可以实现跨地域、混合云组网。 |
| 运维能力 | 无 | 支持流日志，便于审计与故障排查。 |
| 费用 | 免费 | 收取实例费、流量处理费。 用户自建服务支持选择服务使用方付费或服务提供方付费。 |
## 网关终端节点
结合网关终端节点的终端节点策略与OSS的Bucket授权策略，可以降低未授权访问风险，实现双向鉴权：
源端控制：VPC侧仅允许该VPC访问指定Bucket，不允许该VPC访问其他Bucket。
目的端控制：OSS侧仅允许指定VPC访问该Bucket，不允许其他VPC访问。
### 控制台
创建网关终端节点并配置授权策略
开启网关终端节点的VPC、授权Bucket、在VPC内访问OSS的用户，可以分别归属于不同的阿里云账号。
注意网关终端节点[仅在部分地域支持](vpc-connection-to-cloud-service.md)。
创建网关终端节点并配置终端节点策略。
前往[专有网络控制台-网关终端节点](https://vpc.console.aliyun.com/endpoint/cn-hangzhou/vpcEndpoints)页面，单击创建终端节点。
选择地域并自定义终端节点名称，终端节点类型保持为网关终端节点。
终端节点服务选中阿里云服务，并选中对象存储OSS的终端节点服务。
选中VPC并勾选路由表。
网关终端节点完成创建后，系统会自动在选中的路由表里，增加一个自定义路由条目：目标网段为一个系统前缀列表（里面包含[OSS 在该地域的 VIP 网段](../../oss/documents/user-guide/regions-and-endpoints.md)），下一跳为创建的网关终端节点。
配置终端节点策略：语法与访问控制RAM产品的[权限策略语言](../../ram/documents/policy-elements.md)相同。
策略示例
下面的示例表示：VPC仅允许账号ID为1746xxxxxx的用户，访问名称为examplebucket的Bucket，进行OSS相关操作。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "oss:*", "Resource": ["acs:oss:*:*:examplebucket", "acs:oss:*:*:examplebucket/*"], "Principal": ["1746xxxxxx"] } ] }
创建完成后，可以在关联路由表的自定义路由条目中，查看到一条系统自动添加的、下一跳指向网关终端节点的路由条目。
配置OSS的bucket授权策略。
前往[OSS](https://oss.console.aliyun.com/bucket)[控制台-Bucket](https://oss.console.aliyun.com/bucket)页面，单击需要配置授权的Bucket名称。
左侧导航选择权限控制 > Bucket授权策略。单击按语法策略添加，单击编辑。
配置Bucket授权策略：语法与访问控制RAM产品的[权限策略语言](../../ram/documents/policy-elements.md)相同。
策略示例
下面的示例表示：
策略1：拒绝所有账号，从除了实例ID为vpc-bp******的VPC外的其他VPC，访问名称为examplebucket的Bucket，进行OSS相关操作。
OSS的Action汇总请参见[RAM Policy](../../oss/documents/ram-policy-overview.md)[概述](../../oss/documents/ram-policy-overview.md)。Deny策略建议尽量避免配置Action为*，以免导致Bucket所有者在OSS控制台也无法访问Bucket。
策略2：仅允许账号ID为1746xxxxxx的用户，从实例ID为vpc-bp******的VPC，访问名称为examplebucket的Bucket，进行OSS相关操作。
{ "Version": "1", "Statement": [ { "Effect": "Deny", "Action": ["oss:ListObjects","oss:GetObject","oss:PutObject","oss:DeleteObject"], "Resource": ["acs:oss:*:*:examplebucket", "acs:oss:*:*:examplebucket/*"], "Principal": ["*"], "Condition": { "StringNotEquals": { "acs:SourceVpc": [ "vpc-bp******" ] } } },{ "Effect": "Allow", "Action": ["oss:*"], "Resource": ["acs:oss:*:*:examplebucket", "acs:oss:*:*:examplebucket/*"], "Principal": ["1746xxxxxx"], "Condition": { "StringEquals": { "acs:SourceVpc": [ "vpc-bp******" ] } } } ] }
策略配置完成后单击保存。
验证访问策略。
注意如果访问OSS的账号是RAM账号，则RAM账号本身需要授予OSS相关Bucket的操作权限，否则可能导致访问失败。
使用授权账号，在授权VPC访问授权Bucket时，访问成功。
若账号、VPC或Bucket任意一个未授权，则访问失败。
修改权限策略
可以通过修改权限策略，调整授权VPC、授权Bucket或授权账号范围。
调整授权VPC：前往[OSS](https://oss.console.aliyun.com/bucket)[控制台-Bucket](https://oss.console.aliyun.com/bucket)页面，单击目标Bucket名称，左侧导航选择权限控制 > Bucket授权策略，调整现有授权策略的Condition字段，增减可访问Bucket的VPC。
调整授权Bucket：
前往[专有网络控制台-网关终端节点](https://vpc.console.aliyun.com/endpoint/cn-hangzhou/vpcEndpoints)页面，单击目标网关终端节点实例ID，选择终端节点策略页签，调整现有授权策略的Resource字段，增减VPC可访问的Bucket。
前往[OSS](https://oss.console.aliyun.com/bucket)[控制台-Bucket](https://oss.console.aliyun.com/bucket)页面，单击目标Bucket名称，左侧导航选择权限控制 > Bucket授权策略，调整现有授权策略的Resource字段，增减可被访问的Bucket资源。如果涉及多个Bucket，在每个Bucket里均需要进行操作。
调整授权账号：
注意如果访问OSS的账号是RAM账号，则RAM账号本身需要授予OSS相关Bucket的操作权限，否则可能导致访问失败。
前往[专有网络控制台-网关终端节点](https://vpc.console.aliyun.com/endpoint/cn-hangzhou/vpcEndpoints)页面，单击目标网关终端节点实例ID，选择终端节点策略页签，调整现有授权策略的Principal字段，增减可在VPC内访问Bucket的账号。
前往[OSS](https://oss.console.aliyun.com/bucket)[控制台-Bucket](https://oss.console.aliyun.com/bucket)页面，单击目标Bucket名称，左侧导航选择权限控制 > Bucket授权策略，调整现有授权策略的Principal字段，增减可在VPC内访问Bucket的账号。如果涉及多个Bucket，在每个Bucket里均需要进行操作。
绑定/解绑路由表
可以通过网关终端节点绑定/解绑路由表，控制VPC内哪些交换机通过网关终端节点访问云服务。
前往[专有网络控制台-网关终端节点](https://vpc.console.aliyun.com/endpoint/cn-hangzhou/vpcEndpoints)页面，单击目标网关终端节点实例ID。
在关联的路由表页签：
绑定新的路由表：单击关联路由表。绑定完成后，可以在关联路由表的自定义路由条目中，查看到一条系统自动添加的、下一跳指向网关终端节点的路由条目。
解绑已有路由表：单击已关联路由表右侧的解除关联。解绑后，系统添加的路由条目将会被自动移除。
删除网关终端节点
删除网关终端节点前，您需要先解绑所有已关联的路由表。
解绑所有已关联的路由表。
前往[专有网络控制台-网关终端节点](https://vpc.console.aliyun.com/endpoint/cn-hangzhou/vpcEndpoints)页面，单击目标网关终端节点实例右侧的删除。
（可选）由于Bucket中仍然存在Bucket授权策略，会限制其他VPC无法访问该Bucket。如需调整，可以前往[OSS](https://oss.console.aliyun.com/bucket)[控制台-Bucket](https://oss.console.aliyun.com/bucket)页面，单击目标Bucket名称，左侧导航选择权限控制 > Bucket授权策略，调整或删除仅允许从指定VPC访问的策略。
### API
网关终端节点：
创建网关终端节点并配置终端节点策略：调用[CreateVpcGatewayEndpoint](developer-reference/api-vpc-2016-04-28-createvpcgatewayendpoint.md)接口。
创建时需要传入终端节点服务名称字段ServiceName，可以通过调用[ListVpcEndpointServicesByEndUser](developer-reference/api-vpc-2016-04-28-listvpcendpointservicesbyenduser.md)接口，查询可使用的终端节点服务。
PolicyDocument字段用于配置终端节点策略，语法与访问控制RAM产品的[权限策略语言](../../ram/documents/policy-elements.md)相同。
修改网关终端节点策略：调用[UpdateVpcGatewayEndpointAttribute](developer-reference/api-vpc-2016-04-28-updatevpcgatewayendpointattribute.md)接口，传入PolicyDocument字段。
绑定路由表：调用[AssociateRouteTablesWithVpcGatewayEndpoint](developer-reference/api-vpc-2016-04-28-associateroutetableswithvpcgatewayendpoint.md)接口。
解绑路由表：调用[DissociateRouteTablesFromVpcGatewayEndpoint](developer-reference/api-vpc-2016-04-28-dissociateroutetablesfromvpcgatewayendpoint.md)接口。
删除网关终端节点：调用[DeleteVpcGatewayEndpoint](developer-reference/api-vpc-2016-04-28-deletevpcgatewayendpoint.md)接口。
OSS Bucket：
配置OSS的bucket授权策略：调用[PutBucketPolicy](../../oss/documents/developer-reference/putbucketpolicy.md)接口。
修改Bucket授权策略：调用[PutBucketPolicy](../../oss/documents/developer-reference/putbucketpolicy.md)接口，传入JSON形式的权限策略。
删除Bucket授权策略：调用[DeleteBucketPolicy](../../oss/documents/developer-reference/deletebucketpolicy.md)接口。
### Terraform
配置网关终端节点：
Resources：[alicloud_vpc_gateway_endpoint](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_gateway_endpoint)注意删除网关终端节点前，您需要先解绑所有已关联的路由表。provider "alicloud" { region = "cn-hangzhou" } resource "alicloud_vpc_gateway_endpoint" "default" { gateway_endpoint_name = "gateway-endpoint-name" # 网关终端节点名称 service_name = "com.aliyun.cn-hangzhou.oss" # OSS服务名称 vpc_id = "vpc-bp******" # 网关终端节点所属VPC route_tables = ["vtb-bp******","vtb-bp******"] # 关联的路由表ID # 终端节点策略 policy_document = <<EOF { "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "oss:*", "Resource": ["acs:oss:*:*:examplebucket","acs:oss:*:*:examplebucket/*"], "Principal": ["1746******"] } ] } EOF }
配置OSS的bucket授权策略：
Resources：[alicloud_oss_bucket_policy](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/oss_bucket_policy)provider "alicloud" { region = "cn-hangzhou" } resource "alicloud_oss_bucket_policy" "default" { bucket = "examplebucket" # Bucket名称 policy = jsonencode({ Version = "1" Statement = [ { Effect = "Deny" Action = [ "oss:ListObjects", "oss:GetObject", "oss:PutObject", "oss:DeleteObject" ] Principal = [ "*" ] Resource = [ "acs:oss:*:*:examplebucket", "acs:oss:*:*:examplebucket/*" ] Condition = { StringNotEquals = { "acs:SourceVpc" = [ "vpc-bp******" # 请替换为实际的VPC ID ] } } },{ Effect = "Allow" Action = [ "oss:*" ] Principal = [ "1746xxxxxx" # 请替换为实际的阿里云账号ID ] Resource = [ "acs:oss:*:*:examplebucket", "acs:oss:*:*:examplebucket/*" ] Condition = { StringEquals = { "acs:SourceVpc" = [ "vpc-bp******" # 请替换为实际的VPC ID ] } } } ] }) }
## 私网连接（PrivateLink）
参考PrivateLink相关文档：
访问阿里云服务：[通过](https://help.aliyun.com/zh/privatelink/getting-started/access-oss-resources-through-the-private-network)[PrivateLink](https://help.aliyun.com/zh/privatelink/getting-started/access-oss-resources-through-the-private-network)[私网访问](https://help.aliyun.com/zh/privatelink/getting-started/access-oss-resources-through-the-private-network)[OSS](https://help.aliyun.com/zh/privatelink/getting-started/access-oss-resources-through-the-private-network)。
访问用户自建服务（含ISV提供的服务）：[通过](https://help.aliyun.com/zh/privatelink/getting-started/use-privatelink-to-access-alb-across-the-private-network-of-a-vpc)[PrivateLink](https://help.aliyun.com/zh/privatelink/getting-started/use-privatelink-to-access-alb-across-the-private-network-of-a-vpc)[跨](https://help.aliyun.com/zh/privatelink/getting-started/use-privatelink-to-access-alb-across-the-private-network-of-a-vpc)[VPC](https://help.aliyun.com/zh/privatelink/getting-started/use-privatelink-to-access-alb-across-the-private-network-of-a-vpc)[私网访问](https://help.aliyun.com/zh/privatelink/getting-started/use-privatelink-to-access-alb-across-the-private-network-of-a-vpc)[ALB](https://help.aliyun.com/zh/privatelink/getting-started/use-privatelink-to-access-alb-across-the-private-network-of-a-vpc)、[通过](https://help.aliyun.com/zh/privatelink/cross-vpc-private-network-access-through-privatelink)[PrivateLink](https://help.aliyun.com/zh/privatelink/cross-vpc-private-network-access-through-privatelink)[跨](https://help.aliyun.com/zh/privatelink/cross-vpc-private-network-access-through-privatelink)[VPC](https://help.aliyun.com/zh/privatelink/cross-vpc-private-network-access-through-privatelink)[私网访问](https://help.aliyun.com/zh/privatelink/cross-vpc-private-network-access-through-privatelink)[NLB](https://help.aliyun.com/zh/privatelink/cross-vpc-private-network-access-through-privatelink)。
访问网络虚拟设备：[通过](../../slb/documents/gateway-based-load-balancing-gwlb/getting-started/gwlb-quickly-implements-load-balancing-for-ipv4-services.md)[GWLB](../../slb/documents/gateway-based-load-balancing-gwlb/getting-started/gwlb-quickly-implements-load-balancing-for-ipv4-services.md)[快速实现](../../slb/documents/gateway-based-load-balancing-gwlb/getting-started/gwlb-quickly-implements-load-balancing-for-ipv4-services.md)[IPv4](../../slb/documents/gateway-based-load-balancing-gwlb/getting-started/gwlb-quickly-implements-load-balancing-for-ipv4-services.md)[流量的安全检测](../../slb/documents/gateway-based-load-balancing-gwlb/getting-started/gwlb-quickly-implements-load-balancing-for-ipv4-services.md)。
## 更多信息
### 计费说明
网关终端节点功能免费。
私网连接（PrivateLink）请参见[私网连接计费说明](https://help.aliyun.com/zh/privatelink/private-link-billing-description)。
### 支持的地域
| 区域 | 网关终端节点支持的地域 |
| --- | --- |
| 亚太-中国 | 华东 1（杭州） 、 华东 2（上海） 、 华北 1（青岛） 、 华北 2（北京） 、 华北 3（张家口） 、 华北 5（呼和浩特） 、 华南 1（深圳） 、 华北 6（乌兰察布） 、 华南 2（河源） 、 华南 3（广州） 、 西南 1（成都） 、 中国香港 |
| 亚太-其他 | 日本（东京） 、 新加坡 、 马来西亚（吉隆坡） 、 印度尼西亚（雅加达） |
| 欧洲与美洲 | 德国（法兰克福） 、 英国（伦敦） 、 美国（硅谷） 、 美国（弗吉尼亚） |
| 中东 | 阿联酋（迪拜） |
私网连接（PrivateLink）请参见[支持私网连接的地域和可用区](https://help.aliyun.com/zh/privatelink/regions-and-zones-that-support-private-network-connections#section-pmn-jzo-kln)。
### 配额
网关终端节点配额：
针对同一种云服务，一个VPC只能绑定一个网关终端节点，一个VPC路由表也只能关联一个网关终端节点。
一个网关终端节点可以关联多个VPC路由表。
私网连接（PrivateLink）请参见[服务配额](https://help.aliyun.com/zh/privatelink/quotas-and-limits#9b59cc3508wxb)。
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
