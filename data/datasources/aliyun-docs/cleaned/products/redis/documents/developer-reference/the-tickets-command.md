# 时序数据存储聚合计算-TairTS-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/developer-reference/the-tickets-command

# TS
TairTS是基于Redis Module开发的时序数据结构，提供低时延、高并发的内存读写访问，及快速地过滤、聚合查询功能，集存储与计算为一体，在简化了处理时序数据流程的同时，大幅度提高了性能。
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
## 最佳实践
[基于](../use-cases/realization-of-second-level-monitoring-based-on-tairy.md)[TairTS](../use-cases/realization-of-second-level-monitoring-based-on-tairy.md)[实现秒级监控](../use-cases/realization-of-second-level-monitoring-based-on-tairy.md)
## 前提条件
实例为Tair[内存型](../product-overview/dram-based-instances.md)。
当实例为内存型（兼容Redis 5.0）时，小版本需要为1.7.20及以上。
说明
最新小版本将提供更丰富的功能与稳定的服务，建议将实例的小版本升级到最新，具体操作请参见[升级小版本](../user-guide/update-the-minor-version.md)。如果您的实例为集群实例或读写分离架构，请将代理节点的小版本也升级到最新，否则可能出现命令无法识别的情况。
## 注意事项
操作对象为Tair实例中的TairTS数据。
TairTS的优势为实时、高并发的写入与查询性能，缺陷为存储容量有限，请合理设置TTL，及时淘汰过期数据。
重要
Breaking Change公告：
2024年07月22日发布Tair内存型（兼容Redis 6.0）24.7.0.0版本，该版本中新增了ts-auto-del-empty-skey-enable参数，默认为yes，表示当Skey中的所有数据点都过期时，会自动删除Skey。但在Tair内存型（兼容Redis 6.0）24.7.0.0之前的版本中，默认不会删除数据点已过期的Skey。
在Tair内存型（兼容Redis 6.0）实例使用TairTS前，建议将实例升级至24.7.0.0及以上版本，并确认、手动调整ts-auto-del-empty-skey-enable参数的策略，避免因默认行为的改变对业务产生影响。
## 命令列表
表 1.TairTS命令
| 类型 | 命令 | 语法 | 说明 |
| --- | --- | --- | --- |
| 基础写操作 | [EXTS.P.CREATE](the-tickets-command.md) | EXTS.P.CREATE Pkey | 创建一个新的 Pkey（TairTS 数据结构），若 Pkey 已存在则创建失败。 |
| [EXTS.S.CREATE](the-tickets-command.md) | EXTS.S.CREATE Pkey Skey [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 label2 val2 ...] | 在指定的 Pkey 中创建一个 Skey，若 Pkey 不存在则会自动创建，若 Skey 已经存在则创建失败。 说明 您可以在创建 Skey 时设置其相关属性，例如过期时间、是否开启压缩等。 |  |
| [EXTS.S.ALTER](the-tickets-command.md) | EXTS.S.ALTER Pkey Skey [DATA_ET time] | 修改指定 Skey 的元数据信息，当前仅支持修改过期时间（DATA_ET）。 |  |
| [EXTS.S.ADD](the-tickets-command.md) | EXTS.S.ADD Pkey Skey ts value [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] | 向 Skey 中插入一条 Datapoint 数据。若 Pkey 或 Skey 不存在则会自动创建，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |  |
| [EXTS.S.MADD](the-tickets-command.md) | EXTS.S.MADD Pkey keynumber Skey ts value [Skey ts value ...] [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] | 在指定 Pkey 的多个 Skey 中分别插入一条 Datapoint 数据。若 Pkey 或 Skey 不存在则会自动创建，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |  |
| [EXTS.S.INCRBY](the-tickets-command.md) | EXTS.S.INCRBY Pkey Skey ts value [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] | 向 Skey 中插入一条 Datapoint 数据，该命令中的 value 将与 Skey 中最近 Datapoint 的 value 值相加实现递增，也可以指定该命令中的 value 为负数实现递减。若 Pkey 或 Skey 不存在则会自动创建，默认初始值为 0，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |  |
| [EXTS.S.MINCRBY](the-tickets-command.md) | EXTS.S.MINCRBY Pkey keynumber Skey ts value [Skey ts value ...] [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] | 在指定 Pkey 的多个 Skey 分别插入一条 Datapoint 数据，该命令中的 value 将分别与各个 Skey 中最近 Datapoint 的 value 值相加实现递增，也可以指定该命令中的 value 为负数实现相减。若 Pkey 或 Skey 不存在则会自动创建，默认初始值为 0，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |  |
| [EXTS.S.DEL](the-tickets-command.md) | EXTS.S.DEL Pkey Skey | 删除指定 Pkey 中的单个 Skey，并删除目标 Skey 中所有的 Datapoint 数据。 |  |
| 基础读操作 | [EXTS.S.GET](the-tickets-command.md) | EXTS.S.GET Pkey Skey | 查询指定 Skey 中最新的 Datapoint 数据。 |
| [EXTS.S.INFO](the-tickets-command.md) | EXTS.S.INFO Pkey Skey | 查询指定 Skey 的元数据信息，包含 Datapoint 数量、最近 Datapoint 的时间戳与 value 值、Skey 的标签信息等信息。 |  |
| [EXTS.S.QUERYINDEX](the-tickets-command.md) | EXTS.S.QUERYINDEX Pkey filter1 [filter2 ...] | 在 Pkey 中自定义过滤条件（filter），查询目标 Skey。 |  |
| 聚合操作 | [EXTS.S.RANGE](the-tickets-command.md) | EXTS.S.RANGE Pkey Skey fromTs toTs [MAXCOUNT count] [AGGREGATION aggregationType timeBucket] | 在 Skey 中查询指定时间内（包含指定时间点）的 Datapoint 数据。 |
| [EXTS.S.MRANGE](the-tickets-command.md) | EXTS.S.MRANGE Pkey fromTs toTs [MAXCOUNT count] [AGGREGATION aggregationType timeBucket] [WITHLABELS] FILTER filter1 [filter2 ...] | 在 Skey 中自定义过滤条件（filter）与查询时间点（包含指定时间点），查询目标 Datapoint 数据。 |  |
| [EXTS.P.RANGE](the-tickets-command.md) | EXTS.P.RANGE Pkey fromTs toTs pkeyAggregationType pkeyTimeBucket [MAXCOUNT count] [AGGREGATION aggregationType timeBucket] FILTER filter1 [filter2 ...] | 在 Pkey 层级对符合过滤条件（filter）的 Datapoint 数据进行聚合，若您指定了 Skey 层级的聚合，则会优先进行 Skey 层级聚合（效果与 EXTS.S.MRANGE 命令相同），再从 Pkey 层级对第一次聚合结果进行二次聚合。 |  |
| 并发写操作 | [EXTS.S.RAW_MODIFY](the-tickets-command.md) | EXTS.S.RAW_MODIFY Pkey Skey ts value [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] | 修改指定 Skey 中 Datapoint 数据的 value 值。若 Pkey 或 Skey 不存在则会自动创建，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |
| [EXTS.S.RAW_MMODIFY](the-tickets-command.md) | EXTS.S.RAW_MMODIFY Pkey keynumber Skey ts value [Skey ts value ...] [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] | 批量修改多个指定 Skey 中 Datapoint 数据的 value 值。若 Pkey 或 Skey 不存在则会自动创建，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |  |
| [EXTS.S.RAW_INCRBY](the-tickets-command.md) | EXTS.S.RAW_INCRBY Pkey Skey ts value [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] | 该命令中的 value 值会与指定 Skey 中 Datapoint 数据的 value 相加实现递增，也可以指定该命令中的 value 为负数实现递减。若 Pkey 或 Skey 不存在则会自动创建，默认初始值为 0，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |  |
| [EXTS.S.RAW_MINCRBY](the-tickets-command.md) | EXTS.S.RAW_MINCRBY Pkey keynumber Skey ts value [Skey ts value ...] [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] | 批量修改多个指定 Skey 中 Datapoint 数据的 value 值，该命令中的 value 值会与指定 Skey 中 Datapoint 数据的 value 相加实现递增，也可以指定该命令中的 value 为负数实现递减。若 Pkey 或 Skey 不存在则会自动创建，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |  |
| 通用 | [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairTS 数据。 |
说明
本文的命令语法定义如下：
大写关键字：命令关键字。
斜体：变量。
[options]：可选参数，不在括号中的参数为必选。
A|B：该组参数互斥，请进行二选一或多选一。
...：前面的内容可重复。
## EXTS.P.CREATE
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.P.CREATE Pkey |
| 时间复杂度 | O(1) |
| 命令描述 | 创建一个新的 Pkey（TairTS 数据结构），若 Pkey 已存在则创建失败。 |
| 选项 | Pkey ：Key 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.P.CREATE foo 返回示例： OK |
## EXTS.S.CREATE
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.CREATE Pkey Skey [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 label2 val2 ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定的 Pkey 中创建一个 Skey，若 Pkey 不存在则会自动创建，若 Skey 已经存在则创建失败。 说明 您可以在创建 Skey 时设置其相关属性，例如过期时间、是否开启压缩等。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 DATA_ET time ：Datapoint 数据的相对过期时间，单位为毫秒，默认为不填（表示不会过期）。 CHUNK_SIZE ：单个 Chunk 的大小，用于存储 Datapoint。单位为 16 byte（字节），默认值为 256，意味着系统会直接给该 Chunk 分配 4 KB 内存（16 byte * 256）用于存储 Datapoint 数据，当该 Chunk 写满时系统会再创建一个新的 Chunk，以此类推。 CHUNK_SIZE 取值范围为[1,256]。 说明 以 CHUNK_SIZE 为 256 为例，若 Skey 不开启压缩，单个 Chunk 能存储 256 个 Datapoint 数据；若开启压缩，则能存储超过 256 个，但具体能存多少取决于不同数据的压缩效果。 为节省内存空间以及平衡读写效率，关于设置 CHUNK_SIZE 的建议如下： 若 Skey 的平均数据点大于 5,000 个，设置 CHUNK_SIZE 为 256（默认值）。大 Chunk 可以减少整体的 Chunk 数量，减少元数据的占用。 若 Skey 的平均数据点小于 5,000 个，设置 CHUNK_SIZE 为平均数据点个数 / 20。例如某 Skey 的平均数据点为 1,000，可以设置 CHUNK_SIZE 为 50。在小范围查询时仅需解压缩更少数据，可以获得更好的性能。但如果在此情况下写入大量数据，会因创建大量 Chunk 而导致性能变慢。 UNCOMPRESSED ：设置 Skey 不开启压缩，默认为不填（即开启压缩）。 LABELS ：Skey 的属性，输入一组或多组对应的标签名、标签值，例如 LABELS sensor_id 1 。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.CREATE foo temperature DATA_ET 10000000 LABELS sensor_id 1 返回示例： OK |
## EXTS.S.ALTER
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.ALTER Pkey Skey [DATA_ET time] |
| 时间复杂度 | O(1) |
| 命令描述 | 修改指定 Skey 的元数据信息，当前仅支持修改过期时间（DATA_ET）。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 DATA_ET time ：Datapoint 数据的相对过期时间，单位为毫秒，默认为不填（表示不会过期）。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.ALTER foo temperature DATA_ET 100000 返回示例： OK |
## EXTS.S.ADD
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.ADD Pkey Skey ts value [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 向 Skey 中插入一条 Datapoint 数据。若 Pkey 或 Skey 不存在则会自动创建，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 ts ：Datapoint 数据的 Unix 时间戳，单位为毫秒，支持用 * 表示系统当前的时间戳。 value ：Datapoint 数据的值，数据类型为双精度浮点（double）型。 DATA_ET time ：Datapoint 数据的相对过期时间，单位为毫秒，默认为不填（表示不会过期）。 CHUNK_SIZE ：单个 Chunk 的大小，单位为 16 byte（字节），默认值为 256，取值范围为[1,256]。更多信息请参见 [EXTS.S.CREATE](the-tickets-command.md) 中的说明。 UNCOMPRESSED ：设置 Skey 不开启压缩，默认为不填（即开启压缩）。 LABELS ：Skey 的属性，输入一组或多组对应的标签名、标签值，例如 LABELS sensor_id 1 。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.ADD foo temperature * 30.5 DATA_ET 1000000 LABELS sensor_id 1 返回示例： OK |
## EXTS.S.MADD
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.MADD Pkey keynumber Skey ts value [Skey ts value ...] [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] |
| 时间复杂度 | O(n)，其中 n 为 keynumber。 |
| 命令描述 | 在指定 Pkey 的多个 Skey 中分别插入一条 Datapoint 数据。若 Pkey 或 Skey 不存在则会自动创建，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 keynumber ：指定多条数据的个数。 Skey ：Skey 名称。 ts ：Datapoint 数据的 Unix 时间戳，单位为毫秒，支持用 * 表示系统当前的时间戳。 value ：Datapoint 数据的值，数据类型为双精度浮点（double）型。 DATA_ET time ：Datapoint 数据的相对过期时间，单位为毫秒，默认为不填（表示不会过期）。 CHUNK_SIZE ：单个 Chunk 的大小，单位为 16 byte（字节），默认值为 256，取值范围为[1,256]。更多信息请参见 [EXTS.S.CREATE](the-tickets-command.md) 中的说明。 UNCOMPRESSED ：设置 Skey 不开启压缩，默认为不填（即开启压缩）。 LABELS ：Skey 的属性，输入一组或多组对应的标签名、标签值，例如 LABELS sensor_id 1 。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.MADD foo 3 temperature * 30.2 pressure * 2.05 distance * 0.5 返回示例： 1) OK 2) OK 3) OK |
## EXTS.S.INCRBY
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.INCRBY Pkey Skey ts value [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 向 Skey 中插入一条 Datapoint 数据，该命令中的 value 将与 Skey 中最近 Datapoint 的 value 值相加实现递增，也可以指定该命令中的 value 为负数实现递减。若 Pkey 或 Skey 不存在则会自动创建，默认初始值为 0，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 ts ：Datapoint 数据的 Unix 时间戳，单位为毫秒，支持用 * 表示系统当前的时间戳。 value ：待增加操作的值，可以指定该值为负数实现相减，数据类型为双精度浮点（double）型。 DATA_ET time ：Datapoint 数据的相对过期时间，单位为毫秒，默认为不填（表示不会过期）。 CHUNK_SIZE ：单个 Chunk 的大小，单位为 16 byte（字节），默认值为 256，取值范围为[1,256]。更多信息请参见 [EXTS.S.CREATE](the-tickets-command.md) 中的说明。 UNCOMPRESSED ：设置 Skey 不开启压缩，默认为不填（即开启压缩）。 LABELS ：Skey 的属性，输入一组或多组对应的标签名、标签值，例如 LABELS sensor_id 1 。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXTS.S.ADD foo temperature 1644310456023 30.0 命令。 命令示例： EXTS.S.INCRBY foo temperature 1644372093031 2 返回示例： OK 若此时执行 EXTS.S.GET foo temperature 命令，将会返回如下结果： 1) (integer) 1644372093031 2) "32" |
## EXTS.S.MINCRBY
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.MINCRBY Pkey keynumber Skey ts value [Skey ts value ...] [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] |
| 时间复杂度 | O(n)，其中 n 为 keynumber。 |
| 命令描述 | 在指定 Pkey 的多个 Skey 分别插入一条 Datapoint 数据，该命令中的 value 将分别与各个 Skey 中最近 Datapoint 的 value 值相加实现递增，也可以指定该命令中的 value 为负数实现相减。若 Pkey 或 Skey 不存在则会自动创建，默认初始值为 0，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 keynumber ：指定多条数据的个数。 Skey ：Skey 名称。 ts ：Datapoint 数据的 Unix 时间戳，单位为毫秒，支持用 * 表示系统当前的时间戳。 value ：待增加操作的值，可以指定该值为负数实现相减，数据类型为双精度浮点（double）型。 DATA_ET time ：Datapoint 数据的相对过期时间，单位为毫秒，默认为不填（表示不会过期）。 CHUNK_SIZE ：单个 Chunk 的大小，单位为 16 byte（字节），默认值为 256，取值范围为[1,256]。更多信息请参见 [EXTS.S.CREATE](the-tickets-command.md) 中的说明。 UNCOMPRESSED ：设置 Skey 不开启压缩，默认为不填（即开启压缩）。 LABELS ：Skey 的属性，输入一组或多组对应的标签名、标签值，例如 LABELS sensor_id 1 。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.MINCRBY foo 3 temperature * 0.2 pressure * -0.1 distance * 0.0 返回示例： 1) OK 2) OK 3) OK |
## EXTS.S.DEL
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.DEL Pkey Skey |
| 时间复杂度 | O(1) |
| 命令描述 | 删除指定 Pkey 中的单个 Skey，并删除目标 Skey 中所有的 Datapoint 数据。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.DEL foo temperature 返回示例： OK |
## EXTS.S.GET
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.GET Pkey Skey |
| 时间复杂度 | O(1) |
| 命令描述 | 查询指定 Skey 中最新的 Datapoint 数据。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 |
| 返回值 | 执行成功：返回对应的 Datapoint 数据。 nil：表示 Pkey 或 Skey 不存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.GET foo temperature 返回示例： 1) (integer) 1644372730150 2) "32.2" |
## EXTS.S.INFO
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.INFO Pkey Skey |
| 时间复杂度 | O(1) |
| 命令描述 | 查询指定 Skey 的元数据信息，包含 Datapoint 数量、最近 Datapoint 的时间戳与 value 值、Skey 的标签信息等信息。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 |
| 返回值 | 执行成功：返回 Skey 的元数据信息。 nil：表示 Pkey 或 Skey 不存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.INFO foo temperature 返回示例： 1) totalDataPoints // Datapoint 数量。 2) (integer) 1 3) maxDataPoints // Skey 可存储 Datapoint 数量的上限，默认为 0（表示不限制）。 4) (integer) 0 5) maxDataPointsPerChunk // 每个 Chunk 存储的 Datapoint 个数。 6) (integer) 32 7) dataPointsExpireTime // Skey 的相对过期时间（DATA_ET），单位为毫秒，0 表示不过期。 8) (integer) 0 9) lastTimestamp // 最近 Datapoint 的时间戳。 10) (integer) 1644389400996 11) chunkCount // Skey 的 chunk 数量。 12) (integer) 1 13) lastValue // 最近 Datapoint 的 value。 14) (integer) 28 15) labels // Skey 的标签信息。 16) 1) 1) "sensor_id" 2) "1" |
## EXTS.S.QUERYINDEX
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.QUERYINDEX Pkey filter1 [filter2 ...] |
| 时间复杂度 | O(n)，其中 n 为过滤条件中的最大集合数。 |
| 命令描述 | 在 Pkey 中自定义过滤条件（filter），查询目标 Skey。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 filter ：过滤条件，您可以根据 Skey 的标签（LABELS）过滤目标 Skey，更多信息请参见 [索引过滤语法](the-tickets-command.md) 。 说明 构建 filter 时，必须存在 EQ、CONTAINS、LIST_MATCH 逻辑中的任意一个，否则会查询失败。 |
| 返回值 | 执行成功：返回符合过滤条件的 Skey。 nil：表示 Pkey 或 Skey 不存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.QUERYINDEX foo sensor_id=1 返回示例： 1) "temperature" |
## EXTS.S.RANGE
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.RANGE Pkey Skey fromTs toTs [MAXCOUNT count] [AGGREGATION aggregationType timeBucket] |
| 时间复杂度 | O(n)，其中 n 为目标 Datapoint 的数据块个数。 |
| 命令描述 | 在 Skey 中查询指定时间内（包含指定时间点）的 Datapoint 数据。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 fromTs ：查询的开始时间（Unix 时间戳），单位为毫秒。 toTs ：查询的结束时间（Unix 时间戳），单位为毫秒，支持用 * 表示系统当前的时间戳，若该值等于 fromTs 可实现单时间点查询。 MAXCOUNT ：指定返回的 Datapoint 条数，默认为不填（Tair 的上限为 1,000,000 条）。 AGGREGATION ： aggregationType ：聚合类型，例如 MAX （最大值）、 AVG （平均值）、 SUM （求和）等，更多信息请参见 [聚合功能语法](the-tickets-command.md) 。 timeBucket ：采样间隔，单位为毫秒，最小值为 1,000 毫秒。 Tair 会将该时间范围内的数据进行聚合并返回一个结果，返回的时间点为采样间隔的开始时间。 例如 AGGREGATION AVG 5000 将返回每 5,000ms 的平均数。 |
| 返回值 | 执行成功：返回对应的 Datapoint 数据，若命令中指定了聚合，则返回聚合结果。 说明 返回结果中会额外返回一个 token 值，0 表示已全部显示，1 表示还有符合条件的 Datapoint 数据未显示。您可以根据该值，同时将已返回结果中最后一个 Datapoint 的时间戳作为开始时间继续遍历获取，轻松实现分批聚合。 nil：表示 Pkey 或 Skey 不存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.RANGE foo test 1644459031662 * AGGREGATION AVG 10000 MAXCOUNT 2 // 求指定时间点内每 10,000ms 的平均数，同时指定返回 2 条数据。 返回示例： 1) 1) 1) (integer) 1644459730000 2) "20.6" 2) 1) (integer) 1644459790000 2) "21.2" 2) (integer) 1 // 1 表示还有符合条件的 Datapoint 数据未显示，0 表示已全部显示。 |
## EXTS.S.MRANGE
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.MRANGE Pkey fromTs toTs [MAXCOUNT count] [AGGREGATION aggregationType timeBucket] [WITHLABELS] FILTER filter1 [filter2 ...] |
| 时间复杂度 | O(n)，其中 n 为目标 Datapoint 的数据块个数。 |
| 命令描述 | 在 Skey 中自定义过滤条件（filter）与查询时间点（包含指定时间点），查询目标 Datapoint 数据。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 fromTs ：查询的开始时间（Unix 时间戳），单位为毫秒。 toTs ：查询的结束时间（Unix 时间戳），单位为毫秒，支持用 * 表示系统当前的时间戳，若该值等于 fromTs 可实现单时间点查询。 MAXCOUNT ：指定每个 Skey 返回的 Datapoint 条数，默认为不填（Tair 的上限为 1,000,000 条）。 AGGREGATION ： aggregationType ：聚合类型，例如 MAX （最大值）、 AVG （平均值）、 SUM （求和）等，更多信息请参见 [聚合功能语法](the-tickets-command.md) 。 timeBucket ：采样间隔，单位为毫秒，最小值为 1,000 毫秒。 Tair 会将该时间范围内的数据进行聚合并返回一个结果，返回的时间点为采样间隔的开始时间。 WITHLABELS ：设置返回结果中是否包含标签信息，默认为不填（不显示标签信息）。 filter ：过滤条件，您可以根据 Skey 的标签（LABELS）过滤目标 Skey，更多信息请参见 [索引过滤语法](the-tickets-command.md) 。 说明 构建 filter 时，必须存在 EQ、CONTAINS、LIST_MATCH 逻辑中的任意一个，否则会查询失败。 |
| 返回值 | 执行成功：返回符合过滤条件的 Skey 组信息。 nil：表示 Pkey 或 Skey 不存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.MRANGE foo 1644451031662 * AGGREGATION MAX 10000 WITHLABELS FILTER sensor_id=1 返回示例： 1) 1) "temperature" 2) 1) 1) "sensor_id" 2) "1" 3) 1) 1) (integer) 1644481000000 2) "30" 4) (integer) 0 2) 1) "test" 2) 1) 1) "sensor_id" 2) "1" 3) 1) 1) (integer) 1644459730000 2) "20" 2) 1) (integer) 1644459790000 2) "20" 3) 1) (integer) 1644460620000 2) "29" 4) (integer) 0 |
## EXTS.P.RANGE
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.P.RANGE Pkey fromTs toTs pkeyAggregationType pkeyTimeBucket [MAXCOUNT count] [AGGREGATION aggregationType timeBucket] FILTER filter1 [filter2 ...] |
| 时间复杂度 | O(n)，其中 n 为目标 Datapoint 的数据块个数。 |
| 命令描述 | 在 Pkey 层级对符合过滤条件（filter）的 Datapoint 数据进行聚合，若您指定了 Skey 层级的聚合，则会优先进行 Skey 层级聚合（效果与 EXTS.S.MRANGE 命令相同），再从 Pkey 层级对第一次聚合结果进行二次聚合。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 fromTs ：查询的开始时间（Unix 时间戳），单位为毫秒。 toTs ：查询的结束时间（Unix 时间戳），单位为毫秒，支持用 * 表示系统当前的时间戳，若该值等于 fromTs 可实现单时间点查询。 pkeyAggregationType ：Pkey 的聚合类型，更多信息请参见 [聚合功能语法](the-tickets-command.md) 。 pkeyTimeBucket ：Pkey 的采样间隔，单位为毫秒，最小值为 1,000 毫秒。 Tair 会将该时间范围内的数据进行聚合并返回一个结果，返回的时间点为采样间隔的开始时间。 MAXCOUNT ：指定每个 Skey 返回的 Datapoint 条数，默认为不填（Tair 的上限为 1,000,000 条）。 AGGREGATION ： aggregationType ：Skey 的聚合类型，更多信息请参见 [聚合功能语法](the-tickets-command.md) 。 timeBucket ：Skey 的采样间隔，单位为毫秒，最小值为 1,000 毫秒。 Tair 会将该时间范围内的数据进行聚合并返回一个结果，返回的时间点为采样间隔的开始时间。 filter ：过滤条件，您可以根据 Skey 的标签（LABELS）过滤目标 Skey，更多信息请参见 [索引过滤语法](the-tickets-command.md) 。 说明 构建 filter 时，必须存在 EQ、CONTAINS、LIST_MATCH 逻辑中的任意一个，否则会查询失败。 |
| 返回值 | 执行成功：返回聚合结果。 nil：表示 Pkey 或 Skey 不存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.P.RANGE foo 1644451031662 * SUM 500000 AGGREGATION SUM 10000 FILTER sensor_id=1 返回示例： 1) 1) 1) (integer) 1644459500000 2) "40" 2) 1) (integer) 1644460500000 2) "29" 3) 1) (integer) 1644481000000 2) "30" 2) (integer) 0 |
## EXTS.S.RAW_MODIFY
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.RAW_MODIFY Pkey Skey ts value [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 修改指定 Skey 中 Datapoint 数据的 value 值。若 Pkey 或 Skey 不存在则会自动创建，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 ts ：待更新 Datapoint 的 Unix 时间戳，单位为毫秒。 value ：待更新的值，数据类型为双精度浮点（double）型。 DATA_ET time ：Datapoint 数据的相对过期时间，单位为毫秒，默认为不填（表示不会过期）。 CHUNK_SIZE ：单个 Chunk 的大小，单位为 16 byte（字节），默认值为 256，取值范围为[1,256]。更多信息请参见 [EXTS.S.CREATE](the-tickets-command.md) 中的说明。 UNCOMPRESSED ：设置 Skey 不开启压缩，默认为不填（即开启压缩）。 LABELS ：Skey 的属性，输入一组或多组对应的标签名、标签值，例如 LABELS sensor_id 1 。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.RAW_MODIFY foo temperature 1644310456023 31.5 返回示例： OK |
## EXTS.S.RAW_MMODIFY
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.RAW_MMODIFY Pkey keynumber Skey ts value [Skey ts value ...] [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] |
| 时间复杂度 | O(n)，其中 n 为 keynumber。 |
| 命令描述 | 批量修改多个指定 Skey 中 Datapoint 数据的 value 值。若 Pkey 或 Skey 不存在则会自动创建，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 keynumber ：指定多条数据的个数。 Skey ：Skey 名称。 ts ：待更新 Datapoint 的 Unix 时间戳，单位为毫秒。 value ：待更新的值，数据类型为双精度浮点（double）型。 DATA_ET time ：Datapoint 数据的相对过期时间，单位为毫秒，默认为不填（表示不会过期）。 CHUNK_SIZE ：单个 Chunk 的大小，单位为 16 byte（字节），默认值为 256，取值范围为[1,256]。更多信息请参见 [EXTS.S.CREATE](the-tickets-command.md) 中的说明。 UNCOMPRESSED ：设置 Skey 不开启压缩，默认为不填（即开启压缩）。 LABELS ：Skey 的属性，输入一组或多组对应的标签名、标签值，例如 LABELS sensor_id 1 。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.RAW_MMODIFY foo 3 temperature 1644565954814 30.2 pressure 1644565954814 2.05 distance 1644565954814 0.5 返回示例： 1) OK 2) OK 3) OK |
## EXTS.S.RAW_INCRBY
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.RAW_INCRBY Pkey Skey ts value [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 该命令中的 value 值会与指定 Skey 中 Datapoint 数据的 value 相加实现递增，也可以指定该命令中的 value 为负数实现递减。若 Pkey 或 Skey 不存在则会自动创建，默认初始值为 0，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 ts ：待更新 Datapoint 的 Unix 时间戳，单位为毫秒。 value ：待增加操作的值，可以指定该值为负数实现相减，数据类型为双精度浮点（double）型。 DATA_ET time ：Datapoint 数据的相对过期时间，单位为毫秒，默认为不填（表示不会过期）。 CHUNK_SIZE ：单个 Chunk 的大小，单位为 16 byte（字节），默认值为 256，取值范围为[1,256]。更多信息请参见 [EXTS.S.CREATE](the-tickets-command.md) 中的说明。 UNCOMPRESSED ：设置 Skey 不开启压缩，默认为不填（即开启压缩）。 LABELS ：Skey 的属性，输入一组或多组对应的标签名、标签值，例如 LABELS sensor_id 1 。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXTS.S.ADD foo temperature 1644310456 30.0 命令。 命令示例： EXTS.S.RAW_INCRBY foo temperature 1644310456 3.3 返回示例： OK 若此时执行 EXTS.S.GET foo temperature 命令，将会返回如下结果： 1) (integer) 1644310456 2) "33.3" |
## EXTS.S.RAW_MINCRBY
| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.RAW_MINCRBY Pkey keynumber Skey ts value [Skey ts value ...] [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] |
| 时间复杂度 | O(n)，其中 n 为 keynumber。 |
| 命令描述 | 批量修改多个指定 Skey 中 Datapoint 数据的 value 值，该命令中的 value 值会与指定 Skey 中 Datapoint 数据的 value 相加实现递增，也可以指定该命令中的 value 为负数实现递减。若 Pkey 或 Skey 不存在则会自动创建，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 keynumber ：指定多条数据的个数。 Skey ：Skey 名称。 ts ：待更新 Datapoint 的 Unix 时间戳，单位为毫秒。 value ：待增加操作的值，可以指定该值为负数实现相减，数据类型为双精度浮点（double）型。 DATA_ET time ：Datapoint 数据的相对过期时间，单位为毫秒，默认为不填（表示不会过期）。 CHUNK_SIZE ：单个 Chunk 的大小，单位为 16 byte（字节），默认值为 256，取值范围为[1,256]。更多信息请参见 [EXTS.S.CREATE](the-tickets-command.md) 中的说明。 UNCOMPRESSED ：设置 Skey 不开启压缩，默认为不填（即开启压缩）。 LABELS ：Skey 的属性，输入一组或多组对应的标签名、标签值，例如 LABELS sensor_id 1 。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.RAW_MINCRBY foo 3 temperature 1644565954814 30.2 pressure 1644565954814 2.05 distance 1644565954814 0.5 返回示例： 1) OK 2) OK 3) OK |
## 索引过滤语法
您可以根据Skey的标签（LABELS）过滤目标Skey。过滤条件（filter）的语法如下：
说明
构造filter时，支持如下所有命令及组合使用，但必须存在EQ、CONTAINS、LIST_MATCH逻辑中的任意一个。
| filter 命令 | 说明 | 逻辑 |
| --- | --- | --- |
| L = V | 标签 L 等于 V。 | EQ（equals） |
| L != | 标签 L 不为 NULL, 即目标 Skey 包含标签 L。 | CONTAINS |
| L = (v1,v2,...) | 标签 L 为 v1 或 v2 等。 | LIST_TMATCH |
| L != V | 标签 L 不等于 V。 | NOEQ（equals） |
| L = | 标签 L 为 NULL, 即目标 Skey 不包含标签 L。 | NOCONTAINS |
| L != (v1,v2,...) | 标签 L 不为 v1 和 v2 等。 | LIST_NOTMATCH |
## 聚合功能语法
聚合操作会对采集间隔（timeBucket）范围内的数据进行聚合，支持如下聚合类型：
MAX：最大值
MIN：最小值
AVG：平均值
SUM：求和
FIRST：第一个值
LAST：最后一个值
RANGE：范围（最大值 - 最小值）
COUNT：value数量
STD.P：总体方差
STD.S：样本方差
VAR.P：总体标准差
VAR.S：样本标准差
## 常见问题
Q：为什么部分Tair内存型（兼容Redis 5.0）版本的CHUNK_SIZE默认值比较小？
A：Tair内存型（兼容Redis 5.0）实例在25.2.0.0版本起，CHUNK_SIZE的默认值为256，在此之前的版本都是32。
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
