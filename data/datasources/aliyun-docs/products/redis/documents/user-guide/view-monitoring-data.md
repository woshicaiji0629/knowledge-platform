# 查看性能监控以掌握实例运行状况-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/view-monitoring-data

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

# 查看性能监控

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库 Tair（兼容 Redis）性能监控提供了CPU使用率、内存使用率、平均时延、QPS等性能监控指标。您可以查询实例在过去一个月内指定时间段的监控数据，掌握实例的性能与运行状况，排查性能问题。

## 操作步骤

- 

访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏，单击性能监控。

- 

根据实例的架构类型，选择执行下述步骤：

- 

若实例为主备架构：您仅需关注主节点的监控指标即可。

- 

若实例为集群、读写分离架构：

- 

您可以在实例全局中查询集群、读写分离架构实例的整体性能。实例全局的监控指标为各子节点的聚合数据，不同监控指标的聚合方式不同（求平均值、求和等），例如实例全局的CPU使用率为所有子节点CPU使用率的平均值。

- 

您可以在数据节点中查询到各个数据节点的监控指标。

同时，若实例带有Proxy节点，您也可以在实例全局或代理节点中查询Proxy的整体性能或各个Proxy节点的监控指标。

说明

- 

支持查询最近1个月的监控数据，且通常情况下最大查询范围不能超过3天。

- 

为避免对实例的运行产生影响，同时保障性能监控页面中趋势图的展示效果，在选择不同时间范围时，趋势图的数据展示粒度有所不同。

- 

对于读写分离架构实例，聚合监控指标暂不包含只读读节点的监控指标。

## 常见问题

开启读写分离后，为什么只读节点存在写QPS？

只读节点的写QPS并非直接由客户端发起的写请求，而是指主节点同步数据到只读节点时产生的写操作。

集群架构实例的连接数为什么是0？

集群架构的代理模式下，数据节点的连接数显示为0。数据节点的连接数为代理节点到数据节点的连接，此连接复用的，通常只有内部连接，一般平均值计算下来在0~2。客户端连接数需通过代理节点监控界面查看，无需关注数据节点连接数。

## 相关API

| API | 说明 |
| --- | --- |
| [DescribeHistoryMonitorValues](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-describehistorymonitorvalues-redis.md) | 查询实例的历史性能监控信息。 说明 关于 MonitorKeys 参数的说明请参见 [MonitorKeys 参数补充说明](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-describehistorymonitorvalues-redis.md) 。 |


## 相关文档

- 

实例性能问题排查与优化，请参见：

- 

[排查实例](products/redis/documents/user-guide/troubleshoot-high-cpu-utilization-on-an-apsaradb-for-redis-instance.md)[CPU](products/redis/documents/user-guide/troubleshoot-high-cpu-utilization-on-an-apsaradb-for-redis-instance.md)[使用率高的问题](products/redis/documents/user-guide/troubleshoot-high-cpu-utilization-on-an-apsaradb-for-redis-instance.md)

- 

[排查实例内存使用率高的问题](products/redis/documents/user-guide/troubleshoot-the-high-memory-usage-of-an-apsaradb-for-redis-instance.md)

- 

[排查实例流量使用率高的问题](products/redis/documents/user-guide/troubleshoot-high-traffic-usage-on-an-apsaradb-for-redis-instance.md)

- 

[常见](products/redis/documents/user-guide/suggestions-for-handling-common-latency-events.md)[Latency（时延）事件的处理建议](products/redis/documents/user-guide/suggestions-for-handling-common-latency-events.md)

- 

实例性能压测，请参见[性能白皮书](products/redis/documents/support/performance-white-paper.md)。

[上一篇：性能与监控](products/redis/documents/user-guide/performance-monitoring.md)[下一篇：查询性能](products/redis/documents/user-guide/performance-of-queries.md)

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
