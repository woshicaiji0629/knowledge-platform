upRestoreRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的备份中心组件使用该角色访问您在云备份（Cloud Backup）服务和OSS服务中的资源。" policy_name = "AliyunCSManagedBackupRestoreRolePolicy" }
[AliyunCSManagedEdgeRole](../../../../ram/documents/developer-reference/aliyuncsmanagededgerolepolicy.md)
说明：
ACK Edge集群的管控组件使用该角色访问您在智能接入网关、VPC和云企业网CEN服务中的资源。
授权代码：
{ name = "AliyunCSManagedEdgeRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "ACK Edge集群的管控组件使用该角色访问您在智能接入网关、VPC和云企业网CEN服务中的资源。" policy_name = "AliyunCSManagedEdgeRolePolicy" }
AliyunOOSLifecycleHook4CSRole
说明：
系统运维管理OOS使用该角色访问您在容器服务 Kubernetes 版、ECS、PolarDB等服务中的资源。
授权代码：
{ name = "AliyunOOSLifecycleHook4CSRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"oos.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群扩缩容节点池依赖OOS服务，OOS使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunOOSLifecycleHook4CSRolePolicy" }
