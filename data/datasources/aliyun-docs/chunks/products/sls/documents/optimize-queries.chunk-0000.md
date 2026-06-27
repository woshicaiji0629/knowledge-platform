## 增加Shard数量或开启SQL独享版
增加Shard可以提升读写能力，但只对新写入的数据生效。Shard表示计算资源，Shard越多，计算越快，您需要保证平均每个Shard扫描的数据不多于5000万条。您可以通过分裂Shard，增加Shard数量。具体操作，请参见[分裂](manage-shards.md)[Shard](manage-shards.md)。Shard的计费信息，请参见[活跃](why-am-i-charged-for-active-shards.md)[Shard](why-am-i-charged-for-active-shards.md)[租用费用](why-am-i-charged-for-active-shards.md)。
[SQL](dedicated-sql.md)[独享版](dedicated-sql.md)支持更多的分析操作并发数、更多的扫描数据量。
