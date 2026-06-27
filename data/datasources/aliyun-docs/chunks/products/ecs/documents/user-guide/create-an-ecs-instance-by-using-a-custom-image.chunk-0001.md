## CLI
在通过[RunInstances](../developer-reference/api-ecs-2014-05-26-runinstances.md)或[CreateInstance](../developer-reference/api-ecs-2014-05-26-createinstance.md)创建实例时，可通过配置ImageId为对应自定义镜像的ID。命令示例如下：
执行该命令后，会创建一台使用自定义镜像（ID为m-bp1******pi）的实例。aliyun ecs RunInstances \ --region cn-hangzhou \ --RegionId 'cn-hangzhou' \ --ImageId 'm-bp1******pi' \ --InstanceType 'ecs.g7.large' \ --VSwitchId 'vsw-bp1******trg' \ --SecurityGroupId 'sg-bp1******dgl' \ --SystemDisk.Size 40 \ --SystemDisk.Category cloud_essd \
