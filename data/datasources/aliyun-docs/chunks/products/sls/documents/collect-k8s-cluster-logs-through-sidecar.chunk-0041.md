### 正则解析
通过正则表达式提取日志字段，并将日志解析为键值对形式，每个字段都可以被独立查询和分析。
效果示例：

| 未经任何处理的原始日志 | 使用正则解析插件 |
| --- | --- |
| 127.0.0.1 - - [16/Aug/2024:14:37:52 +0800] "GET /wp-admin/admin-ajax.php?action=rest-nonce HTTP/1.1" 200 41 "http://www.example.com/wp-admin/post-new.php?post_type=page" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0" | body_bytes_sent: 41 http_referer: http://www.example.com/wp-admin/post-new.php?post_type=page http_user_agent: Mozilla/5.0 (Windows NT 10.0; Win64; ×64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0 remote_addr: 127.0.0.1 remote_user: - request_method: GET request_protocol: HTTP/1.1 request_uri: /wp-admin/admin-ajax.php?action=rest-nonce status: 200 time_local: 16/Aug/2024:14:37:52 +0800 |
