### Scripting and Functions
说明
磁盘型执行EVAL、EVALSHA、SCRIPT EXISTS等Lua脚本相关命令存在限制，详情请参见[命令限制](limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| EVAL | ✔️ | ✔️ | ✔️ |
| EVAL_RO | ➖ | ➖ | ✔️ |
| EVALSHA | ✔️ | ✔️ | ✔️ |
| EVALSHA_RO | ➖ | ➖ | ✔️ |
| FCALL | ➖ | ➖ | ✔️ |
| FCALL_RO | ➖ | ➖ | ✔️ |
| FUNCTION DELETE | ➖ | ➖ | ✔️ |
| FUNCTION DUMP | ➖ | ➖ | ✔️ |
| FUNCTION FLUSH | ➖ | ➖ | ✔️ |
| FUNCTION HELP | ➖ | ➖ | ✔️ |
| FUNCTION KILL | ➖ | ➖ | ✔️ |
| FUNCTION LIST | ➖ | ➖ | ✔️ |
| FUNCTION LOAD | ➖ | ➖ | ✔️ |
| FUNCTION RESTORE | ➖ | ➖ | ✔️ |
| FUNCTION STATS | ➖ | ➖ | ✔️ |
| SCRIPT DEBUG | ❌ | ❌ | ❌ |
| SCRIPT EXISTS | ✔️ | ✔️ | ✔️ |
| SCRIPT FLUSH | ✔️ | ✔️ | ✔️ |
| SCRIPT KILL | ✔️ | ✔️ | ✔️ |
| SCRIPT LOAD | ✔️ | ✔️ | ✔️ |
