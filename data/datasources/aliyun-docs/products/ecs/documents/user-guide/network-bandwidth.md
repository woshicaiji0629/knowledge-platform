# 网络带宽核心机制与计费详解-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/user-guide/network-bandwidth

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# ECS实例网络带宽

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

网络带宽是指在单位时间内能传输的数据量，带宽数值越大表示传输能力越强，即在单位时间内传输的数据量越多。网络带宽分为公网带宽和内网带宽。

## 公网带宽

公网带宽是指ECS实例到公网之间的网络带宽流量。公网带宽由出网带宽和入网带宽组成，您购买的带宽值实际是出网带宽值。下图为数据流的方向说明。

数据流向以云服务器ECS为参照。

- 

- 

- 

- 

- 

- 

| 带宽类别 | 入网带宽 | 出网带宽 |
| --- | --- | --- |
| 定义 | 入网（下行）指数据流入 ECS，是服务器接收外部网络数据的公网带宽下行流量。例如： 云服务器 ECS 下载外部网络资源。 FTP 客户端上传资源到云服务器 ECS。 | 出网（上行）指数据流出 ECS，是服务器向外部网络传输数据的公网带宽上行流量。例如： 云服务器 ECS 对外提供访问。 FTP 客户端下载云服务器 ECS 内部资源。 |
| 计费 | 免费。 阿里云会为用户提供一定的入网带宽上限，但入网带宽的最大值受出网带宽的影响。 当出网带宽值小于 10 Mbit/s 时，入网带宽最大值为 10 Mbit/s。 当出网带宽值大于 10 Mbit/s 时，入网带宽的值与您购买的出网带宽一致。 | 收费。 带宽计费是按出网带宽来收取。用户需要根据自己的业务需求选择合适的出网带宽大小进行购买，并且不同的计费模式（如按固定带宽计费或者按流量计费）会影响费用和带宽的上限。 固定公网 IP 的出网带宽峰值最高可选规格一般为 200Mbit/s，具体请以购买页为准。当您认为固定公网 IP 带宽峰值过小，不能满足业务需求时，请考虑使用 [EIP](products/eip/documents/product-overview/what-is-eip.md) 与 [共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/product-overview/what-is-internet-shared-bandwidth) 等产品。 重要 按使用流量计费 模式下的出入带宽峰值都是带宽上限，不作为业务承诺指标。当出现资源争抢时，带宽峰值可能会受到限制。如果您的业务需要有带宽的保障，请使用 按固定带宽计费 模式。 |


说明

阿里云控制台上显示的公网带宽值单位通常是Mbps，假设您的ECS实例拥有5 Mbps的公网带宽值，根据换算：5 Mbps = 5 Mbit/s = 0.625 MB/s = 640 KB/s，您的ECS实例出网带宽值（上行带宽速率）为640 KB/s。

### 开通公网带宽

为了使ECS实例实现公网通信，您可以在ECS实例创建时[分配固定公网](products/ecs/documents/user-guide/public-ip-address.md)[IP](products/ecs/documents/user-guide/public-ip-address.md)或创建后[修改公网带宽](products/ecs/documents/user-guide/modify-the-bandwidth-configurations.md)，这两种方式会使ECS实例得到一个固定公网IP从而开通固定公网带宽。

