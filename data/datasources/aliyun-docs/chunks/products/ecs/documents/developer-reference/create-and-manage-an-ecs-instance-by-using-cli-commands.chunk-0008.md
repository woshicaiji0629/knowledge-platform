### 连接实例
获取实例的公网IP信息。
调用[DescribeInstances](api-ecs-2014-05-26-describeinstances.md)，通过实例ID（i-bp1ducce5hs1jm98****）获取实例的公网IP信息。
请求示例
aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --InstanceIds '["i-bp1ducce5hs1jm98****"]'
返回示例
参数PublicIpAddresses为实例的公网IP信息。
连接ECS实例。
ssh <用户名>@<公网IP>
