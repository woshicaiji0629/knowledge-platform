# 配置行动策略时的内容模板介绍-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/variables-in-new-alert-templates

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

# 内容模板变量说明（新版）

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍新版内容模板的变量以及引用方式。

## 引用方式

重要

- 

引用变量时，变量名称必须完全匹配。

- 

对于不存在的变量或者不合法的引用，系统默认替换为空字符串。

- 

如果引用的值为对象类型，则会转换为JSON字符串。

- 

模板的变量名称规则：大小写字母、数字、下划线，且不以数字开头。

- 

如果模板变量名称符合标准规则，则可以通过{{alert.xxx}}获取值。

- 

如果模板变量名称不符合标准规则，例如变量名称为__tag__:__namespace__，获取值的方法为{{alert.annotations["__tag__:__namespace__"] }}。

配置行动策略时必须选择内容模板，内容模板定义具体的发送内容和主题。您可以在发送内容和主题/标题中，通过{{ alert.xxx }}方式引用模板变量。日志服务发送告警通知时，会将发送内容和主题/标题中的模板变量替换为真实值，例如{{ alert.project }}替换为告警规则所属的Project名称。

例如在钉钉渠道的内容模板中，设置标题为SLS 告警，在发送内容中引用模板变量{{ alert.aliuid }}、{{ alert.project }}、{{ alert.alert_name }}、{{ alert.severity }}分别获取账号ID、Project名称、告警规则名称和告警严重度。

除了直接引用变量外，您还可以通过控制流以及内置函数对变量进行操作和处理。具体的模板语法和内置函数请参见[内容模板语法（新版）](products/sls/documents/syntax-for-new-alert-templates.md)、[内置模板函数](products/sls/documents/built-in-functions-in-alert-templates.md)。

## 告警属性

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

