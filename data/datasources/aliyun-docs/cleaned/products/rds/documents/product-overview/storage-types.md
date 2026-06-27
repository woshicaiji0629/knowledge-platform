# 云数据库RDS存储类型的区别及选购建议-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/product-overview/storage-types

# 存储类型
云数据库RDS提供了以下数据存储类型：ESSD云盘、高性能本地盘、SSD云盘、高性能云盘，本文介绍这几种存储类型的基本信息、区别及选购建议。
## 存储类型介绍
| 存储类型 | 说明 | 支持引擎 |
| --- | --- | --- |
| ESSD 云盘 | 增强型 SSD 云盘（Enhanced SSD 云盘，下文简称 ESSD 云盘），是阿里云全新推出的超高性能云盘产品。ESSD 云盘基于新一代分布式块存储架构，结合 25GE 网络和 RDMA 技术，为您提供单盘高达 100 万的随机读写能力和比 SSD 云盘更低的单路时延能力。ESSD 云盘分为如下几类： ESSD PL0 云盘：PL0 性能级别的 ESSD 云盘。 说明 目前仅 RDS MySQL、RDS PostgreSQL 基础系列倚天版规格支持 ESSD PL0 云盘，规格详情请参见 [RDS MySQL](../apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types-5.md) [倚天版（原](../apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types-5.md) [ARM）主实例规格列表](../apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types-5.md) 、 [RDS PostgreSQL](../apsaradb-rds-for-postgresql/primary-apsaradb-rds-for-postgresql-instance-types.md) [主实例规格列表](../apsaradb-rds-for-postgresql/primary-apsaradb-rds-for-postgresql-instance-types.md) 。 ESSD PL1 云盘： 相比 PL0，PL1 性能级别的 ESSD 云盘大约可提升 5 倍 IOPS 和 2 倍的吞吐量。 ESSD PL2 云盘：相比 PL1，PL2 性能级别的 ESSD 云盘大约可提升 2 倍 IOPS 和吞吐量。 ESSD PL3 云盘：相比 PL1，PL3 性能级别的 ESSD 云盘最高可提升 20 倍 IOPS、11 倍吞吐量，适合对极限并发 IO 性能要求极高、读写时延极稳定的业务场景。 关于 ESSD 云盘的性能详情，请参见 [ESSD](../../../ecs/documents/user-guide/essds.md) [云盘](../../../ecs/documents/user-guide/essds.md) 。 | MySQL、PostgreSQL、SQL Server、MariaDB |
| 高性能本地盘 | 高性能本地盘是 RDS 自研智能本地磁盘，与 MySQL 位于同一物理机，数据存储和读写操作均在本地完成，具有高读写 IO、低时延的特性。 高性能本地盘 IOPS 最高可达 15 万，I/O 延时低至微秒级，存储空间最高可达 16 TB，备份恢复速度较自建提升 10 倍。 适用 IO 密集型应用或高并发读写场景，如电商秒杀活动、高频交易系统。 | MySQL |
| 高性能云盘 | 高性能云盘基本兼容 ESSD 云盘的所有特性，在 ESSD 云盘的基础上提供了 IO 性能突发、Buffer Pool Extension（BPE）和数据归档等功能： IO 性能突发（MySQL、PostgreSQL 、SQL Server 支持 ）：使云盘的 IOPS 不受限于最大 IOPS，在业务波峰时提供更高的 IO 能力，满足突发业务需求。 Buffer Pool Extension（BPE）（MySQL、PostgreSQL 支持）：帮助扩展缓存池的大小，提高磁盘 IO 效率和系统的响应速度，实现缓存加速，提升 RDS 实例的整体读写性能。 数据归档（MySQL、PostgreSQL 、SQL Server 支持 ）：可以将低频访问的数据转移至 OSS 中，数据存储成本相较于 ESSD PL1 云盘下降 80%。适用于实例中包含不常访问或修改的表。 更多信息，请参见 [RDS MySQL](../apsaradb-rds-for-mysql/premium-essd.md) [高性能云盘](../apsaradb-rds-for-mysql/premium-essd.md) 、 [RDS PostgreSQL](../apsaradb-rds-for-postgresql/introduction-to-universal-cloud-disk-of-apsaradb-rds-for-postgresql.md) [高性能云盘](../apsaradb-rds-for-postgresql/introduction-to-universal-cloud-disk-of-apsaradb-rds-for-postgresql.md) 、 [RDS SQL Server](../apsaradb-rds-for-sql-server/what-is-a-premium-essd.md) [高性能云盘](../apsaradb-rds-for-sql-server/what-is-a-premium-essd.md) 。 | MySQL、PostgreSQL 、SQL Server |
| SSD 云盘 | SSD 云盘，是基于分布式存储架构的弹性块存储设备，实现计算与存储分离。 说明 SSD 云盘分批下线中，建议使用 ESSD 云盘。更多信息，请参见 [【通知】部分](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md) [RDS](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md) [实例不再提供](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md) [SSD](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md) [云盘售卖](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md) 。 | MySQL、PostgreSQL、SQL Server、MariaDB |
各存储类型之间的性能对比（单盘容量、最大IOPS、最大吞吐量等），请参见[块存储性能](../../../ecs/documents/user-guide/block-storage-performance.md)。
说明
这几种存储类型的可靠性、持久性和读写性能均会满足产品SLA承诺。
高性能本地盘：所属的RDS实例都是一主一备（[高可用系列](../apsaradb-rds-for-mysql/rds-high-availability-edition.md)）架构，主节点故障时，主备节点秒级完成切换。
云盘（SSD云盘、ESSD云盘、高性能云盘）：分布式云盘，通过多副本冗余确保数据可靠性。如果所属RDS实例为高可用系列、集群系列，则具备秒级自动切换能力。
## 查看存储类型
您可以在实例的基本信息页面查看实例的存储类型。
## 不同类型存储的区别
说明
当前仅RDS MySQL高可用系列实例支持高性能本地盘。
| 对比项 | ESSD 云盘 | 高性能云盘 | 高性能本地盘 |
| --- | --- | --- | --- |
| I/O 性能 说明 磁盘在处理数据读写请求时的速度和效率，包括 IOPS、吞吐量和访问时延等。 | ★★★★★ 相对 SSD 云盘有大幅提升： IOPS：由磁盘规格及实例规格共同决定。 IO 延迟：100~200 微秒。 | ★★★★★★ 在 ESSD 云盘的基础上，增加了 [IO](../apsaradb-rds-for-mysql/i-o-performance-burst.md) [性能突发功能](../apsaradb-rds-for-mysql/i-o-performance-burst.md) 、 [Buffer Pool Extension（BPE）功能](../apsaradb-rds-for-mysql/buffer-pool-extension-bpe.md) 和 [数据归档功能](../apsaradb-rds-for-mysql/rds-mysql-data-archiving-function.md) 。IO 性能如下： IOPS：由磁盘规格及实例规格共同决定。 IO 延迟：100~200 微秒。 | ★★★★★ IO 延迟低，性能好： IOPS：由实例规格决定 IO 延迟：10~50 微秒。 |
| 规格配置灵活性 | ★★★★★ 可选配置较多，支持扩容或缩容磁盘空间。 说明 仅 MySQL 和 PostgreSQL 部分满足条件的实例支持缩容，具体请参见 [实例变更项概览](../apsaradb-rds-for-mysql/configuration-items-for-an-apsaradb-rds-for-mysql-instance.md) 和 [变更配置](../apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md) 。 | ★★★★★ 可选配置较多，支持扩容或缩容磁盘空间。 说明 仅 MySQL 和 PostgreSQL 部分满足条件的实例支持缩容，具体请参见 [实例变更项概览](../apsaradb-rds-for-mysql/configuration-items-for-an-apsaradb-rds-for-mysql-instance.md) 和 [变更配置](../apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md) 。 | ★★★★ 可选配置较多，磁盘空间可单独调整。仅部分高性能本地盘实例的磁盘空间大小与实例规格绑定，无法单独调整。 |
| 备份方法 | ESSD 云盘快照备份。 | ESSD 云盘快照备份。 | Xtrabackup 物理备份。 |
| 备份、只读实例创建、实例克隆操作速度 | ★★★★★ 耗时为秒级。 | ★★★★★ 耗时为秒级。 | ★★★ 与磁盘大小相关，耗时为小时级。 |
| 扩容时长 | ★★★★★ 在线升级，秒级扩容。 | ★★★★★ 在线升级，秒级扩容。 | ★★★★ 需要拷贝数据，可能需要几个小时。 |
| 扩容影响 | 无影响。 | 无影响。 | 有闪断。 |
| 数据持久性 | ★★★★★ 数据可靠性达到 99.9999999%，支持单节点基础版形态，降低成本。 | ★★★★★ 数据可靠性达到 99.9999999%，支持单节点基础版形态，降低成本。 | ★★★★ 硬件故障有一定概率导致数据损坏，需要有备库保障。高可用系列本地盘实例 SLA 可达 99.995%。 |
## 选购建议
建议优先选择高性能云盘：
如果IO量比较大，建议开启[Buffer Pool Extension（BPE）功能](../apsaradb-rds-for-mysql/buffer-pool-extension-bpe.md)。
如果IO波动较大，建议开启[IO](../apsaradb-rds-for-mysql/i-o-performance-burst.md)[性能突发功能](../apsaradb-rds-for-mysql/i-o-performance-burst.md)。
如果明确需要使用高PL等级云盘，可以选择ESSD云盘。
## 产品支持度
各个实例类型支持的存储类型及功能请参见：
[MySQL](https://help.aliyun.com/zh/document_detail/317704.html)[功能概览](https://help.aliyun.com/zh/document_detail/317704.html)
[PostgreSQL](../rds-postgresql-database-features.md)[功能概览](../rds-postgresql-database-features.md)
[SQL Server](../features-6.md)[功能概览](../features-6.md)
[MariaDB](../apsaradb-rds-for-mariadb/features-1.md)[功能概览](../apsaradb-rds-for-mariadb/features-1.md)
## 常见问题
[存储空间的常见问题](../support/faq-about-storage-capacity.md)
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
