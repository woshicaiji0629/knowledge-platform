## 应用于生产环境
在实际生产环境中，建议通过以下操作提升远程连接安全。
- 主动验证主机指纹，防范中间人攻击
在第一次连接到实例时，应先[验证实例的主机密钥指纹](connect-to-a-linux-instance-by-using-an-ssh-key-pair.md)，确认连接的是目标实例而非攻击者的服务器。
- 禁用密码登录，强制使用密钥对
密钥对认证远比密码认证安全，可降低暴力破解风险。操作如下：
为实例[绑定密钥对](instance-logon-credential-management.md)。
禁用密码登录：登录实例，编辑/etc/ssh/sshd_config配置文件，找到PasswordAuthentication，修改为PasswordAuthentication no，重启SSH服务生效配置。
- 修改默认SSH端口
将默认22端口改为其他数值较大的非标准端口（如2222），可有效减少被恶意扫描。
放行新端口：在实例所属的安全组中[添加入方向规则](start-using-security-groups.md)，放行新的端口（如2222）
修改SSH服务端口：登录实例，编辑/etc/ssh/sshd_config配置文件，将#Port 22修改为Port 2222。重启SSH服务生效配置。
使用新端口连接：此后使用ssh命令时，需通过-p指定ssh的服务端口，例如：ssh -p 2222 username@instance_ip。
- 仅授权可信的IP访问实例
[修改安全组规则](start-using-security-groups.md)安全组规则，仅允许本机IP或其他受信任的IP访问实例SSH服务，拦截未知主机访问实例。
