## 集群维度KubeConfig管理示例
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择授权管理。
单击KubeConfig 管理页签，单击目标集群右侧的KubeConfig 管理，查看拥有该集群KubeConfig或KubeConfig过去被清除但仍残留RBAC授权的用户列表。
如果您的账号下存在RAM用户或角色已删除，但其KubeConfig仍在生效中的情况，控制台会有对应提示。
用户信息：用户名、用户ID、账号类型以及账号状态。
KubeConfig证书信息：KubeConfig过期时间、KubeConfig状态等。
确认待清除用户的KubeConfig没有被任何业务应用依赖使用后，单击目标用户右侧操作列下的清除 KubeConfig，清除目标用户在该集群下的KubeConfig。
重要
请务必确认不存在风险后，再执行KubeConfig清除操作，否则，您将无法使用该用户的KubeConfig访问集群API Server。
KubeConfig的运维和管理是用户的职责，请您务必及时清除有安全风险的KubeConfig。
单击清除 KubeConfig时，将会对待删除的KubeConfig进行七天内在指定集群API Server审计日志的访问记录检查，此辅助检查使用前提为对应集群[已开启集群的](../security-and-compliance/work-with-cluster-auditing.md)[API Server](../security-and-compliance/work-with-cluster-auditing.md)[审计功能](../security-and-compliance/work-with-cluster-auditing.md)。
