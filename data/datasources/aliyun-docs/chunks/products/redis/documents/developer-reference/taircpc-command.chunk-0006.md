1，则表示写入成功且不存在重复；若为 0 则表示已存在当前 item。若 TairCpc 不存在则自动新建，新建参数用法与 [CPC.ARRAY.UPDATE](taircpc-command.md) 一致。 |
| [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairCpc 数据。 |
