## 变量名称
添加自定义参数时，您可以选择直接使用CDN控制台上预设的变量。变量名称与变量含义见下表。

| 变量名称 | 变量含义 |
| --- | --- |
| $http_host | 请求头中的 Host 值。 |
| $http_user_agent | 请求头中的 User-Agent 值。 |
| $http_referer | 请求头中的 Referer 值。 |
| $http_content_type | 请求头中的 Content-Type 值。 |
| $http_x_forward_for | 请求头中的 X-Forwarded-For 值。 |
| $remote_addr | 请求的 Client IP 信息。 |
| $scheme | 请求的协议类型。 |
| $server_protocol | 请求的协议版本。 |
| $uri | 请求的原始 URI。 |
| $args | 请求的 Query String，不包含问号（?）。 |
| $request_method | 请求方法。 |
| $request_uri | uri+'?'+args 的内容。 |
