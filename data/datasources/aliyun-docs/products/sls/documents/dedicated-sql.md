# 超大规模数据的SQL查询分析-SQL独享版-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/dedicated-sql

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

# 高性能完全精确查询与分析（SQL独享版）

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当数据量较大时，SQL普通版可能存在查询不完整的情况。SQL独享版通过增加计算资源，显著提升单次分析性能和数据量上限。本文介绍SQL独享版的概念、原理、费用及使用限制。

## 为什么要使用SQL独享版

### 普通查询的局限性

普通查询在超大规模数据处理时存在以下局限：

- 

结果不精确：资源限制（如时间片、IO、数据量）可能导致部分数据未加载，影响统计准确性。

- 

性能瓶颈：单Shard仅支持400MB数据量，TB级日志量或更高并发的分析需求可能会受限。

- 

资源竞争：多租户共享资源，可能会出现局部的资源竞争。

### SQL独享版的核心价值

增强模式：高性能与高并发

增强模式适合实时性和高并发需求的场景，核心特点包括：

- 

性能提升：单节点处理能力达2GB，最大支持100并发。

- 

弹性伸缩：按需动态分配资源，存储和计算能力可弹性伸缩。

- 

典型场景：实时监控（如API成功率告警）、高并发点查分析。

完全精确

完全精确模式适合对结果精度要求极高的场景，核心特点包括：

- 

零误差保证：通过时间换资源策略，确保数据完整加载。

- 

独享资源：稳定运行直至完成或超时。

- 

典型场景：严肃分析场景，如财务对账、安全审计、超长时间周期、超大规模趋势分析等。

重要

SQL最大执行时间为55秒，并发上限为5。

| 对比维度 | 增强模式 | 完全精确模式 |
| --- | --- | --- |
| 核心目标 | 性能加速 | 结果精确 |
| 资源策略 | 共享资源池、弹性伸缩 | 独享资源池 + 时间换精度 |
| 典型场景 | 实时监控、高并发分析 | 严肃分析场景，如财务对账、安全审计、超长时间周期、超大规模趋势分析等。 |
| 精度容忍 | 允许有限误差 | 零误差刚性需求 |


## SQL独享版介绍

### SQL增强

日志服务中的数据必定保存在某一个[分区（Shard）](products/sls/documents/manage-shards.md)。当使用SQL分析时，单个分区（Shard）的数据处理能力有限，如果数据规模过大，可能会存在性能问题或数据扫描过程被截断。增加Shard数量可以提升读写能力，但只对新写入的数据生效，而且可能导致[实时消费](products/sls/documents/overview-of-real-time-consumption.md)的客户端过多。[SQL](products/sls/documents/sql-enhancement.md)[增强](products/sls/documents/sql-enhancement.md)在资源调度上实现弹性伸缩，使SQL分析能力得以动态提升，典型场景包括：

- 

分析性能要求高的场景，例如实时数据分析。

- 

长周期的数据分析场景，例如月维度的数据分析。

- 

超大规模的数据分析场景，例如千亿行数据的分析。

- 

高并发的数据分析场景，例如多指标多维度（SQL并发数大于15）的报表分析、点查分析。

### SQL完全精确

日志服务在进行超大规模数据分析时，以下几种情况可能导致数据加载中断：

- 

时间片耗尽：分配的时间资源用完。

- 

数据量超过阈值：加载的数据总量超出限制。

- 

数据行数超过阈值：加载的行数超出限制。

- 

IO操作次数超过阈值：数据的磁盘读取次数超出限制。

这些情况均可能导致部分数据未能完全加载，从而影响最终结果的精确性，[SQL](products/sls/documents/sql-completely-accurate.md)[完全精确](products/sls/documents/sql-completely-accurate.md)可以解决这些问题。典型的场景包括：

- 

业务监控告警：关键业务监控要求数据分析结果精确。

- 

业务运营分析：严肃分析场景，如涉及营收、财务、留存、转化等关键指标的分析。

- 

在线数据服务：基于SQL分析结果对外部用户提供数据服务，要求分析结果必须准确无误。

## 计费信息

按照SQL分析时实际使用的CPU时间计算。单位为核×小时，即1核计算资源独享使用1小时的费用。更多信息，请参见[SQL](products/sls/documents/billing-examples.md)[独享版计费案例](products/sls/documents/billing-examples.md)。

- 

按量付费：SQL独享版费用=CPU时间（小时）×每小时单价

- 

资源包：新版资源包（预付计划2.0），换算成资源额度（CU）进行抵扣。

## 分析功能使用限制

