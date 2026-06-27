### 控制台
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择授权管理。
在授权管理页面，如果您的账号中存在已删除的失效用户的KubeConfig残留，该页面会显示提示信息。
单击红色提示框中的处理与失效账号关联的 KubeConfig，进入清除已删除 RAM 用户/角色的 KubeConfig页面。
该页面可查看KubeConfig 以及 RBAC 授权仍在生效的已删除的 RAM用户或RAM角色列表。
确认待清除用户的KubeConfig没有被任何业务应用依赖使用后，单击已失效用户右侧的清除 KubeConfig，清除该失效用户的KubeConfig。
重要
请务必确认不存在风险后，再执行KubeConfig清除操作，否则，您将无法使用该用户的KubeConfig访问集群API Server。
KubeConfig的运维和管理是用户的职责，请您务必及时清除有安全风险的KubeConfig。
单击清除 KubeConfig时，将会对待删除的KubeConfig进行七天内在指定集群API Server审计日志的访问记录检查，此辅助检查使用前提为对应集群[已开启集群的](../security-and-compliance/work-with-cluster-auditing.md)[API Server](../security-and-compliance/work-with-cluster-auditing.md)[审计功能](../security-and-compliance/work-with-cluster-auditing.md)。
