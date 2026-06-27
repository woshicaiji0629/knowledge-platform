# 如何创建值班组-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/create-an-on-duty-group

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

# 创建值班组

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

值班组是日志服务告警提供的值班轮岗编排机制，支持根据周期、工作时长等安排轮询值班。本文介绍创建值班组的操作步骤。

## 前提条件

已创建用户或用户组。具体操作，请参见[创建用户和用户组](products/sls/documents/create-users-and-user-groups.md)。

## 操作步骤

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

进入值班组管理页面。

- 

在Project列表区域，单击任意一个Project。

- 

在左侧导航栏中，单击告警。

- 

在告警中心页面，选择通知对象>值班组管理。

- 

单击创建。

- 

在添加值班组对话框中，配置如下基本信息。

- 

- 

| 参数 | 说明 |
| --- | --- |
| 标识符 | 值班组唯一标识，单个阿里云账号下不可重复。 |
| 组名 | 值班组名称。 |
| 启用 | 是否启用值班组。 启用：值班组处于正常状态，可安排值班。 不启用：值班组处于禁用状态，不可安排值班。 |


- 

配置值班表。

值班表提供三种视图，分别为最终排班、值班轮岗和代班。配置值班轮岗和代班后，您可以通过最终排班视图看到最终的排班情况。处于值班轮岗中的员工无法值班时，您可以使用代班功能安排其他人进行值班。

- 

配置值班轮岗。

- 

单击>值班轮岗。

- 

在添加值班轮岗对话框中，配置如下参数，并单击保存。

- 

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 开始时间 | 值班开始时间。 |
| 结束时间 | 值班结束时间。 |
| 限制 | 配置详细的值班时间段。 无 ：每天 24 小时值班。 工作日 ：仅在工作日值班，支持添加具体时间段。 非工作日 ：仅在非工作日值班，支持添加具体时间段。 每天 ：每天值班，支持添加具体时间段。 每周 ：在每周特定时间内值班。 |
| 对象 | 值班人员支持选择多个值班人员（用户、用户组）。 说明 如果用户或用户组被禁用，则在排班时自动过滤该用户或用户组。 |
| 轮岗类型 | 支持按照小时班、日班、周班和月班进行轮流值班。 |
| 交班时间 | 根据轮岗类型设置交班的具体时间，支持自定义时间。 |


- 

可选：配置代班。

- 

单击>代班。

- 

在添加代班对话框，配置如下参数，并单击保存。

- 

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 对象 | 原值班人员，支持选择多个值班人员。 |
| 执行对象 | 代班人员，只能选择一个对象。 |
| 开始时间 | 代班开始时间。 |
| 结束时间 | 代班结束时间。 支持快捷设置本周结束、下一周结束、本月结束、本季度结束、今年结束和自定义。 |
| 限制 | 详细的代班时间段。 无 ：每天 24 小时代班。 工作日 ：仅在工作日代班，支持添加具体时间段。 非工作日 ：仅在非工作日代班，支持添加具体时间段。 每天 ：每天代班，支持添加具体时间段。 每周 ：在每周特定时间内代班。 |


- 

查看最终排班。

单击值班轮岗和代班>最终排班。最终排班日历以月视图展示各日期的班次安排，每个日期标注班或休标记，并显示已分配的排班用户标签（如 user1、wan... 等），当前日期以蓝色圆圈高亮。

- 

配置日历。

支持全局默认日历和自定义日历，日历包含了时区、节假日、默认工作时间等定义，并可以进行重置。日历影响了当前值班组在值班轮岗、代班时的真正值班时间以及交班时间等。

- 

自定义日历：自定义工作日和节假日的时间段。配置后为值班组独有的工作日历。

- 

全局默认日历：默认日历，采用预设国家的工作日历。选择该值后，与其他值班组使用相同的工作日历。更多信息，请参见[修改全局默认日历](products/sls/documents/modify-the-global-default-calendar.md)。

- 

单击保存。

[上一篇：创建用户和用户组](products/sls/documents/create-users-and-user-groups.md)[下一篇：Webhook集成](products/sls/documents/create-a-webhook.md)

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
