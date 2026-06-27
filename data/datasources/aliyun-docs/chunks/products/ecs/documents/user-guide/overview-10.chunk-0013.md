| 业务场景 | 参考文档 | 相关 API |
| --- | --- | --- |
| 2017 年 12 月 01 日之后使用公共镜像创建的 ECS 实例，默认预装 云助手 Agent ，因此，部分 ECS 实例仍需自行安装。 | [安装云助手](install-the-cloud-assistant-agent.md) [Agent](install-the-cloud-assistant-agent.md) | [InstallCloudAssistant](../api-installcloudassistant.md) [DescribeCloudAssistantStatus](../api-describecloudassistantstatus.md) |
| 通过程序调用 API。 | [通过](java-programs-use-cloud-assistant-to-manage-ecs-instances.md) [SDK](java-programs-use-cloud-assistant-to-manage-ecs-instances.md) [执行命令](java-programs-use-cloud-assistant-to-manage-ecs-instances.md) | 不涉及 |
| 新建一份云助手命令。 | [创建命令](create-a-command.md) | [RunCommand](../api-runcommand.md) [CreateCommand](../api-createcommand.md) |
| 对目标 ECS 实例执行已创建的命令。 | [执行命令](run-a-command.md) | [RunCommand](../api-runcommand.md) [InvokeCommand](../api-invokecommand.md) |
| 查看命令的执行状态，查看命令的执行结果，即在指定 ECS 实例中的实际输出信息。 | [查看执行结果及修复常见问题](check-execution-results-and-troubleshoot-common-issues.md) | [DescribeInvocations](../api-describeinvocations.md) [DescribeInvocationResults](../api-describeinvocationresults.md) |
| 修改已创建的命令，支持修改命令名称和描述。 | [修改命令](modify-a-command.md) | 不涉及 |
| 为一份云助手命令新增版本。或者您希望修改命令的名称、描述、类型、内容、执行路径或者超时时间等更多属性。 | [克隆命令](clone-a-c
