## 方案概览
在Nginx配置模式下，Logtail会根据log_format中的定义将日志内容结构化。Nginx访问日志相关的主要指令为log_format和access_log，通常在配置文件/etc/nginx/nginx.conf中配置。log_format用来定义日志格式；access_log用来指定日志文件的存放路径。
日志格式和存放路径
log_format和access_log的默认值如下所示。
log_format main '$remote_addr - $remote_user [$time_local] "$request" ' '$request_time $request_length ' '$status $body_bytes_sent "$http_referer" ' '"$http_user_agent"'; access_log /var/log/nginx/access.log main;
日志字段说明如下所示：

| 字段名称 | 说明 |
| --- | --- |
| remote_addr | 客户端 IP 地址。 |
| remote_user | 客户端用户名。 |
| time_local | 服务器时间，前后必须加上中括号（[]）。 |
| request | 请求的 URI 和 HTTP 协议。 |
| request_time | 整个请求的总时间，单位为秒。 |
| request_length | 请求的长度，包括请求行、请求头和请求正文。 |
| status | 请求状态。 |
| body_bytes_sent | 发送给客户端的字节数，不包括响应头的大小。 |
| http_referer | URL 跳转来源。 |
| http_user_agent | 客户端浏览器等信息。 |

原始日志
Nginx根据log_format的定义生成日志：
192.168.1.1 - - [11/Dec/2024:11:21:03 +0800] "GET /nginx-logo.png HTTP/1.1" 0.000 514 200 368 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
被采集到日志服务LogStore中的日志：日志采集到日志服务后，在查询分析页面选择原始日志视图，可看到每条日志按键值对格式逐字段解析展示，同时附带实例名、日志路径、Unix 时间戳等元信息。
