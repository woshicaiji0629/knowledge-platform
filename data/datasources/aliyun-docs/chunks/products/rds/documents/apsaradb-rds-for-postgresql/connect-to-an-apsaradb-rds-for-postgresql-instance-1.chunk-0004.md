### pgAdmin客户端连接
pgAdmin客户端是PostgreSQL官方推荐的数据库连接工具，在[PostgreSQL](https://www.postgresql.org/download/)[官方网站](https://www.postgresql.org/download/)下载并安装PostgreSQL时，将会自动安装pgAdmin 4客户端。下文以pgAdmin 4 V6.2.0为例，介绍如何连接RDS PostgreSQL实例。
如果您不想安装PostgreSQL，也可以单独下载[pgAdmin](https://www.pgadmin.org/download/)[客户端](https://www.pgadmin.org/download/)，仅用于连接远程数据库。
启动pgAdmin 4客户端。
说明
高版本客户端首次登录需要设置Master Password用于保护保存的密码和其他凭据。
右键单击Servers，选择Register>Server...。
在General页签设置连接名称。 在General标签页的Name字段中输入自定义的服务器名称。
选择Connection标签页，输入要连接的实例信息。 在Connection标签页，填写以下连接参数，完成后单击Save。

| 参数 | 说明 |
| --- | --- |
| Host name/address | RDS PostgreSQL 实例的连接地址及对应的端口。 若通过内网连接，需输入 RDS 实例的内网地址和内网端口。 若使用外网连接，需输入 RDS 实例的外网地址和外网端口。 您可以在 RDS PostgreSQL 实例的数据库连接页面查看。 更多信息，请参见 [查看或修改连接地址和端口](view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| Port |  |
| Username | RDS PostgreSQL 实例的账号和密码。 创建 RDS 实例的账号请参见 [创建账号和数据库](create-a-database-and-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| Password |  |
