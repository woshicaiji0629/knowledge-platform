bytes_sent "$http_referer" ' '"$http_user_agent" $request_time $request_length';
生产环境中，此处的log_format必须与Nginx配置文件（通常位于 /etc/nginx/nginx.conf文件中）中的定义保持一致。
日志解析示例：

| 原始日志 | 结构化解析日志 |
| --- | --- |
| 192.168.*.* - - [15/Apr/2025:16:40:00 +0800] "GET /nginx-logo.png HTTP/1.1" 0.000 514 200 368 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.*.* Safari/537.36" | body_bytes_sent: 368 http_referer: - http_user_agent : Mozi11a/5.0 (Nindows NT 10.0; Win64; x64) AppleMebKit/537.36 (KHTML, like Gecko) Chrome/131.0.x.x Safari/537.36 remote_addr:192.168.*.* remote_user: - request_length: 514 request_method: GET request_time: 0.000 request_uri: /nginx-logo.png status: 200 time_local: 15/Apr/2025:16:40:00 |

单击下一步，进入查询分析配置页面，采集配置生效需要1分钟左右，单击自动刷新，出现预览数据，说明采集配置已生效。
