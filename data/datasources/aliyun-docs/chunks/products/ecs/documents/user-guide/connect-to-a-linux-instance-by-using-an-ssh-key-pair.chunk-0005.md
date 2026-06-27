## 密码登录
打开终端（Terminal）。
发起远程连接。
ssh <实例登录名>@<实例公网IP地址>示例：ssh root@47.98.xxx.xxx
（首次连接时）验证主机指纹
当首次连接一台新的ECS时，会显示类似下方的信息，提示验证主机密钥指纹。
这是SSH的一项安全机制，为确保安全，请[获取实例的主机密钥指纹后比对差异](connect-to-a-linux-instance-by-using-an-ssh-key-pair.md)。若不一致，则说明正在遭受中间人攻击，请切换到安全的网络环境下重新连接实例。
确认主机指纹无误后，输入yes并按回车。
The authenticity of host '47.98.xxx.xxx (47.98.xxx.xxx)' can't be established. ED25519 key fingerprint is SHA256:AbCdEf123456... This key is not known by any other names. Are you sure you want to continue connecting (yes/no/[fingerprint])?
输入密码，进入实例
输入密码时屏幕不会显示字符，这是正常现象，输入完成后按回车即可。
密码验证通过后，将看到系统的登录欢迎信息（具体内容因操作系统镜像而异），并且命令提示符会变为[<实例登录名>@<hostname> ~]$的形式。表示已成功登录到ECS实例。
Welcome to Alibaba Cloud Elastic Compute Service ! [root@Connect-Instance-Example ~]#
