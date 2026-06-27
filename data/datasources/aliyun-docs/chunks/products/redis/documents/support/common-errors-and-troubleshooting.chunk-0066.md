### panic: got 4 elements in cluster info address, expected 2 or 3
可能原因：您的Redis版本为7.0及以上，但未使用兼容的Go-redis客户端版本导致，更多信息请参见[redis/go-redis#2085](https://github.com/go-redis/redis/issues/2085)。
解决方案：升级、使用Go-redis客户端9.0及以上版本。
