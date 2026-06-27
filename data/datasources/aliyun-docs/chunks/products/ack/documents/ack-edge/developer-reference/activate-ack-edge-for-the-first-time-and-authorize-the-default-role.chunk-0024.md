### [AliyunCSManagedNlcRole](../../../../ram/documents/developer-reference/aliyuncsmanagednlcrolepolicy.md)
说明：
ACK托管集群和ACK Edge集群的节点生命周期控制器使用该角色访问您的ECS和ACK节点池资源。
授权代码：
{ name = "AliyunCSManagedNlcRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群托管节点池控制组件使用该角色访问您的ECS和ACK节点池资源。" policy_name = "AliyunCSManagedNlcRolePolicy" }
