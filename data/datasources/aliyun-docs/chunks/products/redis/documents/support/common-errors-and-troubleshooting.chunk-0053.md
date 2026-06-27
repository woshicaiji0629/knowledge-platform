### Connection to xxx not allowed. This Partition is not known in the cluster view.
可能原因：Lettuce客户端在默认情况下，配置为refreshOption = null , validateClusterNodeMembership = true，表示开启validateClusterNodeMembership检测。在Tair实例地址发生路由变化后，由于没有开启refreshOption，即不会更新路由表，此时validateClusterNodeMembership检测就会返回该报错。
解决方法：配置refreshOption选项，并且设置validateClusterNodeMembership为false，更多信息请参见[Lettuce](../user-guide/use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)。
