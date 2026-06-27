## 通过SQL的like语法进行精确的模糊查询
like语法满足标准的SQL like语法，在like语法中百分号（%）代表任意个字符。下划线 （_）代表单个字符。
示例：查询key满足abcd开头的所有日志，对应的查询分析语句如下所示。
* | select * from log where key like 'abcd%'
查询key不是以abcd开头的所有日志
* | select * from log where key not like 'abcd%'
