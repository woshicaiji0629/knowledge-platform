## 安全组内实例网络互通
默认情况下，同一普通安全组内的ECS实例间内网互通。为提高安全性，可以将组内连通策略调整为组内隔离，禁止实例间的内网互通。
[企业级安全组](basic-security-groups-and-advanced-security-groups.md)不支持修改组内连通策略。
当实例关联多个安全组时，只要其中任一安全组的组内连通策略设置为组内互通，实例间即可内网互通。
安全组的组内连通策略设置为组内隔离时，可通过配置安全组规则，允许实例间通信。
控制台
前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)，单击目标安全组ID进入安全组详情页。
在安全组详情页面，页签基本信息区域，单击修改组内网络连通策略。
安全组的组内连通策略已更改为组内隔离。
API
调用[ModifySecurityGroupPolicy](../developer-reference/api-ecs-2014-05-26-modifysecuritygrouppolicy.md)，修改普通安全组的组内连通策略。
