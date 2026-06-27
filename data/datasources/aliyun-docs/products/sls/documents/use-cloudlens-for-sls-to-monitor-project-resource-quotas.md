# 如何使用CloudLens for SLS监控Project资源配额-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/use-cloudlens-for-sls-to-monitor-project-resource-quotas

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

# 使用CloudLens for SLS监控Project资源配额

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文主要介绍如何使用CloudLens for SLS中全局错误日志、监控指标做Project资源配额的水位监控、超限监控及提交资源配额提升申请。

## 背景介绍

Alibaba Cloud Lens基于日志服务SLS构建云产品可观测能力。支持一键开启实例日志（重要日志、详细日志、作业运行日志）和全局日志（审计日志、计费日志、错误日志、监控指标）的采集功能。

| 日志分类 | 子分类 | 监控场景说明 |
| --- | --- | --- |
| 实例日志 | 详细日志 | 访问流量监控 访问异常监控 |
| 重要日志 | 消费组监控 Logtail 采集监控 |  |
| 作业运行日志 | 数据加工（新版）监控 定时 SQL 任务监控 |  |
| 全局日志 | 审计日志 | 资源操作监控 |
| 错误日志 | 额度超限监控 访问异常监控 操作异常监控 |  |
| 监控指标 | 访问流量监控 访问异常监控 资源配额水位监控 |  |
| 计费日志 | 资源用量跟踪 |  |


各类型日志说明，请参见[日志索引表](products/sls/documents/log-types-of-cloudlens-applications.md)。

## 前提条件

- 

已创建RAM用户，并对RAM用户授权。具体操作，请参见[创建](products/ram/documents/user-guide/create-a-ram-user.md)[RAM](products/ram/documents/user-guide/create-a-ram-user.md)[用户](products/ram/documents/user-guide/create-a-ram-user.md)和[授权](products/sls/documents/authorize-ram-users-to-operate-cloudlens-for-sls.md)[RAM](products/sls/documents/authorize-ram-users-to-operate-cloudlens-for-sls.md)[用户操作](products/sls/documents/authorize-ram-users-to-operate-cloudlens-for-sls.md)[CloudLens for SLS](products/sls/documents/authorize-ram-users-to-operate-cloudlens-for-sls.md)。

- 

已开启全局日志：错误日志、指标监控采集功能。具体操作，请参见[开启日志采集功能](products/sls/documents/enable-the-log-collection-feature-1.md)。

重要

- 

为了构建实时资源配额水位监控，全局日志需开启：错误日志、指标监控；并且这两种全局日志需存储于同一Project内。

- 

为了避免监控日志存放在业务Project导致监控占用Project的配额，可选择系统推荐的固定地域目标Project，如杭州地域：log-service-{用户ID}-cn-hangzhou。

## 查看额度监控仪表盘

通过CloudLens for SLS额度监控大盘，您可以查看资源配额预警情况、Project重点资源配额实时水位详情及Project资源配额超限详情。

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在日志应用>云产品Lens区域，单击CloudLens for SLS。

- 

选择左侧菜单栏报表中心>额度监控，可查看配额信息。

### 资源配额预警概览

报表提供资源配额预警概览（水位超过80%）以及额度超限分布。

### Project重点资源配额实时水位详情

报表包含Project部分基础资源配额以及数据读写资源配额的实时水位详情。

表格展示各Project的基础资源配额水位，列包括地域、LogStore使用占比(%)、机器组使用占比(%)、Logtail采集配置使用占比(%)以及对应的水位/上限值。使用占比达到或接近100%的单元格以红色高亮标识，80%左右以橙色标识，便于快速识别高水位Project。右上角可单击调整资源配额进行配额调整。

数据读写资源配额表格包含Project、地域、Project写入流量(%)、Project写入次数(%)、Project读取次数(%)、Project每分钟写入流量GB(水位/上限)、Project写入次数(水位/上限)、Project读取次数(水位/上限)列，展示各Project在不同地域的读写配额使用水位与上限。单击右上角调整资源配额可修改配额上限。

### Project资源配额超限详情

报表提供Project资源配额超限详情。

