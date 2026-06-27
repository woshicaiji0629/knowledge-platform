7'
其中，website_log为LogStore名称。
统计请求路径访问情况。
使用[regexp_extract](regular-expression-functions-1.md)[函数](regular-expression-functions-1.md)提取request_uri字段中的文件部分，然后再使用[count](aggregate-function.md)[函数](aggregate-function.md)计算各个请求路径的访问次数。
* | SELECT regexp_extract(request_uri, '.*\/(file.*)', 1) file, count(*) as count group by file
查询结果中，file列值为file-5，count列值为17127，表示 file-5 的访问次数为 17127。
查询request_uri字段中包含%abc%的日志。
* | SELECT * where request_uri like '%/%abc/%%' escape '/'
查询结果返回匹配的日志记录，其request_uri字段值为/request/path-1/file-92 %abc%qereqwr，其中%abc%部分即为模糊匹配命中的内容。
