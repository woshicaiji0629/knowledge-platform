### 将实例移出部署集
如果在删除部署集时，需要保留当前部署集内的实例，可以从部署集中移除实例后再进行删除，移除后实例保持原有状态。
重要
目标实例必须处于运行中或者已停止状态。具体操作，请参见[启动实例](start-an-instance.md)和[停止实例](stop-an-instance.md)。
调用[ModifyInstanceDeployment](../developer-reference/api-ecs-2014-05-26-modifyinstancedeployment.md)，并指定以下参数，将实例移出部署集：
RegionId：选择实例所属地域。例如，cn-hangzhou，即华东1（杭州）。
InstanceId：实例ID。例如，i-bp67acfmxazb4ph***。
DeploymentSetId：部署集ID。例如，ds-bp67acfmxazb4ph****。
RemoveFromDeploymentSet：是否将所选实例移出所选部署集。选择：true。
验证实例是否移除成功：接口调用成功，且返回状态码：200，证明移除成功。
