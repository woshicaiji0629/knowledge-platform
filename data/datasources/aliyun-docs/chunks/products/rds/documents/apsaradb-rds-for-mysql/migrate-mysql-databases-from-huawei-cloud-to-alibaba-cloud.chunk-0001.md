## 迁移限制
结构迁移不支持event的迁移。
对于MySQL的浮点型float和double，DTS通过round(column,precision)来读取该列的值，若列类型没有明确定义其精度，对于float，精度为38位，对于double类型，精度为308，请先确认DTS的迁移精度是否符合业务预期。
如果使用了对象名映射功能后，依赖这个对象的其他对象可能迁移失败。
增量迁移限制如下：
源端的MySQL实例需要按照要求开启binlog。
源库的binlog_format要为row。
源MySQL如果为5.6及以上版本时，它的binlog_row_image必须为full。
增量迁移过程中如果源MySQL实例出现因实例跨机迁移或跨机重建等导致的binlog文件ID乱序，可能导致增量迁移数据丢失。
说明
华为云云数据库RDS MySQL实例的参数修改，请参见[华为云云数据库](https://support.huaweicloud.com/rds/index.html)[RDS](https://support.huaweicloud.com/rds/index.html)[官方文档](https://support.huaweicloud.com/rds/index.html)。
