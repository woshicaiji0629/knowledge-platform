### 阿里云控制台工具
Tair和Redis在控制台提供了Top Key统计和离线全量Key分析功能帮助您快速找出大Key与热Key。

| 方法 | 使用限制 | 说明 | 操作步骤 |
| --- | --- | --- | --- |
| [Top Key](use-the-real-time-key-statistics-feature.md) [统计](use-the-real-time-key-statistics-feature.md) （推荐） | 仅 Redis 开源版 5.0 及以上版本和 Tair（企业版） 内存型、持久内存型支持该功能。 | 实时显示每个分片中各数据类型前三的大 Key 和热 Key 信息。 支持查看 4 天内大 Key 和热 Key 的历史信息。 | 访问 [实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou) ，在上方选择地域，然后单击目标实例 ID。 在左侧导航栏，单击 CloudDBA > 实时 Top Key 统计 或 离线全量 Key 分析 。 |
| [离线全量](offline-key-analysis.md) [Key](offline-key-analysis.md) [分析](offline-key-analysis.md) | 单副本实例或 磁盘型实例不支持该功能。 | 对 RDB 备份文件进行定制化的分析，得出 Key 在内存中的占用和分布、Key 过期时间等信息。 时效性差，RDB 文件较大时耗时较长。 无法分析热 Key 信息。 |  |

如果您的实例不能使用上述功能，请参考以下方法。
