## 数据库账号的权限要求

| 数据库 | 结构迁移 | 全量迁移 | 增量迁移 |
| --- | --- | --- | --- |
| Db2 数据库 | CONNECT、SELECT 权限 | CONNECT、SELECT 权限 | DBADM 权限 |
| RDS MySQL 或 RDS MySQL Serverless 实例 | 读写权限 | 读写权限 | 读写权限 |

数据库账号创建及授权方法：
Db2数据库请参见[创建用户](https://www.ibm.com/support/knowledgecenter/zh/SSEPGG_11.1.0/com.ibm.db2.luw.qb.server.doc/doc/t0006742.html#t0006742)和[权限概述](https://www.ibm.com/support/knowledgecenter/zh/SSEPGG_11.1.0/com.ibm.db2.luw.admin.sec.doc/doc/c0055206.html)。
RDS MySQL或RDS MySQL Serverless请参见[创建账号](create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)和[修改账号权限](modify-the-permissions-of-a-standard-account-on-an-apsaradb-rds-for-mysql-instance.md)。
