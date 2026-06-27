jectName backup_qp.xb' &
说明
此过程的时长取决于实例在备份时的状态，例如备份期间原实例中有太多写入操作，导致实例大量生成redo日志、或实例中执行了大型的事务等情况下，备份时间会变长。当备份顺利完成后，屏幕上会打印出completed OK !。
如您暂时无法使用阿里云OSS服务，可先将自建库备份至本地，等可以顺利访问OSS后再上传。更多信息，请参见[附录](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[3：分步骤执行全量备份和上传至](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[OSS](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)。
完成此步骤后，可以登录[OSS](https://oss.console.aliyun.com/bucket)[控制台](https://oss.console.aliyun.com/bucket)确认备份文件是否上传成功。如未上传成功，请重复执行步骤2。
登录[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在页面左上角选择地域，在左侧导航栏中单击备份管理。
单击用户备份页签下的导入备份按钮。
在弹出的导入备份对话框中，仔细阅读相关说明并单击下一步，直至切换到3. 数据导入页签。
说明
向导窗口引导您如何导入备份，详情如下。更多操作，请参见[分步骤执行全量备份并上传至](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[OSS](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)。
1. 备份你的数据库：全量备份自建库中的数据。
2. 上传备份文件到OSS：将自建库的全量备份数据上传到OSS
