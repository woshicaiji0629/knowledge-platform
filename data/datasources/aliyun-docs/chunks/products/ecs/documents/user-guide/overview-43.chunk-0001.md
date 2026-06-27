## 适用范围
部署集不支持创建专有宿主机。
地域与可用区限制：实例与部署集必须在同一地域；策略为网络低时延的部署集内的实例，必须都在同一可用区。
实例规格族限制：大部分6代及以上实例支持高可用、部署集组高可用及网络低时延策略部署集。
不同部署策略仅支持创建特定的实例规格族
具体支持的规格族，以[DescribeDeploymentSetSupportedInstanceTypeFamily](../developer-reference/api-ecs-2014-05-26-describedeploymentsetsupportedinstancetypefamily.md)接口返回结果为准。
