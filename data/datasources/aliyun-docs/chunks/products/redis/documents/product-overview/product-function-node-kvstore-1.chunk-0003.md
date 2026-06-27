e.md) |  |
| 支持数据闪回 | 支持将实例整体或指定 Key 的数据恢复至某个秒级的时间点。 | [通过数据闪回按时间点恢复数据](../user-guide/use-data-flashback-to-restore-data-by-point-in-time.md) |  |
| 高可用 | 自动和手动执行主备切换 | 支持自动 HA 实现故障转移，支持手动执行主备切换（即切换节点角色），便于您进行实时容灾演练。 | [手动执行主备切换](../user-guide/manually-switch-workloads-from-a-master-node-to-a-replica-node.md) |
| 重启或重搭代理节点 | 支持手动重启或重新搭建代理节点，便于您进行实时容灾演练，也可以在服务异常、延迟较高时发起主动运维。 | [重启或重搭代理节点](../user-guide/restart-or-rebuild-a-proxy-node.md) |  |
| 连接管理 | 修改专有网络/交换机 | 支持修改专有网络或交换机。 | [修改专有网络](../user-guide/change-the-vpc-or-vswitch-of-an-instance.md) [VPC](../user-guide/change-the-vpc-or-vswitch-of-an-instance.md) [或交换机](../user-guide/change-the-vpc-or-vswitch-of-an-instance.md) |
| 申请/释放公网连接地址 | 默认情况下，云数据库 Redis 版仅提供专有网络连接地址，如需从本地通过公网连接 Redis 实例，可以申请 Redis 实例的公网连接地址。 | [申请公网连接地址](../user-guide/apply-for-a-public-endpoint-for-an-apsaradb-for-redis-instance.md) |  |
| 开通/释放直连地址 | 支持开通直连访问模式，兼容原生 Redis Cluster 协议。 | [开通直连访问](../user-guide/enable-the-direct-connection-mode.md) |  |
| 弹性能力 | 手动/自动开启带宽包 | 支持在不调整实例规格的情况下手动或动态增加实例的带宽，轻松应对流量高峰。 | [开启带宽弹性伸缩](../user-guide/enable-bandwidth-auto-scaling.md) |
| 开启/关闭自动扩容 | 当内存平均使用率达到阈值后会自动升级 Redis 实例的规格，帮助您快速弹性适配业务高峰，规避内存溢出的风险。 | [开启自动扩容](../user-
