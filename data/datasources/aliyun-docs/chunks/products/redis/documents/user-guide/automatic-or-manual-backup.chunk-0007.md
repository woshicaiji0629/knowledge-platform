## 常见问题
Q：如何删除备份数据？
A：对于云原生实例，可以直接单击目标手动备份数据右侧的删除按钮进行删除。但所有自动备份数据均不支持删除，自动备份数据在到期后将自动删除。
Q：修改备份策略会影响实例运行吗？
A：不会。
Q：实例是否支持执行SAVE或BGSAVE命令备份数据？
A：不支持，您可以在控制台单击手动创建备份或调用[CreateBackup](../developer-reference/api-r-kvstore-2015-01-01-createbackup-redis.md)接口，手动备份数据。
Q：每天多次备份需要怎么做？
A：自动备份策略最多支持每天一次。如需进行更高频率的备份，您可以编写代码，定时调用[CreateBackup](../developer-reference/api-r-kvstore-2015-01-01-createbackup-redis.md)接口，模拟手动创建备份，更多信息请参见[CreateBackup](https://next.api.aliyun.com/api/R-kvstore/2015-01-01/CreateBackup)集成示例。备份后的数据也在备份列表中。
说明
您也可以考虑使用Tair（企业版）实例提供的数据闪回功能。开启数据闪回功能后，Tair（企业版）实例可实现7x24小时数据备份，也支持恢复至7天内的任意时间时（PITR，point-in-time recovery），更多信息请参见[数据闪回](use-data-flashback-to-restore-data-by-point-in-time.md)。
Q：实例到期或被释放后，备份的数据还会保留吗？
A：云原生实例备份数据支持保留，您可以在[备份管理](https://kvstore.console.aliyun.com/Redis/backupManage/cn-beijing)中进行查询、恢复。但经典版实例的备份集会被删除，如需长期保存，请提前[下载备份集](download-a-backup-file.md)。
