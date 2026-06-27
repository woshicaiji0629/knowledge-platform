## 前提条件
已创建RDS PostgreSQL实例。更多信息，请参见[创建](create-an-apsaradb-rds-for-postgresql-instance-1.md)[RDS PostgreSQL](create-an-apsaradb-rds-for-postgresql-instance-1.md)[实例](create-an-apsaradb-rds-for-postgresql-instance-1.md)。
已创建账号和数据库。更多信息，请参见[创建账号和数据库](create-a-database-and-an-account-on-an-apsaradb-rds-for-postgresql-instance.md)。
已设置白名单，允许客户端所在的ECS或本地设备访问RDS PostgreSQL实例。更多信息，请参见[设置白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance.md)。
如果使用ECS通过内网访问RDS PostgreSQL，ECS与RDS PostgreSQL实例必须位于同一阿里云账号下的同一地域及同一VPC内，同时应将ECS的私网IP地址添加至白名单。
如果使用本地设备访问RDS PostgreSQL，则将本地设备的公网IP添加到白名单。
