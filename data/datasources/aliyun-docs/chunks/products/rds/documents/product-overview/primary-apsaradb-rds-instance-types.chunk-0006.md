### IO带宽（吞吐量）
IO带宽反映了存储系统连续读写数据的能力，是衡量顺序I/O性能的关键指标。影响实例IO带宽的主要因素为：实例规格、存储类型和存储容量，您可以在[主实例规格表](primary-apsaradb-rds-instance-types.md)中查找对应实例规格的最大IO带宽，但实例的实际IO带宽上限需通过以下内容计算：

| 存储类型 | 云盘实例实际 IO 带宽性能公式（IO 带宽单位：MB/s、存储空间单位：GB） |  |
| --- | --- | --- |
| 高性能云盘 | 开启 [IO](../apsaradb-rds-for-mysql/i-o-performance-burst.md) [性能突发](../apsaradb-rds-for-mysql/i-o-performance-burst.md) | min{实例规格最大 IO 带宽, 4000} |
| 未开启 [IO](../apsaradb-rds-for-mysql/i-o-performance-burst.md) [性能突发](../apsaradb-rds-for-mysql/i-o-performance-burst.md) | min{实例规格最大 IO 带宽, 120+0.5x 存储空间, 350} |  |
| ESSD 云盘 | PL3 | min{实例规格最大 IO 带宽, 120+0.5*存储空间, 4000} |
| PL2 | min{实例规格最大 IO 带宽, 120+0.5*存储空间, 750} |  |
| PL1 | min{实例规格最大 IO 带宽, 120+0.5*存储空间, 350} |  |
| SSD 云盘 | min{实例规格最大 IO 带宽, 120+0.5*存储空间, 300} |  |

示例：以ESSD PL3云盘，实例规格mysql.x2.large.2c，存储空间5000 GB为例，计算该实例的实际IO带宽上限：

| 限制因素 | 说明 |
| --- | --- |
| 实例规格 | 查询主实例规格表， mysql.x2.large.2c 实例规格对应的 IO 带宽上限为 192 。 |
| 存储空间 | 5000 GB 存储空间对应的 IO 带宽上限为 120+0.5*5000=2620 。 |
| 存储类型 | ESSD PL3 云盘对应的 IO 带宽上限为 4000 。 |

该实例实际的IO带宽上限取上述三者间最小值：192（主要受实例规格限制）。
