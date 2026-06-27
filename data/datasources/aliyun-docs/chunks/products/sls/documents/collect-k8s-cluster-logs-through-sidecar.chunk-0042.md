r: - request_method: GET request_protocol: HTTP/1.1 request_uri: /wp-admin/admin-ajax.php?action=rest-nonce status: 200 time_local: 16/Aug/2024:14:37:52 +0800 |

配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>正则解析：
正则表达式：用于匹配日志，支持自动生成或手动输入：
自动生成：
单击自动生成正则表达式。
在日志样例中划选需要提取的日志内容。
单击生成正则。
日志样例区域内显示已粘贴的 Apache Combined 格式访问日志样例（包含客户端 IP、时间戳、请求方法路径、状态码、Referer 及 User-Agent 等字段）。
手动输入：根据日志格式手动输入正则表达式。
配置完成后，单击验证，测试正则表达式是否能够正确解析日志内容。
日志提取字段：为提取的日志内容（Value），设置对应的字段名（Key）。
其他参数请参考[场景二：结构化日志](collect-k8s-cluster-logs-through-sidecar.md)中的通用配置参数说明。
