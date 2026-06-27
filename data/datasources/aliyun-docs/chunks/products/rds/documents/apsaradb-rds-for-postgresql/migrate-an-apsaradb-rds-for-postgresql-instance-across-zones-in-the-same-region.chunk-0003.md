## 影响
切换时实例可用性会受到短暂影响，请确保应用具有自动重连机制。
迁移可用区会造成虚拟IP（VIP）的变更，请尽量在您的应用程序中使用连接地址进行连接，不要使用IP地址。
迁移可用区期间如果发生主节点切换，会造成虚拟IP（VIP）的变更，请使用连接地址而非IP地址，并请及时清理客户端DNS缓存。对于JVM的应用，建议将TTL设置为不超过60秒，以确保VIP变更时能及时更新。
说明
JVM中设置TTL的方法请参见JDK官方文档：[Class InetAddress](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/net/InetAddress.html)。
可用区迁移后，需重启正在执行的[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts#concept-26592-zh)任务。
如果迁移的目标可用区资源不足，则可能导致迁移可用区失败。
RDS PostgreSQL已不再支持新购SSD云盘，如果您的实例存储类型为SSD云盘，则在迁移可用区时，会自动从SSD云盘升级为ESSD PL1云盘。更多信息，请参见[【通知】部分](standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[RDS](standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[实例不再提供](standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[SSD](standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[云盘售卖](standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)。
