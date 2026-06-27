# 如何创建内容模板-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/create-an-alert-template

# 创建内容模板
日志服务按照内容模板中定义的内容给您发送告警内容。
## 操作步骤
登录[日志服务控制台](https://sls.console.aliyun.com)。
进入内容模板管理页面。
在Project列表区域，单击任意一个Project。
在左侧导航栏中，单击告警。
在告警中心页面，选择通知策略>内容模板。
在内容模板页签中，单击创建。
在添加内容模板对话框中，配置如下参数，然后单击确定。
您可以在一个内容模板中分别配置短信、语音、邮件、钉钉、WebHook-自定义、通知中心、企业微信、飞书和Slack的告警通知内容。
| 参数 | 描述 |
| --- | --- |
| 标识符 | 内容模板标识符，单个阿里云账号下不可重复。 |
| 名称 | 内容模板的名称。 |
| 短信 | 短信渠道的内容模板说明如下： 非定制内容语言 ：告警通知内容的语言，支持中文和英文。 发送内容 ：告警通知内容。您还可以使用模板变量定义内容。更多信息，请参见 [内容模板变量说明（新版）](variables-in-new-alert-templates.md) 。 |
| 语音 | 语音渠道的内容模板说明如下： 非定制内容语言 ：告警通知内容的语言，支持中文（推荐）和英文。 发送内容 ：告警通知内容。您还可以使用模板变量定义内容。更多信息，请参见 [内容模板变量说明（新版）](variables-in-new-alert-templates.md) 。 |
| 邮件 | 邮件渠道的内容模板说明如下： 非定制内容语言 ：告警通知内容的语言，支持中文和英文。 主题 ：告警消息的主题。您还可以使用模板变量定义主题。 发送内容 ：告警通知内容。您还可以使用模板变量定义内容。更多信息，请参见 [内容模板变量说明（新版）](variables-in-new-alert-templates.md) 。 |
| 钉钉 | 钉钉渠道的内容模板说明如下： 标题 ：告警消息的标题。您还可以使用模板变量定义标题。 发送内容 ：告警通知内容。您还可以使用模板变量定义内容。更多信息，请参见 [内容模板变量说明（新版）](variables-in-new-alert-templates.md) 。 |
| WebHook-自定义 | WebHook 渠道的内容模板说明如下： 发送方式 ：支持逐条发送和合并发送。 例如发送内容配置为 { "project": "{{project}}", "alert_name": "{{alert_name}}"} ，当触发两个告警时： 逐条发送：发送两次告警通知，其内容分别为 { "project": "project-1", "alert_name": "alert-1"} 和 { "project": "project-2", "alert_name": "alert-2"} 。 合并发送：发送一次告警通知，其内容为 [{ "project": "project-1", "alert_name": "alert-1"}, { "project": "project-2", "alert_name": "alert-2"}] 。 选择合并发送时，如果限制了单个分组最多发送的条数，则只发送合并集合中的前 N 条告警。 选择合并发送时，如果您配置的内容可解析为 JSON 格式，则最终发送的内容为 JSON 格式。否则为字符串数组格式。 发送内容 ：告警通知内容。您还可以使用模板变量定义内容。更多信息，请参见 [内容模板变量说明（新版）](variables-in-new-alert-templates.md) 。 说明 发送告警通知时默认添加请求头信息 Content-Type: application/json;charset=utf-8 。如果 Webhook 接收端需要其它格式的请求头，您可以在配置通知渠道时，自定义请求头信息。更多信息，请参见 [Webhook-自定义](notification-methods.md) 。 |
| 通知中心 | 通知中心渠道内容模板说明如下： 非定制内容语言 ：告警通知内容的语言，支持中文和英文。 发送内容 ：告警通知内容。您还可以使用模板变量定义内容。更多信息，请参见 [内容模板变量说明（新版）](variables-in-new-alert-templates.md) 。 |
| 企业微信 | 企业微信渠道的内容模板说明如下： 标题 ：告警消息的标题。您还可以使用模板变量定义标题。 发送内容 ：告警通知内容。您还可以使用模板变量定义内容。更多信息，请参见 [内容模板变量说明（新版）](variables-in-new-alert-templates.md) 。 |
| 飞书 | 飞书渠道的内容模板说明如下： 标题 ：告警消息的标题。您还可以使用模板变量定义标题。 发送内容 ：告警通知内容。您还可以使用模板变量定义内容。更多信息，请参见 [内容模板变量说明（新版）](variables-in-new-alert-templates.md) 。 |
| Slack | Slack 渠道的内容模板说明如下： 标题 ：告警消息的标题。您还可以使用模板变量定义标题。 发送内容 ：告警通知内容。您还可以使用模板变量定义内容。更多信息，请参见 [内容模板变量说明（新版）](variables-in-new-alert-templates.md) 。 |
| EventBridge | 事件总线（EventBridge）渠道的内容模板说明如下： 主题 ：告警消息的主题。您还可以使用模板变量定义主题。 发送内容 ：告警通知内容。您还可以使用模板变量定义内容。更多信息，请参见 [内容模板变量说明（新版）](variables-in-new-alert-templates.md) 。 |
| 函数计算 | 函数计算（FC）渠道的内容模板说明如下： 发送方式 ：支持逐条发送和合并发送。 例如发送内容配置为 { "project": "{{project}}", "alert_name": "{{alert_name}}"} ，当触发两个告警时： 逐条发送：发送两次告警通知，其内容分别为 { "project": "project-1", "alert_name": "alert-1"} 和 { "project": "project-2", "alert_name": "alert-2"} 。 合并发送：发送一次告警通知，其内容为 [{ "project": "project-1", "alert_name": "alert-1"}, { "project": "project-2", "alert_name": "alert-2"}] 。 选择合并发送时，如果限制了单个分组最多发送的条数，则只发送合并集合中的前 N 条告警。 选择合并发送时，如果您配置的内容可解析为 JSON 格式，则最终发送的内容为 JSON 格式。否则为字符串数组格式。 发送内容 ：告警通知内容。您还可以使用模板变量定义内容。更多信息，请参见 [内容模板变量说明（新版）](variables-in-new-alert-templates.md) 。 |
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
