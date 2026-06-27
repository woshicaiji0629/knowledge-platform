## CPC.ARRAY.UPDATE2EST

| 类别 | 说明 |
| --- | --- |
| 语法 | CPC.ARRAY.UPDATE2EST key timestamp item [EX|EXAT|PX|PXAT time ] [SIZE size ] [WIN window_length ] |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定 TairCpc 中，向目标 timestamp 对应的时间窗口添加 item，并返回该时间窗口更新后的基数估算值。若 TairCpc 不存在则自动新建，新建参数用法与 [CPC.ARRAY.UPDATE](taircpc-command.md) 一致。 |
| 选项 | key ：Key 名称（TairCpc 数据结构），用于指定命令调用的 TairCpc 对象。 timestamp ：指定的 Unix 时间戳，单位为毫秒。 item ：待添加的数据。 EX ：指定 key 的相对过期时间，单位为秒，不传此参数表示不过期。 EXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为秒，不传此参数表示不过期。 PX ：指定 key 的相对过期时间，单位为毫秒，不传此参数表示不过期。 PXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为毫秒 ，不传此参数表示不过期。 SIZE ：时间窗口个数，默认为 10，范围为[1,1000]，建议设置在 120 以内。 WIN ：时间窗口的长度（单位为毫秒），默认为 60000 毫秒（1 分钟）。 |
| 返回值 | 执行成功：返回目标时间窗口更新后的估算值。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.ARRAY.UPDATE2EST foo 1645584530000 f3 返回示例： "3" |
