## 前提条件
[开通直连访问](enable-the-direct-connection-mode.md)。
将客户端地址加入[实例白名单](../getting-started/step-2-configure-whitelists.md)。
使用[Jedis](https://github.com/xetorthio/jedis/wiki/Getting-started)、[PhpRedis](https://github.com/phpredis/phpredis)等支持Redis Cluster的客户端。
说明
使用不支持Redis Cluster的客户端，可能因客户端无法重定向请求到正确的分片而获取不到需要的数据。
您可以在Redis官网的[客户端列表](https://redis.io/clients)里查找更多支持Redis Cluster的客户端。
客户端所在的ECS与实例在同一VPC网络（相同VPC ID）。
