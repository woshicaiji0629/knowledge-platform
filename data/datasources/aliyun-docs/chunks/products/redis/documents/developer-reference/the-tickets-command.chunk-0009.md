的 value 值会与指定 Skey 中 Datapoint 数据的 value 相加实现递增，也可以指定该命令中的 value 为负数实现递减。若 Pkey 或 Skey 不存在则会自动创建，属性（过期时间、是否开启压缩等）仅在 Skey 不存在并自动创建的情况下生效。 |  |
| 通用 | [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairTS 数据。 |
