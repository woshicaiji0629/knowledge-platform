## 相关API

| API 接口 | 说明 |
| --- | --- |
| [ModifyBackupPolicy](../developer-reference/api-r-kvstore-2015-01-01-modifybackuppolicy-redis.md) | 修改实例的自动备份策略，可通过 EnableBackupLog 参数开启或关闭数据按时间点恢复功能。 同时，您还需确保已在实例的参数设置中开启 AOF 持久化（appendonly 为 yes），开启后才能使用数据按时间点恢复功能，更多信息请参见 [Tair](parameter-support.md) [企业版配置参数列表](parameter-support.md) 。 |
| [RestoreInstance](../developer-reference/api-r-kvstore-2015-01-01-restoreinstance-redis.md) | 将备份文件中的数据恢复到当前实例中，结合数据按时间点恢复更可实现将指定的 Key 恢复至某个秒级时间点。 |

该文章对您有帮助吗？
反馈
