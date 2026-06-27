## 迁移类型

| 迁移类型 | 说明 |
| --- | --- |
| 结构迁移 | DTS 将迁移对象的结构定义迁移到目标库。 目前 DTS 仅支持结构迁移表和索引，且存在以下限制： 表：不支持嵌套表；对于聚簇表和索引组织表，会在目标端转换成普通的表。 索引：不支持 Function-Based Index、Domain Index、Bitmap Index 和 ReverseIndex。 说明 DTS 暂不支持结构迁移视图、同义词、存储过程、存储函数、包、自定义类型等。 警告 此场景属于异构数据库间的数据迁移，DTS 在执行结构迁移时数据类型无法完全对应，请谨慎评估数据类型的映射关系对业务的影响，详情请参见 [异构数据库间的数据类型映射关系](https://help.aliyun.com/zh/dts/user-guide/data-type-mappings-between-heterogeneous-databases#concept-1813831) 。 |
| 全量数据迁移 | DTS 会将自建 Oracle 数据库迁移对象的存量数据，全部迁移至目标库。 |
| 增量数据迁移 | DTS 在全量数据迁移的基础上轮询并捕获自建 Oracle 数据库产生的 redo log，将自建 Oracle 数据库的增量更新数据迁移到目标库。 通过增量数据迁移可以实现在自建应用不停服的情况下，平滑地完成数据迁移。 |
