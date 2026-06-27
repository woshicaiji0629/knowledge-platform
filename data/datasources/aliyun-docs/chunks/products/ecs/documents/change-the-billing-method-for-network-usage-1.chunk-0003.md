## 按使用流量转按固定带宽
以下操作指导您如何在ECS控制台将实例的公网带宽计费模式由按使用流量计费转换为按固定带宽计费。您也可以通过调用[ModifyInstanceNetworkSpec](developer-reference/api-ecs-2014-05-26-modifyinstancenetworkspec.md)API的方式进行转换。
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
找到待转换的实例，并进入实例详情页面，在全部操作中选择升降配 >更改带宽。
重要
对于包年包月的ECS实例，如果您操作过带宽临时升级，并选择将公网带宽的计费方式从按固定带宽转换为按使用流量，那么所有已生效和未生效的带宽临时升级订单都将被取消并退款。
在高流量使用场景中，公网带宽采用按使用流量方式计费可能会增加您的网络流量费用。建议您预先进行预算评估，以确保该计费方式符合您的预算计划。关于如何选择公网带宽计费方式，请参见[公网带宽计费](public-bandwidth.md)。
在弹出的更改带宽对话框中，操作方式选择更改带宽，带宽计费方式选择按固定带宽，并设置固定带宽值。
仔细阅读页面下方的产品服务协议和服务等级协议内容，单击立即更改。转换完成后，新配置立即生效。
说明
阿里云也为您提供了[在实例列表页执行批量操作](user-guide/batch-operation-of-ecs-instances-through-the-ecs-console.md)的功能，选中多个待转换的实例后，进行批量转换操作。
