SIZE 为 10（10 个时间窗口）、 WIN 为 60000（每个时间窗口为 1 分钟）。当目标 key 中写入第 11 分钟的数据时，第 1 分钟的数据会逐渐被覆盖、删除。 |
| [CPC.ARRAY.ESTIMATE](taircpc-command.md) | CPC.ARRAY.ESTIMATE key timestamp | 获取指定 TairCpc 中目标 timestamp 所在时间窗口的基数估算值。 |
| [CPC.ARRAY.ESTIMATE.RANGE](taircpc-command.md) | CPC.ARRAY.ESTIMATE.RANGE key start_time end_time | 获取指定 TairCpc 的指定时间段内（包含指定时间点）各个时间窗口的基数估算值。 |
| [CPC.ARRAY.ESTIMATE.RANGE.MERGE](taircpc-command.md) | CPC.ARRAY.ESTIMATE.RANGE.MERGE key timestamp range | 获取指定 TairCpc 在指定时间点至往前 range（含当前窗口）个时间窗口内，时间窗口合并、去重后的基数估算值。 |
| [CPC.ARRAY.UPDATE2EST](taircpc-command.md) | CPC.ARRAY.UPDATE2EST key timestamp item [EX|EXAT|PX|PXAT time ] [SIZE size ] [WIN window_length ] | 在指定 TairCpc 中，向目标 timestamp 对应的时间窗口添加 item，并返回该时间窗口更新后的基数估算值。若 TairCpc 不存在则自动新建，新建参数用法与 [CPC.ARRAY.UPDATE](taircpc-command.md) 一致。 |
| [CPC.ARRAY.UPDATE2JUD](taircpc-command.md) | CPC.ARRAY.UPDATE2JUD key timestamp item [EX|EXAT|PX|PXAT time ] [SIZE size ] [WIN window_length ] | 在指定 TairCpc 中，向目标 timestamp 对应的时间窗口添加 item，并返回该时间窗口更新后的基数估算值和其与更新前的差值。若返回的差值为 1，则表示写入成功且不存在重复；若为 0 则表示已存在当前 item。若 TairCpc 不存在则自动新建，新建参数用法与 [CPC.ARRAY.UPDATE](taircpc-command.md) 一致。 |
| [DEL](https://valkey.io/commands/del/) | DEL key [k
