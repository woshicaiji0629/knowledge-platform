### 步骤三：结果验证
以任意一台可以访问公网的终端为例，测试访问ALB的HTTP请求是否能够重定向至HTTPS。
打开终端的命令行窗口。
执行curl -v -L -H "Accept-Language: zh-CN,zh" http://<自有域名>.
如下图所示，收到状态码302，表示访问ALB的请求重定向至HTTPS，应答服务器为ECS01。
重复执行命令，应答服务器变为ECS02。
