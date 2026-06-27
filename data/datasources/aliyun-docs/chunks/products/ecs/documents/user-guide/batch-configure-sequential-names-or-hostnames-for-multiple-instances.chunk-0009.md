## API
您可以调用[RunInstances](../api-runinstances.md)来创建ECS实例，并指定实例名称和主机名称。以下内容主要描述自动排序名称的参数配置：
UniqueSuffix配置为true，系统会对InstanceName和HostName自动排序，增加的后缀从001开始，按实例数量依次递增。自动排序的具体规则，请参见[自动排序](batch-configure-sequential-names-or-hostnames-for-multiple-instances.md)。
本示例创建三台自动排序实例，具体参数配置如下：
Amount：3
InstanceName：ecs
HostName：ecshost
UniqueSuffix：true
按照本文示例，生成的实例名分别为ecs001、ecs002、ecs003，生成的主机名分别为ecshost001、ecshost002、ecshost003。
