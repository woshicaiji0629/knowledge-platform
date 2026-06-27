### Scripting and Functions

| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| EVAL | ⭕️ | ❌ | ✔️ | ✔️ |
| EVAL_RO | ⭕️ | ❌ | ✔️ | ✔️ |
| EVALSHA | ⭕️ | ❌ | ✔️ | ✔️ |
| EVALSHA_RO | ⭕️ | ❌ | ✔️ | ✔️ |
| FCALL | ⭕️ | ❌ | ✔️ | ✔️ |
| FCALL_RO | ⭕️ | ❌ | ✔️ | ✔️ |
| FUNCTION DELETE | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION DUMP | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION FLUSH | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION HELP | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION KILL | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION LIST | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION LOAD | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION RESTORE | ✔️ | ❌ | ✔️ | ❌ |
| FUNCTION STATS | ✔️ | ❌ | ✔️ | ❌ |
| SCRIPT DEBUG | ❌ | ❌ | ❌ | ❌ |
| SCRIPT EXISTS | ✔️ | ❌ | ✔️ | ❌ |
| SCRIPT FLUSH | ✔️ | ❌ | ✔️ | ❌ |
| SCRIPT KILL | ✔️ | ❌ | ✔️ | ❌ |
| SCRIPT LOAD | ✔️ | ❌ | ✔️ | ❌ |
