## 方式一：免密连接（推荐）
免密登录时，默认通过[会话管理](connect-to-an-instance-by-using-session-manager-2.md)方式连接，未开启会话管理则通过[临时](workbench-password-free-login-principle-temporary-ssh-key-pair.md)[SSH](workbench-password-free-login-principle-temporary-ssh-key-pair.md)[密钥对](workbench-password-free-login-principle-temporary-ssh-key-pair.md)方式连接。
登录[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，在页面顶部选择资源组和地域。
找到目标实例后，单击远程连接，在对话框中，单击通过Workbench远程连接对应的立即登录。
在Workbench的登录实例页面，选择免密连接后，输入用户名后，单击登录。
实例登录成功界面如图所示：
重要
Workbench的远程连接会话最久维持6个小时，如果超过6小时没有任何操作，连接会自动断开，需要重新连接，建议[后台执行](../configure-linux-to-keep-the-process-running-after-the-ssh-client-is-disconnected.md)长任务。
