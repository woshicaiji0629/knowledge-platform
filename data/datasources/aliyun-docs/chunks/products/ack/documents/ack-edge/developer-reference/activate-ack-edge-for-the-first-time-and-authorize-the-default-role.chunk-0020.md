### [AliyunCSManagedKubernetesRole](../../../../ram/documents/developer-reference/aliyuncsmanagedkubernetesrolepolicy.md)
说明：
ACK托管集群和ACK Edge集群使用该角色访问您在ECS、VPC、SLB、ACR等服务中的资源。
授权代码：
{ name = "AliyunCSManagedKubernetesRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedKubernetesRolePolicy" }
