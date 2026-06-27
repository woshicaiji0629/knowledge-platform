| 组件名称 | 组件类型 | 描述 |
| --- | --- | --- |
| [ack-advanced-audit](../../product-overview/ack-advanced-audit.md) | 可选组件 | ack-advanced-audit 组件基于开源项目 [Falco](https://falco.org/) ，使用内核提供的 eBPF 特性，实现了容器内操作的系统调用审计能力。通过 ack-advanced-audit 组件实现的容器内部操作审计功能，可以方便您审计组织内成员或应用程序进入容器后执行的命令操作。 |
| [ack-pod-identity-webhook](../../product-overview/ack-pod-identity-webhook.md) | 可选组件 | ack-pod-identity-webhook 组件可以帮您更便捷地使用容器服务提供的 RRSA（RAM Roles for Service Accounts）特性，它可以为您的应用 Pod 自动注入应用依赖的挂载 OIDC Token 和环境变量配置，免去繁琐的手动配置工作。 |
| [ack-ram-authenticator](../../product-overview/ack-ram-authenticator.md) | 系统组件 | ack-ram-authenticator 组件是面向 ACK 托管集群 的认证插件，基于 Kubernetes 原生 [Webhook Token](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#webhook-token-authentication) [认证](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#webhook-token-authentication) 方式，实现通过 RAM 完成集群 API Server 的请求认证。同时，该组件通过 CRD 形式提供 RAM 身份和 RBAC 权限的映射关系，帮您更灵活地配置 RBAC 鉴权。 |
| [gatekeeper](../../product-overview/gatekeeper.md) | 可选组件 | 帮助您方便地管理和应用集群内的 Open Policy Agent（OPA）策略，实现命名空间标签管理等功能。 |
| [kritis-validation-hook](../../product-overview/kritis-validation-hook.md) | 可选组件 | 部署可信容器环节中进行容器镜像签名验
