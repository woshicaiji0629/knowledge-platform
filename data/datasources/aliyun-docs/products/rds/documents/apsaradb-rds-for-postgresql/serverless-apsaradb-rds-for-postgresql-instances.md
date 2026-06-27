# 数据库计算资源自动弹性扩缩容-Serverless实例-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/serverless-apsaradb-rds-for-postgresql-instances

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-postgresql/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-postgresql/getting-started.md)

- [DuckDB分析加速](products/rds/documents/apsaradb-rds-for-postgresql/duckdb-analytics-acceleration.md)

- [RDS for AI](products/rds/documents/apsaradb-rds-for-postgresql/rds-for-ai.md)

- [自研内核 AliPG](products/rds/documents/apsaradb-rds-for-postgresql/proprietary-alipg.md)

- [插件](products/rds/documents/apsaradb-rds-for-postgresql/plug-ins-1.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-postgresql/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-postgresql/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-postgresql/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-postgresql/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-postgresql/support.md)

[首页](https://help.aliyun.com/zh)

# Serverless实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

为了应对不断变化的业务需求，使数据库资源能够适应业务规模的快速变化，避免资源浪费和控制数据库运维成本，云数据库RDS PostgreSQL Serverless实例提供了实时弹性能力。通过本文档，您将了解到Serverless实例的特性、架构和使用方法，帮助您降低成本和提高运营效率。

## 介绍

RDS PostgreSQL Serverless实例提供了CPU、内存的实时弹性能力，构建云盘架构下的RDS PostgreSQL产品新形态。实例不仅提供网络资源、命名空间、存储空间的垂直资源隔离能力，还提供计算资源按需计费的能力，具有资源用量低、简单易用、弹性灵活和价格低廉等优点，赋能用户面向业务峰谷时对计算能力进行快速且独立的扩缩容要求，做到快速响应业务变化的同时，合理优化使用成本，进一步助力企业降本增效。

说明

- 

RDS PostgreSQL Serverless实例计算资源的单位是RCU（RDS Capacity Unit），1个RCU的性能约为1核（最大）2 GB，实例计算资源会在您指定的RCU范围内自动伸缩。

- 

RDS PostgreSQL Serverless实例的最大连接数固定为2400，不支持调整，也不会随RCU的变化而改变。

在业务波动较大的场景下，普通实例和Serverless实例资源使用和规格变化情况如下图所示：

由上图可以看到，在业务波动较大的场景下：

- 

普通实例：在波谷期浪费的资源较多，在高峰期资源不足，业务受损。

- 

Serverless实例：

- 

由于其计算资源随业务需求量随时调整，总体浪费的资源很少，提升了资源利用率，降低了资源使用成本。

- 

在高峰期也能完全满足业务需求，保证业务不受损，提高了系统的稳定性。

- 

打破固定资源付费的模式，做到真正负载与资源动态匹配的按量付费，可节省大量成本。

- 

无需手动变配，提高了运维效率，降低了运维管理人员和开发人员的运维成本。

- 

支持自动启停能力。当没有连接时，实例自动暂停，释放计算资源节约成本；当有连接建立时，自动启动。

- 

对高吞吐写入场景和高并发业务进行了设计优化，同时提供了弹性伸缩能力，适合业务数据量大、并具有典型的业务访问波峰波谷场景。

## 优势

- 

更低的成本：对于创业初期的企业，PostgreSQL Serverless不依赖其他的基础设施和相关服务，即买即用并可以提供稳定和高效的数据存取服务。使用期间只需要为占用的资源按使用量付费。

- 

更大的存储空间：存储空间最大可高达32 TB，根据实例数据量自动扩展，可以有效避免集群存储资源不足对业务造成影响。

- 

计算资源自动弹性扩缩容：用户读取和写入需要的计算资源可弹性伸缩，极大减少了运维成本和系统风险。

- 

全面托管和免运维：系统部署、扩缩容、报警处理等所有运维工作由阿里云专业团队完成，用户无感知，业务无影响，服务持续可用，真正免运维。

## 适用场景

- 

开发、测试环境等低频数据库使用场景

- 

中小企业建站服务等SaaS应用场景

- 

个人开发者用户

- 

学校教学、学生实验等教育场景

- 

物联网（IoT）、边缘计算等不确定负载场景

- 

全托管或希望完全免运维的用户

- 

业务有波动或不可预测的用户

- 

具有间歇性定时任务的业务场景

## 计费说明

[Serverless](products/rds/documents/apsaradb-rds-for-postgresql/pricing-of-serverless-apsaradb-rds-for-sql-server-instances.md)[费用](products/rds/documents/apsaradb-rds-for-postgresql/pricing-of-serverless-apsaradb-rds-for-sql-server-instances.md)

## 使用方法

- 

[创建](products/rds/documents/apsaradb-rds-for-postgresql/create-a-serverless-apsaradb-rds-for-postgresql-instance.md)[RDS PostgreSQL Serverless](products/rds/documents/apsaradb-rds-for-postgresql/create-a-serverless-apsaradb-rds-for-postgresql-instance.md)[实例](products/rds/documents/apsaradb-rds-for-postgresql/create-a-serverless-apsaradb-rds-for-postgresql-instance.md)

- 

[变更资源扩缩容范围（RCU）](products/rds/documents/apsaradb-rds-for-postgresql/change-the-scaling-range-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md)

根据实际业务需求，您可以调整Serverless实例的计算资源扩缩容范围，包括最小RCU和上限RCU，以实现资源的优化配置。

- 

[定时配置](products/rds/documents/apsaradb-rds-for-postgresql/configure-scheduled-tasks-to-adjust-the-number-of-rcus-for-serverless-apsaradb-rds-instances.md)[Serverless](products/rds/documents/apsaradb-rds-for-postgresql/configure-scheduled-tasks-to-adjust-the-number-of-rcus-for-serverless-apsaradb-rds-instances.md)[实例的](products/rds/documents/apsaradb-rds-for-postgresql/configure-scheduled-tasks-to-adjust-the-number-of-rcus-for-serverless-apsaradb-rds-instances.md)[RCU](products/rds/documents/apsaradb-rds-for-postgresql/configure-scheduled-tasks-to-adjust-the-number-of-rcus-for-serverless-apsaradb-rds-instances.md)

如果您对特定时段的稳定性有严格要求，您可以通过定时任务提前配置Serverless实例的RCU，以确保该时段内实例的稳定性。

- 

[变更实例弹性策略](products/rds/documents/apsaradb-rds-for-postgresql/change-the-scaling-policy-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md)

对于Serverless实例的弹性策略，您可以选择默认的非强制执行策略以避免潜在的服务中断，或在性能需求高于持续可用性时选择强制执行策略。

- 

[设置实例自动启停](products/rds/documents/apsaradb-rds-for-postgresql/configure-the-automatic-start-and-stop-feature-for-a-serverless-apsaradb-rds-for-postgresql-instance.md)

开启自动启停后，如果10分钟之内实例中无连接，实例将自动进入暂停状态，该状态下RCU为0，不收取计算费用。实例暂停状态下，有任何连接接入，实例自动恢复运行，并开始收取计算费用。

## 免费试用

如果您符合免费试用的条件，可以[免费试用](https://free.aliyun.com/?product=1384)RDS PostgreSQL Serverless实例。

重要

RDS PostgreSQL Serverless实例的免费试用时间不能延长，试用到期后，会继续运行并产生费用。如果您不再需要继续使用实例，请及时手动关闭并释放实例。实例释放后无法找回，请提前做好数据备份。您可以在[费用与成本](https://billing-cost.console.aliyun.com/home)页面，单击左侧导航栏的我的试用，在我的试用页面查看试用产品的信息，比如试用状态、试用进度等。更多关于免费试用的问题，请参见[免费试用常见问题](https://help.aliyun.com/zh/document_detail/612761.html)。

## 常见问题

Q：为何会收到关于Serverless实例CPU、内存等相关的云监控报警？

A：此情况通常是由于预先配置的全局报警规则所致。如果已存在针对所有RDS PostgreSQL实例（或特定资源组）的CPU、内存等指标的报警规则，那么新创建的 Serverless 实例会自动继承这些规则。尽管 Serverless 实例能够自动伸缩，但当其资源使用率瞬时达到报警阈值时，系统仍会触发并发送报警通知。

要管理这些报警，请登录[云监控控制台](https://cloudmonitornext.console.aliyun.com/)，在报警服务>报警规则页，通过高级筛选功能，查看目标Serverless实例当前启用的报警规则，并对其进行[管理](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/modify-an-alert-rule)。

Q：为什么实例在遭遇高负载时未能及时扩容（提升RCU），导致服务无响应？

A：实例在高负载下未能及时扩容（提升RCU）通常由以下两种原因导致：

- 

已达到 RCU 上限：实例的计算资源已扩容至设定的最大RCU值，无法继续提升。此时需评估业务峰值需求，并适当调高RCU的上限。

- 

扩容延迟无法匹配瞬时流量：Serverless 的弹性扩容机制需要时间响应。扩容通常在CPU或内存使用率超过80%时触发，整个过程约需5秒。如果业务流量在极短时间内（例如，小于5秒）急剧飙升，可能导致实例在触发并完成扩容前就因资源耗尽而无响应。对于这种需要应对瞬时超高并发的业务场景，建议使用预置固定资源的常规实例以保障服务的稳定性。

Q：为什么在业务压力降低后，实例没有自动缩容（降低 RCU）？

A：Serverless 实例的缩容（降低 RCU）操作需要同时满足CPU使用率低于50%和内存使用率低于 50%两个条件。

一个常见原因是数据库的页面缓存（Page Cache）占用了较高内存。即使业务压力下降，PostgreSQL 为优化后续查询性能，可能仍会保留数据在内存中，导致内存使用率无法降至50%以下，从而不满足缩容条件。若需立即触发缩容，可通过重启实例来强制释放页面缓存，降低内存使用率。

Q: 实例已暂停且没有连接的情况下，怎么启动实例？

A:在控制台关闭该实例的自动启停功能，实例即可自动启动。

[上一篇：创建PostgreSQL只读实例](products/rds/documents/apsaradb-rds-for-postgresql/create-a-read-only-apsaradb-rds-for-postgresql-instance.md)[下一篇：免费体验RDS PostgreSQL Serverless极致弹性](products/rds/documents/apsaradb-rds-for-postgresql/free-experience-rds-postgresql-serverless-extreme-flexibility.md)

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
