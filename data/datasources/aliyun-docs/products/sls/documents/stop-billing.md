# 日志服务如何停止计费-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/stop-billing

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

# 停止计费

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

日志服务开通后无法关闭，如果不再需要使用日志服务，您可删除所有Project，日志服务将自动停止计费。

## 停止计费说明

- 

创建LogStore时，日志服务默认预留两个Shard。因此只要LogStore存在，无论是否使用都会产生活跃Shard租用费用。日志服务根据您的活跃Shard租用量收取费用。关于Shard租用费用详细说明，请参见[为什么会产生活跃](products/sls/documents/why-am-i-charged-for-active-shards.md)[Shard](products/sls/documents/why-am-i-charged-for-active-shards.md)[租用费用](products/sls/documents/why-am-i-charged-for-active-shards.md)。

即使没有写入任何日志，只要 LogStore 存在且未关闭索引，仍会因索引流量产生基础费用。

如果您不再需要使用LogStore存储日志，请及时删除，避免产生额外费用。具体操作，请参见[停止计费/删除](products/sls/documents/manage-a-logstore.md)[LogStore](products/sls/documents/manage-a-logstore.md)。

- 

目前日志服务仅支持[修改数据保存时间](products/sls/documents/how-do-i-delete-logs.md)来删除日志，无法手动删除指定内容的日志，当日志保存时间达到您所设置的保存时间后，日志将被删除。如需降低存储费用，您可设置较短的存储周期。如果不再需要已有日志，您可直接[删除](products/sls/documents/stop-billing.md)[Project](products/sls/documents/stop-billing.md)[或](products/sls/documents/stop-billing.md)[LogStore](products/sls/documents/stop-billing.md)。

- 

删除 Project 的当天仍会产生存储等费用，从次日开始不再产生新的费用。

日志服务按天出账。删除资源后，当天的费用会在次日生成账单。因此您在删除后的第三天查看账单时，即可确认无新增费用。

- 

如果您的账号处于欠费状态，存储资源不会立即释放，系统将继续计费直至资源被回收（通常为停服 7 天后）。关于欠费后的具体处理规则，请参见[欠费说明](products/sls/documents/overdue-payments.md)。建议及时删除不需要的资源或为账号充值，以避免持续产生意外费用。

- 

如果您的 Project 已开启回收站功能，删除 Project 后数据会进入回收站保留。在回收站保留期间，仍会产生存储费用。若需立即彻底停止计费，需要在回收站中将该 Project 彻底删除。关于回收站操作的详细说明，请参见[管理 Project 回收站](products/sls/documents/stop-billing.md)。

## 删除Project或LogStore

警告

通过任意方式删除Project或LogStore后，所有日志数据及配置信息都会被释放，不可恢复，请慎重确认，避免数据丢失。

### 云产品日志

在弹性计算、存储服务、安全、数据库等多种阿里云云产品开通日志分析服务，会在日志服务控制台自动创建对应的Project和LogStore。更多信息，请参见[云产品日志概述](products/sls/documents/alibaba-cloud-service-logs.md)。

如果不需要云产品日志，您可按照以下步骤关闭。

- 

在对应云产品控制台关闭日志分析服务。

- 

在日志服务控制台删除Project或LogStore。

- 

如需保留Project仅删除LogStore，请参见[停止计费/删除](products/sls/documents/manage-a-logstore.md)[LogStore](products/sls/documents/manage-a-logstore.md)。

- 

如需删除整个Project，请参见[管理](products/sls/documents/manage-a-project.md)[Project](products/sls/documents/manage-a-project.md)。

重要

云产品日志 Project（如 Web 应用防火墙 WAF、云安全中心 SAS/安骑士等）由对应云产品自动创建，无法在日志服务控制台直接删除。如需删除此类 Project，请前往对应云产品的控制台进行操作。

### 日志审计服务日志

- 

如果您不再需要采集云产品日志，但想要暂时保留已采集的日志（日志将在超出存储天数后被删除），请参见[停止采集日志](products/sls/documents/enable-log-collection-1.md)。

- 

如果您需要清理并删除日志审计服务相关的所有日志服务资源（如Project、LogStore、仪表盘、告警等），请参见[删除审计资源](products/sls/documents/enable-log-collection-1.md)。

### Cloud Lens服务日志

注意事项

警告

CloudLens功能要求云账号下必须存在至少一个Project。

在用户开通和使用CloudLens功能时，日志服务会检测账号下是否存在Project，具体逻辑如下。

检测逻辑

- 

