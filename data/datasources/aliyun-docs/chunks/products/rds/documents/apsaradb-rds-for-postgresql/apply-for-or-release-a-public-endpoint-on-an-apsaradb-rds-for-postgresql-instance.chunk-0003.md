## 相关文档
开通外网地址后，您需要将客户端或应用程序所在机器的公网IP添加到RDS实例的白名单中，才能通过外网访问RDS实例。更多信息，请参见[设置白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance-1.md)。
您可以通过pgAdmin客户端、PostgreSQL命令行工具、应用程序等方式连接RDS实例。更多信息，请参见[连接](connect-to-an-apsaradb-rds-for-postgresql-instance.md)[PostgreSQL](connect-to-an-apsaradb-rds-for-postgresql-instance.md)[实例](connect-to-an-apsaradb-rds-for-postgresql-instance.md)。
您可以通过API开通或释放外网地址。

| API | 描述 |
| --- | --- |
| [AllocateInstancePublicConnection](api-rds-2014-08-15-allocateinstancepublicconnection-postgresql.md) | 开通实例的外网地址 |
| [ReleaseInstancePublicConnection](api-rds-2014-08-15-releaseinstancepublicconnection-postgresql.md) | 关闭实例的外网地址 |

该文章对您有帮助吗？
反馈
