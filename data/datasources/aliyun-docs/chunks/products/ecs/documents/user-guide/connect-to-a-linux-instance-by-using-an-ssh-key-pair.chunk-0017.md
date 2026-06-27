# 直接使用别名连接，SSH会自动读取config中的IP、用户名和密钥信息 ssh web-server
- 连接时出现Connection timed out或提示连接超时？
表示客户端无法连接到服务器。排查顺序：
检查公网IP是否正确。
检查安全组是否放行端口。
检查实例是否处于运行状态。
使用[ECS](https://ecs.console.aliyun.com/troubleshooting)[控制台-自助问题排查](https://ecs.console.aliyun.com/troubleshooting)排查异常。
- 密码输入正确，但提示Permission denied, please try again
表示服务器拒绝了密码。排查顺序：
在控制台[重置密码](instance-logon-credential-management.md)后重试。
使用[ECS](https://ecs.console.aliyun.com/troubleshooting)[控制台-自助问题排查](https://ecs.console.aliyun.com/troubleshooting)排查异常。
- 使用密钥对登录时提示Permission denied (publickey)？
表示服务器拒绝了密钥。排查顺序：
在控制台重新[绑定](instance-logon-credential-management.md)密钥对后重试。
检查私钥文件路径及是否与实例匹配。
（macOS系统下）检查私钥文件权限是否为400或600。
使用[ECS](https://ecs.console.aliyun.com/troubleshooting)[控制台-自助问题排查](https://ecs.console.aliyun.com/troubleshooting)排查异常。
- 通过SSH命令登录实例时，提示WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
这是SSH的安全机制：在第一次连接实例后，会记住主机密钥指纹，后续连接时若指纹不一致，会提示该错误。可能是由于执行过更换系统盘、更换操作系统、删除了实例系统中的主机密钥文件等操作。
解决办法：[验证实例的主机密钥指纹](connect-to-a-linux-instance-by-using-an-ssh-key-pair.md)，若无误，执行以下命令，删除本地保存的主机密钥指纹。
ssh-keygen -R <实例公网IP地址>
该文章对您有帮助吗？
反馈
