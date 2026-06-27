### ERR bad lua script for redis cluster, all the keys that the script uses should be passed using the KEYS array
可能原因：Proxy（代理）节点的Lua脚本限制。
解决方法：所有Key都应该由KEYS数组来传递，例如EVAL "return redis.call('mget', KEYS[1], KEYS[2])" 2 foo {foo}bar，不能使用Lua变量替换KEYS，更多信息请参见[集群架构特殊限制](usage-of-lua-scripts.md)。
