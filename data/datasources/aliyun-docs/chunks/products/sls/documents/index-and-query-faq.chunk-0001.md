## 如何在日志数据中搜索IP地址？
查询某个IP地址。
__tag__:__client_ip__:192.0.2.1
查询192.0.2.开头的日志。
__source__:192.0.2.*
查询包含192.168.XX.XX的日志。还可以使用正则表达式进行模糊查询，请参见[如何模糊查询日志？](how-do-i-query-logs-by-using-fuzzy-match.md)。
* | select * from log where key like '192.168.%.%'
