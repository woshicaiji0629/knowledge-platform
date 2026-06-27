## 数据库账号的权限要求

| 数据库 | 结构迁移 | 全量迁移 | 增量迁移 |
| --- | --- | --- | --- |
| RDS MariaDB 实例 | SELECT 权限 | SELECT 权限 | REPLICATION CLIENT、REPLICATION SLAVE、SHOW VIEW 和 SELECT 权限 |
| RDS MySQL 实例 | 读写权限 | 读写权限 | 读写权限 |

数据库账号创建及授权方法：
RDS MariaDB实例：请参见[创建账号](create-a-database-and-an-account-on-an-apsaradb-rds-for-mariadb-instance.md)。
RDS MySQL实例：请参见[创建账号](../apsaradb-rds-for-mysql/create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)和[修改账号权限](../apsaradb-rds-for-mysql/modify-the-permissions-of-a-standard-account-on-an-apsaradb-rds-for-mysql-instance.md)。
