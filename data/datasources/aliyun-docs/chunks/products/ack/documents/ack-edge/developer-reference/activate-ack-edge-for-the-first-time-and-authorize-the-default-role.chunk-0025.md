### [AliyunCSManagedAutoScalerRole](../../../../ram/documents/developer-reference/aliyuncsmanagedautoscalerrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的弹性伸缩组件使用该角色访问您在ESS和ECS服务中的资源。
授权代码：
{ name = "AliyunCSManagedAutoScalerRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的弹性伸缩组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedAutoScalerRolePolicy" }
