## API
您可以调用[RunInstances](../api-runinstances.md)来创建ECS实例，并指定实例名称和主机名称。以下内容主要描述指定排序名称的参数配置：
InstanceName（实例名称）和HostName（主机名）指定排序的配置格式为name_prefix[begin_number,bits]name_suffix。具体规则，请参见[指定排序](batch-configure-sequential-names-or-hostnames-for-multiple-instances.md)。
本文以创建三台实例，实例名称和主机名称以k8s-node-开头，从0006开始排序，主机名以-ecshost结尾为例，具体参数配置如下：
Amount：3
InstanceName：k8s-node-[6,4]
HostName：k8s-node-[6,4]-ecshost
重要
本示例仅用于指定排序，此处UniqueSuffix保持默认不开启。
按照本文示例，生成的实例名分别为k8s-node-0006、k8s-node-0007、k8s-node-0008，生成的主机名分别为k8s-node-0006-ecshost、k8s-node-0007-ecshost、k8s-node-0008-ecshost。
