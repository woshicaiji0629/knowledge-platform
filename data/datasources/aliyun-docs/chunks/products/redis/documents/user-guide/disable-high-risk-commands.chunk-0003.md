## 执行结果
通过[redis-cli](use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)连接实例并执行被禁用的命令FLUSHALL后，Tair将返回错误提示：ERR command 'FLUSHALL' not support for normal user或者NOPERM this user has no permissions to run the 'flushall' command。
