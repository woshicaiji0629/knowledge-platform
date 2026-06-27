### 磁盘扩缩容问题
Q：实例已扩容磁盘，为何仍显示锁定？
A：磁盘满导致锁定时，扩容后需等待升配任务完成自动解锁。您可在实例基本信息页右上角单击按钮跳转至任务列表页面，查看扩容任务进度。
Q：存储扩容为何会闪断？
A：存储扩容需实例切换，闪断影响详见[实例切换的影响](untitled-document-1701914031929.md)。
Q：扩容磁盘，免费备份额度是否扩大？
A：是。详见[免费备份额度](billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md)。
Q：缩容磁盘时出现错误提示“操作失败，日志备份未开启，无法按时间点恢复。”如何解决？
A：当实例Binlog产生较快时，需要本地保留足够多的日志，才允许实例进行缩容。您可以先短暂[开启日志备份](enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)，若缩容完无需保留日志再[关闭日志备份](enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)即可。更多限制，请参见[限制](change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。
