## Nginx
此处以CentOS 7.9操作系统、Nginx 1.20.1 版本配置为例介绍。具体请以您实际使用的环境为准。
修改Nginx服务配置文件并保存，修改点可参考下方说明。执行nginx -t命令查看配置文件所在路径，默认通常为/etc/nginx/nginx.conf，具体请以实际环境为准。
http { # ... server { listen 80; # BACKEND_SERVER是您配置重写Cookie时输入的Cookie名称；value您可使用自定义字符串。 add_header Set-Cookie "BACKEND_SERVER=value"; # ... } }
执行以下命令重新加载Nginx的配置文件。
sudo nginx -s reload
