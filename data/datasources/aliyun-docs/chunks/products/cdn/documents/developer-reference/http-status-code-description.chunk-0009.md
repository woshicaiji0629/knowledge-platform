### 411
原因：Length Required
原因释义：长度要求
说明：表示客户端未在请求头的Content-Length字段中指定请求主体的长度，而获取资源需要此信息。
解决措施：在客户端的请求头中携带Content-Length字段后重试；如无法估计长度时，可携带Transfer-Encoding: chunked字段定义分块传输编码。
