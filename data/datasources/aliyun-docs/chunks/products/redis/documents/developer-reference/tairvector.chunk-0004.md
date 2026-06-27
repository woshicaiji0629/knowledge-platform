| 类型 | 命令 | 语法 | 说明 |
| --- | --- | --- | --- |
| 索引元数据操作 | [TVS.CREATEINDEX](tairvector.md) | TVS.CREATEINDEX index_name dims algorithm distance_method [ algo_param_key alog_param_value ] ... | 创建一个向量索引空间，同时指定构建索引和查询的具体算法，以及距离函数。该对象仅能通过 TVS.DELINDEX 命令删除。 |
| [TVS.GETINDEX](tairvector.md) | TVS.GETINDEX index_name | 查询指定的向量索引，获取该向量索引的元数据信息。 |  |
| [TVS.DELINDEX](tairvector.md) | TVS.DELINDEX index_name | 删除指定的向量索引及该索引内的所有数据。 |  |
| [TVS.SCANINDEX](tairvector.md) | TVS.SCANINDEX cursor [MATCH pattern ] [COUNT count ] | 扫描 Tair 实例中所有符合条件的向量索引。 |  |
| 向量数据操作 | [TVS.HSET](tairvector.md) | TVS.HSET index_name key attribute_key attribute_value [ attribute_key attribute_value ] ... | 往向量索引中插入数据记录（ key ），若该记录已存在则更新并覆盖原记录。 |
| [TVS.HGETALL](tairvector.md) | TVS.HGETALL index_name key | 查询指定向量索引中的 key 对应的所有数据记录。 |  |
| [TVS.HMGET](tairvector.md) | TVS.HMGET index_name key attribute_key [ attribute_key ...] | 查询指定向量索引的 key 中对应的 attribute_key 所对应的数值。 |  |
| [TVS.DEL](tairvector.md) | TVS.DEL index_name key [ key ...] | 在指定向量索引中，删除指定数据记录（ key ）。 |  |
| [TVS.HDEL](tairvector.md) | TVS.HDEL index_name key attribute_key [ attribute_key ...] | 在向量索引的数据记录（ key ）中，删除指定的 attribute_key 与其数值。 |  |
| [T
