# 使用各告警通知渠道的注意事项、前提条件、配置参数-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/notification-methods

# 通知渠道说明
本文介绍使用各个告警通知渠道的注意事项、前提条件和配置参数等信息。
## 背景信息
您可以在行动组中，选择如下渠道进行告警通知。
用户：短信、语音、邮件
Webhook：
钉钉、企业微信、飞书、Slack、通用Webhook
在行动组中选择您已创建的Webhook。您可以在Webhook集成管理Webhook。更多信息，请参见[Webhook](create-a-webhook.md)[集成](create-a-webhook.md)。
钉钉-自定义、Webhook-自定义
在行动组中填写Webhook URL等信息。保留这两种方式是为了兼顾历史配置。建议新创建的行动策略，使用Webhook集成方式。
其它：消息中心、事件总线、函数计算
## 简介
## 短信
设置告警通知渠道为短信，则触发告警后，日志服务会向指定的用户、用户组或值班组发送短信通知。
注意事项
使用短信告警通知时，发送通知的号码是随机的，无法提供固定号码。
前提条件
已创建用户、用户组或值班组。具体操作，请参见[创建用户和用户组](create-users-and-user-groups.md)、[创建值班组](create-an-on-duty-group.md)。
配置参数
选择短信渠道时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。
| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 短信 。 |
| 接收人 | 选择告警通知的对象（用户、用户组或值班组）。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
## 语音
设置告警通知渠道为语音，则触发告警后，日志服务会向指定的用户、用户组或值班组发送电话通知。
注意事项
如果某次告警电话未接通，将以短信方式发送一次通知。
说明
由于主叫号码池动态变化，因此建议用户关闭运营商和手机助手的拦截功能，否则可能会影响告警电话和短信的正常接收。
前提条件
已创建用户、用户组或值班组。具体操作，请参见[创建用户和用户组](create-users-and-user-groups.md)、[创建值班组](create-an-on-duty-group.md)。
配置参数
选择语音渠道时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。
| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 语音 。 |
| 接收人 | 选择告警通知的对象（用户、用户组或值班组）。 重要 语音渠道仅支持中国内地手机号码（+86），即您在创建用户时，配置的手机号码须为中国内地手机号码。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
## 邮件
设置告警通知渠道为邮件，则触发告警后，日志服务会向指定的用户、用户组或值班组发送邮件通知。
注意事项
日志服务使用monitor@monitor.aliyun.com邮件地址发送邮件告警通知，您可将该邮件地址添加到邮箱白名单中，以免告警邮件被拦截。
前提条件
已创建用户、用户组或值班组。具体操作，请参见[创建用户和用户组](create-users-and-user-groups.md)、[创建值班组](create-an-on-duty-group.md)。
配置参数
选择邮件渠道时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。
| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 邮件 。 |
| 接收人 | 选择告警通知的对象（用户、用户组或值班组）。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
## 钉钉-自定义
设置告警通知渠道为钉钉-自定义，则触发告警后，日志服务会通过钉钉机器人向指定的钉钉群发送告警通知，并且支持提醒指定成员。
注意事项
每个机器人每分钟最多发送20条告警通知。
前提条件
使用钉钉发送告警通知前，需要完成如下配置。
根据[钉钉企业内部应用机器人的创建和安装](https://open.dingtalk.com/document/orgapp/the-creation-and-installation-of-the-application-robot-in-the)创建一个消息接收模式为HTTP模式的机器人应用。
打开钉钉客户端，进入钉钉群，单击右上角的图标。
选择机器人>添加机器人。
选择第一步创建的机器人，并单击添加，再点击完成。
在群聊中的机器人管理页面查看创建好的机器人，复制Webhook链接。
配置参数
选择钉钉-自定义渠道时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。
| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 钉钉-自定义 。 |
| 请求地址 | 配置为您在钉钉群里生成的 Webhook 链接。 |
| 提醒方式 | 支持在钉钉群里提醒指定成员，可选值为不提醒、所有人、指定成员。 配置为 指定成员 时，需选择被提醒的用户、用户组或值班组。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 说明 钉钉支持 Markdown 格式。更多信息，请参见 [钉钉](non-customized-notification-content.md) 。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
## Webhook-自定义
设置告警通知方式为Webhook-自定义，当触发告警时，日志服务会向自定义的Webhook地址发送告警通知。
注意事项
Webhook方式对应的超时时间为5秒，如果发出请求后5秒内没有返回，则表示发送失败。
前提条件
已获取Webhook地址。
配置参数
选择Webhook-自定义渠道时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。
说明
Webhook调用成功时返回的状态码需为200，否则会被日志服务认为请求失败，导致重复调用。
| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 WebHook-自定义 。 |
| 请求地址 | Webhook 地址，必须为公网地址（例如外网域名、IP:Port 格式的 URL）。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 使用自定义 Webhook 时，建议设置内容模板中的内容为 JSON 格式。 |
| 请求方式 | 支持 GET、POST、DELETE、PUT 和 OPTIONS。 无特殊需求时，推荐使用 POST 方法。该方法在各个 Web 框架中的支持程度最好。 |
| 请求头 | 单击 添加请求头 ，可添加请求头信息。例如 Content-Type: application/json;charset=utf-8 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
## 消息中心
设置告警通知渠道为消息中心，则触发告警后，日志服务会通过消息中心向指定人员发送告警通知。
前提条件
使用消息中心发送告警通知前，需先在阿里云消息中心完成如下配置。
登录[阿里云消息中心](https://notifications.console.aliyun.com/?spm=5176.202052012811.aliyun_topbar.162.zRRPhO#/subscribeMsg)。
选择消息接收管理>基本接收管理，单击日志服务（LOG）告警右侧的修改。
在修改消息接收人对话框中，选择消息接收人，单击保存。
本账号负责人可新增消息接收人。配置完成后，系统将自动发送验证信息到所填手机号码和邮箱，通过验证后方可接收消息。
说明
最少需要设置1位消息接收人。
消息接收方式默认为邮件+短信，且不可更改。
配置参数
选择消息中心渠道时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。
| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 消息中心 。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
## 钉钉
设置告警通知渠道为钉钉，则触发告警后，日志服务会通过钉钉机器人向指定的钉钉群发送告警通知，并且支持提醒指定成员。
注意事项
每个机器人每分钟最多发送20条告警通知。
前提条件
已创建Webhook。具体操作，请参见[Webhook](create-a-webhook.md)[集成](create-a-webhook.md)。
配置参数
选择钉钉渠道时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。
| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 钉钉 。 |
| 选择 Webhook | 选择您已创建的 Webhook。 |
| 提醒方式 | 支持在钉钉群里提醒指定成员，可选值为不提醒、所有人、指定成员。 配置为 指定成员 时，需选择被提醒的用户、用户组或值班组。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 说明 钉钉支持 Markdown 格式。更多信息，请参见 [内容格式](custom-notification-content.md) 。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
## 企业微信
设置告警通知渠道为企业微信，则触发告警后，日志服务会通过企业微信机器人向指定的企业微信群发送告警通知。
前提条件
已创建Webhook。具体操作，请参见[Webhook](create-a-webhook.md)[集成](create-a-webhook.md)。
配置参数
选择企业微信渠道时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。
| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 企业微信 。 |
| 选择 Webhook | 选择您已创建的 Webhook。 |
| 提醒方式 | 支持在企业微信群里提醒指定成员，可选值为不提醒、所有人、指定成员。 配置为 指定成员 时，需选择被提醒的用户、用户组或值班组。 重要 配置为 所有人 或 指定成员 时，企业微信的通知内容只能为普通文本格式，不支持 Markdown 格式。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 说明 企业微信支持 Markdown 格式。更多信息，请参见 [内容格式](custom-notification-content.md) 。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
## 飞书
设置告警通知渠道为飞书，则触发告警后，日志服务会通过飞书机器人向指定的飞书群发送告警通知。
前提条件
已创建Webhook。具体操作，请参见[Webhook](create-a-webhook.md)[集成](create-a-webhook.md)。
配置参数
选择飞书渠道时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。
| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 飞书 。 |
| 选择 Webhook | 选择您已创建的 Webhook。 |
| 提醒方式 | 支持在飞书群里提醒所有人，可选值为不提醒、所有人。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 说明 飞书支持 Markdown 格式。更多信息，请参见 [内容格式](custom-notification-content.md) 。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
## Slack
设置告警通知渠道为Slack，则触发告警后，日志服务会向Slack用户发送告警通知。
前提条件
已创建Webhook。具体操作，请参见[Webhook](create-a-webhook.md)[集成](create-a-webhook.md)。
配置参数
选择Slack渠道时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。
| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 Slack 。 |
| 选择 Webhook | 选择您已创建的 Webhook。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 说明 Slack 支持 Markdown 格式。更多信息，请参见 [内容格式](custom-notification-content.md) 。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
## 通用Webhook
设置告警通知渠道为通用Webhook，则当触发告警时，日志服务会向自定义的Webhook地址发送告警通知。
前提条件
已创建Webhook。具体操作，请参见[Webhook](create-a-webhook.md)[集成](create-a-webhook.md)。
配置参数
选择通用Webhook渠道时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。
| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 通用 Webhook 。 |
| 选择 Webhook | 选择您已创建的 Webhook。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
## 事件总线（EventBridge）
设置告警通知渠道为事件总线（EventBridge），则触发告警后，日志服务会向事件总线发送一个告警事件。
前提条件
已在阿里云事件总线EventBridge服务中创建自定义总线。具体操作，请参见[创建自定义总线](https://help.aliyun.com/zh/eventbridge/user-guide/manage-custom-event-buses#section-sfl-pcs-6rh)。
说明
在创建自定义总线时，可忽略事件源的配置。如果要添加事件源，则需创建一个名为acs.sls.alert的事件源，与告警事件中source字段的值保持一致。
如果您使用的是RAM用户，需先授予该RAM用户AliyunEventBridgeReadOnlyAccess权限。
配置参数
选择事件总线（EventBridge）时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。
| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 事件总线(EventBridge) 。 |
| 地域 | 选择您已创建的事件总线的所在地域。 |
| 事件总线 | 选择您已创建的事件总线。日志服务将发送告警事件给该事件总线。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
事件字段说明
触发告警后，日志服务会生成一个告警事件并发送给事件总线，事件规范请参见[事件概述](https://help.aliyun.com/zh/eventbridge/user-guide/event-overview#concept-1938024)。日志服务生成的事件字段说明如下：
重要
如果生成了多个告警，则每个告警都会发送告警事件，不会进行告警合并。
如果内容模板（事件总线）中的发送内容不是JSON格式，则告警事件发送成功后，在事件总线的事件规则中将无法使用data字段中的变量。
| 字段名称 | 说明 |
| --- | --- |
| id | 事件 ID，全局唯一。 |
| source | 事件源，固定为 acs.sls.alert。 |
| specversion | CloudEvents 协议版本，当前为 1.0 版本。 |
| type | 事件类型。 如果告警状态为触发告警，则事件类型为 sls:AlertEvent:Firing。 如果告警状态为恢复通知，则事件类型为 sls:AlertEvent:Resolved。 |
| datacontenttype | data 字段的内容格式，固定为 application/json。 |
| subject | 事件主题，对应内容模板中设置的 EventBridge 主题。 |
| time | 事件产生的时间，对应告警消息中的 alert_time 字段。 |
| data | 事件内容，对应内容模板中设置的 EventBridge 发送内容，必须为 JSON 格式。 |
## 函数计算（FC）
设置告警通知渠道为函数计算（FC），则告警触发后，日志服务会调用您所创建的函数。
注意事项
只支持非HTTP函数。如果是HTTP函数，请使用自定义Webhook方式。
只支持以sls-ops-开头的函数。
前提条件
已经在阿里云函数计算服务中创建服务以及函数（仅支持非HTTP函数）。更多信息，请参见[快速创建函数](https://help.aliyun.com/zh/functioncompute/fc-2-0/create-a-function-in-the-function-compute-console#multiTask782)。
如果您使用的是RAM用户，需先授予该RAM用户AliyunFCReadOnlyAccess权限。
配置参数
选择函数计算（FC）时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。
| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 函数计算(FC) 。 |
| 地域 | 选择您已创建的函数的所在地域。 |
| 服务 | 选择您已创建的函数计算服务。 |
| 版本/别名 | 选择服务的版本或别名，默认为 LATEST。 |
| 函数 | 选择您已创建的函数。仅支持以 sls-ops-开头的函数。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
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
