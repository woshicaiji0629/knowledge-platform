### 查询实例的详细信息
您可以调用[DescribeInstances](../api-describeinstances.md)接口查询一台或多台ECS实例的详细信息。
示例1：根据实例ID查询ECS实例
假设查询实例ID为i-bp14a7xie8erwsvo****的实例信息。
请求示例
aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --InstanceIds '["i-bp14a7xie8erwsvo****"]' \ --output cols=InstanceId,InstanceName,Description,ImageId,Status rows=Instances.Instance[]
返回示例
InstanceId | InstanceName | Description | ImageId | Status ---------- | ------------ | ----------- | ------- | ------ i-bp1de173dp87k5uv**** | ecs_cli_demo | | aliyun_3_x64_20G_alibase_20240528.vhd | Running
示例2：根据标签查询ECS实例
假设查询绑定owner:zhangsan标签的ECS实例信息。
请求示例
aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --Tag.1.Key owner \ --Tag.1.Value zhangsan \ --output cols=InstanceId,InstanceName,Description,ImageId,Status rows=Instances.Instance[]
返回示例
InstanceId | InstanceName | Description | ImageId | Status ---------- | ------------ | ----------- | ------- | ------ i-bp1de173dp87k5uv**** | ecs_cli_demo | | aliyun_3_x64_20G_alibase_20240528.vhd | Running
示例3：根据镜像ID查询ECS实例
查询镜像为m-bp12qhgxbmp5eh02****标签的ECS实例信息。
请求示例
aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --ImageId m-bp12qhgxbmp5eh02**** \ --output cols=InstanceId,InstanceNa
