限制部署在集群指定范围内的 Pod 必须具有 "cluster-autoscaler.kubernetes.io/safe-to-evict": "true" 注释标签。默认情况下 autoscaler 在集群自动伸缩时不会驱逐使用 HostPath 或 EmptyDir 卷的 Pod。为了允许驱逐这些 Pod，必须在 Pod 上添加该注释标签。 | low |  |
| ACKOSSStorageLocationConstraint | 限制指定 Namespaces 下的部署只能使用指定 Region 中的阿里云 OSS 存储卷 | low |  |
| ACKPVSizeConstraint | 限制集群中创建的 PV 实例中能够申请的最大磁盘容量。 | medium |  |
| ACKPVCConstraint | 限制能够部署 PVC 实例的命名空间白名单列表以及限制 PVC 实例中能够申请的最大磁盘容量。 | medium |  |
| ACKBlockVolumeTypes | 限制在集群指定范围内部署的 Pod 禁止使用的 Volume 挂载类型。 | medium |  |
| ASMSidecarInjectionEnforced | 限制 Pod 必须注入 ASM Sidecar。 | high |  |
| K8s-general | ACKAllowedRepos | 限制在集群指定范围部署的应用 Pod 中拉取白名单列表外的镜像。 | high |
| ACKBlockAutoinjectServiceEnv | 要求在应用中配置 enableServiceLinks: false 防止在 Pod 环境变量中透出服务 IP。 | low |  |
| ACKBlockAutomountToken | 要求在应用中设置 automountServiceAccountToken: false 字段以防止自动挂载 serviceaccount 。 | high |  |
| ACKBlockEphemeralContainer | 限制在集群指定范围的应用 Pod 中启动临时容器。 | medium |  |
| ACKBlockLoadBalancer | 限制在集群指定范围内部署 LoadBalancer 类型的 Service。 | high |  |
| ACKBlockNodePort | 限制在集群指定范围内使用 NodePort 类型的 Service。 | high |  |
| ACKContainerLimits | 要求集群指定范围的应用 Pod 配置资源 limits 。 | low |  |
| ACKExternalIPs | 限制在集群指定范围内的 Service 实例使用白名单范围之外的 extern
