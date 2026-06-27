# 多维度对比自建数据库的优势-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/product-overview/competitive-advantages-of-apsaradb-rds-instances-over-self-managed-databases

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

# RDS与自建数据库对比优势

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库RDS提供高可用、高可靠、高安全、可扩展的托管数据库服务，在性能等同于商业数据库的同时，其价格相比ECS自建数据库和自购服务器搭建数据库更加低廉，能够节约大量部署及维护成本。

## RDS与自建数据库对比优势

## RDS MySQL与自建数据库对比优势

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

- 

- 

- 

- 

- 

- 

| 对比项 | RDS MySQL | ECS 自建 | 自购服务器搭建数据库 |
| --- | --- | --- | --- |
| 性价比 | 弹性资源。 [AliSQL](products/rds/documents/apsaradb-rds-for-mysql/overview-of-alisql-features.md) 深度定制的独立 MySQL 分支，提供了类似于 MySQL 企业版的诸多功能，提升用户使用感受。 最多 2 倍存储空间大小的 [免费备份空间](products/rds/documents/apsaradb-rds-for-mysql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md) 。 公网流量免费。 免费使用自带的域名。 更新速度快，紧跟 MySQL 最新版本。 | 弹性资源。 开源版无性能优化。 备份空间独立收费。 公网流量收费。 | 一次投入的沉没成本大。 开源版无性能优化。 需要独立准备备份资源，成本极高。 公网流量收费，域名费用高。 |
| 可用性 | 基础系列约 15 分钟即可完成故障转移。 高可用系列和集群系列提供自研高可用系统，实现 30 秒内故障恢复。 [只读实例](products/rds/documents/overview-of-read-only-apsaradb-rds-for-mysql-instances.md) 自动实现负载均衡。 [读写分离](products/rds/documents/apsaradb-rds-for-mysql/enable-the-proxy-terminal-feature-for-an-apsaradb-rds-for-mysql-instance.md) 使用方便。 未来会推出分析节点，满足分析型场景需求。 | 基础系列约 30 分钟完成故障转移。 需要单独购买高可用系统。 需要单独实现或者购买负载均衡服务。 分析型场景需要与分析型数据库结合，搭建难度大、成本高。 | 单机实例，少则两小时，多则等待配货数周。 需要单独购买高可用系统。 需要单独实现或者购买负载均衡设备。 分析型场景需要与分析型数据库结合，搭建难度大、成本高。 |
| 可靠性 | 数据可靠性高，自动主备复制、数据备份、日志备份等。 MySQL 集群系列实现多可用区容灾，通过组复制技术提供数据强一致性，并且提供可靠性更强的备节点。备节点的故障发现时长为秒级，在 99%的场景下，备节点从故障发生到节点恢复不超过 10 分钟。 | 在好的架构下才能实现高可靠性。 实现 RPO=0 的成本极高，需要单独购买研发服务。 | 数据可靠性一般，取决于单块磁盘的损害概率。 实现 RPO=0 的成本极高，需要单独购买研发服务。 |
| 易用性 | [自动化备份恢复](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md) 系统，支持按时间点恢复、单库备份恢复等，流式备份对实例性能影响小。 [自动化监控告警](products/rds/documents/apsaradb-rds-for-mysql/configure-an-alert-rule-for-an-apsaradb-rds-for-mysql-instance.md) 系统，支持秒级监控，覆盖实例和数据库所有性能指标，支持短信、邮箱、旺旺、钉钉等通道，且根据消费提供大额度的免费短信数量。 支持 [异地容灾](products/rds/documents/apsaradb-rds-for-mysql/create-a-disaster-recovery-apsaradb-rds-for-mysql-instance.md) 。 支持 [一键版本升级](products/rds/documents/apsaradb-rds-for-mysql/update-the-minor-engine-version-of-an-apsaradb-rds-for-mysql-instance.md) 。 | 无自动备份系统，流式备份能力需要单独实现，实现按时间点恢复功能成本高。 需要单独购买监控系统，在云监控中配置告警系统。 技术实现难度极大。 版本升级成本高。 | 无自动备份系统，流式备份能力需要单独实现，实现按时间点恢复功能成本高。 需要单独购买或配置监控系统，通道较少，成本较高。 异地数据中心成本极高，技术实现难度也大，很难实现异地容灾。 版本升级成本高。 |
| 性能 | MySQL 的高性能本地盘实例性能极佳。 MySQL 的 ESSD 性能较 SSD 提升显著。 增加只读实例之后性能强劲且负载均衡。 [数据库自治服务](https://help.aliyun.com/zh/document_detail/144875.html) [DAS](https://help.aliyun.com/zh/document_detail/144875.html) 提供高级优化能力。 [SQL](products/rds/documents/use-sql-explorer-features-on-apsaradb-rds-for-mysql-instances.md) [洞察](products/rds/documents/use-sql-explorer-features-on-apsaradb-rds-for-mysql-instances.md) 满足大部分监控及性能优化数据库场景。 | ECS 本地盘意味着降低数据可靠性，采用云盘需要规划架构，成本支出较大。 实现集群系列的难度较高，咨询成本较高，维护成本极高。 依赖资深 DBA，支出大，受制于人。 | 比云计算硬件更新速度慢，性能一般都会低于云数据库。 难以实现计算和存储分离，若使用高端存储实现计算和存储分离，动辄需要数千万支出。 实现集群系列的难度较高，咨询成本较高，维护成本极高。 依赖资深 DBA，支出大，受制于人。 |
| 安全 | 事前防护： [白名单](products/rds/documents/use-a-database-client-or-the-cli-to-connect-to-an-apsaradb-rds-for-mysql-instance-2.md) 、 [安全组](products/rds/documents/use-a-database-client-or-the-cli-to-connect-to-an-apsaradb-rds-for-mysql-instance-2.md) 、 [专有网络隔离](products/vpc/documents/what-is-vpc.md) 。 事中保护： [连接链路加密](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) 、 [数据落盘加密](products/rds/documents/apsaradb-rds-for-mysql/configure-tde-for-an-apsaradb-rds-for-mysql-instance.md) （BYOK 覆盖多种存储介质）。 事后审计： [SQL](products/rds/documents/use-sql-explorer-features-on-apsaradb-rds-for-mysql-instances.md) [洞察](products/rds/documents/use-sql-explorer-features-on-apsaradb-rds-for-mysql-instances.md) 、 [历史事件](products/rds/documents/view-the-event-history-of-an-apsaradb-rds-instance-3.md) 。 | 事前防护：白名单、安全组、专有网络隔离。 事中保护：需要单独实现连接链路加密和数据落盘加密，BYOK 密钥轮转难度大，咨询成本较高。 事后审计：审计困难，需要单独保存 SQL 日志。 | 事前防护：白名单和专有网络隔离的咨询成本较高。 事中保护：需要单独实现连接链路加密和数据落盘加密，BYOK 密钥轮转难度大，咨询成本较高。 事后审计：审计困难，需要单独保存 SQL 日志。 |


## RDS PostgreSQL与自建数据库对比优势

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

| 对比项 | RDS PostgreSQL | ECS 自建 | 自购服务器搭建数据库 |
| --- | --- | --- | --- |
| 性价比 | 弹性资源。 [AliPG](products/rds/documents/apsaradb-rds-for-postgresql/alipg-benefits.md) 兼容 PostgreSQL 开源数据库，提供更多特有的功能模块，提升用户使用感受。 最多 2 倍存储空间大小的 [免费备份空间](products/rds/documents/apsaradb-rds-for-postgresql/view-the-free-quota-for-backup-storage-of-an-apsaradb-rds-for-postgresql-instance.md) 。 公网流量免费。 免费使用自带的域名。 更新速度快，紧跟 PostgreSQL 最新版本。 | 弹性资源。 开源版无性能优化。 备份空间独立收费。 公网流量收费。 | 一次投入的沉没成本大。 开源版无性能优化。 需要独立准备备份资源，成本极高。 公网流量收费，域名费用高。 |
| 可用性 | 基础系列约 15 分钟即可完成故障转移。 高可用系列 和集群系列 提供自研高可用系统，实现 30 秒内故障恢复。 [只读实例](products/rds/documents/overview-of-read-only-apsaradb-rds-for-postgresql-instances.md) 自动实现负载均衡。 | 基础系列约 30 分钟完成故障转移。 需要单独购买高可用系统。 需要单独实现或者购买负载均衡服务。 | 单机实例，少则两小时，多则等待配货数周。 需要单独购买高可用系统。 需要单独实现或者购买负载均衡设备。 |
| 可靠性 | 数据可靠性高，自动主备复制、数据备份、日志备份等。 支持设置保护级别，最高 RPO=0。 MySQL 集群系列实现多可用区容灾，通过组复制技术提供数据强一致性，并且提供可靠性更强的备节点。备节点的故障发现时长为秒级，在 99%的场景下，备节点从故障发生到节点恢复不超过 10 分钟。 | 在好的架构下才能实现高可靠性。 实现 RPO=0 的成本极高，需要单独购买研发服务。 | 数据可靠性一般，取决于单块磁盘的损坏概率。 实现 RPO=0 的成本极高，需要单独购买研发服务。 |
| 易用性 | [自动化备份恢复](products/rds/documents/apsaradb-rds-for-postgresql/back-up-an-apsaradb-rds-for-postgresql-instance.md) 系统，支持按时间点恢复、单库备份恢复等，流式备份对实例性能影响小。 [自动化监控告警](products/rds/documents/apsaradb-rds-for-postgresql/manage-the-alert-rules-of-an-apsaradb-rds-for-postgresql-instance.md) 系统，覆盖实例和数据库所有性能指标，支持短信、邮箱、旺旺、钉钉等通道，且根据消费有大额度的免费短信数量。 | 无自动备份系统，流式备份能力需要单独实现，实现按时间点恢复功能成本高。 需要单独购买监控系统，在云监控中配置告警系统。 | 无自动备份系统，流式备份能力需要单独实现，实现按时间点恢复功能成本高。 需要单独购买或配置监控系统，通道较少，成本较高。 |
| 性能 | PostgreSQL 的 ESSD 性能较 SSD 提升显著。 增加只读实例之后性能强劲且负载均衡。 [数据库自治服务](https://help.aliyun.com/zh/document_detail/159166.html) [DAS](https://help.aliyun.com/zh/document_detail/159166.html) 提供高级优化能力。 [SQL](products/rds/documents/use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) [审计（数据库审计）](products/rds/documents/use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) 满足大部分监控及性能优化数据库场景。 | ECS 本地盘意味着降低数据可靠性，采用云盘需要规划架构，成本支出较大。 实现集群系列的难度较高，咨询成本较高，维护成本极高。 依赖资深 DBA，支出大，受制于人。 | 与云计算相比，硬件更新速度慢，性能一般都会低于云数据库。 难以实现计算和存储分离，若使用高端存储实现计算和存储分离，动辄需要数千万元的支出。 实现集群系列的难度较高，咨询成本较高，维护成本极高。 依赖资深 DBA，支出大，受制于人。 |
| 安全 | 事前防护： [白名单](products/rds/documents/apsaradb-rds-for-postgresql/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance-1.md) 、 [安全组](products/rds/documents/apsaradb-rds-for-postgresql/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance.md) 、 [专有网络隔离](products/vpc/documents/what-is-vpc.md) 。 事中保护： [连接链路加密](products/rds/documents/apsaradb-rds-for-postgresql/configure-disk-encryption-for-an-apsaradb-rds-for-postgresql-instance.md) 、 [云盘加密](products/rds/documents/apsaradb-rds-for-postgresql/configure-disk-encryption-for-an-apsaradb-rds-for-postgresql-instance.md) 。 事后审计： [SQL](products/rds/documents/use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) [审计（数据库审计）](products/rds/documents/use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) 、 [历史事件](products/rds/documents/view-the-event-history-of-an-apsaradb-rds-instance.md) 。 | 事前防护：白名单、安全组、专有网络隔离。 事中保护：需要单独实现连接链路加密。 事后审计：审计困难，需要单独保存 SQL 日志。 | 事前防护：白名单和专有网络隔离的咨询成本较高。 事中保护：需要单独实现连接链路加密。 事后审计：审计困难，需要单独保存 SQL 日志。 |


## RDS SQL Server与自建数据库对比优势

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

| 对比项 | RDS SQL Server | ECS 自建 | 自购服务器搭建数据库 |
| --- | --- | --- | --- |
| 性价比 | 弹性资源。 Web 版性价比极高。 备份有 [一半实例空间免费](products/rds/documents/apsaradb-rds-for-sql-server/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-sql-server-instance.md) 。 公网流量免费。 | 弹性资源。 不可使用 Web 版。 备份空间独立收费。 公网流量收费。 | 一次投入的沉没成本大。 不可使用 Web 版。 需要独立准备备份资源，成本极高。 公网流量收费，域名费用高。 |
| 可用性 | 基础系列约 15 分钟即可完成故障转移。 高可用系列和集群系列提供自研高可用系统，实现 30 秒内故障恢复。 集群系列的 [只读实例](products/rds/documents/overview-of-read-only-apsaradb-rds-for-sql-server-instances.md) 自动实现负载均衡。 集群系列的 [读写分离](products/rds/documents/overview-of-read-or-write-splitting.md) 使用方便。 | 基础系列约 30 分钟完成故障转移。 需要单独购买高可用系统。 需要单独实现或者购买负载均衡服务。 | 单机实例，少则两小时，多则等待配货数周。 需要单独购买高可用系统。 需要单独实现或者购买负载均衡设备。 |
| 可靠性 | 数据可靠性高，自动主备复制、数据备份、日志备份等。 集群系列可实现 RPO（Recovery Point Object）=0。 | 在好的架构下才能实现高可靠性。 实现 RPO=0 的成本极高，需要单独购买研发服务。 | 数据可靠性一般，取决于单块磁盘的损害概率。 实现 RPO=0 的成本极高，需要单独购买研发服务。 |
| 易用性 | [自动化备份恢复](products/rds/documents/apsaradb-rds-for-sql-server/back-up-an-apsaradb-rds-for-sql-server-instance.md) 系统，支持按时间点恢复、单库备份恢复等，流式备份对实例性能影响小。 [自动化监控告警](products/rds/documents/apsaradb-rds-for-sql-server/configure-an-alert-rule-for-an-apsaradb-rds-for-sql-server-instance.md) 系统，支持秒级监控，覆盖实例和数据库所有性能指标，支持短信、邮箱、旺旺、钉钉等通道，且根据消费有大额度的免费短信数量。 即将支持异地容灾。 | 无自动备份系统，流式备份能力需要单独实现，实现按时间点恢复功能成本高。 需要单独购买监控系统，在云监控中配置告警系统。 技术实现难度极大。 | 无自动备份系统，流式备份能力需要单独实现，实现按时间点恢复功能成本高。 需要单独购买或配置监控系统，通道较少，成本较高。 异地数据中心成本极高，技术实现难度也大，很难实现异地容灾。 |
| 性能 | SQL Server 2008 R2 的高性能本地盘实例性能极佳，SQL Server 201x 版本新计算存储分离架构可享受硬件红利 。 SQL Server 的 ESSD 性能较 SSD 提升显著。 增加只读实例之后性能强劲且负载均衡。 [数据库自治服务](https://help.aliyun.com/zh/document_detail/98989.html) [DAS](https://help.aliyun.com/zh/document_detail/98989.html) 提供高级优化能力。 | ECS 本地盘意味着降低数据可靠性，采用云盘需要规划架构，成本支出较大。 基于 ESSD 的 RDS SQL Server 进行了参数调优及相关适配，性能高于基于 ESSD 的 ECS 自建 SQL Server。 实现集群系列的难度较高，咨询成本较高，维护成本极高。 依赖资深 DBA，支出大，受制于人。 | 比云计算硬件更新速度慢，性能一般都会低于云数据库。 难以实现计算和存储分离，若使用高端存储实现计算和存储分离，动辄需要数千万支出。 实现集群系列的难度较高，咨询成本较高，维护成本极高。 依赖资深 DBA，支出大，受制于人。 |
| 安全 | 事前防护： [白名单](products/rds/documents/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-sql-server-instance-1.md) 、 [专有网络隔离](products/vpc/documents/what-is-vpc.md) 。 事中保护： [连接链路加密](products/rds/documents/apsaradb-rds-for-sql-server/configure-ssl-encryption-for-an-apsaradb-rds-for-sql-server-instance.md) 、 [数据落盘加密](products/rds/documents/apsaradb-rds-for-sql-server/configure-tde-for-an-apsaradb-rds-for-sql-server-instance.md) 。 事后审计： [SQL](https://help.aliyun.com/zh/document_detail/95712.html#concept-njf-cr4-ydb) [审计（数据库审计）](https://help.aliyun.com/zh/document_detail/95712.html#concept-njf-cr4-ydb) 、 [历史事件](products/rds/documents/view-the-event-history-of-an-apsaradb-rds-instance-3.md) 。 微软安全更新，阿里技术兜底。 | 事前防护：白名单、安全组、专有网络隔离。 事中保护：需要单独实现连接链路加密和数据落盘加密，咨询成本较高。 事后审计：审计困难，需要单独保存 SQL 日志。 | 事前防护：白名单和专有网络隔离的咨询成本较高。 事中保护：需要单独实现连接链路加密和数据落盘加密，咨询成本较高。 事后审计：审计困难，需要单独保存 SQL 日志。 |
| 法律 | 附带 License，无法律风险。 | 只有单独购买 License。 | 只有单独购买 License，否则法律风险极大。 |


## 开始使用RDS

- 

[快速入门](products/rds/documents/getting-started.md)

- 

[学习路径图](https://help.aliyun.com/learn/learningpath/rds.html)

- 

自建数据库迁移至云数据库RDS：

- 

MySQL：[从自建](products/rds/documents/apsaradb-rds-for-mysql/data-migration-from-a-user-created-database-to-an-apsaradb-rds-mysql-instance.md)[MySQL](products/rds/documents/apsaradb-rds-for-mysql/data-migration-from-a-user-created-database-to-an-apsaradb-rds-mysql-instance.md)[迁移至](products/rds/documents/apsaradb-rds-for-mysql/data-migration-from-a-user-created-database-to-an-apsaradb-rds-mysql-instance.md)[RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/data-migration-from-a-user-created-database-to-an-apsaradb-rds-mysql-instance.md)

- 

SQL Server：[从自建](products/rds/documents/overview-of-data-migration-methods.md)[SQL Server](products/rds/documents/overview-of-data-migration-methods.md)[迁移至](products/rds/documents/overview-of-data-migration-methods.md)[RDS SQL Server](products/rds/documents/overview-of-data-migration-methods.md)

- 

PostgreSQL：[从自建](products/rds/documents/apsaradb-rds-for-postgresql/migrate-user-created-databases-to-apsaradb.md)[PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/migrate-user-created-databases-to-apsaradb.md)[迁移至](products/rds/documents/apsaradb-rds-for-postgresql/migrate-user-created-databases-to-apsaradb.md)[RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/migrate-user-created-databases-to-apsaradb.md)

- 

MariaDB：[从自建](products/rds/documents/apsaradb-rds-for-mariadb/data-migration.md)[MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/data-migration.md)[迁移至](products/rds/documents/apsaradb-rds-for-mariadb/data-migration.md)[RDS MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/data-migration.md)

[上一篇：高安全性](products/rds/documents/product-overview/high-security.md)[下一篇：产品类型](products/rds/documents/product-overview/product-types.md)

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
