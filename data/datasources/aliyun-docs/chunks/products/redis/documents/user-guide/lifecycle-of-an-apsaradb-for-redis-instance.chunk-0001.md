| 操作 | 说明 |
| --- | --- |
| [创建实例](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md) | 云数据库 Tair（兼容 Redis） 分为 Tair（企业版） 和 Redis 开源版 ，其中 Tair（企业版） 包含多种形态： [内存型](../product-overview/dram-based-instances.md) 、 [持久内存型](../product-overview/persistent-memory-optimized-instances-1.md) 、 [磁盘型](../product-overview/essd-based-instances-1.md) 。您可以创建适应业务需求的实例。 |
| [变更实例配置](change-the-configurations-of-an-instance.md) | 通过变更实例的规格、架构和类型，适应不同场景对实例性能和兼容性的需求。 |
| [调整集群分片数](adjust-the-number-of-cluster-shards.md) | 分片数量越多，实例的整体性能越强。您可以根据业务对性能的需求，调整实例的分片数量。 |
| [开启读写分离](enable-read-write-splitting.md) | 当读请求流量非常大，超过节点性能上限时，您可以开启写分类功能。开启后，您无需修改业务代码，实例能够自动识别读、写请求并进行对应转发，满足高并发读写的业务场景。 |
| [增删备节点](node-management.md) | 增加实例的备节点数，可以提高实例的容灾能力。 |
| [重启实例](restart-one-or-more-apsaradb-for-redis-instances.md) | 当实例出现连接数满或性能问题时，您可以重启实例以释放所有连接。 |
| [升级大版本](upgrade-the-major-version-1.md) | 升级 Redis 开源版 实例的大版本，例如从兼容 Redis 5.0 升级到 7.0，升级后可体验新版本的相关特性与功能。更多信息请参见 [Redis](../support/new-features-of-apsaradb-for-redis.md) [开源版大版本新特性与兼容性](../support/new-features-of-apsaradb-for-redis.md) 。 |
| [升级小版本与代理版本](update-the-minor-version.md) | 云数据库 Tair（兼容 Redis） 会不断地对内核进行深度优化，修复安全漏洞，提升服务稳定性。建议定期检查并升级小版本。 |
