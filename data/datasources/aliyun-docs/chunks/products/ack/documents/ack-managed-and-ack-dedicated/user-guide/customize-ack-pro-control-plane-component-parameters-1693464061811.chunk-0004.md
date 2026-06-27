API Server 仍无法访问 oidcIssuerURL 配置项中的地址，您可以通过 kubectl get endpoints 来检查 Kubernetes 后端的 IP 数量。 如果 IP 大于 1 个，请登录 Worker 节点尝试访问 oidcIssuerURL，并检查公网配置、安全组规则等。 如果只有 1 个 IP，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 处理。 |  |
| oidcClientId | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcUsernameClaim | 默认值为 sub 。支持 1.18 以上集群。 |  |
| oidcUsernamePrefix | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcGroupsPrefix | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcGroupsClaim | 默认为空。支持 1.18 及以上集群。 |  |
| oidcRequiredClaim | 默认为空。支持 1.18 及以上集群。 |  |
| oidcCAContent | 默认为空。支持 1.18 及以上集群。 |  |
| hostAliases | 默认为空。支持 1.26 及以上集群。 |  |
| enableTrace | 默认为空。支持 1.28 及以上集群。 相关操作文档，请参见 [为集群控制面组件启用链路追踪](enable-tracing-for-control-plane-components.md) 。 |  |
| samplingRatePerMillion |  |  |
| Kube Controller Manager | horizontalPodAutoscalerSyncPeriod | 默认为空。 |
| horizontalPodAutoscalerTolerance | 默认为空。 |  |
| concurrentTTLAfterFinishedSyncs | 默认为空。 |  |
| concurrentHorizontalPodAutoscalerSyncs | 默认为空。支持 1.26 及以上集群。 |  |
| largeClusterSizeThreshold | 默认为空。 |  |
| unhealthyZoneThreshold | 默认为空。 |  |
| secondaryNodeEvictionRate | 默认为空。 |  |
| nodeEvictionRate | 默认为空。 |  |
| terminatedPodGCThreshold | 默认为空。 |  |
| kubeAPIQPS
