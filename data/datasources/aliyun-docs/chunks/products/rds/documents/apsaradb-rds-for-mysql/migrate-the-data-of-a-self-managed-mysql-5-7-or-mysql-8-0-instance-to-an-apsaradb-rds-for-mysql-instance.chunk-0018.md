## 查看用户备份的日志信息
在[备份自建库](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)过程中，如果源库中存在数据修改的操作，则备份文件中会带有日志信息，方便您恢复这部分增量数据。
登录[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在页面左上角选择地域，并在左侧导航栏中单击备份管理。
单击目标备份ID右侧操作列下的详情。
在弹出的窗口中即可查询到日志的具体信息。
说明
日志信息中包含如下内容：
Master_Log_File：：日志的文件名，展示增量数据所在的起始日志文件。
Master_Log_Position：：日志文件中的位置信息，展示日志文件中增量数据的起始位置。
