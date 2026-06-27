# 旧版内容模板支持的变量以及引用方式有哪些-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/variables-in-original-alert-templates

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

# 内容模板变量说明（旧版）

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍旧版内容模板所支持的变量以及引用方式。

## 引用方式

重要

引用变量时，变量名称必须完全匹配。对于不存在的变量或者不合法的引用默认替换为空字符串。如果引用的值为对象类型，则会转换为JSON字符串。

配置行动策略时必须选择内容模板，内容模板定义具体的发送内容和主题。您可以在发送内容和主题中，通过${fieldName}方式引用模板变量。日志服务发送告警通知时，会将发送内容和主题中的模板变量替换为真实值，例如${project}替换为告警规则所属的Project名称。

## 可用变量及其引用

目前支持的所有可用变量及引用方式如下表所示。

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
| aliuid | Project 所属的阿里云账号 ID。 | string | 117918664953**** | ${aliuid} 用户的告警规则已触发。 |
| alert_instance_id | 告警触发的实例的 ID。 | string | ee16a8f435485f3f-5be6b81edc520-3d6**** | 实例 ID 为 ${alert_instance_id} 。 |
| project | 告警规则所属 Project。 | string | my-project | ${project} 项目中的告警规则已触发。 |
| alert_id | 告警规则 ID，Project 内唯一。 | string | 0fdd88063a611aa114938f9371daeeb6-1671a52**** | 告警规则 ID 是 ${alert_id} 。 |
| alert_type | 告警类型。 sls_alert：由告警监控规则触发的告警。 sls_pub：来自于开放告警中的告警。 | string | sls_alert | 告警类型是 ${alert_type} 。 |
| alert_name | 告警规则名称。 | string | 告警规则 new2 | 告警规则 ${alert_name} 已经触发。 |
| next_eval_interval | 下一次评估间隔。 | int | 900 | 下一次评估时间为 ${next_eval_interval} 秒后。 |
| alert_time | 本次评估时间。 | int | 1616744734 | 本次评估告警的时间为 ${alert_time} 。 |
| fire_time | 首次触发时间。 | int | 1616059834 | 告警首次触发时间为 ${fire_time} 。 |
| status | 告警状态。 firing：触发告警。 resolved：恢复通知。 | string | firing | 告警状态为 ${status} 。 |
| resolve_time | 告警恢复时间。 如果告警状态是 firing，取值为 0。 如果告警状态是 resolved，取值为具体恢复时间。 | int | 0 | 告警恢复的时间为 ${resolve_time} 。 |
| results | 查询参数和中间结果，数组类型。变量取值说明，请参见 [QueryData](products/sls/documents/variables-in-original-alert-templates.md) [结构](products/sls/documents/variables-in-original-alert-templates.md) 。 | array | [ { "store_type": "log", "region": "cn-hangzhou", "project": "sls-alert-test", "store": "test", "query": "* | select count(1) as cnt", "start_time": 1616741485, "end_time": 1616745085, "dashboard_id": "mydashboard", "raw_results": [{"cnt": "4"}], "raw_result_count": 1, "truncated": false, "role_arn": "" } ] | 第一个查询的开始时间为 ${results[0].start_time} ；结束时间为 ${results[0].end_time} 。 说明 其中 0 为图表编号。 |
| labels | 标签列表。 | map | {"env":"test"} | 告警标签为 ${labels} 。 |
| annotations | 标注列表。 | map | { "title": "告警标题","desc": "告警描述" } | 告警标注为 ${annotations} 。 |
| severity | 告警严重度。 10：严重 8：高 6：中 4：低 2：仅报告 | int | 10 | 告警严重度为 ${severity} 。 |
| policy | 告警策略或者行动策略。变量取值说明，请参见 [Policy](products/sls/documents/variables-in-original-alert-templates.md) [结构](products/sls/documents/variables-in-original-alert-templates.md) 。 | map | { "alert_policy_id": "sls.test-alert", "action_policy_id": "sls.test-action", "use_default": false, "repeat_interval": "6m0s" } | 告警策略 ID 为 ${policy.alert_policy_id} 。 |
| region | 地域。 | string | cn-hangzhou | 告警触发的地域为 ${region} 。 |
| drill_down_query | 用于下钻分析的查询语句。在自定义告警中值为空，目前适用于日志审计服务、成本管家和 SLB 日志中心的告警内容模板。 | string | * | select count(1) as cnt | 无 |
| alert_url | 告警的详细 URL 地址。 | string | https://sls.console.aliyun.com/lognext/project/test-xxxx/alert/alert-1617164106-940166 | 告警 URL 为 ${alert_url} 。 |
| query_url | 查询统计中第一个查询页面的 URL 地址。 | string | https://sls-stg.console.aliyun.com/lognext/project/test-xxx/logsearch/test-alert-access?encode=base64&endTime=1617175989&queryString=KiB8IHNlbGVjdCBjb3VudCgxKSBhcyBjbnQ%3D&queryTimeType=99&startTime=1617175089 | 查询统计中第一个查询页面的 URL 地址为 ${query_url} 。 |
| alert_history_dashboard_url | 告警历史统计报表的 URL 地址。 | string | https://sls.console.aliyun.com/lognext/project/test-xx/dashboard/internal-alert-analysis | 告警历史统计报表的 URL 地址为 ${alert_history_dashboard_url} 。 |
| condition | 触发告警的评估表达式。其中，以触发告警的值替换您所配置的变量，并使用中括号（[ ]）包裹。格式为 Count:数量表达式; Condition:匹配表达式 。 | string | Count:[5] > 3;Condition:[example.com]=='example.com' | 告警评估表达式为 ${condition} 。 |
| raw_condition | 原始的评估表达式，即变量未被替换为真实值的原始表达式。格式为 Count:数量表达式; Condition:匹配表达式 。 | string | Count:__count__ > 3;Condition:host=='example.com' | 原始评估表达式为 ${raw_condition} 。 |
| dashboard | 告警关联的仪表盘名称。 | string | mydashboard | 告警关联的仪表盘名称为 ${dashboard} 。 |
| dashboard_url | 告警关联的仪表盘地址。 | string | https://sls.console.aliyun.com/next/project/myproject/dashboard/mydashboard | 告警关联的仪表盘地址为 ${dashboard_url} 。 |
| fire_results | 触发告警的数据，即集合操作后的数据，最多 100 条。 | array | [{ "host":example.com", "host__1":"example.com", "pv":"836", "slbid":"slb-02", "status":"200"},{ "host":"example.com", "host__1":"example.org", "pv":"836", "slbid":"slb-02", "status":"200" },{ "host":"example.com", "host__1":"example.com", "pv":"836", "slbid":"slb-02", "status":"200" },{ "host":"example.com", "host__1":"example.com", "pv":"836", "slbid":"slb-02", "status":"200" },{ "host":"example.com", "host__1":"example.com", "pv":"780", "slbid":"slb-01", "status":"200" }] | 告警触发时产生的数据为 ${fire_results} 。 |
| fire_results_count | 触发告警的数据的总条数，可能多于 100，比如笛卡尔积操作后的总条数。 | int | 3 | 告警触发时产生的总数据条数为 ${fire_results_count} 。 |
| fire_results_as_kv | 触发告警的数据，即集合操作后的数据，最多 100 条。以 [key1:value1,key2:value2] 形式展示。 | array | [host:example.com,pv:836,status:200][host:example.com,pv:780,status:200] | 告警触发时产生的数据详情为 ${fire_results_as_kv} 。 |


## Policy结构

policy变量中可引用的变量说明如下表所示。

| 字段 | 说明 | 数据类型 | 举例 |
| --- | --- | --- | --- |
| alert_policy_id | 告警策略 ID。 | string | sls.test-alert |
| action_policy_id | 告警监控规则指定的行动策略 ID，仅在告警策略使用动态行动策略时有用。 | string | sls.test-action |
| repeat_interval | 重复等待时间，仅在告警策略使用行动策略时有用。 | string | 4h |


## QueryData结构

results变量中可引用的变量说明如下表所示。

- 

- 

- 

| 变量 | 说明 | 数据类型 | 举例 |
| --- | --- | --- | --- |
| role_arn | 使用服务角色。 | string | acs:ram::117918664953****:role/aliyunslsalertmonitorrole |
| store_type | 存储类型。 log：日志。 metric：时序数据。 meta：资源数据。 | string | log |
| region | 查询统计目标库所在地域。 存储类型为资源数据时，该变量值为空。 | string | cn-hangzhou |
| project | 查询统计目标库所在 Project。 存储类型为资源数据时，该变量值为空。 | string | sls-test-alert |
| store | 查询统计目标库名称。 | string | test-LogStore |
| query | 查询语句。 | string | error | select count(1) as cnt |
| start_time | 查询开始时间。 存储类型为资源数据时，该变量值为空。 | int | 2006-01-02 15:04:05 |
| start_time_ts | 查询开始时间，Unix 格式。 存储类型为资源数据时，该变量值为空。 | int | 1616741485 |
| end_time | 查询结束时间。 存储类型为资源数据时，该变量值为空。 | int | 2006-01-02 15:04:05 |
| end_time_ts | 查询结束时间，Unix 格式。 存储类型为资源数据时，该变量值为空。 | int | 1616745085 |
| dashboard_id | 查询时关联的仪表盘 ID。 | string | mydashboard |
| raw_results | 实际查询内容，数组格式，最多 100 行。 | array | [{ "host":"example.com", "slbid":"slb-02", "status":"200" },{ "host":"example.com", "slbid":"slb-01", "status":"200" },{ "host":"example.com", "slbid":"slb-02", "status":"306" },{ "host":"example.com", "slbid":"slb-02", "status":"200" },{ "host":"example.com", "slbid":"slb-01", "status":"200" },{ "host":"example.com", "slbid":"slb-02", "status":"200" }] |


[上一篇：内容模板变量说明（新版）](products/sls/documents/variables-in-new-alert-templates.md)[下一篇：免登录查看告警详情](products/sls/documents/view-alert-details-in-logon-free-mode.md)

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
