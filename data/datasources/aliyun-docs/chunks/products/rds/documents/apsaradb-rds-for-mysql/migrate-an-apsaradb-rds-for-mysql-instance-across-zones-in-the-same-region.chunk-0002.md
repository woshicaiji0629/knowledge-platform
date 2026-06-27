## 注意事项
仅支持在同地域下的可用区之间进行迁移。如需跨地域迁移可用区，可以在目标地域和可用区[购买新实例](create-an-apsaradb-rds-for-mysql-instance-1.md)，使用DTS[将原实例数据迁移至新实例](migrate-data-between-apsaradb-rds-for-mysql-instances.md)，检查无误后[释放原实例](release-or-unsubscribe-from-an-instance.md)。
主节点切换：迁移可用区期间可能会导致主节点切换，造成主节点连接地址、代理连接地址短时间不可用，请确保应用具有自动重连机制。若无自动重连机制，请手动进行应用与数据库的重连。具体影响请参见[实例切换的影响](untitled-document-1701914031929.md)。主节点切换的场景如下：
当主节点目标可用区与主节点当前可用区不一致时，会发生主节点切换。
当主节点目标可用区与当前主实例网络资源所在可用区不一致时，会发生主节点切换。
虚拟IP（VIP）变更：迁移可用区期间如果发生主节点切换，会造成虚拟IP（VIP）的变更，连接地址不会发生变化，请尽量在您的应用程序中使用连接地址进行连接，请勿使用IP地址。
如果您的RDS MySQL实例挂载在PolarDB-X实例之下，VIP的变更会影响到RDS实例与PolarDB-X实例之间的连通性，请及时手动修复。更多信息，请参见[修复分库连接](https://help.aliyun.com/zh/polardb/polardb-for-xscale/user-guide/fix-database-shard-connections#multiTask294)。
请及时清理客户端DNS缓存。客户端采用JVM的应用，建议将JVM配置中的TTL设置为不超过60秒，可确保在连接地址的VIP地址发生变更时，应用程序可以通过重新查询DNS来接收和使用资源的新VIP地址。
说明
JVM中设置TTL的方法请参见JDK官方文档：[Class InetAddress](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/net/InetAddress.html)。
DTS任务中断：如果有正在执行的[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts#concept-26592-zh)任务，可用区迁移后，需要重启相应的DTS任务。
重新创建表文件：迁移可用区会重新创建表文件，从而导致表文件的创建时间发生变化，进而引起INFORMATION_SCHEMA中表的CREATE_TIME字段发生变化。
如果迁移的
