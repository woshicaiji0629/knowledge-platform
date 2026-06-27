## 前提条件
实例满足以下条件：
大版本：PostgreSQL 10或以上版本
存储类型：ESSD云盘或高性能云盘
说明
您可以前往实例基本信息页查看以上信息。
如果在2022年10月10日前（旧架构实例）创建的云盘实例，需要升级内核小版本到最新后，再缩容存储空间。更多信息，请参见[升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md)。
如果您的RDS实例为高性能本地盘实例，建议使用大版本升级功能，将实例升级到云盘高版本，在升级的同时支持存储空间缩容。更多信息，请参见[升级数据库大版本](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md)。
您的阿里云账号没有未支付的续费订单。
您可以前往[订单列表](https://usercenter2.aliyun.com/order/list)页查看是否存在未支付的订单，然后支付或作废订单。
实例状态为运行中。
只读实例存储空间缩容时，其所属主实例的状态必须为运行中。
