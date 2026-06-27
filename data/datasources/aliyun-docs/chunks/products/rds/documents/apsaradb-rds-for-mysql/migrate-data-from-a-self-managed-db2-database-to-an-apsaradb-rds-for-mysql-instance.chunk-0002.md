## 注意事项
不支持DDL操作的同步。
如果待迁移数据库名称不符合阿里云RDS的定义规范，您需要在配置迁移任务之前在阿里云RDS MySQL中创建数据库。
说明
关于阿里云RDS的定义规范和创建数据库的操作方法，请参见[创建数据库](create-a-database-for-an-apsaradb-rds-for-mysql-instance.md)。
DTS在执行全量数据迁移时将占用源库和目标库一定的读写资源，可能会导致数据库的负载上升，在数据库性能较差、规格较低或业务量较大的情况下（例如源库有大量慢SQL、存在无主键表或目标库存在死锁等），可能会加重数据库压力，甚至导致数据库服务不可用。因此您需要在执行数据迁移前评估源库和目标库的性能，同时建议您在业务低峰期执行数据迁移（例如源库和目标库的CPU负载在30%以下）。
对于迁移失败的任务，DTS会触发自动恢复。在将业务切换至目标实例前，请务必先结束或释放该任务，避免该任务被自动恢复后，源端数据覆盖目标实例的数据。
由于DTS基于Db2的CDC复制技术，将Db2数据库的增量更新数据同步到目标库中，但是CDC复制技术自身具有限制，请参见[CDC](https://www.ibm.com/support/knowledgecenter/SSTRGZ_11.4.0/com.ibm.swg.im.iis.db.repl.sqlrepl.doc/topics/iiyrssubdatarestrict.html)[复制技术所支持数据类型的限制](https://www.ibm.com/support/knowledgecenter/SSTRGZ_11.4.0/com.ibm.swg.im.iis.db.repl.sqlrepl.doc/topics/iiyrssubdatarestrict.html)。
