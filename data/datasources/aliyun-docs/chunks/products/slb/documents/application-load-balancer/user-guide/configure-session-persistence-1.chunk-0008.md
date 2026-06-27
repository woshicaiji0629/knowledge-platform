# ... Listen 80 # BACKEND_SERVER是您配置重写Cookie时输入的Cookie名称；value您可使用自定义字符串。 Header always set Set-Cookie "BACKEND_SERVER=value" # ...
执行以下命令，重新加载Apache的配置文件，使以上改动生效。
sudo systemctl reload httpd.service
参考以上步骤，修改服务器组中其余后端服务器的配置。
