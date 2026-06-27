## EXTS.S.INFO

| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.INFO Pkey Skey |
| 时间复杂度 | O(1) |
| 命令描述 | 查询指定 Skey 的元数据信息，包含 Datapoint 数量、最近 Datapoint 的时间戳与 value 值、Skey 的标签信息等信息。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 |
| 返回值 | 执行成功：返回 Skey 的元数据信息。 nil：表示 Pkey 或 Skey 不存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.INFO foo temperature 返回示例： 1) totalDataPoints // Datapoint 数量。 2) (integer) 1 3) maxDataPoints // Skey 可存储 Datapoint 数量的上限，默认为 0（表示不限制）。 4) (integer) 0 5) maxDataPointsPerChunk // 每个 Chunk 存储的 Datapoint 个数。 6) (integer) 32 7) dataPointsExpireTime // Skey 的相对过期时间（DATA_ET），单位为毫秒，0 表示不过期。 8) (integer) 0 9) lastTimestamp // 最近 Datapoint 的时间戳。 10) (integer) 1644389400996 11) chunkCount // Skey 的 chunk 数量。 12) (integer) 1 13) lastValue // 最近 Datapoint 的 value。 14) (integer) 28 15) labels // Skey 的标签信息。 16) 1) 1) "sensor_id" 2) "1" |
