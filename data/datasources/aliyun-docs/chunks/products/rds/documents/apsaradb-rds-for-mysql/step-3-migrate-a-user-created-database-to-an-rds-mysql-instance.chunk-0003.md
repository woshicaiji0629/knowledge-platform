## 方法一：使用DTS迁移至RDS MySQL实例
[数据传输服务](https://help.aliyun.com/zh/dts/product-overview/what-is-dts)[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts)（Data Transmission Service）是阿里云提供的实时数据流服务，支持关系型数据库（RDBMS）、非关系型的数据库（NoSQL）、数据多维分析（OLAP）等数据源间的数据交互，集数据同步、迁移、订阅、集成、加工于一体，助您构建安全、可扩展、高可用的数据架构。
本教程以ECS自建数据库为例，展示如何创建与配置DTS数据迁移任务，将自建数据库平滑迁移至RDS MySQL实例。
说明
从自建数据库向RDS MySQL迁移时，建议保持ECS实例与RDS实例在同一地域与同一VPC下（实例满足[内网访问条件](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)），使数据迁移过程更快速且稳定。
使用DTS进行数据迁移时的相关限制和注意事项请参见[从自建](migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md)[MySQL](migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md)[迁移至](migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md)[实例](migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md)。
登录[DMS](https://dms.aliyun.com/new?spm=a2c4g.211596.0.0.99dc646bcQs6s4)[数据管理服务](https://dms.aliyun.com/new?spm=a2c4g.211596.0.0.99dc646bcQs6s4)。
在顶部菜单栏选择Data + AI>数据传输 (DTS)>数据迁移。如果顶部没有菜单栏，可以点击右上
