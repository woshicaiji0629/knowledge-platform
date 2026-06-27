## 迁移限制
结构迁移不支持event的迁移。
对于MySQL的浮点型float和double，DTS通过round(column,precision)来读取该列的值，若列类型没有明确定义其精度，对于float类型，精度为38位，对于double类型，精度为308，请先确认DTS的迁移精度是否符合业务预期。
如果使用了对象名映射功能后，依赖这个对象的其他对象可能迁移失败。
当选择增量迁移时，源端的MySQL实例需要按照要求开启binlog。
当选择增量迁移时，源库的binlog_format要为row。
当选择增量迁移且源MySQL如果为5.6及以上版本时，它的binlog_row_image必须为full。
当选择增量迁移时，增量迁移过程中如果源MySQL实例出现因实例跨机迁移或跨机重建等导致的binlog文件ID乱序，可能导致增量迁移数据丢失。
说明
腾讯云云数据库MySQL参数的修改，请参见[腾讯云云数据库](https://cloud.tencent.com/document/product/236)[MySQL](https://cloud.tencent.com/document/product/236)[官网文档](https://cloud.tencent.com/document/product/236)。
