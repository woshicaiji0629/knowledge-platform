# VPC与外部网络互通解决方案-专有网络VPC-阿里云

Source: https://help.aliyun.com/zh/vpc/connect-vpc-to-local-idc-office-terminal-other-cloud

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/vpc/documents/vpc-user-guide.md)

- [开发参考](products/vpc/documents/developer-reference.md)

- [产品计费](products/vpc/documents/product-billing.md)

- [常见问题](products/vpc/documents/troubleshooting.md)

- [动态与公告](products/vpc/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# VPC连接本地数据中心/其他云

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以使用高速通道、VPN网关产品，实现阿里云VPC与用户本地数据中心、办公终端或其他云厂商网络互通。

## VPC连接本地数据中心

### 选择连接方案

常见的有如下两种连接方案：

- 

专线：通过运营商物理专线将本地数据中心网络连接到阿里云接入点机房。在物理专线两端距离很远的情况下，仍可以提供低时延、低丢包率和高带宽的内网级通信质量。

- 

VPN：通过建立公网加密隧道的方式，实现本地数据中心与阿里云VPC之间建立安全可靠的网络连接。VPN连接质量会受到公网网络质量的影响。

| 连接方式 | 专线 | VPN |
| --- | --- | --- |
| 网络时延 | 低 | 中 |
| 建设周期 | 长 | 短 |
| 总体成本 | 高 | 低 |
| 安全性 | 高 | 中 |
| 扩展便捷性 | 低 | 高 |


### 使用专线连接

本地数据中心使用专线连接到阿里云，您需要使用到[高速通道](https://help.aliyun.com/zh/express-connect/product-overview/what-is-express-connect/)产品。

连接过程中您需要进行的操作：

- 

申请物理专线端口，并完成您本地数据中心设备到阿里云接入点机房设备的[物理专线连接](https://help.aliyun.com/zh/express-connect/user-guide/what-is-a-physical-connection/)。物理专线类型分为独享专线和共享专线，会涉及到运营商工勘、专线铺设、布线施工等工作，整个施工周期预计按月为单位，建议您提前做好时间与预算规划。

- 

独享专线：运营商从您的本地数据中心机房，新增一条专线并连接到阿里云接入点机房，整个施工周期预计需要1至3个月。该条专线及对应端口为您独有。

- 

共享专线：部分运营商会预先与阿里云接入点建立连接，使用共享专线需要运营商从运营商的接入点新增专线，并连接到您的本地数据中心机房，整个施工周期一般在1个月内。在这种连接方式下，运营商接入点和阿里云接入点之间的连接是多租户共享。

- 

配置[边界路由器](https://help.aliyun.com/zh/express-connect/user-guide/what-is-a-virtual-border-router/)[VBR](https://help.aliyun.com/zh/express-connect/user-guide/what-is-a-virtual-border-router/)、[专线网关](https://help.aliyun.com/zh/express-connect/user-guide/ecr/)[ECR](https://help.aliyun.com/zh/express-connect/user-guide/ecr/)实例，并完成与VPC的连接。

其他建议：

- 

为了避免单条物理专线可能因外界不可抗力导致网络中断（例如专线某处被误挖断），您可以通过双专线、双接入点的方式，提升物理专线链路可靠性。对于非核心业务，您可考虑[使用专线+VPN](https://help.aliyun.com/zh/cloud-network-well-architected-design/dedicated-line-to-build-hybrid-cloud-multi-cloud-network#b47123fe77xk2)[做主备](https://help.aliyun.com/zh/cloud-network-well-architected-design/dedicated-line-to-build-hybrid-cloud-multi-cloud-network#b47123fe77xk2)，降低总体成本。

- 

由于专线流量本身没有加密机制，而部分行业又因安全合规政策，要求敏感数据即使通过专线传输也需要进行加密，此时您可以参考：[通过私网](https://help.aliyun.com/zh/cloud-network-well-architected-design/build-a-branch-to-cloud-network-by-ipsec-vpn#18797162c8xki)[VPN](https://help.aliyun.com/zh/cloud-network-well-architected-design/build-a-branch-to-cloud-network-by-ipsec-vpn#18797162c8xki)[网关实现物理专线加密通信](https://help.aliyun.com/zh/cloud-network-well-architected-design/build-a-branch-to-cloud-network-by-ipsec-vpn#18797162c8xki)。

- 

实际生产环境中，通常有多个VPC需要与本地数据中心互通，同时VPC之间也需要互通，人工配置路由相对繁琐，您可以考虑更加便捷的组网方式。您可以通过将专有网络VPC与专线网关ECR均连接至[转发路由器](products/cen/documents/product-overview/how-transit-routers-work.md)[TR](products/cen/documents/product-overview/how-transit-routers-work.md)，结合BGP动态路由实现全网高效互联。动态路由能够根据网络拓扑的变化自动调整路由表，减少人工配置的工作量，降低组网配置复杂度。

### 使用VPN连接

本地数据中心使用VPN连接到阿里云，推荐您使用[IPsec-VPN](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/product-overview/what-is-ipsec-vpn)产品。

IPsec-VPN有2种使用方式，主要区别如下：

| 使用方式 | 绑定 VPN 网关 | 绑定转发路由器 TR |
| --- | --- | --- |
| 应用场景 | 本地数据中心仅能与 VPN 网关实例所在的 VPC 互通。 | 本地数据中心可以通过 [转发路由器](products/cen/documents/product-overview/how-transit-routers-work.md) [TR](products/cen/documents/product-overview/how-transit-routers-work.md) 实例与 [云企业网](products/cen/documents/product-overview/what-is-cen.md) [CEN](products/cen/documents/product-overview/what-is-cen.md) 内的任意 VPC、其他本地数据中心互通。 |
| 双隧道时实现高可用链路的方式 | 主备链路 | ECMP 链路 ECMP（Equal-Cost Multipath Routing）通过多路径同时分担流量，实现负载均衡和链路备份，提升网络效率和可靠性。 |
| IPsec 连接带宽是否可扩充 | 否 | 是。可以创建多个 IPsec 连接，通过 ECMP 链路同时传输流量，从而间接实现带宽扩充。 |


## 绑定VPN网关

IPsec连接绑定VPN网关场景下，两条隧道一主一备。在一条隧道故障后，可以切换至另一条隧道进行传输。

实际生产环境中，部分企业在进行网络设计时往往会设计单独的DMZ VPC，用于统一公网出入口管控、安全隔离公网流量。您可参考该方案设计VPN上云：[通过](https://help.aliyun.com/zh/cloud-network-well-architected-design/build-a-branch-to-cloud-network-by-ipsec-vpn#28526b1963ehl)[VPN](https://help.aliyun.com/zh/cloud-network-well-architected-design/build-a-branch-to-cloud-network-by-ipsec-vpn#28526b1963ehl)[网关连接到](https://help.aliyun.com/zh/cloud-network-well-architected-design/build-a-branch-to-cloud-network-by-ipsec-vpn#28526b1963ehl)[DMZ VPC](https://help.aliyun.com/zh/cloud-network-well-architected-design/build-a-branch-to-cloud-network-by-ipsec-vpn#28526b1963ehl)[方式（主备隧道）](https://help.aliyun.com/zh/cloud-network-well-architected-design/build-a-branch-to-cloud-network-by-ipsec-vpn#28526b1963ehl)。

## 绑定转发路由器TR

IPsec连接绑定转发路由器TR场景下，两条隧道自动形成ECMP链路，本地网关设备也开启ECMP时，两条隧道均传输流量。在一条隧道故障后，可以切换至另一条隧道进行传输。

## VPC连接其他云（多云）

VPC连接其他云，与[VPC](products/vpc/documents/connect-vpc-to-local-idc-office-terminal-other-cloud.md)[连接本地数据中心](products/vpc/documents/connect-vpc-to-local-idc-office-terminal-other-cloud.md)类似。您可以将其他云视为“特殊的本地数据中心”，使用专线或IPsec-VPN进行连接，构建多云环境。

以阿里云VPC与AWS VPC进行互通为例。

## 专线连接多云

建议双专线、双接入点等方式，提升专线链路可靠性。

多云环境下，往往有多个VPC需要互通，人工配置路由相对繁琐，您可以通过将专有网络VPC与专线网关ECR均连接至[转发路由器](products/cen/documents/product-overview/how-transit-routers-work.md)[TR](products/cen/documents/product-overview/how-transit-routers-work.md)，结合BGP动态路由实现全网高效互联。动态路由能够根据网络拓扑的变化自动调整路由表，减少人工配置的工作量，降低组网配置复杂度。

## IPsec-VPN连接多云

阿里云和AWS平台下的IPsec-VPN连接均支持双隧道模式，但由于AWS平台的两条隧道默认关联至同一个客户网关，而阿里云侧两条隧道拥有不同的IP地址，导致AWS平台和阿里云侧的两条隧道无法做到一一对应建立连接。

为确保阿里云侧IPsec-VPN连接下两条隧道同时启用，您需要在AWS平台创建两个站点到站点的VPN连接，每个站点到站点VPN连接关联不同的客户网关。

多云环境下，往往有多个VPC需要互通，人工配置路由相对繁琐，您可以通过将IPsec连接绑定至[转发路由器](products/cen/documents/product-overview/how-transit-routers-work.md)[TR](products/cen/documents/product-overview/how-transit-routers-work.md)，结合BGP动态路由实现全网高效互联。动态路由能够根据网络拓扑的变化自动调整路由表，减少人工配置的工作量，降低组网配置复杂度。

阿里云IPsec-VPN绑定转发路由器TR时，默认开启ECMP，建议您在AWS侧也开启ECMP。如果AWS侧未开启ECMP，则AWS流向阿里云的流量需要指定连接，阿里云流向AWS的流量则会根据ECMP自动选择隧道。

## 办公终端连接VPC

办公终端使用VPN连接到阿里云VPC，推荐您使用[SSL-VPN](https://help.aliyun.com/zh/vpn/sub-product-ssl-vpn/product-overview/what-is-ssl-vpn)产品。

SSL-VPN支持市场主流的桌面客户端（Windows、Linux、macOS）和移动客户端（Android、iOS）接入。

如果企业一部分应用同时部署在本地数据中心，您可以为VPN网关实例一并开启IPsec-VPN和SSL-VPN功能，同时连接本地数据中心和客户端。

连接建立后，客户端和本地数据中心均可以访问VPC，且客户端和本地数据中心之间可以互相通信。

[上一篇：VPC对等连接](products/vpc/documents/vpc-peer-to-peer-connection.md)[下一篇：VPC私网访问云服务](products/vpc/documents/vpc-connection-to-cloud-service.md)

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
