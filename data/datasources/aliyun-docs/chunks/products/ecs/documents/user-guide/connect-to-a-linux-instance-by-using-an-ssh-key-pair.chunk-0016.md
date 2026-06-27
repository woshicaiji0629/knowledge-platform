# 为Web服务器配置一个别名 "web-server" Host web-server HostName 47.98.xxx.xxx User root Port 22 （可选）如果使用密钥对登录，请指定私钥路径，使用密码登录请忽略 IdentityFile /path/to/your/private_key.pem # 可以为其他服务器添加更多配置 Host other-server HostName 8.123.xxx.xxx User ecs-user Port 2222 IdentityFile ~/.ssh/another_key.pem
参数说明：
Host：服务器的别名，可自定义。
HostName：实例的公网IP地址。
User：登录用户名。
Port：SSH端口号（默认为22）。
IdentityFile：私钥文件的绝对路径。
使用别名快速连接
保存config文件后，可以直接使用别名来连接实例。
