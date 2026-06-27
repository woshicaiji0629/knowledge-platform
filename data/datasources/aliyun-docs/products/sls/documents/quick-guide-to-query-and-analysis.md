# 快速完成查询与分析日志-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/quick-guide-to-query-and-analysis

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

# 查询与分析快速指引

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

日志服务提供查询和分析功能，支持秒级查询十亿到千亿级别的日志，并支持通过SQL对查询结果进行统计分析。本文以Nginx日志为例，为您介绍如何快速开启索引，并在控制台完成查询与分析的基本操作。

## 前提条件

已创建Project、标准型LogStore并完成日志采集。具体操作，请参见[管理](products/sls/documents/manage-a-project.md)[Project](products/sls/documents/manage-a-project.md)、[创建基础](products/sls/documents/manage-a-logstore.md)[LogStore](products/sls/documents/manage-a-logstore.md)和[数据采集概述](products/sls/documents/data-collection-overview.md)。

## 步骤一：配置索引

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在日志存储>日志库页签中，单击目标Logstore。

- 

在LogStore的查询和分析页面，单击开启索引。

说明

开启后等待1min左右即可查询最新数据。

- 

单击开启索引后，全文索引开关默认打开。在查询分析页面单击自动生成索引。日志服务会根据采集时预览数据中的第一条内容，自动生成字段索引。

说明

其他配置项保持默认即可，更多信息，请参见[创建索引](products/sls/documents/create-indexes.md)。

生成的字段索引配置如下所示：

## 步骤二：查询和分析日志

说明

- 

[SLS Query Skill 智能查询分析日志](products/sls/documents/sls-query-skill-intelligent-log-query-and-analysis.md)：日志服务提供了Agent Skill，支持在本地 AI Agent 中通过自然语言查询和分析 SLS 日志数据。

- 

[通过](products/sls/documents/copilot-automatic-generation-of-ai-assisted-sql-statements.md)[AI](products/sls/documents/copilot-automatic-generation-of-ai-assisted-sql-statements.md)[智能生成查询与分析语句（Copilot）](products/sls/documents/copilot-automatic-generation-of-ai-assisted-sql-statements.md)：日志服务也提供了AI智能辅助SQL语句的使用，支持自然语言生成SQL、解释复杂SQL、优化SQL语句。

在查询 / 分析页面的搜索栏，输入查询或分析语句，并单击查询 / 分析。

- 

### 查询语句

用于日志数据的查看、简单搜索和过滤。用户使用查询语句，通过特定条件（例如时间范围、请求类型、关键字等）筛选出感兴趣的数据集。查询语句可以单独使用，具体用法请参见[查询语法与功能](products/sls/documents/query-syntax.md)。

示例：查询状态码为200的日志，可使用以下语句。

status :200

更多查询示例，请参见[查询语句示例](products/sls/documents/query-syntax.md)。

- 

### 分析语句

用于对日志数据进行过滤、转换、统计、聚合等操作，例如统计一段时间内数据的平均值、获取数据的同比和环比结果。分析语句必须配合查询语句一起使用，格式为查询语句|分析语句，语法说明请参见[SQL](products/sls/documents/sql-syntax-and-functions.md)[分析语法与功能](products/sls/documents/sql-syntax-and-functions.md)。

示例：查询日志中所有记录，并分析各请求状态的数量，可使用以下语句。

* | SELECT status, count(*) AS PV GROUP BY status

更多查询分析示例，请参见[SQL](products/sls/documents/sql-function.md)[函数](products/sls/documents/sql-function.md)和[SQL](products/sls/documents/sql-syntax.md)[子句](products/sls/documents/sql-syntax.md)。

说明

默认情况下，在日志库列表单击LogStore时，系统会进入查询 / 分析页面并自动执行一次查询操作。您可单击页面右上角的图标，在查询设置页签下，关闭该功能或设置查询时间。

## 配置时间范围

您可通过以下三种方式设置日志查询 / 分析的时间范围。如果在分析语句中设置了时间范围，则查询分析结果以该时间范围为准。

- 

在页面顶端的下拉列表中，选择时间范围例如15分钟。

- 

在分析语句中通过__time__字段指定时间范围（闭合区间），例如：

* | SELECT * FROM log WHERE __time__>1731297600 AND __time__< 1731310038

- 

在分析语句中指定时间时，使用[from_unixtime](products/sls/documents/date-and-time-functions-1.md)[函数](products/sls/documents/date-and-time-functions-1.md)或[to_unixtime](products/sls/documents/date-and-time-functions-1.md)[函数](products/sls/documents/date-and-time-functions-1.md)转换时间格式。例如：

- * | SELECT * FROM log WHERE from_unixtime(__time__) > from_unixtime(1731297600) AND from_unixtime(__time__) < now()

- * | SELECT * FROM log WHERE __time__ > to_unixtime(date_parse('2024-10-19 15:46:05', '%Y-%m-%d %H:%i:%s')) AND __time__ < to_unixtime(now())

说明

执行查询和分析语句后，默认只返回100行。如果您希望返回更多数据，可使用LIMIT语法。更多信息，请参见[LIMIT](products/sls/documents/limit-clause.md)[子句](products/sls/documents/limit-clause.md)。

## 查询/分析页面说明

### 页面概览

### 直方图

- 

将鼠标悬浮在绿色数据块上时，您可以查看该数据块代表的时间范围和日志命中次数。

- 

双击绿色数据块，您可以查看更细时间粒度的日志分布，同时原始日志页签中将同步展示指定时间范围内的查询结果。

### 原始日志

- 日志详情

- 

单击表格或原始，切换日志格式。

