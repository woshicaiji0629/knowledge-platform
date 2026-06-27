| 应用类型 | 常用应用 | 选型原则 | 推荐实例规格族 |
| --- | --- | --- | --- |
| 负载均衡 | Nginx | 应用特点：需要支持高频率的新建连接操作。 CPU 计算能力：要求较高。 内存：要求不高。 | c8i、c7、c7nex、g5ne |
| RPC 产品 | SOFA Dubbo | 应用特点：网络链接密集型；进程运行时需要消耗较高的内存。 | g8a、g7nex、g8i、g7 |
| 缓存 | Redis Memcache Solo | CPU 计算能力：要求不高。 内存：要求较高。 | r8i、r8a、r7、r7a |
| 配置中心 | ZooKeeper | 在应用启动协商时会有大量 I/O 读写操作。 CPU 计算能力：要求不高。 内存：要求不高。 | c8a、c7、c8i、u1 |
| 消息队列 | Kafka RabbitMQ | 从消息完整性方面考虑，存储优先选用云盘。 CPU 计算能力：要求不高。 内存和 vCPU 配比通常为 1:1。 存储：要求不高。 | c8a、c7、c8i、u1 |
| 容器编排 | Kubernetes | 通过弹性裸金属服务器和容器的组合，可以最大限度地挖掘计算潜能。 | ebmc6e、ebmg6e、ebmc6、ebmg6、ebmc6a、ebmc7a、ebmg6a、ebmg7a 系列 |
| 大表存储 | HBase | 一般可以选择 d 系列。 如果业务存在超高 IOPS（Input/Output Operations Per Second）需求，可以选择 i 系列。 | d3c、d3s、i4 |
| 数据库 | MySQL NoSQL | 对于存储有弹性扩展的需求，可以选择 ECS 和 ESSD。 对于 I/O 敏感型业务的需求，优先选择 i 系列。 | g8a、g7、g8i、i4, |
| SQLServer | 由于 Windows 的 I/O 单通道特性，对 I/O 读写能力要求较高，优先选择 ESSD。 ECS 的逻辑和物理扇区设置为 4 K。 | g8a、g7、r7、r8i、g8i |  |
| 文本搜索 | Elasticsearch | 选用内存与 vCPU 配比较大的 ECS 规格。 日常需要将数据库数据导出成 ES 文件，对 I/O 读写有要求。 | i4、i4r、i3、i2 |
| 实时计算 | Flink Blink | 基于存储量可以选择 ECS 通用规格和云盘，也可以选择 d 系列。 | i4g、i4、d3c |
| 离线计算 | Hadoop HDFS CDH | 优先选择 d 系列。 | d3s、d3c |
| 视频转码 | 点播 直播 | CPU 计算能力：要求高 内存：要求不高 IO：要求不高 | c8y 、hfc8i |
| 大
