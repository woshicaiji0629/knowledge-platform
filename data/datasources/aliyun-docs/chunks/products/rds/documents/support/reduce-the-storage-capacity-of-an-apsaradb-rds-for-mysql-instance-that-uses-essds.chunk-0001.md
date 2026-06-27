## 前提条件
RDS MySQL实例需满足以下条件才能缩容，您可前往实例基本信息页面查看实例信息：
数据库版本：
MySQL 8.4
MySQL 8.0、5.7：内核小版本在20210430及以上
存储类型：ESSD云盘、高性能云盘（不支持SSD云盘）
说明
SSD云盘实例请先[升级至](../apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md)[ESSD](../apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md)[云盘](../apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md)后，再缩容存储空间。
实例架构版本：仅支持新架构（kindcode=18）版本。
说明
您可通过API（[DescribeDBInstanceAttribute](../developer-reference/api-rds-2014-08-15-describedbinstanceattribute.md)）查询实例架构版本，若为旧架构（kindcode=1或3），需先[发起一次内核小版本升级操作](../apsaradb-rds-for-mysql/update-the-minor-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)升级到新架构后再缩容。
实例运行中，且已开启[日志备份功能](use-the-log-backup-feature.md)。
您的阿里云账号没有未支付的续费订单。
说明
如果有未支付的续费订单，请您在RDS控制台右上方，将鼠标悬浮至费用，单击订单，在订单列表页面完成支付或作废订单。
云盘版只读实例存储空间缩容时，其所属主实例的状态必须为运行中，且主实例已开启[日志备份功能](use-the-log-backup-feature.md)。
