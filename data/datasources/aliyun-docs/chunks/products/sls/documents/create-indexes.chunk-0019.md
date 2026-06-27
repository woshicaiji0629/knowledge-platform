### 字段索引
不同数据类型的字段的索引流量计算方式不同。
text类型：字段名和字段值都被计入索引流量中。
long类型和double类型：字段名不计入索引流量中，每个字段值所占的索引流量统一为8字节。
例如对status字段设置了索引（long类型），字段值为200，则字符串status不会被计入在索引流量中，200的索引流量统一为8字节。
JSON类型：字段名和字段值都被计入到索引流量中，包括未被创建索引的子节点。更多信息，请参见[如何计算](why-is-index-traffic-generated-for-json-subfields-that-are-not-indexed.md)[JSON](why-is-index-traffic-generated-for-json-subfields-that-are-not-indexed.md)[类型字段的索引流量](why-is-index-traffic-generated-for-json-subfields-that-are-not-indexed.md)。
如果未对子节点设置索引，则其索引流量按照text类型进行计算。
如果对子节点设置了索引，则其索引流量按照其子节点数据类型（text、long或double）进行计算。
