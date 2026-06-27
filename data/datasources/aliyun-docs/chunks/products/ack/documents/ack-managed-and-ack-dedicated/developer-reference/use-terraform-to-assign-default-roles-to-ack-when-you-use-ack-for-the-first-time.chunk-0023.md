uncskubernetesauditrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的审计功能组件使用该角色来访问您在SLS服务中的资源。
授权代码：
{ name = "AliyunCSKubernetesAuditRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群审计功能使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSKubernetesAuditRolePolicy" }
[AliyunCSManagedNetworkRole](../../../../ram/documents/developer-reference/aliyuncsmanagednetworkrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的网络组件使用该角色访问您在ECS、VPC服务中的资源。
授权代码：
{ name = "AliyunCSManagedNetworkRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群网络组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedNetworkRolePolicy" }
[AliyunCSDefaultRole](../../../../ram/documents/developer-reference/aliyuncsdefaultrolepolicy.md)
说明：
容器服务 Kubernetes 版在管控操作中使用该角色访问您在ECS、VPC、SLB、ROS、ESS等服务中的资源。
授权代码：
{ name = "AliyunCSDefaultRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliy
