### 手动排查问题
在远程连接失败时，如果您没有收到系统返回的报错信息，您可以根据以下步骤手动排查问题：
步骤一：使用阿里云Workbench工具测试远程登录
通过阿里云提供的Workbench工具进行远程登录，Workbench工具在远程登录出现异常时会返回具体的错误信息及解决方案。测试步骤如下：
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
单击目标实例ID进入实例详情页，单击远程连接。
在弹出的远程连接对话框中，单击通过Workbench远程连接对应的立即登录。
测试是否可以远程登录。
Workbench工具将自动填充登录目标实例所需的基本信息，请确认基本信息的正确性并输入登录的用户名和认证信息。并根据以下结果进行处理：通过Workbench远程登录Linux实例的具体操作，请参见[通过](user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[远程登录](user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)。
如仍然无法登录，Workbench工具会返回错误提示和解决方案，请根据提示进行处理。处理完毕后重新使用Workbench工具进行远程登录测试。为了便于您解决问题，列举Workbench工具使用时常见的异常问题：[通过](through-vnc-instance-remote-connection-problems.md)[VNC](through-vnc-instance-remote-connection-problems.md)[远程连接实例的问题](through-vnc-instance-remote-connection-problems.md)
如可以通过Workbench工具正常登录，说明目标实例上的SSH服务正常运行，即排除SSH服务端异常的可能性，继续执行[步骤二：检查网络](trou
