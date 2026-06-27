RE](tairvector.md) | TVS.HEXPIRE index_name key timestamp | 在指定向量索引中，为指定数据记录（ key ）设置相对过期时间，精确到秒。 |  |
| [TVS.HPTTL](tairvector.md) | TVS.HPTTL index_name key | 在指定向量索引中，查看指定数据记录（ key ）的剩余过期时间，精确到毫秒。 |  |
| [TVS.HTTL](tairvector.md) | TVS.HTTL index_name key | 在指定向量索引中，查看指定数据记录（ key ）的剩余过期时间，精确到秒。 |  |
| [TVS.HPEXPIRETIME](tairvector.md) | TVS.HPEXPIRETIME index_name key | 在指定向量索引中，查看指定数据记录（ key ）的绝对过期时间，精确到毫秒。 |  |
| [TVS.HEXPIRETIME](tairvector.md) | TVS.HEXPIRETIME index_name key | 在指定向量索引中，查看指定数据记录（ key ）的绝对过期时间，精确到秒。 |  |
| 向量近邻查询 | [TVS.KNNSEARCH](tairvector.md) | TVS.KNNSEARCH index_name topN vector [filter_string] [param_key param_value] | 在指定向量索引中，对指定的向量（VECTOR）进行近邻查询，最多可返回 topN 条。 |
| [TVS.KNNSEARCHFIELD](tairvector.md) | TVS.KNNSEARCHFIELD index_name topN vector field_count field_name [field_name ...] [filter_string] [param_key param_value] | 在指定向量索引中，对指定的向量（VECTOR）进行近邻查询，检索逻辑与 TVS.KNNSEARCH 相同，额外支持返回标签属性。 |  |
| [TVS.GETDISTANCE](tairvector.md) | TVS.GETDISTANCE index_name vector key_count key [ key , ...] [TOPN topN ] [FILTER filter_string ] [MAX_DIST max_distance] | 在指定向量索引中，针对指定 Key 列表，进行向量（VECTOR）近邻查询。 |  |
| [TVS.MKNNSEARCH](tairvector.md) | TVS.MKNNSEARCH index_na
