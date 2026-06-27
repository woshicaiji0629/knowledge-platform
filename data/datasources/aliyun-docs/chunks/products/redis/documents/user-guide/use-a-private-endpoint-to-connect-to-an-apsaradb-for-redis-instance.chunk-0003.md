## 注意事项
由于部署架构的不同，相对标准架构来说，集群架构的实例在原生Redis命令的支持上有一定的区别（例如Lua存在使用限制等）。更多信息，请参见[集群架构实例的命令限制](../developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。
直连模式下，如果执行[变更实例配置](change-the-configurations-of-an-instance.md)，系统会采用Slot（槽）迁移的方式来完成，此场景下，客户端可能因访问到正在迁移的Slot而提示MOVED、TRYAGAIN等错误信息。如需确保请求的成功执行，请为客户端设计重试机制。更多信息，请参见[客户端重试指南](../use-cases/retry-mechanisms-for-redis-clients.md)。
直连模式支持使用SELECT命令切换DB，但部分Redis Cluster客户端（例如stackExchange.redis）不支持SELECT命令，如果使用该类客户端则只能使用DB0。
直连地址仅支持通过阿里云内网访问，且同时支持[VPC](enable-password-free-access.md)[免密](enable-password-free-access.md)和[账号密码认证](create-and-manage-database-accounts.md)。
