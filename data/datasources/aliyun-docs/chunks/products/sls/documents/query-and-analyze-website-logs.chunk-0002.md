### 查询语句
查询包含Chrome的日志。
Chrome
查询请求时间大于60秒的日志。
request_time > 60
查询请求时间在60秒~120秒之间的日志。
request_time in [60 120]
查询GET请求成功（状态码为200~299）的日志。
request_method : GET and status in [200 299]
查询request_uri字段值为/request/path-2/file-2的日志。
request_uri:/request/path-2/file-2
