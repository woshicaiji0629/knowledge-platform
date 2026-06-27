| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [CPC.UPDATE](taircpc-command.md) | CPC.UPDATE key item [EX|EXAT|PX|PXAT time ] | 在指定 TairCpc 中添加 item。若 TairCpc 不存在则自动新建，若待添加的 item 已存在于目标 TairCpc 中，则不会进行操作。 |
| [CPC.ESTIMATE](taircpc-command.md) | CPC.ESTIMATE ke y | 获取指定 TairCpc 去重后的基数估算值，返回值的数据类型为 double 类型，您可以仅取整数部分（忽略小数点后的数据）。 |
| [CPC.UPDATE2EST](taircpc-command.md) | CPC.UPDATE2EST key item [EX|EXAT|PX|PXAT time ] | 在指定 TairCpc 中添加 item，返回更新后的基数估算值。若 TairCpc 不存在则自动新建。 |
| [CPC.UPDATE2JUD](taircpc-command.md) | CPC.UPDATE2JUD key item [EX|EXAT|PX|PXAT time ] | 在指定 TairCpc 中添加 item，并返回更新后的基数估算值和其与更新前的差值。若返回的差值为 1 则表示写入成功且不存在重复；若为 0 则表示已存在当前 item。若 TairCpc 不存在则自动新建。 |
| [CPC.ARRAY.UPDATE](taircpc-command.md) | CPC.ARRAY.UPDATE key timestamp item [EX|EXAT|PX|PXAT time ] [SIZE size ] [WIN window_length ] | 在指定 TairCpc 中，向目标 timestamp 对应的时间窗口添加 item。若 TairCpc 不存在则自动新建， SIZE 为时间窗口个数， WIN 为时间窗口的长度（单位为毫秒）。随着流式数据的写入，TairCpc 会持续向前更新并保存 SIZE * WIN 时间范围内的数据，超过该时间范围的数据会被覆盖、删除。 SIZE 和 WIN 属性仅在新建 TairCpc 的时生效。 说明 例如目标 key 为计算近 10 分钟内每分钟的数据：可以设置 SIZE 为 10（10 个时间窗口）、 WIN 为 60000（每个时间窗口为 1 分钟）。当目标 key 中写入第 11 分钟的数据时，第 1 分钟的数据会逐渐被覆盖、删除。 |
| [CPC.ARRAY.ESTIMATE](taircpc-command.md) | CPC.ARRAY.ESTIMATE key
