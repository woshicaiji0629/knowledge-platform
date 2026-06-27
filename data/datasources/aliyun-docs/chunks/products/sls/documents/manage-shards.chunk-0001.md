### Shard范围
每个Shard均有范围，为MD5左闭右开区间[BeginKey,EndKey)。每个Shard范围不会相互覆盖，且属于整个MD5范围内[00000000000000000000000000000000,ffffffffffffffffffffffffffffffff）。在创建LogStore或MetricStore时指定Shard个数，日志服务将自动平均划分整个MD5范围。
BeginKey：指定Shard范围的起始值，Shard范围中包含该值。
EndKey：指定Shard范围的结束值，Shard范围中不包含该值。
例如LogStore A中包含4个Shard，各个Shard范围如下：
表 1.Shard范围

| Shard ID | 范围 |
| --- | --- |
| Shard0 | [00000000000000000000000000000000,40000000000000000000000000000000) |
| Shard1 | [40000000000000000000000000000000,80000000000000000000000000000000) |
| Shard2 | [80000000000000000000000000000000,c0000000000000000000000000000000) |
| Shard3 | [c0000000000000000000000000000000,ffffffffffffffffffffffffffffffff) |

在Shard读写数据过程中，读数据时必须指定Shard ID，写数据时可通过负载均衡模式或者指定Hash Key的模式。
负载均衡模式：每个数据包随机写入当前可用的Shard中。
如果写入流量大于单Shard的服务能力，建议采用负载均衡模式。
指定Hash Key模式：指定MD5的Key值，数据将被写入包含该Key值的Shard中。
例如[Shard](shard.md)[范围](shard.md)所示，当写入数据时指定MD5的Key值为5F时，则数据将被写入包含5F的Shard1上；当写入数据时指定MD5的Key值为8C时，则数据将被写入包含8C的Shard2上。
