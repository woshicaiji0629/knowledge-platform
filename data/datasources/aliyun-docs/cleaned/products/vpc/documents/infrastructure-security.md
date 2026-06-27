# VPC网络安全防护体系与功能-专有网络VPC-阿里云

Source: https://help.aliyun.com/zh/vpc/infrastructure-security

# 基础设施安全
本文为您介绍专有网络VPC基础设施安全的相关内容。
## 网络隔离
专有网络VPC是阿里云上用户自己的云上私有网络，是一个隔离的网络环境，专有网络之间逻辑上彻底隔离。
在专有网络VPC中，交换机（vSwitch）是组成专有网络的基础网络设备，用来连接不同的云资源实例。您可以创建多个交换机来划分VPC的网络空间，并可以将不同的ECS实例部署在不同的交换机中，不同交换机之间可以进行网络隔离。每个交换机都有自己的IP地址段和路由表，可以通过路由表进行访问控制。
## 控制网络流量
您可以使用以下方法来控制VPC中资源的网络流量：
创建VPC类型的ECS实例时，可以使用系统提供的默认安全组规则，也可以选择VPC中已有的其他安全组来控制ECS实例的出站和入站流量。[安全组](../../ecs/documents/user-guide/overview-44.md)是VPC内的虚拟防火墙，能够控制进出ECS实例的流量。通过将具有相同安全需求并相互信任的ECS实例放入相同的安全组，可以划分安全域，保障云上资源的安全。此外，[网络](network-acl-overview.md)[ACL](network-acl-overview.md)能够控制进出交换机的流量，通过将多个交换机绑定相同的网络ACL，可统一控制进出多个交换机的流量。结合使用安全组和网络ACL，可以有效地保护VPC内的资源安全。
[IPv4](ipv4-gateway-overview.md)[网关](ipv4-gateway-overview.md)是VPC边界上的公网IPv4流量控制组件。结合路由表配置，可以实现控制公网访问流量统一经过IPv4网关，降低分散接入带来的安全风险。
[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)[网关](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)是VPC的公网IPv6流量网关，通过[配置](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth)[公网带宽](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth)和[仅主动出规则](https://help.aliyun.com/zh/ipv6-gateway/user-guide/create-and-manage-an-egress-only-rule)，可以灵活定义IPv6的出流量和入流量。
创建[自定义路由表](network-traffic-management-using-custom-routing-tables.md)并绑定交换机，添加自定义路由条目来控制该交换机的流量，便于更灵活地进行网络管理。
通过创建[VPC](vpc-peer-to-peer-connection.md)[对等连接](vpc-peer-to-peer-connection.md)，并为两端VPC分别配置路由，可以实现VPC私网互通。对等连接功能支持同账号/跨账号、同地域/跨地域VPC互通，配置前需确保两端VPC的网段不重叠。
[云企业网](../../cen/documents/product-overview/what-is-cen.md)作为多VPC互连的解决方案，可以实现企业内部多个VPC之间的网络互通，打造灵活、可靠、大规模的企业级云上网络。
使用[高速通道](https://help.aliyun.com/zh/express-connect/product-overview/what-is-express-connect/)、[VPN](https://help.aliyun.com/zh/vpn/product-overview/what-is-vpn-gateway)[网关](https://help.aliyun.com/zh/vpn/product-overview/what-is-vpn-gateway)，可以实现[阿里云](connect-vpc-to-local-idc-office-terminal-other-cloud.md)[VPC](connect-vpc-to-local-idc-office-terminal-other-cloud.md)[与用户本地数据中心、办公终端或其他云厂商网络互通](connect-vpc-to-local-idc-office-terminal-other-cloud.md)。
[网关终端节点](vpc-connection-to-cloud-service.md)是虚拟网关设备，在VPC中创建云服务的网关终端节点并指定关联的路由表，系统自动将增加下一跳指向网关终端节点的路由条目，实现对云服务的私网访问。
使用VPC的[流日志](vpc-flow-logs.md)功能捕获VPC网络中弹性网卡ENI的传入和传出流量信息，可以检查访问控制规则、监控网络流量和排查网络故障。
## 网络ACL与安全组
阿里云提供安全组和网络ACL两种访问控制方式，可实现VPC内实例级别或交换机级别的网络隔离。
| 对比项 | 安全组 | 网络 ACL |
| --- | --- | --- |
| 示意图 |  |  |
| 作用范围 | 实例级别 您可以将安全组绑定一个或多个 ECS。 | 交换机级别 您可以将网络 ACL 绑定一个或多个交换机。 |
| 工作方式 | 有状态，自动允许回包。 例如允许入方向访问 80 端口的流量时，您只需为 请求 添加入方向规则，无需配置出方向规则，相关 响应 流量会自动放行。 | 无状态，回包需单独放行。 例如允许入方向访问 80 端口的流量时，您既要为 请求 添加入方向规则，也要为 响应 添加出方向规则。 |
| 组内控制策略 | 普通安全组：可选组内互通或隔离。 企业级安全组：默认组内隔离。 | 不控制同一个交换机内的 ECS 实例间的流量。 |
| 应用场景 | 实例间互访、对外开放端口 | 交换机级别的隔离、跨交换机访问控制 |
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
