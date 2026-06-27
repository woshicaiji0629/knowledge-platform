mand.md) | EXHKEYS key | 获取 key 指定的 TairHash 中所有的 field。 |
| [EXHVALS](the-tairhash-command.md) | EXHVALS key | 获取 key 指定的 TairHash 中所有 field 的值。 |
| [EXHGETALL](the-tairhash-command.md) | EXHGETALL key | 获取 key 指定的 TairHash 中所有 field 及其 value。 |
| [EXHSCAN](the-tairhash-command.md) | EXHSCAN key op subkey [MATCH pattern] [COUNT count] | 扫描 Key 指定的 TairHash。 说明 仅内存型实例支持该命令。 |
| [EXHDEL](the-tairhash-command.md) | EXHDEL key field [field ...] | 删除 key 指定的 TairHash 中的一个 field，如果 TairHash 不存在或者 field 不存在则返回 0 ，成功删除返回 1。 |
| [DEL](https://valkey.io/commands/del/) | DEL <key> [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairHash 数据。 |
