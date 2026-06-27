## 前提条件
RDS实例需满足以下条件：
实例系列：高可用系列、基础系列（不支持Serverless实例）
实例规格：不能是[历史规格](primary-apsaradb-rds-for-mysql-instance-types.md)。如需变更实例规格，请参见[变更配置](change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。
实例运行状态：运行中
说明
如果当前实例创建了只读实例，则只读实例的状态也需要为运行中，否则主节点迁移可用区时将报错OperationDenied.MasterDBInstancestate。
如果为云盘实例，内核小版本不可低于20201031。如何升级内核小版本，请参见[升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)。
实例所在的地域需要有多个可用区，才支持迁移可用区功能。关于地域和可用区的详情，请参见[地域和可用区](https://help.aliyun.com/zh/document_detail/40654.html#concept-2459516)。
实例未开通共享代理。
说明
确认共享代理的方法：您可以在实例控制台的数据库代理页面查看，如果有读写分离（共享）页签表示当前使用的是共享代理。
共享代理功能已于2021年04月01日停止更新维护，若您仍在使用共享代理，建议您[升级共享代理为独享型代理](upgrade-the-database-proxy-of-an-apsaradb-rds-for-mysql-instance-from-a-shared-proxy-to-a-dedicated-proxy.md)。
使用独享型代理或者通用型代理，不会影响可用区迁移。
其他引擎迁移可用区请参见：
[PostgreSQL](../apsaradb-rds-for-postgresql/migrate-an-apsaradb-rds-for-postgresql-instance-across-zones-in-the-same-region.md)[迁移可用区](../apsaradb-rds-for-postgresql/migrate-an-apsaradb-rds-for-postgresql-instance-across-zones-in-the-same-region.md)
[SQL Server](../apsaradb-rds-for-sql-server/migrate-an-apsaradb-rds-for-sql-server-instance-across-zones.md)[迁移可用区](../ap