详情页以表格形式展示Project、ErrorMsg（错误信息）、count（次数）三列，记录各 Project 的超限类型及发生次数，常见超限类型包括报表额度超限和LogStore数超限。页面右上角提供调整资源配额按钮，可快速调整对应资源配额。

## 资源监控

CloudLens for SLS支持提供基础资源、数据读写等额度监控和LogStore监控、机器组监控、Project写入监控等高级监控。

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在日志应用区域，单击CloudLens for SLS。

- 

在CloudLens for SLS配置界面，单击左侧菜单栏中的异常检测，可配置资源告警监控。

### 额度监控

额度监控项分类说明如下：

- 

- 

- 

- 

- 

- 

| 分类 | 监控项 | 说明 |
| --- | --- | --- |
| 实时水位监控 | [基础资源配额水位监控](products/sls/documents/use-cloudlens-for-sls-to-monitor-project-resource-quotas.md) | 监控 Project 内 LogStore 数量、机器组数量、Logtail 采集配置水位是否超阈值预期百分比。 依赖时序库：internal-monitor-metric |
| [数据读写配额水位监控](products/sls/documents/use-cloudlens-for-sls-to-monitor-project-resource-quotas.md) | 监控 Project 写入流量、Project 写入次数超配额次数。 依赖时序库：internal-monitor-metric |  |
| 额度超限监控 | [资源配额超限次数监控](products/sls/documents/use-cloudlens-for-sls-to-monitor-project-resource-quotas.md) | 监控基础配额、数据读写超配额次数。 依赖日志库：internal-error_log |


基础资源配额水位监控

- 

单击新建告警，配置告警规则。

- 

选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。

- 

根据业务场景配置告警触发条件、以及告警策略。

根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告警监控规则](products/sls/documents/alarm-settings-quick-start.md)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | 基础资源配额水位监控 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：指标库 授权方式：默认 指标库：internal-monitor-metric 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 * | select Project, region, logstore_ratio, machine_group_ratio, logtail_config_ratio from (SELECT A.id as Project , A.region as region, round(COALESCE(SUM(B.count_logstore), 0)/cast(json_extract(A.quota, '$.logstore') as double) * 100, 3) as logstore_ratio, cast(json_extract(A.quota, '$.logstore') as double) as quota_logstore, round(COALESCE(SUM(C.count_machine_group), 0)/cast(json_extract(A.quota, '$.machine_group') as double) * 100, 3) as machine_group_ratio, cast(json_extract(A.quota, '$.machine_group') as double) as quota_machine_group, round(COALESCE(SUM(D.count_logtail_config), 0)/cast(json_extract(A.quota, '$.config') as double) * 100, 3) as logtail_config_ratio, cast(json_extract(A.quota, '$.config') as double) as quota_logtail_config FROM "resource.sls.cmdb.project" as A LEFT JOIN ( SELECT project, COUNT(*) AS count_logstore FROM "resource.sls.cmdb.logstore" as B GROUP BY project ) AS B ON A.id = B.project LEFT JOIN ( SELECT project, COUNT(*) AS count_machine_group FROM "resource.sls.cmdb.machine_group" as C GROUP BY project ) AS C ON A.id = C.project LEFT JOIN ( SELECT project, COUNT(*) AS count_logtail_config FROM "resource.sls.cmdb.logtail_config" as D GROUP BY project ) AS D ON A.id = D.project group by A.id, A.quota, A.region) where quota_logstore is not null and quota_machine_group is not null and quota_logtail_config is not null and (logstore_ratio > 80 or machine_group_ratio > 80 or logtail_config_ratio > 80) limit 10000 |
| 分组评估 | 标签自动 |
| 触发条件 | 说明 当有 Project 的 LogStore 数、机器组数、Logtail 采集配置其中一个水位超过额度的 90%时告警级别为严重。 当有 Project 的 LogStore 数、机器组数、Logtail 采集配置其中一个水位超过额度的 80%时告警级别为中。 当有数据匹配 logstore_ratio > 90 || machine_group_ratio > 90 || logtail_config_ratio > 90 时，严重度：严重。 当有数据匹配 logstore_ratio > 80 || machine_group_ratio > 80 || logtail_config_ratio > 80 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。 |


