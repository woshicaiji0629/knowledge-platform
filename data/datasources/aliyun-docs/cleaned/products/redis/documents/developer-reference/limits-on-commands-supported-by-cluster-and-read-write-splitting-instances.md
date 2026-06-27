# 命令支持列表及使用规范-云数据库Tair（兼容Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances

# 集群架构与读写分离实例的命令限制
相对标准架构，集群架构与读写分离架构的云数据库 Tair（兼容 Redis）实例在Redis命令的支持上有一定的区别，例如禁用某些命令、单个命令不支持访问跨Slot的Key等，请在使用过程中了解并遵守相应的规范。
## 集群架构命令限制
集群架构实例本身兼容不同的Redis版本，各版本整体的命令支持情况请参见[Redis](commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](commands-supported-by-apsaradb-for-redis-community-edition.md)与[Tair（企业版）命令支持与限制](limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。
集群架构支持直连模式与代理模式，其命令限制有所不同：
### 集群架构直连模式
支持SELECT命令。直连模式仅支持集群初始化方式，但由于某些客户端在集群初始化方式下不支持SELECT命令，因此在上述场景中无法执行该命令。
仅兼容Redis 7.0版的集群架构实例支持SWAPDB命令。
如需执行涉及多Key的命令，请确保命令操作的Key都分布在同一个Slot中，例如使用Hash tag等。
在集群架构直连模式中执行事务时，要求与开源Redis Cluster行为一致，即严格要求事务所操作的Key均在同一Slot。
### 集群架构代理模式
支持SELECT命令，代理模式通过中间层屏蔽集群架构细节，具有更好的客户端兼容性。
在集群架构直连模式的基础上，代理节点不支持CLIENT INFO、CLIENT ID等命令，但支持对如下命令执行跨Slot的多Key操作：DEL、EXISTS等，详细介绍请参见[代理模式（Proxy）支持的命令列表](limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。
CLIENT KILL命令目前支持的格式为：CLIENT KILL <ip:port>和CLIENT KILL ADDR <ip:port>。
执行CLIENT LIST命令会列出所有连接到该代理节点的连接信息，返回结果与Redis原生命令有所不同，说明如下：
id、age、idle、addr、fd、name、db、multi、omem、cmd字段和原生Redis的含义一致。
sub、psub在代理节点上没有区分，统一为1或0。
qbuf、qbuf-free、obl和oll字段目前没有具体意义。
关于事务的限制：
当事务内所有的Key都在同一个Slot时，事务可以正常执行，且遵循事务语义。
当不满足事务内所有的Key都在同一个Slot，但满足每个命令内部的Key都在同一个Slot时，事务可以正常执行，属于同一个Slot的命令之间遵循事务语义，属于不同Slot的命令之间不保证事务语义。
当事务不满足同一个命令内的Key都属于同一个Slot时，命令无法执行。
部分没有Key的命令不支持在事务中执行，详情查看代理模式（Proxy）支持的命令列表。
SCAN 0命令将从集群的首个数据分片开始，按序遍历各分片数据。仅当当前分片遍历完成后，才会转向下一个分片。若需对特定分片进行定向扫描，请使用[ISCAN](in-house-commands-for-tair-instances-in-proxy-mode.md)命令。
为便于日常管理和运维，集群架构代理模式实例支持多个自研的命令，更多信息请参见[阿里云自研的](in-house-commands-for-tair-instances-in-proxy-mode.md)[Proxy](in-house-commands-for-tair-instances-in-proxy-mode.md)[命令](in-house-commands-for-tair-instances-in-proxy-mode.md)。
除此之外，Redis Cluster对使用Lua脚本增加了一些限制，云数据库 Tair（兼容 Redis）集群架构在此基础上存在额外限制，更多信息请参见[集群架构特殊限制](../support/usage-of-lua-scripts.md)。
## 读写分离实例的命令限制
读写分离实例兼容不同的Redis版本，各版本整体的命令支持情况请参见[Redis](commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](commands-supported-by-apsaradb-for-redis-community-edition.md)与[Tair（企业版）命令支持与限制](limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。
由于读写分离实例默认为代理模式，读写分离实例存在代理节点的命令限制，例如代理节点不支持CLIENT INFO、CLIENT ID等命令，详细介绍请参见[代理模式（Proxy）支持的命令列表](limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。
为便于日常管理和运维，读写分离架构实例支持多个自研的命令，更多信息请参见[阿里云自研的](in-house-commands-for-tair-instances-in-proxy-mode.md)[Proxy](in-house-commands-for-tair-instances-in-proxy-mode.md)[命令](in-house-commands-for-tair-instances-in-proxy-mode.md)。
## 代理模式（Proxy）支持的命令列表
以下内容适用于集群架构代理模式和读写分离架构，为便于浏览和内容表达，本文的表格约定使用下述注释：
✔️表示Proxy支持该命令，若该命令支持多Key，则表示支持跨Slot执行该命令。
⭕️表示Proxy支持该命令，但存在限制，请确保命令所要操作的Key都分布在1个Slot中，例如使用Hash tag等。
❌表示Proxy不支持该命令。
数字标记①：为兼容某些客户端框架，该命令仅返回OK或空结果，不会真正执行。
数字标记②：该请求由Proxy直接处理返回，不受Redis DB版本限制。
### Bitmap
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| BITCOUNT | ✔️ | ✔️ | ✔️ | ✔️ |
| BITFIELD | ✔️ | ✔️ | ✔️ | ✔️ |
| BITFIELD_RO | ❌ | ❌ | ❌ | ❌ |
| BITOP | ⭕️ | ⭕️ | ✔️ | ✔️ |
| BITPOS | ✔️ | ✔️ | ✔️ | ✔️ |
| GETBIT | ✔️ | ✔️ | ✔️ | ✔️ |
| SETBIT | ✔️ | ✔️ | ✔️ | ✔️ |
### Cluster management
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| CLUSTER ADDSLOTS ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER ADDSLOTSRANGE | ❌ | ❌ | ❌ | ❌ |
| CLUSTER BUMPEPOCH | ❌ | ❌ | ❌ | ❌ |
| CLUSTER COUNT-FAILURE-REPORTS ② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER COUNTKEYSINSLOT ② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER DELSLOTS ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER DELSLOTSRANGE | ❌ | ❌ | ❌ | ❌ |
| CLUSTER FAILOVER ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER FLUSHSLOTS | ❌ | ❌ | ❌ | ❌ |
| CLUSTER FORGET ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER GETKEYSINSLOT ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER INFO ② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER KEYSLOT ② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER LINKS | ❌ | ❌ | ❌ | ❌ |
| CLUSTER MEET ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER MYID | ❌ | ❌ | ❌ | ❌ |
| CLUSTER NODES ② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER REPLICAS | ❌ | ❌ | ❌ | ❌ |
| CLUSTER REPLICATE ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER RESET ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER SAVECONFIG ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER SET-CONFIG-EPOCH ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER SETSLOT ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER SHARDS | ❌ | ❌ | ❌ | ❌ |
| CLUSTER SLAVES ② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER SLOTS ② | ✔️ | ❌ | ✔️ | ❌ |
| READONLY ①② | ✔️ | ❌ | ✔️️ | ❌ |
| READWRITE ①② | ✔️ | ❌ | ✔️ | ❌ |
### Connection management
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| AUTH | ✔️ | ❌ | ✔️ | ✔️ |
| CLIENT CACHING | ❌ | ❌ | ❌ | ❌ |
| CLIENT GETNAME ② | ✔️ | ❌ | ✔️ | ❌ |
| CLIENT GETREDIR | ❌ | ❌ | ❌ | ❌ |
| CLIENT ID | ❌ | ❌ | ❌ | ❌ |
| CLIENT INFO | ❌ | ❌ | ❌ | ❌ |
| CLIENT KILL ② | ✔️ | ❌ | ✔️ | ❌ |
| CLIENT LIST ② | ✔️ | ❌ | ✔️ | ❌ |
| CLIENT NO-EVICT | ❌ | ❌ | ❌ | ❌ |
| CLIENT PAUSE | ❌ | ❌ | ❌ | ❌ |
| CLIENT REPLY | ❌ | ❌ | ❌ | ❌ |
| CLIENT SETNAME ② | ✔️ | ❌ | ✔️ | ❌ |
| CLIENT TRACKING | ❌ | ❌ | ❌ | ❌ |
| CLIENT TRACKINGINFO | ❌ | ❌ | ❌ | ❌ |
| CLIENT UNBLOCK | ❌ | ❌ | ❌ | ❌ |
| CLIENT UNPAUSE | ❌ | ❌ | ❌ | ❌ |
| ECHO | ✔️ | ❌ | ✔️ | ✔️ |
| HELLO | ✔️（有限制） | ✔️（有限制） | ✔️（有限制） | ✔️（有限制） |
| PING ② | ✔️ | ❌ | ✔️ | ✔️ |
| QUIT ② | ✔️ | ✔️ | ✔️ | ✔️ |
| RESET | ❌ | ❌ | ❌ | ❌ |
| SELECT | ✔️ | ✔️ | ✔️ | ✔️ |
说明
默认情况下，不支持使用HELLO命令。如需使用该命令，请确保Proxy的小版本[升级](../user-guide/update-the-minor-version.md)至7.0.9及以上，并且已[启用](../user-guide/modify-the-values-of-parameters-for-an-instance.md)hello_enabled参数。
### Generic
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| COPY | ⭕️ | ⭕️ | ✔️ | ✔️ |
| DEL | ✔️ | ⭕️ | ✔️ | ✔️ |
| DUMP | ✔️ | ✔️ | ✔️ | ✔️ |
| EXISTS | ✔️ | ⭕️ | ✔️ | ✔️ |
| EXPIRE | ✔️ | ✔️ | ✔️ | ✔️ |
| EXPIREAT | ✔️ | ✔️ | ✔️ | ✔️ |
| EXPIRETIME | ✔️ | ✔️ | ✔️ | ✔️ |
| KEYS | ✔️ | ❌ | ✔️ | ✔️ |
| MIGRATE | ❌ | ❌ | ❌ | ❌ |
| MOVE | ✔️ | ✔️ | ✔️ | ✔️ |
| OBJECT | ✔️ | ✔️ | ✔️ | ✔️ |
| OBJECT HELP | ✔️ | ✔️ | ✔️ | ✔️ |
| PERSIST | ✔️ | ✔️ | ✔️ | ✔️ |
| PEXPIRE | ✔️ | ✔️ | ✔️ | ✔️ |
| PEXPIREAT | ✔️ | ✔️ | ✔️ | ✔️ |
| PEXPIRETIME | ✔️ | ✔️ | ✔️ | ✔️ |
| PTTL | ✔️ | ✔️ | ✔️ | ✔️ |
| RANDOMKEY | ✔️ | ❌ | ✔️ | ✔️ |
| RENAME | ⭕️ | ⭕️ | ✔️ | ✔️ |
| RENAMENX | ⭕️ | ⭕️ | ✔️ | ✔️ |
| RESTORE | ✔️ | ✔️ | ✔️ | ✔️ |
| SCAN | ✔️ | ❌ | ✔️ | ✔️ |
| SORT | ⭕️ | ⭕️ | ✔️ | ✔️ |
| SORT_RO | ⭕️ | ⭕️ | ✔️ | ✔️ |
| TOUCH | ✔️ | ⭕️ | ✔️ | ✔️ |
| TTL | ✔️ | ✔️ | ✔️ | ✔️ |
| TYPE | ✔️ | ✔️ | ✔️ | ✔️ |
| UNLINK | ✔️ | ⭕️ | ✔️ | ✔️ |
| WAIT | ✔️ | ❌ | ✔️ | ✔️ |
### Geospatial indices
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| GEOADD | ✔️ | ✔️ | ✔️ | ✔️ |
| GEODIST | ✔️ | ✔️ | ✔️ | ✔️ |
| GEOHASH | ✔️ | ✔️ | ✔️ | ✔️ |
| GEOPOS | ✔️ | ✔️ | ✔️ | ✔️ |
| GEORADIUS | ⭕️ | ⭕️ | ✔️ | ✔️ |
| GEORADIUSBYMEMBER | ⭕️ | ⭕️ | ✔️ | ✔️ |
| GEOSEARCH | ✔️ | ✔️ | ✔️ | ✔️ |
| GEOSEARCHSTORE | ⭕️ | ⭕️ | ✔️ | ✔️ |
### Hash
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| HDEL | ✔️ | ✔️ | ✔️ | ✔️ |
| HEXISTS | ✔️ | ✔️ | ✔️ | ✔️ |
| HGET | ✔️ | ✔️ | ✔️ | ✔️ |
| HGETALL | ✔️ | ✔️ | ✔️ | ✔️ |
| HINCRBY | ✔️ | ✔️ | ✔️ | ✔️ |
| HINCRBYFLOAT | ✔️ | ✔️ | ✔️ | ✔️ |
| HKEYS | ✔️ | ✔️ | ✔️ | ✔️ |
| HLEN | ✔️ | ✔️ | ✔️ | ✔️ |
| HMGET | ✔️ | ✔️ | ✔️ | ✔️ |
| HMSET | ✔️ | ✔️ | ✔️ | ✔️ |
| HRANDFIELD | ✔️ | ✔️ | ✔️ | ✔️ |
| HSCAN | ✔️ | ✔️ | ✔️ | ✔️ |
| HSET | ✔️ | ✔️ | ✔️ | ✔️ |
| HSETNX | ✔️ | ✔️ | ✔️ | ✔️ |
| HSTRLEN | ✔️ | ✔️ | ✔️ | ✔️ |
| HVALS | ✔️ | ✔️ | ✔️ | ✔️ |
### HyperLogLog
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| PFADD | ✔️ | ✔️ | ✔️ | ✔️ |
| PFCOUNT | ⭕️ | ⭕️ | ✔️ | ✔️ |
| PFMERGE | ⭕️ | ⭕️ | ✔️ | ✔️ |
### Lists
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| BLPOP | ⭕️ | ⭕️ | ✔️ | ✔️ |
| BLMOVE | ⭕️ | ⭕️ | ✔️ | ✔️ |
| BLMPOP | ⭕️ | ⭕️ | ✔️ | ✔️ |
| BRPOP | ⭕️ | ⭕️ | ✔️ | ✔️ |
| BRPOPLPUSH | ⭕️ | ⭕️ | ✔️ | ✔️ |
| LINDEX | ✔️ | ✔️ | ✔️ | ✔️ |
| LINSERT | ✔️ | ✔️ | ✔️ | ✔️ |
| LLEN | ✔️ | ✔️ | ✔️ | ✔️ |
| LMOVE | ⭕️ | ⭕️ | ✔️ | ✔️ |
| LMPOP | ⭕️ | ⭕️ | ✔️ | ✔️ |
| LPOP | ✔️ | ✔️ | ✔️ | ✔️ |
| LPUSH | ✔️ | ✔️ | ✔️ | ✔️ |
| LPUSHX | ✔️ | ✔️ | ✔️ | ✔️ |
| LRANGE | ✔️ | ✔️ | ✔️ | ✔️ |
| LREM | ✔️ | ✔️ | ✔️ | ✔️ |
| LSET | ✔️ | ✔️ | ✔️ | ✔️ |
| LTRIM | ✔️ | ✔️ | ✔️ | ✔️ |
| RPOP | ✔️ | ✔️ | ✔️ | ✔️ |
| RPOPLPUSH | ⭕️ | ⭕️ | ✔️ | ✔️ |
| RPUSH | ✔️ | ✔️ | ✔️ | ✔️ |
| RPUSHX | ✔️ | ✔️ | ✔️ | ✔️ |
### Pub/Sub
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| PSUBSCRIBE | ✔️ | ❌ | ✔️ | ❌ |
| PUBLISH | ✔️ | ✔️ | ✔️ | ✔️ |
| PUBSUB | ✔️ | ❌ | ✔️ | ✔️ |
| PUBSUB HELP | ❌ | ❌ | ❌ | ❌ |
| PUBSUB SHARDCHANNELS | ✔️ | ❌ | ✔️ | ✔️ |
| PUBSUB SHARDNUMSUB | ✔️ | ❌ | ✔️ | ✔️ |
| PUNSUBSCRIBE | ✔️ | ❌ | ✔️ | ❌ |
| SPUBLISH | ✔️ | ✔️ | ✔️ | ✔️ |
| SUBSCRIBE | ✔️ | ❌ | ✔️ | ❌ |
| SSUBSCRIBE | ✔️ | ❌ | ✔️ | ❌ |
| SUNSUBSCRIBE | ✔️ | ❌ | ✔️ | ❌ |
| UNSUBSCRIBE | ✔️ | ❌ | ✔️ | ❌ |
### Scripting and Functions
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| EVAL | ⭕️ | ❌ | ✔️ | ✔️ |
| EVAL_RO | ⭕️ | ❌ | ✔️ | ✔️ |
| EVALSHA | ⭕️ | ❌ | ✔️ | ✔️ |
| EVALSHA_RO | ⭕️ | ❌ | ✔️ | ✔️ |
| FCALL | ⭕️ | ❌ | ✔️ | ✔️ |
| FCALL_RO | ⭕️ | ❌ | ✔️ | ✔️ |
| FUNCTION DELETE | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION DUMP | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION FLUSH | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION HELP | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION KILL | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION LIST | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION LOAD | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION RESTORE | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION STATS | ✔️ | ❌ | ✔️ | ❌ |
| SCRIPT DEBUG | ❌ | ❌ | ❌ | ❌ |
| SCRIPT EXISTS | ✔️ | ❌ | ✔️ | ❌ |
| SCRIPT FLUSH | ✔️ | ❌ | ✔️ | ❌ |
| SCRIPT KILL | ✔️ | ❌ | ✔️ | ❌ |
| SCRIPT LOAD | ✔️ | ❌ | ✔️ | ❌ |
### Server management
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| ACL CAT | ❌ | ❌ | ❌ | ❌ |
| ACL DELUSER | ❌ | ❌ | ❌ | ❌ |
| ACL DRYRUN | ❌ | ❌ | ❌ | ➖ |
| ACL GENPASS | ❌ | ❌ | ❌ | ❌ |
| ACL GETUSER | ❌ | ❌ | ❌ | ❌ |
| ACL HELP | ❌ | ❌ | ❌ | ❌ |
| ACL LIST | ❌ | ❌ | ❌ | ❌ |
| ACL LOAD | ❌ | ❌ | ❌ | ❌ |
| ACL LOG | ❌ | ❌ | ❌ | ❌ |
| ACL SAVE | ❌ | ❌ | ❌ | ❌ |
| ACL SETUSER | ❌ | ❌ | ❌ | ❌ |
| ACL USERS | ❌ | ❌ | ❌ | ❌ |
| ACL WHOAMI | ❌ | ❌ | ❌ | ❌ |
| BGREWRITEAOF | ❌ | ❌ | ❌ | ❌ |
| BGSAVE | ❌ | ❌ | ❌ | ❌ |
| COMMAND | ✔️ | ❌ | ✔️ | ✔️ |
| COMMAND COUNT | ✔️ | ❌ | ✔️ | ✔️ |
| COMMAND DOCS | ✔️ | ❌ | ✔️ | ✔️ |
| COMMAND GETKEYS | ✔️ | ❌ | ✔️ | ✔️ |
| COMMAND GETKEYSANDFLAGS | ✔️ | ❌ | ✔️ | ✔️ |
| COMMAND INFO | ✔️ | ❌ | ✔️ | ✔️ |
| COMMAND LIST | ✔️ | ❌ | ✔️ | ✔️ |
| CONFIG GET | ✔️ | ❌ | ✔️ | ✔️ |
| CONFIG HELP | ❌ | ❌ | ❌ | ❌ |
| CONFIG RESETSTAT | ❌ | ❌ | ❌ | ❌ |
| CONFIG REWRITE | ❌ | ❌ | ❌ | ❌ |
| CONFIG SET ①② | ✔️ | ❌ | ✔️ | ✔️ |
| DBSIZE | ✔️ | ❌ | ✔️ | ✔️ |
| DEBUG OBJECT | ❌ | ❌ | ❌ | ❌ |
| DEBUG SEGFAULT | ❌ | ❌ | ❌ | ❌ |
| FAILOVER | ❌ | ❌ | ❌ | ❌ |
| FLUSHALL | ✔️ | ❌ | ✔️ | ✔️ |
| FLUSHDB | ✔️ | ❌ | ✔️ | ✔️ |
| INFO | ✔️ | ❌ | ✔️ | ✔️ |
| LASTSAVE | ❌ | ❌ | ❌ | ❌ |
| LATENCY DOCTOR | ❌ | ❌ | ❌ | ❌ |
| LATENCY GRAPH | ❌ | ❌ | ❌ | ❌ |
| LATENCY HELP | ❌ | ❌ | ❌ | ❌ |
| LATENCY HISTOGRAM | ❌ | ❌ | ❌ | ❌ |
| LATENCY HISTORY | ❌ | ❌ | ❌ | ❌ |
| LATENCY LATEST | ❌ | ❌ | ❌ | ❌ |
| LATENCY RESET | ❌ | ❌ | ❌ | ❌ |
| LOLWUT | ✔️ | ❌ | ✔️ | ✔️ |
| MEMORY DOCTOR | ✔️ | ❌ | ✔️ | ❌ |
| MEMORY HELP | ✔️ | ❌ | ✔️ | ❌ |
| MEMORY MALLOC-STATS | ✔️ | ❌ | ✔️ | ❌ |
| MEMORY PURGE | ✔️ | ❌ | ✔️ | ❌ |
| MEMORY STATS | ✔️ | ❌ | ✔️ | ❌ |
| MEMORY USAGE | ✔️ | ❌ | ✔️ | ❌ |
| MODULE LIST | ❌ | ❌ | ❌ | ❌ |
| MODULE LOAD | ❌ | ❌ | ❌ | ❌ |
| MODULE LOADEX | ❌ | ❌ | ❌ | ❌ |
| MODULE UNLOAD | ❌ | ❌ | ❌ | ❌ |
| MONITOR | ✔️ | ❌ | ✔️ | ❌ |
| PSYNC | ❌ | ❌ | ❌ | ❌ |
| REPLICAOF | ❌ | ❌ | ❌ | ❌ |
| ROLE ② | ✔️ | ❌ | ✔️ | ❌ |
| SAVE | ❌ | ❌ | ❌ | ❌ |
| SHUTDOWN | ❌ | ❌ | ❌ | ❌ |
| SLAVEOF | ❌ | ❌ | ❌ | ❌ |
| SLOWLOG | ✔️ | ❌ | ✔️ | ✔️ |
| SLOWLOG HELP | ✔️ | ❌ | ✔️ | ✔️ |
| SLOWLOG RESET | ✔️ | ❌ | ✔️ | ✔️ |
| SWAPDB | ✔️ | ❌ | ✔️ | ✔️ |
| SYNC | ❌ | ❌ | ❌ | ❌ |
| TIME | ✔️ | ❌ | ✔️ | ✔️ |
### Sentinel
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| SENTINEL sentinels ② | ✔️ | ❌ | ✔️ | ❌ |
| SENTINEL get-master-addr-by-name ② | ✔️ | ❌ | ✔️ | ❌ |
### Set
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| SADD | ✔️ | ✔️ | ✔️ | ✔️ |
| SCARD | ✔️ | ✔️ | ✔️ | ✔️ |
| SDIFF | ✔️ | ⭕️ | ✔️ | ✔️ |
| SDIFFSTORE | ✔️ | ⭕️ | ✔️ | ✔️ |
| SINTER | ✔️ | ⭕️ | ✔️ | ✔️ |
| SINTERCARD | ✔️ | ⭕️ | ✔️ | ✔️ |
| SINTERSTORE | ✔️ | ⭕️ | ✔️ | ✔️ |
| SISMEMBER | ✔️ | ✔️ | ✔️ | ✔️ |
| SMEMBERS | ✔️ | ✔️ | ✔️ | ✔️ |
| SMISMEMBER | ✔️ | ✔️ | ✔️ | ✔️ |
| SMOVE | ✔️ | ⭕️ | ✔️ | ✔️ |
| SPOP | ✔️ | ✔️ | ✔️ | ✔️ |
| SRANDMEMBER | ✔️ | ✔️ | ✔️ | ✔️ |
| SREM | ✔️ | ✔️ | ✔️ | ✔️ |
| SSCAN | ✔️ | ✔️ | ✔️ | ✔️ |
| SUNION | ✔️ | ⭕️ | ✔️ | ✔️ |
| SUNIONSTORE | ✔️ | ⭕️ | ✔️ | ✔️ |
### Sorted Set
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| BZMPOP | ⭕️ | ⭕️ | ✔️ | ✔️ |
| BZPOPMAX | ⭕️ | ⭕️ | ✔️ | ✔️ |
| BZPOPMIN | ⭕️ | ⭕️ | ✔️ | ✔️ |
| ZADD | ✔️ | ✔️ | ✔️ | ✔️ |
| ZCARD | ✔️ | ✔️ | ✔️ | ✔️ |
| ZCOUNT | ✔️ | ✔️ | ✔️ | ✔️ |
| ZDIFF | ✔️ | ⭕️ | ✔️ | ✔️ |
| ZDIFFSTORE | ✔️ | ⭕️ | ✔️ | ✔️ |
| ZINCRBY | ✔️ | ✔️ | ✔️ | ✔️ |
| ZINTER | ✔️ | ✔️ | ✔️ | ✔️ |
| ZINTERCARD | ✔️ | ⭕️ | ✔️ | ✔️ |
| ZINTERSTORE | ✔️ | ⭕️ | ✔️ | ✔️ |
| ZLEXCOUNT | ✔️ | ✔️ | ✔️ | ✔️ |
| ZMPOP | ⭕️ | ⭕️ | ✔️ | ✔️ |
| ZMSCORE | ✔️ | ✔️ | ✔️ | ✔️ |
| ZPOPMAX | ✔️ | ✔️ | ✔️ | ✔️ |
| ZPOPMIN | ✔️ | ✔️ | ✔️ | ✔️ |
| ZRANDMEMBER | ✔️ | ✔️ | ✔️ | ✔️ |
| ZRANGE | ✔️ | ✔️ | ✔️ | ✔️ |
| ZRANGEBYLEX | ✔️ | ✔️ | ✔️ | ✔️ |
| ZRANGEBYSCORE | ✔️ | ✔️ | ✔️ | ✔️ |
| ZRANGESTORE | ⭕️ | ⭕️ | ✔️ | ✔️ |
| ZRANK | ✔️ | ✔️ | ✔️ | ✔️ |
| ZREM | ✔️ | ✔️ | ✔️ | ✔️ |
| ZREMRANGEBYLEX | ✔️ | ✔️ | ✔️ | ✔️ |
| ZREMRANGEBYRANK | ✔️ | ✔️ | ✔️ | ✔️ |
| ZREMRANGEBYSCORE | ✔️ | ✔️ | ✔️ | ✔️ |
| ZREVRANGE | ✔️ | ✔️ | ✔️ | ✔️ |
| ZREVRANGEBYLEX | ✔️ | ✔️ | ✔️ | ✔️ |
| ZREVRANGEBYSCORE | ✔️ | ✔️ | ✔️ | ✔️ |
| ZREVRANK | ✔️ | ✔️ | ✔️ | ✔️ |
| ZSCAN | ✔️ | ✔️ | ✔️ | ✔️ |
| ZSCORE | ✔️ | ✔️ | ✔️ | ✔️ |
| ZUNION | ✔️ | ⭕️ | ✔️ | ✔️ |
| ZUNIONSTORE | ✔️ | ⭕️ | ✔️ | ✔️ |
### Stream
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| XACK | ✔️ | ✔️ | ✔️ | ✔️ |
| XADD | ✔️ | ✔️ | ✔️ | ✔️ |
| XAUTOCLAIM | ✔️ | ✔️ | ✔️ | ✔️ |
| XCLAIM | ✔️ | ✔️ | ✔️ | ✔️ |
| XDEL | ✔️ | ✔️ | ✔️ | ✔️ |
| XGROUP | ✔️ | ✔️ | ✔️ | ✔️ |
| XGROUP CREATECONSUMER | ✔️ | ✔️ | ✔️ | ✔️ |
| XINFO | ✔️ | ✔️ | ✔️ | ✔️ |
| XLEN | ✔️ | ✔️ | ✔️ | ✔️ |
| XPENDING | ✔️ | ✔️ | ✔️ | ✔️ |
| XRANGE | ✔️ | ✔️ | ✔️ | ✔️ |
| XREAD | ⭕️ | ⭕️ | ✔️ | ✔️ |
| XREADGROUP | ⭕️ | ⭕️ | ✔️ | ✔️ |
| XREVRANGE | ✔️ | ✔️ | ✔️ | ✔️ |
| XTRIM | ✔️ | ✔️ | ✔️ | ✔️ |
### String
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| APPEND | ✔️ | ✔️ | ✔️ | ✔️ |
| DECR | ✔️ | ✔️ | ✔️ | ✔️ |
| DECRBY | ✔️ | ✔️ | ✔️ | ✔️ |
| GET | ✔️ | ✔️ | ✔️ | ✔️ |
| GETDEL | ✔️ | ✔️ | ✔️ | ✔️ |
| GETEX | ✔️ | ✔️ | ✔️ | ✔️ |
| GETRANGE | ✔️ | ✔️ | ✔️ | ✔️ |
| GETSET | ✔️ | ✔️ | ✔️ | ✔️ |
| LCS | ✔️ | ⭕️ | ✔️ | ✔️ |
| INCR | ✔️ | ✔️ | ✔️ | ✔️ |
| INCRBY | ✔️ | ✔️ | ✔️ | ✔️ |
| INCRBYFLOAT | ✔️ | ✔️ | ✔️ | ✔️ |
| MGET | ✔️ | ⭕️ | ✔️ | ✔️ |
| MSET | ✔️ | ⭕️ | ✔️ | ✔️ |
| MSETNX | ⭕️ | ⭕️ | ✔️ | ✔️ |
| PSETEX | ✔️ | ✔️ | ✔️ | ✔️ |
| SET | ✔️ | ✔️ | ✔️ | ✔️ |
| SETEX | ✔️ | ✔️ | ✔️ | ✔️ |
| SETNX | ✔️ | ✔️ | ✔️ | ✔️ |
| SETRANGE | ✔️ | ✔️ | ✔️ | ✔️ |
| STRALGO | ❌ | ❌ | ❌ | ❌ |
| STRLEN | ✔️ | ✔️ | ✔️ | ✔️ |
### Transactions
| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| DISCARD | ✔️ | ✔️ | ✔️ | ✔️ |
| EXEC | ✔️ | ✔️ | ✔️ | ✔️ |
| MULTI | ✔️ | ❌ | ✔️ | ❌ |
| UNWATCH | ✔️ | ❌ | ✔️ | ✔️ |
| WATCH | ⭕️ | ❌ | ✔️ | ❌ |
## 常见问题
Q：代理模式的集群架构和读写分离架构实例支持WAIT命令吗？
A：代理版本7.1.5及之后支持WAIT命令，版本过低可[升级代理版本](../user-guide/update-the-minor-version.md)。
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
