### IOPS
IOPS反映了存储系统处理读写请求的能力，是衡量随机I/O性能的关键指标。影响实例IOPS的主要因素为：实例规格、存储类型和存储容量，您可以在[各引擎主实例规格表](primary-apsaradb-rds-instance-types.md)中查找对应实例规格的最大IOPS，但实例的实际IOPS上限需通过以下内容计算：
高性能本地盘实例：实际IOPS上限仅受实例规格影响，主实例规格表中的最大IOPS即为实际IOPS上限。
云盘实例：实际IOPS上限受实例规格、存储容量和存储类型三者共同影响，计算公式如下：

| 存储类型 | 实际最大 IOPS 计算公式（存储空间单位：GB） |  |
| --- | --- | --- |
| 高性能云盘 | 开启 [IO](../apsaradb-rds-for-mysql/i-o-performance-burst.md) [性能突发](../apsaradb-rds-for-mysql/i-o-performance-burst.md) | min{实例规格最大 IOPS,1000000} |
| 未开启 [IO](../apsaradb-rds-for-mysql/i-o-performance-burst.md) [性能突发](../apsaradb-rds-for-mysql/i-o-performance-burst.md) | min{实例规格最大 IOPS, 1800+50*存储空间, 50000} |  |
| ESSD 云盘 | PL3 | min{实例规格最大 IOPS, 1800+50*存储空间, 1000000} |
| PL2 | min{实例规格最大 IOPS, 1800+50*存储空间, 100000} |  |
| PL1 | min{实例规格最大 IOPS, 1800+50*存储空间, 50000} |  |
| SSD 云盘 | min{实例规格最大 IOPS, 1800+30*存储空间, 25000} |  |

示例：以ESSD PL1云盘，实例规格mysql.x2.large.2c，存储空间20 GB为例，计算该实例的实际IOPS：

| 限制因素 | 说明 |
| --- | --- |
| 实例规格 | 查询主实例规格表， mysql.x2.large.2c 实例规格对应的 IOPS 上限为 20000 。 |
| 存储空间 | 20 GB 存储空间对应的 IOPS 上限为 1800+50*20=2800 。 |
| 存储类型 | ESSD PL1 云盘对应的 IOPS 上限为 50000 。 |
