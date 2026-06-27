## Windows系统
重要
默认情况下，Windows系统仅支持两个不同的用户同时通过RDP远程连接实例，如需两个以上用户同时登录Windows实例，需要使用微软的[远程桌面服务（Remote Desktop Services）](https://learn.microsoft.com/zh-cn/windows-server/remote/remote-desktop-services/remote-desktop-services-overview)的能力。
[使用](connect-to-a-windows-instance-through-workbench.md)[Workbench](connect-to-a-windows-instance-through-workbench.md)[登录实例](connect-to-a-windows-instance-through-workbench.md)，按以下步骤操作：
- 创建用户

| 打开控制面板，找到 用户账户 ， 单击下面的 更改账户类型 。 |  |
| --- | --- |
| 在 管理账户 页面，单击 添加用户账户 ，进入 添加用户 页面。 |  |
| 在添加用户页面，根据界面提示，设置新用户的用户名及密码。 本示例以创建 exampleuser 为例，请根据需求设置 用户名 。 单击 下一步 ，然后单击 完成 。完成新用户的创建。 |  |

- 将新用户添加到Remote Desktop Users用户组
只有Remote Desktop Users用户组下的用户，才能以远程登录的方式登录实例。

| 在任务栏的搜索框搜索 计算机管理 ， 单击搜索到的 计算机管理 进入 计算机管理 页面。 |  |
| --- | --- |
| 在 系统工具 > 本地用户和组 > 组 下，找到 Remote Desktop Users 用户组。双击进入 Remote Desktop Users 属性 页面。 |  |
| 操作流程如图所示。 在 Remote Desktop Users 属性 页面，单击 添加 。 输入 步骤 2 中创建用户的用户名，单击 检查名称 ，之后输入框会自动根据输入的用户名补全用户的名称全称。 单击 确定 。在 Remote Desktop Users 属性 页面依次单击 应用 、 确定 。完成将用户添加到用户组的操作。 |  |

- （验证）使用新创建的用户远程登录到ECS实例。
