## 注意事项
默认情况下，自建库迁移到RDS以后表名统一变为小写。您可以通过如下两种方法让RDS MySQL或RDS MySQL Serverless实例区分表名大小写。
在[创建](create-an-apsaradb-rds-for-mysql-instance-1.md)[RDS MySQL](create-an-apsaradb-rds-for-mysql-instance-1.md)[实例](create-an-apsaradb-rds-for-mysql-instance-1.md)或[创建](rds-mysql-serverless.md)[RDS MySQL Serverless](rds-mysql-serverless.md)[实例](rds-mysql-serverless.md)时将表名大小写设置为区分大小写。
已经创建好的实例，可以[设置实例参数](modify-the-parameters-of-an-apsaradb-rds-for-mysql-instance.md)lower_case_table_names的参数值为0以区分表名大小写。
警告
lower_case_table_names参数设置为0后，务必不要再次设置为1，否则可能导致ERROR 1146 (42S02): Table doesn't exist错误，对业务造成严重影响。
RDS MySQL 8.0和8.4版本实例暂不支持修改该参数，请在创建实例时进行设置。
