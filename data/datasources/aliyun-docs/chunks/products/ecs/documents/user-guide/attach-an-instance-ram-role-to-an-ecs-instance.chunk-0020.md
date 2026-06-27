### 收回/更改ECS的实例RAM角色
通过控制台收回/更改
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。在页面左侧顶部，选择目标资源所在的资源组和地域。
找到要操作的ECS实例，选择>实例设置>授予/收回RAM角色。
收回实例RAM角色：操作类型选择收回，单击确定。
更改实例RAM角色：操作类型选择授予，选择所需的实例RAM角色，单击确定完成更改。
通过API收回/更改
收回实例RAM角色：调用[DetachInstanceRamRole](../api-detachinstanceramrole.md)接口收回实例RAM角色。
更改实例RAM角色：
调用[DetachInstanceRamRole](../api-detachinstanceramrole.md)接口收回实例RAM角色。
调用[AttachInstanceRamRole](../api-attachinstanceramrole.md)接口重新为实例授予新的RAM角色。
