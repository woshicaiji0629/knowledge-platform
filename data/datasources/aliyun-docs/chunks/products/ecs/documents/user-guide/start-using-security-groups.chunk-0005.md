## 为实例关联安全组
当您为ECS实例关联安全组时，实际上是在为ECS实例的主网卡关联安全组。
控制台
前往[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)单击目标实例ID进入实例详情页。
在实例详情页切换至安全组页签，在安全组列表页单击更换安全组，按需将安全组加入实例或者移除实例。关联多个安全组时，安全组规则会合并，且按照优先级排序生效。
API
调用[ModifyInstanceAttribute](../developer-reference/api-ecs-2014-05-26-modifyinstanceattribute.md)，为一台ECS实例设置多个安全组。
调用[JoinSecurityGroup](../developer-reference/api-ecs-2014-05-26-joinsecuritygroup.md)，将一台ECS实例加入到指定的安全组。
调用[LeaveSecurityGroup](../developer-reference/api-ecs-2014-05-26-leavesecuritygroup.md)，将一台ECS实例移出指定的安全组。
