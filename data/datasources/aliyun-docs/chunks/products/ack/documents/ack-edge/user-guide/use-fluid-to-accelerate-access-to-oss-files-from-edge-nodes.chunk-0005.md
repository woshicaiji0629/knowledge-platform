| 参数 | 说明 |
| --- | --- |
| mountPoint | oss://<oss_bucket>/<bucket_dir> 表示挂载 UFS 的路径。此路径必须指向一个目录，无法挂载单个文件，并且不需要包含 Endpoint 信息。 |
| fs.oss.endpoint | OSS Bucket 的 Endpoint 信息，公网或私网地址均支持。更多信息，请参见 [地域和](../../../../oss/documents/user-guide/regions-and-endpoints.md) [Endpoint](../../../../oss/documents/user-guide/regions-and-endpoints.md) 。 |
| replicas | 表示创建 JindoFS 集群的 Worker 数量。 |
| mediumtype | 表示缓存类型。在创建 JindoRuntime 模板样例时，JindoFS 暂时只支持 HDD/SSD/MEM 中的其中一种缓存类型。 |
| path | 表示存储路径，暂时只支持单个路径。当选择 MEM 做缓存时，需指定一个本地路径来存储 Log 等文件。 |
| quota | 表示缓存最大容量，单位 GB。 |
| high | 表示存储容量上限大小。 |
| low | 表示存储容量下限大小。 |
