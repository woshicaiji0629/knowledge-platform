# 为什么只创建Project和LogStore会产生费用？
当您在创建LogStore时，日志服务默认预留Shard资源，因此可能产生活跃Shard租用费用。活跃Shard租用费用的详细说明请参见[为什么会产生活跃](why-am-i-charged-for-active-shards.md)[Shard](why-am-i-charged-for-active-shards.md)[租用费用？](why-am-i-charged-for-active-shards.md)。
当您确保不再使用此LogStore时，请及时删除，避免产生额外费用。
警告
LogStore一旦被删除，其存储的日志数据将被永久删除，不可恢复，请谨慎操作。
该文章对您有帮助吗？
反馈
