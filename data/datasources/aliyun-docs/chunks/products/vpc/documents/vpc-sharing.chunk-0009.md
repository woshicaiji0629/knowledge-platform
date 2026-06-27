建共享单元，并确保将AllowExternalTargets参数设为False。
二、创建云资源
登录交换机使用者的账号：
调用[DescribeVSwitches](developer-reference/api-vpc-2016-04-28-describevswitches.md)获取交换机列表。
在交换机列表中，过滤出共享交换机（ShareType字段值为Sharing）。
调用云资源的创建接口（例如ECS的[RunInstances](../../ecs/documents/developer-reference/api-ecs-2014-05-26-runinstances.md)），基于共享交换机创建云资源。
