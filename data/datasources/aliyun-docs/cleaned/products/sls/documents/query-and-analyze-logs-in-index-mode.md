# 通过索引模式查询和分析日志-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/query-and-analyze-logs-in-index-mode

# 索引模式查询与分析
日志服务支持通过配置索引查询和分析日志。该功能结合了SQL计算功能。本文介绍查询与分析功能的基本语法、使用限制和SQL函数等信息。
## 阅读引导
日志服务提供查询和分析日志功能。具体操作，请参见[查询与分析快速指引](quick-guide-to-query-and-analysis.md)。
如果您要查询与分析日志，则必须将日志采集到Standard LogStore中，参考[管理](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。[创建索引](create-indexes.md)后，查询与分析只针对增量日志生效。当您需要对[历史日志文件](import-historical-logs.md)查询分析，需要[重建索引](reindex-logs-for-a-logstore.md)。
如果您需要查询百亿级的日志数据量，您可以参见[控制台提示“查询结果不精确”，如何解决？](what-are-the-reasons-for-inaccurate-queries.md)。
日志服务默认存在保留字段。如果您要分析保留字段，请参见[保留字段](reserved-fields.md)。
## 查询与分析
日志服务支持秒级查询十亿到千亿级别的日志，并支持通过SQL对查询结果进行统计分析。查询语句可单独使用，分析语句必须与查询语句一起使用，即分析功能是基于查询结果或全量数据进行的。
说明
[SLS Query Skill 智能查询分析日志](sls-query-skill-intelligent-log-query-and-analysis.md)：日志服务提供了Agent Skill，支持在本地 AI Agent 中通过自然语言查询和分析 SLS 日志数据。
[通过](copilot-automatic-generation-of-ai-assisted-sql-statements.md)[AI](copilot-automatic-generation-of-ai-assisted-sql-statements.md)[智能生成查询与分析语句（Copilot）](copilot-automatic-generation-of-ai-assisted-sql-statements.md)：日志服务也提供了AI智能辅助SQL语句的使用，支持自然语言生成SQL、解释复杂SQL、优化SQL语句。
### 基本语法
查询语句和分析语句以竖线|分割。查询语句可单独使用，分析语句必须与查询语句一起使用。即分析功能是基于查询结果或全量数据进行的。
查询语句|分析语句
| 类型 | 说明 |
| --- | --- |
| 查询语句 | 查询语句用于指定日志查询时的过滤规则，返回符合条件的日志。格式为： 查询语句 ，例如 status: 200 。 查询条件可使用关键词、数值、数值范围、空格、 * 等。 如果为空格或 * ，表示无过滤条件。更多信息，请参见 [查询语法与功能](query-syntax.md) 。 重要 查询语句中建议不超过 30 个条件。 |
| 分析语句 | 如需使用分析功能，则必须将日志采集到 Standard LogStore 中，且在配置索引时打开对应字段的 开启统计 开关。 分析语句对查询结果或全量数据进行计算和统计。日志服务支持的分析函数和语法，请参见： [SQL](sql-function.md) [函数](sql-function.md) ：SQL 函数通常用于对数据进行计算、转换和格式化。例如，计算总和、平均值、字符串操作、日期处理等。 [SQL](sql-syntax.md) [子句](sql-syntax.md) ：SQL 子句用于构建完整的 SQL 查询或数据操作语句，决定数据的来源、条件、分组、排序等。 [嵌套子查询](nested-subquery.md) ：嵌套子查询是指将一个 SELECT 语句嵌套在另一个 SELECT 语句中，用于复杂的分析场景。 [Logstore](join-queries-on-a-logstore-and-a-mysql-database.md) [和](join-queries-on-a-logstore-and-a-mysql-database.md) [MySQL](join-queries-on-a-logstore-and-a-mysql-database.md) [联合查询分析](join-queries-on-a-logstore-and-a-mysql-database.md) ：支持通过 Join 语法将 LogStore 与 MySQL 联合查询，结果可保存至 MySQL。 [使用](use-spl-to-query-and-analyze-logs.md) [SPL](use-spl-to-query-and-analyze-logs.md) [查询和分析日志](use-spl-to-query-and-analyze-logs.md) ：当您需要对日志数据进行结构化信息提取、字段操作和数据过滤时，可以使用 SPL。 重要 分析语句默认分析当前 LogStore 中的数据，不需要填写 FROM 子句和 WHERE 子句。 分析语句不支持使用 offset，不区分大小写，末尾不需要加分号。 |
日志服务查询分析提供了antlr语法文件，支持用户结合antlr工具进行基于SLS查询的二次开发。
以下是antlr语法文件：
[IndexQueryParser](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250814/jjzlqs/IndexQueryParser.g4)
[IndexQueryLexer](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250814/jodlnb/IndexQueryLexer.g4)
### 示例
* | SELECT status, count(*) AS PV GROUP BY status
查询与分析结果如下图所示：
## 高级功能
[LiveTail](livetail.md)：实现实时监控线上日志，减轻运维压力。
[日志聚类](logreduce.md)：采集日志时，提取相似日志的共同模式，快速了解日志全貌。
[上下文查询](contextual-query.md)：支持查看指定日志的上下文信息，方便故障排查和问题定位。
[字段分析](field-analysis.md)：提供字段分布、统计指标及TOP5时间序列图，帮助理解数据。
[事件配置](configure-events.md)：通过事件配置，轻松获取原始日志的详细信息。
[数据视图（StoreView）概述](dataset-storeview-overview.md)：：使用StoreView功能，实现跨地域、跨Store的联合查询。
[Copilot](copilot-automatic-generation-of-ai-assisted-sql-statements.md)：生成、解释和优化SQL语句。
## 查询功能使用限制
| 限制项 | 说明 |
| --- | --- |
| 关键词个数 | 关键词查询时，除布尔逻辑符外的条件个数。每次查询最多 30 个。 |
| 字段值大小 | 单个字段值最大为 512 KB，超出部分不参与查询。 如果单个字段长度大于 512 KB，有一定几率无法通过关键词查询到日志，但数据仍然是完整的。 说明 如需设置日志字段值的最大长度，请参见 [为什么查询和分析时，字段值会被截断？](index-and-query-faq.md) |
| 操作并发数 | 单个 Project 支持的最大查询操作并发数为 100 个。 例如 100 个用户同时在同一个 Project 的各个 LogStore 中执行查询操作。 |
| 返回结果 | 每次查询时，每页最多显示 100 条查询结果，您可翻页读取完整的查询结果。 |
| 模糊查询 | 执行模糊查询时，日志服务最多查询到符合条件的 100 个词，并返回包含这 100 个词并满足查询条件的所有日志。更多信息，请参见 [模糊查询](query-syntax.md) 。 |
| 查询结果排序 | 默认按照秒级时间（如果存在纳秒级则以纳秒级时间）从最新开始展示。 |
## 分析功能使用限制
| 限制项 | 普通实例 | SQL 独享实例 |  |
| --- | --- | --- | --- |
| SQL 增强 | 完全精确 |  |  |
| 并发数 | 单个 Project 支持的最大查询并发数为 15 个。 | 单个 Project 支持的最大查询并发数为 100 个。 | 单个 Project 支持的最大查询并发数为 5 个。 |
| 数据量 | 单次查询分析最大支持扫描 400MB 日志数据（不包含缓存数据），超过部分截断，标记为 查询结果不精确。 | 单次查询分析最大支持扫描 2GB 日志数据（不包含缓存数据），超过部分截断，标记为 查询结果不精确 。 | 无限制。 |
| 开启模式 | 默认开启。 | 通过开关开启。具体操作，请参见 [SQL](sql-enhancement.md) [增强](sql-enhancement.md) 。 | 通过开关开启。具体操作，请参见 [SQL](sql-completely-accurate.md) [完全精确](sql-completely-accurate.md) 。 |
| 费用 | 免费。 | 根据实际使用的 CPU 时间付费。 | 根据实际使用的 CPU 时间付费。 |
| 数据生效机制 | 分析功能只对开启统计功能后写入的数据生效。 如果您需要分析历史数据，请对历史数据 [重建索引](reindex-logs-for-a-logstore.md) 。 | 分析功能只对开启统计功能后写入的数据生效。 如果您需要分析历史数据，请对历史数据 [重建索引](reindex-logs-for-a-logstore.md) 。 | 分析功能只对开启统计功能后写入的数据生效。 如果您需要分析历史数据，请对历史数据 [重建索引](reindex-logs-for-a-logstore.md) 。 |
| 返回结果 | 执行分析操作后，默认最多返回 100 行数据，最大返回 100MB 的数据，超过 100MB 的分析语句会报错。 如果您需要返回更多数据，请使用 [LIMIT](limit-clause.md) [子句](limit-clause.md) 。 | 执行分析操作后，默认最多返回 100 行数据，最大返回 100MB 的数据，超过 100MB 的分析语句会报错。 如果您需要返回更多数据，请使用 [LIMIT](limit-clause.md) [子句](limit-clause.md) 。 | 执行分析操作后，默认最多返回 100 行数据，最大返回 100MB 的数据，超过 100MB 的分析语句会报错。 如果您需要返回更多数据，请使用 [LIMIT](limit-clause.md) [子句](limit-clause.md) 。 |
| 字段值大小 | 单个字段值最大长度的默认值为 2 KB（2048 字节），可调整配置最高支持 16 KB（16384 字节），但超出部分将不再参与日志分析和检索操作。 说明 如果您需要修改字段值的最大长度，可设置 统计字段（text）最大长度 。更新索引设置只对增量数据有效。具体操作，请参见 [创建索引](create-indexes.md) 。 | 单个字段值最大长度的默认值为 2 KB（2048 字节），可调整配置最高支持 16 KB（16384 字节），但超出部分将不再参与日志分析和检索操作。 说明 如果您需要修改字段值的最大长度，可设置 统计字段（text）最大长度 。更新索引设置只对增量数据有效。具体操作，请参见 [创建索引](create-indexes.md) 。 | 单个字段值最大长度的默认值为 2 KB（2048 字节），可调整配置最高支持 16 KB（16384 字节），但超出部分将不再参与日志分析和检索操作。 说明 如果您需要修改字段值的最大长度，可设置 统计字段（text）最大长度 。更新索引设置只对增量数据有效。具体操作，请参见 [创建索引](create-indexes.md) 。 |
| 超时时间 | 分析操作的最大超时的时间为 55 秒。 | 分析操作的最大超时的时间为 55 秒。 | 分析操作的最大超时的时间为 55 秒。 |
| Double 类型字段值位数 | Double 类型字段值最多 52 位。 如果浮点数编码位数超过 52 位，会造成精度损失。 | Double 类型字段值最多 52 位。 如果浮点数编码位数超过 52 位，会造成精度损失。 | Double 类型字段值最多 52 位。 如果浮点数编码位数超过 52 位，会造成精度损失。 |
## 常见问题
[查询与分析日志的常见报错](resolve-common-errors-that-may-occur-when-i-query-and-analyze-logs.md)
[如何模糊查询日志？](how-do-i-query-logs-by-using-fuzzy-match.md)
[如何精确查询日志？](how-do-i-query-logs-by-using-exact-match.md)
[如何在查询和分析语句中使用引号？](how-do-i-use-quotation-marks-in-query-statements.md)
## 相关文档
[常见分析案例](case-study.md)
[提高查询分析日志速度的方法](optimize-queries.md)
[查询和分析网站日志](query-and-analyze-website-logs.md)
[SQL](sql-syntax-and-functions.md)[分析语法与功能](sql-syntax-and-functions.md)
相关API
[通过时间查询](developer-reference/api-sls-2020-12-30-getcursor.md)[Cursor](developer-reference/api-sls-2020-12-30-getcursor.md)
[通过](developer-reference/api-sls-2020-12-30-getcursortime.md)[Cursor](developer-reference/api-sls-2020-12-30-getcursortime.md)[查询服务器端时间](developer-reference/api-sls-2020-12-30-getcursortime.md)
[GetLogs - 查询日志库日志（返回结果不压缩传输）](developer-reference/api-sls-2020-12-30-getlogs.md)
[GetLogsV2 - 查询](developer-reference/api-sls-2020-12-30-getlogsv2.md)[LogStore](developer-reference/api-sls-2020-12-30-getlogsv2.md)[中的日志数据（返回结果压缩后传输）](developer-reference/api-sls-2020-12-30-getlogsv2.md)
[查询上下文日志](developer-reference/api-sls-2020-12-30-getcontextlogs.md)
[查询日志分布情况](developer-reference/api-sls-2020-12-30-gethistograms.md)
[创建定时](developer-reference/api-sls-2020-12-30-createscheduledsql.md)[SQL](developer-reference/api-sls-2020-12-30-createscheduledsql.md)[任务](developer-reference/api-sls-2020-12-30-createscheduledsql.md)
[创建](developer-reference/api-sls-2020-12-30-createsqlinstance.md)[SQL](developer-reference/api-sls-2020-12-30-createsqlinstance.md)[独享实例](developer-reference/api-sls-2020-12-30-createsqlinstance.md)
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
