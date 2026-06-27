## 实例内手动绑定（无需重启）
- 生成密钥对
不同的工具生成密钥对的步骤有所差别，本步骤以ssh-keygen工具为例。
输入以下命令生成密钥对。
ssh-keygen -t rsa -b 2048 -f id_rsa
参数说明：
-t rsa：代表密钥类型为rsa密钥对。
-b 2048：代表密钥长度为2048位。
-f id_rsa：代表生成密钥对的文件名以及保存位置。
系统将提示你输入一个口令（passphrase）。这个口令用于保护你的私钥。设置口令是推荐的安全措施。如果不需要口令，直接按回车键继续。
命令执行成功后，当前目录下会生成两个文件：
id_rsa：你的私钥。
id_rsa.pub：你的公钥。
重要
请妥善保存私钥，不要泄漏给他人。
- 为实例绑定公钥
在[使用](connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录实例](connect-to-a-linux-instance-by-using-a-password-or-key.md)后，按以下步骤操作。
为root用户绑定公钥与为非root用户绑定公钥操作有所差异，根据实际情况选择对应操作。