在添加标注区域，设置title为${alert_name}告警触发，desc为${alert_name}告警触发，自动添加标注保持关闭。

- 

参数配置完成后，单击确定。

数据读写配额水位监控

- 

单击新建告警，配置告警规则。

- 

选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。

- 

根据业务场景配置告警触发条件、以及告警策略。

根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告警监控规则](products/sls/documents/alarm-settings-quick-start.md)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | 数据读写配额水位监控 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：指标库 授权方式：默认 指标库：internal-monitor-metric 查询区间：5 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 (*)| select Project, region, inflow_ratio, write_cnt_ratio from (SELECT cmdb.id as Project, cmdb.region as region, round(COALESCE(M.name1,0)/round(cast(json_extract(cmdb.quota, '$.inflow_per_min') as double)/1000000000, 3) * 100, 3) as inflow_ratio, round(COALESCE(M.name2,0)/cast(json_extract(cmdb.quota, '$.write_cnt_per_min') as double) * 100, 3) as write_cnt_ratio from "resource.sls.cmdb.project" as cmdb LEFT JOIN ( select project, round(MAX(name1)/1000000000, 3) as name1, MAX(name2) as name2 from (SELECT __time_nano__ as time, element_at( split_to_map(__labels__, '|', '#$#') , 'project') as project, sum(CASE WHEN __name__ = 'logstore_origin_inflow_bytes' THEN __value__ ELSE NULL END) AS name1, sum(CASE WHEN __name__ = 'logstore_write_count' THEN __value__ ELSE NULL END) AS name2 FROM "internal-monitor-metric.prom" where __name__ in ('logstore_origin_inflow_bytes','logstore_write_count' ) and regexp_like(element_at( split_to_map(__labels__, '|', '#$#') , 'project') , '.*') group by project,time )group by project) AS M ON cmdb.id = M.project) where inflow_ratio > 80 or write_cnt_ratio > 80 limit 10000 |
| 分组评估 | 标签自动 |
| 触发条件 | 说明 当有 Project 的 Project 写入流量、写入次数其中一个水位超过额度的 90%时告警级别为严重。 当有 Project 的 Project 写入流量、写入次数其中一个水位超过额度的 80%时告警级别为中。 当有数据匹配 where inflow_ratio > 90 || write_cnt_ratio > 90 时，严重度：严重。 当有数据匹配 where inflow_ratio > 80 || write_cnt_ratio > 80 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。 |


在添加标注区域，设置title为${alert_name}告警触发，desc为${alert_name}告警触发。

- 

参数配置完成后，单击确定。

资源配额超限次数监控

- 

单击新建告警，配置告警规则。

- 

选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。

- 

根据业务场景配置告警触发条件、以及告警策略。

根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告警监控规则](products/sls/documents/alarm-settings-quick-start.md)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | 资源配额超限次数监控 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：日志库 授权方式：默认 日志库：internal-error_log 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 ((* and (ErrorCode: ExceedQuota or ErrorCode: QuotaExceed or ErrorCode: ProjectQuotaExceed or ErrorCode:WriteQuotaExceed or ErrorCode: ShardWriteQuotaExceed or ErrorCode: ShardReadQuotaExceed)))| SELECT Project, CASE WHEN ErrorMsg like '%Project write quota exceed: inflow%' then 'Project 写入流量超限' WHEN ErrorMsg like '%Project write quota exceed: qps%' then 'Project 写入次数超限' WHEN ErrorMsg like '%dashboard quota exceed%' then '报表额度超限' WHEN ErrorMsg like '%config count%' then 'Logtail 采集配置超限' WHEN ErrorMsg like '%machine group count%' then '机器组超限' WHEN ErrorMsg like '%Alert count %' then '告警超限' WHEN ErrorMsg like '%logstore count %' then 'LogStore 数超限' WHEN ErrorMsg like '%shard count%' then 'Shard 数超限' WHEN ErrorMsg like '%shard write bytes%' then 'Shard 写入超限' WHEN ErrorMsg like '%shard write quota%' then 'Shard 写入超限' WHEN ErrorMsg like '%user can only run%' then 'SQL 分析操作并发数超限' ELSE ErrorMsg END AS ErrorMsg, COUNT(1) AS count GROUP BY Project, ErrorMsg Limit 1000 |
| 分组评估 | 不分组 |
| 触发条件 | 说明 当有任意额度超限 10 次错误告警级别为严重。 当有任意额度发生超限 1 次错误时告警级别为中。 当有数据匹配 count > 10 时，严重度：严重。 当有数据匹配 count > 1 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。 |


