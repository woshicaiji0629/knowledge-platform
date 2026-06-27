MEDIUM | 2020-11-28 | 新特性 | 合并社区 6.0.9 版本的更新内容，更多信息，请参见 [Redis 6.0 release notes](https://raw.githubusercontent.com/redis/redis/6.0/00-RELEASENOTES) 。 支持槽（slot）的无感迁移能力。 支持通过公网获取虚拟 IP（VIP）地址，为使用 [直连模式](../user-guide/enable-the-direct-connection-mode.md) 客户端提供更好的支持。 |
| 功能优化 | 优化实例健康检查能力，提升在磁盘抖动场景下的主备切换速度。 |  |  |  |
| 6.0.0.5 | HIGH | 2020-08-21 | 缺陷修复 | 修复热点 Key 统计不准确的问题。 |
| 6.0.0.4 | HIGH | 2020-07-20 | 缺陷修复 | 修复部分参数的配置在重启后失效的问题。 修复慢日志对链路中备库标志错误的问题。 |
| 6.0.0.3 | LOW | 2020-06-11 | 新特性 | 合并社区 6.0.5 版本的更新内容，更多信息，请参见 [Redis 6.0 release notes](https://raw.githubusercontent.com/redis/redis/6.0/00-RELEASENOTES) 。 INFO 命令返回值中， Replication 部分支持展示 role 信息（例如 role:master ），可兼容 Redisson 客户端在部分场景下对该信息的调用。 支持对读写命令 QPS 的统计，更多信息，请参见 [查看性能监控](../user-guide/view-monitoring-data.md) 。 |
| 6.0.0.2 | LOW | 2020-06-02 | 新特性 | 合并社区 6.0.4 版本的更新内容，更多信息，请参见 [Redis 6.0 release notes](https://raw.githubusercontent.com/redis/redis/6.0/00-RELEASENOTES) 。 |
| 6.0.0.1 | LOW | 2020-05-06 | 首次发布 | 首次发布的小版本，基于社区 6.0.1 版本，更多信息，请参见 [Redis 6.0 release notes](https://raw.githubusercontent.com/redis/redis/6.0/00-RELEASENOTES) 。 |
