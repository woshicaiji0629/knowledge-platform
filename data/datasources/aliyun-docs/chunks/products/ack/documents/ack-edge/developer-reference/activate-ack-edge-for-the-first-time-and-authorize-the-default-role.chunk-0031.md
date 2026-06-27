### [AliyunCSManagedCsiProvisionerRole](../../../../ram/documents/developer-reference/aliyuncsmanagedcsiprovisionerrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的存储组件（csi-provisioner托管组件）使用该角色访问您在ECS、NAS、OSS、服务中的资源。
授权代码：
{ name = "AliyunCSManagedCsiProvisionerRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "ACK托管集群、ACK Edge集群和ACK Serverless集群的存储组件（新版csi-provisioner组件）使用该角色访问您在ECS、NAS、OSS服务中的资源。" policy_name = "AliyunCSManagedCsiProvisionerRolePolicy" }
