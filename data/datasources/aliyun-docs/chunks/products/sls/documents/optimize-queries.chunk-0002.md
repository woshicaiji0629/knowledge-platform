（速度慢）
* | select count(distinct(ip))
低基数场景，使用多个distinct聚合函数。
多个distinct需要拷贝复制多次原始数据网络开销大，可以开启session开关enable_opt_distinct_aggs。示例如下：
查询和分析语句（速度快）
* | select count(1), count(distinct projectId), count(distinct logstore) from log
查询和分析语句（速度慢）
* | set session enable_opt_distinct_aggs=true; select count(1), count(distinct projectId), count(distinct logstore) from log
在SQL分析语句中指定获取需要的列，尽量不要读取所有列。
在SQL分析语句中，尽量只读取需要参与计算的列。如果要获取所有列，请使用查询语法。示例如下：
查询和分析语句（速度快）
* |select a,b c
查询和分析语句（速度慢）
* |select *
不是用于分组的列，尽量放在聚合函数中。
例如userid与用户名必定是一一对应的，您只需使用GROUP BY语法对userid进行分组统计即可。示例如下：
查询和分析语句（速度快）
* | select userid, arbitrary(username), count(1) group by userid
查询和分析语句（速度慢）
* | select userid, username, count(1) group by userid,username
尽量避免使用IN语法
尽量避免在分析语句中使用IN语法，您可以在查询语句中使用OR语法代替。示例如下：
查询和分析语句（速度快）
key: a or key: b or key: c | select count(1)
查询和分析语句（速度慢）
* | select count(1) where key in ('a','b')
该文章对您有帮助吗？
反馈
