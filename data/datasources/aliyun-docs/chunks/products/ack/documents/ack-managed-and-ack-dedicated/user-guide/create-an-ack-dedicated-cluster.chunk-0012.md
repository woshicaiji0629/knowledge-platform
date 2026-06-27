e/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md) [SAN](../security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md) 。 |
| 服务账户令牌卷投影 | 传统模式下 Pod 的身份凭证永久有效且多个 Pod 共享，存在安全风险。启用后，每个 Pod 将获得专属的临时身份凭证，且支持配置自动过期和权限限制。 如需后续启用，请参见 [使用](../security-and-compliance/enable-service-account-token-volume-projection.md) [ServiceAccount Token](../security-and-compliance/enable-service-account-token-volume-projection.md) [卷投影](../security-and-compliance/enable-service-account-token-volume-projection.md) 。 |
| 节点服务端口范围 | 创建 NodePort 类型的 Service 时，可用的端口范围。 |
| 集群 CA | 启用后，可以将 CA 证书添加到集群中，加强服务端和客户端之间信息交互的安全性。 |
