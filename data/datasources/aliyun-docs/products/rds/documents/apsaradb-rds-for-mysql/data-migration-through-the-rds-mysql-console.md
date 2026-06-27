# RDS MySQL控制台操作，数据迁移，DTS，RDS MySQL，数据传输服务-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/data-migration-through-the-rds-mysql-console

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

# RDS MySQL控制台操作（数据迁移）

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍如何使用RDS MySQL控制台中的数据迁移功能，通过内部集成的数据传输服务（DTS）实现多种实例间的数据迁移链路。

## 前提条件

- 

已创建RDS MySQL实例。如未创建，请参见[快速创建](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[实例](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)。

- 

若您的MySQL数据库部署在本地或其他云上，您需要将DTS服务器的IP地址添加到该数据库远程连接的白名单中，以允许其访问您的数据库。更多信息，请参见[添加](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)[DTS](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)[服务器](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)[IP](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)[地址白名单](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)或[什么是数据传输服务](https://help.aliyun.com/zh/dts/product-overview/what-is-dts)[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts)。

- 

已根据业务需求创建对应的源库或目标库。当此RDS MySQL实例作为目标库时，实例的存储空间需大于已创建存储空间的源端实例。如需扩容RDS MySQL存储空间，请参见[变更配置](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。

说明

建议您开启RDS MySQL实例自动扩容功能，系统会在存储空间达到阈值时自动进行扩容。具体操作，请参见[设置存储空间自动扩容](products/rds/documents/apsaradb-rds-for-mysql/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-mysql-instance.md)。

- 

[授予](https://help.aliyun.com/zh/dts/user-guide/authorize-dts-to-access-alibaba-cloud-resources)[DTS](https://help.aliyun.com/zh/dts/user-guide/authorize-dts-to-access-alibaba-cloud-resources)[访问云资源的权限](https://help.aliyun.com/zh/dts/user-guide/authorize-dts-to-access-alibaba-cloud-resources)。

## 费用说明

该功能内部由DTS实现，收费项同DTS保持一致。更多信息，请参见[计费项](https://help.aliyun.com/zh/dts/product-overview/billable-items)。

## 操作步骤

- 

进入实例的数据迁移及同步页面。

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)。

- 

在上方选择地域，然后单击目标实例ID。

- 

进入实例页面后，单击左侧导航栏数据迁移及同步。

- 

选择数据迁移页签，然后单击创建迁移任务并进行以下步骤。

- 

配置源库及目标库

说明

选择当前RDS MySQL实例作为源端或目标端时，实例地区及RDS实例ID会自动配置且不支持手动修改。

- 

配置源端信息。

- 

输入数据库账号和数据库密码。

- 

选择连接方式。

- 

配置目标端信息。

- 

选择需要迁移的数据库类型及接入方式。

- 

选择目标端实例地区及RDS实例ID。

- 

选择连接方式。

- 

单击测试连接以进行下一步。

- 

对象配置

说明

此步骤与DTS旧版控制台一致，DTS新版控制台在此步骤进行了配置流程优化。详情请参见[DTS](https://help.aliyun.com/zh/dts/product-overview/dts-console-fully-upgraded)[新版控制台升级](https://help.aliyun.com/zh/dts/product-overview/dts-console-fully-upgraded)。

- 

选择迁移类型：库表结构迁移、全量迁移、增量迁移。

- 

选择目标已存在表的处理模式：预检查并报错拦截、忽略报错并继续执行。

- 

配置目标库对象名称大小写策略，您可以配置目标实例中迁移对象的库名、表名和列名的英文大小写策略。

说明

默认情况下选择DTS默认策略，您也可以选择与源库、目标库默认策略保持一致。更多信息，请参见[目标库对象名称大小写策略](https://help.aliyun.com/zh/dts/user-guide/specify-the-capitalization-of-object-names-in-the-destination-instance-2#concept-2045083)。

- 

在源库对象框中单击待迁移的对象，然后单击将其移动到已选择对象框。

- 

针对单个或多个（点击右上角批量编辑）迁移对象在目标实例中的名称进行更改。

- 

单击高级配置（选填）下拉框，进行高级参数配置。

- 

选择数据校验配置的数据校验方式，可选择的校验方式与[选择迁移类型](products/rds/documents/apsaradb-rds-for-mysql/data-migration-through-the-rds-mysql-console.md)步骤中的选项相对应。

- 

高级配置及后续步骤与DTS控制台保持一致，根据迁移源端和目标端的区别，请参见下表进行后续配置。

| 源库 | 目标库 | 相关文档 |
| --- | --- | --- |
| RDS MySQL | MySQL | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-apsaradb-rds-for-mysql-instances) [实例间的迁移](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-apsaradb-rds-for-mysql-instances) |
| PolarDB for MySQL | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-polardb-for-mysql-cluster-1) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-polardb-for-mysql-cluster-1) [PolarDB MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-polardb-for-mysql-cluster-1) [版](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-polardb-for-mysql-cluster-1) |  |
| AnalyticDB MySQL 3.0 | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-an-analyticdb-for-mysql-v3-0-cluster) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-an-analyticdb-for-mysql-v3-0-cluster) [AnalyticDB MySQL 3.0](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-an-analyticdb-for-mysql-v3-0-cluster) |  |
| Tair/Redis | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-tair-or-redis-instance) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-tair-or-redis-instance) [Tair/Redis](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-tair-or-redis-instance) |  |
| PostgreSQL | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-an-apsaradb-rds-for-postgresql-instance) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-an-apsaradb-rds-for-postgresql-instance) [RDS PostgreSQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-an-apsaradb-rds-for-postgresql-instance) |  |
| Kafka | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-message-queue-for-apache-kafka-instance) [迁移至阿里云消息队列](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-message-queue-for-apache-kafka-instance) [Kafka](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-message-queue-for-apache-kafka-instance) [版](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-message-queue-for-apache-kafka-instance) |  |
| AnalyticDB PostgreSQL | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-an-analyticdb-for-postgresql-instance) [迁移至云原生数据仓库 AnalyticDB PostgreSQL 版](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-an-analyticdb-for-postgresql-instance) |  |
| Oracle | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-self-managed-oracle-database) [迁移至自建](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-self-managed-oracle-database) [Oracle](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-self-managed-oracle-database) |  |
| PolarDB-X 1.0 | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-polardb-x-1-0-instance) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-polardb-x-1-0-instance) [PolarDB-X 1.0](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-polardb-x-1-0-instance) |  |
| PolarDB-X 2.0 | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-polardb-x-2-0-instance) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-polardb-x-2-0-instance) [PolarDB-X 2.0](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-polardb-x-2-0-instance) |  |
| ClickHouse | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-clickhouse-cluster) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-clickhouse-cluster) [ClickHouse](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-clickhouse-cluster) [集群](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-clickhouse-cluster) |  |
| DataHub | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-datahub-project) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-datahub-project) [DataHub](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-datahub-project) |  |
| Elasticsearch | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-an-elasticsearch-cluster) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-an-elasticsearch-cluster) [Elasticsearch](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-an-elasticsearch-cluster) |  |
| MaxCompute | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-maxcompute-project) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-maxcompute-project) [MaxCompute](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-maxcompute-project) |  |
| SelectDB | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-an-apsaradb-for-selectdb-instance) [迁移至云数据库](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-an-apsaradb-for-selectdb-instance) [SelectDB](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-an-apsaradb-for-selectdb-instance) [版](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-an-apsaradb-for-selectdb-instance) |  |
| Tablestore | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-tablestore-instance) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-tablestore-instance) [Tablestore](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-tablestore-instance) |  |
| Lindorm | [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-lindorm-instance) [迁移至云原生多模数据库](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-lindorm-instance) [Lindorm](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mysql-instance-to-a-lindorm-instance) |  |
| MySQL | RDS MySQL | [自建](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance-1) [MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance-1) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance-1) [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance-1) |
| PolarDB for MySQL | [PolarDB MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-polardb-for-mysql-cluster-to-an-apsaradb-rds-for-mysql-instance) [版迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-polardb-for-mysql-cluster-to-an-apsaradb-rds-for-mysql-instance) [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-polardb-for-mysql-cluster-to-an-apsaradb-rds-for-mysql-instance) |  |
| SQL Server | [RDS SQL Server](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-sql-server-instance-to-an-apsaradb-rds-for-mysql-instance) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-sql-server-instance-to-an-apsaradb-rds-for-mysql-instance) [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-sql-server-instance-to-an-apsaradb-rds-for-mysql-instance) |  |
| PostgreSQL | [RDS PostgreSQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-postgresql-instance-to-an-apsaradb-rds-for-mysql-instance-1) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-postgresql-instance-to-an-apsaradb-rds-for-mysql-instance-1) [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-postgresql-instance-to-an-apsaradb-rds-for-mysql-instance-1) |  |
| Oracle | [自建](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-oracle-database-to-an-apsaradb-rds-for-mysql-instance-1) [Oracle](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-oracle-database-to-an-apsaradb-rds-for-mysql-instance-1) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-oracle-database-to-an-apsaradb-rds-for-mysql-instance-1) [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-oracle-database-to-an-apsaradb-rds-for-mysql-instance-1) |  |
| PolarDB-X 1.0 | [PolarDB-X 1.0](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-polardb-x-1-0-instance-to-an-apsaradb-rds-for-mysql-instance) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-polardb-x-1-0-instance-to-an-apsaradb-rds-for-mysql-instance) [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-polardb-x-1-0-instance-to-an-apsaradb-rds-for-mysql-instance) |  |
| PolarDB-X 2.0 | [PolarDB-X 2.0](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-polardb-x-2-0-instance-to-an-apsaradb-rds-for-mysql-instance) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-polardb-x-2-0-instance-to-an-apsaradb-rds-for-mysql-instance) [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-polardb-x-2-0-instance-to-an-apsaradb-rds-for-mysql-instance) |  |
| DB2 LUW | [Db2 for LUW](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-db2-for-luw-database-to-an-apsaradb-rds-for-mysql-instance) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-db2-for-luw-database-to-an-apsaradb-rds-for-mysql-instance) [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-db2-for-luw-database-to-an-apsaradb-rds-for-mysql-instance) |  |
| Mariadb | [RDS MariaDB](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mariadb-instance-to-an-apsaradb-rds-for-mysql-instance-new) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mariadb-instance-to-an-apsaradb-rds-for-mysql-instance-new) [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-apsaradb-rds-for-mariadb-instance-to-an-apsaradb-rds-for-mysql-instance-new) |  |
| MaxCompute | [MaxCompute](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-maxcompute-project-to-an-apsaradb-rds-for-mysql-instance-new) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-maxcompute-project-to-an-apsaradb-rds-for-mysql-instance-new) [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-maxcompute-project-to-an-apsaradb-rds-for-mysql-instance-new) |  |
| OceanBase（MySQL） | [OceanBase（MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-oceanbase-mysql-database-to-an-rds-mysql-instance) [模式）迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-oceanbase-mysql-database-to-an-rds-mysql-instance) [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-oceanbase-mysql-database-to-an-rds-mysql-instance) |  |
| TiDB | [自建](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-tidb-database-to-an-apsaradb-rds-for-mysql-instance) [TiDB](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-tidb-database-to-an-apsaradb-rds-for-mysql-instance) [迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-tidb-database-to-an-apsaradb-rds-for-mysql-instance) [RDS MySQL](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-tidb-database-to-an-apsaradb-rds-for-mysql-instance) |  |


