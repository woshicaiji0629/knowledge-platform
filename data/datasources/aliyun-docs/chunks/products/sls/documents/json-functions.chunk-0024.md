### 示例
SQL
示例1
将字符串[1,2,3]转换为JSON数组[1, 2, 3]。
查询和分析语句（[调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DICogfCBTRUxFQ1QganNvbl9wYXJzZSgnWzEsIDIsIDNdJyk%3D)）
* | SELECT json_parse('[1, 2, 3]')
查询和分析结果为[1,2,3]。
示例2
提取logging字段中的各个子字段。
字段样例如下，logging字段为JSON对象，包含message、processName、thread、threadName、module、funcName、levelName、process等键值对。
查询和分析语句（[调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/internal-etl-log?encode%3Dbase64%26queryString%3DKnwgU0VMRUNUIG1hcF9rZXlzKHRyeV9jYXN0KGpzb25fcGFyc2UobG9nZ2luZykgQVMgbWFwKHZhcmNoYXIsIGpzb24pKSk%3D)）
*| SELECT map_keys(try_cast(json_parse(logging) AS map(varchar, json)))
查询和分析结果为["funcName","levelname","message","module","process","processName","thread","threadName"]。
SPL
将字符串[1,2,3]转换为JSON数组[1, 2, 3]。
SPL语句
* | extend a = json_parse('[1, 2, 3]')
SPL结果
返回结果中，字段a的值为[1, 2, 3]。
