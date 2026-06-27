# 如何创建日志告警监控规则-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/create-an-alert-monitoring-rule-for-logs

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

# 创建告警监控规则

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

创建日志告警监控规则后，日志服务根据您定义的检查频率、触发条件等配置产生告警，并根据您所选择的告警策略和行动策略进行告警降噪和通知。

## 前提条件

- 

已采集数据。

支持采集[日志](products/sls/documents/data-collection-overview.md)、[时序数据](products/sls/documents/collect-metric-data-from-hosts.md)。

重要

基于查询和分析语句创建告警监控规则前，需要先将日志采集到Standard Logstore中。更多信息，请参见[管理](products/sls/documents/manage-a-logstore.md)[LogStore](products/sls/documents/manage-a-logstore.md)。

- 

如果采集的是日志，需要创建索引。具体操作，请参见[创建索引](products/sls/documents/create-indexes.md)。

## 操作步骤

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在日志存储>日志库页签中，单击目标Logstore。

- 

在查询/分析页面，单击图标。

- 

在告警监控规则面板中，配置如下参数，单击确定。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

### 

- 

- 

- 

### 

- 

- 

- 

### 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 规则名称 | 告警监控规则的名称。 |
| 检查频率 | 日志服务根据您配置的频率对查询和分析结果进行检查。 每小时 ：每小时检查一次查询和分析结果。 每天 ：在每天的某个固定时间点检查一次查询和分析结果。 每周 ：在周几的某个固定时间点检查一次查询和分析结果。 固定间隔 ：按照固定间隔检查查询和分析结果。 Cron ：通过 Cron 表达式指定时间间隔，按照指定的时间间隔检查查询和分析结果。 说明 Cron 表达式在日志服务的告警规则里最小精度为分钟，格式为 24 小时制。例如： 0/5 * * * * 从 0 分钟开始，每隔 5 分钟检查一次 0 0/1 * * * 从 0 点 0 分开始，每隔 1 小时检查一次 0 18 * * * 每天 18 点 0 分检查一次 0 0 1 * * 每月 1 日 0 点 0 分检查一次 Cron 表达式语法，可参见 [Cron](products/ecs/documents/user-guide/cron-scheduled-tasks.md) [定时任务](products/ecs/documents/user-guide/cron-scheduled-tasks.md) 。 |
| 查询统计 | 单击输入框，在 查询统计 对话框中，设置查询和分析语句。 关联报表 页签：选择监控仪表盘。 高级配置 页签： 在 类型 列表选择： 日志库 ：用于存储日志，相关的查询分析配置请参见 [查询与分析快速指引](products/sls/documents/quick-guide-to-query-and-analysis.md) 。 指标库 ：用于存储时序数据，相关的查询分析配置请参见 [查询和分析时序数据](products/sls/documents/query-and-analyze-metric-data.md) 。 资源数据 ：用于配置特定告警监控规则所关联的外部数据。更多信息，请参见 [创建资源数据](products/sls/documents/create-resource-data.md) 。 选择 类型 为 日志库 或 指标库 ，且设置了查询和分析语句时，您可以选择是否开启独享 SQL。更多信息，请参见 [高性能完全精确查询与分析（SQL](products/sls/documents/dedicated-sql.md) [独享版）](products/sls/documents/dedicated-sql.md) 。 自动 ：默认不使用独享 SQL。当遇到查询并发限制或者查询结果不精确时，自动尝试使用独享 SQL 再次查询。 启用 ：始终使用独享 SQL 进行查询和分析。 关闭 ：关闭独享 SQL。 配置多个查询统计时，您可以指定 集合操作 关联多个查询结果。更多信息，请参见 [设置查询统计语句](products/sls/documents/set-query-statistics-statement.md) 。 |
| 分组评估 | 日志服务支持对查询和分析结果进行分组。更多信息，请参见 [设置分组评估](products/sls/documents/use-the-group-evaluation-feature.md) 。 标签自定义 ：日志服务根据您配置的字段对查询和分析结果进行分组。分组后，每个组单独评估触发条件。在每个检查周期内，查询和分析结果满足触发条件时，各个分组各自产生一条告警。 支持设置多个字段。 不分组 ：在每个检查周期内，满足触发条件时，只产生一条告警。 标签自动 ：当您在 查询统计 中选择 指标库 （即监控时序数据的查询和分析结果）时 ，日志服务支持标签自动分组。 分组后，每个组单独评估触发条件。在每个检查周期内，查询和分析结果满足触发条件时，各个分组各自产生一条告警。 |
| 触发条件 | 配置触发条件及严重度。 触发条件 有数据 ：当查询和分析结果中存在数据时，触发告警。 有特定条数据 ：当查询和分析结果中存在 N 条数据时，触发告警。 有数据匹配 ：当查询和分析结果中存在数据满足告警表达式时，触发告警。 有特定条数据匹配 ：当查询和分析结果中存在 N 条数据满足告警表达式时，触发告警。 严重度 主要用于告警降噪控制和告警通知控制，即您在创建告警策略或行动策略时，可添加关于告警严重度的判断条件。更多信息，请参见 [设置告警严重度](products/sls/documents/specify-severity-levels-for-alerts.md) 。 简单配置：直接选择告警严重度，则表示通过该规则产生的告警都为同一严重度。 分条件配置：单击 添加 ，分条件设置告警严重度。 告警条件表达式的相关语法，请参见 [告警条件表达式语法](products/sls/documents/syntax-of-trigger-conditions-in-alert-rules.md) 。 |
| 添加标签 | 日志服务允许您给产生的告警添加标识性属性，键值对格式。主要用于告警降噪控制和告警通知控制，即您在创建告警策略或行动策略时，可添加关于标签的判断条件。更多信息，请参见 [添加标签和标注](products/sls/documents/labels-and-annotations.md) 。 |
| 添加标注 | 日志服务允许您给产生的告警添加非标识性属性，键值对格式。主要用于告警降噪控制和告警通知控制，即您在创建告警策略或行动策略时，可添加关于标注的判断条件。更多信息，请参见 [添加标签和标注](products/sls/documents/labels-and-annotations.md) 。 您还可以打开 自动添加标注 开关，系统自动在告警中添加 __count__ 等信息。更多信息，请参见 [自动标注](products/sls/documents/labels-and-annotations.md) 。 |
| 恢复通知 | 打开 恢复通知 开关后，告警恢复时触发一条恢复告警。例如您创建了一个告警监控规则，用于监控各个主机的 CPU 指标，当 CPU 使用率超过 95%时触发告警，主机 CPU 使用率下降为正常值（低于等于 95%）后发送一条恢复通知。更多信息，请参见 [设置恢复通知](products/sls/documents/recovery-notifications.md) 。 |
| 高级配置>连续触发阈值 | 连续多少次执行检查评估都满足触发条件时，才会触发一次告警。不满足触发条件时不计入统计。 |
| 高级配置>无数据告警 | 打开 无数据告警 开关后，如果查询和分析的结果（有多个时，进行集合操作后的结果）为无数据的次数超过 连续触发阈值 ，则产生一条告警。更多信息，请参见 [无数据告警](products/sls/documents/user-guide/no-data-alert.md) 。 |
| 输出目标 | 输出目标用于配置告警事件的输出位置，可以配置一个或多个输出目标。 事件库 ：将告警事件写入到 EventStore。 云监控事件中心 ：将告警事件写入到云监控系统事件中心，通过云监控对告警进行管理和通知。 SLS 通知 ：将告警事件输出到 SLS 的通知服务，通过告警策略、行动策略等对告警进行管理和通知。 |
| 输出目标-事件库 | 开启 ：打开事件库开启开关后，告警将写入到 EventStore 中。 地域 ：告警写入的 EventStore 所属地域。 Project ：告警写入的 EventStore 所属项目。 事件库 ：告警写入的 EventStore。 授权方式 ： 默认角色 ：单击 前往授权 ，根据界面提示完成授权，并扮演阿里云系统角色 AliyunLogETLRole 将告警写入目标 EventStore。具体操作，请参见 [默认角色授权](products/sls/documents/configure-permissions-for-writing-alarms-to-the-event-library.md) 。 自定义角色 ：扮演自定义角色将告警写入目标 EventStore，填写角色 ARN。具体操作，请参见 [自定义角色授权](products/sls/documents/configure-permissions-for-writing-alarms-to-the-event-library.md) 。 |
| 输出目标-云监控事件中心 | 开启 ：打开云监控事件中心开启开关后，告警将发送到云监控事件中心。更多信息，请参见 [查看系统事件](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/view-system-events) 。 |
| 输出目标-SLS 通知 | 开启 ：打开 SLS 通知开关后，告警将发送到 SLS 通知服务进行后续的管理和通知。 告警策略 极简模式 日志服务默认使用 SLS 内置动态告警策略（sls.builtin.dynamic）进行告警管理。 配置行动组。 您配置行动组后，日志服务自动为您创建一个名为 规则名称-行动策略 的行动策略。由该告警监控规则触发的所有告警都通过该行动策略发送通知。如何配置，请参见 [通知渠道说明](products/sls/documents/notification-methods.md) 。 重要 您可以在行动策略管理页面，修改该行动策略。具体操作，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。如果您在修改行动策略时添加了判断条件，则此处的 告警策略 将自动变更为 普通模式 。 重复等待 ：在重复等待时间内，重复的告警只触发一次行动策略，即只发送一次告警通知。 普通模式 日志服务默认使用 SLS 内置动态告警策略（sls.builtin.dynamic）进行告警管理。 选择内置的或自定义的行动策略进行告警通知。如何创建行动策略，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。 重复等待 ：在重复等待时间内，重复的告警只触发一次行动策略，即只发送一次告警通知。 高级模式 选择内置的或自定义的告警策略进行告警管理。如何创建告警策略，请参见 [创建告警策略](products/sls/documents/create-an-alert-policy.md) 。 选择内置的或自定义的行动策略进行告警通知。如何创建行动策略，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。还可以开启或关闭 自定义行动策略 。更多信息，请参见 [动态行动策略机制](products/sls/documents/dynamic-action-policy-mechanism.md) 。 重复等待 ：在重复等待时间内，重复的告警只触发一次行动策略，即只发送一次告警通知。 |


[上一篇：配置告警写入事件库的权限](products/sls/documents/configure-permissions-for-writing-alarms-to-the-event-library.md)[下一篇：管理告警监控规则](products/sls/documents/manage-an-alert-monitoring-rule.md)

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
