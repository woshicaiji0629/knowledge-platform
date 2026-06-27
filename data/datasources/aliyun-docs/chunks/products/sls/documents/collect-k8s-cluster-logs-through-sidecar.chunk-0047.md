### Apache日志解析
根据Apache日志配置文件中的定义将日志内容结构化，解析为多个键值对形式。
效果示例：

| 未经任何处理的原始日志 | Apache 通用日志格式 combined 解析 |
| --- | --- |
| 1 192.168.1.10 - - [08/May/2024:15:30:28 +0800] "GET /index.html HTTP/1.1" 200 1234 "https://www.example.com/referrer" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.X.X Safari/537.36" | http_referer:https://www.example.com/referrer http_user_agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.X.X Safari/537.36 remote_addr:192.168.1.10 remote_ident:- remote_user:- request_method:GET request_protocol:HTTP/1.1 request_uri:/index.html response_size_bytes:1234 status:200 time_local:[08/May/2024:15:30:28 +0800] |

配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>APACHE模式解析：
日志格式：combined
APACHE配置字段：系统会根据日志格式自动填充配置。
重要
请务必核对自动填充的内容，确保与服务器上 Apache 配置文件（通常位于/etc/apache2/apache2.conf）中定义的 LogFormat 完全一致。
其他参数请参考[场景二：结构化日志](collect-k8s-cluster-logs-through-sidecar.md)中的通用配置参数说明。
