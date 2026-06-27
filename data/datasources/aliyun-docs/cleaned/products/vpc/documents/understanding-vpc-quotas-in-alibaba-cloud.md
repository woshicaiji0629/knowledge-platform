# 限制与配额-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/understanding-vpc-quotas-in-alibaba-cloud

# 限制与配额
服务配额是指一个阿里云账号（主账号）可以使用的云资源的最大值或操作次数的最大值。本文介绍专有网络 VPC（Virtual Private Cloud）资源配额的名称、默认值、是否支持调整，以及VPC相关限制等信息。
阿里云服务配额一般基于账号或地域限定，按照限制的维度可以分为以下类型：
通用配额：指一个阿里云账号可使用的云资源的最大值。
API速率配额：指允许一个阿里云账号调用云服务API频率，即QPS限制。
权益配额：指一个阿里云账号通过阿里云授权后获得的权益，如使用特定功能的权益。
您可以通过登录阿里云[配额中心控制台](https://quotas.console.aliyun.com/products)或者登录[专有网络控制台](https://vpcnext.console.aliyun.com/quota)等途径查看配额或申请提升配额。关于VPC配额管理的操作指引，请参见[管理](manage-vpc-quotas.md)[VPC](manage-vpc-quotas.md)[配额](manage-vpc-quotas.md)。
通用配额调整后，对新创建资源和存量资源均生效。
## 通用配额
下表中分别列举了专有网络VPC的通用配额。
### VPC和交换机使用限制与配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_instances_num vpc_quota_instances_num_${RegionId}优先级高于 vpc_quota_instances_num | 单个地域支持创建的 VPC 的数量 | 10 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_instances_num_${RegionId} ${RegionId}为地域的变量，表示不同地域的配额名称不同。 | 指定地域支持创建的 VPC 的数量 | 10 个 |  |
| vpc_quota_vswitches_num | 单个 VPC 支持创建的交换机的数量 | 150 个 |  |
| vpc_quota_secondary_cidr_num | 单个 VPC 支持创建的附加 IPv4 网段的数量 | 5 个 |  |
| 无 | 单个 VPC 支持创建的附加 IPv6 网段的数量 | 5 个 | 无法提升 |
| 单个 VPC 支持创建的 IPv4 预留网段的数量 | 100 个 |  |  |
| 单个 VPC 支持创建的 IPv6 预留网段的数量 | 100 个 |  |  |
| 单个 VPC 支持创建的用户网段的数量 | 3 个 |  |  |
| 单个 VPC 支持云资源使用的私网网络地址数量 | 300,000 个 1、如果 ECS 实例仅有一个私网 IP，则该 ECS 实例仅使用一个网络地址。 2、如果 ECS 实例绑定了多个网卡或网卡配置了多个 IP，则该 ECS 实例使用的网络地址数为与 ECS 实例绑定的网卡上分配的 IP 地址数量之和。 |  |  |
| 单个 VPC 支持绑定的标签数量 | 20 个 |  |  |
| 单个交换机支持绑定的标签数量 | 20 个 |  |  |
### 路由器和路由表使用限制与配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_route_tables_num | 单个 VPC 支持创建的自定义路由表的数量 | 9 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_route_entrys_num | 单个路由表支持创建的自定义路由条目的数量（不包括 [动态传播路由条目](vpc-route-table.md) ） | 200 条 |  |
| vpc_quota_dynamic_route_entrys_num | 单个路由表来自动态传播的路由条目数量 | 200 条 |  |
| vpc_quota_havip_custom_route_entry | 指向一个 HaVip 实例的自定义路由上限 | 5 个 |  |
| vpc_quota_vpn_custom_route_entry | 单个 VPC 内指向 VPN 的自定义路由上限 | 50 个 |  |
| 无 | 单个路由表支持绑定的标签数量 | 20 个 | 无法提升 |
| 单个 VPC 支持创建的路由器的数量 | 1 个 |  |  |
| 单个 VPC 支持指向转发路由器 TR 连接的最大路由条目数量 | 600 条 |  |  |
### DHCP选项集使用限制与配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| 无 | 单个账号支持创建的 DHCP 选项集的数量 | 10 个 | 无法提升 |
| 单个 DHCP 选项集支持关联的 VPC 的数量 | 10 个 |  |  |
| 单个 VPC 支持关联的 DHCP 选项集的数量 | 1 个 |  |  |
| 单个 DHCP 选项集支持配置的域名的数量 | 1 个 |  |  |
| 单个 DHCP 选项集支持配置的 DNS 服务器 IP 地址的数量 | 4 个 |  |  |
### 共享VPC使用限制与配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_sharedvpc_share_user_num_per_vpc | 单个 VPC 支持共享的交换机使用者的数量 | 50 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_sharedvpc_share_user_num_per_vswitch | 单个 VPC 内的单个交换机支持共享的交换机使用者的数量 | 50 个 |  |
| vpc_quota_sharedvpc_accept_shared_vswitch_num | 单个交换机使用者支持接收的共享交换机的数量 | 30 个 |  |
### 流日志使用限制与配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_flowlog_inst_nums_per_user | 用户支持创建的流日志实例的数量 | 10 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
### 网络ACL使用限制与配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_nacl_ingress_entry | 单个网络 ACL 支持创建的入方向规则数量 网络 ACL 所属 VPC 开启了 IPv6 时，支持创建的 IPv4/IPv6 入方向规则，默认均为 20 条。 | 20 条 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_nacl_egress_entry | 单个网络 ACL 支持创建的出方向规则数量 网络 ACL 所属 VPC 开启了 IPv6 时，支持创建的 IPv4/IPv6 入方向规则，默认均为 20 条。 | 20 条 |  |
| nacl_quota_vpc_create_count | 单个 VPC 支持创建的网络 ACL 数量 | 20 个 |  |
### 高可用虚拟IP使用限制与配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| 无 | 支持创建高可用虚拟 IP（HaVip）的网络类型 | VPC 类型 | 无法提升 |
| 单个 ECS 实例支持同时绑定的 HaVip 数量 | 5 个 |  |  |
| 单个 HaVip 支持同时绑定的 EIP 数量 | 1 个 |  |  |
| 单个 HaVip 支持同时绑定的 ECS 实例或弹性网卡的数量 | 10 个 1、1 个 HaVip 支持同时绑定 10 个 ECS 实例或同时绑定 10 个弹性网卡，但 1 个 HaVip 不能同时绑定 ECS 实例和弹性网卡。 2、HaVip 具有子网属性，仅支持绑定到同一交换机下的 ECS 实例或弹性网卡上。 |  |  |
| HaVip 是否支持广播和组播通信 | 不支持 HaVip 只支持单播，如果您使用 Keepalived 等第三方软件实现高可用，需要修改配置文件中的通信方式为单播通信。 |  |  |
| 单个账号支持创建的 HaVip 的数量 | 50 个 |  |  |
| 单个 VPC 支持创建的 HaVip 的数量 | 50 个 |  |  |
| vpc_quota_havip_custom_route_entry | 单个路由表内，目的地址指向 HaVip 的路由条目的数量 | 5 条 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
### 流量镜像使用限制与配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| trafficmirror_quota_source_num_per_session | 单个镜像会话支持加入的镜像源个数 | 10 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_traffic_mirror_source_num_per_large_ecs_target | 镜像目的为弹性网卡，且弹性网卡绑定的是以下规格的 ECS 实例时，单个镜像目的支持的镜像源个数 ECS 实例规格 ecs.ebmc7.32xlarge、ecs.ebmg7.32xlarge、ecs.ebmr7.32xlarge、ecs.ebmhfg7.48xlarge、ecs.ebmhfc7.48xlarge、ecs.ebmhfr7.48xlarge、ecs.ebmc7a.64xlarge、ecs.ebmg7a.64xlarge、ecs.ebmg7se.32xlarge、ecs.ebmg6a.64xlarge、ecs.ebmg6e.26xlarge、ecs.ebmc6a.64xlarge、ecs.ebmc6e.26xlarge、ecs.ebmr7a.64xlarge、ecs.ebmr6a.64xlarge、ecs.ebmr6e.26xlarge、ecs.c8i.48xlarge、ecs.g8i.48xlarge、ecs.c7nex.32xlarge、ecs.g7nex.32xlarge、 ecs.g7ne.24xlarge、ecs.c7.32xlarge、ecs.g7.32xlarge、ecs.r7.32xlarge、ecs.r6e.26xlarge、 ecs.g7t.32xlarge、ecs.g6t.26xlarge、ecs.g6e.26xlarge、ecs.c7t.32xlarge、ecs.c6t.26xlarge、ecs.c6e.26xlarge、ecs.g5ne.18xlarge、ecs.r7t.32xlarge | 200 个 |  |
| vpc_quota_traffic_mirror_source_num_per_small_ecs_target | 镜像目的为弹性网卡，且弹性网卡绑定的不是以下规格的 ECS 实例，单个镜像目的支持的镜像源个数 ECS 实例规格 ecs.ebmc7.32xlarge、ecs.ebmg7.32xlarge、ecs.ebmr7.32xlarge、ecs.ebmhfg7.48xlarge、ecs.ebmhfc7.48xlarge、ecs.ebmhfr7.48xlarge、ecs.ebmc7a.64xlarge、ecs.ebmg7a.64xlarge、ecs.ebmg7se.32xlarge、ecs.ebmg6a.64xlarge、ecs.ebmg6e.26xlarge、ecs.ebmc6a.64xlarge、ecs.ebmc6e.26xlarge、ecs.ebmr7a.64xlarge、ecs.ebmr6a.64xlarge、ecs.ebmr6e.26xlarge、ecs.c8i.48xlarge、ecs.g8i.48xlarge、ecs.c7nex.32xlarge、ecs.g7nex.32xlarge、 ecs.g7ne.24xlarge、ecs.c7.32xlarge、ecs.g7.32xlarge、ecs.r7.32xlarge、ecs.r6e.26xlarge、 ecs.g7t.32xlarge、ecs.g6t.26xlarge、ecs.g6e.26xlarge、ecs.c7t.32xlarge、ecs.c6t.26xlarge、ecs.c6e.26xlarge、ecs.g5ne.18xlarge、ecs.r7t.32xlarge | 20 个 |  |
| vpc_quota_traffic_mirror_rules_num_per_filter | 单个筛选条件支持的筛选规则数 | 20 个 |  |
| 无 | 单账号单地域支持的最大镜像会话数 | 20000 个 | 无法提升 |
| 单个镜像源支持创建的最大镜像会话数 | 3 个 |  |  |
| 镜像目的为私网传统型负载均衡 CLB 时，单个镜像目的支持的镜像源个数 | 500 个 |  |  |
| 镜像目的为网关型负载均衡终端节点 GWLBe 时，单个镜像目的支持的镜像源个数 | 500 个 |  |  |
| 单账号单地域支持的最大筛选条件数 | 100 个 |  |  |
| 单个筛选条件支持关联的镜像会话数 | 2000 个 |  |  |
### VPC对等连接使用限制与配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_cross_region_peer_num_per_vpc | 单个 VPC 支持的跨地域 VPC 对等连接数量 | 20 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_intra_region_peer_num_per_vpc | 单个 VPC 支持的同地域 VPC 对等连接数量 | 10 个 |  |
| vpc_quota_peer_num | 单个阿里云账号单地域支持的 VPC 对等连接数量 | 20 个 |  |
| vpc_quota_peer_cross_border_bandwidth | 跨境带宽允许的最大值 | 1024 Mbps |  |
| vpc_quota_peer_cross_region_bandwidth | 跨地域带宽允许的最大值 | 1024 Mbps |  |
### IPv4网关使用限制与配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| 无 | 单个 VPC 支持的 IPv4 网关个数 | 1 个 | 无法提升 |
| 单个 IPv4 网关支持的网关路由表个数 | 1 个 |  |  |
### 前缀列表使用限制与配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_prefixlist_num | 单个阿里云账号支持创建的前缀列表个数 | 10 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_prefixlist_cidr_num_per_prefixlist | 单个前缀列表支持的 CIDR 条目数 | 50 条 |  |
| vpc_quota_prefixlist_accept_shared_prefixlist_num | 单个资源使用者支持接受的共享前缀列表个数 | 100 个 |  |
| vpc_quota_prefixlist_share_user_num_per_prefixlist | 单个前缀列表支持共享给资源使用者的个数 | 10 个 |  |
### IP地址管理（IPAM）使用限制与配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| ipam_quota_per_region | 每个用户在每个地域支持创建的 IPAM 数量 | 1 个 | 无法提升 |
| ipam_scope_quota_per_ipam | 每个 IPAM 支持创建的 IPAM 作用范围数量 | 5 个 |  |
| ipam_pool_quota_depth | 每个地址池最大深度 | 10 |  |
| ipam_cidr_quota_per_ipam_pool | 每个地址池中允许预置的 CIDR 的数量 | 50 个 |  |
| ipam_sub_pool_quota_per_ipam_pool | 每个地址池允许创建的子地址池的数量 | 50 个 |  |
| ipam_pool_quota_per_scope | 每个 IPAM 私有范围支持创建的地址池的数量 | 500 个 |  |
| custom_ipam_resource_discovery_quota_per_region | 单地域单账号允许创建的自定义资源发现数量 | 1 个 |  |
| resource_share_quota_per_ipam_resource_discovery | 每个资源发现支持创建的共享资源数量 | 100 个 |  |
| shared_ipam_resource_discovery_quota_per_user | 每个用户允许拥有的共享资源发现的数量 | 100 个 |  |
| resource_share_quota_per_ipam_pool | 每个 IPAM 地址池允许创建的共享资源数量 | 100 个 |  |
| shared_ipam_pool_quota_per_user | 每个用户允许拥有的共享地址池的数量 | 100 个 |  |
| ipam_public_ipv6_top_pool_quota_per_region_isp | 每个用户在每个地域支持创建的每种 ISP 类型的公网 IPv6 IPAM 顶级地址池数量 | 1 个 |  |
| ipam_cidr_quota_per_public_ipv6_top_pool | 每个用户在每个地域支持为公网 IPv6 IPAM 顶级地址池预置的 CIDR 数量 | 1 个 |  |
## API速率配额
| 限制项 | 限制 | 提升配额 |
| --- | --- | --- |
| API 速率配额 | 任选以下方式查看 API 速率配额限制： 在 [配额中心](https://quotas.console.aliyun.com/flow-control-products/vpc/quotas) 的 API 速率配额列表 页面，查看专有网络 VPC API 接口的速率配额。 在 [配额管理页面](https://vpc.console.aliyun.com/quota) 的配额类型区域，单击 API 速率配额页签查看专有网络 VPC API 接口的速率配额。 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/flow-control-products/vpc/quotas?regionId=cn-hangzhou) 申请提升配额。 |
## 权益配额
专有网络VPC的权益配额项默认值为0，表示默认不可用，通过阿里云授权后方可获得使用权益。下表列举了专有网络VPC的权益配额。
| 配额名称 | 描述 | 提升配额 |
| --- | --- | --- |
| havip 特权白名单 | 用于一个新上线的功能（HaVip）内测邀请客户使用阶段的开通白名单控制 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/white-list-products/vpc/quotas) 申请提升配额。 |
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
