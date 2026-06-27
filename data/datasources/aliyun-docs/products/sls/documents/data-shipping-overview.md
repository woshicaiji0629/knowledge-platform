# 数据投递功能的概念、功能优势、应用场景、计费规则、投递目标等信息-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/data-shipping-overview

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 数据投递概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

日志服务提供投递功能，支持通过控制台将数据实时投递至OSS、MaxCompute等阿里云产品。本文介绍数据投递功能的概念、功能优势、应用场景、计费规则、投递目标等信息。

## 数据投递

数据投递是指将日志服务采集的数据通过控制台投递至其他阿里云产品，便于您存储数据或联合其他系统消费数据。启用数据投递后，日志服务将定时将采集到的数据投递至对应的云产品。

## 应用场景

数据投递适用于数据存储、离线分析等场景。数据投递的实时性较弱，通常为5分钟~30分钟。数据存储时间依赖于存储系统。

## 功能优势

数据投递具有以下优势：

- 

操作简易

您只需要在控制台上完成简单的配置，即可将日志服务的数据投递到OSS等云产品。

- 

数据集中

日志服务已完成不同机器上的数据集中化，您只需将采集到的数据投递到OSS等云产品。

- 

分类管理

您可以利用日志服务的数据分类管理功能，将不同项目、不同类型的数据投递到不同的OSS Bucket、MaxCompute表等云产品目标中。

## 计费规则

- 

若涉及的LogStore的计费模式为按写入数据量计费模式，数据投递将不产生费用。具体内容，可参见[按写入数据量计费](products/sls/documents/billing-per-amount-of-data-written.md)。

- 

若涉及的LogStore的计费模式为按功能付费模式，数据投递涉及多个计费项，包括读写流量、数据投递费用、请求费用等。更多信息，请参见[按使用功能计费模式计费项](products/sls/documents/billable-items.md)。

## 投递目标

日志服务支持的数据投递目标如下表所示。

- 

- 

| 目标 | 说明 |
| --- | --- |
| 对象存储 OSS | 日志服务支持将数据投递至对象存储 OSS。 更多信息，请参见 [投递日志到](products/sls/documents/ship-log-data-from-log-service-to-oss.md) [OSS（旧版）](products/sls/documents/ship-log-data-from-log-service-to-oss.md) 、 [投递日志到](products/sls/documents/create-oss-shipping-tasks-new-version.md) [OSS（新版）](products/sls/documents/create-oss-shipping-tasks-new-version.md) 。 |
| MaxCompute | 日志服务支持通过以下方式将数据投递至 MaxCompute。 日志服务 通过日志服务投递至 MaxCompute。具体操作，请参见 [投递日志到](products/sls/documents/ship-logs-to-maxcompute.md) [MaxCompute（旧版）](products/sls/documents/ship-logs-to-maxcompute.md) 、 [投递日志到](products/sls/documents/create-a-maxcompute-logship-task-new-version.md) [MaxCompute（新版）](products/sls/documents/create-a-maxcompute-logship-task-new-version.md) 。 DataWorks 通过 DataWorks 数据集成投递至 MaxCompute。具体操作，请参见 [通过数据集成投递日志服务数据](https://help.aliyun.com/zh/dataworks/user-guide/use-data-integration-to-synchronize-data-from-loghub-to-a-destination#task-2353708) 。 |
| 云原生数据仓库 AnalyticDB MySQL 版 | 日志服务支持将数据投递至云原生数据仓库 AnalyticDB MySQL 版。具体操作，请参见 [将日志服务数据投递到](products/sls/documents/ship-logs-to-analyticdb-for-mysql.md) [AnalyticDB MySQL](products/sls/documents/ship-logs-to-analyticdb-for-mysql.md) 。 |
| 表格存储 TableStore | 日志服务支持通过表格存储的传送服务将数据拉取至表格存储 TableStore。具体操作，请参见 [通过传送服务投递日志服务数据](https://help.aliyun.com/zh/tablestore/overview-7#concept-urh-1tt-lgb) 。 |


[上一篇：数据投递](products/sls/documents/data-shipping.md)[下一篇：投递日志到OSS（旧版）](products/sls/documents/ship-logs-to-oss.md)

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