- 

参数配置完成后，单击确定。

### 高级监控

高级监控项分类说明如下：

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

| 分类 | 场景 | 监控项 | 说明 |
| --- | --- | --- | --- |
| 基础资源配额 | [LogStore](products/sls/documents/use-cloudlens-for-sls-to-monitor-project-resource-quotas.md) [监控](products/sls/documents/use-cloudlens-for-sls-to-monitor-project-resource-quotas.md) | 实时水位监控 | 监控 Project 下 LogStore 数水位是否超阈值预期百分比。 依赖时序库：internal-monitor-metric |
| 额度超限监控 | 监控 Project 下 LogStore 数超配额次数 依赖日志库：internal-error_log |  |  |
| [机器组监控](products/sls/documents/use-cloudlens-for-sls-to-monitor-project-resource-quotas.md) | 实时水位监控 | 监控 Project 下机器组数水位是否超阈值预期百分比。 依赖时序库：internal-monitor-metric |  |
| 额度超限监控 | 监控 Project 下机器组数超配额次数。 依赖日志库：internal-error_log |  |  |
| [Logtail](products/sls/documents/use-cloudlens-for-sls-to-monitor-project-resource-quotas.md) [采集配置](products/sls/documents/use-cloudlens-for-sls-to-monitor-project-resource-quotas.md) | 实时水位监控 | 监控 Project 下 Logtail 采集配置数水位是否超阈值预期百分比。 依赖时序库：internal-monitor-metric |  |
| 额度超限监控 | 监控 Project 下 Logtail 采集配置数超配额次数。 依赖日志库：internal-error_log |  |  |
| 数据读写资源配额 | [Project](products/sls/documents/use-cloudlens-for-sls-to-monitor-project-resource-quotas.md) [写入流量监控](products/sls/documents/use-cloudlens-for-sls-to-monitor-project-resource-quotas.md) | 实时水位监控 | 监控 Project 写入流量水位是否超阈值预期百分比。 依赖时序库：internal-monitor-metric |
| 额度超限监控 | 监控 Project 写入流量超配额次数。 依赖日志库：internal-error_log |  |  |
| [Project](products/sls/documents/use-cloudlens-for-sls-to-monitor-project-resource-quotas.md) [写入次数监控](products/sls/documents/use-cloudlens-for-sls-to-monitor-project-resource-quotas.md) | 实时水位监控 | 监控 Project 写入次数水位是否超阈值预期百分比。 依赖时序库：internal-monitor-metric |  |
| 额度超限监控 | 监控 Project 写入次数超配额次数。 依赖日志库：internal-error_log |  |  |


LogStore监控

## 实时水位监控

- 

单击新建告警，配置告警规则。

- 

选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。

- 

根据业务场景配置告警触发条件、以及告警策略。

根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告警监控规则](products/sls/documents/alarm-settings-quick-start.md)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | LogStore 数水位监控 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：指标库 授权方式：默认 指标库：internal-monitor-metric 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 * | select Project, region, round(count_logstore/quota_logstore * 100, 3) as logstore_ratio from (SELECT A.id as Project , A.region as region, COALESCE(SUM(B.count_logstore), 0) AS count_logstore , cast(json_extract(A.quota, '$.logstore') as double) as quota_logstore FROM "resource.sls.cmdb.project" as A LEFT JOIN ( SELECT project, COUNT(*) AS count_logstore FROM "resource.sls.cmdb.logstore" as B GROUP BY project ) AS B ON A.id = B.project group by A.id, A.quota, A.region) where quota_logstore is not null order by logstore_ratio desc limit 1000 |
| 分组评估 | 标签自动 |
| 触发条件 | 说明 当有 Project 的 LogStore 数超过额度的 90%时告警级别为严重。 当有 Project 的 LogStore 数超过额度的 80%时告警级别为中。 当有数据匹配 logstore_ratio > 90 时，严重度：严重。 当有数据匹配 logstore_ratio > 80 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。 |


