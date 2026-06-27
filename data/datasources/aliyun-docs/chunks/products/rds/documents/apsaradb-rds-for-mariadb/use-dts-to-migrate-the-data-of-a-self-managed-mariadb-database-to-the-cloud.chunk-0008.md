## 数据库账号的权限要求

| 数据库 | 库表结构迁移 | 全量迁移 | 增量迁移 |
| --- | --- | --- | --- |
| 自建 MariaDB 数据库 | SELECT 权限 | SELECT 权限 | 增量数据迁移：待迁移对象的 SELECT 权限 REPLICATION CLIENT、REPLICATION SLAVE、SHOW VIEW 建库建表的权限，以允许 DTS 创建库 test ，用于记录迁移期间的心跳数据 |
| RDS MariaDB 实例 | 读写权限 |  |  |

数据库账号创建及授权方法：
自建MariaDB实例请参见[创建账号](https://mariadb.com/kb/zh-cn/create-user/)和[账号授权](https://mariadb.com/kb/zh-cn/grant/)。
RDS MariaDB实例请参见[创建账号](create-an-account-on-an-apsaradb-rds-for-mariadb-instance.md)和[修改或重置账号权限](modify-the-permissions-of-a-standard-account-on-an-apsaradb-rds-for-mariadb-instance.md)。
