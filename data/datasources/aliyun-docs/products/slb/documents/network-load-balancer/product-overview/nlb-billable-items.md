# NLB计费规则-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/network-load-balancer/product-overview/nlb-billable-items

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/slb/documents/network-load-balancer/product-overview.md)

- [快速入门](products/slb/documents/network-load-balancer/getting-started.md)

- [操作指南](products/slb/documents/network-load-balancer/user-guide.md)

- [实践教程](products/slb/documents/network-load-balancer/use-cases.md)

- [开发参考](products/slb/documents/network-load-balancer/developer-reference.md)

- [服务支持](products/slb/documents/network-load-balancer/service-support.md)

[首页](https://help.aliyun.com/zh)

# NLB计费规则

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/slb)

[我的收藏](https://help.aliyun.com/my_favorites.html)

网络型负载均衡NLB（Network Load Balancer）支持按量付费。本文为您介绍NLB的计费组成、计费规则等信息。

## 按量付费说明

- 

- 

| 特性 | 说明 |
| --- | --- |
| 计费说明 | 按量付费是一种先使用后付费的计费方式，也称为后付费，在每个结算周期生成账单并从账户中扣除相应费用。 |
| 计费周期及出账时间 | NLB 的实例费和性能容量单位 LCU（Loadbalancer Capacity Unit）费均为按小时计费，并按照使用量结算产生的费用。账单出账时间通常在当前计费周期结束后一小时，具体出账时间以系统为准。 公网 NLB 会收取公网网络费用，公网 NLB 通过弹性公网 IP（EIP）提供公网能力，因此公网网络费用的计费周期、扣费及出账时间与按量付费 EIP 的计费周期、扣费及出账时间一致。更多信息，请参见 [弹性公网](products/eip/documents/pay-as-you-go.md) [IP](products/eip/documents/pay-as-you-go.md) [按量付费](products/eip/documents/pay-as-you-go.md) 。 |


## NLB计费组成

NLB的费用由三部分组成：实例费、性能容量单位LCU费和公网网络费。

| 实例网络类型 | 实例费 | 性能容量单位 LCU 费 | 公网网络费 |
| --- | --- | --- | --- |
| 公网 | 包含 | 包含 | 包含 |
| 私网 | 包含 | 包含 | 不涉及 |


说明

NLB限时免实例费活动已结束，系统已于2023年10月01日开始收取NLB实例费。

## 实例费

NLB实例费按小时收取，计费周期为1小时。在一个计费周期内，如果您使用的时长不足1小时，按1小时计算。计费时长为实例创建完成到实例释放结束的时间段。

实例费=实例单价(元/小时)×计费时长(小时)

下表中的价格为产品目录价，实际购买价格请以[购买页](https://common-buy.aliyun.com/?commodityCode=slb_nlb_public_cn#/buy)为准。

| 计费项 | 实例费单价（元/小时） |
| --- | --- |
| 实例费 | 0.147 说明 NLB 限时免实例费活动已结束，系统已于 2023 年 10 月 01 日开始收取 NLB 实例费。 |


## 性能容量单位LCU费

性能容量单位LCU（Loadbalancer Capacity Unit）是用来衡量负载均衡消耗资源的最小计量单位。

### LCU用量定义

NLBLCU费按小时收取，计费周期为1小时。在一个计费周期内，如果您使用的时长不足1小时，按1小时计算。

每小时LCU费=LCU单价(元/个)×每小时LCU个数 每小时LCU个数=max{新建连接数LCU个数，并发连接数LCU个数，处理流量LCU个数}

单个LCU包含的性能指标与NLB监听的协议有关。

- 

TCP流量

| 指标名称 | 描述 | 计量时间 | LCU 系数 | 各指标每小时 LCU 个数计算 |
| --- | --- | --- | --- | --- |
| 新建连接数 | 每秒处理的新建 TCP 连接的数量。 | 秒 | 800 个 | 在一个计费周期内，系统会统计所有每秒新建 TCP 连接数，然后使用最大每秒新建连接数除以 LCU 系数，得到该计费周期内的新建连接数 LCU 个数。计算公式如下： LCU 个数=最大新建连接数÷LCU 系数 |
| 并发连接数 | 每分钟内并发 TCP 连接的数量。 | 分钟 | 100,000 个 | 在一个计费周期内，系统会统计每分钟的并发 TCP 连接数，然后使用最大每分钟并发连接数除以 LCU 系数，得出该计费周期内的并发连接数 LCU 个数。计算公式如下： LCU 个数=最大并发连接数÷LCU 系数 |
| 处理数据量 | NLB 处理的 TCP 请求和响应的数据处理量，单位为 GB。 | 小时 | 1 GB | 在一个计费周期内，系统会统计总的 TCP 请求和响应的数据处理量，然后使用总的数据处理量除以 LCU 系数，得出该计费周期内的处理数据量的 LCU 个数。计算公式如下： LCU 个数=总处理数据量÷LCU 系数 |


- 

UDP流量

| 指标名称 | 描述 | 计量时间 | LCU 系数 | 各指标每小时 LCU 个数计算 |
| --- | --- | --- | --- | --- |
| 新建连接数 | 每秒处理的新建 UDP 连接的数量。 | 秒 | 400 个 | 在一个计费周期内，系统会统计所有每秒新建 UDP 连接数，然后使用最大每秒新建连接数除以 LCU 系数，得到该计费周期内的新建连接数 LCU 个数。计算公式如下： LCU 个数=最大新建连接数÷LCU 系数 |
| 并发连接数 | 每分钟内并发 UDP 连接的数量。 | 分钟 | 50,000 个 | 在一个计费周期内，系统会统计每分钟的并发 UDP 连接数，然后使用最大每分钟并发连接数除以 LCU 系数，得出该计费周期内的并发连接数 LCU 个数。计算公式如下： LCU 个数=最大并发连接数÷LCU 系数 |
| 处理数据量 | NLB 处理的 UDP 请求和响应的数据处理量，单位为 GB。 | 小时 | 1 GB | 在一个计费周期内，系统会统计总的 UDP 请求和响应的数据处理量，然后使用总的数据处理量除以 LCU 系数，得出该计费周期内的处理数据量的 LCU 个数。计算公式如下： LCU 个数=总处理数据量÷LCU 系数 |


- 

TCPSSL流量

| 指标名称 | 描述 | 计量时间 | LCU 系数 | 各指标每小时 LCU 个数计算 |
| --- | --- | --- | --- | --- |
| 新建连接数 | 每秒处理的新建 TCPSSL 连接的数量。 | 秒 | 50 个 | 在一个计费周期内，系统会统计所有每秒新建 TCPSSL 连接数，然后使用最大每秒新建连接数除以 LCU 系数，得到该计费周期内的新建连接数 LCU 个数。计算公式如下： LCU 个数=最大新建连接数÷LCU 系数 |
| 并发连接数 | 每分钟内并发 TCPSSL 连接的数量。 | 分钟 | 3,000 个 | 在一个计费周期内，系统会统计每分钟的并发 TCPSSL 连接数，然后使用最大每分钟并发连接数除以 LCU 系数，得出该计费周期内的并发连接数 LCU 个数。计算公式如下： LCU 个数=最大并发连接数÷LCU 系数 |
| 处理数据量 | NLB 处理的 TCPSSL 请求和响应的数据处理量，单位为 GB。 | 小时 | 1 GB | 在一个计费周期内，系统会统计总的 TCPSSL 请求和响应的数据处理量，然后使用总的数据处理量除以 LCU 系数，得出该计费周期内的处理数据量的 LCU 个数。计算公式如下： LCU 个数=总处理数据量÷LCU 系数 |


各个监听在1小时内消耗的LCU数量根据上述指标进行换算，按照LCU使用量最多的指标来进行付费。单个NLB实例的LCU费为各个监听的LCU费之和。

### LCU单价

某小时内NLB实例各指标换算LCU后，按照实际使用量计算该小时LCU消耗，最小精度为0.000001 LCU。例如您某小时消耗了0.1 LCU，即该小时的LCU费用为0.1×0.037=0.0037元。

下表中的价格为产品目录价，实际购买价格请以[购买页](https://common-buy.aliyun.com/?commodityCode=slb_nlb_public_cn#/buy)为准。

| 计费项 | LCU 单价（元/个/小时） |
| --- | --- |
| 性能容量单位 LCU | 0.037 |


### LCU计费示例

您于2022年11月02日08:10:00在华东1（杭州）地域创建了1个按使用量计费的NLB实例，并为该实例配置了TCP和UDP监听，于2022年11月02日08:50:00释放了该实例。在08:10:00~08:50:00时间段（一个计费周期）该NLB实例的最大新建连接数、最大并发连接数和处理数据量的示例数据如下表所示。

| 指标名称 | TCP | UDP |
| --- | --- | --- |
| 新建连接数（秒） | 该小时内最大新建 TCP 连接数为 4,000 个。 LCU 换算值： 4,000÷800=5.0 | 该小时内最大新建 UDP 连接数为 2,000 个。 LCU 换算值： 2,000÷400=5.0 |
| 并发连接数（分钟） | 该小时内最大并发 TCP 连接数为 720,000。 LCU 换算值： 720,000÷100,000=7.2 | 该小时内最大并发 UDP 连接数为 420,000。 LCU 换算值： 420,000÷50,000=8.4 |
| 处理数据量（小时） | 该小时内处理的 TCP 请求和响应的流量数据为 10 GB。 LCU 换算值： 10÷1=10.0 | 该小时处理的 UDP 请求和响应的流量数据为 8 GB。 LCU 换算值： 8÷1=8.0 |


本示例中，TCP监听消耗的最大指标是处理数据量（10.0个LCU），UDP监听消耗的最大指标是并发连接数（8.4个LCU）。

TCP监听每小时LCU费=0.037元/个×10.0个=0.37元 UDP监听每小时LCU费=0.037元/个×8.4个=0.3108元 该NLB实例每小时LCU费=TCP监听每小时LCU费+UDP监听每小时LCU费=0.37元+0.3108元=0.6808元

### 预估LCU消耗

您可以使用[NLB LCU](https://www.aliyun.com/price/product?spm=5176.28047174.J_5718740570.4.54a27e0eIrBfEU#/commodity/slb_nlb_public_cn)[估算器](https://www.aliyun.com/price/product?spm=5176.28047174.J_5718740570.4.54a27e0eIrBfEU#/commodity/slb_nlb_public_cn)来预估LCU的消耗。

## 公网网络费

私网NLB不收取公网网络费用，只有当您购买公网NLB才会收取公网网络费用。

公网NLB通过弹性公网IP（EIP）提供公网能力，选择公网NLB将会收取EIP费用。

说明

NLB仅可绑定暂未加入共享带宽的按量付费（按使用流量计费）的EIP。

更多信息，请参见[按量付费](products/eip/documents/pay-as-you-go.md)。

[上一篇：NLB计费概述](products/slb/documents/network-load-balancer/product-overview/nlb-billing-overview.md)[下一篇：NLB资源包](products/slb/documents/network-load-balancer/product-overview/nlb-resource-plans.md)

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
