### [AliyunCSManagedNimitzRole](../../../../ram/documents/developer-reference/aliyuncsmanagednimitzrolepolicy.md)
说明：
ACK Edge集群的管控组件使用该角色访问您在智能接入网关、VPC和云企业网CEN服务中的资源。
授权代码：
{ name = "AliyunCSManagedNimitzRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "ACK灵骏集群的网络组件使用该角色访问您在智能计算灵骏服务中的资源。" policy_name = "AliyunCSManagedNimitzRolePolicy" }
