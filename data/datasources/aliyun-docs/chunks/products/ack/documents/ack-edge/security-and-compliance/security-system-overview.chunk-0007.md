of-a-cluster.md)。ACK负责维护访问凭证中签发的身份信息，对于可能泄露的已下发Kubeconfig，可以及时进行吊销操作，具体操作，请参见[吊销集群的](../../ack-managed-and-ack-dedicated/user-guide/revoke-a-kubeconfig-credential.md)[KubeConfig](../../ack-managed-and-ack-dedicated/user-guide/revoke-a-kubeconfig-credential.md)[凭证](../../ack-managed-and-ack-dedicated/user-guide/revoke-a-kubeconfig-credential.md)。
在集群创建时，ACK支持服务账户令牌卷投影（Service Account Token Volume Projection）特性以增强在应用中使用ServiceAccount的安全性。具体操作，请参见[部署服务账户令牌卷投影](../../ack-managed-and-ack-dedicated/security-and-compliance/enable-service-account-token-volume-projection.md)。
细粒度访问控制
基于Kubernetes RBAC实现了对ACK集群内Kubernetes资源的访问控制，它是保护应用安全的一个基本且必要的加固措施。ACK在控制台的授权管理页面中提供了命名空间维度的细粒度RBAC授权能力，主要包括以下几点。
根据企业内部不同人员对权限需求的不同，系统预置了管理员、运维人员、开发人员等对应的RBAC权限模板，降低了RBAC授权的使用难度。
支持多集群和多个子账号的批量授权。
支持RAM角色扮演用户的授权。
支持绑定用户在集群中自定义的ClusterRole。
更多信息，请参见[配置](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[RAM](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[用户或](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[RAM](../../ack-managed-and-ack-dedicated/user-guide/gr
