### 默认安装的应用版本及性能提升
默认安装的应用版本及性能提升的说明如下表所示。
倚天实例

| 应用 | 默认安装应用版本 | 测试工具 | 主要指标 | 性能提升比例 |
| --- | --- | --- | --- | --- |
| Nginx | 1.20.1 | wrk | rps（requests per second） | HTTP/HTTPS 小包场景：30% 大包+Gzip 场景：12% |
| MySQL | 8.0.26 | sysbench | qps（queries per second） | 20%（纯读、纯写、混合读写） |
| Redis | 6.0.2 | memtier-benchmark | rps（requests per second） | 25%（单 pipeline 小包场景） |
| PostgreSQL | 13.10-1.0.1 | sysbench | qps（queries per second） | 20%（纯读、纯写、混合读写） |
| Memcached | 1.5.22-2.1 | memtier-benchmark | rps（requests per second） | 10% ~ 20%（单 pipeline 小包场景） |
| x264/x265 | ffmpeg 5.0.1+ x264 0.164.x+ x265 3.5+ | ffmpeg/x264/x265 | fps (frames per second) | x264 编码：20%~30% x265 编码：20%~30% |
| Spark 性能加速扩展 | 3.3 说明 不安装 Spark，仅支持对 Spark 3.3 进行加速。 | TPC-DS | s（second） | 20%~60% |

AMD实例

| 应用 | 默认安装应用版本 | 测试工具 | 主要指标 | 性能提升比例 |
| --- | --- | --- | --- | --- |
| Nginx | 1.20.1 | wrk | rps（requests per second） | HTTP/HTTPS 小包场景：10% |
| MySQL | 8.0.26 | sysbench | qps（queries per second） | 5%（纯读、纯写、混合读写） |
| Memcached | 1.5.22-2.1 | memtier-benchmark | rps（requests per second） | 7%（单 pipeline 小包场景） |

Intel实例
