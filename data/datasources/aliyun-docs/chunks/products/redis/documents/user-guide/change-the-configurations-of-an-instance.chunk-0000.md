## 支持的变配项及影响
变配不会影响什么？
所有变配操作：
连接地址、账号密码、白名单等不变：变更完成后应用代码无需修改。
通常不丢失数据：但在切换的瞬间，若发生原主节点宕机等并发的极端情况，存在丢失少量未同步数据的理论风险。

| 变配类型 | 变配影响 |
| --- | --- |
| 单节点变配到高可用（主从双副本） | 1~2 次 30 秒内连接闪断，1 分钟左右只读。 |
| [标准（主备）转集群](change-the-architecture-of-an-instance.md) | 1~2 次 30 秒内连接闪断，1 分钟左右只读。 |
| [集群转标准（主备）](change-the-architecture-of-an-instance.md) | 1~2 次 30 秒内连接闪断，1 分钟左右只读。 |
| [升降实例规格](change-the-instance-specification.md) | 可能出现 1~2 次 30 秒内连接闪断，1 分钟左右只读。 |
| [调整集群分片数](adjust-the-number-of-cluster-shards.md) | 可能出现 1~2 次 30 秒内连接闪断，1 分钟左右只读。 |
| [开关读写分离](enable-read-write-splitting.md) | 秒级闪断。 |
| [增删备节点](node-management.md) | 无。 |
| [转为云原生部署模式](change-to-the-cloud-native-deployment-mode.md) | 1 次 30 秒内连接闪断，1 分钟左右只读。 |
