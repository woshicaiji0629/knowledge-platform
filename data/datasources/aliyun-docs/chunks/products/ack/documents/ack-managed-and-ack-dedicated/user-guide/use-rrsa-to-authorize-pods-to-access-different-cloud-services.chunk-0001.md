## 背景信息
ECS实例元数据包含了在阿里云系统中关于ECS实例（ECI实例基于ECS实例实现）的详细信息。您可以在运行中的实例内部访问这些元数据，从而配置或管理实例。通过实例元数据，Kubernetes集群内应用可以获取实例RAM角色策略生成的STS临时凭证，并通过这些临时凭证访问云资源OpenAPI。更多信息，请参见[实例元数据](../../../../ecs/documents/user-guide/view-instance-metadata.md)。
出于安全考虑，当您需要限制集群内不同应用的RAM权限时，应禁止这些应用通过ECS或ECI实例元数据获取您的实例关联角色对应的临时凭证，或者不为实例关联角色分配任何RAM权限策略。然而，这些应用仍然需要一种安全的途径去获取访问云资源的临时凭证。因此，阿里云容器服务ACK联合RAM访问控制服务推出了RRSA功能。
基于RRSA功能，您可以在集群内实现Pod级别隔离的应用关联RAM角色功能。各个应用可以扮演独立的RAM角色并使用获取的临时凭证访问云资源，从而实现应用RAM权限最小化以及无AccessKey访问阿里云OpenAPI避免AccessKey泄露的需求。
从用户侧视角来看，RRSA功能的工作流程如下。
用户提交使用了服务账户令牌卷投影功能的应用Pod。
集群将为该应用Pod创建和挂载相应的服务账户OIDC Token文件。
Pod内程序使用挂载的OIDC Token文件访问STS服务的AssumeRoleWithOIDC接口，获取扮演指定RAM角色的临时凭证。
说明
请提前修改RAM角色配置，允许Pod使用的服务账户扮演该RAM角色。更多信息，请参见[AssumeRoleWithOIDC](../../../../ram/documents/api-assumerolewithoidc.md)。
从文件中读取的OIDC Token是一个临时Token，建议应用程序每次在使用时都从文件中读取最新的Token，集群会在Token过期前更新替换文件内已有的Token。
Pod内程序使用获取到的临时凭证访问云资源OpenAPI。
