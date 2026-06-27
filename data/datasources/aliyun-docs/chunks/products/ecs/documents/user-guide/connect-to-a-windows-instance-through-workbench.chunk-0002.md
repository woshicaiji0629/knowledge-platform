## 常见问题
如何记住密码？
为避免每次登录需要重复输入用户名和密码，可以将用户名和密码保存为凭据，以便之后使用。
该凭据不会与其他用户共享，仅供创建凭据者登录实例使用。
- 保存登录凭据
在登录实例时，勾选保存登录凭据，登录成功后，凭据即被保存。
- 使用凭据登录实例
在登录实例，设置用户名时，可通过使用凭据选项，使用已保存的凭证登录。
Workbench通过私网连接实例原理是什么？
在Workbench通过私网IP连接实例时，会自动在实例所属的VPC内创建反向访问规则，以建立安全的双向通信通道。可在>私网链路查看或管理。
Windows实例的默认登录名/初始登录名是什么？
Windows实例默认登录名为Administrator。
实例的默认密码/初始密码是什么？
实例没有默认密码或初始密码。如需设置，可[重置密码](instance-logon-credential-management.md)。
无法远程连接故障排查
在无法远程连接实例时，可优先通过以下自助问题诊断工具排查问题，也可通过[无法连接](../troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)[Linux](../troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)[实例的排查方法](../troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)自助排查。
单击一键诊断进入自助问题排查页面，并切换至目标地域。
单击实例无法连接下的发起诊断，根据界面提示选择问题实例并发起诊断。
诊断完成后，可根据提示完成修复操作。
该文章对您有帮助吗？
反馈
