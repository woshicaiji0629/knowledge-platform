### 2. 构建接口的请求对象
在构建请求对象之前，请查看该接口的[API](api-ecs-2014-05-26-describeinstances.md)[文档](api-ecs-2014-05-26-describeinstances.md)获取参数信息。
说明
请求对象命名规则：{API名称}Request，例如DescribeInstances该接口的请求对象为DescribeInstancesRequest。
// 构造请求对象 DescribeInstancesRequest request = new DescribeInstancesRequest().setRegionId("cn-hangzhou");
