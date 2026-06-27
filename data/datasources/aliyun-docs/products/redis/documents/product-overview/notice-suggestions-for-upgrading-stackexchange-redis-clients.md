# 【通知】StackExchange.Redis客户端升级建议-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/notice-suggestions-for-upgrading-stackexchange-redis-clients

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/redis/documents/product-overview.md)

- [快速入门](products/redis/documents/getting-started.md)

- [Tair AI能力](products/redis/documents/tair-ai-ability.md)

- [操作指南](products/redis/documents/user-guide.md)

- [实践教程](products/redis/documents/use-cases.md)

- [安全合规](products/redis/documents/security-compliance.md)

- [开发参考](products/redis/documents/developer-reference.md)

- [服务支持](products/redis/documents/support.md)

- [视频专区](products/redis/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 【通知】StackExchange.Redis客户端升级建议

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

2024年02月，[StackExchange.Redis](https://github.com/StackExchange/StackExchange.Redis)社区修复了一个Bug：在使用StackExchange.Redis客户端访问代理（Proxy）模式的云数据库 Tair（兼容 Redis）实例时，如果使用了多数据库（Database，DB）功能，会出现超时报错。请将StackExchange.Redis升级至2.7.20及以上版本，可解决该问题。

## 详细信息

### 影响范围

当同时满足以下三种情况时，会出现超时报错：

- 

StackExchange.Redis客户端版本低于2.7.20（不包含）。

- 

Tair实例为集群架构代理模式或读写分离架构。

- 

使用多DB功能，即使用了SELECT命令。

### 报错示例

1. StackExchange.Redis.RedisTimeoutException: Timeout performing xxx (5000ms), inst: 0, qu: 0, qs: 0, aw: False, rs: ReadAsync, ws: Idle, in: 0, in-pipe: 0, out-pipe: 0, serverEndpoint: XX.XX.XX.XX:6379, mgr: 10 of 10 available, clientName: 67c80fdab92d, PerfCounterHelperkeyHashSlot: 11235, IOCP: (Busy=0,Free=1000,Min=12,Max=1000), WORKER: (Busy=18,Free=32749,Min=12,Max=32767), v: xx.y.xx.xxx (Please take a look at this article for some common client-side issues that can cause timeouts: https://stackexchange.github.io/StackExchange.Redis/Timeouts) 2. Multiple databases are not supported on this server; cannot switch to database

### 原因描述

开源Redis集群不支持多DB功能，用户在从主备架构变配至集群架构后，无法执行SELECT命令。而云数据库 Tair（兼容 Redis）的代理模式支持多DB功能。通过代理模式，您可以在集群架构、读写分离架构中使用SELECT命令，切换至其他DB。该功能可以帮助您更平滑地从单机版升级至集群架构或读写分离架构，更多信息请参见[Tair Proxy](products/redis/documents/product-overview/features-of-proxy-nodes.md)[特性说明](products/redis/documents/product-overview/features-of-proxy-nodes.md)。

StackExchange.Redis 2.7.20（不包含）之前的版本在识别阿里云Tair的代理节点时，将其识别为Cluster，从而导致SELECT命令无法执行，该问题已经在StackExchange.Redis 2.7.20版本进行了修复。

## 解决方案

将StackExchange.Redis升级至[2.7.20](https://www.nuget.org/packages/StackExchange.Redis/2.7.20)及以上版本。

## 相关文档

- 

[StackExchange/StackExchange.Redis#2642](https://github.com/StackExchange/StackExchange.Redis/issues/2642)

- 

[StackExchange/StackExchange.Redis#2646](https://github.com/StackExchange/StackExchange.Redis/pull/2646)

- 

[Tair Proxy](products/redis/documents/product-overview/features-of-proxy-nodes.md)[特性说明](products/redis/documents/product-overview/features-of-proxy-nodes.md)

- 

[客户端程序连接教程](products/redis/documents/user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance.md)

[上一篇：【降价通知】云数据库 Tair（兼容 Redis）包年包月价格下调](products/redis/documents/product-overview/notice-on-price-reduction-for-apsaradb-for-redis-subscription-instances.md)[下一篇：【通知】Redis开源版2.8版本实例计划停止全面支持（EOFS）](products/redis/documents/product-overview/end-of-full-support-for-redis-2-8.md)

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
