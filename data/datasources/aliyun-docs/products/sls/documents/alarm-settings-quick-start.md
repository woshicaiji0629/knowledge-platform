# 如何快速设置日志告警-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/alarm-settings-quick-start

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

# 告警设置快速入门

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

将日志采集到LogStore后，您可以添加告警规则。本文以告警通知发送到钉钉群为例，为您介绍设置日志告警的操作步骤。

## 操作概览

本文以告警通知发送到钉钉群为例，将日志采集到LogStore后，告警规则每15分钟检测一次目标LogStore是否有数据，有数据则触发告警，钉钉机器人发送告警信息并提醒用户处理。具体步骤如下：

- 

配置通知对象：配置用户Bob，并将Bob添加进用户组。

- 

配置告警规则：每15分钟检查一次目标LogStore是否有数据，有数据则触发告警。

- 

配置通知策略：使用日志服务内置的告警内容模板，通过钉钉渠道发送告警到钉钉群并提醒Bob。

- 

查看告警触发记录：触发告警后，查看告警大盘与通知详情。

## 操作步骤

说明

设置告警前，需要确保LogStore中可以正常采集到日志。

### 步骤一：配置通知对象

配置用户和用户组用于指定告警通知对象。

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在左侧导航栏中，单击告警。在告警中心页面，参照以下步骤，例如配置用户Bob相关信息，单击确认。

单击通知对象页签，选择用户管理页签，单击创建按钮。在添加用户对话框中，填写标识符、姓名、手机号（可开启可收短信和可接电话开关）、邮箱等信息，并确认启用开关已开启。

- 

参照以下步骤，在添加用户组对话框中，将Bob加入到test组，单击确认。

单击用户组管理页签，再单击创建按钮打开对话框。在标识符中输入test，在待添加成员列表中勾选目标成员后单击>按钮将其移入已添加成员列表，确认启用开关已开启。

### 步骤二：配置告警规则

告警监控规则用于监控日志数据。在本文示例中，告警规则配置成每15分钟检测一次目标LogStore是否存在数据，有数据则触发钉钉群告警。

- 

在告警中心>告警规则页签，单击新建告警。

- 

在新建告警面板中，配置查询统计，单击添加。

其中规则名称可设为新告警规则，检查频率选择固定间隔15分钟，分组评估选择不分组。

- 

在查询统计对话框中，选择目标日志库，单击预览查看数据，然后单击确认。

选择高级配置Tab，类型选择日志库，查询语句设置为* | select *。

- 

在新建告警面板中，触发条件选择当有数据时告警，严重度选择中，点击确定。

### 步骤三：配置通知策略

配置内容模板日志服务按照内容模板中定义的内容给用户发送告警内容。例如使用SLS内置内容模板，通过钉钉推送告警。

- 

在告警中心>通知策略>内容模板页签，选择SLS内置内容模板，在操作列单击修改。

- 

配置钉钉告警的发送内容。

在标题中输入SLS告警，在发送内容中输入以下模板变量：告警规则名称：${alert_name}、告警严重度：${severity}、标注串：{{ alert.annotations | to_json }}、告警主机: {{alert.fire_results[0].__source__}}，然后单击确认。

配置SLS通知日志服务按照输出目标选择渠道推送告警。例如通过SLS通知配置钉钉渠道推送告警。

- 

前提条件

使用钉钉发送告警通知前，需要完成如下配置。

- 

根据[钉钉企业内部应用机器人的创建和安装](https://open.dingtalk.com/document/orgapp/the-creation-and-installation-of-the-application-robot-in-the)创建一个消息接收模式为HTTP模式的机器人应用。

- 

打开钉钉客户端，进入钉钉群，单击右上角的图标。

- 

选择机器人>添加机器人。

- 

选择通过Webhook接入自定义服务，点击添加，配置机器人名字，安全设置选择自定义关键字，输入告警，点击完成。

- 

在群聊中的机器人管理页面查看创建好的机器人，复制Webhook链接。

- 

配置通知对象

在新建Webhook对话框，请求地址填写复制的Webhook链接，按照如下说明配置，然后单击确定。

在对话框中填写标识符和名称，将类型设置为钉钉。加签密钥为可选项，仅在安全设置为加签时需要填写。

- 

配置通知渠道

在告警规则页签中，选择目标规则，单击编辑。

在编辑告警面板中，按照如下说明配置，然后单击确定。

在输出目标中勾选SLS通知，打开开启开关。告警策略选择极简模式。在行动组中添加钉钉通知渠道，选择Webhook设为sample_test，提醒方式设为指定成员，接收人类型设为静态接收人，接收人设为Bob，内容模板设为SLS内置内容模板，发送时段设为任意。

### 步骤四：查看告警触发记录

查看告警大盘

在告警中心>告警大盘>告警规则中心页面，查看告警触发次数。

该页面展示告警规则统计、告警规则评估状态、告警触发趋势及告警触发次数四个区域，支持通过Project、告警ID、告警名称等条件筛选告警数据。

查看通知详情

- 

在告警中心>告警规则页面，单击目标规则。

- 

您可以查看详细的告警信息。是否触发告警为true，表示已成功触发。

在告警概览页面的告警历史表格中，执行结果为Success，详情为Successful，确认告警已正常执行并触发。

## 相关参考

- 

日志告警更多通知渠道，具体请参见[通知渠道说明](products/sls/documents/notification-methods.md)。

- 

仅短信通知和语音通知会产生费用，具体请参见[费用说明](products/sls/documents/user-guide/the-alerting-feature-of-log-service.md)。

- 

告警属性说明，具体请参见[告警属性参考](products/sls/documents/alert-attributes.md)。

- 

内容模板变量，具体请参见[内容模板变量说明（新版）](products/sls/documents/variables-in-new-alert-templates.md)，创建内容模板请参见[创建内容模板](products/sls/documents/create-an-alert-template.md)。

[上一篇：告警](products/sls/documents/sls-alerting.md)[下一篇：授权](products/sls/documents/sls-alerting-authorization.md)

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
