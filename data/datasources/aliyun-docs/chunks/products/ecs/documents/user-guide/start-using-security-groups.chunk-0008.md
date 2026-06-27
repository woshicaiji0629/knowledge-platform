## 安全组间实例网络互通
将其他安全组设为规则的授权对象时，可允许其他安全组内实例，通过内网访问本安全组内的实例。图中为安全组A设置了入方向的授权对象安全组B后，安全组B内的实例可以通过内网访问安全组A内的实例。
[企业级安全组](basic-security-groups-and-advanced-security-groups.md)规则不支持添加授权对象为安全组的规则。
控制台
前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)，单击目标安全组ID进入安全组详情页。
在目标安全组详情页面，选择规则需要控制方向，单击增加规则。
在新建安全组规则页面选择访问来源为安全组或跨账号安全组。
API
调用[AuthorizeSecurityGroup](../developer-reference/api-ecs-2014-05-26-authorizesecuritygroup.md)在安全组入方向规则中设置SourceGroupId授权已创建的安全组。
调用[AuthorizeSecurityGroupEgress](../developer-reference/api-ecs-2014-05-26-authorizesecuritygroupegress.md)在安全组出方向规则中设置DestGroupId授权已创建的安全组。