用户第一次开通CloudLens功能，日志服务会自动检测您当前的阿里云账号下是否存在任意Project，如果没有Project，则会在华南2（河源）地域创建一个名称为aliyun-product-data-阿里云账号ID-cn-heyuan的Project。

- 

用户开通CloudLens功能后进入CloudLens，日志服务只会自动检测您当前的阿里云账号下是否存在任意Project，不会在华南2（河源）地域创建Project，用户可以手动创建任意Project，创建Project的步骤请参见[管理](products/sls/documents/manage-a-project.md)[Project](products/sls/documents/manage-a-project.md)。

删除Project

- 

如果您要删除aliyun-product-data-阿里云账号ID-cn-heyuan这个Project，可以打开[云命令行](https://shell.aliyun.com/)，执行以下命令进行删除，请根据实际情况替换阿里云账号ID。

aliyunlog log delete_project --project_name=aliyun-product-data-阿里云账号ID-cn-heyuan --region-endpoint=cn-heyuan.log.aliyuncs.com

- 

删除其他Project和LogStore的步骤，请参见[管理](products/sls/documents/manage-a-logstore.md)[LogStore](products/sls/documents/manage-a-logstore.md)和[管理](products/sls/documents/manage-a-project.md)[Project](products/sls/documents/manage-a-project.md)。

### 其他日志

- 

如需保留Project仅删除LogStore，请参见[停止计费/删除](products/sls/documents/manage-a-logstore.md)[LogStore](products/sls/documents/manage-a-logstore.md)。

- 

如需删除整个Project，请参见[管理](products/sls/documents/manage-a-project.md)[Project](products/sls/documents/manage-a-project.md)。

精细化停止计费：如果希望保留特定业务日志（如 OSS 访问日志）但停止其他无关 LogStore 的计费，可以单独删除不需要的 LogStore，而无需删除整个 Project。这样可以实现单独停止某类日志的计费。

说明

删除 LogStore 前，请先确认该 LogStore 不再被任何 Logtail 采集配置引用。控制台会在删除时自动检查，如存在 Logtail 采集配置将阻断删除操作并提示"该 LogStore 下存在 Logtail 采集配置，请先删除采集配置"。此外，建议在删除前也确认该 LogStore 没有被仪表盘、告警规则或数据加工任务引用，以免这些配置报错。

## 如何确认日志服务已完全停止计费？

删除 Project 或 LogStore 后，可以通过以下方式确认已完全停止计费：

- 

资源检查：登录[日志服务控制台](https://sls.console.aliyun.com)，确认名下所有地域的 Project 列表为空，或仅剩明确需要保留的资源。

- 

关联服务检查：如果使用了云安全中心、Web 应用防火墙等其他云产品的日志分析功能，需确认已在对应产品控制台关闭日志采集，并在日志服务中删除了对应的 Project 或 LogStore。云产品日志 Project 无法在日志服务控制台直接删除。

- 

账单验证：日志服务按天出账，建议在操作删除后的第 2～3 天查看账单明细，确认无日志服务相关的新增扣费项目。如果账号处于欠费状态，存储资源不会立即释放，系统会继续计费直至资源被回收（通常为停服 7 天后）。

## 相关文档

- 

查看Project、LogStore的存储容量，请参见[如何查看日志服务的存储容量和消费记录](products/sls/documents/how-to-view-the-storage-capacity-and-consumption-records-of-log-service.md)。

- 

节省计划仅支持抵扣按写入数据量计费模式原始写入数据量计费项费用，不支持抵扣按使用功能计费模式下的计费项抵扣。更多信息，请参见[节省计划概述](products/sls/documents/overview-of-savings-plan.md)。

- 

新版资源包可用于抵扣日志服务所有的计费项，在有效期内，每月有相同的资源额度。当月额度用完后，自动转为按量付费方式。更多信息，请参见[资源包介绍](products/sls/documents/overview-11.md)。

- 

日志服务支持使用API方式删除Project或LogStore。具体操作，请参见[删除指定](products/sls/documents/developer-reference/api-sls-2020-12-30-deleteproject.md)[Project](products/sls/documents/developer-reference/api-sls-2020-12-30-deleteproject.md)和[删除](products/sls/documents/developer-reference/api-sls-2020-12-30-deletelogstore.md)[LogStore](products/sls/documents/developer-reference/api-sls-2020-12-30-deletelogstore.md)。

[上一篇：费用优化](products/sls/documents/cost-optimization.md)[下一篇：产品计费常见问题](products/sls/documents/bill-faq-8.md)

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
