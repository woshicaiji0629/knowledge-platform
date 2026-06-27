录，进入Smartbi。
说明
管理员默认登录账号为admin，密码为manager。
如果是首次登录，则需要修改管理员密码。
在左侧单击
在新建关系数据库对话框中配置相关参数，然后单击测试连接(T)。驱动程序存放目录选择产品内置，链接方式选择用户名密码，验证类型选择静态，填写完成后单击测试连接(T)验证连接是否正常。

| 参数 | 说明 |
| --- | --- |
| 名称 | 数据库连接的名称，自定义。 |
| 驱动程序类型 | 固定选择为 PostgreSQL。 |
| 驱动程序类 | 选择 驱动程序类型 后自动选择，无需修改。 |
| 连接字符串 | 连接 RDS PostgreSQL 实例的 JDBC 连接串，格式如下： jdbc:postgresql://<servername>:<port>/<dbName>?defaultRowFetchSize=10000 <servername>:<port> ：RDS PostgreSQL 实例的连接地址和对应的端口。 若通过内网连接，需输入 RDS 实例的内网地址和内网端口。 若使用外网连接，需输入 RDS 实例的外网地址和外网端口。 您可以在 RDS PostgreSQL 实例的数据库连接页面查看。 更多信息，请参见 [查看或修改连接地址和端口](view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) 。 <dbName> ：postgres 是 RDS PostgreSQL 实例默认的系统数据库，请勿在该数据库中进行任何操作。 建议配置 RDS 实例下已创建的其他数据库。如何创建和查看数据库，请参见 [创建数据库](create-a-database-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 用户名 、 密码 | 创建 RDS 实例的账号请参见 [创建账号](create-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |

测试通过后，单击保存，出现如下信息，表示连接成功。连接成功后，左侧导航面板的数据连接列表中将显示RDS_PostgreSQL节点，展开该节点可查看表关系视图、计算字段和过滤器三个子项。
