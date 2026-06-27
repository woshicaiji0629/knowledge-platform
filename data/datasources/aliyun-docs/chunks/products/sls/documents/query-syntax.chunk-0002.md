## 全文查询
不针对具体的字段进行查询，支持通配符（*、?）和逻辑运算符（如and、or等）。
查询语法keywords1 [ and | or | not ] keywords2 ...
示例
示例1
查询关键词为GET相关的日志。则查询语法：GET。
示例2
查询关键词为GET或POST相关的日志。则查询语法：GET or POST。
示例3
查询以Jo开头相关的日志，例如Joe、Jon等。则查询语法为：Jo？。
