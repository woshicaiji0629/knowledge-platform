| 分类 | 超限说明 | 解决方案 |  |
| --- | --- | --- | --- |
| 写入超限 | WriteQuotaExceed（Project 级别超限） | Project 写流量：Project write quota exceed: inflow: xxx Project 写次数：Project write quota exceed: qps: xxx | 在 [日志服务控制台](https://sls.console.aliyun.com) 调整资源配置。具体操作，请参见 [调整资源配额](adjust-resource-quotas.md) 。 |
| ShardWriteQuotaExceed（Shard 级别超限） | Shard 写：shard write quota exceed, please split shard（所有可用 Shard 写入都超过限制） Shard 写：shard write quota exceed, shard: xxx | 使用手动或自动分裂方式新增 Shard。具体操作，请参见 [管理](manage-shards.md) [Shard](manage-shards.md) 。 |  |
| 读取超限 | ShardReadQuotaExceed（Shard 级别超限，Project 级别没有限制读） | Shard 读次数：shard read qps exceed quota limits Shard 读流量：shard read bytes exceed quota limits | 使用手动或自动分裂方式新增 Shard。具体操作，请参见 [管理](manage-shards.md) [Shard](manage-shards.md) 。 |
| 资源创建超限 | ProjectQuotaExceed | Logstore 数量：project xxx logstore count quota exceed Project 数量： Account <aliuid> most has <project quota> project Shard 数量： project <project name>, shard count quota exceed | 在 [日志服务控制台](https://sls.console.aliyun.com) 调整资源配置。具体操作，请参见 [调整资源配额](adjust-resource-quotas.md) 。 |
| 请求类超限 | 仪表盘数量超限 | dashboard quota exceed | 在 [日志服务控制台](https://sls.console.aliyun.com) 调整资源配置。具体操作，请参见 [调整资源配额](adjus
