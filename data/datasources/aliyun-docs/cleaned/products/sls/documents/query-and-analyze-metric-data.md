# 如何在MetricStore中查询和分析时序数据-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/query-and-analyze-metric-data

# 查询和分析时序数据
本文介绍如何在日志服务MetricStore中查询和分析时序数据、设置时序图图例名称等相关操作。
## 前提条件
已采集到时序数据。
## 操作步骤
说明
在日志服务MetricStore查询和分析页面，只支持使用PromQL查询语法。如果您要使用标准SQL语法或SQL+PromQL组合语法，请选择更多操作>自定义分析，在LogStore查询和分析页面进行。
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在时序存储>时序库页签中，单击目标MetricStore。
在页面右上角，单击15分钟（相对），设置查询和分析的时间范围。
说明
查询和分析结果相对于指定的时间范围来说，存在1分钟以内的误差。
执行查询和分析操作。
您可以通过如下方式输入查询和分析语句。
直接输入PromQL语句，单击立即执行。
日志服务支持添加多个查询和分析操作以及在时序图中叠加展示多个查询和分析结果。
在Metrics探索框中，单击目标监控项对应的图标，日志服务将自动生成查询和分析语句。
您也可以在Metrics探索框中，单击目标监控项对应的继续探索，设置标签值。日志服务将根据您的设置，自动生成查询和分析语句。具体操作，请参见[指标探索](query-and-analyze-metric-data.md)。
输入PromQL语句时，编辑器支持自动补全功能，会根据已输入内容列出匹配的函数（如abs、avg、avg_over_time等）和指标名称，供您快速选择。
## 校验PromQL语法
开启自动树状解析功能后，输入PromQL语句，系统将提示PromQL函数、聚合函数、指标名、标签名、标签值、时间范围等信息。更多信息，请参见[Prometheus](https://prometheus.io/docs/prometheus/latest/querying/functions/)[官方文档](https://prometheus.io/docs/prometheus/latest/querying/functions/)。
输入PromQL语句时，日志服务还支持实时进行语法校验。
正确语法
如果提示语法正确，表示校验通过且生成语法解析树。
错误语法
如果出现错误信息，表示校验不通过，仅生成部分语法解析树且提示错误位置与原因。
以下为存在语法错误的 PromQL 示例，其中[5]缺少时间单位（如m、s、h），导致解析错误4:1 parse error: unexpected <aggr:sum>：
label_replace( sum by(pod_name)( rate(container_cpu_usage_seconds_total{namespace= "redash"}[5]) ), "pod", "$1", "pod_name", "(.+)" )
在校验过程中，您还可以执行如下操作。
单击图标，刷新语法解析树。
单击图标，简化展示语法解析树中的节点信息。
单击图标、图标，展开或收起节点。
单击图标、图标，开启或关闭自动树状解析功能。
## 指标探索
单击Metric探索，日志服务将展示指标信息，并且支持您继续探索指标下的Label数据。在Metrics 探索页面，可通过搜索栏按名称检索指标。页面以双列表格展示检索到的指标列表（如cpu_count、cpu_guest_util、cpu_sys_util等），并显示指标总数及查询时间范围。每个指标的操作栏提供继续探索、复制和添加功能。
在Metric探索面板中，您可以执行如下操作。
设置时间范围：为保证响应速度，指标探索的默认查询范围为最近5分钟。如果您的MetricStore记录间隔较长或者您有自定义需求，可单击更改修改时间范围。
单击图标，可将查询时间范围恢复为默认设置。
过滤指标：在搜索框中，输入指标名称，过滤指标。
复制指标名称：单击图标，复制指标名称。
添加到查询框：单击图标，将指标名添加到查询框中。
继续探索：单击继续探索，查看指标的Label数据，包括标签名、唯一数、标签值示例等信息。
您可以单击筛选，设置标签值。此处支持PromQL语法的4种操作符、支持选择或手动输入筛选条件、支持正则表达式。
设置完成后，系统自动显示对应的查询和分析语句，您可以单击复制查询语句或添加到查询框，进行查询和分析操作。
## 设置图例格式化
执行查询和分析操作后，您可以设置时序图图例的显示名称。
步长默认会根据查询时间段的长度进行调整，同时支持自定义。
默认由Metric name和Labels拼接组成时序图图例名称，日志服务支持使用变量引用Labels中指定的值，格式为{{值名称}}。例如Labels为{ip="192.0.2.1"}，则将图例格式化设置为{{ip}}后，时序图图例显示为192.0.2.1。在查询输入框下方的配置行中，找到图例格式化右侧的输入框，输入自定义的图例名称格式。
## 相关操作
| 操作 | 说明 |
| --- | --- |
| 指标统计 | 单击 指标统计 ，系统将跳转至 指标统计 仪表盘。该仪表盘展示时序库重要统计信息，包含数据量、指标数、时间线、数据条目、Top 类指标的快速定位和同环比变化等信息。 |
| 指标治理 | 单击 指标治理 ，系统将跳转至 指标治理 仪表盘。该仪表盘展示重点指标的时序场景分析结果、提供重点指标的时序图变化、提供看板式指标摘要统计、提供原生统计->数据分析->优化效果->异常诊断链路式解决方案。 |
| 查看表格数据 | 打开 表格数据 开关，系统将以表格形式展示查询和分析结果。 |
| 预览原始数据 | 单击 预览原始数据 ，系统将展示原始的时序数据。 |
| 数据加工 | 选择 更多操作 > 数据加工 ，进行数据加工操作。更多信息，请参见 [数据加工概述](data-transformation-overview.md) 。 |
| 自定义分析 | 选择 更多操作 > 自定义分析 ，系统将跳转到对应的 LogStore 查询和分析页面，支持 SQL 查询、SQL+PromQL 查询。 |
| 定时保存分析结果 | 选择 更多操作 > 另存为定时 SQL ，将时序数据通过定时 SQL 处理后存储到目标 MetricStore 中。具体操作，请参见 [创建定时](metricstore-import-metricstore.md) [SQL-时序库导入时序库](metricstore-import-metricstore.md) 。 |
| 添加到仪表盘 | 单击 添加到仪表盘 ，将查询和分析结果添加到仪表盘中。具体操作，请参见 [添加统计图表到仪表盘](add-a-chart-to-a-dashboard.md) 。 将时序图添加到仪表盘后，您可以自定义修改时序图属性。更多信息，请参见 [时序图](time-series-chart.md) 。 |
| 另存为告警 | 单击 另存为告警 ，为查询和分析结果设置告警。具体操作，请参见 [设置告警](configure-an-alert-rule.md) 。 |
| 复制查询和分析窗口 | 单击 图标，复制当前的查询和分析，新增一个查询和分析窗口。 |
| 删除查询和分析窗口 | 单击 图标，删除当前的查询和分析窗口。 |
| 刷新数据 | 单击 立即执行 右侧的 ，设置对应的刷新时间。日志服务会根据您的设置，定期自动刷新 MetricStore。 |
| 分享 | 单击 ，复制当前 MetricStore 查询和分析页面的链接。您可以将该链接发送给有查看该 MetricStore 权限的其他用户。其他用户看到的 MetricStore 查询和分析页面会保留您的一系列设置。 |
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
