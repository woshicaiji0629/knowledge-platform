## 安全限制

| 限制项 | 限制说明 |
| --- | --- |
| 密码 | 密码需要满足以下要求： 长度为 8~32 个字符。 由大写字母、小写字母、数字、特殊字符中的至少三种组成。特殊字符为： !@#$%^&*()_+-= 。 |
| 端口 | RDS PostgreSQL 实例的默认端口为 5432，允许用户手动修改端口号。 |
| 实例参数 | 出于安全和稳定性考虑，部分参数不支持修改。大部分实例参数可以使用控制台或 API 进行修改，修改参数方法请参见 [设置实例参数](modify-the-parameters-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 云盘加密 | 云盘加密只能在创建实例时开启且不能关闭。设置云盘加密，请参见 [云盘加密](configure-disk-encryption-for-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 实例可加入安全组数量 | 最大 10 个。 如果云数据库 RDS 实例与云服务器处于不同的安全组，云服务器不能访问 RDS。 RDS 实例只能添加与自身网络类型相同的安全组，即实例为专有网络 VPC 时，只能添加 VPC 类型的安全组；实例为经典网络时，只能添加经典网络类型的安全组。 设置安全组，请参见 [设置安全组](configure-a-security-group-for-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 实例可添加白名单分组数量 | 最大 50 个。添加白名单，请参见 [设置白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance-1.md) 。 |
| root 权限账号 | 不可创建，RDS 无法向用户提供 superuser 权限。 |
| 高权限账号 | 高权限账号只能通过控制台或 API 创建和管理。支持多个高权限账号，可以断开任意账号的连接。 创建账号，请参见 [创建账号](create-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 普通账号 | 普通账号可以通过控制台、API 或者 SQL 语句创建和管理。需要手动给普通账号授予特定数据库的权限。不能创建和管理其他账号，也不能断开其他账号的连接。 创建账号，请参见 [创建账号](create-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |
