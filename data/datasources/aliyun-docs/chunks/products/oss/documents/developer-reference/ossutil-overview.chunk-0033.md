### 使用ECSRAMRole
如果应用程序运行在ECS实例、ECI实例、容器服务Kubernetes版的Worker节点中，建议使用ECSRAMRole初始化凭证提供者。该方式底层实现是STS Token。ECSRAMRole允许将一个角色关联到ECS实例、ECI实例或容器服务 Kubernetes 版的Worker节点，实现在实例内部自动刷新STS Token。该方式无需提供一个AK或STS Token，消除了手动维护AK或STS Token的风险。如何获取ECSRAMRole，请参见[创建角色](../../../ram/documents/developer-reference/api-ram-2015-05-01-createrole.md)。
说明
不支持通过环境变量方式设置。
EcsRamRole模式