您也可以通过为实例[绑定](products/ecs/documents/user-guide/associate-or-disassociate-an-eip.md)[EIP](products/ecs/documents/user-guide/associate-or-disassociate-an-eip.md)或者[购买公网](products/nat-gateway/documents/user-guide/use-internet-nat-gateway-for-public-network-access.md)[NAT](products/nat-gateway/documents/user-guide/use-internet-nat-gateway-for-public-network-access.md)[网关](products/nat-gateway/documents/user-guide/use-internet-nat-gateway-for-public-network-access.md)等方式来开通公网带宽。IPv6地址也可以开通公网带宽，详见[开通](products/ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[IPv6](products/ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[公网带宽](products/ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。

### 带宽计费

固定公网带宽，即固定公网IP的公网带宽支持按固定带宽计费和按流量计费两种计费方式，不同计费方式请参见[公网带宽计费](products/ecs/documents/public-bandwidth.md)。

如果您使用了EIP，计费规则请参见[EIP](products/eip/documents/billing-overview.md)[计费概述](products/eip/documents/billing-overview.md)。如果使用了公网NAT网关，计费规则请参见[NAT](products/nat-gateway/documents/nat-gateway-billing.md)[网关计费说明](products/nat-gateway/documents/nat-gateway-billing.md)。

如果您期望地域级的带宽共享和复用，可以购买[共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/product-overview/what-is-internet-shared-bandwidth#concept-mks-snx-b2b)。您可以将同地域下的弹性公网IP（EIP）添加到共享带宽实例中，复用共享带宽中的带宽，节省公网带宽使用成本。[共享流量包](https://help.aliyun.com/zh/dtp/product-overview/what-is-a-data-transfer-plan#concept-usr-lsx-b2b)是一款流量套餐产品，可以抵扣按量计费的固定公网IP、EIP、CLB和按主流量计费的共享带宽产生的IPv4流量（不包含EIP精品流量）费用，降低公网带宽使用费用。

### 带宽安全

- 

云安全中心默认为ECS实例免费提供最大5 Gbps的流量攻击的防护，不同实例规格的免费防护流量不同。更多信息，请参见[DDoS](https://help.aliyun.com/zh/anti-ddos/basic-ddos-protection/product-overview/view-the-thresholds-that-trigger-blackhole-filtering-in-anti-ddos-origin-basic#concept-40033-zh)[基础防护黑洞阈值](https://help.aliyun.com/zh/anti-ddos/basic-ddos-protection/product-overview/view-the-thresholds-that-trigger-blackhole-filtering-in-anti-ddos-origin-basic#concept-40033-zh)。

- 

启用DDoS基础防护后，云安全中心会实时监控进入ECS实例的流量。当监测到超大流量或者包括DDoS攻击在内的异常流量时，在不影响正常业务的前提下，云安全中心会将可疑流量从原始网络路径中重定向到净化产品上，识别并剥离恶意流量，并将还原的合法流量回注到原始网络中转发给目标ECS实例。更多信息，请参见[DDoS](https://help.aliyun.com/zh/anti-ddos/anti-ddos-origin/product-overview/what-is-anti-ddos-origin#concept-63643-zh)[原生防护](https://help.aliyun.com/zh/anti-ddos/anti-ddos-origin/product-overview/what-is-anti-ddos-origin#concept-63643-zh)。

- 

当ECS实例遭受DDoS攻击时，您可以根据推送的事件及时进行处理。更多信息，请参见[DDoS](products/ecs/documents/user-guide/summary.md)[安全攻击事件](products/ecs/documents/user-guide/summary.md)。

### 使用限制

自2020年11月27日起，创建和变配ECS实例时带宽峰值受账户限速策略影响。如需更大带宽峰值，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)。

具体限速策略如下：

- 

单个地域下，所有按使用流量计费ECS实例的实际运行带宽峰值总和不大于5 Gbps。

- 

单个地域下，所有按固定带宽计费ECS实例的实际运行带宽峰值总和不大于50 Gbps。

单ECS实例的公网带宽上限与实例规格有关，可以通过[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)列表的网络带宽基础指标查看，单实例的公网带宽之和不会高于此上限。

更多信息，请参见[公网带宽限制](products/ecs/documents/user-guide/limitations.md)。

## 内网带宽

内网带宽是指同一地域同一专有网络内的云服务器ECS实例之间传输的内网带宽流量。云服务器ECS与云数据库、负载均衡以及对象存储之间也可以使用内网相互连接。当前同地域内内网带宽流量是免费的。内网带宽大小跟实例规格有关，带宽值可通过[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)列表的网络带宽基础指标查看。如果实例有多个网卡，所有网卡的内网带宽之和不高于实例的带宽值。

说明

- 

不同可用区之间流量带宽受限于实例规格带宽，但延迟会因可用区之间的距离增大而增加。

- 

部署集内及部署集之间内网流量带宽受限于实例规格带宽。

- 

实例规格中的网络带宽性能一般是基于使用1514字节大小的数据包来定义的。如果实例中传输的数据包的大小较小（小于1514字节），则可达到的网络带宽性能也会相应降低。

当您使用内网带宽时，您需要注意以下信息：

- 

不同实例会共享物理网络带宽。内网带宽会受其他实例内网流量影响而产生波动，但一般都可以达到实例规格标注的带宽值。测试内网带宽性能请参见[网络性能测试方法](products/ecs/documents/user-guide/best-practices-for-testing-network-performance.md)。

- 

当业务带宽偶尔超过实例规格网络基础带宽时，可以选择拥有[突发带宽](products/ecs/documents/user-guide/network-bandwidth.md)的实例规格。

- 

面对高性能计算、大数据处理、AI训练等场景，您可以选择具有[弹性](products/ecs/documents/user-guide/erdma-overview.md)[RDMA](products/ecs/documents/user-guide/erdma-overview.md)[能力](products/ecs/documents/user-guide/erdma-overview.md)的实例规格，满足低延迟、高吞吐的网络服务。RDMA通过绕过内核协议栈，将数据直接从用户态程序转移到HCA（Host Channel Adapter）中进行网络传输，有效降低CPU负载和延迟。

- 

如果您需要100 Gbps及以上内网带宽，您可以选择支持[物理网卡映射](products/ecs/documents/user-guide/network-card-mapping.md)的实例规格，通过指定物理网卡索引，将弹性网卡绑定到底层不同的通信信道，最大限度地利用带宽。

- 

对于有并发接收和发送内网流量需求的业务，推荐使用七代及之后规格族的ECS，以享受全双工的收发带宽。即接收和发送速率单独计算，在全速率接收流量的同时，也能全速率地发送数据包，两者互不干扰，从而提高通信效率。例如一个实例拥有1Gbps的内网带宽，那么它可以同时以1Gbps的速度接收内网数据，也以1Gbps的速度发送内网数据。

### 突发带宽

六代及之后的部分实例规格开始支持突发网络带宽，当整机网络带宽资源充足，且该实例有网络突发积分时，网络连接可以临时突破基础带宽限制的能力，您可以在业务突增时获得更高的传输速率。网络突发带宽是利用闲置资源的让利，不承诺SLA。如果您的业务有明确的带宽需求，实例选型请参考实例基础网络带宽。

ECS实例网络带宽是否具备突发能力及突发带宽最高限制等，请参见[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)。

说明

突发带宽只针对于内网带宽，不适用于公网带宽。

网络突发积分

阿里云ECS实例在内网带宽空闲时（实时带宽小于基础带宽）会积攒积分，积分上限取决于实例规格。当带宽突增（实时带宽超过基础带宽）时，可消耗积分临时提升带宽。积分耗尽后，带宽恢复至基础带宽。网络突发积分只是网络突发带宽的前提条件之一，不作为网络突发带宽的承诺，不提供查询服务。

网络突发积分详细规则说明

- 

积分

积分用于表示ECS实例在超过网络基础带宽后，每1个积分允许您在多长时间内达到最大突发带宽，带宽和时间成反比，带宽越高，持续的时间越短，1个积分提供的带宽总量是固定的。以ecs.g8i.large为例，最大突发带宽是15 Gbps，表示如果有1个积分可以：

- 

以15 Gbps的带宽持续运行1秒。

- 

以7.5 Gbps的带宽持续运行2秒。

- 

以5 Gbps的带宽持续运行3秒。

- 

启动积分

当ECS实例启动时，根据其规格和配置，会为该实例分配一定数量的启动积分，并将其作为累积积分上限。

- 

累计积分上限

实例可以累计的最高积分。累计积分上限与实例规格相关，规格越大，累积积分上限越高。

- 

获取积分

ECS实例启动后尚未产生网络流量时，持续获取积分，获取速度与实例规格相关，获取的积分可以满足实时消耗的网络带宽运行到基础带宽。以ecs.g8i.large为例：

（基础带宽2.5 Gbps / 突发带宽15 Gbps）* 60秒 = 10，表示每分钟获取10积分。

- 

累积积分

ECS实例在运行状态且实时消耗的网络带宽小于基础带宽时，多余的积分会累积，但不会超过累积积分上限，累积速度与实时消耗的网络带宽相关，实时消耗带宽越高，累计越慢。

每分钟累计积分数= (基础带宽−实时消耗带宽​) / 突发带宽 * 60 。以ecs.g8i.large为例：

- 

假如当前实时消耗的网络带宽是2.0 Gbps，（基础带宽2.5 Gbps - 实时消耗带宽2.0 Gbps）/（突发带宽15 Gbps）* 60秒 = 2，表示网络带宽每分钟累积2积分。

- 

假如当前实时消耗的网络带宽是1.5 Gbps，（基础带宽2.5 Gbps - 实时消耗带宽1.5 Gbps）/（突发带宽15 Gbps）* 60秒 = 4，表示网络带宽每分钟累积4积分。

- 

消耗积分

ECS实例实时消耗的网络带宽大于基础带宽时，开始消耗积分，当积分耗尽时，实时消耗带宽被限制到基础带宽。消耗速度与实时网络带宽相关，实时网络带宽越高，消耗速度越快。

每分钟消耗积分数=（实时消耗带宽 / 突发带宽）* 60 。以ecs.g8i.large为例：

- 

假如当前实时消耗的网络带宽是15 Gbps，（实时消耗带宽15 Gbps / 突发带宽15 Gbps）* 60秒 = 60，表示网络带宽每分钟消耗60积分。

- 

假如当前实时消耗的网络带宽是10 Gbps，（实时消耗带宽10 Gbps / 突发带宽15 Gbps）* 60秒 = 40，表示网络带宽每分钟消耗40积分。

## 监控网络带宽

说明

目前不支持控制台查看ECS所在虚拟交换机的实时总内网流量。

您可以通过以下步骤在ECS控制台监控实例的内网带宽与公网带宽使用情况：

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。

- 

在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

找到目标实例，点击进入实例详情页。

- 

单击监控页签。

- 

设置监控时间范围，查看内网带宽与公网带宽等信息。

由于监控曲线显示的聚合方式不一样，选择时间段的长短会影响显示的精度。选择的时间范围越小，显示效果越精细。例如，1小时和6小时的平均值会显示不一样的结果，请您根据实际需要选择适合的时间范围。

假设您购买的公网带宽为1 Mbps，当公网流出带宽达到1024 Kbit/s时，表示您的公网带宽已经满负荷。当您发现带宽使用率过高或过低时，可以考虑[修改带宽配置](products/ecs/documents/user-guide/modify-bandwidth-configurations.md)。

说明

如果此页面显示暂无数据，可能是由于此ECS实例的云监控插件未安装，或者云监控插件运行异常，您可以尝试重新安装云监控插件，详细信息，请参见[安装和卸载云监控插件](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/install-and-uninstall-the-cloudmonitor-agent-for-cpp)。

除了使用上述方式，您也可以通过[云监控](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/what-is-cloudmonitor#concept-2452587)或[网络分析与监控](https://help.aliyun.com/zh/document_detail/341648.html#a9eff49079ji3)来监控网络带宽。

## 相关文档

- 

如果当前带宽计费方式不满足业务需求，您可以转换公网带宽计费方式：[转换固定公网](products/ecs/documents/change-the-billing-method-for-network-usage-1.md)[IP](products/ecs/documents/change-the-billing-method-for-network-usage-1.md)[的带宽计费方式](products/ecs/documents/change-the-billing-method-for-network-usage-1.md)。

- 

如果发现公网带宽无法满足或者超出业务需求，您可以修改公网带宽：[修改固定公网带宽](products/ecs/documents/user-guide/modify-the-bandwidth-configurations.md)。

- 

如果您使用的是弹性公网IP，您可以通过变更EIP带宽功能实时调整EIP带宽峰值和计费方式：[变更](products/ecs/documents/user-guide/modify-the-bandwidth-of-an-eip.md)[EIP](products/ecs/documents/user-guide/modify-the-bandwidth-of-an-eip.md)[带宽](products/ecs/documents/user-guide/modify-the-bandwidth-of-an-eip.md)。

- 

BGP（多线）适用于中国香港本地、中国香港和海外之间的互联网访问。使用 BGP（多线）回国将绕行国际运营商出口，如需要优化回国时延，请选择 BGP（多线）精品线路。

- 

依托阿里云优质的BGP带宽和全球传输网络，您也可以通过[任播弹性公网](https://help.aliyun.com/zh/anycast-eip/product-overview/what-is-anycast-eip#concept-2494813)[IP](https://help.aliyun.com/zh/anycast-eip/product-overview/what-is-anycast-eip#concept-2494813)提升公网访问质量。

[上一篇：网络](products/ecs/documents/user-guide/network.md)[下一篇：开通公网](products/ecs/documents/user-guide/best-practices-for-configuring-public-bandwidth.md)

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
