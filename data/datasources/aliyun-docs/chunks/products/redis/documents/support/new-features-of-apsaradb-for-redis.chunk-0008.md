### 兼容性
关于社区演进的Breaking change，请参见[5.0 release note](https://raw.githubusercontent.com/redis/redis/5.0/00-RELEASENOTES)。
例如Lua脚本执行的命令不再对结果进行排序。
账号名称的大小写敏感。
开通VPC免密后，免密连接可通过AUTH切换不同账号。
说明
若您的不同账号设置了不同权限，请确保应用程序在权限范围内执行命令，否则会出现权限不足的报错。
开放READONLY和READWRITE命令。
云原生版与经典版存在部分差异：云原生版实例开通VPC免密后，所有连接仍需进行白名单验证，且无法设置#no_loose_check-whitelist-always参数。
关于其他命令的支持变化，请参见[Redis](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)。
