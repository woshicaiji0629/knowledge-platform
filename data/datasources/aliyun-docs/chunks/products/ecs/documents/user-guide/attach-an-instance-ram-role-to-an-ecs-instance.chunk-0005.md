### 步骤三：验证角色授予是否成功
在集成应用前，确认ECS实例已成功获取角色身份。
控制台
登录ECS实例。
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。在页面左侧顶部，选择目标资源所在的资源组和地域。
进入目标实例详情页，单击远程连接，选择通过Workbench远程连接。根据页面提示登录，进入终端页面。
查询实例当前被授予的角色名称。
该命令返回已授予的角色名称列表，用于验证角色是否成功绑定。
curl http://100.100.100.200/latest/meta-data/ram/security-credentials/
成功：若返回授予的角色名称，表示角色授予成功。
失败：
返回404 Not Found：表示实例未被授予任何RAM角色。请返回[步骤二](attach-an-instance-ram-role-to-an-ecs-instance.md)，检查授予操作是否成功。
若命令无响应或连接超时：表示实例无法访问元数据服务。请检查安全组和防火墙是否拦截了IP地址100.100.100.200。
API
调用[DescribeInstanceRamRole](../developer-reference/api-ecs-2014-05-26-describeinstanceramrole.md)接口查询ECS实例被授予RAM角色。
