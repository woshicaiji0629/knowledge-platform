## 读写分离实例的命令限制
读写分离实例兼容不同的Redis版本，各版本整体的命令支持情况请参见[Redis](commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](commands-supported-by-apsaradb-for-redis-community-edition.md)与[Tair（企业版）命令支持与限制](limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。
由于读写分离实例默认为代理模式，读写分离实例存在代理节点的命令限制，例如代理节点不支持CLIENT INFO、CLIENT ID等命令，详细介绍请参见[代理模式（Proxy）支持的命令列表](limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。
为便于日常管理和运维，读写分离架构实例支持多个自研的命令，更多信息请参见[阿里云自研的](in-house-commands-for-tair-instances-in-proxy-mode.md)[Proxy](in-house-commands-for-tair-instances-in-proxy-mode.md)[命令](in-house-commands-for-tair-instances-in-proxy-mode.md)。
