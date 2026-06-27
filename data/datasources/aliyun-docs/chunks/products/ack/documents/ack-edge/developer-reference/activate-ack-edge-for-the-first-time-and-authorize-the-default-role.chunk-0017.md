### [AliyunCSKubernetesAuditRole](../../../../ram/documents/developer-reference/aliyuncskubernetesauditrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的审计功能组件使用该角色来访问您在SLS服务中的资源。
授权代码：
{ name = "AliyunCSKubernetesAuditRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群审计功能使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSKubernetesAuditRolePolicy" }
