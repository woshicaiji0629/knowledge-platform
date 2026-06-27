### 兼容性
关于社区演进的Breaking change请参见[6.0 release note](https://raw.githubusercontent.com/redis/redis/6.0/00-RELEASENOTES)。
账号管理与社区ACL账号权限存在部分差异，如下为云数据库 Tair（兼容 Redis）的账号管理说明：
默认账号为default，实例名账号（例如r-bp1857n194kiuv****）为另外一个单独账号。
通过AUTH命令连接Redis时，若未指定账号则使用default账号鉴权。
关于其他命令的支持变化，请参见[Redis](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)。
