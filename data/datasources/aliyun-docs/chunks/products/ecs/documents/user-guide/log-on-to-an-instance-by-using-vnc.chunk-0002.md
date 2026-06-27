## 常见问题
- 如何粘贴命令？
在实例中选中需要粘贴内容的地方。
在界面左上角，单击复制命令输入。
最大支持2000个字符，暂不支持中文等非标准键盘值特殊字符。
在文本内容对话框中，输入拷贝的内容，然后单击确定。
- 如何发送远程命令？
可通过发送远程命令功能模拟特定快捷键操作，例如Windows解除锁屏（CTRL+ALT+DELETE）或Linux切换虚拟终端（CTRL+ALT+F1到CTRL+ALT+F10切换到该实例的不同虚拟终端。）。
使用VNC方式成功登录ECS实例。
在界面左上角，单击发送远程命令，在下拉菜单中单击对应命令即可模拟特定快捷键。
- 忘记密码或未设置实例密码怎么办？
连接时，忘记或未设置实例密码时，可进入实例详情页，在全部操作中选择重置实例密码，根据界面提示完成重置密码操作。
- 连接时，出现“该资源目前的状态不支持此操作”是什么原因？
TDX机密计算环境的实例暂不支持VNC连接。
- ECS默认用户名、初始用户名、默认登录名、初始登录名是什么？
Linux系统实例：默认为root，若创建实例时设置了使用ecs-user则为ecs-user。
Windows系统实例：默认为Administrator。
- ECS默认密码、初始密码、默认远程密码、初始登录密码是什么？
没有。
出于安全考虑，阿里云不会为ECS实例设置默认或初始密码。如在创建实例时未设置密码。
- 连接时提示“当前操作未被授权，请联系主账号进行RAM授权后再执行操作”怎么办？
需要[授予](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)RAM用户ecs:DescribeInstances和ecs:DescribeInstanceVncUrl权限。权限策略文件如下：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "ecs:DescribeInstances", "ecs:DescribeInstanceVncUrl" ], "Resource": "*" } ] }
- 登录实例时出现Login Incorrect或密码不正确，请再试一次，怎么办？
请保证密码输入无误，若忘记密码，请进入实例详情页，在全部操作中选择重置实例密码，根据界面提示完成重置密码操作后再连接。
- 为什么Linux实例连接后是黑屏？
Linux实例进入休眠状态时会显示黑屏，可单击键盘上任意键唤醒。
- 在轻量应用服务器中如何通过VNC连接？
VNC远程连接在轻量应用服务器中功能名为[救援登录](https://help.aliyun.com/zh/simple-application-server/user-guid
