### 可选角色
[AliyunCSManagedAcrRole](../../../../ram/documents/developer-reference/aliyuncsmanagedacrrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的免密组件镜像拉取使用该角色访问您在ACR容器镜像服务中的资源。
授权代码：
{ name = "AliyunCSManagedAcrRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的镜像拉取免密插件使用该角色访问您在ACR容器镜像服务中的资源。" policy_name = "AliyunCSManagedAcrRolePolicy" }
[AliyunCSManagedNlcRole](../../../../ram/documents/developer-reference/aliyuncsmanagednlcrolepolicy.md)
说明：
ACK托管集群和ACK Edge集群的节点生命周期控制器使用该角色访问您的ECS和ACK节点池资源。
授权代码：
{ name = "AliyunCSManagedNlcRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群托管节点池控制组件使用该角色访问您的ECS和ACK节点池资源。" policy_name = "AliyunCSManagedNlcRolePolicy" }
[AliyunCSManagedAutoScalerRole](../../../../ram/documents/developer-reference/aliyuncsmanagedautoscalerrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的弹性伸缩组件使用该角色访问您在ESS和ECS服务中的资源。
授权代码：
{ name = "AliyunCSManagedAutoScalerRole" policy_document = "{\"Statem
