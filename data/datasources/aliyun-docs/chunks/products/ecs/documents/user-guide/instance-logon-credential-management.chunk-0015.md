## 设置非root用户的公钥
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
- 开启SSH服务的公钥认证功能
配置公钥后，必须在服务器上启用 SSH 公钥认证。否则，密钥登录会失败。
备份SSH配置文件/etc/ssh/sshd_config。
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
使用文本编辑器（如[Vim](use-the-vim-editor.md)）打开/etc/ssh/sshd_config文件，并找到PubkeyAuthentication参数，设置为yes，代表开启公钥认证功能。
sudo vim /etc/ssh/sshd_config
重启SSH服务以应用更改。
以Alibaba Cloud Linux 3为例：
sudo systemctl restart sshd部分操作系统（Ubuntu/Debian）的SSH服务名为ssh而非sshd，请根据实际情况调整。
重要
如果正通过SSH的方式连接到实例，重启服务可能导致连接中断，服务重启完成后，即可重新连接。
