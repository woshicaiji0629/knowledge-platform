## RDS MySQL基础系列（云盘）
重要
实际最大IOPS：受存储类型、存储空间大小和实例规格共同影响，请参见[最大](../product-overview/primary-apsaradb-rds-instance-types.md)[IOPS](../product-overview/primary-apsaradb-rds-instance-types.md)[计算公式](../product-overview/primary-apsaradb-rds-instance-types.md)。
实际最大IO带宽：受存储类型、存储空间大小和实例规格共同影响，请参见[最大吞吐量计算公式](../product-overview/primary-apsaradb-rds-instance-types.md)。

| 系列 | 规格族 | 规格代码 | CPU 和内存 | 最大连接数默认值 | 存储 |  |
| --- | --- | --- | --- | --- | --- | --- |
| 实例规格的最大 IOPS | 实例规格的最大 IO 带宽（MB/s） | 存储空间 |  |  |  |  |
| 基础系列 | 通用型 | mysql.n2.medium.1 | 2 核 4GB | 4000 | 通用型无法保证最大 IOPS 和最大 IO 带宽。如果业务对 IOPS 敏感，建议选择高可用系列独享型。 | ESSD PL0 云盘：10 GB~32000 GB ESSD PL1 云盘：20 GB~64000 GB 高性能云盘：10 GB~64000 GB SSD 云盘：20 GB~6000 GB |
| mysql.n4.medium.1 | 2 核 8GB | 6000 |  |  |  |  |
| mysql.n2.large.1 | 4 核 8GB | 6000 |  |  |  |  |
| mysql.n4.large.1 | 4 核 16GB | 8000 |  |  |  |  |
| mysql.n2.xlarge.1 | 8 核 16GB | 8000 |  |  |  |  |
| mysql.n4.xlarge.1 | 8 核 32GB | 10000 |  |  |  |  |
