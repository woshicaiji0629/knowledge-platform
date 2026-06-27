| sysbench | qps（queries per second） | 5%（纯读、纯写、混合读写） |
| Memcached | 1.5.22-2.1 | memtier-benchmark | rps（requests per second） | 7%（单 pipeline 小包场景） |

Intel实例

| 应用 | 默认安装应用版本 | 测试工具 | 主要指标 | 性能提升比例 |
| --- | --- | --- | --- | --- |
| MySQL | 8.0.26 | sysbench | qps（queries per second） | 7%（纯读、纯写、混合读写） |

说明
推荐使用默认安装的应用版本，如果后续您自选应用版本，可能无法获取部分优化。优化范围说明如下：
应用本身性能收益（不使用默认安装的应用版本无法获取），包括应用二进制编译和应用配置的优化。
OS相关的性能收益（不使用默认安装的应用版本仍然可以获取），包括boot cmdline、内存配置、网络优化（绑核、XPS、RPS、RFS等）。
