### ERR for redis cluster, eval/evalsha number of keys can't be negative or zero
可能原因：执行EVAL和EVALSHA命令未传入Key或numkeys参数的值未大于0。
解决方法：执行EVAL和EVALSHA命令时，至少需要传入一个Key且numkeys参数的值大于0，更多信息请参见[Lua](usage-of-lua-scripts.md)[脚本基本语法](usage-of-lua-scripts.md)。
