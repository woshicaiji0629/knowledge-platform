### PostgreSQL命令行工具连接
通过[PostgreSQL](https://www.postgresql.org/download/)[官方网站](https://www.postgresql.org/download/)下载并安装PostgreSQL时，将会自动安装PostgreSQL命令行终端工具（Command Line Tools）。
在命令行终端中输入如下命令连接RDS PostgreSQL数据库。
psql -h <实例连接地址> -U <用户名> -p <端口号> [-d <数据库名>]
C:\Users\Administrator>psql -h pgm-xxx.pg.rds.aliyuncs.com -p 5432 -U xxx -d postgres 用户 xxx 的口令; psql (13.4, 服务器 11.9) 输入 "help" 来获取帮助信息. postgres=>

| 参数 | 说明 |
| --- | --- |
| 实例连接地址 | RDS PostgreSQL 实例的连接地址及对应的端口。 若通过内网连接，需输入 RDS 实例的内网地址和内网端口。 若使用外网连接，需输入 RDS 实例的外网地址和外网端口。 您可以在 RDS PostgreSQL 实例的数据库连接页面查看。 更多信息，请参见 [查看或修改连接地址和端口](view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 端口号 |  |
| 用户名 | RDS PostgreSQL 实例的账号。 创建 RDS 实例的账号请参见 [创建账号和数据库](create-a-database-and-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 数据库名 | 可选，需要连接的数据库名，postgres 是 RDS PostgreSQL 实例默认的系统数据库，请勿在该数据库中进行任何操作，建议配置 RDS 实例下已创建的其他数据库。 如何创建和查看数据库，请参见 [创建数据库](create-a-database-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |
