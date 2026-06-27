# 公网访问场景与产品解决方案-专有网络VPC-阿里云

Source: https://help.aliyun.com/zh/vpc/public-network-access

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

# 公网访问

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

VPC为您提供安全隔离、弹性扩展的云上网络环境，默认与公网不互通。但您可以结合弹性公网IP、负载均衡、NAT网关等产品，满足VPC内资源公网访问的需求。

## 选择公网IP地址类型

## IPv4地址

VPC内的资源依赖公网IP地址与公网进行IPv4通信。公网IPv4地址类型分为固定公网IP与弹性公网IP。

固定公网IP只能在ECS/CLB等实例创建时分配，并且创建后无法更换绑定/解绑，只能随着实例删除。而[弹性公网](products/eip/documents/product-overview/what-is-eip.md)[IP](products/eip/documents/product-overview/what-is-eip.md)是独立的公网IP资源，可以单独创建与持有、动态绑定/解绑，满足灵活管理的要求，推荐您使用弹性公网IP。

公网ALB、公网NLB、公网NAT网关是通过绑定的弹性公网IP提供公网访问能力。公网ECS、公网CLB的固定公网IP，可以转为弹性公网IP。

弹性公网IP有不同类型：

- 

弹性公网IP（BGP多线）：通过接入多条运营商线路并自动选择最优路径，为用户提供快速稳定的访问体验。

- 

[弹性公网](products/eip/documents/use-boutique-eip-to-optimize-access-to-international-business-in-mainland-china.md)[IP（BGP](products/eip/documents/use-boutique-eip-to-optimize-access-to-international-business-in-mainland-china.md)[多线-精品）](products/eip/documents/use-boutique-eip-to-optimize-access-to-international-business-in-mainland-china.md)：为中国内地终端客户（不包括中国内地数据中心）专门优化的海外回中国内地流量的公网线路，通过运营商精品公网直连降低时延，提升国际业务访问质量。

- 

