## 阿里云CLI
如果您已经配置好了阿里云CLI，您可以通过以下命令获取实例ID。具体参数说明，请参见[查询实例的详细信息列表](../developer-reference/api-ecs-2014-05-26-describeinstances.md)。
以查询杭州地域下名称为SessionManager-example的实例为例。aliyun ecs DescribeInstances --region cn-hangzhou --RegionId 'cn-hangzhou' --InstanceName 'SessionManager-example'
返回结果中InstanceId即实例ID。
