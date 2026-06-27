## 操作步骤
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
单击目标实例ID进入实例详情页，单击远程连接。
单击展开其他登录方式，找到通过会话管理远程连接，确保会话管理已开启（全地域），如果显示会话管理已关闭，请先打开功能开关。
重要
打开会话管理功能开关前，请确保RAM用户具有查看会话管理配置的DescribeUserBusinessBehavior权限和打开或关闭会话管理功能的ModifyUserBusinessBehavior权限，详细的权限策略示例，请参见[前提条件](connect-to-an-instance-by-using-session-manager-1.md)。
单击免密登录。
连接成功后，Linux实例默认以ecs-assist-user用户登录实例，Windows实例默认以system用户登录。以Linux实例为例，效果如图所示。
