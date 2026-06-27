| 组件名 | 参数 | 参数说明 |
| --- | --- | --- |
| Kube API Server | enableAdmissionPlugins | 默认为空。 |
| serviceNodePortRange | 可选范围 10000～65535，默认为空。 重要 您在修改 NodePort 端口范围时必须十分谨慎。务必保证 NodePort 端口范围与集群节点上 Linux 内核提供的 net.ipv4.ip_local_port_range 参数的端口范围不冲突。更多信息，请参见 [如何正确配置](faq-about-network-management.md) [NodePort](faq-about-network-management.md) [范围？](faq-about-network-management.md) 。 |  |
| requestTimeout | 默认为空。 |  |
| defaultNotReadyTolerationSeconds | 默认为空。 |  |
| defaultUnreachableTolerationSeconds | 默认为空。 |  |
| maxMutatingRequestsInflight | 可选范围 1~1000，默认为空。 |  |
| maxRequestsInflight | 可选范围 1~3000，默认为空。 |  |
| featureGates | 可选参数包括 ServerSideApply 、 TTLAfterFinished 、 EphemeralContainers 、 RemoveSelfLink 、 HPAScaleToZero ，默认为空。 说明 支持在 1.18 及以上集群中使用 HPAScaleToZero ，不支持在 1.24 及以上集群中修改 RemoveSelfLink 。 |  |
| oidcIssuerURL | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcClientId | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcUsernameClaim | 默认值为 sub 。支持 1.18 以上集群。 |  |
| oidcUsernamePrefix | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcGroupsPrefix | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcGroupsClaim | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcRequiredClaim | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcCAContent | 默认为空。 支持 1.18 及以上集群。 |  |
| Kube Co
