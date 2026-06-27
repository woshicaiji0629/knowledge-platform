## 离线重置密码（需重启）
重要
离线重置密码需要重启实例才能生效。重启可能会中断实例中的业务，请合理规划时间。
进入[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，选择地域与资源组，找到待操作实例。
根据以下指引，进入重置实例密码功能对话框。

| 简捷版控制台 | 标准版控制台 |
| --- | --- |
| 单击 重置密码 。 | 单击 操作 列下的 重置实例密码 。 |

在重置实例密码对话框，完成如下配置后单击确认修改等待密码重置完成。
新密码/确认密码：输入新实例密码。请为实例设置强密码（包含大小写字母、数字、特殊字符）。
重置密码的方式：离线重置密码。
[重启实例](restart-instances.md)。
重置密码需要重启实例才能生效。可在业务低峰期重启，以免影响业务稳定性。
[通过](log-on-to-an-instance-by-using-vnc.md)[VNC](log-on-to-an-instance-by-using-vnc.md)[连接并登录实例](log-on-to-an-instance-by-using-vnc.md)。
VNC登录成功，代表在操作系统中，密码已经成功重置。
如果VNC登录实例成功，但Workbench等工具登录失败，证明密码已经重置成功，可能是SSH配置存在问题，建议通过[无法连接](../troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)[Linux](../troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)[实例的排查方法](../troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)。
