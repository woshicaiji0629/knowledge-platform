| 系列 | 规格族 | 规格代码 | CPU 和内存 | 最大连接数默认值 | 存储 |  |
| --- | --- | --- | --- | --- | --- | --- |
| 实例规格的最大 IOPS | 实例规格的最大 IO 带宽（MB/s） | 存储空间 |  |  |  |  |
| 集群系列 | 通用型 | mysql.n2.small.xc | 1 核 2GB | 2200 | 通用型无法保证最大 IOPS 和最大 IO 带宽。如果业务对 IOPS 敏感，建议选择独享型。 | ESSD PL1 云盘：20 GB~64000 GB ESSD PL2 云盘：500 GB~64000 GB ESSD PL3 云盘：1500 GB~64000 GB 高性能云盘：10 GB~64000 GB 说明 RDS MySQL 支持在存储空间达到阈值时自动进行扩容，详情请参见 [存储/性能自动扩容](automatic-expansion-of-cloud-disk.md) 。 |
| mysql.n2.medium.xc | 2 核 4GB | 4000 |  |  |  |  |
| mysql.n4.medium.xc | 2 核 8GB | 6000 |  |  |  |  |
| mysql.n8.medium.xc | 2 核 16GB | 8000 |  |  |  |  |
| mysql.n2.large.xc | 4 核 8GB | 6000 |  |  |  |  |
| mysql.n4.large.xc | 4 核 16GB | 8000 |  |  |  |  |
| mysql.n8.large.xc | 4 核 32GB | 12000 |  |  |  |  |
| mysql.n2.xlarge.xc | 8 核 16GB | 12000 |  |  |  |  |
| mysql.n4.xlarge.xc | 8 核 32GB | 12000 |  |  |  |  |
| mysql.n8.xlarge.xc | 8 核 64GB | 16000 |  |  |  |  |
| mysql.n2.2xlarge.xc | 16 核 32GB | 16000 |  |  |  |  |
| mysql.n4.2xlarge.xc | 16 核 64GB | 20000 |  |  |  |  |
| 独享型 | mysql.x2.medium.xc | 2 核 4GB | 4000 | 10000 | 125 |  |
| mysql.x4.medium.xc | 2 核 8GB | 6000 |  |  |  |  |
| mysql.x8.medium.xc | 2 核 16GB | 8000 |  |  |