[任播弹性公网](https://help.aliyun.com/zh/anycast-eip/product-overview/what-is-anycast-eip)[IP（Anycast EIP）](https://help.aliyun.com/zh/anycast-eip/product-overview/what-is-anycast-eip)：每一个Anycast EIP实例会被分配一个可在整个接入区域内发布、不受地域限制的公网IP地址。在将此IP地址与后端资源进行绑定后，接入区域内的用户流量将通过该IP地址从就近接入点进入阿里云网络。进入阿里云网络后，Anycast EIP可以智能选择路由并自动完成网络调度，将用户的网络访问请求送达至后端资源节点，提升用户的公网访问体验。

- 

- 

- 

- 

- 

- 

| 对比项 | 弹性公网 IP（BGP 多线） | 弹性公网 IP（BGP 多线-精品） | 任播弹性公网 IP（Anycast EIP） |
| --- | --- | --- | --- |
| 适用场景 | 通用低成本公网访问 | 海外回中国内地流量 | 全球多地域使用相同 IP |
| 限制说明 | 业务部署在某地域（不限） 终端用户使用互联网，从任意地区访问 | 业务仅限部署在 [海外部分地域](products/eip/documents/use-boutique-eip-to-optimize-access-to-international-business-in-mainland-china.md) 终端用户使用互联网，从中国内地访问 | 业务仅限部署在 [海外部分地域](https://help.aliyun.com/zh/anycast-eip/product-overview/what-is-anycast-eip#title-8ea-s1r-s8b) 终端用户使用互联网，从海外地区 [Anycast EIP](https://help.aliyun.com/zh/anycast-eip/product-overview/what-is-anycast-eip#title-f48-q88-8mz) [接入点位置](https://help.aliyun.com/zh/anycast-eip/product-overview/what-is-anycast-eip#title-f48-q88-8mz) 就近访问 |
| 质量 | 一般（流量经过运营商普通线路） | 较高（流量经过运营商精品线路） | 较高（流量经过运营商普通线路、阿里云优质全球骨干网络） |
| 成本 | 低 | 中 | 高 |


## IPv6地址

为专有网络和交换机开启IPv6后，系统将自动创建[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)[网关](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)并分配IPv6网段，默认仅支持私网通信。

您可以通过在IPv6网关中为IPv6地址[开通](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-dvo-wjp-zcb)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-dvo-wjp-zcb)[公网带宽](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-dvo-wjp-zcb)，使其具备公网通信能力。

IPv6地址是具备全局唯一性的网络地址。IPv6访问公网无需再单独申请特定的公网IP地址资源。

## 用负载均衡统一公网流量入口

单台后端服务器直接使用公网IP对外提供服务时，如果服务器出现问题容易导致业务单点故障。

实际业务场景中，推荐您使用负载均衡产品，在负载均衡后端挂载不同可用区的多台后端服务器，通过将流量分发到不同的后端服务来扩展应用系统的服务吞吐能力，消除系统中的单点故障，提升应用系统的可用性。

推荐您优先使用新一代负载均衡产品，即[应用型负载均衡](products/slb/documents/application-load-balancer/product-overview/what-is-alb.md)[ALB](products/slb/documents/application-load-balancer/product-overview/what-is-alb.md)和[网络型负载均衡](products/slb/documents/network-load-balancer/product-overview/what-is-nlb.md)[NLB](products/slb/documents/network-load-balancer/product-overview/what-is-nlb.md)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 对比项 | 应用型负载均衡 ALB | 网络型负载均衡 NLB |
| --- | --- | --- |
| 产品定位 | 强大的七层处理能力与丰富的高级路由功能 聚焦 HTTP、HTTPS 和 QUIC 协议 | 强大的四层处理能力与大规模 TCPSSL 证书卸载功能 聚焦 TCP、UDP 和 TCPSSL 协议 |
| 产品性能 | 单实例最大支持 100 万 QPS | 单实例最大支持 1 亿并发 |
| 后端资源类型 | 云服务器 ECS 弹性网卡 ENI 弹性容器实例 ECI IP 地址 函数计算 FC | 云服务器 ECS 弹性网卡 ENI 弹性容器实例 ECI IP 地址 |
| 运维能力 | 均支持弹性和快速扩容，处理能力随着业务峰值自动伸缩，无需人工干预 |  |
| 典型应用场景 | 互联网应用七层高性能自动弹性场景 音视频应用大流量低时延场景 云原生应用金丝雀蓝绿发布场景 | 四层大流量高并发业务场景 物联网、车联网等 IoT 业务入口场景 多活容灾、IDC 云上出入口场景 |


## 用NAT网关统一公网流量出口

单台服务器可以通过公网IP地址主动访问公网。

但当需要主动访问公网的服务器较多时，需要占用较多的公网IP资源与成本，也加大了网络运维管理的复杂度。

您可以使用[公网](products/nat-gateway/documents/user-guide/public-network-nat-gateway.md)[NAT](products/nat-gateway/documents/user-guide/public-network-nat-gateway.md)[网关](products/nat-gateway/documents/user-guide/public-network-nat-gateway.md)并配置SNAT条目，实现VPC内的多个ECS实例共享EIP上网，节省公网IP资源与成本、简化网络运维管理。同时公网NAT网关通过地址转换，隐藏云服务器的真实IP地址避免对外暴露，提升了公网安全性。

- 

- 

- 

- 

| 对比项 | 直接使用弹性公网 IP | 公网 NAT 网关 |
| --- | --- | --- |
| 是否支持多服务器共享使用 EIP | 不支持 | 支持 |
| 使用单个 EIP 的粒度 | ECS/弹性网卡粒度 | VPC 粒度 交换机粒度 ECS/弹性网卡粒度 自定义网段粒度 |
| 服务器较多时总体资源成本 | 高 | 低 |
| 安全性 | 一般 | 较高 |


## 用公网网关集中控制公网访问

## IPv4网关

默认情况下VPC内的资源通过绑定公网IP即可与公网直接进行IPv4通信，企业可能会存在未经运维部门管控的公网访问方式（例如业务部门随意为ECS实例配置公网IP），这为企业网络管理带来安全风险。

您可使用[IPv4](products/vpc/documents/ipv4-gateway-overview.md)[网关](products/vpc/documents/ipv4-gateway-overview.md)，结合路由表配置来实现控制公网访问流量统一经过IPv4网关，降低分散接入带来的安全风险。

公有交换机：绑定的路由表中存在目标网段为0.0.0.0/0，下一跳为IPv4网关的路由，其中的资源绑定公网IP即可访问公网。私有交换机：绑定的路由表中不存在指向IPv4网关的路由。其中的资源绑定公网IP后仍无法直接访问公网；但可以配置路由指向公有交换机中的NAT网关，将公网访问流量路由至NAT网关，使用NAT网关绑定的公网IP间接访问公网。为避免激活IPv4网关后私有交换机中的资源无法访问公网，您需确保在激活前完成路由配置。

重要

IPv4网关是VPC的公网IPv4流量网关，激活后会改变VPC默认能够访问公网的行为，如果配置不当可能导致“VPC断网”，请谨慎考虑后再进行配置。详情可了解[IPv4](products/vpc/documents/ipv4-gateway-overview.md)[网关工作模式切换逻辑](products/vpc/documents/ipv4-gateway-overview.md)。

IPv4网关同时可用于实现[公网网段私用、公网出入流量安全引流（第三方安全设备）](products/vpc/documents/ipv4-gateway-overview.md)。

## IPv6网关

VPC内实例默认申请的IPv6地址只具备IPv6私网通信能力。您可以使用[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)[网关](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)，为IPv6地址[开通](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth)[公网带宽](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth)，使其具备公网通信能力。

IPv6网关是VPC的公网IPv6流量网关，可以支持设置[仅主动出规则](https://help.aliyun.com/zh/ipv6-gateway/user-guide/create-and-manage-an-egress-only-rule)，使IPv6地址仅可主动访问公网，无法被公网的客户端访问。

公网CLB不属于VPC内的资源，IPv6流量不受IPv6网关的控制。

## 公网全球加速访问

对于一部分全球化行业应用场景，例如AI智能体出海、游戏加速、互联网应用等，因公网网络质量不高可能导致的网络高延迟、多抖动、低速率等问题，严重影响终端用户使用体验。

您可以通过使用[全球加速](https://help.aliyun.com/zh/ga/product-overview/what-is-global-accelerator/)产品，使终端用户访问请求就近接入阿里云，通过阿里云优质全球骨干网络到达应用服务器，极大地缩短了公网传输路径，减少延时、抖动、速率低等网络问题，提升终端用户使用体验。

## 节省公网成本

除了云资源本身的费用外，公网费用往往占据用户较大的成本。

推荐您使用如下方式来节省公网成本：

- 

节省公网IP成本：通过用负载均衡统一公网流量入口、用NAT网关统一公网流量出口，可以减少公网IP数量，从而降低[公网](products/eip/documents/pay-as-you-go.md)[IP](products/eip/documents/pay-as-you-go.md)[保有费（原](products/eip/documents/pay-as-you-go.md)[EIP](products/eip/documents/pay-as-you-go.md)[配置费）](products/eip/documents/pay-as-you-go.md)。

- 

节省公网流量成本：您可以使用[云数据传输](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt)[CDT](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt)，CDT支持免费流量额度、多款云产品IPv4/IPv6流量统一汇总计费、累计阶梯定价等多种优惠方式，可有效节省您的公网流量成本。

[上一篇：网络互通](products/vpc/documents/network-interworking.md)[下一篇：IPv4网关](products/vpc/documents/ipv4-gateway-overview.md)

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
