## 前提条件
您已创建PostgreSQL主实例，主实例满足以下条件：
实例版本：需为在售版本，[停售版本](lifecycles-of-major-engine-versions.md)不支持创建只读实例。
实例系列：高可用系列。
实例规格：
云盘：无特殊要求。
高性能本地盘：如果使用高性能本地盘，规格为独享套餐（8核32 GB及以上）。
计费方式：包年包月或按量付费，Serverless计费方式的实例暂不支持创建只读实例。
说明
创建PostgreSQL只读实例前，请在基本信息页面确认实例系列及规格信息。如果不满足要求，且需要创建只读实例时，请单击变更配置，将[基础系列变更为高可用系列](upgrade-an-apsaradb-rds-for-postgresql-instance-from-basic-edition-to-high-availability-edition.md)后再创建只读实例。
支持创建[高可用系列](rds-high-availability-edition.md)或[基础系列](rds-basic-edition.md)的只读实例；其中高可用系列的只读实例为高可用架构（由主节点和备节点组成）。
