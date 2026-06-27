### ERR unknown command 'xxx'
可能原因：当前的实例不支持此命令。
如出现：ERR unknown command 'WAIT'，是由于云上集群架构代理模式不支持WAIT命令，需要用直连模式。
解决方法：检查当前实例版本的命令支持情况，更多信息请参见[Tair（企业版）命令支持与限制](https://help.aliyun.com/zh/tair/developer-reference/limits-on-commands-supported-by-tair#concept-1960075)、[Redis](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持与限制](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)及[集群架构与读写分离实例的命令限制](../developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。
说明
最新小版本将提供更丰富的功能与稳定的服务，建议将实例的小版本升级到最新，具体操作请参见[升级小版本与代理版本](../user-guide/update-the-minor-version.md)。
