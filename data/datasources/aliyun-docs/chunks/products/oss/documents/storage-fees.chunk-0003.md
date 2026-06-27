### 已存储时长容量（本地冗余）

| 计费项 | 计费项 Code | 最小计量单位限制 |
| --- | --- | --- |
| 标准存储（本地冗余）容量 | Storage | 无 （按照实际大小计算） |
| 低频访问（本地冗余）容量 | ChargedDatasize | 64 KB （小于 64 KB，按照 64 KB 计算；大于或等于 64 KB，按照实际大小计算） |
| 归档（本地冗余）容量 | ChargedDatasize |  |
| 冷归档（本地冗余）容量 | ChargedDatasizeCA |  |
| 深度冷归档（本地冗余）容量 | ChargedDatasizeDeepCA |  |
| 无地域属性存储容量 | AnywhereReservedCapacityLRS | 无 （按照实际大小计算） |

由于低频、归档、冷归档以及深度冷归档存储类型有最小计量单位64 KB的限制，会导致Bucket内计费容量大于实际存储容量的情况。如需了解这些存储类型的实际容量以及计费容量，请参见[获取](developer-reference/query-the-storage-capacity-of-a-bucket-1.md)[Bucket](developer-reference/query-the-storage-capacity-of-a-bucket-1.md)[的存储容量](developer-reference/query-the-storage-capacity-of-a-bucket-1.md)。
