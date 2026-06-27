## RAM用户或RAM角色维度KubeConfig管理示例
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择授权管理。
在授权管理页面，单击RAM 用户页签，然后单击目标用户右侧的管理 KubeConfig进入该用户的管理 KubeConfig页面。
可查看该用户各个集群KubeConfig的下发状态列表。
集群信息：集群名称和ID。
KubeConfig证书信息：KubeConfig过期时间和状态、七天日志检查（即证书访问记录）。
单个或批量清除该用户对应集群的KubeConfig。清除前，请确认待清除用户的KubeConfig没有被任何业务应用依赖使用。
单个清除：单击目标集群右侧操作列下的清除 KubeConfig，清除当前用户在该集群下的KubeConfig。
批量清除：在集群名称列选择多个待清除的集群，然后在页面左下角单击清除 KubeConfig。
重要
请务必确认不存在风险后，再执行KubeConfig清除操作，否则，您将无法使用该用户的KubeConfig访问集群API Server。
KubeConfig的运维和管理是用户的职责，请您务必及时清除有安全风险的KubeConfig。
单击清除 KubeConfig时，将会对待删除的KubeConfig进行七天内在指定集群API Server审计日志的访问记录检查，此辅助检查使用前提为对应集群[已开启集群的](../security-and-compliance/work-with-cluster-auditing.md)[API Server](../security-and-compliance/work-with-cluster-auditing.md)[审计功能](../security-and-compliance/work-with-cluster-auditing.md)。
