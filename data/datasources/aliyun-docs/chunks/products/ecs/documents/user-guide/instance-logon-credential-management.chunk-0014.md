## 设置root用户的公钥
创建authorized_keys配置文件。
如果/root/.ssh目录或authorized_keys文件不存在，运行以下命令创建。
sudo mkdir /root/.ssh sudo touch /root/.ssh/authorized_keys
添加公钥。
使用文本编辑器（如[Vim](use-the-vim-editor.md)）打开authorized_keys文件。
sudo vim /root/.ssh/authorized_keys
将你的公钥内容粘贴到文件中。可配置多个公钥，每个公钥占一行。配置完成后保存并关闭文件。
设置文件权限。
SSH 要求严格的权限设置，错误的权限会导致 SSH 登录失败。
运行以下命令，设置正确的权限。
sudo chmod 700 /root/.ssh sudo chmod 600 /root/.ssh/authorized_keys
