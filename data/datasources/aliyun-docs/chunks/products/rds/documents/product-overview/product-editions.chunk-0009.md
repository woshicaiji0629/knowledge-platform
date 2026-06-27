## RDS SQL Server产品系列

| 系列 | 说明 | 适用场景 |
| --- | --- | --- |
| [基础系列](../apsaradb-rds-for-mysql/rds-basic-edition.md) | 单节点，计算与存储分离。 不支持增加只读实例。 | 个人学习。 微型网站。 中小企业的开发测试环境。 |
| [高可用系列](../apsaradb-rds-for-mysql/rds-high-availability-edition.md) | 一主一备的高可用架构，支持自动故障切换。备节点不可访问。 不支持增加只读实例。 | 大中型企业的生产数据库。 互联网、物联网、零售电商、物流、游戏等行业的数据库。 |
| [集群系列](../apsaradb-rds-for-mysql/rds-cluster-edition.md) | 一主一备的高可用架构，支持自动故障切换。备节点可访问，提升读能力。 支持增加 1~7 个 [只读实例](../apsaradb-rds-for-sql-server/create-a-read-only-apsaradb-rds-for-sql-server-instance.md) ，只读实例用于进一步提升读能力，但不参与主节点选举和切换。 | 大中型企业的生产数据库。 互联网新零售行业、汽车制造行业、企业大型 ERP 系统等。 |
