### [AliyunCSDefaultRole](../../../../ram/documents/developer-reference/aliyuncsdefaultrolepolicy.md)
说明：
容器服务 Kubernetes 版在管控操作中使用该角色访问您在ECS、VPC、SLB、ROS、ESS等服务中的资源。
授权代码：
{ name = "AliyunCSDefaultRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群操作时默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSDefaultRolePolicy" }
