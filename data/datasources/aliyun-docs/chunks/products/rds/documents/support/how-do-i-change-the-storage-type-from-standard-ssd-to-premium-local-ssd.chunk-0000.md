# 云盘如何变更为高性能本地盘
本文介绍RDS的云盘如何变更为高性能本地盘。
仅当RDS实例为RDS MySQL 5.7基础系列（SSD云盘）时，可在使用变更配置功能将实例系列变更为高可用系列的同时，将存储类型变更为高性能本地盘。具体操作，请参见[变更配置](../apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。
其它情况，不支持直接将存储类型变更为高性能本地盘，您可以[创建](../create-an-apsaradb-rds-for-mysql-instance.md)一个新的RDS高性能本地盘实例，再将旧实例的数据[迁移](../apsaradb-rds-for-mysql/migrate-data-between-apsaradb-rds-for-mysql-instances.md)到新实例。
该文章对您有帮助吗？
反馈
