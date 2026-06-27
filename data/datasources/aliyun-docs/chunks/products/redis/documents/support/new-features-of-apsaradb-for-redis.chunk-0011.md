## Redis开源版2.8（已停售）
展开查看详情
新特性
关于Redis2.8的新特性请参见[2.8 release note](https://raw.githubusercontent.com/redis/redis/2.8/00-RELEASENOTES)。
支持[设置白名单](../getting-started/step-2-configure-whitelists.md)。
支持[VPC](../user-guide/enable-password-free-access.md)[免密](../user-guide/enable-password-free-access.md)，开启该功能后：
来自该VPC内的网络连接无需进行IP白名单验证。
来自该VPC内的网络连接执行AUTH命令时，直接返回OK，无需进行密码验证。
支持[SSL](../user-guide/configure-ssl-encryption.md)[加密](../user-guide/configure-ssl-encryption.md)。
支持设置[禁用命令](../user-guide/disable-high-risk-commands.md)。
支持代理模式（Proxy）的集群架构。
兼容性
关于社区演进的Breaking change请参见[2.8 release note](https://raw.githubusercontent.com/redis/redis/2.8/00-RELEASENOTES)。
不支持部分调试类命令和管理类命令，更多信息请参见[Redis](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)。
提供有限的CONFIG SET/GET命令支持：
CONFIG GET：仅返回部分配置项，不返回安全相关的配置项。
CONFIG SET：仅返回OK，不会修改参数。
提供有限的INFO命令支持，例如不返回Persistence、Replication等安全相关信息。
集群架构代理模式不支持部分命令，更多信息请参见[集群架构与读写分离实例的命令限制](../developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。
该文章对您有帮助吗？
反馈
