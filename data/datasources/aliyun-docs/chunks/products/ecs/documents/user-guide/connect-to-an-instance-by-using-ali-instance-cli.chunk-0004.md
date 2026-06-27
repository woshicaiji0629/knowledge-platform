## 阿里云CLI
如果您已经配置好了阿里云CLI，您可以通过以下命令查询实例运行状态。关于该API的更多参数说明，请参见[查询实例的状态信息列表](../developer-reference/api-ecs-2014-05-26-describeinstancestatus.md)。
以查询杭州地域下实例ID为i-bp1******实例为例，输入以下命令查询实例运行状态。aliyun ecs DescribeInstanceStatus --region cn-hangzhou --RegionId 'cn-hangzhou' --InstanceId.1 'i-bp1******'
如果查询出对应实例的Status为Running则实例为运行中。
{ "TotalCount": 1, "RequestId": "A413****-****-****-****-****611B", "PageSize": 1, "PageNumber": 1, "InstanceStatuses": { "InstanceStatus": [ { "Status": "Running", "InstanceId": "i-bp1******" } ] } }
除此API外，您还可以通过其他API查询实例运行状态，请参见[查询实例的详细信息列表](../developer-reference/api-ecs-2014-05-26-describeinstances.md)。
