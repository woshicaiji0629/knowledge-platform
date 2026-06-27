## API
通过API安装云助手Agent不区分操作系统类型。
调用[DescribeCloudAssistantStatus](../developer-reference/api-ecs-2014-05-26-describecloudassistantstatus.md)查询目标ECS实例是否安装了云助手Agent。
CloudAssistantStatus返回false时，表示未安装。
若实例未安装云助手Agent，则调用[InstallCloudAssistant](../developer-reference/api-ecs-2014-05-26-installcloudassistant.md)安装云助手Agent。
安装完成之后，调用[RebootInstance](../api-rebootinstance.md)重启ECS实例使安装生效。
