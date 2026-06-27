topN ] [FILTER filter_string ] [MAX_DIST max_distance] | 在指定向量索引中，针对指定 Key 列表，进行向量（VECTOR）近邻查询。 |  |
| [TVS.MKNNSEARCH](tairvector.md) | TVS.MKNNSEARCH index_name topN vector_count vector [vector ...] [filter_string] [param_key param_value] | 在指定向量索引中，批量对多条向量（VECTOR）进行近邻查询。 |  |
| [TVS.MINDEXKNNSEARCH](tairvector.md) | TVS.MINDEXKNNSEARCH index_count index_name [index_name ...] topN vector [filter_string] [param_key param_value] | 在多个向量索引中，对指定的向量（VECTOR）进行近邻查询。 |  |
| [TVS.MINDEXKNNSEARCHFIELD](tairvector.md) | TVS.MINDEXKNNSEARCHFIELD index_count index_name [index_name ...] topN vector field_count field_name [field_name ...] [filter_string] [param_key param_value] | 在多个向量索引中，对指定的向量（VECTOR）进行近邻查询，支持返回标签属性。 |  |
| [TVS.MINDEXMKNNSEARCH](tairvector.md) | TVS.MINDEXMKNNSEARCH index_count index_name [index_name ...] topN vector_count vector [vector ...] [filter_string] [param_key param_value] | 在多个向量索引中，批量对多条向量（VECTOR）进行近邻查询。 |  |
| 通用 | [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairVector 数据。 |
