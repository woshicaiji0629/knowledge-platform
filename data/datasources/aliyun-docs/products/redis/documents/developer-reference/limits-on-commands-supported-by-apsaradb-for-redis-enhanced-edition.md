# Tair（企业版）命令支持与限制列表-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/redis/documents/product-overview.md)

- [快速入门](products/redis/documents/getting-started.md)

- [Tair AI能力](products/redis/documents/tair-ai-ability.md)

- [操作指南](products/redis/documents/user-guide.md)

- [实践教程](products/redis/documents/use-cases.md)

- [安全合规](products/redis/documents/security-compliance.md)

- [开发参考](products/redis/documents/developer-reference.md)

- [服务支持](products/redis/documents/support.md)

- [视频专区](products/redis/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# Tair（企业版）命令支持与限制

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Tair（企业版）支持多个引擎版本和架构类型，不同的引擎版本和架构类型对Redis命令的支持度有所不同。本文以原生Redis的相关命令为基准，介绍详细的命令支持情况和使用限制，为您的实例选型提供相关参考。

## Tair（企业版）命令支持

Tair（企业版）实例兼容多个原生Redis版本：

- 

Tair内存型（兼容Redis 7.0、6.0和5.0）：

- 

Tair内存型（兼容Redis 7.0）：完全兼容Redis社区7.0版本及以下版本接口，额外支持Tair扩展数据结构。

- 

Tair内存型（兼容Redis 6.0）：完全兼容Redis社区6.2版本及以下版本接口，额外支持Tair扩展数据结构。

- 

Tair内存型（兼容Redis 5.0）：完全兼容Redis社区5.0版本及以下版本接口，额外支持Tair扩展数据结构。

- 

Tair持久内存型：兼容Redis社区6.0版本及以下版本接口，部分限制请参见[Tair（企业版）持久内存型和磁盘型额外的命令限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。

- 

Tair磁盘型：兼容Redis社区6.0版本及以下版本接口，部分限制请参见[Tair（企业版）持久内存型和磁盘型额外的命令限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。

为便于浏览和内容表达，本文的表格约定使用下述注释：

- 

✔️表示支持该命令。

- 

❌表示不支持该命令。

- 

数字标记①：集群架构实例在执行该命令时，需要开通直连访问并使用直连地址连接至实例，详情请参见[使用直连模式连接实例](products/redis/documents/user-guide/use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)。通过Proxy节点的连接地址连接至实例时，也兼容支持该命令。

- 

数字标记②：为兼容某些客户端框架，执行CONFIG SET命令时仅返回OK，不会真正地修改参数。如果您的业务需要对参数进行修改，可通过控制台和API进行操作，具体操作请参见[设置参数](products/redis/documents/user-guide/modify-the-values-of-parameters-for-an-instance.md)。

- 

本文以最新内核小版本进行介绍，部分命令可能在指定小版本后开放支持，详情请参见[Tair](products/redis/documents/support/apsaradb-for-redis-enhanced-edition-1.md)[小版本发布日志](products/redis/documents/support/apsaradb-for-redis-enhanced-edition-1.md)和[Proxy](products/redis/documents/support/apsaradb-for-redis-proxy-nodes.md)[小版本发布日志](products/redis/documents/support/apsaradb-for-redis-proxy-nodes.md)。

说明

各命令族中的命令，如无特殊备注和说明，默认支持实例的所有架构，即标准架构、集群架构及读写分离架构。集群架构与读写分离架构实例在使用某些特定的命令时存在一些限制，详情请参见[集群架构与读写分离实例的命令限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。

### Bitmap

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| BITCOUNT | ✔️ | ✔️ | ✔️ |
| BITFIELD | ✔️ | ✔️ | ✔️ |
| BITFIELD_RO | ➖ | ✔️ | ✔️ |
| BITOP | ✔️ | ✔️ | ✔️ |
| BITPOS | ✔️ | ✔️ | ✔️ |
| GETBIT | ✔️ | ✔️ | ✔️ |
| SETBIT | ✔️ | ✔️ | ✔️ |


### Cluster management

- 

Cluster命令族的命令不适用于标准架构。

- 

通过代理节点连接实例时，会兼容支持部分Cluster命令族的命令，具体为CLUSTER INFO、CLUSTER KEYSLOT、CLUSTER NODES、CLUSTER SLAVES、CLUSTER SLOTS。

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| CLUSTER ADDSLOTS | ❌ | ❌ | ❌ |
| CLUSTER ADDSLOTSRANGE | ➖ | ➖ | ❌ |
| CLUSTER BUMPEPOCH | ❌ | ❌ | ❌ |
| CLUSTER COUNT-FAILURE-REPORTS | ❌ | ❌ | ❌ |
| CLUSTER COUNTKEYSINSLOT ① | ❌ | ❌ | ❌ |
| CLUSTER DELSLOTS | ❌ | ❌ | ❌ |
| CLUSTER DELSLOTSRANGE | ➖ | ➖ | ❌ |
| CLUSTER FAILOVER | ❌ | ❌ | ❌ |
| CLUSTER FLUSHSLOTS | ❌ | ❌ | ❌ |
| CLUSTER FORGET | ❌ | ❌ | ❌ |
| CLUSTER GETKEYSINSLOT | ❌ | ❌ | ❌ |
| CLUSTER INFO ① | ✔️ | ✔️ | ✔️ |
| CLUSTER KEYSLOT ① | ✔️ | ✔️ | ✔️ |
| CLUSTER LINKS | ➖️ | ➖️ | ❌ |
| CLUSTER MEET | ❌ | ❌ | ❌ |
| CLUSTER MYID | ❌ | ❌ | ❌ |
| CLUSTER NODES ① | ✔️ | ✔️ | ✔️ |
| CLUSTER REPLICAS | ❌ | ❌ | ❌ |
| CLUSTER REPLICATE | ❌ | ❌ | ❌ |
| CLUSTER RESET | ❌ | ❌ | ❌ |
| CLUSTER SAVECONFIG | ❌ | ❌ | ❌ |
| CLUSTER SET-CONFIG-EPOCH | ❌ | ❌ | ❌ |
| CLUSTER SETSLOT | ❌ | ❌ | ❌ |
| CLUSTER SHARDS | ➖ | ➖ | ✔️ |
| CLUSTER SLAVES | ❌ | ❌ | ❌ |
| CLUSTER SLOTS | ✔️ | ✔️ | ✔️ |
| READONLY | ✔️️ | ✔️ | ✔️ |
| READWRITE | ✔️ | ✔️ | ✔️ |


### Connection management

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| AUTH | ✔️ | ✔️ | ✔️ |
| CLIENT CACHING | ➖ | ✔️ | ✔️ |
| CLIENT GETNAME | ✔️ | ✔️ | ✔️ |
| CLIENT GETREDIR | ➖ | ✔️ | ✔️ |
| CLIENT ID | ✔️ | ✔️ | ✔️ |
| CLIENT INFO | ➖ | ➖ | ✔️ |
| CLIENT KILL | ✔️ | ✔️ | ✔️ |
| CLIENT LIST | ✔️ | ✔️ | ✔️ |
| CLIENT NO-EVICT | ➖ | ➖ | ✔️ |
| CLIENT PAUSE | ❌ | ❌ | ❌ |
| CLIENT REPLY | ❌ | ❌ | ❌ |
| CLIENT SETNAME | ✔️ | ✔️ | ✔️ |
| CLIENT TRACKING | ➖ | ✔️ | ✔️ |
| CLIENT TRACKINGINFO | ➖ | ➖ | ✔️ |
| CLIENT UNBLOCK | ✔️ | ✔️ | ✔️ |
| CLIENT UNPAUSE | ➖ | ➖ | ❌ |
| ECHO | ✔️ | ✔️ | ✔️ |
| HELLO | ➖ | ✔️ | ✔️ |
| PING | ✔️ | ✔️ | ✔️ |
| QUIT | ✔️ | ✔️ | ✔️ |
| RESET | ➖ | ➖ | ✔️ |
| SELECT | ✔️ | ✔️ | ✔️ |


### Generic

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| COPY | ➖ | ➖ | ✔️ |
| DEL | ✔️ | ✔️ | ✔️ |
| DUMP | ✔️ | ✔️ | ✔️ |
| EXISTS | ✔️ | ✔️ | ✔️ |
| EXPIRE | ✔️ | ✔️ | ✔️ |
| EXPIREAT | ✔️ | ✔️ | ✔️ |
| EXPIRETIME | ➖ | ➖ | ✔️ |
| KEYS | ✔️ | ✔️ | ✔️ |
| MIGRATE | ❌ | ❌ | ❌ |
| MOVE | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ 说明 持久内存型存在限制，详情请参见 [命令限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md) 。 | ✔️ |
| OBJECT | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| OBJECT HELP | ➖ | ➖ | ✔️ |
| PERSIST | ✔️ | ✔️ | ✔️ |
| PEXPIRE | ✔️ | ✔️ | ✔️ |
| PEXPIREAT | ✔️ | ✔️ | ✔️ |
| PEXPIRETIME | ➖ | ➖ | ✔️ |
| PTTL | ✔️ | ✔️ | ✔️ |
| RANDOMKEY | ✔️ | ✔️ | ✔️ |
| RENAME | ✔️ | ✔️ 说明 持久内存型、磁盘型存在限制，详情请参见 [命令限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md) 。 | ✔️ |
| RENAMENX | ✔️ | ✔️ 说明 持久内存型、磁盘型存在限制，详情请参见 [命令限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md) 。 | ✔️ |
| RESTORE | ✔️ | ✔️ | ✔️ |
| SCAN | ✔️ | ✔️ | ✔️ |
| SORT | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| SORT_RO | ➖ | ➖ | ✔️ |
| TOUCH | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| TTL | ✔️ | ✔️ | ✔️ |
| TYPE | ✔️ | ✔️ | ✔️ |
| UNLINK | ✔️ | ✔️ | ✔️ |
| WAIT | ✔️ | ✔️ | ✔️ |


### Geospatial indices

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| GEOADD | ✔️ | ✔️ | ✔️ |
| GEODIST | ✔️ | ✔️ | ✔️ |
| GEOHASH | ✔️ | ✔️ | ✔️ |
| GEOPOS | ✔️ | ✔️ | ✔️ |
| GEORADIUS | ✔️ | ✔️ | ✔️ |
| GEORADIUSBYMEMBER | ✔️ | ✔️ | ✔️ |
| GEOSEARCH | ➖ | ➖ | ✔️ |
| GEOSEARCHSTORE | ➖ | ➖ | ✔️ |


### Hash

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| HDEL | ✔️ | ✔️ | ✔️ |
| HEXISTS | ✔️ | ✔️ | ✔️ |
| HGET | ✔️ | ✔️ | ✔️ |
| HGETALL | ✔️ | ✔️ | ✔️ |
| HINCRBY | ✔️ | ✔️ | ✔️ |
| HINCRBYFLOAT | ✔️ | ✔️ | ✔️ |
| HKEYS | ✔️ | ✔️ | ✔️ |
| HLEN | ✔️ | ✔️ | ✔️ |
| HMGET | ✔️ | ✔️ | ✔️ |
| HMSET | ✔️ | ✔️ | ✔️ |
| HRANDFIELD | ➖ | ➖ | ✔️ |
| HSCAN | ✔️ | ✔️ | ✔️ |
| HSET | ✔️ | ✔️ | ✔️ |
| HSETNX | ✔️ | ✔️ | ✔️ |
| HSTRLEN | ✔️ | ✔️ | ✔️ |
| HVALS | ✔️ | ✔️ | ✔️ |


### HyperLogLog

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| PFADD | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| PFCOUNT | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| PFMERGE | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |


### Lists

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| BLPOP | ✔️ | ✔️ | ✔️ |
| BLMOVE | ➖ | ➖ | ✔️ |
| BLMPOP | ➖ | ➖ | ✔️ |
| BRPOP | ✔️ | ✔️ | ✔️ |
| BRPOPLPUSH | ✔️ | ✔️ | ✔️ |
| LINDEX | ✔️ | ✔️ | ✔️ |
| LINSERT | ✔️ | ✔️ | ✔️ |
| LLEN | ✔️ | ✔️ | ✔️ |
| LMOVE | ➖ | ➖ | ✔️ |
| LMPOP | ➖ | ➖ | ✔️ |
| LPOP | ✔️ | ✔️ | ✔️ |
| LPOS | ➖ | ✔️ | ✔️ |
| LPUSH | ✔️ | ✔️ | ✔️ |
| LPUSHX | ✔️ | ✔️ | ✔️ |
| LRANGE | ✔️ | ✔️ | ✔️ |
| LREM | ✔️ | ✔️ | ✔️ |
| LSET | ✔️ | ✔️ | ✔️ |
| LTRIM | ✔️ | ✔️ | ✔️ |
| RPOP | ✔️ | ✔️ | ✔️ |
| RPOPLPUSH | ✔️ | ✔️ | ✔️ |
| RPUSH | ✔️ | ✔️ | ✔️ |
| RPUSHX | ✔️ | ✔️ | ✔️ |


### Pub/Sub

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| PSUBSCRIBE | ✔️ | ✔️ | ✔️ |
| PUBLISH | ✔️ | ✔️ | ✔️ |
| PUBSUB | ✔️ | ✔️ | ✔️ |
| PUBSUB HELP | ➖ | ➖ | ✔️ |
| PUBSUB SHARDCHANNELS | ➖ | ➖ | ✔️ |
| PUBSUB SHARDNUMSUB | ➖ | ➖ | ✔️ |
| PUNSUBSCRIBE | ✔️ | ✔️ | ✔️ |
| SPUBLISH | ➖ | ➖ | ✔️ |
| SUBSCRIBE | ✔️ | ✔️ | ✔️ |
| SSUBSCRIBE | ➖ | ➖ | ✔️ |
| SUNSUBSCRIBE | ➖ | ➖ | ✔️ |
| UNSUBSCRIBE | ✔️ | ✔️ | ✔️ |


### Scripting and Functions

说明

磁盘型执行EVAL、EVALSHA、SCRIPT EXISTS等Lua脚本相关命令存在限制，详情请参见[命令限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| EVAL | ✔️ | ✔️ | ✔️ |
| EVAL_RO | ➖ | ➖ | ✔️ |
| EVALSHA | ✔️ | ✔️ | ✔️ |
| EVALSHA_RO | ➖ | ➖ | ✔️ |
| FCALL | ➖ | ➖ | ✔️ |
| FCALL_RO | ➖ | ➖ | ✔️ |
| FUNCTION DELETE | ➖ | ➖ | ✔️ |
| FUNCTION DUMP | ➖ | ➖ | ✔️ |
| FUNCTION FLUSH | ➖ | ➖ | ✔️ |
| FUNCTION HELP | ➖ | ➖ | ✔️ |
| FUNCTION KILL | ➖ | ➖ | ✔️ |
| FUNCTION LIST | ➖ | ➖ | ✔️ |
| FUNCTION LOAD | ➖ | ➖ | ✔️ |
| FUNCTION RESTORE | ➖ | ➖ | ✔️ |
| FUNCTION STATS | ➖ | ➖ | ✔️ |
| SCRIPT DEBUG | ❌ | ❌ | ❌ |
| SCRIPT EXISTS | ✔️ | ✔️ | ✔️ |
| SCRIPT FLUSH | ✔️ | ✔️ | ✔️ |
| SCRIPT KILL | ✔️ | ✔️ | ✔️ |
| SCRIPT LOAD | ✔️ | ✔️ | ✔️ |


### Server management

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| ACL CAT | ➖ | ❌ | ❌ |
| ACL DELUSER | ➖ | ❌ | ❌ |
| ACL DRYRUN | ➖ | ➖ | ❌ |
| ACL GENPASS | ➖ | ❌ | ❌ |
| ACL GETUSER | ➖ | ❌ | ❌ |
| ACL HELP | ➖ | ❌ | ❌ |
| ACL LIST | ➖ | ❌ | ❌ |
| ACL LOAD | ➖ | ❌ | ❌ |
| ACL LOG | ➖ | ❌ | ❌ |
| ACL SAVE | ➖ | ❌ | ❌ |
| ACL SETUSER | ➖ | ❌ | ❌ |
| ACL USERS | ➖ | ❌ | ❌ |
| ACL WHOAMI | ➖ | ❌ | ✔️ |
| BGREWRITEAOF | ❌ | ❌ | ❌ |
| BGSAVE | ❌ | ❌ | ❌ |
| COMMAND | ✔️ | ✔️ | ✔️ |
| COMMAND COUNT | ✔️ | ✔️ | ✔️ |
| COMMAND DOCS | ➖ | ➖ | ✔️ |
| COMMAND GETKEYS | ✔️ | ✔️ | ✔️ |
| COMMAND GETKEYSANDFLAGS | ➖ | ➖ | ✔️ |
| COMMAND INFO | ✔️ | ✔️ | ✔️ |
| COMMAND LIST | ➖ | ➖ | ✔️ |
| CONFIG GET | ✔️ | ✔️ | ✔️ |
| CONFIG HELP | ✔️ | ✔️ | ❌ |
| CONFIG RESETSTAT | ✔️ | ✔️ | ❌ |
| CONFIG REWRITE | ❌ | ❌ | ❌ |
| CONFIG SET ② | ✔️ | ✔️ | ❌ |
| DBSIZE | ✔️ | ✔️ | ✔️ |
| DEBUG OBJECT | ❌ | ❌ | ❌ |
| DEBUG SEGFAULT | ❌ | ❌ | ❌ |
| FAILOVER | ➖ | ➖ | ❌ |
| FLUSHALL | ✔️ | ✔️ | ✔️ |
| FLUSHDB | ✔️ | ✔️ 说明 磁盘型存在限制，详情请参见 [命令限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md) 。 | ✔️ |
| INFO | ✔️ | ✔️ | ✔️ |
| LASTSAVE | ❌ | ❌ | ❌ |
| LATENCY DOCTOR | ✔️ | ✔️ | ✔️ |
| LATENCY GRAPH | ✔️ | ✔️ | ✔️ |
| LATENCY HELP | ✔️ | ✔️ | ✔️ |
| LATENCY HISTOGRAM | ➖ | ➖ | ✔️ |
| LATENCY HISTORY | ✔️ | ✔️ | ✔️ |
| LATENCY LATEST | ✔️ | ✔️ | ✔️ |
| LATENCY RESET | ✔️ | ✔️ | ➖ |
| LOLWUT | ✔️ | ✔️ | ✔️ |
| MEMORY DOCTOR | ✔️ | ✔️ | ✔️ |
| MEMORY HELP | ✔️ | ✔️ | ✔️ |
| MEMORY MALLOC-STATS | ✔️ | ✔️ | ✔️ |
| MEMORY PURGE | ✔️ | ✔️ | ✔️ |
| MEMORY STATS | ✔️ | ✔️ | ✔️ |
| MEMORY USAGE | ✔️ | ✔️ | ✔️ |
| MODULE LIST | ❌ | ❌ | ❌ |
| MODULE LOAD | ❌ | ❌ | ❌ |
| MODULE LOADEX | ➖ | ➖ | ❌ |
| MODULE UNLOAD | ❌ | ❌ | ❌ |
| MONITOR | ✔️ | ✔️ | ✔️ |
| PSYNC | ❌ | ❌ | ❌ |
| REPLICAOF | ❌ | ❌ | ❌ |
| ROLE | ✔️ | ✔️ | ✔️ |
| SAVE | ❌ | ❌ | ❌ |
| SHUTDOWN | ❌ | ❌ | ❌ |
| SLAVEOF | ❌ | ❌ | ❌ |
| SLOWLOG | ✔️ | ✔️ | ✔️ |
| SLOWLOG HELP | ➖ | ➖ | ✔️ |
| SLOWLOG RESET | ❌ | ❌ | ❌ |
| SWAPDB | ✔️ | 内存型✔️ 持久内存型、磁盘型❌ | ✔️ |
| SYNC | ❌ | ❌ | ❌ |
| TIME | ✔️ | ✔️ | ✔️ |


### Sentinel

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| SENTINEL sentinels | ✔️ | ✔️ | ✔️ |
| SENTINEL get-master-addr-by-name | ✔️ | ✔️ | ✔️ |


### Set

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| SADD | ✔️ | ✔️ | ✔️ |
| SCARD | ✔️ | ✔️ | ✔️ |
| SDIFF | ✔️ | ✔️ | ✔️ |
| SDIFFSTORE | ✔️ | ✔️ | ✔️ |
| SINTER | ✔️ | ✔️ | ✔️ |
| SINTERCARD | ➖ | ➖ | ✔️ |
| SINTERSTORE | ✔️ | ✔️ | ✔️ |
| SISMEMBER | ✔️ | ✔️ | ✔️ |
| SMEMBERS | ✔️ | ✔️ | ✔️ |
| SMISMEMBER | ❌ | ✔️ | ✔️ |
| SMOVE | ✔️ | ✔️ | ✔️ |
| SPOP | ✔️ | ✔️ | ✔️ |
| SRANDMEMBER | ✔️ | ✔️ | ✔️ |
| SREM | ✔️ | ✔️ | ✔️ |
| SSCAN | ✔️ | ✔️ | ✔️ |
| SUNION | ✔️ | ✔️ | ✔️ |
| SUNIONSTORE | ✔️ | ✔️ | ✔️ |


### Sorted Set

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| BZMPOP | ➖ | ➖ | ✔️ |
| BZPOPMAX | ✔️ | ✔️ | ✔️ |
| BZPOPMIN | ✔️ | ✔️ | ✔️ |
| ZADD | ✔️ | ✔️ | ✔️ |
| ZCARD | ✔️ | ✔️ | ✔️ |
| ZCOUNT | ✔️ | ✔️ | ✔️ |
| ZDIFF | ➖ | ➖ | ✔️ |
| ZDIFFSTORE | ➖ | ➖ | ✔️ |
| ZINCRBY | ✔️ | ✔️ | ✔️ |
| ZINTER | ➖ | ➖ | ✔️ |
| ZINTERCARD | ➖ | ➖ | ✔️ |
| ZINTERSTORE | ✔️ | ✔️ | ✔️ |
| ZLEXCOUNT | ✔️ | ✔️ | ✔️ |
| ZMPOP | ➖ | ➖ | ✔️ |
| ZMSCORE | ➖ | ➖ | ✔️ |
| ZPOPMAX | ✔️ | ✔️ | ✔️ |
| ZPOPMIN | ✔️ | ✔️ | ✔️ |
| ZRANDMEMBER | ➖ | ➖ | ✔️ |
| ZRANGE | ✔️ | ✔️ | ✔️ |
| ZRANGEBYLEX | ✔️ | ✔️ | ✔️ |
| ZRANGEBYSCORE | ✔️ | ✔️ | ✔️ |
| ZRANGESTORE | ➖ | ➖ | ✔️ |
| ZRANK | ✔️ | ✔️ | ✔️ |
| ZREM | ✔️ | ✔️ | ✔️ |
| ZREMRANGEBYLEX | ✔️ | ✔️ | ✔️ |
| ZREMRANGEBYRANK | ✔️ | ✔️ | ✔️ |
| ZREMRANGEBYSCORE | ✔️ | ✔️ | ✔️ |
| ZREVRANGE | ✔️ | ✔️ | ✔️ |
| ZREVRANGEBYLEX | ✔️ | ✔️ | ✔️ |
| ZREVRANGEBYSCORE | ✔️ | ✔️ | ✔️ |
| ZREVRANK | ✔️ | ✔️ | ✔️ |
| ZSCAN | ✔️ | ✔️ | ✔️ |
| ZSCORE | ✔️ | ✔️ | ✔️ |
| ZUNION | ➖ | ➖ | ✔️ |
| ZUNIONSTORE | ✔️ | ✔️ | ✔️ |


### Stream

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| XACK | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| XADD | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| XAUTOCLAIM | ➖ | ➖ | ✔️ |
| XCLAIM | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| XDEL | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| XGROUP | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| XGROUP CREATECONSUMER | ➖ | ➖ | ✔️ |
| XINFO | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| XLEN | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| XPENDING | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| XRANGE | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| XREAD | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| XREADGROUP | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| XREVRANGE | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| XTRIM | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |


### String

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| APPEND | ✔️ | ✔️ | ✔️ |
| DECR | ✔️ | ✔️ | ✔️ |
| DECRBY | ✔️ | ✔️ | ✔️ |
| GET | ✔️ | ✔️ | ✔️ |
| GETDEL | ➖ | ➖ | ✔️ |
| GETEX | ➖ | ➖ | ✔️ |
| GETRANGE | ✔️ | ✔️ | ✔️ |
| GETSET | ✔️ | ✔️ | ✔️ |
| LCS | ➖ | ➖ | ✔️ |
| INCR | ✔️ | ✔️ | ✔️ |
| INCRBY | ✔️ | ✔️ | ✔️ |
| INCRBYFLOAT | ✔️ | ✔️ | ✔️ |
| MGET | ✔️ | ✔️ | ✔️ |
| MSET | ✔️ | ✔️ | ✔️ |
| MSETNX | ✔️ | ✔️ | ✔️ |
| PSETEX | ✔️ | ✔️ | ✔️ |
| SET | ✔️ | ✔️ | ✔️ |
| SETEX | ✔️ | ✔️ | ✔️ |
| SETNX | ✔️ | ✔️ | ✔️ |
| SETRANGE | ✔️ | ✔️ | ✔️ |
| STRALGO | ➖ | ✔️ | ➖ |
| STRLEN | ✔️ | ✔️ | ✔️ |


### Transactions

说明

磁盘型执行DISCARD、EXEC、WATCH等事务相关命令存在限制，详情请参见[命令限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| DISCARD | ✔️ | ✔️ | ✔️ |
| EXEC | ✔️ | ✔️ | ✔️ |
| MULTI | ✔️ | ✔️ | ✔️ |
| UNWATCH | ✔️ | ✔️ | ✔️ |
| WATCH | ✔️ | ✔️ | ✔️ |


## Tair（企业版）持久内存型和磁盘型额外的命令限制

说明

- 

以下为实例最新小版本的兼容情况。若您的实例存在更多限制，请您升级实例小版本后重试，具体操作请参见[升级小版本与代理版本](products/redis/documents/user-guide/update-the-minor-version.md)。

- 

如需了解Release notes，请参见[Tair](products/redis/documents/support/apsaradb-for-redis-enhanced-edition-1.md)[小版本发布日志](products/redis/documents/support/apsaradb-for-redis-enhanced-edition-1.md)。

- 

关于设置参数的具体操作，请参见[设置参数](products/redis/documents/user-guide/modify-the-values-of-parameters-for-an-instance.md)。

- 

持久内存型

| 命令族 | 限制项 |
| --- | --- |
| Keys（键） | MOVE 与 RENAME 系列命令，需通过 pena_rename_move_compatible_enabled 参数开启兼容模式，才能执行。 |
| Server（数据库管理） | 不支持命令：SWAPDB。 |


- 

磁盘型

- 

- 

- 

- 

| 命令族 | 限制项 |
| --- | --- |
| Hyperloglog | 不支持命令：PFADD、PFCOUNT、PFMERG。 |
| Keys（键） | 不支持命令：MOVE、OBJECT、SORT、TOUCH。 Rename、RenameNX 最大支持修改 max-rename-commit-size 大小（默认为 16 MB）的 Key。 |
| Server（数据库管理） | 不支持命令：SWAPDB。 仅支持 FLUSHDB 命令同步执行模式，不支持异步执行模式。在生产环境中，请谨慎执行 FLUSHDB 命令。 |
| Stream（流） | 不支持该系列命令。 |
| Scripting（Lua 脚本） | Lua 脚本相关命令，例如 EVAL、EVALSHA、SCRIPT EXISTS 等，需通过 txn-isolation-lock 参数和 #no_loose_lua-strict-mode 参数开启、控制。 |
| Transactions（事务） | 事务相关命令，例如 DISCARD、EXEC、WATCH 等，可通过 txn-isolation-lock 参数开启、控制。 |


[上一篇：命令概览](products/redis/documents/developer-reference/overview-3.md)[下一篇：Redis开源版命令支持](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)

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
