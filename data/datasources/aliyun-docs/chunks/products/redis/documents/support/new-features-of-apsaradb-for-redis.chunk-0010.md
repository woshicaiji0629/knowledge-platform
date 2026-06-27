，将客户端IP透传给DB节点，更多信息请参见[参数支持](../user-guide/supported-parameters.md)。
兼容性
关于社区演进的Breaking change请参见[4.0 release note](https://raw.githubusercontent.com/redis/redis/4.0/00-RELEASENOTES)。
例如集群架构下需要记录Slot-to-Key的映射关系，所以相同数据的内存占用会比标准架构多。
例如集群架构下SORT命令不支持BY和GET参数。
不再支持[SSL](../user-guide/configure-ssl-encryption.md)[加密](../user-guide/configure-ssl-encryption.md)。
集群架构直连模式不支持部分CLUSTER命令，更多信息请参见[Redis](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)。
集群架构直连模式支持SELECT命令。
说明
您无法再使用SELECT命令来判断当前连接是否为Cluster mode，否则会导致误判。
在集群架构直连模式中，PUBLISH命令不会广播至其他节点。
关于其他命令的支持变化，请参见[Redis](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)。
