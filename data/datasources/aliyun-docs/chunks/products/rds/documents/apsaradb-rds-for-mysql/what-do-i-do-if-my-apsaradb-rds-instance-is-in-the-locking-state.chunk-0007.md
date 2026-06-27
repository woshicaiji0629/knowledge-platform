系统文件（标准监控中对应undolog_size）
产生原因：当存在对InnoDB表长时间不结束的查询语句，而且在查询过程中表有大量的数据变化时，系统会生成大量的undo信息，占用大量存储空间，导致存储空间耗尽。
解决方法：请参见[系统文件堆积导致空间不足](troubleshoot-storage-issues-on-an-apsaradb-rds-for-mysql-instance.md)。
