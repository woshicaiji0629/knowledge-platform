# 主实例规格与核心性能参数详解-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/product-overview/primary-apsaradb-rds-instance-types

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/product-overview.md)

- [快速入门](products/rds/documents/getting-started.md)

- [操作指南](products/rds/documents/user-guide.md)

- [实践教程](products/rds/documents/use-cases.md)

- [安全合规](products/rds/documents/security-compliance.md)

- [开发参考](products/rds/documents/developer-reference.md)

- [服务支持](products/rds/documents/support.md)

[首页](https://help.aliyun.com/zh)

# 主实例规格列表

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

RDS提供多种主实例规格以满足不同业务场景下对性能、稳定性及成本的要求，选择合适的实例规格是优化数据库性能和成本的关键步骤。本文旨在帮助您了解RDS主实例的规格信息、各规格的具体配置和核心参数说明。

## 各引擎主实例规格表

您可以通过下表查询各引擎主实例规格及对应的规格族、CPU、内存、实例规格最大IOPS和最大IO带宽等参数。

- 

- 

| 实例引擎 | 支持产品类型 | 支持存储类型 | 主实例规格表 |
| --- | --- | --- | --- |
| MySQL | 标准版、倚天版 | 云盘、高性能本地盘 | [RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md) [标准版（原](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md) [X86）主实例规格列表](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md) [RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types-5.md) [倚天版（原](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types-5.md) [ARM）主实例规格列表](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types-5.md) |
| PostgreSQL | 标准版、倚天版 | 云盘 | [RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/primary-apsaradb-rds-for-postgresql-instance-types.md) [标准版与倚天版主实例规格列表](products/rds/documents/apsaradb-rds-for-postgresql/primary-apsaradb-rds-for-postgresql-instance-types.md) |
| SQL Server | 不涉及 | 云盘 | [RDS SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/primary-apsaradb-rds-for-sql-server-instance-types.md) [主实例规格列表](products/rds/documents/apsaradb-rds-for-sql-server/primary-apsaradb-rds-for-sql-server-instance-types.md) |
| MariaDB | 标准版 | 云盘 | [RDS MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/instance-types.md) [主实例规格列表](products/rds/documents/apsaradb-rds-for-mariadb/instance-types.md) |


## 核心概念说明

各引擎主实例规格表中主要涉及以下三个核心概念：实例规格族、IOPS和IO带宽。

### 实例规格族

实例规格族决定了资源的分配方式，会直接影响实例性能。

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

| 规格族 | 存储类型 | 独享/共享资源 | 说明 |
| --- | --- | --- | --- |
| 共享型 | 云盘 | 独享：内存、存储 共享：CPU、I/O 资源 | 仅 SQL Server 引擎支持 当物理机负载过高时，可能存在性能波动。 |
| 通用型 | 云盘 | 独享：内存、存储 共享：CPU、I/O 资源 | 当物理机负载过高时，可能存在性能波动。 |
| 高性能本地盘 | 独享：内存 共享：CPU、存储、I/O 资源 |  |  |
| 独享型 | 云盘 | 完全独享 CPU、内存、存储介质以及 I/O 资源。 | 性能稳定，无资源争抢。 |
| 高性能本地盘 | 独享：CPU、内存、存储 共享：I/O 资源 |  |  |
| 独占物理机 | 高性能本地盘 | 完全独享 CPU、内存、存储介质以及 I/O 资源。 | 提供最高的性能稳定性和隔离性。 |


### IOPS

IOPS反映了存储系统处理读写请求的能力，是衡量随机I/O性能的关键指标。影响实例IOPS的主要因素为：实例规格、存储类型和存储容量，您可以在[各引擎主实例规格表](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)中查找对应实例规格的最大IOPS，但实例的实际IOPS上限需通过以下内容计算：

- 

高性能本地盘实例：实际IOPS上限仅受实例规格影响，主实例规格表中的最大IOPS即为实际IOPS上限。

- 

云盘实例：实际IOPS上限受实例规格、存储容量和存储类型三者共同影响，计算公式如下：

| 存储类型 | 实际最大 IOPS 计算公式（存储空间单位：GB） |  |
| --- | --- | --- |
| 高性能云盘 | 开启 [IO](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) [性能突发](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) | min{实例规格最大 IOPS,1000000} |
| 未开启 [IO](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) [性能突发](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) | min{实例规格最大 IOPS, 1800+50*存储空间, 50000} |  |
| ESSD 云盘 | PL3 | min{实例规格最大 IOPS, 1800+50*存储空间, 1000000} |
| PL2 | min{实例规格最大 IOPS, 1800+50*存储空间, 100000} |  |
| PL1 | min{实例规格最大 IOPS, 1800+50*存储空间, 50000} |  |
| SSD 云盘 | min{实例规格最大 IOPS, 1800+30*存储空间, 25000} |  |


示例：以ESSD PL1云盘，实例规格mysql.x2.large.2c，存储空间20 GB为例，计算该实例的实际IOPS：

| 限制因素 | 说明 |
| --- | --- |
| 实例规格 | 查询主实例规格表， mysql.x2.large.2c 实例规格对应的 IOPS 上限为 20000 。 |
| 存储空间 | 20 GB 存储空间对应的 IOPS 上限为 1800+50*20=2800 。 |
| 存储类型 | ESSD PL1 云盘对应的 IOPS 上限为 50000 。 |


该实例实际的IOPS上限取上述三者间最小值：2800（主要受存储空间限制）。

说明

- 

数据库实际读写次数与磁盘I/O并非等价关系。以MySQL为例，单次MySQL读写默认为16KB，而云盘I/O块大小为4KB，因此MySQL执行一次读写会消耗4次云盘I/O。

- 

在相同磁盘I/O的情况下，因不同引擎的默认页（Page）大小不同，会导致数据库读实际写次数不同（即在相同IOPS指标下，不同数据库的读写处理能力不同）。例如：云盘I/O块大小为4KB，同样是1000次磁盘I/O，对应MySQL引擎（默认页大小为16KB）实际读写次数为250次，对应SQL Server引擎（默认页大小为8KB）实际读写次数为500次。

### IO带宽（吞吐量）

IO带宽反映了存储系统连续读写数据的能力，是衡量顺序I/O性能的关键指标。影响实例IO带宽的主要因素为：实例规格、存储类型和存储容量，您可以在[主实例规格表](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)中查找对应实例规格的最大IO带宽，但实例的实际IO带宽上限需通过以下内容计算：

| 存储类型 | 云盘实例实际 IO 带宽性能公式（IO 带宽单位：MB/s、存储空间单位：GB） |  |
| --- | --- | --- |
| 高性能云盘 | 开启 [IO](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) [性能突发](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) | min{实例规格最大 IO 带宽, 4000} |
| 未开启 [IO](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) [性能突发](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) | min{实例规格最大 IO 带宽, 120+0.5x 存储空间, 350} |  |
| ESSD 云盘 | PL3 | min{实例规格最大 IO 带宽, 120+0.5*存储空间, 4000} |
| PL2 | min{实例规格最大 IO 带宽, 120+0.5*存储空间, 750} |  |
| PL1 | min{实例规格最大 IO 带宽, 120+0.5*存储空间, 350} |  |
| SSD 云盘 | min{实例规格最大 IO 带宽, 120+0.5*存储空间, 300} |  |


示例：以ESSD PL3云盘，实例规格mysql.x2.large.2c，存储空间5000 GB为例，计算该实例的实际IO带宽上限：

| 限制因素 | 说明 |
| --- | --- |
| 实例规格 | 查询主实例规格表， mysql.x2.large.2c 实例规格对应的 IO 带宽上限为 192 。 |
| 存储空间 | 5000 GB 存储空间对应的 IO 带宽上限为 120+0.5*5000=2620 。 |
| 存储类型 | ESSD PL3 云盘对应的 IO 带宽上限为 4000 。 |


该实例实际的IO带宽上限取上述三者间最小值：192（主要受实例规格限制）。

### IOPS与IO带宽间的制约关系

云盘IOPS与IO带宽并非独立的性能指标，除共同受实例规格、存储类型和存储空间影响外，两者之间也会互相制约：

- 

换算公式：IO带宽(MB/s) = IOPS × I/O块大小(KB) / 1024（此处I/O块大小指磁盘单次I/O操作大小（云盘默认为为4KB），而非数据库的页（Page） 大小。）

- 

制约关系：大部分情况下，IOPS和IO带宽不会同时触达上限。

- 

当IOPS达到上限时，如果I/O块较小（如4KB），实例IO带宽可能未达上限，此时IOPS会成为业务性能瓶颈。

- 

当IO带宽达到上限时，如果I/O块较大（如256KB），实例IOPS可能未达上限，此时IO带宽会成为业务性能瓶颈。

## 常见问题

- 

Q1：为什么入门级规格的性能看起来比企业级规格的性能要好？

A：因为入门级规格一般是共享/通用型规格族，企业级规格一般是独享型规格族。实际使用中企业级规格由于独享CPU和内存，会更加稳定。详细区别，请参见[实例规格族](products/rds/documents/product-overview/instance-families.md)。

- 

Q2：想查询当前售卖资源怎么办？

A：可以在售卖页查询或使用[DescribeAvailableResource](products/rds/documents/api-query-available-resources.md)接口查询。

- 

Q3：为什么不展示QPS和TPS？

A：QPS和TPS需要RDS上面部署相关对象测试。同一个规格的实例在不同业务系统中，根据实现方法不同，QPS和TPS也会有较大的差距。QPS和TPS的测试方法，请参见[性能测试指导](products/rds/documents/support/test-guidelines.md)。

## 相关内容

- 

RDS还支持通过添加只读实例（[MySQL](products/rds/documents/overview-of-read-only-apsaradb-rds-for-mysql-instances.md)[只读实例](products/rds/documents/overview-of-read-only-apsaradb-rds-for-mysql-instances.md)、[SQL Server](products/rds/documents/overview-of-read-only-apsaradb-rds-for-sql-server-instances.md)[只读实例](products/rds/documents/overview-of-read-only-apsaradb-rds-for-sql-server-instances.md)、[PostgreSQL](products/rds/documents/overview-of-read-only-apsaradb-rds-for-postgresql-instances.md)[只读实例](products/rds/documents/overview-of-read-only-apsaradb-rds-for-postgresql-instances.md)）来扩展读性能。关于只读实例规格，请参见[只读实例规格列表](products/rds/documents/product-overview/read-only-apsaradb-rds-instance-types.md)。

- 

选定主实例规格后您就可以创建并使用实例。具体操作，请参见[快速创建](products/rds/documents/apsaradb-rds-for-mysql/step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[实例](products/rds/documents/apsaradb-rds-for-mysql/step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)、[快速创建](products/rds/documents/apsaradb-rds-for-sql-server/create-an-apsaradb-rds-for-sql-server-instance.md)[RDS SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/create-an-apsaradb-rds-for-sql-server-instance.md)[实例](products/rds/documents/apsaradb-rds-for-sql-server/create-an-apsaradb-rds-for-sql-server-instance.md)、[快速创建](products/rds/documents/apsaradb-rds-for-postgresql/create-an-apsaradb-rds-for-postgresql-instance.md)[RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/create-an-apsaradb-rds-for-postgresql-instance.md)[实例](products/rds/documents/apsaradb-rds-for-postgresql/create-an-apsaradb-rds-for-postgresql-instance.md)。

[上一篇：实例规格族](products/rds/documents/product-overview/instance-families.md)[下一篇：只读实例规格列表](products/rds/documents/product-overview/read-only-apsaradb-rds-instance-types.md)

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
