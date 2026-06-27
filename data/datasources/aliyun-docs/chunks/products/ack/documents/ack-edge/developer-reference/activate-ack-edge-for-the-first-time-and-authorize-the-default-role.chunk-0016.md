### [AliyunCSServerlessKubernetesRole](../../../../ram/documents/developer-reference/aliyuncsserverlesskubernetesrolepolicy.md)
说明：
ACK Edge集群和ACK Serverless集群使用该角色来访问您在ECS、VPC、SLB、Private Zone等服务中的资源。
授权代码：
{ name = "AliyunCSServerlessKubernetesRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSServerlessKubernetesRolePolicy" }
