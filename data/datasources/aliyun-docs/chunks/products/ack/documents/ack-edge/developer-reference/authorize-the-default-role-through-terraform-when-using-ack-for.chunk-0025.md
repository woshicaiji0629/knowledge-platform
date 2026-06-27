":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群Arms插件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedArmsRolePolicy" }
- [AliyunCISDefaultRole](../../../../ram/documents/developer-reference/aliyuncisdefaultrolepolicy.md)
说明：
ACK容器智能运维平台将使用该角色访问您在ECS、VPC、SLB等服务中的资源，为您提供诊断和巡检等服务。
授权代码：
{ name = "AliyunCISDefaultRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "容器服务（CS）智能运维使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCISDefaultRolePolicy" }
