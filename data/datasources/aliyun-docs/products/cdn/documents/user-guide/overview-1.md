# 实时投递CDN日志进行分析-实时日志-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/user-guide/overview-1

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

# 什么是实时日志

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在使用CDN访问资源时，会产生大量的日志数据。阿里云CDN通过与日志服务（SLS）融合，将这些日志实时推送至SLS进行分析。通过实时日志分析，您可以快速发现和定位问题，提高数据决策能力。

## 功能介绍

使用CDN服务时，会产生大量的网络日志数据。通过实时日志功能，您可以实时采集并投递节点日志到日志服务，以便快速监控和定位业务问题。开启实时日志并成功投递后，计费将根据日志投递条数计算。

如需深入了解日志服务，请参见[什么是日志服务](products/sls/documents/what-is-log-service.md)。

## 注意事项

通过CDN/DCDN控制台（或者OpenAPI）的监控查询、用量查询（实际计费流量）功能查到的加速域名使用的流量数据与通过日志统计的流量数据有差异。通常来说，通过监控查询、用量查询功能查到的加速域名使用的流量数据是通过日志统计的流量数据的1.1倍，详细请参见[为什么监控查询流量、用量查询流量与日志统计流量有差异](products/cdn/documents/product-overview/traffic-amount-in-the-monitoring-and-usage-analytics-or-in-the-usage-statistics-feature-different-from-the-logged-traffic-amount.md)。

## CDN提供的实时日志与离线日志服务的区别

- 

日志延迟

CDN实时日志为实时采集的日志数据，日志数据延迟不超过3分钟，而离线日志的数据延迟通常在24小时之内。

- 

日志分析

CDN实时日志打通了SLS日志服务的日志转存和日志分析能力，预制了CDN基础数据、CDN错误分析、CDN热门资源、CDN用户分析这四张常用分析报表，也支持自定义日志分析策略，可以一站式提供日志存储和日志分析能力，而离线日志目前只支持日志转存到OSS云存储，尚未打通日志分析能力。

## 实时日志服务的优势

- 

日志延迟小

日志数据延迟不超过3分钟，可以帮助您快速对访问日志进行分析，及时发现问题并做出应对决策。

- 

一站式服务

传统的离线日志分析模式，需要用户将日志下载，再重新上传至数据仓库，然后在数据仓库进行一系列的清洗和数据模型定义，这一系列操作处理完以后才能进行数据分析，整个过程需要的人力较多，时间较长；CDN实时日志打通了SLS日志服务的日志转存和日志分析能力，免去传统模式下繁琐的离线日志分析流程。

## 计费详情

您需要按照实时日志推送成功条数进行付费（CDN产品收取），该费用不包含日志的存储和分析相关费用。

实时日志推送成功之后，您需要支付的服务费用包含：

- 

CDN节点实时日志推送产生费用，该部分由CDN产品收取。关于CDN收费标准，请参见[增值服务计费-实时日志投递](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.10.1b444ee22Dxy8y#/cdn/detail)。

- 

实时日志的存储和分析相关费用，该部分由日志服务SLS产品收取。详细信息，请参见[产品定价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.11.66cd2aab6wAn6p#/sls/detail)。

| 计费项名称 | 计费规则 | 付费方式 | 计费周期 |
| --- | --- | --- | --- |
| 实时日志投递条数。 | 开启实时日志，并成功投递日志后，会产生日志投递费。 | 按量后付费。 | 以天为周期进行结算，出账会存在 3~4 个小时的延迟。 |


## 适用场景

实时日志可以帮助您分析加速域名遇到的异常问题，也可以帮助您了解用户的访问情况。当前阿里云CDN提供4类日志数据报表，如下表所示。

| 日志分析场景 | 报表作用描述 |
| --- | --- |
| CDN 基础数据 | 该数据可以帮助您快速了解到 CDN 整体的服务质量以及终端用户的访问效率（命中率、访问延时、下载速度等），同时也可以在服务质量出现异常情况下及时进行处理。 |
| CDN 访问错误 | 该数据可以帮助您在应用访问出现异常时，快速定位到 CDN 服务问题的源头，例如：部分 URI 问题、源站出现故障、部分节点不可用、部分省份网络问题、部分运营商网络问题等。 |
| CDN 热门资源 | 该数据可以帮助您更好地了解热门资源情况，分析出热门域名、热门 URI、热门省份、热门运营商等，您也可以从热门数据了解到您的运营活动效果是否正常、热点时间内流量的上涨是否符合预期，以帮助您及时调整运营策略。 |
| CDN 用户构成 | 该数据可以帮助您更好地了解网站的用户构成，包括用户的客户端类型、省份、运营商等，也能够统计出访问量 TOP 用户、下载量 TOP 用户。 |


如果您想开通实时日志推送服务，请参见[配置实时日志推送](products/cdn/documents/user-guide/configure-real-time-log-delivery.md)。

开通后，您可以通过[投递](products/cdn/documents/user-guide/best-practices-for-shipping-and-analyzing-alibaba-cloud-cdn-real-time-logs-in-log-service.md)[CDN](products/cdn/documents/user-guide/best-practices-for-shipping-and-analyzing-alibaba-cloud-cdn-real-time-logs-in-log-service.md)[实时日志到](products/cdn/documents/user-guide/best-practices-for-shipping-and-analyzing-alibaba-cloud-cdn-real-time-logs-in-log-service.md)[SLS](products/cdn/documents/user-guide/best-practices-for-shipping-and-analyzing-alibaba-cloud-cdn-real-time-logs-in-log-service.md)[来分析用户访问数据](products/cdn/documents/user-guide/best-practices-for-shipping-and-analyzing-alibaba-cloud-cdn-real-time-logs-in-log-service.md)来了解如何使用日志分析模块及实现常见的用户访问数据分析。

[上一篇：实时日志](products/cdn/documents/user-guide/real-time-logs.md)[下一篇：配置实时日志推送](products/cdn/documents/user-guide/configure-real-time-log-delivery.md)

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