- 

>下载日志：可下载日志到本地。具体操作，请参见[下载日志](products/sls/documents/download-logs.md)。

- 

>JSON设置：设置JSON展示类型和展示级别。

- 

>事件配置：为原始日志[配置事件](products/sls/documents/configure-events.md)。

- 

：复制日志内容。

- 

：SLS Copilot，基于日志内容总结信息、查找错误信息等。

- 

：查看指定日志在原始文件中的上下文信息。只有通过Logtail采集到的日志才支持上下文浏览功能。具体操作，请参见[上下文查询](products/sls/documents/contextual-query.md)。

- 

：实时监控日志内容，提取关键日志信息。只有通过Logtail采集到的日志才支持LiveTail功能。 具体操作，请参见[LiveTail](products/sls/documents/livetail.md)。

- 显示字段

- 

在显示字段区域，单击目标字段后的，将索引字段从显示字段中清除，右侧的日志信息中不再显示。

- 

：收藏视图。在区域5设置显示字段后，可以收藏显示视图。在区域4上方的下拉列表选择视图。

- 

>tag设置：将字段设置为系统Tag。

- 

>别名：开启后，字段名称将被别名替换，未设置别名的字段仍展示字段名称。设置字段别名的步骤，请参见[创建索引](products/sls/documents/create-indexes.md)。

- 索引字段

- 

在索引字段区域，单击目标字段后的，将字段添加到显示字段中，在右侧的日志信息中显示。

- 

：查看字段的基本分布情况、统计指标等信息。具体操作，请参见[字段设置](products/sls/documents/quick-analysis.md)。

### 统计图表

统计图表是日志服务根据查询与分析语句渲染出的结果。日志服务提供表格、线图、柱状图等多种图表类型。具体操作，请参见[统计图表](products/sls/documents/statistical-charts.md)。 执行查询和分析语句后，您可以在统计图表页签中查看可视化的查询和分析结果。

本页签其他功能说明：

- 

添加到仪表盘：仪表盘是日志服务提供的实时数据分析大盘。单击添加到仪表盘，将查询和分析结果以图表形式保存到仪表盘中。具体操作，请参见[可视化概述](products/sls/documents/overview-of-visualization.md)。

- 

另存为定时SQL：日志服务提供定时SQL功能，用于定时分析数据、存储聚合数据、投影与过滤数据。具体操作，请参见[定时](products/sls/documents/how-scheduled-sql-works.md)[SQL](products/sls/documents/how-scheduled-sql-works.md)。

- 

交互事件：交互事件是数据分析中不可缺少的功能之一，通过改变数据维度的层次、变换分析的粒度从而获取数据中更详尽的信息。具体操作，请参见[为仪表盘添加交互事件实现下钻分析](products/sls/documents/drill-down-events.md)。

### 日志聚类

在日志聚类页签中，单击开启日志聚类，可实现在采集日志时聚合相似度高的日志。具体操作，请参见[日志聚类](products/sls/documents/logreduce.md)。

### SQL增强

单击右上角图标，可单次开启SQL独享版。当您在使用SQL分析时，如果数据量较大，日志服务无法在一次查询中完整分析这个时间段内的所有日志。通过开启SQL独享版，增加计算资源，可以提升单次分析的数据量。如需设置默认开启，请参见[高性能完全精确查询与分析（SQL](products/sls/documents/dedicated-sql.md)[独享版）](products/sls/documents/dedicated-sql.md)。

### 告警

单击右上角图标，将查询和分析结果另存为告警。具体操作，请参见[告警设置快速入门](products/sls/documents/alarm-settings-quick-start.md)。

### 快速查询

单击右上角图标，将当前查询和分析语句另存为快速查询。您可通过保存的历史操作，快速执行查询和分析操作。具体操作，请参见[快速查询](products/sls/documents/saved-search.md)。

### 分享

单击右上角图标，复制本页面链接，分享给其他用户。具体操作，请参见[控制台内嵌及分享](products/sls/documents/developer-reference/embed-console-pages-and-share-log-data.md)。

### 数据加工

单击左上角数据加工，可跳转至数据加工页面。数据加工服务可应用于数据规整与信息提取、数据清洗与过滤、数据分发至多目标LogStore等数据处理场景。具体操作，请参见[创建数据加工（新版）任务](products/sls/documents/create-a-data-processing-new-version-job.md)。

## 相关文档

- 

[查询语法与功能](products/sls/documents/query-syntax.md)

- 

[SQL](products/sls/documents/sql-syntax-and-functions.md)[分析语法与功能](products/sls/documents/sql-syntax-and-functions.md)

- 

[时间字段转换示例](products/sls/documents/time-field-conversion-examples.md)

- 

[查询和分析网站日志](products/sls/documents/query-and-analyze-website-logs.md)

- 

[查询和分析](products/sls/documents/query-and-analyze-json-logs.md)[JSON](products/sls/documents/query-and-analyze-json-logs.md)[日志](products/sls/documents/query-and-analyze-json-logs.md)

- 

[分析负载均衡](products/sls/documents/analyze-layer-7-access-logs-of-slb.md)[7](products/sls/documents/analyze-layer-7-access-logs-of-slb.md)[层访问日志](products/sls/documents/analyze-layer-7-access-logs-of-slb.md)

- 

[查询与分析常见问题](products/sls/documents/user-guide/faq-about-query-and-analysis.md)

[上一篇：查询与分析](products/sls/documents/index-and-query.md)[下一篇：通过AI智能生成查询与分析语句（Copilot）](products/sls/documents/copilot-automatic-generation-of-ai-assisted-sql-statements.md)

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
