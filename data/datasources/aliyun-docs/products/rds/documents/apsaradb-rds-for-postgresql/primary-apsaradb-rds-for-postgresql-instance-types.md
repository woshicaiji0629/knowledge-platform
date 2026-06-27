# RDS PostgreSQL可购买的规格列表及性能配置-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/primary-apsaradb-rds-for-postgresql-instance-types

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-postgresql/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-postgresql/getting-started.md)

- [DuckDB分析加速](products/rds/documents/apsaradb-rds-for-postgresql/duckdb-analytics-acceleration.md)

- [RDS for AI](products/rds/documents/apsaradb-rds-for-postgresql/rds-for-ai.md)

- [自研内核 AliPG](products/rds/documents/apsaradb-rds-for-postgresql/proprietary-alipg.md)

- [插件](products/rds/documents/apsaradb-rds-for-postgresql/plug-ins-1.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-postgresql/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-postgresql/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-postgresql/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-postgresql/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-postgresql/support.md)

[首页](https://help.aliyun.com/zh)

# RDS PostgreSQL主实例规格列表

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍RDS PostgreSQL主实例规格，帮助您了解RDS PostgreSQL主实例的最新规格信息和历史规格信息。

重要

- 

云盘实例的底层操作系统以及相关管理服务会占用一部分内存，因此实例实际可用的内存不会达到规格显示的内存大小。占用内存详情如下：

- 

底层操作系统：约500~700 MB。

- 

RDS相关管理服务：约500 MB。

- 

RDS PostgreSQL云盘实例只支持专有网络，创建实例时，网络类型请配置为专有网络。如果使用API配置，参数InstanceNetworkType必须配置为VPC，更多信息，请参见[创建一个](products/rds/documents/api-create-an-instance.md)[RDS](products/rds/documents/api-create-an-instance.md)[实例](products/rds/documents/api-create-an-instance.md)。

## 规格清单

重要

- 

标准版和倚天版的区别，请参见[产品类型](products/rds/documents/product-overview/product-types.md)。

- 

实际最大IOPS：受存储类型、存储空间大小和实例规格共同影响，详情请参见[最大](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)[IOPS](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)[计算公式](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)。

- 

实际最大吞吐量：受存储类型、存储空间大小和实例规格共同影响，详情请参见[最大吞吐量计算公式](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md)。

### 基础系列规格

标准版规格

- 

- 

- 

- 

| 规格族 | 规格代码 | CPU 和内存 | 最大连接数 | 最大 IOPS | 最大 IO 带宽 （MB/s） | 存储空间 |
| --- | --- | --- | --- | --- | --- | --- |
| 通用型 | pg.n2.1c.1m | 1 核 2GB | 取决于云盘性能 | 无法保证最大 IOPS 和最大 IO 带宽。如果业务对 IOPS 敏感，建议选择独享型。 | ESSD PL1 云盘：20 GB~64000 GB ESSD PL2 云盘：500 GB~64000 GB ESSD PL3 云盘：1500 GB~64000 GB 高性能云盘：10 GB~64000 GB |  |
| pg.n1e.2c.1m | 2 核 2GB | 200 |  |  |  |  |
| pg.n2e.1c.1m | 1 核 2GB | 50 |  |  |  |  |
| pg.n2e.2c.1m | 2 核 4GB | 400 |  |  |  |  |
| pg.n2.2c.1m | 2 核 4GB | 400 |  |  |  |  |
| pg.n4.2c.1m | 2 核 8GB | 800 |  |  |  |  |
| pg.n2.4c.1m | 4 核 8GB | 800 |  |  |  |  |
| pg.n4.4c.1m | 4 核 16GB | 1600 |  |  |  |  |
| pg.n4.6c.1m | 6 核 24GB | 2400 |  |  |  |  |
| 独享型 | pg.x8.medium.1 | 2 核 16GB | 1600 | 10000 | 128 |  |
| pg.x8.large.1 | 4 核 32GB | 3200 | 20000 | 192 |  |  |
| pg.x8.xlarge.1 | 8 核 64GB | 6400 | 25000 | 256 |  |  |
| pg.x4.2xlarge.1 | 16 核 64GB | 6400 | 40000 | 384 |  |  |
| pg.x8.2xlarge.1 | 16 核 128GB | 12800 | 40000 | 384 |  |  |
| pg.x4.4xlarge.1 | 32 核 128GB | 12800 | 60000 | 640 |  |  |
| pg.x8.4xlarge.1 | 32 核 256GB | 25600 | 60000 | 640 |  |  |


倚天版规格

如果需要购买倚天版规格，您必须满足以下条件：

- 

实例大版本：RDS PostgreSQL 13或以上版本。

- 

实例存储类型为：ESSD云盘和高性能云盘。

- 

实例地域为（仅部分可用区）：华东1（杭州）、华东2（上海）、华北2（北京）、华北3（张家口）、华南1（深圳）和新加坡。

当前倚天版规格支持的地域较少，更多地域及可用区逐步支持中，具体请以购买页为准。

重要

- 

基础系列倚天版规格主要用于测试与环境验证，不支持将其他规格变更为此类规格。

- 

基础系列倚天版的规格相对较小，如需在生产环境中使用，建议[升级配置](products/rds/documents/apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)至基础系列的更高规格，或选择升级至[高可用系列](products/rds/documents/apsaradb-rds-for-postgresql/upgrade-an-apsaradb-rds-for-postgresql-instance-from-basic-edition-to-high-availability-edition.md)及[集群系列](products/rds/documents/apsaradb-rds-for-postgresql/upgrade-the-rds-edition-from-rds-basic-edition-or-rds-high-availability-edition-to-rds-cluster-edition.md)。

- 

- 

- 

- 

- 

| 规格族 | 规格代码 | CPU 和内存 | 最大连接数 | 最大 IOPS | 最大 IO 带宽 （MB/s） | 存储空间 |
| --- | --- | --- | --- | --- | --- | --- |
| 通用型 | pg.n1e.1c.1m | 1 核 1GB | 20 | 无法保证最大 IOPS 和最大 IO 带宽。如果业务对 IOPS 敏感，建议选择 基础系列标准版独享型 或 高可用系列倚天版独享型 规格。 | ESSD PL0 云盘：10 GB~30000 GB ESSD PL1 云盘：20 GB~64000 GB ESSD PL2 云盘：500 GB~64000 GB ESSD PL3 云盘：1500 GB~64000 GB 高性能云盘：10 GB~64000 GB |  |
| pg.n2e.1c.1m | 1 核 2GB | 50 |  |  |  |  |
| pg.n1e.2c.1m | 2 核 2GB | 200 |  |  |  |  |
| pg.n2e.2c.1m | 2 核 4GB | 400 |  |  |  |  |


### 高可用系列规格

标准版规格

常规规格

- 

- 

- 

- 

| 规格族 | 规格代码 | CPU 和内存 | 最大连接数 | 最大 IOPS | 最大 IO 带宽 （MB/s） | 存储空间 |
| --- | --- | --- | --- | --- | --- | --- |
| 通用型 | pg.n2.2c.2m | 2 核 4GB | 400 | 无法保证最大 IOPS 和最大 IO 带宽。如果业务对 IOPS 敏感，建议选择独享型。 | ESSD PL1 云盘：20 GB~64000 GB ESSD PL2 云盘：500 GB~64000 GB ESSD PL3 云盘：1500 GB~64000 GB 高性能云盘：10 GB~64000 GB |  |
| pg.n2.4c.2m | 4 核 8GB | 800 |  |  |  |  |
| pg.n2.8c.2m | 8 核 16GB | 1600 |  |  |  |  |
| pg.n4.2c.2m | 2 核 8GB | 800 |  |  |  |  |
| pg.n4.4c.2m | 4 核 16GB | 1600 |  |  |  |  |
| pg.n4.6c.2m | 6 核 24GB | 2400 |  |  |  |  |
| pg.n4.8c.2m | 8 核 32GB | 3200 |  |  |  |  |
| pg.n4.12c.2m | 12 核 48GB | 4800 |  |  |  |  |
| 独享型 | pg.x2.medium.2c | 2 核 4GB | 400 | 10000 | 128 |  |
| pg.x4.medium.2c | 2 核 8GB | 800 | 10000 | 128 |  |  |
| pg.x8.medium.2c | 2 核 16GB | 1600 | 10000 | 128 |  |  |
| pg.x2.large.2c | 4 核 8GB | 800 | 20000 | 192 |  |  |
| pg.x4.large.2c | 4 核 16GB | 1600 | 20000 | 192 |  |  |
| pg.x8.large.2c | 4 核 32GB | 3200 | 20000 | 192 |  |  |
| pg.x2.xlarge.2c | 8 核 16GB | 1600 | 25000 | 256 |  |  |
| pg.x4.xlarge.2c | 8 核 32GB | 3200 | 25000 | 256 |  |  |
| pg.x8.xlarge.2c | 8 核 64GB | 6400 | 25000 | 256 |  |  |
| pg.x2.3large.2c | 12 核 24GB | 2400 | 30000 | 320 |  |  |
| pg.x4.3large.2c | 12 核 48GB | 4800 | 30000 | 320 |  |  |
| pg.x8.3large.2c | 12 核 96GB | 9600 | 30000 | 320 |  |  |
| pg.x2.2xlarge.2c | 16 核 32GB | 3200 | 40000 | 384 |  |  |
| pg.x4.2xlarge.2c | 16 核 64GB | 6400 | 40000 | 384 |  |  |
| pg.x8.2xlarge.2c | 16 核 128GB | 12800 | 40000 | 384 |  |  |
| pg.x2.3xlarge2c | 24 核 48GB | 4800 | 50000 | 512 |  |  |
| pg.x4.3xlarge.2c | 24 核 96GB | 9600 | 50000 | 512 |  |  |
| pg.x8.3xlarge.2c | 24 核 192GB | 19200 | 50000 | 512 |  |  |
| pg.x2.4xlarge.2c | 32 核 64GB | 6400 | 60000 | 640 |  |  |
| pg.x4.4xlarge.2c | 32 核 128GB | 12800 | 60000 | 640 |  |  |
| pg.x8.4xlarge.2c | 32 核 256GB | 25600 | 60000 | 640 |  |  |
| pg.x2.13large.2c | 52 核 96GB | 9600 | 100000 | 1024 |  |  |
| pg.x4.13large.2c | 52 核 192GB | 19200 | 100000 | 1024 |  |  |
| pg.x8.13large.2c | 52 核 384GB | 38400 | 100000 | 1024 |  |  |
| pg.x2.8xlarge.2c | 64 核 128GB | 12800 | 120000 | 1280 |  |  |
| pg.x4.8xlarge.2c | 64 核 256GB | 25600 | 120000 | 1280 |  |  |
| pg.x8.8xlarge.2c | 64 核 512GB | 51200 | 120000 | 1280 |  |  |
| pg.x2.12xlarge.2c | 96 核 192GB | 19200 | 240000 | 2048 |  |  |
| pg.x4.12xlarge.2c | 96 核 384GB | 38400 | 240000 | 2048 |  |  |
| pg.x8.12xlarge.2c | 96 核 768GB | 76800 | 240000 | 2048 |  |  |
| pg.x2.13xlarge.2c | 104 核 192GB | 19200 | 200000 | 2048 |  |  |
| pg.x4.13xlarge.2c | 104 核 384GB | 38400 | 200000 | 2048 |  |  |
| pg.x8.13xlarge.2c | 104 核 768GB | 76800 | 200000 | 2048 |  |  |
| pg.x2.16xlarge.2c | 128 核 256GB | 25600 | 320000 | 2560 |  |  |
| pg.x4.16xlarge.2c | 128 核 512GB | 51200 | 320000 | 2560 |  |  |
| pg.x8.16xlarge.2c | 128 核 1024GB | 102400 | 320000 | 2560 |  |  |
| pg.x2.24xlarge.2c | 192 核 384GB | 38400 | 500000 | 4096 |  |  |
| pg.x4.24xlarge.2c | 192 核 768GB | 76800 | 500000 | 4096 |  |  |
| pg.x8.24xlarge.2c | 192 核 1536GB | 153600 | 500000 | 4096 |  |  |


Intel SGX 安全增强型规格

RDS PostgreSQL提供全密态数据库（硬件加固版）功能，开启此功能，您可以对数据库表中的敏感数据列进行加密，这些列中的敏感数据将以密文进行传输、计算和存储。全密态数据库（硬件加固版）功能可以利用安全增强型规格为用户提供基于可信执行环境的数据安全保护。全密态数据库（硬件加固版）功能的使用方法，请参见[全密态数据库](products/rds/documents/overview.md)。

说明

Intel SGX 安全增强型规格正在如下地域售卖中：

| 地域 | 可用区 |
| --- | --- |
| 华东 1（杭州） | 可用区 K |
| 华东 2（上海） | 可用区 B 和可用区 L |
| 华北 2（北京） | 可用区 I 和可用区 K |
| 中国（香港） | 可用区 B 和可用区 D |


- 

- 

- 

- 

| 系列 | 规格族 | 规格代码 | CPU 和内存 | 加密内存 | 最大连接数 | 最大 IOPS | 存储空间 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 高可用系列 | Intel SGX 安全增强 | pg.x4t.medium.2c | 2 核 8GB | 4GB | 400 | 见 [IOPS](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md) 。 | ESSD PL1 云盘：20 GB~64000 GB ESSD PL2 云盘：500 GB~64000 GB ESSD PL3 云盘：1500 GB~64000 GB 高性能云盘：10 GB~64000 GB |
| pg.x4t.large.2c | 4 核 16GB | 8GB | 800 |  |  |  |  |
| pg.x4t.xlarge.2c | 8 核 32GB | 16GB | 1600 |  |  |  |  |
| pg.x4t.2xlarge.2c | 16 核 64GB | 32GB | 3200 |  |  |  |  |
| pg.x4t.4xlarge.2c | 32 核 128GB | 64GB | 6400 |  |  |  |  |


倚天版规格

如果需要购买倚天版规格，您必须满足以下条件：

- 

实例大版本：RDS PostgreSQL 13或以上版本。

- 

实例存储类型为：ESSD PL1、ESSD PL2或ESSD PL3云盘。

- 

实例地域为：华东1（杭州）、华东2（上海）、华北2（北京）、华北3（张家口）、华南1（深圳）和新加坡。

说明

当前倚天版规格支持的地域较少，更多地域及可用区逐步支持中，具体请以购买页为准。

注意事项

- 

当前倚天版规格暂不支持[Babelfish for RDS PostgreSQL](https://help.aliyun.com/zh/document_detail/428613.html)功能。

- 

RDS PostgreSQL实例支持将标准版规格变更为倚天版规格，更多信息，请参见[变更配置](products/rds/documents/apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)。

规格列表

- 

- 

- 

- 

| 系列 | 规格族 | 规格代码 | CPU 和内存 | 最大连接数 | 最大 IOPS | 最大 IO 带宽 （MB/s） | 存储空间 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 高可用系列 | 通用型 | pg.n4m.2c.2m | 2 核 8GB | 800 | 无法保证最大 IOPS 和最大 IO 带宽。如果业务对 IOPS 敏感，建议选择独享型。 | ESSD PL1 云盘：20 GB~64000 GB ESSD PL2 云盘：500 GB~64000 GB ESSD PL3 云盘：1500 GB~64000 GB 高性能云盘：10 GB~64000 GB |  |
| pg.n4m.4c.2m | 4 核 16GB | 1600 |  |  |  |  |  |
| pg.n4m.8c.2m | 8 核 32GB | 3200 |  |  |  |  |  |
| pg.n2m.2c.2m | 2 核 4GB | 400 |  |  |  |  |  |
| pg.n2m.4c.2m | 4 核 8GB | 800 |  |  |  |  |  |
| pg.n2m.8c.2m | 8 核 16GB | 1600 |  |  |  |  |  |
| 独享型 | pg.x2m.medium.2c | 2 核 4GB | 400 | 20000 | 192 |  |  |
| pg.x4m.medium.2c | 2 核 8GB | 800 | 20000 | 192 |  |  |  |
| pg.x8m.medium.2c | 2 核 16GB | 1600 | 20000 | 192 |  |  |  |
| pg.x2m.large.2c | 4 核 8GB | 800 | 40000 | 256 |  |  |  |
| pg.x4m.large.2c | 4 核 16GB | 1600 | 40000 | 256 |  |  |  |
| pg.x8m.large.2c | 4 核 32GB | 3200 | 40000 | 256 |  |  |  |
| pg.x2m.xlarge.2c | 8 核 16GB | 1600 | 50000 | 384 |  |  |  |
| pg.x4m.xlarge.2c | 8 核 32GB | 3200 | 50000 | 384 |  |  |  |
| pg.x8m.xlarge.2c | 8 核 64GB | 6400 | 50000 | 384 |  |  |  |
| pg.x2m.2xlarge.2c | 16 核 32GB | 3200 | 80000 | 640 |  |  |  |
| pg.x4m.2xlarge.2c | 16 核 64GB | 6400 | 80000 | 640 |  |  |  |
| pg.x8m.2xlarge.2c | 16 核 128GB | 12800 | 80000 | 640 |  |  |  |
| pg.x2m.4xlarge.2c | 32 核 64GB | 6400 | 125000 | 1024 |  |  |  |
| pg.x4m.4xlarge.2c | 32 核 128GB | 12800 | 125000 | 1024 |  |  |  |
| pg.x8m.4xlarge.2c | 32 核 256GB | 25600 | 125000 | 1024 |  |  |  |
| pg.x2m.8xlarge.2c | 64 核 128GB | 12800 | 240000 | 2048 |  |  |  |
| pg.x4m.8xlarge.2c | 64 核 256GB | 25600 | 240000 | 2048 |  |  |  |
| pg.x8m.8xlarge.2c | 64 核 512GB | 51200 | 240000 | 2048 |  |  |  |


### 集群系列规格

标准版规格

常规规格

- 

- 

- 

- 

| 规格族 | 规格代码 | CPU 和内存 | 最大连接数 | 最大 IOPS | 最大 IO 带宽 （MB/s） | 存储空间 |
| --- | --- | --- | --- | --- | --- | --- |
| 通用型 | pg.n2.2c.xc | 2 核 4GB | 400 | 无法保证最大 IOPS 和最大 IO 带宽。如果业务对 IOPS 敏感，建议选择独享型。 | ESSD PL1 云盘：20 GB~64000 GB ESSD PL2 云盘：500 GB~64000 GB ESSD PL3 云盘：1500 GB~64000 GB 高性能云盘：10 GB~64000 GB |  |
| pg.n2.4c.xc | 4 核 8GB | 800 |  |  |  |  |
| pg.n2.8c.xc | 8 核 16GB | 1600 |  |  |  |  |
| pg.n4.2c.xc | 2 核 8GB | 800 |  |  |  |  |
| pg.n4.4c.xc | 4 核 16GB | 1600 |  |  |  |  |
| pg.n4.8c.xc | 8 核 32GB | 3200 |  |  |  |  |
| 独享型 | pg.x2.medium.xc | 2 核 4GB | 400 | 10000 | 128 |  |
| pg.x4.medium.xc | 2 核 8GB | 800 | 10000 | 128 |  |  |
| pg.x8.medium.xc | 2 核 16GB | 1600 | 10000 | 128 |  |  |
| pg.x2.large.xc | 4 核 8GB | 800 | 20000 | 192 |  |  |
| pg.x4.large.xc | 4 核 16GB | 1600 | 20000 | 192 |  |  |
| pg.x8.large.xc | 4 核 32GB | 3200 | 20000 | 192 |  |  |
| pg.x2.xlarge.xc | 8 核 16GB | 1600 | 25000 | 256 |  |  |
| pg.x4.xlarge.xc | 8 核 32GB | 3200 | 25000 | 256 |  |  |
| pg.x8.xlarge.xc | 8 核 64GB | 6400 | 25000 | 256 |  |  |
| pg.x2.3large.xc | 12 核 24GB | 2400 | 30000 | 320 |  |  |
| pg.x4.3large.xc | 12 核 48GB | 4800 | 30000 | 320 |  |  |
| pg.x8.3large.xc | 12 核 96GB | 9600 | 30000 | 320 |  |  |
| pg.x2.2xlarge.xc | 16 核 32GB | 3200 | 40000 | 384 |  |  |
| pg.x4.2xlarge.xc | 16 核 64GB | 6400 | 40000 | 384 |  |  |
| pg.x8.2xlarge.xc | 16 核 128GB | 12800 | 40000 | 384 |  |  |
| pg.x2.3xlarge.xc | 24 核 48GB | 4800 | 50000 | 512 |  |  |
| pg.x4.3xlarge.xc | 24 核 96GB | 9600 | 50000 | 512 |  |  |
| pg.x8.3xlarge.xc | 24 核 192GB | 19200 | 50000 | 512 |  |  |
| pg.x2.4xlarge.xc | 32 核 64GB | 6400 | 60000 | 640 |  |  |
| pg.x4.4xlarge.xc | 32 核 128GB | 12800 | 60000 | 640 |  |  |
| pg.x8.4xlarge.xc | 32 核 256GB | 25600 | 60000 | 640 |  |  |
| pg.x2.13large.xc | 52 核 96GB | 9600 | 100000 | 1024 |  |  |
| pg.x4.13large.xc | 52 核 192GB | 19200 | 100000 | 1024 |  |  |
| pg.x8.13large.xc | 52 核 384GB | 38400 | 100000 | 1024 |  |  |
| pg.x2.8xlarge.xc | 64 核 128GB | 12800 | 120000 | 1280 |  |  |
| pg.x4.8xlarge.xc | 64 核 256GB | 25600 | 120000 | 1280 |  |  |
| pg.x8.8xlarge.xc | 64 核 512GB | 51200 | 120000 | 1280 |  |  |
| pg.x2.12xlarge.xc | 96 核 192GB | 9200 | 240000 | 2048 |  |  |
| pg.x4.12xlarge.xc | 96 核 384GB | 38400 | 240000 | 2048 |  |  |
| pg.x8.12xlarge.xc | 96 核 768GB | 76800 | 240000 | 2048 |  |  |
| pg.x2.13xlarge.xc | 104 核 192GB | 19200 | 200000 | 2048 |  |  |
| pg.x4.13xlarge.xc | 104 核 384GB | 38400 | 200000 | 2048 |  |  |
| pg.x8.13xlarge.xc | 104 核 768GB | 76800 | 200000 | 2048 |  |  |
| pg.x2.16xlarge.xc | 128 核 256GB | 25600 | 320000 | 2560 |  |  |
| pg.x4.16xlarge.xc | 128 核 512GB | 51200 | 320000 | 2560 |  |  |
| pg.x8.16xlarge.xc | 128 核 1024GB | 102400 | 320000 | 2560 |  |  |
| pg.x2.24xlarge.xc | 192 核 384GB | 38400 | 500000 | 4096 |  |  |
| pg.x4.24xlarge.xc | 192 核 768GB | 76800 | 500000 | 4096 |  |  |
| pg.x8.24xlarge.xc | 192 核 1536GB | 153600 | 500000 | 4096 |  |  |


倚天版规格

如果需要购买倚天版规格，您必须满足以下条件：

- 

实例大版本：RDS PostgreSQL 14或以上版本。

- 

实例存储类型为：ESSD PL1、ESSD PL2或ESSD PL3云盘。

- 

实例地域为：华东1（杭州）、华东2（上海）、华北2（北京）、华北3（张家口）、华南1（深圳）和新加坡。

说明

当前倚天版规格支持的地域较少，更多地域及可用区正在逐步支持中，具体请以购买页为准。

注意事项

- 

当前倚天版规格暂不支持[Babelfish for RDS PostgreSQL](https://help.aliyun.com/zh/document_detail/428613.html)功能。

- 

RDS PostgreSQL实例支持将标准版规格变更为倚天版规格，更多信息，请参见[变更配置](products/rds/documents/apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)。

规格列表

- 

- 

- 

- 

| 系列 | 规格族 | 规格代码 | CPU 和内存 | 最大连接数 | 最大 IOPS | 最大 IO 带宽 （MB/s） | 存储空间 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 集群系列 | 通用型 | pg.n4e.2c.xc | 2 核 8GB | 800 | 无法保证最大 IOPS 和最大 IO 带宽。如果业务对 IOPS 敏感，建议选择独享型。 | ESSD PL1 云盘：20 GB~64000 GB ESSD PL2 云盘：500 GB~64000 GB ESSD PL3 云盘：1500 GB~64000 GB 高性能云盘：10 GB~64000 GB |  |
| pg.n4e.4c.xc | 4 核 16GB | 1600 |  |  |  |  |  |
| pg.n4e.8c.xc | 8 核 32GB | 3200 |  |  |  |  |  |
| pg.n2e.2c.xc | 2 核 4GB | 400 |  |  |  |  |  |
| pg.n2e.4c.xc | 4 核 8GB | 800 |  |  |  |  |  |
| pg.n2e.8c.xc | 8 核 16GB | 1600 |  |  |  |  |  |
| 独享型 | pg.x2e.medium.xc | 2 核 4GB | 400 | 20000 | 192 |  |  |
| pg.x4e.medium.xc | 2 核 8GB | 800 | 20000 | 192 |  |  |  |
| pg.x8e.medium.xc | 2 核 16GB | 1600 | 20000 | 192 |  |  |  |
| pg.x2e.large.xc | 4 核 8GB | 800 | 40000 | 256 |  |  |  |
| pg.x4e.large.xc | 4 核 16GB | 1600 | 40000 | 256 |  |  |  |
| pg.x8e.large.xc | 4 核 32GB | 3200 | 40000 | 256 |  |  |  |
| pg.x2e.xlarge.xc | 8 核 16GB | 1600 | 50000 | 384 |  |  |  |
| pg.x4e.xlarge.xc | 8 核 32GB | 3200 | 50000 | 384 |  |  |  |
| pg.x8e.xlarge.xc | 8 核 64GB | 6400 | 50000 | 384 |  |  |  |
| pg.x2e.2xlarge.xc | 16 核 32GB | 3200 | 80000 | 640 |  |  |  |
| pg.x4e.2xlarge.xc | 16 核 64GB | 6400 | 80000 | 640 |  |  |  |
| pg.x8e.2xlarge.xc | 16 核 128GB | 12800 | 80000 | 640 |  |  |  |
| pg.x2e.4xlarge.xc | 32 核 64GB | 6400 | 125000 | 1024 |  |  |  |
| pg.x4e.4xlarge.xc | 32 核 128GB | 12800 | 125000 | 1024 |  |  |  |
| pg.x8e.4xlarge.xc | 32 核 256GB | 25600 | 125000 | 1024 |  |  |  |
| pg.x2e.8xlarge.xc | 64 核 128GB | 12800 | 240000 | 2048 |  |  |  |
| pg.x4e.8xlarge.xc | 64 核 256GB | 25600 | 240000 | 2048 |  |  |  |
| pg.x8e.8xlarge.xc | 64 核 512GB | 51200 | 240000 | 2048 |  |  |  |


## 历史规格

以下为RDS PostgreSQL历史规格列表。新申请实例不再提供历史规格，建议您使用最新规格。

历史规格清单

| 规格代码 | CPU 核数 | 内存 | 最大连接数 | 最大 IOPS |
| --- | --- | --- | --- | --- |
| rds.pg.t1.small | 1 | 1 GB | 100 | 600 |
| pg.x8.4xlarge.2 | 32 | 256 GB | 20000 | 50000 |
| pg.n1.micro.1 | 1 | 1 GB | 100 | 见 [IOPS](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md) |
| pg.gn5i-c2g1.large.1 | 2 | 8 GB | 800 |  |
| pg.gn5i-c4g1.xlarge.1 | 4 | 16 GB | 1600 |  |
| pg.gn5i-c8g1.2xlarge.1 | 8 | 32 GB | 3200 |  |
| pg.gn5i-c16g1.4xlarge.1 | 16 | 64 GB | 6400 |  |
| pg.gn5i-c16g1.8xlarge.1 | 32 | 128 GB | 12800 |  |
| pg.gn5i-c28g1.14xlarge.1 | 56 | 224 GB | 22000 |  |
| pg.n2.small.2c | 1 | 2 GB | 200 |  |
| pg.n2.medium.2c | 2 | 4 GB | 400 |  |
| rds.pg.s1.small | 1 | 2 GB | 200 |  |
| pg.n2.small.1 | 1 | 2 GB | 200 |  |
| pg.n4.8xlarge.1 | 64 | 256 GB | 22000 |  |
| pg.n8.8xlarge.1 | 64 | 512 GB | 48000 |  |
| rds.pg.s2.large | 2 | 4 GB | 400 | 2000 |
| rds.pg.s3.large | 4 | 8 GB | 800 | 5000 |
| rds.pg.c1.large | 8 | 16 GB | 1500 | 8000 |
| rds.pg.c1.xlarge | 8 | 32 GB | 2000 | 12000 |
| rds.pg.c2.xlarge | 16 | 64 GB | 2000 | 14000 |
| pg.x8.medium.2 | 2 | 16 GB | 2500 | 4500 |
| pg.x8.large.2 | 4 | 32 GB | 5000 | 9000 |
| pg.x8.xlarge.2 | 8 | 64 GB | 10000 | 18000 |
| pg.x8.2xlarge.2 | 16 | 128 GB | 12000 | 36000 |
| pg.x4.large.2 | 4 | 16 GB | 2500 | 4500 |
| pg.x4.xlarge.2 | 8 | 32 GB | 5000 | 9000 |
| pg.x4.2xlarge.2 | 16 | 64 GB | 10000 | 18000 |
| pg.x4.4xlarge.2 | 32 | 128 GB | 20000 | 36000 |
| rds.pg.st.h43 | 60 | 470 GB | 12000 | 50000 |
| pg.n2.medium.1 | 2 | 4 GB | 400 | 见 [IOPS](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md) |
| pg.n4.medium.1 | 2 | 8 GB | 800 |  |
| pg.n2.large.1 | 4 | 8 GB | 800 |  |
| pg.n4.large.1 | 4 | 16 GB | 1600 |  |
| pg.n2.xlarge.1 | 8 | 16 GB | 1600 |  |
| pg.n4.xlarge.1 | 8 | 32 GB | 3200 |  |
| pg.n2.2xlarge.1 | 16 | 32 GB | 3200 |  |
| pg.n4.2xlarge.1 | 16 | 64 GB | 6400 |  |
| pg.n8.2xlarge.1 | 16 | 128 GB | 10000 |  |
| pg.n4.4xlarge.1 | 32 | 128 GB | 12800 |  |
| pg.n8.4xlarge.1 | 32 | 256 GB | 20000 |  |


[上一篇：产品规格](products/rds/documents/apsaradb-rds-for-postgresql/specifications-1.md)[下一篇：RDS PostgreSQL只读实例规格列表](products/rds/documents/apsaradb-rds-for-postgresql/read-only-apsaradb-rds-for-postgresql-instance-types.md)

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
