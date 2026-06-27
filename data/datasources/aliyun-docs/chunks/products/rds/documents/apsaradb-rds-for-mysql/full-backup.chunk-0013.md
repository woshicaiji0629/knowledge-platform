ition.md) 或 [集群系列](rds-cluster-edition.md) | 备份在备实例执行，不占用主实例 CPU，不影响主实例性能。 说明 少数情况下，备实例不可用时，备份会在主实例执行。 |
| [基础系列](rds-basic-edition.md) | 由于是单节点架构，备份时会影响实例性能。 |

Q：数据备份或日志备份是否可以关闭？
A：数据备份不可以关闭，但可以减少备份频率（一周至少2次），保留天数最少7天；日志备份可以关闭，在备份策略页面可以关闭日志备份开关。具体请参考[删除或减少备份](delete-the-backup-files-or-reduce-the-size-of-backup-files-of-an-apsaradb-rds-for-mysql-instance.md)教程减少RDS MySQL备份。
Q：按量付费实例进入欠费状态后，是否仍会进行自动备份？
A：在延期免停额度内（即欠费7天内），自动备份功能将继续执行。超过7天的延期额度后，阿里云将暂停该实例的服务（即停服），并停止计费。同时，自动备份功能将立即终止。更多信息请参见[欠费说明](overdue-payments.md)。
Q：为什么有时候备份任务会失败？
A：备份过程中执行耗时长的DDL或更新语句，会导致锁表，进而导致备份失败。
Q：为什么数据只有几GB，快照备份有几十GB？
A：单次备份文件的大小可能比数据量大，也可能比数据量小。云盘实例采用快照备份，单次快照备份文件的大小可能远大于数据的大小。云盘实例备份免费额度为实例存储容量的200%，高性能本地盘实例备份免费额度为实例存储容量的50%。
说明
计算单次快照备份文件的大小时，会计算所有非空块的大小。如果写入时比较分散（例如3MB的数据可能占用2个、3个甚至4个块），会导致较多非空块，因此快照备份较大。
因此控制台备份恢复页面显示的所有备份集的备份文件大小总和，可能会与显示的备份使用量不一致。
Q：数据库的备份文件占用实例磁盘空间吗？
A：数据备份和日志备份存放于阿里云提供的备份空间，不占用实例的存储空间。
说明
备份空间不对外开放访问。如需下载备份，请参见[下载备份](download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance-download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance.md)。
备份空间提供免费额度，超出额度时需付费，具体请参见[备份费用](billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md)。
