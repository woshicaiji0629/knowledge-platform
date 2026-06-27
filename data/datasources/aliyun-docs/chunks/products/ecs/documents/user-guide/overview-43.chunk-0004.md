### 步骤二：在部署集内创建或添加ECS实例
通过控制台
重要
ECS实例的规格、地域、数量需符合使用限制要求。具体，请参见[使用限制](overview-43.md)。
在部署集内创建新实例：
在部署集列表页面，找到目标部署集，在部署集的操作列中，单击创建实例，跳转到自定义购买页面完成实例配置选项。
将已创建实例加入部署集：具体操作，可参见[调整实例所属部署集](overview-43.md)。
通过API
在部署集内创建新实例：调用[RunInstances](../developer-reference/api-ecs-2014-05-26-runinstances.md)接口，并指定DeploymentSetId（部署集ID）。
为部署集组高可用策略设置分组数量。
将已创建实例加入至部署集：调用[ModifyInstanceDeployment](../developer-reference/api-ecs-2014-05-26-modifyinstancedeployment.md)接口，并指定参数InstanceId（实例ID）和DeploymentSetId（部署集ID）。
说明
如果指定的部署集对应策略为AvailabilityGroup（部署集组高可用策略），可以通过参数DeploymentSetGroupNo指定实例在部署集中的分组号。
