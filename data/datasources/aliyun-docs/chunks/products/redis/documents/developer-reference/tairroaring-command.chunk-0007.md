返回 0。 说明 该命令在集群架构实例中不支持执行跨 Slot 的 Key。 | V2.2 新增 |  |
| [TR.RANK](tairroaring-command.md) | TR.RANK key offset | 获取 Roaring Bitmap 中从 offset 为 0 到指定 offset 区间内（包含该值），bit 值为 1 的数量。 | V2.2 新增 |  |
| 通用 | [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairRoaring 数据。 | - |
