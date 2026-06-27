## 前提条件
已创建源数据库自建Oracle和目标实例RDS MySQL。
说明
目标实例RDS MySQL的创建方式，请参见[快速创建](../create-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](../create-an-apsaradb-rds-for-mysql-instance.md)[实例](../create-an-apsaradb-rds-for-mysql-instance.md)。
源数据库和目标实例支持的版本，请参见[迁移方案概览](https://help.aliyun.com/zh/dts/user-guide/overview-of-data-migration-scenarios#concept-26618-zh)。
自建Oracle数据库已开启ARCHIVELOG（归档模式），设置合理的归档日志保持周期且归档日志能够被访问，详情请参见[ARCHIVELOG](https://docs.oracle.com/database/121/ADMIN/archredo.htm#ADMIN008)。
自建Oracle数据库已开启Supplemental Logging，且已开启supplemental_log_data_pk，supplemental_log_data_ui，详情请参见[Supplemental Logging](https://docs.oracle.com/database/121/SUTIL/GUID-D857AF96-AC24-4CA1-B620-8EA3DF30D72E.htm#SUTIL1582)。
已创建目标RDS MySQL实例，创建方式，请参见[快速创建](../create-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](../create-an-apsaradb-rds-for-mysql-instance.md)[实例](../create-an-apsaradb-rds-for-mysql-instance.md)。
建议在执行数据迁移前了解源库为Oracle时DTS支持的能力和限制条件，并使用ADAM（Advanced Database & Application Migration）进行数据库评估，以便您平滑地迁移上云。更多信息，请参见[Oracle](https://help.aliyun.com/zh/dts/user-guide/configure-the-oracle-database-and-create-an-account)[数据库的限制和准备工作](https://help.aliyun.com/zh/dts/user-guide/configure-the-or
