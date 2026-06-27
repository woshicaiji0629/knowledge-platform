## 同城容灾（多可用区）方案
云数据库 Tair（兼容 Redis）提供多可用区的同城容灾架构。如果业务为单一地域部署，且对容灾要求较高，可在创建实例时，选择支持同城容灾的多可用区。操作方法，请参见[创建实例](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md)。
图 5.创建同城容灾实例
完成创建后，备机房将创建与主机房相同规格的Replica实例，主备机房的实例数据通过专门的复制通道同步。
当主机房出现电力或网络问题时，Replica实例将升级为Master实例，系统调用Config Server接口为Proxy更新路由信息。同时，云数据库 Tair（兼容 Redis）优化了Redis的同步机制，在同步位点上借鉴MySQL的GTID，实现了全局Opid，查找Opid的操作通过后台线程无锁进行，发送AOF binlog是异步同步的过程（可限流），保障了Redis服务的性能。
图 6.同城容灾实例的数据同步过程
