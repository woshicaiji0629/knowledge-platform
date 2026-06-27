2.168.*.* remote_user: - request_length: 514 request_method: GET request_time: 0.000 request_uri: /nginx-logo.png status: 200 time_local: 15/Apr/2025:16:40:00 |

配置步骤：在Logtail配置页面的处理配置区域
添加解析插件：单击添加处理插件，根据实际格式配置[正则解析、分隔符解析、JSON 解析等插件](host-text-log-collection-auto-install.md)。此处以采集NGINX日志为例，选择原生处理插件>NGINX模式解析。
NGINX日志配置：将 Nginx 服务器配置文件（nginx.conf）中的log_format定义完整地复制并粘贴到此文本框中。
示例：
log_format main '$remote_addr - $remote_user [$time_local] "$request" ''$request_time $request_length ''$status $body_bytes_sent "$http_referer" ''"$http_user_agent"';
重要
此处的格式定义必须与服务器上生成日志的格式完全一致，否则将导致日志解析失败。
通用配置参数说明：以下参数在多种数据解析插件中都会出现，其功能和用法是统一的。
原始字段：指定要解析的源字段名。默认为content，即采集到的整条日志内容。
解析失败时保留原始字段：推荐开启。当日志无法被插件成功解析时（例如格式不匹配），此选项能确保原始日志内容不会丢失，而是被完整保留在指定的原始字段中。
解析成功时保留原始字段：选中后，即使日志解析成功，原始日志内容也会被保留。
