## CPC.ARRAY.UPDATE

| 类别 | 说明 |
| --- | --- |
| 语法 | CPC.ARRAY.UPDATE key timestamp item [EX|EXAT|PX|PXAT time ] [SIZE size ] [WIN window_length ] |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定 TairCpc 中，向目标 timestamp 对应的时间窗口添加 item。若 TairCpc 不存在则自动新建， SIZE 为时间窗口个数， WIN 为时间窗口的长度（单位为毫秒）。随着流式数据的写入，TairCpc 会持续向前更新并保存 SIZE * WIN 时间范围内的数据，超过该时间范围的数据会被覆盖、删除。 SIZE 和 WIN 属性仅在新建 TairCpc 的时生效。 说明 例如目标 key 为计算近 10 分钟内每分钟的数据：可以设置 SIZE 为 10（10 个时间窗口）、 WIN 为 60000（每个时间窗口为 1 分钟）。当目标 key 中写入第 11 分钟的数据时，第 1 分钟的数据会逐渐被覆盖、删除。 |
| 选项 | key ：Key 名称（TairCpc 数据结构），用于指定命令调用的 TairCpc 对象。 timestamp ：指定的 Unix 时间戳，单位为毫秒。 item ：待添加的数据。 EX ：指定 key 的相对过期时间，单位为秒，不传此参数表示不过期。 EXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为秒，不传此参数表示不过期。 PX ：指定 key 的相对过期时间，单位为毫秒，不传此参数表示不过期。 PXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为毫秒 ，不传此参数表示不过期。 SIZE ：时间窗口个数，默认为 10，范围为[1,1000]，建议设置在 120 以内。 WIN ：时间窗口的长度（单位为毫秒），默认为 60000 毫秒（1 分钟）。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.ARRAY.UPDATE foo 1645584510000 f1 SIZE 120 WIN 10000 返回示例： OK |
