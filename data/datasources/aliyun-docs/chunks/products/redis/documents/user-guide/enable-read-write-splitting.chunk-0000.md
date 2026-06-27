# 开启读写分离
云数据库 Tair（兼容 Redis）支持开关读写分离功能及自定义只读节点数量。[读写分离功能](../product-overview/read-or-write-splitting-instances-1.md)采用星型复制架构，所有只读节点均从主节点同步数据，数据同步延迟低。
