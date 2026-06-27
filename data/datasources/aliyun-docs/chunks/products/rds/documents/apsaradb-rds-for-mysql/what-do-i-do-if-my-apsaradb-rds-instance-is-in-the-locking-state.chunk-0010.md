## 更多运维建议
建议您配置如下内容，避免实例被锁定。
设置实例到期欠费预警提醒通知。
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[管理控制台](https://rdsnext.console.aliyun.com/rdsList/basic)。
单击页面右上方的图标，进入消息中心页面。
在左侧导航栏，单击基本接收管理。
在基本接收管理页面的消息类型中勾选产品的欠费、停服、即将释放相关信息通知，单击修改。
在修改消息接收人对话框，勾选需通知的联系人，单击保存，即可完成设置。
设置实例[存储空间报警](configure-an-alert-rule-for-an-apsaradb-rds-for-mysql-instance.md)，建议设置存储空间大于90%时报警。
[开启](use-the-sql-explorer-and-audit-feature-on-an-apsaradb-rds-for-mysql-instance.md)[SQL](use-the-sql-explorer-and-audit-feature-on-an-apsaradb-rds-for-mysql-instance.md)[洞察与审计](use-the-sql-explorer-and-audit-feature-on-an-apsaradb-rds-for-mysql-instance.md)，当存储空间突增时，结合监控与报警，查询存储空间增长期间的历史SQL语句，对SQL进行优化。
设置自动扩容存储空间，当资源不足时，系统将自动扩容。详情请参见[设置](configure-automatic-storage-expansion-for-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](configure-automatic-storage-expansion-for-an-apsaradb-rds-for-mysql-instance.md)[存储空间自动扩容](configure-automatic-storage-expansion-for-an-apsaradb-rds-for-mysql-instance.md)、[设置](../apsaradb-rds-for-postgresql/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-postgresql-instance.md)[RDS PostgreSQL](../apsaradb-rds-for-postgresql/configure-automatic-storage-expansion-for-an-apsar
