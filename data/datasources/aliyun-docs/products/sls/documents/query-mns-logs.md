# 如何实时查询轻量消息队列（原 MNS）推送的常用场景及操作步骤-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/query-mns-logs

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

# 查询轻量消息队列（原MNS）日志

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

轻量消息队列（原 MNS）日志推送到日志服务后，可进行实时查询，本文介绍实时查询的常用场景及操作步骤，您也可以通过多个关键字组合方式实现更加复杂的查询。

## 前提条件

- 

已采集轻量消息队列（原 MNS）日志。具体操作，请参见[轻量消息队列（原 MNS）日志](products/sls/documents/mns-operations-logs-usage-notes.md)。

- 

已配置索引。具体操作，请参见[创建索引](products/sls/documents/create-indexes.md)。

## 背景信息

轻量消息队列（原 MNS）日志包括队列消息操作日志和主题消息操作日志，日志内容包含消息生命周期的所有信息，例如时间、客户端、操作等。您可以通过实时查询、实时计算和离线计算三种方式对日志进行分析计算。

- 

实时查询：在日志服务控制台上进行实时查询，例如：查询消息轨迹、写入量、删除量等。

- 

实时计算：使用Spark、Storm、StreamCompute、Consumer Library等方式对轻量消息队列（原 MNS）日志进行实时计算。例如：计算某个队列中，Top 10消息的产生者和消费者；计算生产和消费的速度，确认是否均衡；计算某些消费者的处理延时，确认是否存在瓶颈等。

- 

离线计算：使用MaxCompute、E-MapReduce、Hive进行长时间跨度的计算，例如：计算最近一周内消息从发布到被消费的平均延迟。

## 查询队列消息的消息轨迹

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在日志存储>日志库页签中，单击目标Logstore。

- 

输入查询语句，然后单击最近15分钟，设置查询的时间范围。

本案例要查询队列消息的消息轨迹，即输入队列名称和消息ID，格式为$QueueName and $MessageId，例如log and EED287A265726135146E6A9CADC880FA。

查询结果记录了某条消息从发送到接收的过程。查询结果显示两条 MNSLogging 日志记录，MessageId 均为EED287A265726135146E6A9CADC880FA。其中一条记录的 Action 为SendMessage（时间 2020-10-21 16:50:53），另一条的 Action 为ReceiveMessage（时间 2020-10-21 16:50:57），表明该消息在队列sgw-express-sync-queue-gw-0008q1m4pv7qjse4na31-5796中完成了发送和接收的完整轨迹。

## 查询队列消息发送量

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在日志存储>日志库页签中，单击目标Logstore。

- 

输入查询语句，然后单击最近15分钟，设置查询的时间范围。

本案例要查询队列消息发送量，即输入队列名称和发送操作，查询语句格式为$QueueName and (SendMessage or BatchSendMessage)，例如log and (SendMessage or BatchSendMessage)。

查询结果显示，当前查询时段内，生产者向log队列发送了3条队列消息。执行该查询语句后，查询结果显示结果精确，日志条数为 3。每条日志记录包含Action（如SendMessage，红色高亮）、QueueName、Time、MessageId、RequestId、RemoteAddress等字段信息。

## 查询队列消息消费量

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在日志存储>日志库页签中，单击目标Logstore。

- 

输入查询语句，然后单击最近15分钟，设置查询的时间范围。

本案例要查询队列消息消费量，即输入队列名称和消费操作，查询语句格式为$QueueName and (ReceiveMessage or BatchReceiveMessage)，例如log and (ReceiveMessage or BatchReceiveMessage)。

查询结果显示，当前查询时段内，log队列中有12条消息被消费。执行查询后，查询结果显示共 12 条日志记录。每条原始日志包含Action（如ReceiveMessage）、QueueName（如log）、MessageId、RequestId、NextVisibleTime、ProcessTime、RemoteAddress等字段信息。

## 查询队列消息删除量

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在日志存储>日志库页签中，单击目标Logstore。

- 

输入查询语句，然后单击最近15分钟，设置查询的时间范围。

本案例要查询队列消息删除量，即输入队列名称和删除操作，查询语句格式为$QueueName and (DeleteMessage or BatchDeleteMessage)，例如log and (DeleteMessage or BatchDeleteMessage)。

当前查询时段内，61条log队列消息被删除。执行查询后，在查询结果区域查看日志条数，该数值即为队列消息删除量。

## 查询主题消息的消息轨迹

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在日志存储>日志库页签中，单击目标Logstore。

- 

输入查询语句，然后单击最近15分钟，设置查询的时间范围。

本案例要查询主题消息的消息轨迹，即输入主题名称和MessageId，查询语句格式为$TopicName and $MessageId，例如logtest and 8798453B65727FC6433E6AB4F746D4CE。

查询结果如下所示，记录了某条消息从发送到通知的过程。查询结果返回两条日志记录，其中 Action 字段分别为 PublishMessage 和 Notify，表示同一消息先被发布再被推送通知。

1 10-21 17:17:24 ... MNSLogging 1603271947 ProcessTime :1 TopicName :logtest Time :2020-10-21 17:17:24.679000 AccountId :xxx Action :PublishMessage MessageId :8798453B65727FC6433E6AB4F746D4CE RequestId :5F8FFCA4453241C3099B4BC9 RemoteAddress :xxx MessageTag : 1 10-21 17:17:24 ... MNSLogging 1603271947 ProcessTime :1 TopicName :logtest Time :2020-10-21 17:17:24.679000 AccountId :xxx Action : Notify MessageId :8798453B65727FC6433E6AB4F746D4CE RequestId :5F8FFCA4453241C3099B4BC9 RemoteAddress :xxx MessageTag :

## 查询主题消息发布量

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在日志存储>日志库页签中，单击目标Logstore。

- 

输入查询语句，然后单击最近15分钟，设置查询的时间范围。

本案例要查询主题消息发布量，即输入主题名称和发布操作，查询语句格式为$TopicName and PublishMessage，例如logtest and PublishMessage。

查询结果显示，当前查询时段内，生产者向logtest主题发布了3条消息。执行查询后，返回3条精确匹配的日志记录，日志详情中包含TopicName（值为 logtest）、Action（值为 PublishMessage）、MessageId、RequestId、RemoteAddress等字段信息。

## 查询某个客户端消息处理量

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在日志存储>日志库页签中，单击目标Logstore。

- 

输入查询语句，然后单击最近15分钟，设置查询的时间范围。

本案例要查询某个客户端消息处理量，即输入客户端IP地址，查询语句格式为$ClientIP，例如10.10.10.0。

如果您要查询某个客户端的某类操作日志，可使用多个关键字组合方式，例如$ClientIP and (SendMessage or BatchSendMessage)。

查询结果如下图所示，当前查询时段内，该客户端处理了66条消息。

[上一篇：关联LogStore与OSS外表进行查询和分析](products/sls/documents/associate-a-logstore-with-an-oss-external-table-to-perform-query-and-analysis.md)[下一篇：采集和查询分析Nginx监控日志](products/sls/documents/collect-and-analyze-nginx-monitoring-logs.md)

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
