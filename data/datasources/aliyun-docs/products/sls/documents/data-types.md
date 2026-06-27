# 索引数据的类型-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/data-types

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

# 数据类型

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您在创建索引时，可将字段的数据类型设置为text、long、double或JSON。本文介绍各个数据类型的配置示例及注意事项。

## 数据类型概述

在[创建索引](products/sls/documents/create-indexes.md)时，推荐使用控制台方式创建索引，日志服务会根据采集时预览数据中的第一条内容，自动生成字段索引，同时也支持自定义字段索引。

日志服务提供如下数据类型，请按情况进行选择：

- 

text、long、double类型：

- 

如果您要查询和分析字符串类型的字段，需在配置索引时，将字段的数据类型设置为text，并开启统计功能。

说明

text、long 和 double 类型的字段均可独立开启统计功能。只有开启统计功能后，该字段才能用于 SQL 查询中的 WHERE 条件过滤、聚合分析（SELECT/GROUP BY）以及可视化展示。若未开启统计，字段在 SQL 查询分析中可能无法提取或返回 null。

在控制台键值索引属性配置界面中，每个字段行均有一个开启统计开关，text/long/double 三种类型均可独立开启，不随字段类型变化而隐藏。

- 

只有字段的数据类型为long或double时，您才能通过数值范围查询该字段的值，但不支持使用星号（*）或半角问号（?）进行模糊查询。

- 

如果日志字段的值为整数类型，请将字段的数据类型设置为long。

- 

如果日志字段的值为浮点数类型，请将字段的数据类型设置double，否则无法查询该字段。

- 

如果设置数据类型为long或double，而实际字段值为字符串类型，则无法查询该字段。

重要

如果字段的值为非法的数值，则使用not key > -1000000语句进行查询，表示查询所有有效数值之外的日志，其中-1000000为足够小的值即可。

- 

JSON类型：字段的值为JSON类型，您可在配置索引时，将字段的数据类型设置为JSON。

- 

针对JSON对象中的字段，您可根据其值，将数据类型设置为long、double或text，并开启统计功能。开启统计功能后，日志服务支持您查询和分析JSON对象中的字段。

通过选中对Json内所有文本字段自动索引，可实现JSON对象中的所有文本字段自动创建索引。创建索引后，将产生索引流量。

- 

针对非完全合法的JSON数据，日志服务支持解析合法部分。

例如以下为非完整的JSON日志，日志服务可正确解析content.remote_addr字段、content.request.request_length字段和content.request.request_method字段。

content: { remote_addr:"192.0.2.0" request: { request_length:"73" request_method:"GE

重要

- 

日志服务支持JSON对象中的叶子节点建立索引，但不支持包含叶子节点的子节点建立索引。

- 

日志服务不支持值为JSON数组的字段建立索引，也不支持JSON数组中的字段建立索引。

- 

如果字段的值为Boolean类型，则您可以在建立索引时，将字段的数据类型设置为text。

- 

查询和分析语句格式为查询语句|分析语句。在分析语句中，您必须使用双引号（""）包裹字段名称，使用单引号（''）包裹字符串。

- 

更多参考信息

- 

关于查询和分析JSON日志的更多操作场景和常见问题，包括设置索引、查询和分析具有索引的JSON字段、使用JSON函数、分析JSON数组等，请参见[查询和分析](products/sls/documents/faq-about-the-query-and-analysis-of-json-logs.md)[JSON](products/sls/documents/faq-about-the-query-and-analysis-of-json-logs.md)[日志的常见问题](products/sls/documents/faq-about-the-query-and-analysis-of-json-logs.md)。

- 

查询和分析JSON日志相关的基础配置和基本用法，请参见[查询和分析](products/sls/documents/query-and-analyze-json-logs.md)[JSON](products/sls/documents/query-and-analyze-json-logs.md)[日志](products/sls/documents/query-and-analyze-json-logs.md)。

- 

在查询和分析JSON日志时，如果数据量比较小，您可以不对JSON叶子节点建立字段索引，而是使用JSON函数进行查询和分析。另外，针对一些特殊情况，只能使用JSON函数进行查询与分析。相关案例，请参见[何时使用](products/sls/documents/faq-about-the-query-and-analysis-of-json-logs.md)[JSON](products/sls/documents/faq-about-the-query-and-analysis-of-json-logs.md)[函数](products/sls/documents/faq-about-the-query-and-analysis-of-json-logs.md)。关于JSON函数的完整介绍和案例，请参见[JSON](products/sls/documents/json-functions.md)[函数](products/sls/documents/json-functions.md)。

## 操作步骤

- 

在[创建索引](products/sls/documents/create-indexes.md)中按照控制台方式进行索引创建。

- 

在配置索引中选择对应的索引类型。

## text、long、double类型

- 

日志样例

- 

配置索引

- 

查询和分析语句示例

- 

查询请求时间大于60秒的日志：request_time > 60。

- 

查询请求时间大于等于60秒，并且小于200秒的日志：request_time in [60 200)或者request_time >= 60 and request_time < 200。

- 

查询请求状态码为200的日志：status = 200。

- 

查询非GET请求的日志：not request_method : GET。

- 

查询以cn开头的日志：cn*。

- 

统计客户端分布情况：* | SELECT ip_to_province(client_ip) as province, count(*) AS pv GROUP BY province ORDER BY pv。

## JSON类型

- 

日志样例

JSON日志样例如下所示，除日志服务保留字段外，还包括class字段、latency字段、status字段和info字段。其中info字段的值是JSON对象，并存在多层嵌套。

- 

配置索引

相关说明如下：

- 

IP字段和data字段的值为JSON数组，所以您无法为IP字段和data字段建立索引，也无法通过这两个字段进行查询和分析。

- 

region字段和CreateTime字段在JSON数组中，所以您无法为region字段和CreateTime字段建立索引，也无法通过这两个字段进行查询和分析。

- 

查询和分析语句示例

- 

查询usedTime字段的值大于60秒的日志：info.usedTime > 60。

- 

查询success字段的值为true的日志：info.success : true。

- 

查询usedTime字段的值大于60秒且projectName的值不为project01的日志：info.usedTime > 60 not info.param.projectName : project01。

- 

计算获取Project信息的平均时长：methodName = getProjectInfo | SELECT avg("info.usedTime") AS avg_time。

在配置索引时，请注意以下规则：

- 

全文索引属性和键值索引属性必须至少启用一种。

- 

字段索引配置会覆盖全文索引中同名字段的设置。例如，全文索引中已对某个字段进行分词检索，如果在键值索引中对该字段单独配置了类型和属性，则以键值索引中的配置为准。

- 

索引类型为 long/double 时，大小写敏感和分词符属性无效。

- 

目前只支持缩短索引保存时间。

- 

索引配置修改（包括新增字段、修改类型、开启统计/查询开关等）后约 1 分钟生效，但仅对索引生效后写入的新数据可查询。如需查询历史数据，需对历史数据执行重建索引操作。具体操作请参见[重建索引](products/sls/documents/reindex-logs-for-a-logstore.md)。

- 

重建索引仅支持最近 30 天且至少 15 分钟前的数据。

[上一篇：创建索引](products/sls/documents/create-indexes.md)[下一篇：重建索引](products/sls/documents/reindex-logs-for-a-logstore.md)

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
