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
除此之外，Redis Cluster对使用Lua脚本增加了一些限制，云数据库 Tair（兼容 Redis）集群架构在此基础上存在额外限制，更多信息请参见[集群架构特殊限制](../support/usage-of-lua-script
