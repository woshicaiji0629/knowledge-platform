## 背景信息
某网站将其所有的访问日志存储在LogStore（website_log）中，目前为了提升用户体验，需要对用户访问错误进行分析。所以，需求是将访问状态码为4XX的访问日志筛选出来，同时过滤掉访问的用户个人信息，并将结果写入新的LogStore（website_fail）,提供给业务分析人员使用。日志样例如下：
body_bytes_sent: 1061 http_user_agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5 remote_addr: 192.0.2.2 remote_user: vd_yw request_method: GET request_uri: /request/path-1/file-5 status: 400 time_local: 10/Jun/2021:19:10:59 error: Invalid time range
