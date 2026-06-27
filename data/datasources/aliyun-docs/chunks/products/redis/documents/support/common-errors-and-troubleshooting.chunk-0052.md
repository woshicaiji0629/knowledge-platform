### No way to dispatch this command to Redis Cluster because keys have different slots
可能原因：JedisCluster操作的Key不在同一个Slot（槽）中。
解决方法：通过Hash tags对Key进行改造。
说明
您也可以使用Proxy（代理）模式屏蔽集群的限制。