- 

参数配置完成后，单击确定。

## 额度超限监控

- 

单击新建告警，配置告警规则。

- 

选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。

- 

根据业务场景配置告警触发条件、以及告警策略。

根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告警监控规则](products/sls/documents/alarm-settings-quick-start.md)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | LogStore 数额度超限 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：日志库 授权方式：默认 日志库：internal-error_log 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 * and (ErrorCode: ExceedQuota or ErrorCode: QuotaExceed or ErrorCode: ProjectQuotaExceed or ErrorCode:WriteQuotaExceed)| SELECT Project, COUNT(1) AS count where ErrorMsg like '%logstore count %' GROUP BY Project ORDER BY count DESC LIMIT 1000 |
| 分组评估 | 不分组 |
| 触发条件 | 说明 当有 Project 的 LogStore 发生超限 10 次错误告警级别为严重。 当有 Project 的 LogStore 发生超限 1 次错误时告警级别为中。 当有数据匹配 count > 10 时，严重度：严重。 当有数据匹配 count > 1 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。 |


- 

参数配置完成后，单击确定。

机器组监控

## 实时水位监控

- 

单击新建告警，配置告警规则。

- 

选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。

- 

根据业务场景配置告警触发条件、以及告警策略。

根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告监控规则](products/sls/documents/alarm-settings-quick-start.md)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | 机器组水位监控 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：指标库 授权方式：默认 指标库：internal-monitor-metric 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 * | select Project, region, round(count_machine_group/quota_machine_group * 100, 3) as machine_group_ratio from (SELECT A.id as Project , A.region as region, COALESCE(SUM(B.count_machine_group), 0) AS count_machine_group , cast(json_extract(A.quota, '$.machine_group') as double) as quota_machine_group FROM "resource.sls.cmdb.project" as A LEFT JOIN ( SELECT project, COUNT(*) AS count_machine_group FROM "resource.sls.cmdb.machine_group" as B GROUP BY project ) AS B ON A.id = B.project group by A.id, A.quota, A.region) where quota_machine_group is not null order by machine_group_ratio desc limit 1000 |
| 分组评估 | 标签自动 |
| 触发条件 | 说明 当有 Project 的机器组超过额度的 90%时告警级别为严重。 当有 Project 的机器组超过额度的 80%时告警级别为中。 当有数据匹配 machine_group_ratio > 90 时，严重度：严重。 当有数据匹配 machine_group_ratio > 80 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。 |


- 

参数配置完成后，单击确定。

## 额度超限监控

- 

单击新建告警，配置告警规则。

- 

选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。

- 

根据业务场景配置告警触发条件、以及告警策略。

根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告警监控规则](products/sls/documents/alarm-settings-quick-start.md)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | LogStore 数额度超限 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：日志库 授权方式：默认 日志库：internal-error_log 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 * and (ErrorCode: ExceedQuota or ErrorCode: QuotaExceed or ErrorCode: ProjectQuotaExceed or ErrorCode:WriteQuotaExceed)| SELECT Project, COUNT(1) AS count where ErrorMsg like '%machine group count%' GROUP BY Project ORDER BY count DESC LIMIT 1000 |
| 分组评估 | 不分组 |
| 触发条件 | 说明 当有 Project 的机器组发生超限 10 次错误告警级别为严重。 当有 Project 的机器组发生超限 1 次错误时告警级别为中。 当有数据匹配 count > 10 时，严重度：严重。 当有数据匹配 count > 1 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。 |


- 

参数配置完成后，单击确定。

Logtail采集配置

## 实时水位监控

- 

单击新建告警，配置告警规则。

- 

选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。

- 

根据业务场景配置告警触发条件、以及告警策略。

