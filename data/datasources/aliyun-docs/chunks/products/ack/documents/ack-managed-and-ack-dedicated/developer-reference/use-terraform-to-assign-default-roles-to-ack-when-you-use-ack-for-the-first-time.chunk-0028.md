管理API、ECS和ECI服务中的资源。
授权代码：
{ name = "AliyunCSManagedCostRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的成本分析组件使用该角色访问您在账单管理API、ECS和ECI服务中的资源。" policy_name = "AliyunCSManagedCostRolePolicy" }
[AliyunCSManagedNimitzRole](../../../../ram/documents/developer-reference/aliyuncsmanagednimitzrolepolicy.md)
说明：
ACK Edge集群的管控组件使用该角色访问您在智能接入网关、VPC和云企业网CEN服务中的资源。
授权代码：
{ name = "AliyunCSManagedNimitzRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "ACK灵骏集群的网络组件使用该角色访问您在智能计算灵骏服务中的资源。" policy_name = "AliyunCSManagedNimitzRolePolicy" }
[AliyunCSManagedBackupRestoreRole](../../../../ram/documents/developer-reference/aliyuncsmanagedbackuprestorerolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的备份中心服务组件使用该角色访问您在云备份（Cloud Backup）服务和OSS服务中的资源。
授权代码：
{ name = "AliyunCSManagedBackupRestoreRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Vers
