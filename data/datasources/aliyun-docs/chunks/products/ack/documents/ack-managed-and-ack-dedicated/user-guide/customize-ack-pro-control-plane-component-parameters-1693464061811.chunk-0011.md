。 |  |
| oidcGroupsClaim | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcRequiredClaim | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcCAContent | 默认为空。 支持 1.18 及以上集群。 |  |
| Kube Controller Manager | horizontalPodAutoscalerSyncPeriod | 默认为空。 |
| horizontalPodAutoscalerTolerance | 默认为空。 |  |
| concurrentTTLAfterFinishedSyncs | 默认为空。 |  |
| largeClusterSizeThreshold | 默认为空。 |  |
| unhealthyZoneThreshold | 默认为空。 |  |
| secondaryNodeEvictionRate | 默认为空。 |  |
| nodeEvictionRate | 默认为空。 |  |
| podEvictionTimeout | 默认为空。 |  |
| kubeAPIQPS | 可选范围 1~1000，默认为空。 |  |
| kubeAPIBurst | 可选范围 1~1000，默认为空。 |  |
| featureGates | 可选参数为 TTLAfterFinished ，默认为空。 |  |
| Cloud Controller Manager | routeTableIDs | 默认为空。如果 VPC 内有多个路由表，可以手动设置 CCM 支持多个路由表 ID，以半角逗号（,）分隔，例如 vtb-**,vtb*** 。 |
| Kube Scheduler | 关于通过 Kube Scheduler 自定义参数，请参见 [自定义调度器参数](customize-the-scheduler-parameters.md) 。 |  |
