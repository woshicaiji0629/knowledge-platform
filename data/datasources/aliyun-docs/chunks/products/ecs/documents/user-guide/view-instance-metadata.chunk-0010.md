## CLI
调用[ModifyInstanceMetadataOptions](../developer-reference/api-ecs-2014-05-26-modifyinstancemetadataoptions.md)，设置HttpEndpoint=enabled、HttpTokens=required切换实例元数据访问模式为仅加固模式。命令示例：
aliyun ecs ModifyInstanceMetadataOptions \ --region cn-hangzhou \ --RegionId 'cn-hangzhou' \ --InstanceId 'i-bp1******ke' \ --HttpEndpoint enabled \ --HttpTokens required
