## 绑定密钥对
在本机生成密钥对文件。
重要
安全起见，请不要在实例中通过ssh-keygen创建密钥对，请不要将生成的私钥保存在需要连接的ECS实例中。
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
为用户绑定公钥。
创建authorized_keys配置文件。
如果/root/.ssh目录或authorized_keys文件不存在，运行以下命令创建。
命令中<username>为待绑定公钥用户的用户名。sudo mkdir /home/<username>/.ssh sudo touch /home/<username>/.ssh/authorized_keys
添加公钥。
使用文本编辑器（如[Vim](use-the-vim-editor.md)）打开authorized_keys文件。
sudo vim /home/<username>/.ssh/authorized_keys
将你的公钥内容粘贴到文件中。可配置多个公钥，每个公钥占一行。配置完成后保存并关闭文件。
设置文件权限。
SSH 要求严格的权限设置，错误的权限会导致 SSH 登录失败。
运行以下命令，设置正确的权限。
sudo chown -R <username>:<username> /home/<username>/.ssh sudo chmod 700 /home/<username>/.ssh sudo chmod 600 /home/<username>/.ssh/authorized_keys
开启SSH服务的公钥认证功能。
配置公钥后，必须在服务器上启用 SSH 公钥认证。否则，密钥登录会失败。
备份SSH配置文件/etc/ssh/sshd_config。
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
使用文本编辑器（如[Vim](use-the-vim-editor.md)）打开/etc/ssh/sshd_config文件，并找到PubkeyAuthentication参数，设置为yes，代表开启公钥认证功能。
sudo vim /etc/ssh/ssh
