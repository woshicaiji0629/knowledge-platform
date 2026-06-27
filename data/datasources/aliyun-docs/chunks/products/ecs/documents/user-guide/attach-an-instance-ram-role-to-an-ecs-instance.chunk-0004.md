### 步骤二：为ECS实例授予RAM角色
将创建好的角色身份赋予指定的ECS实例。
控制台
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。在页面左侧顶部，选择目标资源所在的资源组和地域。
单击目标ECS实例ID，在实例详情页单击全部操作，选择实例设置>授予/收回RAM角色。
在对话框中，操作类型选择授予，然后选择授予ECS实例的RAM角色，单击确定。
API
调用[AttachInstanceRamRole](../api-attachinstanceramrole.md)接口将RAM角色授予ECS实例。
