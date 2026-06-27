## TairTS简介
相比[RedisTimeSeries](https://redis.com/modules/redis-timeseries/)，TairTS提供了更丰富的功能：
通过Pkey（额外一层Hash结构）结构，轻松实现Pkey级别（多时间线）聚合查询。
例如您可以在foo（Pkey）中创建以各项指标名称与设备ID命名的Skey，例如temperature:1、pressure:1、distance:1等，可通过TairTS自带的[EXTS.S.MRANGE](../tairts-commands.md)命令轻松获取设备ID为1的自定义监控信息，而使用RedisTimeSeries则需要在业务逻辑代码中嵌入大量数据聚合运算才能实现该功能。
图 1.TairTS与RedisTS数据结构对比图
TairTS数据结构解析：
Pkey（一组时间线）：TairTS数据结构，可包含多个Skey。
Skey（一条时间线）：包含多个固定容量的Chunk，每个Skey可设置不同的Label（标签），可通过Label在海量数据中快速过滤目标Skey。
Chunk（数据块）：可存储多个Datapoint。
Chunk的容量支持自定义，若不开启压缩，最多存储256个Datapoint；若开启压缩，则能存储超过256个。
Chunk为最小的过期单元，即单个Chunk中所有Datapoint都过期后才会删除该Chunk。
Datapoint（时序数据）：包含一个时间戳和一个value数据（double类型）。
支持降采样、属性过滤、分批查询、多种数值函数等条件下的聚合操作，将批量查询与聚合计算集成到单条命令中，减少网络交互，实现毫秒级响应。
支持对历史时序数据的更新或累加。
支持时间线级别的TTL设定，保证每条时间线都可以按时间窗口自动滚动。
采用高效的Gorilla压缩算法与特定存储，极大降低存储成本。
典型场景
监控数据的存储与计算
基于时间窗口的数据分析
IoT（物联网）数据分析与处理
热点消息缓存
APM秒级监控
限流风控
