### ERR FLUSHDB is not allowed in migrating mode
可能原因：Tair云原生版集群架构实例在执行增加或减少数据节点时，禁止使用FLUSHDB或FLUSHALL命令。
解决方法：等待Tair云原生版集群架构实例执行增加或减少数据节点结束，更多信息请参见[调整集群分片数](../user-guide/adjust-the-number-of-cluster-shards.md)。
