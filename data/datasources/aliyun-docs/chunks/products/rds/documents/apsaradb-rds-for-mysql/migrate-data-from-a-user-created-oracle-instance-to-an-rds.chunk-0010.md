## 准备工作
登录待迁移的Oracle数据库，创建用于采集数据的账号并授权。
说明
如您已创建包含下述权限的账号，可跳过本步骤。

| 数据库 | 结构迁移 | 全量迁移 | 增量数据迁移 |
| --- | --- | --- | --- |
| 自建 Oracle 数据库 | Schema 的 Owner 权限 | Schema 的 Owner 权限 | 需要精细化授权 |
| RDS MySQL 实例 | 待迁入数据库的写权限 |  |  |

数据库账号创建及授权方法：
自建Oracle数据库请参见[数据库账号准备](https://help.aliyun.com/zh/dts/user-guide/configure-the-oracle-database-and-create-an-account#546a5ab1643wq)、[CREATE USER](https://docs.oracle.com/cd/B19306_01/server.102/b14200/statements_8003.htm)和[GRANT](https://docs.oracle.com/cd/B19306_01/server.102/b14200/statements_9013.htm)。
RDS MySQL实例请参见[创建账号](create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)和[修改账号权限](modify-the-permissions-of-a-standard-account-on-an-apsaradb-rds-for-mysql-instance.md)。
重要
如需迁移增量数据，您还需要开启归档和补充日志，以获取数据的增量变更。更多信息，请参见[数据库配置](https://help.aliyun.com/zh/dts/user-guide/configure-the-oracle-database-and-create-an-account#4f5033b1646ss)。
