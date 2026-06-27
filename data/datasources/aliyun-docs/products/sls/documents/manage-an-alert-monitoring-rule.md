# 告警监控规则相关操作-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/manage-an-alert-monitoring-rule

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

# 管理告警监控规则

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

配置告警后，您可以在告警概览页面查看告警监控规则详情与状态等信息，以及执行修改、删除等操作。

## 查看告警监控规则信息

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在左侧导航栏中，单击告警。

- 

在告警中心页面的告警规则页签中，单击目标告警监控规则。

- 

在告警概览页面中，查看告警所属仪表盘、创建时间、上次更新、检查频率、启用状态、监控状态、告警历史统计报表等信息。

告警历史统计报表包含告警次数、执行成功率和告警触发趋势三个统计面板。

## 修改告警监控规则

您可以在告警概览页面中，单击修改配置，修改告警监控规则。其参数配置和创建告警监控规则界面一致。具体操作，请参见[创建告警监控规则](products/sls/documents/create-an-alert-monitoring-rule-for-logs.md)。

## 关闭与启用告警监控规则

创建告警监控规则后，您可以在告警概览页面的基本信息区域，配置启用状态，启用或关闭告警。

说明

关闭告警监控规则后，日志服务不再执行告警检查、发送通知等操作。

## 关闭与恢复告警通知

告警监控规则的状态为已开启时，支持关闭告警通知。 在告警概览页面，单击监控状态后的设置，并设置关闭时长。

在关闭告警通知期间，您可在监控状态中查看告警通知的恢复时间。单击监控状态后的设置，可在自动恢复告警通知前，手动恢复告警通知。

说明

在关闭告警通知期间，日志服务仍会定期执行告警规则检查，即使满足告警条件也不会发送告警通知。

## 删除告警监控规则

当您不再使用该告警监控规则时，您可以在告警概览页面，单击删除告警，删除该告警监控规则。

重要

删除告警监控规则后不可恢复，请谨慎操作。

## 复制告警监控规则

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在左侧导航栏中，单击告警。

- 

在告警中心页面的告警规则页签中，单击目标告警监控规则操作列>复制。

- 

在目标Project弹框，选择要复制到的目标Project以及LogStore。在更多设置区域，可以重置目标告警名称、目标告警状态和目标告警ID，然后单击确定。

警告

- 

如果未重置目标告警名称、目标告警状态和目标告警ID，则沿用源配置。

- 

如果复制的告警关联了仪表盘，默认会同时复制仪表盘，这可能会覆盖掉目标project下相同ID的仪表盘。

- 

复制告警时，若未选择目标LogStore，默认查找和源同名的LogStore；若目标Project下无该库，告警时会导致LogStoreNotExist错误而告警失败。

- 

在复制结果弹框可以查看复制详情。

复制详情包含目标Project、告警、第一个资源库(其他资源库使用原值)、复制告警状态和复制告警信息等列，可逐条确认告警规则是否复制成功。

- 

复制成功后，进入到目标Project，在告警中心页面，查看复制成功的告警规则。复制的告警规则与源告警规则配置一样。

复制的告警规则名称会自动添加-copy后缀（如新告警规则-copy），状态为运行中。

[上一篇：创建告警监控规则](products/sls/documents/create-an-alert-monitoring-rule-for-logs.md)[下一篇：设置查询统计语句](products/sls/documents/set-query-statistics-statement.md)

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
