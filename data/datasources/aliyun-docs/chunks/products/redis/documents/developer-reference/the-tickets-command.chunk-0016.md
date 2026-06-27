## EXTS.S.INCRBY

| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.INCRBY Pkey Skey ts value [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 向 Skey 中插入一条 Datapoint 数据，该命令中的 value 将与 Skey 中最近 Datapoint 的 value 值相加实现递增，也可以指定该命令中的 value 为负数实现递减。若 Pkey 或 Skey 不存在则会自动创建，默认初始值为 0，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 ts ：Datapoint 数据的 Unix 时间戳，单位为毫秒，支持用 * 表示系统当前的时间戳。 value ：待增加操作的值，可以指定该值为负数实现相减，数据类型为双精度浮点（double）型。 DATA_ET time ：Datapoint 数据的相对过期时间，单位为毫秒，默认为不填（表示不会过期）。 CHUNK_SIZE ：单个 Chunk 的大小，单位为 16 byte（字节），默认值为 256，取值范围为[1,256]。更多信息请参见 [EXTS.S.CREATE](the-tickets-command.md) 中的说明。 UNCOMPRESSED ：设置 Skey 不开启压缩，默认为不填（即开启压缩）。 LABELS ：Skey 的属性，输入一组或多组对应的标签名、标签值，例如 LABELS sensor_id 1 。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXTS.S.ADD foo temperature 1644310456023 30.0 命令。 命令示例： EXTS.S.INCRBY foo temperature 1644372093031 2 返回示例： OK 若此时执行 EXTS.S.GET foo temperature 命令，将会返回如下结果： 1) (integer) 1644372093031 2) "32" |
