# 阿里云RDS数据库被锁定，报错LOCK_WRITE_GROWTH或LOCK_READ或LOCK_WRITE-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/what-do-i-do-if-my-apsaradb-rds-instance-is-in-the-locking-state

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-mysql/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-mysql/getting-started.md)

- [AI能力中心](products/rds/documents/apsaradb-rds-for-mysql/ai-capability-center.md)

- [自研内核AliSQL](products/rds/documents/apsaradb-rds-for-mysql/proprietary-alisql.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-mysql/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-mysql/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-mysql/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-mysql/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-mysql/support.md)

[首页](https://help.aliyun.com/zh)

# 实例状态显示“锁定中”时如何解决？

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

## 现象说明

- 

实例基本信息页实例运行状态为锁定中。

- 

实例为锁定中时，无法INSERT和UPDATE数据。

说明

- 

以RDS MySQL 5.6、5.7、8.0中20190815及之后的小版本为例，实例的锁定状态有以下三种：

- 

LOCK_WRITE_GROWTH：禁止磁盘增长锁，一般由于主实例磁盘满，禁止会使磁盘用量上升的操作。DELETE语句会产生大量binlog，会导致磁盘用量上升，如需清理数据，可使用DROP和TRUNCATE语句。

- 

LOCK_READ：禁读锁，一般由于只读实例磁盘满，禁止执行查询和写入。

- 

LOCK_WRITE：禁写锁，可能是由于实例过期、主机过期（仅MyBase产品有的状态）、实例迁移等产生，除LOCK_WRITE_GROWTH限制外，额外禁止了其他数据写入，如DROP和TRUNCATE等。

在实例锁定时，执行部分SQL语句会报ERROR 1290 (HY000): The MySQL server is running with the LOCK_WRITE_GROWTH option so it cannot execute this statement的错误提示。

- 

对于RDS MySQL 5.1、5.5所有小版本以及5.6、5.7、8.0中20190815之前的小版本，各种原因导致实例一旦被锁定，锁定后将无法进行任何操作。

## 常见原因

- 

实例存储空间已满。

- 

账号欠费或实例到期。

## 实例存储空间已满处理方法

在实例基本信息页查看实例存储空间是否已满。

解决方案：

- 

[释放存储空间](products/rds/documents/apsaradb-rds-for-mysql/what-do-i-do-if-my-apsaradb-rds-instance-is-in-the-locking-state.md)

- 

[扩容存储空间](products/rds/documents/apsaradb-rds-for-mysql/what-do-i-do-if-my-apsaradb-rds-instance-is-in-the-locking-state.md)

### 释放存储空间

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

单击左侧导航栏的监控与报警，查看实例各类数据占用的磁盘空间信息。

- 

根据不同数据库类型，清理对应磁盘空间。

警告

数据无价，请您谨慎清理，如非必要，不推荐清理数据，请采用扩容存储空间方式解除锁定；如果必须清理，请在清理前对数据库进行备份，避免数据丢失。

- 

临时文件（标准监控中对应temp_file_size）

产生原因：MySQL实例可能会由于查询语句的排序、分组、关联表产生的临时表文件，或者大事务未提交前产生的binlog cache文件，导致实例磁盘空间满。

解决方法：请参见[RDS MySQL](products/rds/documents/support/what-do-i-do-if-an-apsaradb-rds-for-mysql-instance-is-in-the-locked-state-because-its-storage-capacity-is-exhausted-by-temporary-files.md)[临时文件导致实例磁盘空间满且出现“锁定中”状态](products/rds/documents/support/what-do-i-do-if-an-apsaradb-rds-for-mysql-instance-is-in-the-locked-state-because-its-storage-capacity-is-exhausted-by-temporary-files.md)。

- 

日志文件（标准监控中对应binlog_size和general_log_size）

产生原因：数据库管理系统会生成查询日志、慢查询日志、错误日志等，帮助管理员监控数据库的性能和健康状况。

- 

- 

| 引擎 | 处理办法 |
| --- | --- |
| MySQL | 根据 监控与报警 中，磁盘空间的占用信息，清理对应的日志文件。 [MySQL Binlog](products/rds/documents/apsaradb-rds-for-mysql/what-do-i-do-if-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-is-exhausted-by-binary-log-files.md) [文件导致实例空间满的解决办法](products/rds/documents/apsaradb-rds-for-mysql/what-do-i-do-if-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-is-exhausted-by-binary-log-files.md) [General log](products/rds/documents/apsaradb-rds-for-mysql/handle-the-issue-that-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-is-exhausted-by-the-general-log-file.md) [导致实例空间满的解决办法](products/rds/documents/apsaradb-rds-for-mysql/handle-the-issue-that-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-is-exhausted-by-the-general-log-file.md) |
| PostgreSQL | RDS PostgreSQL 日志文件不支持手动删除。 您可以通过手动删除非活跃的 Replication Slot 来让 RDS PostgreSQL 内核自动清理 WAL 日志。具体方法，请参见 [WAL](products/rds/documents/apsaradb-rds-for-postgresql/use-the-wal-log-management-feature-for-an-apsaradb-rds-for-postgresql-instance.md) [日志管理](products/rds/documents/apsaradb-rds-for-postgresql/use-the-wal-log-management-feature-for-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| SQL Server | RDS SQL Server 日志文件不支持手动删除，但可以通过控制台 [收缩事务日志](products/rds/documents/apsaradb-rds-for-sql-server/troubleshoot-insufficient-storage-space-issues-on-an-apsaradb-rds-for-sql-server-instance.md) 。 |


- 

数据文件（标准监控中对应user_data_size）

- 

- 

- 

- 

- 

- 

- 

- 

| 数据库引擎 | 处理方法 |
| --- | --- |
| MySQL | [通过](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md) [DMS](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md) [连接实例](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md) 。 执行以下 SQL 语句，查看数据库的表大小，确认其中可以删除的历史数据或无用数据。 SELECT TABLE_NAME, concat(round((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024,2),'MB') AS DATA FROM information_schema. TABLES WHERE TABLE_SCHEMA = '<数据库名>' ORDER BY DATA + 0 DESC; 在对应数据库下使用 DROP TABLE <表名>; 命令清理数据。 清理后需要耐心等待一段时间（5 分钟左右），RDS 实例才会解锁。 |
| PostgreSQL | 通过 DMS 连接实例，详情请参见 [通过](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md) [DMS](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md) [登录](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md) [RDS](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md) [数据库](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md) 。 说明 若无法连接实例，请首先 [扩容存储空间](products/rds/documents/apsaradb-rds-for-mysql/what-do-i-do-if-my-apsaradb-rds-instance-is-in-the-locking-state.md) ，待扩容完成后再进行相应的磁盘空间清理。清理完成后，根据实际需求选择是否进行缩容。缩容的相关操作请参见 [变更配置](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md) 。 执行以下 SQL 语句，查看数据库的表大小，确认其中可以删除的历史数据或无用数据。 SELECT table_schema || '.' || table_name AS table_full_name, pg_total_relation_size('"' || table_schema || '"."' || table_name || '"') AS size FROM information_schema.tables ORDER BY pg_total_relation_size('"' || table_schema || '"."' || table_name || '"') DESC; 在对应数据库下使用 DROP TABLE <表名>; 命令清理数据。 清理后需要耐心等待一段时间（5 分钟左右），RDS 实例才会解锁。 |
| SQL Server | 请参见 [RDS SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/troubleshoot-insufficient-storage-space-issues-on-an-apsaradb-rds-for-sql-server-instance.md) [空间不足问题](products/rds/documents/apsaradb-rds-for-sql-server/troubleshoot-insufficient-storage-space-issues-on-an-apsaradb-rds-for-sql-server-instance.md) 处理。 |


- 

系统文件（标准监控中对应undolog_size）

产生原因：当存在对InnoDB表长时间不结束的查询语句，而且在查询过程中表有大量的数据变化时，系统会生成大量的undo信息，占用大量存储空间，导致存储空间耗尽。

解决方法：请参见[系统文件堆积导致空间不足](products/rds/documents/apsaradb-rds-for-mysql/troubleshoot-storage-issues-on-an-apsaradb-rds-for-mysql-instance.md)。

### 扩容存储空间

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在基本信息页面的配置信息区域单击变更配置，[扩容实例存储空间](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。

- 

完成支付后，您可在进入[任务中心](https://rdsnext.console.aliyun.com/jobCenter/cn-hangzhou)查看变配进度。

扩容时长与存储类型相关，具体如下。您可以访问[RDS](https://rdsnext.console.aliyun.com/dashboard/cn-hangzhou)[控制台首页](https://rdsnext.console.aliyun.com/dashboard/cn-hangzhou)，在左侧导航栏的任务中心中查看扩容进度。

- 

- 

- 

- 

| 存储类型 | 扩容时长 | 说明 |
| --- | --- | --- |
| 高性能本地盘 | 以实际情况为准。 | 本地无资源可用的情况下会触发跨机迁移，扩容时长受较多因素影响，推荐在业务低峰期进行扩容。 变配会出现约 15 秒的闪断，请在业务低峰期进行变配，并确保您的应用有自动重连机制。闪断期间，与数据库、账号、网络等相关的大部分操作都无法执行。 |
| 云盘 | 5 分钟左右。 | MySQL、PostgreSQL 云盘实例扩容期间不会发生业务闪断。 SQL Server 云盘实例 [扩容](products/rds/documents/apsaradb-rds-for-sql-server/change-the-specifications-of-an-apsaradb-rds-for-sql-server-instance.md) 期间可能会出现一次约 30 秒的闪断，与数据库、账号、网络等相关的大部分操作都无法执行，请尽量在业务低峰期执行变配操作，或确保您的应用有自动重连机制。 目前部分实例已支持无损扩容能力，不会造成数据库访问中断。 |


## 账号欠费或实例到期处理方法

- 

包年包月：如果实例已到期且未续费，为实例[续费](products/rds/documents/apsaradb-rds-for-mysql/manually-renew-an-apsaradb-rds-for-mysql-instance.md)后，等待5分钟查看实例状态是否为运行中。

- 

按量付费：如果账号已欠费，为账号[充值](https://usercenter2.aliyun.com/finance/fund-management/recharge)后，等待5分钟查看实例状态是否为运行中。

## 更多运维建议

建议您配置如下内容，避免实例被锁定。

- 

设置实例到期欠费预警提醒通知。

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[管理控制台](https://rdsnext.console.aliyun.com/rdsList/basic)。

- 

单击页面右上方的图标，进入消息中心页面。

- 

在左侧导航栏，单击基本接收管理。

- 

在基本接收管理页面的消息类型中勾选产品的欠费、停服、即将释放相关信息通知，单击修改。

- 

在修改消息接收人对话框，勾选需通知的联系人，单击保存，即可完成设置。

- 

设置实例[存储空间报警](products/rds/documents/apsaradb-rds-for-mysql/configure-an-alert-rule-for-an-apsaradb-rds-for-mysql-instance.md)，建议设置存储空间大于90%时报警。

- 

[开启](products/rds/documents/apsaradb-rds-for-mysql/use-the-sql-explorer-and-audit-feature-on-an-apsaradb-rds-for-mysql-instance.md)[SQL](products/rds/documents/apsaradb-rds-for-mysql/use-the-sql-explorer-and-audit-feature-on-an-apsaradb-rds-for-mysql-instance.md)[洞察与审计](products/rds/documents/apsaradb-rds-for-mysql/use-the-sql-explorer-and-audit-feature-on-an-apsaradb-rds-for-mysql-instance.md)，当存储空间突增时，结合监控与报警，查询存储空间增长期间的历史SQL语句，对SQL进行优化。

- 

设置自动扩容存储空间，当资源不足时，系统将自动扩容。详情请参见[设置](products/rds/documents/apsaradb-rds-for-mysql/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-mysql-instance.md)[存储空间自动扩容](products/rds/documents/apsaradb-rds-for-mysql/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-mysql-instance.md)、[设置](products/rds/documents/apsaradb-rds-for-postgresql/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-postgresql-instance.md)[RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-postgresql-instance.md)[存储空间自动扩容](products/rds/documents/apsaradb-rds-for-postgresql/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-postgresql-instance.md)和[设置](products/rds/documents/apsaradb-rds-for-sql-server/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-sqlserver-instance.md)[RDS SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-sqlserver-instance.md)[存储空间自动扩容](products/rds/documents/apsaradb-rds-for-sql-server/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-sqlserver-instance.md)。

- 

对于临时文件较大的场景，应优化SQL语句，避免频繁使用ORDER BY、GROUP BY操作。

## 实例已删除大量数据，为什么还是LOCK_WRITE_GROWTH？

使用DELETE语句删除数据时，数据库仅将记录或数据页标记为可复用，而不会直接减少磁盘文件的大小，即表空间不会自动回收。若需释放表空间，可[使用](products/rds/documents/apsaradb-rds-for-mysql/how-do-i-use-the-optimize-table-statement-to-release-the-tablespace-of-an-apsaradb-rds-for-mysql-instance.md)[OPTIMIZE TABLE](products/rds/documents/apsaradb-rds-for-mysql/how-do-i-use-the-optimize-table-statement-to-release-the-tablespace-of-an-apsaradb-rds-for-mysql-instance.md)[命令释放](products/rds/documents/apsaradb-rds-for-mysql/how-do-i-use-the-optimize-table-statement-to-release-the-tablespace-of-an-apsaradb-rds-for-mysql-instance.md)[MySQL](products/rds/documents/apsaradb-rds-for-mysql/how-do-i-use-the-optimize-table-statement-to-release-the-tablespace-of-an-apsaradb-rds-for-mysql-instance.md)[实例的表空间](products/rds/documents/apsaradb-rds-for-mysql/how-do-i-use-the-optimize-table-statement-to-release-the-tablespace-of-an-apsaradb-rds-for-mysql-instance.md)。

## 实例已经有充足空间或者已续费，为什么实例仍然被锁定？

因为实例当前有任务（如变更配置）在运行，需要等待任务结束后才会自动解锁。您可以在实例基本信息页右上角单击按钮页面跳转至任务列表页面查看任务进度。

## 实例显示“锁定中”，此时是否可以升降配？

只有实例因磁盘满导致的锁定可以升降配，欠费导致的锁定只能先续费后再升降配。

## 待解锁的实例是历史规格，如何通过扩容存储空间的方式解锁？

先将实例规格变更为在售实例规格，然后再扩容实例的存储空间。在售实例规格，请参见[主实例规格列表](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)。

## 实例处于“锁定中”，为何存储空间会有所增加？

在“锁定中”状态下，无法执行INSERT和UPDATE操作。然而，实例仍然可能因查询操作生成日志文件或其他临时数据，从而导致存储空间进一步增加。

[上一篇：通过自治服务解决MySQL实例CPU使用率过高的问题](products/rds/documents/apsaradb-rds-for-mysql/how-do-i-use-clouddba-to-reduce-the-cpu-utilization-of-my-apsaradb-rds-for-mysql-instance.md)[下一篇：使用OPTIMIZE TABLE命令释放MySQL实例的表空间](products/rds/documents/apsaradb-rds-for-mysql/how-do-i-use-the-optimize-table-statement-to-release-the-tablespace-of-an-apsaradb-rds-for-mysql-instance.md)

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
