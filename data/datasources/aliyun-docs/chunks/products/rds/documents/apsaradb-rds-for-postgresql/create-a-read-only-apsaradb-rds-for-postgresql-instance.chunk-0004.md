DS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在实例分布区域，单击只读实例后的添加。
设置只读实例的参数。

| 参数 | 说明 |
| --- | --- |
| 计费方式 | 包年包月 ：适合长期使用（一次性付费）。 按量付费 ：适合短期使用（按小时付费）。您可以先创建按量付费的只读实例，确认实例符合要求后再转包年包月。 |
| 产品系列 | 基础系列 ：单节点的只读实例，性价比高，适用于学习或测试。故障恢复和重启耗时较长。 高可用系列 （默认）：拥有一个主节点和一个备节点，可实现只读实例的高可用，适用于生产环境，适合 80%以上的用户场景。 说明 如果 产品系列 选择高可用系列，则还需选择主节点可用区、部署方案（多可用区部署或单可用区部署）以及备节点可用区。 |
| 产品类型 | 仅当主实例 存储类型 为 ESSD 云盘 或 高性能云盘 时，才支持选择 倚天版 。 标准版 和 倚天版 的更多信息，请参见 [产品类型](../product-overview/product-types.md) 。 |
| 可用区 | 可用区是地域中的一个独立物理区域，不同可用区之间没有实质性区别。相比单可用区，多可用区能提供可用区级别的容灾。 |
| 实例规格 | 通用规格 ：通用型的实例规格，独享被分配的内存和 I/O 资源，与同一服务器上的其他通用型实例共享 CPU 和存储资源。 独享规格 ：独享或独占型的实例规格。独享型指独享被分配的 CPU、内存、存储和 I/O 资源。独占型是独享型的顶配，独占整台服务器的 CPU、内存、存储和 I/O 资源。 说明 每种规格都有对应的 CPU 核数、内存、最大连接数和最大 IOPS。高性能本地盘主实例的只读实例规格不能低于主实例。规格详情请参见 [RDS PostgreSQL](read-only-apsaradb-rds-for-postgresql-instance-types.md) [只读实例规格列表](read-only-apsaradb-rds-for-postgresql-instance-types.md) 。 |
| 存储空间 | 存储空间包括数据空间、系统文件空间、WAL 文件空间和事务文件空间。调整存储空间时最小单位为 5 GB。 说明 只读实例存储空间不能低于主实例。各规格的存储空间大小，请参见 [RDS PostgreSQL](read-only-apsaradb-rds-for-postgresql-instance-types.md) [只读实例规格列表](read-only-apsaradb-rds-for-postgresql-instance-types.md) 。 |