| 变量 | 说明 | 数据类型 | 取值示例 | 引用示例 |
| --- | --- | --- | --- | --- |
| aliuid | Project 所属的阿里云账号 ID。 | string | 117918634953**** | {{ alert.aliuid }} 用户的告警规则已触发。 |
| alert_instance_id | 告警触发的实例的 ID。 | string | ee16a8f435485f3f-5be6b81edc520-3d6**** | 实例 ID 为 {{ alert.alert_instance_id }} 。 |
| alert_id | 告警规则 ID，Project 内唯一。 | string | alert-12345 | 告警规则 ID 是 {{ alert.alert_id }} 。 |
| alert_name | 告警规则名称。 | string | 测试告警规则 | 告警规则 {{ alert.alert_name }} 已经触发。 |
| alert_type | 告警类型。 sls_alert：由告警监控规则触发的告警。 sls_pub：来自于开放告警的告警。 sls_ml：由智能巡检触发的告警。 | string | sls_alert | 告警类型是 {{ alert.alert_type }} ，格式化显示为 {{ alert.alert_type | format_type }} 。 |
| region | 地域。 | string | cn-hangzhou | 告警触发的地域为 {{ alert.region }} 。 |
| project | 告警规则所属 Project。 | string | my-project | {{ alert.project }} 项目中的告警规则已触发。 |
| next_eval_interval | 下一次评估间隔，单位为秒。 | int | 300 | 下一次评估时间为 {{ alert.next_eval_interval }} 秒后。 |
| alert_time | 本次评估时间。 | int | 1616744734 | 本次评估告警的时间为 {{ alert.alert_time }} ，格式化显示为 {{ alert.alert_time | format_date }} 。 |
| fire_time | 首次触发时间。 | int | 1616059834 | 告警首次触发时间为 {{ alert.fire_time }} ，格式化显示为 {{ alert.fire_time | format_date }} 。 |
| status | 告警状态。 firing：触发告警。 resolved：恢复通知。 | string | firing | 告警状态为 {{ alert.status }} ，格式化显示为 {{ alert.status | format_status }} 。 |
| resolve_time | 告警恢复时间。 如果告警状态是 firing，取值为 0。 如果告警状态是 resolved，取值为具体恢复时间。 | int | 0 | 告警恢复的时间为 {{ alert.resolve_time }} ，格式化显示为 {{ alert.resolve_time | format_date }} 。 |
| severity | 告警严重度。 10：严重 8：高 6：中 4：低 2：仅报告 | int | 10 | 告警严重度为 {{ alert.severity }} ，格式化显示为 {{ alert.severity | format_severity }} 。 |
| labels | 标签列表。 | map | {"env":"test"} | 告警标签为 {{ alert.labels | to_list }} |
| annotations | 标注列表。 | map | { "title": "告警标题","desc": "告警描述" } | 告警标注为 {{ alert.annotations | to_list }} 。 |
| results | 查询参数和中间结果，数组类型。变量取值说明，请参见 [QueryData](products/sls/documents/variables-in-new-alert-templates.md) [结构](products/sls/documents/variables-in-new-alert-templates.md) 。 | array | 参见本文末尾附录。 | 第一个查询的开始时间为 {{ alert.results[0].start_time }} ；结束时间为 {{ alert.results[0].end_time }} ；count 的值为 {{ alert.results[0].fire_result.cnt }} ；查询和分析语句为 {{ alert.results[0].query }} 。 |
| fire_results | 触发告警的数据，即集合操作后的数据，最多 100 条。 fire_results 变量值超过 2KB，并且查询结果字段内容的长度超过 1KB 时，超出部分会被截断。数据被截断处理方式请参见 [触发告警的日志太多，在告警通知中展示不完全时，如何处理？](products/sls/documents/faq-about-alert-notifications.md) | array | 参见本文末尾附录。 | 告警触发时产生的数据为 {{ alert.fire_results | to_json }} 。 |
| fire_results_count | 触发告警的数据的总条数，可能多于 100，例如笛卡尔积操作后的总条数。 | int | 3 | 告警触发时产生的总数据条数为 {{ alert.fire_results_count }} 。 |
| condition | 触发告警的评估表达式。其中，以触发告警的值替换您所配置的变量，并使用中括号（[ ]）包裹。格式为 Count:数量表达式;Condition:匹配表达式 。 | string | Count:[5] > 3;Condition:[example.com]=='example.com' | 告警评估表达式为 {{ alert.condition }} 。 |
| raw_condition | 原始的评估表达式，即变量未被替换为真实值的原始表达式。格式为 Count:数量表达式;Condition:匹配表达式 。 | string | Count:__count__ > 3;Condition:host=='example.com' | 原始评估表达式为 {{ alert.raw_condition }} 。 |
| policy | 告警策略或者行动策略。变量取值说明，请参见 [Policy](products/sls/documents/variables-in-new-alert-templates.md) [结构](products/sls/documents/variables-in-new-alert-templates.md) 。 | map | 参见本文末尾附录。 | 告警策略 ID 为 {{ alert.policy.alert_policy_id }} 。 |
| dashboard | 告警关联的仪表盘名称。 | string | mydashboard | 告警关联的仪表盘名称为 {{ alert.dashboard }} 。 |
| alert_url | 告警的详细 URL 地址。 | string | https://sls.console.aliyun.com/lognext/project/test-xxxx/alert/alert-1617164106-940166 | 告警 URL 为 {{ alert.alert_url }} 。 |
| query_url | 查询统计中第一个查询页面的 URL 地址。 | string | https://sls.console.aliyun.com/lognext/project/test-xxx/logsearch/test-alert-access?encode=base64&endTime=1617175989&queryString=KiB8IHNlbGVjdCBjb3VudCgxKSBhcyBjbn****&queryTimeType=99&startTime=1617175089 | 查询统计中第一个查询页面的 URL 地址为 {{ alert.query_url }} 。 |
| alert_history_dashboard_url | 告警历史统计报表的 URL 地址。 | string | https://sls.console.aliyun.com/lognext/project/test-xx/dashboard/internal-alert-analysis | 告警历史统计报表的 URL 地址为 {{ alert.alert_history_dashboard_url }} 。 |
| dashboard_url | 告警关联的仪表盘地址。 | string | https://sls.console.aliyun.com/next/project/myproject/dashboard/mydashboard | 告警关联的仪表盘地址为 {{ alert.dashboard_url }} 。 |
| fingerprint | 告警指纹。更多信息，请参见 [基于告警指纹去重](products/sls/documents/deduplicate-alerts-based-on-fingerprints.md) 。 | string | 478325709134bc5c | 告警指纹为 {{ alert.fingerprint }} 。 |
| signin_url | 免登录控制台即可查看告警详情。更多信息，请参见 [免登录查看告警详情](products/sls/documents/view-alert-details-in-logon-free-mode.md) 。 | string | https://sls.console.aliyun.com/console/AlertAjax/slsSignIn.json?token=xxxx | [查看详情]({{ alert.signin_url }}) 。 |


## Policy结构

policy变量中可引用的变量说明如下表所示。

| 变量 | 说明 | 数据类型 | 取值示例 |
| --- | --- | --- | --- |
| alert_policy_id | 告警策略 ID。 | string | sls.test-alert |
| action_policy_id | 告警监控规则指定的行动策略 ID，仅在告警策略使用动态行动策略时有用。 | string | sls.test-action |
| repeat_interval | 重复等待时间，仅在告警策略使用动态行动策略时有用。 | string | 4h |


## QueryData结构

results变量中可引用的变量说明如下表所示。