说明

跨云迁移请参见[跨阿里云账号迁移](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-apsaradb-rds-instances-of-different-alibaba-cloud-accounts)[RDS](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-apsaradb-rds-instances-of-different-alibaba-cloud-accounts)[实例](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-apsaradb-rds-instances-of-different-alibaba-cloud-accounts)。

## 常见问题

Q：运行DTS任务时出现报错信息DTS-RETRY-ERR-0069：Datasource rejected establishment of connection (.*)? Too many connections，如何解决？

A：可能原因：源端或目标端数据库的连接数过多。

解决方法：调整源端或目标端数据库的最大连接数，并重新启动任务。具体操作，请参见[修改最大连接数](products/rds/documents/apsaradb-rds-for-mysql/modify-the-parameters-that-specify-the-maximum-number-of-connections-to-an-apsaradb-rds-for-mysql-instance.md)。

更多DTS报错信息及解决方法，请参见[常见报错](https://help.aliyun.com/zh/dts/support/common-errors-and-troubleshooting/)。

[上一篇：数据迁移](products/rds/documents/apsaradb-rds-for-mysql/data-migration-1.md)[下一篇：从CSV文件、TXT文件或SQL脚本导入数据到RDS](products/rds/documents/apsaradb-rds-for-mysql/import-data-from-csv-files-txt-files-or-sql-scripts-to-rds-instances.md)

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
