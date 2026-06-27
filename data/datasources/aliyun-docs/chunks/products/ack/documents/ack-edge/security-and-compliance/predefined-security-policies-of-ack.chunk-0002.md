| Category | Policy | Description | Severity |
| --- | --- | --- | --- |
| Compliance | ACKNoEnvVarSecrets | 限制 Secret 以 secretKeyRef 的形式挂载到应用 Pod 环境变量中。 | medium |
| ACKPodsRequireSecurityContext | 限制 Pod 中所有容器必须配置 securityContext 字段。 | low |  |
| ACKRestrictNamespaces | 限制资源部署在集群指定的命名空间中。 | low |  |
| ACKRestrictRoleBindings | 限制指定命名空间下的 rolebinding 使用指定范围内的 Role 或 Clusterrole。 | high |  |
| ACKNamespacesDeleteProtection | 限制指定的 Namespace 被误删除。 | medium |  |
| ACKServicesDeleteProtection | 防止 Namespace 中的 Service 实例被误删除。 | medium |  |
| ACKProtectBoundingPV | 防止绑定状态的持久化存储卷（PV）被删除。 | high |  |
| ACKBlockNodeDelete | 防止带有自定义标签的节点（Node）被删除。 | high |  |
| ACKResourceDeletionProtection | 防止带有自定义标签的多种资源（包括 Service、Namespace、Ingress 等）被删除。 | high |  |
| ACKProtectCoreDNS | 防止 kube-system 命名空间中 CoreDNS 相关资源被删除。 | high |  |
| Infra | ACKBlockProcessNamespaceSharing | 限制在集群指定范围部署的应用中使用 shareProcessNamespace 。 | high |
| ACKEmptyDirHasSizeLimit | 要求 emptyDir 类型的 Volume 必须指定 sizelimit 。 | low |  |
| ACKLocalStorageRequireSafeToEvict | 限制部署在集群指定范围内的 Pod 必须具有 "cluster-autoscaler.kubernetes.io/safe-to-evict": "true" 注释标签。默认情况下 autoscaler 在集群自动伸缩时不会驱逐使用 HostPath 或 EmptyDir 卷的 Pod。为了允许驱逐这些 Pod，必须
