## 创建账号
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏中选择账号管理。
单击创建账号。
设置如下参数。

| 参数 | 说明 |
| --- | --- |
| 数据库账号 | 长度为 2~63 个字符。 由小写字母、数字或下划线组成。 以字母开头，以字母或数字结尾。 不能和已有的账号名重复。 不能以 pg 开头。 不能使用 SQL 关键字。具体请参见 [SQL](https://www.postgresql.org/docs/14/sql-keywords-appendix.html) [关键字](https://www.postgresql.org/docs/14/sql-keywords-appendix.html) 。 |
| 账号类型 | RDS PostgreSQL 实例支持两种数据库账号：高权限账号和普通账号。 高权限账号拥有所有数据库的所有操作权限。 普通账号拥有已授权数据库（owner）的所有操作权限。 说明 操作权限包括 SELECT、INSERT、UPDATE、DELETE、TRUNCATE、REFERENCES、TRIGGER。 如需对账号权限进行精细化管理，例如创建只读账号，请参见 [RDS PostgreSQL](manage-permissions-in-an-apsaradb-rds-for-postgesql-instance.md) [权限管理最佳实践](manage-permissions-in-an-apsaradb-rds-for-postgesql-instance.md) 。 |
| 新密码 | 长度为 8~32 个字符。 由大写字母、小写字母、数字、特殊字符中的任意三种组成。 特殊字符为!@#$%^&*()_+-= |
| 确认密码 | 再次输入相同的密码。 |
| 备注 | 填写备注信息。 |

单击确定。
