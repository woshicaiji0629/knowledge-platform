# 【通知】StackExchange.Redis客户端升级建议
2024年02月，[StackExchange.Redis](https://github.com/StackExchange/StackExchange.Redis)社区修复了一个Bug：在使用StackExchange.Redis客户端访问代理（Proxy）模式的云数据库 Tair（兼容 Redis）实例时，如果使用了多数据库（Database，DB）功能，会出现超时报错。请将StackExchange.Redis升级至2.7.20及以上版本，可解决该问题。
