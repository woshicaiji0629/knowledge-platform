## 步骤一：创建索引
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
在LogStore的查询和分析页面的右上角，选择查询分析属性>属性。如果还未创建索引，需要先单击开启索引。全文索引和字段索引的更多信息、创建索引的详细步骤，请参见[创建索引](create-indexes.md)。
说明
如果需要查询日志中的所有字段，建议使用全文索引。如果只需查询部分字段、建议使用字段索引，减少索引流量。如果需要对字段进行分析（SELECT语句），必须创建字段索引。
配置字段索引。以下是JSON格式的日志示例和对应字段的配置。
{ "@timestamp": "2023-01-01T00:00:00+08:00", "remote_addr": "192.168.0.1", "remote_user": "-", "request": { "request_length": 123, "request_method": "GET", "request_uri": "/index.html" }, "status": 200, "http_referer": "http://example.com", "http_user_agent": "Mozilla/5.0", "server_protocal": "HTTP/1.1", "http_x_forward_for": "192.168.0.1", "upstream_addr": "10.0.0.1:8080", "time": { "request_time": 0.006, "upstream_response_time": 0.004 }, "body_bytes_sent": [123, 456] }
将content字段类型设为json，request下的叶子节点还包括request.request_length（long）、request.request_method（text）、request.request_uri（text）。所有字段均打开开启统计开关。
__topic__、__source__、__tag__是系统的保留字段，更多信息请参见[保留字段](reserved-fields.md)。
@timestamp、remote_addr、remote_user、http_referer、http_user_agent、status、server_protocal、http_x_forward_for、upstream_addr字段不包含叶子节点，可以在content字段下直接建立索引。
request、time字段包含叶子节点，而且叶子节点不是JSO
