## 方法二：使用客户端连接实例
RDS与原生的数据库服务完全兼容，所以您可以使用任何通用的数据库客户端连接到RDS实例，且连接方法类似。下文以[HeidiSQL](https://www.heidisql.com/)为例。
启动HeidiSQL客户端。
在左下角单击新建。
输入要连接的RDS实例信息，参数说明如下。

| 参数 | 说明 |
| --- | --- |
| 网络类型 | 连接数据库的形式。选择 MariaDB or MySQL（TCP/IP） 。 |
| Library | 动态链接库。保持默认值即可。 |
| 主机名/IP 地址 | 输入 RDS 实例的内网地址或外网地址，例如 rm-bp1xxxxxxxxxxxxxx.mysql.rds.aliyuncs.com 。 关于如何查看地址信息，请参见 [查看或修改内外网地址和端口](view-and-change-the-internal-and-public-endpoints-and-port-numbers-of-an-apsaradb-rds-for-mariadb-instance.md) 。 若您的客户端部署在 ECS 实例上，且 ECS 实例与要访问的 RDS 实例的地域、网络类型相同，请使用内网地址。例如 ECS 实例和 RDS 实例都是华东 1 的专有网络实例，使用内网地址连接能提供安全高效的访问。 其它情况只能使用外网地址。 |
| 用户 | RDS 实例中创建的账号名称。关于如何创建账号，请参见 [创建数据库和账号](create-a-database-and-an-account-on-an-apsaradb-rds-for-mariadb-instance.md) 。 |
| 密码 | 账号对应的密码。 |
| 端口 | 若使用内网连接，需输入 RDS 实例的内网端口。若使用外网连接，需输入 RDS 实例的外网端口。更多信息，请参见 [查看或修改内外网地址和端口](view-and-change-the-internal-and-public-endpoints-and-port-numbers-of-an-apsaradb-rds-for-mariadb-instance.md) 。 |
