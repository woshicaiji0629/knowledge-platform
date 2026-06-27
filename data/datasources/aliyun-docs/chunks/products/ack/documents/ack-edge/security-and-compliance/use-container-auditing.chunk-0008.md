## （可选）步骤四：配置操作审计告警
通过日志服务的告警功能，您可以配置容器内部操作审计的实时告警，便于监控容器内关键的操作事件。告警方式支持短信、钉钉机器人、邮件、自定义Webhook和通知中心。本文以配置钉钉告警的方式，介绍如何配置容器内部操作审计告警。更多告警配置方式，请参见[告警](../../../../sls/documents/sls-alerting.md)。
登录[日志服务控制台](https://sls.console.aliyun.com)。
进入Webhook集成页面。
在Project列表区域，单击目标Project。
在左侧导航栏中，单击告警。
在告警中心页面，单击通知对象页签，然后单击Webhook集成。
创建Webhook。
在Webhook集成页面，单击创建。
在新建Webhook对话框中，配置如下配置项，然后单击确认。

| 配置项 | 描述 |
| --- | --- |
| 标识符 | Webhook 的唯一标识，不可重复。本示例配置为 ack-container-operation-audit-alert 。 |
| 名称 | Webhook 名称。本示例配置为 Kubernetes 容器内部操作审计告警 。 |
| 类型 | Webhook 类型。本示例选择 钉钉 。 |
| 请求地址 | Webhook URL 地址。 在钉钉侧创建自定义机器人，并获取 Webhook URL 地址。 更多信息，请参见 [自定义机器人接入](https://open.dingtalk.com/document/group/custom-robot-access) 。 |

新建内容模板。
在告警中心页面，单击通知策略页签，然后单击内容模板。
在内容模板页面，单击创建。
配置内容模板的标识符和名称，然后配置钉钉告警通知的标题和发送内容。
关于添加内容模板的更多信息，请参见[创建内容模板](../../../../sls/documents/create-an-alert-template.md)。本文需配置两个内容模板，具体配置内容如下。