- 

- 

- 

| 变量 | 说明 | 数据类型 | 取值示例 |
| --- | --- | --- | --- |
| store_type | 存储类型。 log：日志。 metric：时序数据。 meta：资源数据。 | string | log |
| region | 查询统计目标库所在地域。 存储类型为资源数据时，该变量值为空。 | string | cn-hangzhou |
| project | 查询统计目标库所在 Project。 存储类型为资源数据时，该变量值为空。 | string | sls-test-alert |
| store | 查询统计中的目标库名称。 | string | test-LogStore |
| query | 查询分析语句。 | string | error | select count(1) as cnt |
| start_time | 查询开始时间。 存储类型为资源数据时，该变量值为空。 | int | 1616741485 |
| end_time | 查询结束时间。 存储类型为资源数据时，该变量值为空。 | int | 1616745085 |
| raw_results | 实际查询内容，数组格式，最多 100 行。 raw_results 变量值超过 2KB，并且查询结果字段内容的长度超过 1KB 时，超出部分会被截断。 | array | [{ "host": "example.com", "slbid": "slb-02", "status": "200" }, { "host": "example.com", "slbid": "slb-01", "status": "200" }] |
| raw_results_count | 实际查询数据的总条数，可能多于 100。 | int | 20 |
| fire_result | 告警触发内容中的第一条数据。告警触发结果集可能包含多条数据，该参数只返回第一条数据。 | map | { "host": "example.com", "slbid": "slb-02", "status": "200" } |
| query_url | 查询的 URL 地址。 存储类型为资源数据时，该变量值为空。 | string | https://sls.console.aliyun.com/lognext/project/test-xxx/logsearch/test-alert-access?encode=base64&endTime=1617175989&queryString=KiB8IHNlbGVjdCBjb3VudCgxKSBhcy*******&queryTimeType=99&startTime=1617175089 |
| dashboard_url | 查询关联的仪表盘地址。 | string | https://sls.console.aliyun.com/next/project/myproject/dashboard/mydashboard |
| role_arn | 使用服务角色的 ARN。 | string | acs:ram::117918634953****:role/aliyunslsalertmonitorrole |


## 常见问题

- 

[如何在通知中引用日志内容？](products/sls/documents/faq-about-alert-notifications.md)

- 

[如何在通知中展示触发告警的日志内容？](products/sls/documents/faq-about-alert-notifications.md)

- 

[触发告警的日志太多，在告警通知中展示不完全时，如何处理？](products/sls/documents/faq-about-alert-notifications.md)

## 附录

- 

results结构

[{ "store_type": "log", "region": "cn-hangzhou", "project": "sls-alert-test", "store": "test", "query": "* | select count(1) as cnt", "start_time": 1616741485, "end_time": 1616745085, "dashboard_id": "mydashboard", "raw_results": [{ "cnt": "4" }], "raw_result_count": 1, "fire_result": { "cnt": "4" }, "truncated": false, "role_arn": "" }]

- 

fire_results结构

[{ "host": "example.com", "host__1": "example.com", "pv": "836", "slbid": "slb-02", "status": "200" }, { "host": "example.com", "host__1": "example.com", "pv": "836", "slbid": "slb-02", "status": "200" }]

- 

policy结构

{ "alert_policy_id": "sls.test-alert", "action_policy_id": "sls.test-action", "repeat_interval": "5m0s" }

## 示例

通过新版内容模板定义通知内容的示例如下：

- 

告警内容

{ "alert_id": "test-alert", "alert_name": "PV/UV Alert", "project": "project-1", "status": "firing", "severity": 6, "labels": { "app": "nginx", "host": "host-1" }, "results": [ { "project": "project-1", "logstore": "logstore-1", "query": "* | select count(*) as pv" }, { "project": "project-2", "logstore": "logstore-2", "query": "* | select count(distinct user_id) as uv" } ] }

- 

内容模板配置

- Alert ID: {{ alert.alert_id }} - Alert Name: {{ alert.alert_name }} - Project: {{ alert.project }} - Status: {% if alert.status == "firing" %}FIRING{% else %}RESOLVED{% endif %} - Labels: {%- for key, val in alert.labels.items() %} - {{ key }}: {{ val }} {%- endfor %} - Query: {{ alert.results[0].query }}

- 

输出结果

- Alert ID: test-alert - Alert Name: PV/UV Alert - Project: project-1 - Status: FIRING - Labels: - app: nginx - host: host-1 - Query: * | select count(*) as pv

[上一篇：内置模板函数](products/sls/documents/built-in-functions-in-alert-templates.md)[下一篇：内容模板变量说明（旧版）](products/sls/documents/variables-in-original-alert-templates.md)

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
