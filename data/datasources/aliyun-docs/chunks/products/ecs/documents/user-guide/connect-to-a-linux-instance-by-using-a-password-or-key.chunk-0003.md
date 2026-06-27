###

| 配置项 | 说明 |
| --- | --- |
| 实例 | 自动填充当前实例的信息。 |
| 连接方式 | 选择 终端连接 ，该方式底层使用 SSH 协议连接实例。 |
| 认证方式 | 重要 SSH 密钥认证相比密码有较高的安全性，推荐 [绑定密钥对](instance-logon-credential-management.md) 后，通过 SSH 密钥认证方式登录。 SSH 密钥认证 用户名 ：Linux 实例默认用户名为 root。 若创建实例时设置使用 ecs-user 作为登录名，则需输入 ecs-user。 私钥 ：输入私钥文件的内容。如果私钥文件设置了口令，还需输入 密钥口令 。 为避免每次登录需要重复输入用户名和私钥，可以 [记住密钥](connect-to-a-linux-instance-by-using-a-password-or-key.md) ，以便之后使用。 SSH 端口 （可选）：SSH 连接端口默认 22，可在 登录实例 界面的 完整选项 > 端口 中修改。 密码认证 用户名 ：Linux 实例默认用户名为 root。 若创建实例时设置使用 ecs-user 作为登录名，则需输入 ecs-user。 密码 ：若忘记密码或未设置需先 [重置密码](instance-logon-credential-management.md) 。 为避免每次登录需要重复输入用户名和密码，可以 [记住密码](connect-to-a-linux-instance-by-using-a-password-or-key.md) ，以便之后使用。 SSH 端口 （可选）：SSH 连接端口默认 22，可在 登录实例 界面的 完整选项 > 端口 中修改。 |

单击登录后，系统因需要放行Workbench的IP地址段，可能会提示添加安全组规则，以允许其访问实例的SSH端口（默认为22），可单击一键添加快速完成安全组的配置，具体配置的安全组规则以控制台界面为准。
登录成功界面如图所示。
重要
Workbench的远程连接会话最久维持6个小时，如果超过6小时没有任何操作，连接会自动断开，需要重新连接，建议[后台执行](../configure-linux-to-keep-the-process-running-after-the-ssh-client-is-disconnected.md)长任务。
