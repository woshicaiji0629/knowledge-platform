onfig /etc/ssh/sshd_config.bak
使用文本编辑器（如[Vim](use-the-vim-editor.md)）打开/etc/ssh/sshd_config文件，并找到PubkeyAuthentication参数，设置为yes，代表开启公钥认证功能。
sudo vim /etc/ssh/sshd_config
重启SSH服务以应用更改。
以Alibaba Cloud Linux 3为例：
sudo systemctl restart sshd部分操作系统（Ubuntu/Debian）的SSH服务名为ssh而非sshd，请根据实际情况调整。
重要
如果正通过SSH的方式连接到实例，重启服务可能导致连接中断，服务重启完成后，即可重新连接。
