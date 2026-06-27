## 常见问题
Q1：测试连接报错“JDBC: [conn_error, cause: null, message from server: "Host 'XXX' is not allowed to connect to this MySQL server"]; PING: []; TELNET: []; requestId=[XXX]”
该报错为JDBC异常，请您检查JDBC的账号、密码及权限问题，或使用高权限账号测试连接。
Q2：创建迁移任务，为什么无法选择福州地域的RDS实例？
目前DTS不支持福州地域的实例。您可以将[MySQL 5.7、8.0](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[自建数据库备份上云](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)。
该文章对您有帮助吗？
反馈
