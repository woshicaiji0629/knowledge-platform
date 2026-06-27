## CLI
通过[阿里云](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)[CLI](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)安装云助手Agent不区分操作系统类型。请替换命令中的<YOUR-REGION-ID>为ECS实例所在[地域](regions-and-zones.md)[ID](regions-and-zones.md)，<YOUR-INSTANCE-ID>为ECS实例ID。
Red Hat Enterprise Linux (RHEL) 不支持通过阿里云CLI安装。
调用[DescribeCloudAssistantStatus](../developer-reference/api-ecs-2014-05-26-describecloudassistantstatus.md)查询目标ECS实例是否安装了云助手Agent。
aliyun ecs DescribeCloudAssistantStatus --RegionId <YOUR-REGION-ID> --InstanceId.1 <YOUR-INSTANCE-ID> --output cols=CloudAssistantStatus rows=InstanceCloudAssistantStatusSet.InstanceCloudAssistantStatus[]
返回CloudAssistantStatus=true时，表示ECS实例已安装云助手Agent。
调用[InstallCloudAssistant](../developer-reference/api-ecs-2014-05-26-installcloudassistant.md)安装云助手Agent。
aliyun ecs InstallCloudAssistant --RegionId <YOUR-REGION-ID> --InstanceId.1 <YOUR-INSTANCE-ID>
调用[RebootInstance](../api-rebootinstance.md)重启ECS实例。
aliyun ecs RebootInstance --InstanceId <YOUR-INSTANCE-ID>
