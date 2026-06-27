## 创建采集配置
心跳状态为OK后，单击下一步，进入Logtail配置页面：
配置名称：填写配置名称，如：nginx-access-log-config。
文件路径：日志采集的路径，第一个输入框填写文件夹路径：/var/log/nginx，第二个输入框填写文件名access.log。
处理配置：
日志样例：单击添加日志样例，粘贴一行示例日志：
192.168.*.* - - [15/Apr/2025:16:40:00 +0800] "GET /nginx-logo.png HTTP/1.1" 0.000 514 200 368 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.*.* Safari/537.36"
处理模式：单击NGINX模式解析插件，在NGINX日志配置中配置log_format，复制并粘贴如下内容，单击确认。
log_format main '$remote_addr - $remote_user [$time_local] "$request" ' '$status $body_bytes_sent "$http_referer" ' '"$http_user_agent" $request_time $request_length';
生产环境中，此处的log_format必须与Nginx配置文件（通常位于 /etc/nginx/nginx.conf文件中）中的定义保持一致。
日志解析示例：
