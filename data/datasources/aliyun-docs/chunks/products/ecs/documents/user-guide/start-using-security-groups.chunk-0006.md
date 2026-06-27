## 为辅助弹性网卡关联安全组
安全组实际作用在ECS实例的[弹性网卡](eni-overview.md)上。实例有多张弹性网卡时，为弹性网卡关联不同的安全组，并配置差异化的安全组规则，可以实现实例内部网络流量的分级管控与业务隔离。
控制台
前往[ECS](https://ecs.console.aliyun.com/networkInterfaces)[控制台-弹性网卡](https://ecs.console.aliyun.com/networkInterfaces)页面，单击目标辅助网卡的ID，进入辅助弹性网卡详情页。
单击更换安全组，勾选要关联的安全组，单击确定。
API
调用[JoinSecurityGroup](../developer-reference/api-ecs-2014-05-26-joinsecuritygroup.md)将弹性网卡加入到指定的安全组。
调用[LeaveSecurityGroup](../developer-reference/api-ecs-2014-05-26-leavesecuritygroup.md)将弹性网卡移出指定的安全组。
使用[ModifyNetworkInterfaceAttribute](../developer-reference/api-ecs-2014-05-26-modifynetworkinterfaceattribute.md)为弹性网卡指定多个安全组。
