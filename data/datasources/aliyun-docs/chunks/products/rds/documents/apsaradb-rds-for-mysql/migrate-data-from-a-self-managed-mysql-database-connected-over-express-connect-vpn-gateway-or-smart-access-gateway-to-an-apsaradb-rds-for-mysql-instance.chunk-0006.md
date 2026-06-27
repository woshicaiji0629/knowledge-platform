## 数据库账号的权限要求

| 数据库 | 结构迁移 | 全量迁移 | 增量迁移 |
| --- | --- | --- | --- |
| 自建 MySQL 数据库 | SELECT 权限 | SELECT 权限 | REPLICATION SLAVE、REPLICATION CLIENT、SHOW VIEW 和 SELECT 权限 |
| RDS MySQL 或 RDS MySQL Serverless 实例 | 读写权限 | 读写权限 | 读写权限 |

数据库账号创建及授权方法：
自建MySQL数据库请参见[为自建](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)[MySQL](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)[创建账号并设置](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)[binlog](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)。
RDS MySQL或RDS MySQL Serverless实例请参见[创建账号](create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)和[修改账号权限](modify-the-permissions-of-a-standard-account-on-an-apsaradb-rds-for-mysql-instance.md)。
