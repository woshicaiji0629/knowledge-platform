| 字段 | 说明 |
| --- | --- |
| body_bytes_sent | 发送给客户端的 http body 的字节数。 |
| client_ip | 请求客户端 IP 地址。 |
| client_port | 请求客户端端口。 |
| host | 优先从请求参数中获取 host，如果获取不到则从 host header 取值，如果还是获取不到则以处理请求的后端服务器 IP 地址作为 host。 |
| http_host | 请求报文 host header 的内容。 |
| http_referer | 负载均衡收到的请求报文中 HTTP 的 referer header 的内容。 |
| http_user_agent | 负载均衡收到的请求报文中 http_user_agent header 的内容。 |
| http_x_forwarded_for | 负载均衡收到的请求报文中 x-forwarded-for header 的内容。 |
| http_x_real_ip | 客户端真实的 IP 地址。 |
| read_request_time | 负载均衡读取请求的时间，单位：毫秒。 |
| request_length | 请求报文的长度，包括 startline、http header 和 http body。 |
| request_method | 请求报文的方法。 |
| request_time | 负载均衡收到第一个请求报文的时间到 SLB 返回应答之间的间隔时间，单位：秒。 |
| request_uri | 负载均衡收到的请求报文的 URI。 |
| scheme | 请求的 scheme，包括 http、https。 |
| server_protocol | 负载均衡收到的 HTTP 协议的版本，例如 HTTP/1.0 或 HTTP/1.1。 |
| slb_vport | 负载均衡的监听端口。 |
| slbid | 负载均衡实例 ID。 |
| ssl_cipher | 建立 SSL 连接使用的密码，例如 ECDHE-RSA-AES128-GCM-SHA256 等。 |
| ssl_protocol | 建立 SSL 连接使用的协议，例如 TLSv1.2。 |
| status | 负载均衡应答报文的状态。 |
| tcpinfo_rtt | 客户端 TCP 连接时间，单位：微秒。 |
| time | 日志记录时间。 |
| upstream_addr | 后端服务器的 IP 地址和端口。 |
| upstream_response_time | 从与后端建立连接开始到接受完数据然后关闭连接为止的时间，单位：秒。 |
| upstream_status | 负载均衡收到的后端服务器的响应状态码。
