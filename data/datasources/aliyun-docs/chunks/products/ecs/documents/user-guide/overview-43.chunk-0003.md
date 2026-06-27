### 步骤一：创建部署集
通过控制台
访问[ECS](https://ecs.console.aliyun.com/deploymentSet/region)[控制台-部署集](https://ecs.console.aliyun.com/deploymentSet/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
在部署集页面，单击创建部署集。
在创建部署集对话框，输入部署集名称和描述，选择策略。如果选择高可用策略，还可以设置部署类型（物理机、机架或交换机）和亲和度（1~10）。[如何选择部署策略？](overview-43.md)
通过API
调用[CreateDeploymentSet](../developer-reference/api-ecs-2014-05-26-createdeploymentset.md)在指定的地域内创建一个部署集，并设置部署集策略。
如果部署策略为部署集组高可用策略，可指定参数GroupCount设置分组数量。
如果部署策略为高可用策略，可指定参数Type设置部署类型（host、rack或sw），默认值为host。
如果部署策略为高可用策略，可指定参数Affinity设置亲和度（1~10），默认值为1。
