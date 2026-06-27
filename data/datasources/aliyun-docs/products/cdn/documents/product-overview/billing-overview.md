# CDN如何计费-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/product-overview/billing-overview

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/cdn/documents/product-overview.md)

- [快速入门](products/cdn/documents/getting-started.md)

- [操作指南](products/cdn/documents/user-guide.md)

- [实践教程](products/cdn/documents/use-cases.md)

- [安全合规](products/cdn/documents/security-and-compliance.md)

- [开发参考](products/cdn/documents/developer-reference.md)

- [服务支持](products/cdn/documents/support.md)

- [视频专区](products/cdn/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 计费概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

通过阅读本文，您可以快速了解阿里云CDN的付费方式、计费组成和定价等计费信息。

重要

- 

CDN所有计费方式均按照账户UID维度进行统计收费。

- 

无特别说明的情况下，CDN的按流量计费、按带宽峰值计费和月结95带宽峰值计费，都是指在CDN的L1节点上产生的下行流量带宽。

- 

在CDN控制台添加的且“业务类型”为全站加速的加速域名，将根据全站加速产品的价格计费。您可以前往[全站加速控制台](https://dcdn.console.aliyun.com)查看和使用这些域名。

- 

CDN可与全站加速共享下行流量资源包、静态HTTPS请求数包和边缘WAF请求数包。

- 

CDN产品出账存在3~4小时延迟。

- 

CDN和全站加速（DCDN）的加速域名独立管理，同一个域名不会同时存在于CDN和DCDN中，两个产品各自按实际用量独立计费，不存在重复计费。

## 快速选择付费方式

CDN支持按量付费（默认）和资源包（针对常用付费服务）两种付费方式，根据业务流量特征，可参考下表快速选择付费方式。

- 

- 

| 业务流量是否稳定？ | 付费方式 | 优势 | 说明 | 定价详情 |
| --- | --- | --- | --- | --- |
| 波动较大 ，有明显波峰波谷或无法预估 | 按量付费（后付费） | 按实际使用量结算，用多少付多少，灵活应对业务变化。 | 按照各计费项的实际用量结算费用， 先使用，后付费 。 | 阿里云 CDN 各计费项价格：可参见 [按流量计费](products/cdn/documents/product-overview/billing-rules-of-basic-services.md) 。 |
| 相对稳定 ，可预估月度用量 | 资源包（预付费） | 价格比按量付费更优惠，适合成本可控的业务。 | 预先购买针对不同的计费项推出的优惠资源包，在费用结算时，优先从资源包抵扣用量， 先购买，后抵扣 。 超出资源包抵扣额度的用量将计入按量计费，会产生后付费账单，请根据您的所需服务、业务量，购买适合业务额度的资源包。关于资源包的介绍、选购和抵扣规则等，请参见 [资源包介绍](products/cdn/documents/product-overview/resource-plan-overview.md) 、 [资源包选购](products/cdn/documents/product-overview/guidelines-for-choosing-resource-plans.md) 和 [资源包抵扣规则](products/cdn/documents/product-overview/rules-for-applying-resource-plans.md) 。 | 资源包定价：可参见 [资源包定价](https://common-buy.aliyun.com/?spm=5176.7933777.J_3537169050.2.2429496ezmVFeY&commodityCode=dcdnpaybag#/buy) 。 |


## 计费组成

CDN计费分为，基础服务计费（必选）+增值服务计费（可选），计费项组成如下图：

- 

[基础服务计费](products/cdn/documents/product-overview/billing-rules-of-basic-services.md)（必选）：CDN加速产生的核心费用。基础服务费需要在按流量计费和按带宽峰值计费和月结95带宽峰值计费中选择一种，默认为按流量计费。

- 

[增值服务计费](products/cdn/documents/product-overview/billing-of-value-added-services.md)（可选，单独计费）：如使用了静态HTTPS请求、实时日志投递等高级功能，会产生相应的额外费用。

## 核心计费概念

### 下行流量与回源流量

- 

下行流量（计费）：指用户通过浏览器或客户端访问业务时，从CDN边缘节点下载数据所产生的流量。这是CDN基础服务费的主要计费内容。

- 

回源流量（不计费）：指CDN边缘节点因未缓存或缓存过期，返回源站（如ECS、OSS）拉取数据时产生的流量。这部分流量不计入CDN的计费，但源站可能会因此产生出方向流量费用。

### 计费区域

系统会根据访问用户的IP地址判断其所属区域，并按该区域的单价进行计费。

阿里云CDN在全球各计费大区均部署了节点，可根据访问者IP地址进行精准的区域计费。各计费大区覆盖的国家和地区详情，请参见[节点分布](products/cdn/documents/product-overview/pop-distribution.md)。

| 计费区域 | 英文缩写 | 覆盖区域 |
| --- | --- | --- |
| 中国内地 | CN | 中国内地 |
| 北美 | NA | 美国 |
| 欧洲 | EU | 乌克兰、英国、法国、荷兰、意大利、瑞典、德国、西班牙 |
| 亚太 1 区 | AP1 | 中国香港、日本、新加坡、泰国、菲律宾、马来西亚 |
| 亚太 2 区 | AP2 | 印度尼西亚、印度、韩国、巴基斯坦 |
| 亚太 3 区 | AP3 | 澳大利亚 |
| 中东/非洲 | MEAA | 土耳其、阿联酋、科威特、卡塔尔、阿曼、尼日利亚、南非 |
| 南美 | SA | 巴西 |


### 计费周期

CDN服务的计费周期如下：

- 

- 

- 

- 

| 计费周期 | 扣费及出账时间 | 适用的计费项 |  |
| --- | --- | --- | --- |
| 小时 | 按小时结算，账单出账时间通常在当前计费周期结束后 3~4 小时左右，具体以系统实际出账时间为准。 | 基础服务 | [按流量计费](products/cdn/documents/product-overview/billing-rules-of-basic-services.md) |
| 增值服务 | [静态](products/cdn/documents/product-overview/billing-of-https-requests-for-static-content.md) [HTTPS](products/cdn/documents/product-overview/billing-of-https-requests-for-static-content.md) [请求数](products/cdn/documents/product-overview/billing-of-https-requests-for-static-content.md) [静态](products/cdn/documents/product-overview/billing-of-quic-requests-for-static-content.md) [QUIC](products/cdn/documents/product-overview/billing-of-quic-requests-for-static-content.md) [请求数](products/cdn/documents/product-overview/billing-of-quic-requests-for-static-content.md) [CDN WAF](products/cdn/documents/product-overview/alibaba-cloud-cdn-waf-requests.md) [请求数](products/cdn/documents/product-overview/alibaba-cloud-cdn-waf-requests.md) [实时日志投递](products/cdn/documents/product-overview/billing-of-real-time-log-delivery.md) |  |  |
| 日 | 按日计费，每日凌晨 4 点左右出前一日账单并扣费，具体出账时间以系统为准。 | 基础服务 | [按带宽峰值计费](products/cdn/documents/product-overview/billing-rules-of-basic-services.md) |
| 月 | 当前计费周期结束的下个自然月 1 日凌晨 4 点左右。 | 基础服务 | [月结](products/cdn/documents/product-overview/billing-rules-of-basic-services.md) [95](products/cdn/documents/product-overview/billing-rules-of-basic-services.md) [带宽峰值计费](products/cdn/documents/product-overview/billing-rules-of-basic-services.md) |


## 视频讲解

## 相关文档

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

| 选择加速服务计费方式 | [基础服务计费](products/cdn/documents/product-overview/billing-rules-of-basic-services.md) [增值服务计费](products/cdn/documents/product-overview/billing-of-value-added-services.md) [变更计费方式](products/cdn/documents/product-overview/change-the-metering-method.md) [CDN](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.10.1b444ee22Dxy8y#/cdn/detail/cdn) [定价详情](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.10.1b444ee22Dxy8y#/cdn/detail/cdn) |
| --- | --- |
| 资源包 | [资源包选购](products/cdn/documents/product-overview/guidelines-for-choosing-resource-plans.md) [资源包抵扣规则](products/cdn/documents/product-overview/rules-for-applying-resource-plans.md) [查询资源包明细](products/cdn/documents/product-overview/query-the-details-of-resource-plans-1.md) [设置资源包预警](products/cdn/documents/product-overview/configure-low-capacity-alerts.md) [退款说明](products/cdn/documents/product-overview/money-back-guarantees.md) |
| 更多参考 | [欠费说明](products/cdn/documents/product-overview/overdue-payments.md) [用量概述](products/cdn/documents/user-guide/resource-usage-overview.md) [账单查询](products/cdn/documents/product-overview/query-bills.md) [高额账单风险警示](products/cdn/documents/product-overview/configure-high-bill-alerts.md) [计费常见问题](products/cdn/documents/product-overview/faq-about-billing.md) |


[上一篇：产品计费](products/cdn/documents/product-overview/billing.md)[下一篇：基础服务计费](products/cdn/documents/product-overview/billing-rules-of-basic-services.md)

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
