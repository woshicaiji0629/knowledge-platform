### Multiple databases are not supported on this server; cannot switch to database
可能原因：集群架构不支持执行SELECT命令。
解决方法：将cluster_compat_enable参数设置为0（即关闭原生Redis Cluster语法兼容），具体操作请参见[设置参数](../user-guide/modify-the-values-of-parameters-for-an-instance.md)，然后重启客户端应用后重试。
