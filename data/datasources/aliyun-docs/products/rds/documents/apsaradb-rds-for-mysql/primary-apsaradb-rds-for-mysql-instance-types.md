# RDS MySQL标准版主实例规格型号、CPU核数、内存、连接数、IOPS、磁盘空间等-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-mysql/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-mysql/getting-started.md)

- [AI能力中心](products/rds/documents/apsaradb-rds-for-mysql/ai-capability-center.md)

- [自研内核AliSQL](products/rds/documents/apsaradb-rds-for-mysql/proprietary-alisql.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-mysql/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-mysql/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-mysql/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-mysql/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-mysql/support.md)

[首页](https://help.aliyun.com/zh)

# RDS MySQL标准版（原X86）主实例规格列表

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍RDS MySQL标准版（原X86）的主实例规格，帮助您了解RDS MySQL主实例的最新规格信息和历史规格信息，您可以查看本文了解各个规格的具体配置。

说明

- 

DuckDB分析实例规格，请参见[DuckDB](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md)[分析主实例规格表](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md)和[DuckDB](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md)[分析只读实例规格表](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md)。

- 

倚天版和标准版的区别，请参见[产品类型](products/rds/documents/product-overview/product-types.md)。

- 

当前规格列表中可能存在部分已下线的规格，请以实际售卖页的规格为准。

- 

[RDS MySQL Serverless](products/rds/documents/apsaradb-rds-for-mysql/rds-mysql-serverless.md)[实例](products/rds/documents/apsaradb-rds-for-mysql/rds-mysql-serverless.md)采用RCU作为资源计量单位，无传统CPU和内存规格概念，但为兼容现有流程仍设置规格码，具体为mysql.n2.serverless.1c（基础系列）和mysql.n2.serverless.2c（高可用系列）。

- 

当前规格列表中部分RDS实例不再提供SSD云盘售卖，提供性能更高的ESSD云盘售卖，详情请参见[【通知】部分](products/rds/documents/apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[RDS](products/rds/documents/apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[实例不再提供](products/rds/documents/apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[SSD](products/rds/documents/apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[云盘售卖](products/rds/documents/apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)。

- 

规格列表中的最大连接数表示同时最多可连接RDS MySQL实例的进程数。

- 

如果您在变更规格时，发现无法选择目标规格，可能因为各地域支持的规格有差异，请以实际购买页为准。

- 

RDS MySQL不支持调整公网带宽。

## RDS MySQL基础系列（云盘）

重要

- 

实际最大IOPS：受存储类型、存储空间大小和实例规格共同影响，请参见[最大](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)[IOPS](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)[计算公式](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)。

- 

实际最大IO带宽：受存储类型、存储空间大小和实例规格共同影响，请参见[最大吞吐量计算公式](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)。

- 

- 

- 

- 

| 系列 | 规格族 | 规格代码 | CPU 和内存 | 最大连接数默认值 | 存储 |  |
| --- | --- | --- | --- | --- | --- | --- |
| 实例规格的最大 IOPS | 实例规格的最大 IO 带宽（MB/s） | 存储空间 |  |  |  |  |
| 基础系列 | 通用型 | mysql.n2.medium.1 | 2 核 4GB | 4000 | 通用型无法保证最大 IOPS 和最大 IO 带宽。如果业务对 IOPS 敏感，建议选择高可用系列独享型。 | ESSD PL0 云盘：10 GB~32000 GB ESSD PL1 云盘：20 GB~64000 GB 高性能云盘：10 GB~64000 GB SSD 云盘：20 GB~6000 GB |
| mysql.n4.medium.1 | 2 核 8GB | 6000 |  |  |  |  |
| mysql.n2.large.1 | 4 核 8GB | 6000 |  |  |  |  |
| mysql.n4.large.1 | 4 核 16GB | 8000 |  |  |  |  |
| mysql.n2.xlarge.1 | 8 核 16GB | 8000 |  |  |  |  |
| mysql.n4.xlarge.1 | 8 核 32GB | 10000 |  |  |  |  |


## RDS MySQL高可用系列（云盘）

重要

- 

实际最大IOPS：受存储类型、存储空间大小和实例规格共同影响，请参见[最大](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)[IOPS](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)[计算公式](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)。

- 

实际最大IO带宽：受存储类型、存储空间大小和实例规格共同影响，请参见[最大吞吐量计算公式](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)。

- 

- 

- 

- 

- 

| 系列 | 规格族 | 规格代码 | CPU 和内存 | 最大连接数默认值 | 存储 |  |
| --- | --- | --- | --- | --- | --- | --- |
| 实例规格的最大 IOPS | 实例规格的最大 IO 带宽（MB/s） | 存储空间 |  |  |  |  |
| 高可用系列 | 通用型 | mysql.n2.small.2c | 1 核 2GB | 2000 | 通用型无法保证最大 IOPS 和最大 IO 带宽。如果业务对 IOPS 敏感，建议选择独享型。 | ESSD PL1 云盘：20 GB~64000 GB ESSD PL2 云盘：500 GB~64000 GB ESSD PL3 云盘：1500 GB~64000 GB 高性能云盘：10 GB~64000 GB SSD 云盘：20 GB~6000 GB 说明 RDS MySQL 支持在存储空间达到阈值时自动进行扩容，详情请参见 [存储/性能自动扩容](products/rds/documents/apsaradb-rds-for-mysql/automatic-expansion-of-cloud-disk.md) 。 |
| mysql.n2.medium.2c | 2 核 4GB | 4000 |  |  |  |  |
| mysql.n4.medium.2c | 2 核 8GB | 6000 |  |  |  |  |
| mysql.n8.medium.2c | 2 核 16GB | 8000 |  |  |  |  |
| mysql.n2.large.2c | 4 核 8GB | 6000 |  |  |  |  |
| mysql.n4.large.2c | 4 核 16GB | 8000 |  |  |  |  |
| mysql.n8.large.2c | 4 核 32GB | 12000 |  |  |  |  |
| mysql.n2.xlarge.2c | 8 核 16GB | 8000 |  |  |  |  |
| mysql.n4.xlarge.2c | 8 核 32GB | 10000 |  |  |  |  |
| mysql.n8.xlarge.2c | 8 核 64GB | 16000 |  |  |  |  |
| 独享型 | mysql.x2.medium.2c | 2 核 4GB | 4000 | 10000 | 125 |  |
| mysql.x4.medium.2c | 2 核 8GB | 6000 |  |  |  |  |
| mysql.x8.medium.2c | 2 核 16GB | 8000 |  |  |  |  |
| mysql.x2.large.2c | 4 核 8GB | 6000 | 20000 | 187.5 |  |  |
| mysql.x4.large.2c | 4 核 16GB | 8000 |  |  |  |  |
| mysql.x8.large.2c | 4 核 32GB | 12000 |  |  |  |  |
| mysql.x2.xlarge.2c | 8 核 16GB | 8000 | 25000 | 250 |  |  |
| mysql.x4.xlarge.2c | 8 核 32GB | 10000 |  |  |  |  |
| mysql.x8.xlarge.2c | 8 核 64GB | 16000 |  |  |  |  |
| mysql.x2.3large.2c | 12 核 24GB | 12000 | 30000 | 312.5 |  |  |
| mysql.x4.3large.2c | 12 核 48GB | 15000 |  |  |  |  |
| mysql.x8.3large.2c | 12 核 96GB | 24000 |  |  |  |  |
| mysql.x2.2xlarge.2c | 16 核 32GB | 16000 | 40000 | 375 |  |  |
| mysql.x4.2xlarge.2c | 16 核 64GB | 20000 |  |  |  |  |
| mysql.x8.2xlarge.2c | 16 核 128GB | 32000 |  |  |  |  |
| mysql.x2.3xlarge.2c | 24 核 48GB | 24000 | 50000 | 500 |  |  |
| mysql.x4.3xlarge.2c | 24 核 96GB | 30000 |  |  |  |  |
| mysql.x8.3xlarge.2c | 24 核 192GB | 48000 |  |  |  |  |
| mysql.x2.4xlarge.2c | 32 核 64GB | 32000 | 60000 | 625 |  |  |
| mysql.x4.4xlarge.2c | 32 核 128GB | 40000 |  |  |  |  |
| mysql.x8.4xlarge.2c | 32 核 256GB | 64000 |  |  |  |  |
| mysql.x2.13large.2c | 52 核 96GB | 52000 | 100000 | 1000 |  |  |
| mysql.x4.13large.2c | 52 核 192GB | 65000 |  |  |  |  |
| mysql.x8.13large.2c | 52 核 384GB | 104000 |  |  |  |  |
| mysql.x2.8xlarge.2c | 64 核 128GB | 64000 | 120000 | 1025 |  |  |
| mysql.x4.8xlarge.2c | 64 核 256GB | 80000 | 150000 | 1025 |  |  |
| mysql.x8.8xlarge.2c | 64 核 512GB | 128000 | 150000 | 1000 |  |  |
| mysql.x2.13xlarge.2c | 104 核 192GB | 104000 | 200000 | 2000 |  |  |
| mysql.x4.13xlarge.2c | 104 核 384GB | 130000 |  |  |  |  |
| mysql.x8.13xlarge.2c | 104 核 768GB | 208000 |  |  |  |  |
| mysql.x4.16xlarge.2c | 128 核 512GB | 128000 | 300000 | 2560 |  |  |


## RDS MySQL集群系列（云盘）

RDS MySQL集群系列实例当前支持5.7和8.0版本。

重要

- 

集群系列实例除了阿联酋（迪拜）、华东5 （南京-本地地域-关停中）、华东6（福州-本地地域-关停中）外，其他地域均已上线。未上线的地域也将陆续上线，请以实际上线时间为准。

- 

实际最大IOPS：受存储类型、存储空间大小和实例规格共同影响，请参见[最大](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)[IOPS](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)[计算公式](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)。

- 

实际最大IO带宽：受存储类型、存储空间大小和实例规格共同影响，请参见[最大吞吐量计算公式](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)。

- 

- 

- 

- 

| 系列 | 规格族 | 规格代码 | CPU 和内存 | 最大连接数默认值 | 存储 |  |
| --- | --- | --- | --- | --- | --- | --- |
| 实例规格的最大 IOPS | 实例规格的最大 IO 带宽（MB/s） | 存储空间 |  |  |  |  |
| 集群系列 | 通用型 | mysql.n2.small.xc | 1 核 2GB | 2200 | 通用型无法保证最大 IOPS 和最大 IO 带宽。如果业务对 IOPS 敏感，建议选择独享型。 | ESSD PL1 云盘：20 GB~64000 GB ESSD PL2 云盘：500 GB~64000 GB ESSD PL3 云盘：1500 GB~64000 GB 高性能云盘：10 GB~64000 GB 说明 RDS MySQL 支持在存储空间达到阈值时自动进行扩容，详情请参见 [存储/性能自动扩容](products/rds/documents/apsaradb-rds-for-mysql/automatic-expansion-of-cloud-disk.md) 。 |
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
| mysql.x8.medium.xc | 2 核 16GB | 8000 |  |  |  |  |
| mysql.x2.large.xc | 4 核 8GB | 6000 | 20000 | 187.5 |  |  |
| mysql.x4.large.xc | 4 核 16GB | 8000 |  |  |  |  |
| mysql.x8.large.xc | 4 核 32GB | 12000 |  |  |  |  |
| mysql.x2.xlarge.xc | 8 核 16GB | 12000 | 25000 | 250 |  |  |
| mysql.x4.xlarge.xc | 8 核 32GB | 12000 |  |  |  |  |
| mysql.x8.xlarge.xc | 8 核 64GB | 16000 |  |  |  |  |
| mysql.x2.3large.xc | 12 核 24GB | 12000 | 30000 | 312.5 |  |  |
| mysql.x4.3large.xc | 12 核 48GB | 15000 |  |  |  |  |
| mysql.x8.3large.xc | 12 核 96GB | 24000 |  |  |  |  |
| mysql.x2.2xlarge.xc | 16 核 32GB | 16000 | 40000 | 375 |  |  |
| mysql.x4.2xlarge.xc | 16 核 64GB | 20000 |  |  |  |  |
| mysql.x8.2xlarge.xc | 16 核 128GB | 32000 |  |  |  |  |
| mysql.x2.3xlarge.xc | 24 核 48GB | 24000 | 50000 | 500 |  |  |
| mysql.x4.3xlarge.xc | 24 核 96GB | 30000 |  |  |  |  |
| mysql.x8.3xlarge.xc | 24 核 192GB | 48000 |  |  |  |  |
| mysql.x2.4xlarge.xc | 32 核 64GB | 32000 | 60000 | 625 |  |  |
| mysql.x4.4xlarge.xc | 32 核 128GB | 40000 |  |  |  |  |
| mysql.x8.4xlarge.xc | 32 核 256GB | 64000 |  |  |  |  |
| mysql.x2.13large.xc | 52 核 96GB | 52000 | 100000 | 1000 |  |  |
| mysql.x4.13large.xc | 52 核 192GB | 65000 |  |  |  |  |
| mysql.x8.13large.xc | 52 核 384GB | 104000 |  |  |  |  |
| mysql.x2.8xlarge.xc | 64 核 128GB | 64000 | 120000 | 1025 |  |  |
| mysql.x4.8xlarge.xc | 64 核 256GB | 80000 | 150000 | 1025 |  |  |
| mysql.x8.8xlarge.xc | 64 核 512GB | 128000 | 150000 | 1000 |  |  |
| mysql.x2.13xlarge.xc | 104 核 192GB | 104000 | 200000 | 2000 |  |  |
| mysql.x4.13xlarge.xc | 104 核 384GB | 130000 |  |  |  |  |
| mysql.x8.13xlarge.xc | 104 核 768GB | 208000 |  |  |  |  |


## RDS MySQL高可用系列（高性能本地盘）

自北京时间 2025年09月19日起，RDS MySQL高性能本地盘部分独享型实例提升了默认最大连接数和最大IOPS。详情请参见[【产品/功能变更】提升](products/rds/documents/apsaradb-rds-for-mysql/the-default-maximum-number-of-connections-and-maximum-iops-of-apsaradb-rds-for-mysql-instances-with-premium-local-ssds-are-increased.md)[RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/the-default-maximum-number-of-connections-and-maximum-iops-of-apsaradb-rds-for-mysql-instances-with-premium-local-ssds-are-increased.md)[高性能本地盘实例默认最大连接数和最大](products/rds/documents/apsaradb-rds-for-mysql/the-default-maximum-number-of-connections-and-maximum-iops-of-apsaradb-rds-for-mysql-instances-with-premium-local-ssds-are-increased.md)[IOPS](products/rds/documents/apsaradb-rds-for-mysql/the-default-maximum-number-of-connections-and-maximum-iops-of-apsaradb-rds-for-mysql-instances-with-premium-local-ssds-are-increased.md)。

- 

- 

| 系列 | 规格族 | 规格代码 | CPU 和内存 | 最大连接数默认值 | 存储 |  |
| --- | --- | --- | --- | --- | --- | --- |
| 实例规格的最大 IOPS | 存储空间 |  |  |  |  |  |
| 高可用系列 | 通用型 | rds.mysql.t1.small | 1 核 1GB | 300 | 1200 | 5 GB~4000 GB |
| rds.mysql.s1.small | 1 核 2GB | 600 | 2000 |  |  |  |
| rds.mysql.s2.large | 2 核 4GB | 1200 | 4000 |  |  |  |
| rds.mysql.s2.xlarge | 2 核 8GB | 2000 | 6000 |  |  |  |
| rds.mysql.s3.large | 4 核 8GB | 2000 | 8000 |  |  |  |
| rds.mysql.m1.medium | 4 核 16GB | 4000 | 14000 |  |  |  |
| rds.mysql.c1.large | 8 核 16GB | 4000 | 20000 | 5 GB~5000 GB |  |  |
| rds.mysql.c1.xlarge | 8 核 32GB | 8000 | 28000 |  |  |  |
| rds.mysql.c2.xlarge | 16 核 64GB | 16000 | 40000 | 20 GB~12000 GB |  |  |
| rds.mysql.c2.xlp2 | 16 核 96GB | 24000 | 40000 |  |  |  |
| 独享型 | mysql.x2.medium.2 | 2 核 4GB | 4000 | 15000 | 20 GB~4000 GB |  |
| mysql.x4.medium.2 | 2 核 8GB | 6000 | 20000 |  |  |  |
| mysql.x6.medium.2 | 2 核 12GB | 7000 | 25000 |  |  |  |
| mysql.x8.medium.2 | 2 核 16GB | 8000 | 30000 |  |  |  |
| mysql.x2.large.2 | 4 核 8GB | 6000 | 30000 |  |  |  |
| mysql.x4.large.2 | 4 核 16GB | 8000 | 40000 |  |  |  |
| mysql.x6.large.2 | 4 核 24GB | 10000 | 40000 |  |  |  |
| mysql.x8.large.2 | 4 核 32GB | 12000 | 60000 |  |  |  |
| mysql.x2.xlarge.2 | 8 核 16GB | 8000 | 45000 | 20 GB~5000 GB |  |  |
| mysql.x4.xlarge.2 | 8 核 32GB | 12000 | 60000 |  |  |  |
| mysql.x6.xlarge.2 | 8 核 48GB | 14000 | 60000 |  |  |  |
| mysql.x8.xlarge.2 | 8 核 64GB | 16000 | 90000 |  |  |  |
| mysql.x2.2xlarge.2 | 16 核 32GB | 12000 | 60000 | 20 GB~12000 GB |  |  |
| mysql.x4.2xlarge.2 | 16 核 64GB | 16000 | 75000 |  |  |  |
| mysql.x6.2xlarge.2 | 16 核 96GB | 24000 | 75000 |  |  |  |
| mysql.x8.2xlarge.2 | 16 核 128GB | 32000 | 105000 |  |  |  |
| mysql.x2.4xlarge.2 | 32 核 64GB | 16000 | 80000 | 5.7、8.0 版本：20 GB~24000 GB（新加坡、中国（香港）地域，最大存储空间为 16000GB） 5.6 版本：20 GB~16000 GB |  |  |
| mysql.x4.4xlarge.2 | 32 核 128GB | 32000 | 105000 |  |  |  |
| mysql.x6.4xlarge.2 | 32 核 192GB | 36000 | 120000 |  |  |  |
| mysql.x8.4xlarge.2 | 32 核 256GB | 40000 | 135000 |  |  |  |
| mysql.x2.8xlarge.2 | 64 核 128GB | 32000 | 140000 |  |  |  |
| mysql.x4.8xlarge.2 | 64 核 256GB | 40000 | 150000 |  |  |  |
| mysql.x6.8xlarge.2 | 64 核 384GB | 60000 | 150000 |  |  |  |
| mysql.x8.8xlarge.2 | 64 核 512GB | 80000 | 150000 |  |  |  |
| mysql.x4.12xlarge.2 | 96 核 384GB | 70000 | 200000 |  |  |  |
| mysql.x6.12xlarge.2 | 96 核 576GB | 90000 | 220000 |  |  |  |
| mysql.x8.12xlarge.2 | 96 核 768GB | 100000 | 240000 |  |  |  |
| 独占物理机型 | rds.mysql.st.h43 | 60 核 470GB | 100000 | 150000 | 20 GB~12000 GB |  |
| rds.mysql.st.v52 | 90 核 720GB | 150000 | 150000 |  |  |  |


## 历史规格RDS MySQL

以下为RDS MySQL历史规格列表。不支持新购历史规格，历史规格可以升级到部分在售规格。不支持历史规格产生新订单，例如：不支持在规格不变的情况下，生成[变更存储](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)空间的订单。建议您使用最新规格。

说明

由于历史规格无法支持部分新特性，建议您升级到最新规格。

| 规格代码 | CPU 核数 | 内存 | 最大连接数 |
| --- | --- | --- | --- |
| rds.mys2.small | 2 | 240MB | 60 |
| rds.mys2.mid | 4 | 600MB | 150 |
| rds.mys2.standard | 6 | 1200MB | 300 |
| rds.mys2.large | 8 | 2400MB | 600 |
| rds.mys2.xlarge | 9 | 6000MB | 1500 |
| rds.mys2.2xlarge | 10 | 12000MB | 2000 |
| rds.mys2.4xlarge | 11 | 24000MB | 2000 |
| rds.mys2.8xlarge | 13 | 48000MB | 2000 |
| rds.mysql.st.d13 | 30 | 220GB | 64000 |
| mysql.x8.medium.3 | 2 | 16GB | 2500 |
| mysql.x4.large.3 | 4 | 16GB | 2500 |
| mysql.x8.large.3 | 4 | 32GB | 5000 |
| mysql.x4.xlarge.3 | 8 | 32GB | 5000 |
| mysql.x8.xlarge.3 | 8 | 64GB | 10000 |
| mysql.x4.2xlarge.3 | 16 | 64GB | 10000 |
| mysql.x8.2xlarge.3 | 16 | 128GB | 20000 |
| mysql.x4.4xlarge.3 | 32 | 128GB | 20000 |
| mysql.x8.4xlarge.3 | 32 | 256GB | 40000 |
| mysql.st.8xlarge.3 | 60 | 470GB | 100000 |
| mysql.n2.2xlarge.1 | 16 | 32GB | 10000 |
| mysql.n4.2xlarge.1 | 16 | 64GB | 15000 |
| mysql.n8.2xlarge.1 | 16 | 128GB | 20000 |
| mysql.x2.3xlarge2c | 24 | 48GB | 24000 |
| mysql.n4.4xlarge.1 | 32 | 128GB | 20000 |
| mysql.n8.4xlarge.1 | 32 | 256GB | 64000 |
| mysql.n4.8xlarge.1 | 56 | 224GB | 64000 |
| mysql.n8.8xlarge.1 | 56 | 480GB | 64000 |
| mysql.n1.micro.1 | 1 | 1GB | 2000 |
| mysql.n2.small.1 | 1 | 2GB | 2000 |


[上一篇：产品规格](products/rds/documents/apsaradb-rds-for-mysql/specifications-2.md)[下一篇：RDS MySQL倚天版（原ARM）主实例规格列表](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types-5.md)

该文章对您有帮助吗？

反馈

### 为什么选择阿里云

[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)

### 大模型

[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)

### 产品和定价

[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)

### 技术内容

[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)

### 权益

[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)

### 服务

[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)

### 关注阿里云

关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务

联系我们：4008013260

[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)

### 友情链接

[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)

© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
