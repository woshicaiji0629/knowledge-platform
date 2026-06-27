### 按性能分类
按云盘性能不同，分为ESSD系列云盘和上一代云盘。
ESSD系列云盘

| 云盘类型 | 特点 | 应用场景 | 数据可靠性保证 | 计费 |
| --- | --- | --- | --- | --- |
| [ESSD](essds.md) [云盘](essds.md) | 高 IOPS 低延迟 | 时延敏感的应用或者 I/O 密集型业务场景： 大型 OLTP 数据库 NoSQL 数据库 Elasticsearch 分布式日志 | 99.9999999% | 云盘容量费 |
| [ESSD AutoPL](essd-autopl-disks.md) [云盘](essd-autopl-disks.md) | 容量与性能可解耦 支持预配置云盘性能（允许在存储容量不变的情况下，根据业务需求灵活配置预配置性能） 支持性能突发（波动性业务在面临突发的数据读写压力时，ESSD AutoPL 云盘会根据业务实际情况临时提升云盘性能） | ESSD 云盘所适用的场景 云盘容量固定，云盘性能要求高 业务波动较大，波峰高频出现，需应对突发业务 | 99.9999999% | 云盘容量费 预配置性能费（开启后按量收费） 突发性能费（开启后按量收费） |
| [ESSD](regional-essd-disks.md) [同城冗余云盘](regional-essd-disks.md) | 高 IOPS（Input/Output Operations per Second） 同城冗余 | ESSD 云盘所适用的场景 数据库多可用区容灾 跨可用区的容器部署 自建或在云上部署 SaaS 服务 | 99.9999999999% | 云盘容量费 |
| [ESSD PL-X](essd-pl-x-cloud-disk.md) [云盘（邀测）](essd-pl-x-cloud-disk.md) | 超高 IOPS 超高吞吐量 超低时延 支持预配置云盘性能 | 对云盘 IOPS、吞吐量和时延有更高要求的 OLTP 数据库和 KV 数据库 | 99.9999999% | 云盘容量费 预配置性能费（默认开启，开启后收费） |
| ESSD Entry 云盘 仅 [通用算力型（U](general-work-force.md) [实例）](general-work-force.md) 和 [经济型实例规格族](shared-instance-families.md) [e](shared-instance-families.md) 支持挂载 ESSD Entry 云盘。 | 高 IOPS 低延迟 | 开发与测试业务 作为系统盘 | 99.9999999% | 云盘容量费 |
