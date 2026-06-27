## 实例内
[使用](connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录实例](connect-to-a-linux-instance-by-using-a-password-or-key.md)后执行以下命令，查看主机密钥指纹：
for f in /etc/ssh/ssh_host_*_key.pub; do ssh-keygen -l -f "$f"; done
输出示例：
1024 SHA256:9C******co root@Connect-Instance-Example (DSA) 256 SHA256:u6******SU root@Connect-Instance-Example (ECDSA) 256 SHA256:iQ******jg root@Connect-Instance-Example (ED25519) 3072 SHA256:8R******64 root@Connect-Instance-Example (RSA)
请仔细核对本地客户端提示的指纹（如上例中的 SHA256:******）是否与日志中显示的指纹完全一致。若不一致，则可能正在遭受中间人攻击，需切换至安全网络环境后重试连接。
- 如何通过SSH的config配置文件简化连接命令？
每次连接都输入完整的ssh -i /path/to/key.pem username@instance_ip命令较为繁琐。通过在本地创建和配置SSHconfig文件，可以为服务器设置别名，简化连接命令。
找到或创建config文件