根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告警监控规则](products/sls/documents/alarm-settings-quick-start.md)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | Logtail 采集配置水位监控 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：指标库 授权方式：默认 指标库：internal-monitor-metric 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 * | select Project, region, round(count_logtail_config/quota_logtail_config * 100, 3) as logtail_config_ratio from (SELECT A.id as Project , A.region as region, COALESCE(SUM(B.count_logtail_config), 0) AS count_logtail_config , cast(json_extract(A.quota, '$.config') as double) as quota_logtail_config FROM "resource.sls.cmdb.project" as A LEFT JOIN ( SELECT project, COUNT(*) AS count_logtail_config FROM "resource.sls.cmdb.logtail_config" as B GROUP BY project ) AS B ON A.id = B.project group by A.id, A.quota, A.region) where quota_logtail_config is not null order by logtail_config_ratio desc limit 1000 |
| 分组评估 | 标签自动 |
| 触发条件 | 说明 当有 Project 的 Logtail 采集配置数超过额度的 90%时告警级别为严重。 当有 Project 的 Logtail 采集配置数超过额度的 80%时告警级别为中。 当有数据匹配 logtail_config_ratio > 90 时，严重度：严重。 当有数据匹配 logtail_config_ratio > 80 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。 |


- 

参数配置完成后，单击确定。

## 额度超限监控

- 

单击新建告警，配置告警规则。

- 

选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。

- 

根据业务场景配置告警触发条件、以及告警策略。

根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告警监控规则](products/sls/documents/alarm-settings-quick-start.md)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | Logtail 采集配置额度超限 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：日志库 授权方式：默认 日志库：internal-error_log 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 * and (ErrorCode: ExceedQuota or ErrorCode: QuotaExceed or ErrorCode: ProjectQuotaExceed or ErrorCode:WriteQuotaExceed)| SELECT Project, COUNT(1) AS count where ErrorMsg like '%config count%' GROUP BY Project ORDER BY count DESC LIMIT 1000 |
| 分组评估 | 不分组 |
| 触发条件 | 说明 当有 Project 的 Logtail 采集配置发生超限 10 次错误告警级别为严重。 当有 Project 的 Logtail 采集配置发生超限 1 次错误时告警级别为中。 当有数据匹配 count > 10 时，严重度：严重。 当有数据匹配 count > 1 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。 |


- 

参数配置完成后，单击确定。

Project写入流量监控

## 实时水位监控

- 

单击新建告警，配置告警规则。

- 

选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。

- 

根据业务场景配置告警触发条件、以及告警策略。

根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告警监控规则](products/sls/documents/alarm-settings-quick-start.md)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | Project 写入流量水位监控 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：指标库 授权方式：默认 指标库：internal-monitor-metric 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 (*)| SELECT Project, region , round(count_inflow/cast(quota_inflow as double) * 100, 3) as inflow_ratio FROM (SELECT cmdb.id as Project, cmdb.region as region, COALESCE(M.name1,0) as count_inflow, round(cast(json_extract(cmdb.quota, '$.inflow_per_min') as double)/1000000000, 3) as quota_inflow from "resource.sls.cmdb.project" as cmdb LEFT JOIN ( select project, round(MAX(name1)/1000000000, 3) as name1 from (SELECT __time_nano__ as time, element_at( split_to_map(__labels__, '|', '#$#') , 'project') as project, sum(CASE WHEN __name__ = 'logstore_origin_inflow_bytes' THEN __value__ ELSE NULL END) AS name1 FROM "internal-monitor-metric.prom" where __name__ ='logstore_origin_inflow_bytes' and regexp_like(element_at( split_to_map(__labels__, '|', '#$#') , 'project') , '.*') group by project,time )group by project) AS M ON cmdb.id = M.project )order by inflow_ratio desc limit 1000 |
| 分组评估 | 标签自动 |
| 触发条件 | 说明 当有 Project 写入流量超过额度的 90%时告警级别为严重。 当有 Project 写入流量超过额度的 80%时告警级别为中。 当有数据匹配 inflow_ratio > 90 时，严重度：严重。 当有数据匹配 inflow_ratio > 80 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。 |


- 

参数配置完成后，单击确定。

## 额度超限监控

- 

单击新建告警，配置告警规则。

- 

选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。

- 

根据业务场景配置告警触发条件、以及告警策略。

