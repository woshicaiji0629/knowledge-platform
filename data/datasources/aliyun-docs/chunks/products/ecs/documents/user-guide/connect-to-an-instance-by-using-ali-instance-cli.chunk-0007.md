## 阿里云CLI
如果您已经配置好了阿里云CLI，您可以通过以下命令查询实例是否安装云助手且云助手版本是否支持使用会话管理。具体参数说明，请参见[查询云助手安装状态](../developer-reference/api-ecs-2014-05-26-describecloudassistantstatus.md)。
以查询杭州地域下实例ID为i-bp1******实例为例，输入以下命令查询实例运行状态。aliyun ecs DescribeCloudAssistantStatus --region cn-hangzhou --RegionId 'cn-hangzhou' --InstanceId.1 'i-bp1******'
如果查询出CloudAssistantStatus（云助手运行状态）为true且SupportSessionManager（是否支持会话管理）也为true，即该实例支持通过会话管理连接实例。
{ "TotalCount": 1, "PageSize": 1, "RequestId": "DB34****-****-****-****-****A749", "NextToken": "", "PageNumber": 1, "InstanceCloudAssistantStatusSet": { "InstanceCloudAssistantStatus": [ { "CloudAssistantVersion": "2.2.3.857", "SupportSessionManager": true, "InstanceId": "i-bp1******", "InvocationCount": 4, "OSType": "Linux", "CloudAssistantStatus": "true", "LastHeartbeatTime": "2024-12-10T02:38:04Z", "LastInvokedTime": "2024-12-08T16:02:45Z", "ActiveTaskCount": 0 } ] } }