| 限制项 | 普通实例 | SQL 独享实例 |  |
| --- | --- | --- | --- |
| SQL 增强 | 完全精确 |  |  |
| 并发数 | 单个 Project 支持的最大查询并发数为 15 个。 | 单个 Project 支持的最大查询并发数为 100 个。 | 单个 Project 支持的最大查询并发数为 5 个。 |
| 数据量 | 单次查询分析最大支持扫描 400MB 日志数据（不包含缓存数据），超过部分截断，标记为 查询结果不精确。 | 单次查询分析最大支持扫描 2GB 日志数据（不包含缓存数据），超过部分截断，标记为 查询结果不精确 。 | 无限制。 |
| 开启模式 | 默认开启。 | 通过开关开启。具体操作，请参见 [SQL](products/sls/documents/sql-enhancement.md) [增强](products/sls/documents/sql-enhancement.md) 。 | 通过开关开启。具体操作，请参见 [SQL](products/sls/documents/sql-completely-accurate.md) [完全精确](products/sls/documents/sql-completely-accurate.md) 。 |
| 费用 | 免费。 | 根据实际使用的 CPU 时间付费。 | 根据实际使用的 CPU 时间付费。 |
| 数据生效机制 | 分析功能只对开启统计功能后写入的数据生效。 如果您需要分析历史数据，请对历史数据 [重建索引](products/sls/documents/reindex-logs-for-a-logstore.md) 。 | 分析功能只对开启统计功能后写入的数据生效。 如果您需要分析历史数据，请对历史数据 [重建索引](products/sls/documents/reindex-logs-for-a-logstore.md) 。 | 分析功能只对开启统计功能后写入的数据生效。 如果您需要分析历史数据，请对历史数据 [重建索引](products/sls/documents/reindex-logs-for-a-logstore.md) 。 |
| 返回结果 | 执行分析操作后，默认最多返回 100 行数据，最大返回 100MB 的数据，超过 100MB 的分析语句会报错。 如果您需要返回更多数据，请使用 [LIMIT](products/sls/documents/limit-clause.md) [子句](products/sls/documents/limit-clause.md) 。 | 执行分析操作后，默认最多返回 100 行数据，最大返回 100MB 的数据，超过 100MB 的分析语句会报错。 如果您需要返回更多数据，请使用 [LIMIT](products/sls/documents/limit-clause.md) [子句](products/sls/documents/limit-clause.md) 。 | 执行分析操作后，默认最多返回 100 行数据，最大返回 100MB 的数据，超过 100MB 的分析语句会报错。 如果您需要返回更多数据，请使用 [LIMIT](products/sls/documents/limit-clause.md) [子句](products/sls/documents/limit-clause.md) 。 |
| 字段值大小 | 单个字段值最大长度的默认值为 2 KB（2048 字节），可调整配置最高支持 16 KB（16384 字节），但超出部分将不再参与日志分析和检索操作。 说明 如果您需要修改字段值的最大长度，可设置 统计字段（text）最大长度 。更新索引设置只对增量数据有效。具体操作，请参见 [创建索引](products/sls/documents/create-indexes.md) 。 | 单个字段值最大长度的默认值为 2 KB（2048 字节），可调整配置最高支持 16 KB（16384 字节），但超出部分将不再参与日志分析和检索操作。 说明 如果您需要修改字段值的最大长度，可设置 统计字段（text）最大长度 。更新索引设置只对增量数据有效。具体操作，请参见 [创建索引](products/sls/documents/create-indexes.md) 。 | 单个字段值最大长度的默认值为 2 KB（2048 字节），可调整配置最高支持 16 KB（16384 字节），但超出部分将不再参与日志分析和检索操作。 说明 如果您需要修改字段值的最大长度，可设置 统计字段（text）最大长度 。更新索引设置只对增量数据有效。具体操作，请参见 [创建索引](products/sls/documents/create-indexes.md) 。 |
| 超时时间 | 分析操作的最大超时的时间为 55 秒。 | 分析操作的最大超时的时间为 55 秒。 | 分析操作的最大超时的时间为 55 秒。 |
| Double 类型字段值位数 | Double 类型字段值最多 52 位。 如果浮点数编码位数超过 52 位，会造成精度损失。 | Double 类型字段值最多 52 位。 如果浮点数编码位数超过 52 位，会造成精度损失。 | Double 类型字段值最多 52 位。 如果浮点数编码位数超过 52 位，会造成精度损失。 |


[上一篇：图文解析带你精通时序PromQL语法](products/sls/documents/promql-deep-dive.md)[下一篇：SQL增强](products/sls/documents/sql-enhancement.md)

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
