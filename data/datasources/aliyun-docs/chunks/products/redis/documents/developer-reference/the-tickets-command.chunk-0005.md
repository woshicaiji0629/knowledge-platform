| 类型 | 命令 | 语法 | 说明 |
| --- | --- | --- | --- |
| 基础写操作 | [EXTS.P.CREATE](the-tickets-command.md) | EXTS.P.CREATE Pkey | 创建一个新的 Pkey（TairTS 数据结构），若 Pkey 已存在则创建失败。 |
| [EXTS.S.CREATE](the-tickets-command.md) | EXTS.S.CREATE Pkey Skey [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 label2 val2 ...] | 在指定的 Pkey 中创建一个 Skey，若 Pkey 不存在则会自动创建，若 Skey 已经存在则创建失败。 说明 您可以在创建 Skey 时设置其相关属性，例如过期时间、是否开启压缩等。 |  |
| [EXTS.S.ALTER](the-tickets-command.md) | EXTS.S.ALTER Pkey Skey [DATA_ET time] | 修改指定 Skey 的元数据信息，当前仅支持修改过期时间（DATA_ET）。 |  |
| [EXTS.S.ADD](the-tickets-command.md) | EXTS.S.ADD Pkey Skey ts value [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] | 向 Skey 中插入一条 Datapoint 数据。若 Pkey 或 Skey 不存在则会自动创建，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |  |
| [EXTS.S.MADD](the-tickets-command.md) | EXTS.S.MADD Pkey keynumber Skey ts value [Skey ts value ...] [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] | 在指定 Pkey 的多个 Skey 中分别插入一条 Datapoint 数据。若 Pkey 或 Skey 不存在则会自动创建，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |  |
| [EXTS.S.INCRBY](the-tickets-command.md) | EXTS.S.INCRBY Pkey Skey ts value [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED]
