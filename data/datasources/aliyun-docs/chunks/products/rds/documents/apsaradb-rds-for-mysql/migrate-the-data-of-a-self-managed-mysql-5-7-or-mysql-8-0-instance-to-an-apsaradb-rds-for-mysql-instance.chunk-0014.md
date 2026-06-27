| 参数名 | 说明 |
| --- | --- |
| MySQL 版本 | 系统自动显示为 5.7/8.0 。 说明 仅支持导入备份自建数据库的版本为 MySQL 5.7 或 8.0。 |
| 地域 | [步骤](restore-the-data-of-a-self-managed-mysql-instance-to-an-apsaradb-rds-for-mysql-instance.md) [1](restore-the-data-of-a-self-managed-mysql-instance-to-an-apsaradb-rds-for-mysql-instance.md) 中选择的地域，该地域需要和备份文件所在的 OSS Bucket 的地域一致。 |
| OSS Bucket | 选择自建库备份文件所在的 OSS Bucket。关于 OSS Bucket 的更多信息，请参见 [上传文件](../../../oss/documents/upload-download-and-manage-objects-upload-objects.md) 。 |
| OSS 文件名 | 选择 OSS Bucket 中的自建库备份文件。您可以在 OSS 文件名 右侧的文本框中输入备份文件的文件名快速查找。本功能支持模糊匹配和精确匹配。 说明 OSS 中的备份文件必须为 _QP.XB 格式，或者将 _QP.XB 格式的文件压缩为 TAR.GZ 格式进行存储。 更多限制，请参见 [附录：使用限制](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md) 。 |
| 备注 | 自定义备份文件的备注信息。 |
| 可用区 | 设置用户备份的可用区。选择可用区后，系统会在该可用区内创建一个秒级快照，大幅节省备份导入所需要的时间。 说明 用户备份导入完成，并通过其恢复到新实例时，该可用区即为新实例所在的可用区。 |

说明
如您未授权RDS访问OSS，请先在3. 数据导入页面下方单击授权地址，在跳转到的页面左下角单击同意授权。
更多导入备份时的注意事项请仔细阅读该页面下的说明。
系统会在用户备份中生成备份文件校验任务，等待任务状态由校验中变更为完成即可。
重要
备份文件的校验时长取决于实例在备份时的状态。例如，备份期间原实例中若有太多写入操作，会导致实例大量生成redo日志、或实例中执行了大型的事务等情况下，备份文件校验时间会变长。
单击目标备份ID/备注右侧操作列下的恢复。
设置如下参数，单击下一步：实例配置。
