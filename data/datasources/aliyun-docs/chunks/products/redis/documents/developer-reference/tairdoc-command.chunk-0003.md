command.md) | JSON.STRLEN key path | 获取目标 key 中 path 对应值的字符串长度，path 对应值的类型需要为字符串。 |
| [JSON.ARRAPPEND](tairdoc-command.md) | JSON.ARRAPPEND key path json [ json ...] | 在指定 path 对应数组（array）的末尾添加 JSON 数据，支持添加多个 JSON。 |
| [JSON.ARRPOP](tairdoc-command.md) | JSON.ARRPOP key path [ index ] | 移除并返回 path 对应数组（array）中指定位置（index）的元素。 |
| [JSON.ARRINSERT](tairdoc-command.md) | JSON.ARRINSERT key path [ index ] json [ json ...] | 将 JSON 插入到 path 对应的数组（array）中，原有元素会往后移动。 |
| [JSON.ARRLEN](tairdoc-command.md) | JSON.ARRLEN key path | 获取 path 对应数组（array）的长度。 |
| [JSON.ARRTRIM](tairdoc-command.md) | JSON.ARRTRIM key path start stop | 修剪目标 key 的 path 对应的数组（array），保留 start 至 stop 范围内的数据。 |
| [DEL](https://valkey.io/commands/del/) | DEL <key> [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairDoc 数据。 |
