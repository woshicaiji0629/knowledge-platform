### [AliyunCSManagedBackupRestoreRole](../../../../ram/documents/developer-reference/aliyuncsmanagedbackuprestorerolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的备份中心服务组件使用该角色访问您在云备份（Cloud Backup）服务和OSS服务中的资源。
授权代码：
{ name = "AliyunCSManagedBackupRestoreRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的备份中心组件使用该角色访问您在云备份（Cloud Backup）服务和OSS服务中的资源。" policy_name = "AliyunCSManagedBackupRestoreRolePolicy" }
