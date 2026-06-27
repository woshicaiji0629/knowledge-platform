## Tair（企业版）持久内存型和磁盘型额外的命令限制
说明
以下为实例最新小版本的兼容情况。若您的实例存在更多限制，请您升级实例小版本后重试，具体操作请参见[升级小版本与代理版本](../user-guide/update-the-minor-version.md)。
如需了解Release notes，请参见[Tair](../support/apsaradb-for-redis-enhanced-edition-1.md)[小版本发布日志](../support/apsaradb-for-redis-enhanced-edition-1.md)。
关于设置参数的具体操作，请参见[设置参数](../user-guide/modify-the-values-of-parameters-for-an-instance.md)。
持久内存型

| 命令族 | 限制项 |
| --- | --- |
| Keys（键） | MOVE 与 RENAME 系列命令，需通过 pena_rename_move_compatible_enabled 参数开启兼容模式，才能执行。 |
| Server（数据库管理） | 不支持命令：SWAPDB。 |

磁盘型

| 命令族 | 限制项 |
| --- | --- |
| Hyperloglog | 不支持命令：PFADD、PFCOUNT、PFMERG。 |
| Keys（键） | 不支持命令：MOVE、OBJECT、SORT、TOUCH。 Rename、RenameNX 最大支持修改 max-rename-commit-size 大小（默认为 16 MB）的 Key。 |
| Server（数据库管理） | 不支持命令：SWAPDB。 仅支持 FLUSHDB 命令同步执行模式，不支持异步执行模式。在生产环境中，请谨慎执行 FLUSHDB 命令。 |
| Stream（流） | 不支持该系列命令。 |
| Scripting（Lua 脚本） | Lua 脚本相关命令，例如 EVAL、EVALSHA、SCRIPT EXISTS 等，需通过 txn-isolation-lock 参数和 #no_loose_lua-strict-mode 参数开启、控制。 |
| Transactions（事务） | 事务相关命令，例如 DISCARD、EXEC、WATCH 等，可通过 txn-isolation-lock 参数开启、控制。 |

该文章对您有帮助吗？
反馈
