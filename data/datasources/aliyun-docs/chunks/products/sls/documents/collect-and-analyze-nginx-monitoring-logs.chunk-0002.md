## 步骤一：配置stub_status模块
说明
本文以Linux系统为例介绍操作步骤。
执行以下命令，安装和启动Nginx。
sudo yum install -y nginx sudo systemctl restart nginx
执行以下命令确认Nginx已具备[status](https://nginx.org/en/docs/http/ngx_http_stub_status_module.html)[功能](https://nginx.org/en/docs/http/ngx_http_stub_status_module.html)。
nginx -V 2>&1 | grep -o with-http_stub_status_module
返回以下信息，表示已支持status功能。
with-http_stub_status_module
配置Nginx服务器。
打开Nginx的配置文件，在server {..}块中添加以下代码。关于nginx_status的更多信息，请参见[Nginx status](https://easyengine.io/tutorials/nginx/status-page/)。
location /nginx_status { stub_status on; #启用stub_status模块 access_log off; allow ${服务器IP}; #允许访问的服务器IP deny all; # 拒绝所有其他 IP 地址访问这个状态页面 }
执行以下命令，验证配置结果。
nginx -t sudo systemctl restart nginx curl http://${服务器IP}/nginx_status
返回以下结果，表示配置成功。
Active connections: 1 server accepts handled requests 2507455 2507455 2512972 Reading: 0 Writing: 1 Waiting: 0
