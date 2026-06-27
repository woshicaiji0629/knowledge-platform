于 2022 年 12 月 12 日 10:30:10 过期。 说明 该功能仅支持偏移 Key 级别的过期时间，不支持偏移 Tair 自研数据结构中 Key 内部的过期时间，例如 exHash 的 Field、TS 的 Skey 等。 设置过期偏移时间 不能早于指定的 闪回时间点 ，也不能晚于提交恢复任务的时间点。 |

单击确定。
选择恢复模式为原实例时，当前实例将进入备份恢复中状态，等待实例状态变更为运行中即可。
选择恢复模式为新建实例时，您需要在跳转到的克隆实例，选择备份时间点（即数据要恢复到的时间点）和新实例的配置。
说明
新实例的架构需选择为标准版或集群版，且实例规格的容量需大于等于原实例，关于创建实例的各参数的解释，请参见[创建](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md)[Redis](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md)[实例](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md)。
