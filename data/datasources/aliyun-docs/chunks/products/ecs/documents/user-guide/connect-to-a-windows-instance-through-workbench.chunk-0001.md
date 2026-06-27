## 操作步骤
登录[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，在页面顶部选择资源组和地域。
找到目标实例后，单击远程连接，在对话框中，单击通过Workbench远程连接对应的立即登录。
在Workbench的登录实例页面，完成以下配置后，单击登录。

| 配置项 | 说明 |
| --- | --- |
| 实例 | 自动填充当前实例的信息。 |
| 连接方式 | 选择 终端连接 ，该方式底层使用 RDP 协议连接实例。 |
| 认证方式 | 密码认证 。 |
| 用户名 | Windows 实例默认用户名为 Administrator。 |
| 密码 | 若忘记或未设置密码，需先 [重置](instance-logon-credential-management.md) 。 为避免每次登录需要重复输入用户名和密码，可以 [记住密码](connect-to-a-windows-instance-through-workbench.md) ，以便之后使用。 |
| RDP 端口 （可选） | RDP 连接端口默认 3389，可在 登录实例 界面的 完整选项 > 端口 中修改。 |

单击登录后，系统因需要放行Workbench的IP地址段，可能会提示添加安全组规则，以允许其访问实例的RDP端口（默认为3389），可单击一键添加快速完成安全组的配置，具体配置的安全组规则以控制台界面为准。
重要
Workbench的远程连接会话最久维持6个小时，如果超过6小时没有任何操作，连接会自动断开，需要重新连接。
