开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |  |
| [EXTS.S.INCRBY](the-tickets-command.md) | EXTS.S.INCRBY Pkey Skey ts value [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] | 向 Skey 中插入一条 Datapoint 数据，该命令中的 value 将与 Skey 中最近 Datapoint 的 value 值相加实现递增，也可以指定该命令中的 value 为负数实现递减。若 Pkey 或 Skey 不存在则会自动创建，默认初始值为 0，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |  |
| [EXTS.S.MINCRBY](the-tickets-command.md) | EXTS.S.MINCRBY Pkey keynumber Skey ts value [Skey ts value ...] [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] | 在指定 Pkey 的多个 Skey 分别插入一条 Datapoint 数据，该命令中的 value 将分别与各个 Skey 中最近 Datapoint 的 value 值相加实现递增，也可以指定该命令中的 value 为负数实现相减。若 Pkey 或 Skey 不存在则会自动创建，默认初始值为 0，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |  |
| [EXTS.S.DEL](the-tickets-command.md) | EXTS.S.DEL Pkey Skey | 删除指定 Pkey 中的单个 Skey，并删除目标 Skey 中所有的 Datapoint 数据。 |  |
| 基础读操作 | [EXTS.S.GET](the-tickets-command.md) | EXTS.S.GET Pkey Skey | 查询指定 Skey 中最新的 Datapoint 数据。 |
| [EXTS.S.INFO](the-tickets-command.md) | EXTS.S.INFO Pkey Skey | 查询指定 Skey 的元数据信息，包含 Datapoint 数量、最近 Datapoint 的时间戳与 value 值、Skey 的标签信息等信息。 |  |
| [EXTS.S.QUERYINDEX](the-tickets-command.md) | EXTS.S.QUERYINDEX Pkey filter1 [filter2
