录（ key ）。 |  |
| [TVS.HDEL](tairvector.md) | TVS.HDEL index_name key attribute_key [ attribute_key ...] | 在向量索引的数据记录（ key ）中，删除指定的 attribute_key 与其数值。 |  |
| [TVS.SCAN](tairvector.md) | TVS.SCAN index_name cursor [MATCH pattern ] [COUNT count ] [FILTER filter_string] [VECTOR vector] [MAX_DIST max_distance] | 在指定向量索引中，扫描符合条件的数据记录（ key ）。 |  |
| [TVS.HINCRBY](tairvector.md) | TVS.HINCRBY index_name key attribute_key num | 在指定向量索引中，将指定数据记录（ key ）的 attribute_key 的值增加 num，num 为一个整数。 |  |
| [TVS.HINCRBYFLOAT](tairvector.md) | TVS.HINCRBYFLOAT index_name key attribute_key num | 在指定向量索引中，将指定数据记录（ key ）的 attribute_key 的值增加 num，num 为一个浮点数。 |  |
| [TVS.HPEXPIREAT](tairvector.md) | TVS.HPEXPIREAT index_name key milliseconds-timestamp | 在指定向量索引中，为指定数据记录（ key ）设置绝对过期时间，精确到毫秒。 |  |
| [TVS.HPEXPIRE](tairvector.md) | TVS.HPEXPIRE index_name key milliseconds-timestamp | 在指定向量索引中，为指定数据记录（ key ）设置相对过期时间，精确到毫秒。 |  |
| [TVS.HEXPIREAT](tairvector.md) | TVS.HEXPIREAT index_name key timestamp | 在指定向量索引中，为指定数据记录（ key ）设置绝对过期时间，精确到秒。 |  |
| [TVS.HEXPIRE](tairvector.md) | TVS.HEXPIRE index_name key timestamp | 在指定向量索引中，为指定数据记录（ key ）设置相对过期时间，精确到秒。 |  |
| [TVS.HPTTL](tairvector.md) | TVS.HPTTL index_name key |
