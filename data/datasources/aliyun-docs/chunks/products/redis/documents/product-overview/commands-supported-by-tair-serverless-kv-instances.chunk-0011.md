### Server management

| 命令 | 是否支持 |
| --- | --- |
| ACL | ❌ |
| BGREWRITEAOF | ❌ |
| BGSAVE | ❌ |
| BKLIST | ❌ |
| COMMAND | ✔️ |
| CONFIG | ❌ |
| DBSIZE | ✔️ |
| DEBUG | ❌ |
| FLUSHALL | ✔️ |
| FLUSHDB | ✔️ 重要 仅支持 FLUSHDB 命令同步执行模式，不支持异步执行模式。在生产环境中，请谨慎执行 FLUSHDB 命令。 |
| INFO | ✔️ |
| LASTSAVE | ❌ |
| LATENCY | ❌ |
| LOLWUT | ❌ |
| MEMORY | ❌ |
| MONITOR | ❌ |
| REWRITEAOF | ❌ |
| SAVE | ❌ |
| SHUTDOWN | ❌ |
| SLOWLOG | ✔️ |
| SWAPDB | ❌ |
| TIME | ✔️ |
