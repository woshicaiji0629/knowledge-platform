### LUA
重要
必须[设置参数](../user-guide/modify-the-values-of-parameters-for-an-instance.md)txn-isolation-lock的值为yes才能使用LUA脚本相关命令。
执行EVAL、EVALSHA、EVAL_RO、EVALSHA_RO命令，至少需要传入一个Key且numkeys参数的值大于0。

| 命令 | 是否支持 |
| --- | --- |
| EVAL① | ✔️ |
| EVALSHA① | ✔️ |
| EVAL_RO① | ✔️ |
| EVALSHA_RO① | ✔️ |
| SCRIPT | ✔️ |
