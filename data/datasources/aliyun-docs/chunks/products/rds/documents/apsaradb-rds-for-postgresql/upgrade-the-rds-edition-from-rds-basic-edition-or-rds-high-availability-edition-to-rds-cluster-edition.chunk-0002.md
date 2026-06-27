## 前提条件
实例大版本为RDS PostgreSQL 14或以上版本。
实例系列为基础系列或高可用系列。
说明
您可以在实例的基本信息页面查看实例的系列。
实例存储类型为ESSD云盘或高性能云盘。
说明
实例存储类型为高性能云盘时，未开启IO加速或数据归档功能。
如果实例的存储类型为SSD云盘，请先升级为ESSD云盘。升级操作请参见[SSD](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)[云盘升级为](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)[ESSD](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)[云盘](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)。
实例为主实例，且没有只读实例。
实例未开通数据库代理服务。
实例未启用Babelfish，即小版本号后缀不带babelfish。
实例未开通连接池（PgBouncer）。
