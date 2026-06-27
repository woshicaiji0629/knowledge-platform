### Connection management

| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| AUTH | ✔️ | ❌ | ✔️ | ✔️ |
| CLIENT CACHING | ❌ | ❌ | ❌ | ❌ |
| CLIENT GETNAME ② | ✔️ | ❌ | ✔️ | ❌ |
| CLIENT GETREDIR | ❌ | ❌ | ❌ | ❌ |
| CLIENT ID | ❌ | ❌ | ❌ | ❌ |
| CLIENT INFO | ❌ | ❌ | ❌ | ❌ |
| CLIENT KILL ② | ✔️ | ❌ | ✔️ | ❌ |
| CLIENT LIST ② | ✔️ | ❌ | ✔️ | ❌ |
| CLIENT NO-EVICT | ❌ | ❌ | ❌ | ❌ |
| CLIENT PAUSE | ❌ | ❌ | ❌ | ❌ |
| CLIENT REPLY | ❌ | ❌ | ❌ | ❌ |
| CLIENT SETNAME ② | ✔️ | ❌ | ✔️ | ❌ |
| CLIENT TRACKING | ❌ | ❌ | ❌ | ❌ |
| CLIENT TRACKINGINFO | ❌ | ❌ | ❌ | ❌ |
| CLIENT UNBLOCK | ❌ | ❌ | ❌ | ❌ |
| CLIENT UNPAUSE | ❌ | ❌ | ❌ | ❌ |
| ECHO | ✔️ | ❌ | ✔️ | ✔️ |
| HELLO | ✔️（有限制） | ✔️（有限制） | ✔️（有限制） | ✔️（有限制） |
| PING ② | ✔️ | ❌ | ✔️ | ✔️ |
| QUIT ② | ✔️ | ✔️ | ✔️ | ✔️ |
| RESET | ❌ | ❌ | ❌ | ❌ |
| SELECT | ✔️ | ✔️ | ✔️ | ✔️ |

说明
默认情况下，不支持使用HELLO命令。如需使用该命令，请确保Proxy的小版本[升级](../user-guide/update-the-minor-version.md)至7.0.9及以上，并且已[启用](../user-guide/modify-the-values-of-parameters-for-an-instance.md)hello_enabled参数。
