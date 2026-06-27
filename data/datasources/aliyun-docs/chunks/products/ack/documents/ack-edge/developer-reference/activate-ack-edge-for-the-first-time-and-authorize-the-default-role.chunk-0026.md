### [AliyunCSManagedSecurityRole](../../../../ram/documents/developer-reference/aliyuncsmanagedsecurityrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的落盘加密和凭据管理组件使用该角色访问您在KMS服务中的资源。
授权代码：
{ name = "AliyunCSManagedSecurityRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的落盘加密插件使用该角色访问您在KMS服务中的资源。" policy_name = "AliyunCSManagedSecurityRolePolicy" }
