# 如何开启、查看、对比日志聚类-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/logreduce

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

# 日志聚类

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍日志聚类功能及其操作，包括开启日志聚类、查看聚类结果和原始日志、对比不同时间段的聚类日志数量等。

## 前提条件

- 

已创建Standard Logstore。具体操作，请参见[创建基础](products/sls/documents/manage-a-logstore.md)[LogStore](products/sls/documents/manage-a-logstore.md)。

- 

已采集日志。具体操作，请参见[数据采集](products/sls/documents/data-collection-overview.md)。

- 

已配置索引。具体操作，请参见[配置索引](products/sls/documents/create-indexes.md)。

## 背景信息

日志服务提供日志聚类功能，支持在采集日志时，将相似度高的日志聚合，提取共同的日志模式（Pattern），快速掌握日志全貌。支持多种格式的文本日志聚合，可应用于DevOps中的问题定位、异常检测、版本回归等运维动作，或应用于安全场景下的入侵检测等。您还可以将聚类结果以分析图表的形式保存在仪表盘中，实时查看聚类数据。

## 功能优势

- 

支持任意格式日志，例如Log4j、JSON、单行等。

- 

亿级数据，秒级输出结果。

- 

日志数据可以按任意模式聚类。

- 

按pattern聚类的数据可以根据pattern的签名反查原始数据。

- 

比较不同时间段的pattern。

- 

动态调整聚类精度。

## 操作视频

## 索引流量

开启日志聚类功能后，索引总量会增加原始日志大小的10%。例如原始数据为100 GB/天，开启该功能后，索引总量增加10 GB。

| 原始日志大小 | 索引比例 | 日志聚类功能产生的索引量 | 索引总量 |
| --- | --- | --- | --- |
| 100 GB | 20%（20 GB） | 100 * 10% | 30 GB |
| 100 GB | 40%（40 GB） | 100 * 10% | 50 GB |
| 100 GB | 100%（100 GB） | 100 * 10% | 110 GB |


## 开启日志聚类功能

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在日志存储>日志库页签中，单击目标Logstore。

- 

开启日志聚类功能。

- 

单击查询分析属性>属性。

如果您还未开启索引，请单击开启索引。

- 

在查询分析面板中，打开日志聚类开关。

- 

可选：设置聚类字段的白名单和黑名单。

说明

不支持同时设置黑白名单。

| 聚类字段过滤 | 说明 |
| --- | --- |
| 白名单 | 设置了白名单后，日志服务将根据白名单中的字段进行日志聚类。 |
| 黑名单 | 设置了黑名单后，日志服务不会对黑名单中的字段进行日志聚类。 |
| 未设置黑白名单 | 未设置黑白名单时，日志服务将根据聚类规则对所有的字段进行日志聚类。 |


- 

单击确定。

## 查看聚类结果和原始日志

- 

在查询分析页面，输入查询语句，设置查询时间范围，然后单击查询 / 分析。

说明

此处仅支持输入查询语句来过滤日志，但不支持分析语句，即不能对分析结果进行日志聚类。

- 

单击日志聚类页签，查看聚类结果。

您还可以单击添加到仪表盘，将聚类结果保存到仪表盘。

聚类结果页面提供Pattern 分类滑块（可左右拖动调整聚类粒度，从多到少）、复制查询语句按钮和Log Compare按钮。

| 参数 | 说明 |
| --- | --- |
| Number | 聚类序号。 |
| Count | 当前指定的查询时间段内，某 Pattern 对应的日志条数。 |
| Pattern | 某类日志的具体模式，每个聚类会有一个或多个子 Pattern。 |


- 

鼠标指向Count列的数字，在悬浮框展示当前聚类的子Pattern及每个子Pattern的占比。单击数字前的加号（+），展开子Pattern列表。

- 

单击Count列的数字，跳转到原始日志页签，查看对应pattern的原始日志。

## 调整聚类精度

在日志聚类页签中，拖拽Pattern分类中的滑动条，调整聚类的精度。

- 

聚类偏向于多，表示聚类结果分类细，Pattern细节被保留的多。

- 

聚类偏向于少，表示聚类结果分类粗，Pattern细节被隐藏的多。

## 对比不同时间段的聚类日志数量

- 

在日志聚类页签中，单击Log Compare。

- 

设置对比时间，单击确定。

例如：在执行查询操作时，时间范围选择为15分钟。在Log Compare中，选择1天，则自动显示开始时间和结束时间，时间范围为1天前的15分钟。

| 参数 | 说明 |
| --- | --- |
| Number | 聚类编号。 |
| Pre_Count | 在 Log Compare 中设置的时间段内，该 Pattern 对应的日志数量。 |
| Count | 当前指定的查询时间段内，某模式对应的日志条数。 |
| Diff | 某模式在两个时段的日志数量差值及升降百分比。 |
| Pattern | 某类日志的具体模式。 |


## SQL示例

日志服务还支持通过执行查询分析语句获取日志聚类结果。

- 

获取日志聚类结果

- 

查询分析语句

* | select a.pattern, a.count,a.signature, a.origin_signatures from (select log_reduce(3) as a from log) limit 1000

说明

查看聚类结果时，您可以单击复制查询语句获取日志聚类结果所对应的查询分析语句。

- 

修改参数

修改查询分析语句中的log_reduce(precision)，precision代表聚类精度，取值范围1~16，数字越小，聚类精度越高，生成的模式格式越多，默认为3。

- 

返回字段

在统计图表页签中返回日志聚类详细信息。

| 参数 | 说明 |
| --- | --- |
| pattern | 某类日志的具体模式。 |
| count | 当前指定的查询时间段内，某模式对应的日志条数。 |
| signature | 某模式的签名。 |
| origin_signatures | 某模式的二级签名，可以通过二级签名，反查原始数据。 |


- 

对比不同时间段日志聚类结果

- 

查询分析语句

* | select v.pattern, v.signature, v.count, v.count_compare, v.diff from (select compare_log_reduce(3, 86400) as v from log) order by v.diff desc limit 1000

说明

Log Compare对比不同时间段日志聚类结果后，您可以单击复制查询语句获取对应的查询分析语句。

- 

修改参数

修改查询分析语句中的compare_log_reduce(precision, compare_interval)。

- 

precision代表聚类精度，取值范围1~16，数字越小，聚类精度越高，生成的模式格式越多，默认为3。

- 

compare_interval表示对比N秒之前某一时间段的日志，正整数。

- 

返回字段

| 参数 | 说明 |
| --- | --- |
| pattern | 某类日志的具体模式。 |
| count_compare | 在前一时间段内，某模式对应的日志数量。 |
| count | 当前指定的查询时间段内，某模式对应的日志条数。 |
| diff | count 和 count_compare 的差值。 |
| signature | 某模式的签名。 |


## 关闭日志聚类功能

如果您不再需要使用日志聚类功能，可关闭该功能。

- 

在查询分析页面，单击查询分析属性>属性。

- 

关闭日志聚类开关。

- 

单击确定。

[上一篇：LiveTail](products/sls/documents/livetail.md)[下一篇：新版日志聚类](products/sls/documents/new-version-of-log-clustering.md)

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