根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告警监控规则](products/sls/documents/alarm-settings-quick-start.md)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | Project 写入流量额度超限 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：日志库 授权方式：默认 日志库：internal-error_log 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 * and (ErrorCode: ExceedQuota or ErrorCode: QuotaExceed or ErrorCode: ProjectQuotaExceed or ErrorCode:WriteQuotaExceed)| SELECT Project, COUNT(1) AS count where ErrorMsg like '%Project write quota exceed: inflow%' GROUP BY Project ORDER BY count DESC LIMIT 1000 |
| 分组评估 | 不分组 |
| 触发条件 | 说明 当有 Project 写入流量发生超限 10 次错误告警级别为严重。 当有 Project 写入流量发生超限 1 次错误时告警级别为中。 当有数据匹配 count > 10 时，严重度：严重。 当有数据匹配 count > 1 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。 |


- 

参数配置完成后，单击确定。

Project写入次数监控

## 实时水位监控

- 

单击新建告警，配置告警规则。

- 

选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。

- 

根据业务场景配置告警触发条件、以及告警策略。

根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告警监控规则](products/sls/documents/alarm-settings-quick-start.md)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | Project 写入次数水位监控 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：指标库 授权方式：默认 指标库：internal-monitor-metric 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 (*)| SELECT Project, region, round(count_write_cnt/cast(quota_write_cnt as double) * 100, 3) as write_cnt_ratio FROM (SELECT cmdb.id as Project, cmdb.region as region, COALESCE(M.name1,0) as count_write_cnt, cast(json_extract(cmdb.quota, '$.write_cnt_per_min') as bigint) as quota_write_cnt from "resource.sls.cmdb.project" as cmdb LEFT JOIN ( select project, MAX(name1) as name1 from (SELECT __time_nano__ as time, element_at( split_to_map(__labels__, '|', '#$#') , 'project') as project, sum(CASE WHEN __name__ = 'logstore_write_count' THEN __value__ ELSE NULL END) AS name1 FROM "internal-monitor-metric.prom" where __name__ = 'logstore_write_count' and regexp_like(element_at( split_to_map(__labels__, '|', '#$#') , 'project') , '.*') group by project,time )group by project) AS M ON cmdb.id = M.project ) order by write_cnt_ratio desc limit 1000 |
| 分组评估 | 标签自动 |
| 触发条件 | 说明 当有 Project 写入次数超过额度的 90%时告警级别为严重。 当有 Project 写入次数超过额度的 80%时告警级别为中。 当有数据匹配 inflow_ratio > 90 时，严重度：严重。 当有数据匹配 inflow_ratio > 80 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。 |


在添加标注中，设置title的 value 为${alert_name}告警触发，设置desc的 value 为${alert_name}告警触发。

- 

参数配置完成后，单击确定。

## 额度超限监控

- 

单击新建告警，配置告警规则。

- 

选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。

- 

根据业务场景配置告警触发条件、以及告警策略。

根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告警监控规则](products/sls/documents/alarm-settings-quick-start.md)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | Project 写入次数额度超限 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：日志库 授权方式：默认 日志库：internal-error_log 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 * and (ErrorCode: ExceedQuota or ErrorCode: QuotaExceed or ErrorCode: ProjectQuotaExceed or ErrorCode:WriteQuotaExceed)| SELECT Project, COUNT(1) AS count where ErrorMsg like '%Project write quota exceed: qps%' GROUP BY Project ORDER BY count DESC LIMIT 1000 |
| 分组评估 | 不分组 |
| 触发条件 | 说明 当有 Project 写入次数发生超限 10 次错误告警级别为严重。 当有 Project 写入次数发生超限 1 次错误时告警级别为中。 当有数据匹配 count > 10 时，严重度：严重。 当有数据匹配 count > 1 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](products/sls/documents/create-an-action-policy.md) 。 |


- 

参数配置完成后，单击确定。

## 资源配额调整申请

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

单击图标。

- 

单击资源配额对应的管理。

- 

在资源配额面板中，调整目标资源的配额，然后单击保存。

[上一篇：使用CloudLens for SLS分析资源用量](products/sls/documents/use-cloudlens-for-sls-to-analyze-resource-usage.md)[下一篇：任务监控大盘异常处理](products/sls/documents/handle-errors-for-a-job-monitoring-dashboard.md)

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
