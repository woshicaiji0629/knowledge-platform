内使用 NodePort 类型的 Service。 | high |  |
| ACKContainerLimits | 要求集群指定范围的应用 Pod 配置资源 limits 。 | low |  |
| ACKExternalIPs | 限制在集群指定范围内的 Service 实例使用白名单范围之外的 externalIPs。 | high |  |
| ACKImageDigests | 限制在集群指定范围内部署不符合 digest 格式的镜像。 | low |  |
| ACKRequiredLabels | 限制在集群指定范围内部署没有指定范式 label 标签的应用。 | low |  |
| ACKRequiredProbes | 限制在集群指定范围内部署的 Pod 配置指定类型的 readinessProbe 和 livenessProbe。 | medium |  |
| ACKCheckNginxPath | 限制在 Ingress 实例的 spec.rules[].http.paths[].path 字段中使用危险配置。Ingress-nginx 1.2.1 以下版本建议开启该策略。 | high |  |
| ACKCheckNginxAnnotation | 限制在 Ingress 实例的 metadata.annotations 字段中使用危险配置。Ingress-nginx 1.2.1 以下版本建议开启该策略。 | high |  |
| ACKBlockInternetLoadBalancer | 限制创建公网类型的 LoadBalancer Service。 | high |  |
| RatifyVerification | 您在集群中安装应用市场组件 Ratify 后，可以验证在集群指定范围内部署的 Pod 镜像中的签名或 SBOM 等安全元数据。 | high |  |
| PSP | ACKPSPAllowPrivilegeEscalationContainer | 限制在集群指定范围内部署的 Pod 配置 allowPrivilegeEscalation 参数。 | medium |
| ACKPSPAllowedUsers | 限制在集群指定范围内部署的 Pod 中的启动 user 、 group 、 supplementalGroups 以及 fsGroup 。 | medium |  |
| ACKPSPAppArmor | 限制在集群指定范围内部署的 Pod 配置 AppArmor。 | low |  |
| ACKPSPCapabilities | 限制在集群指定范围内部署的 Pod 配置 Linux Capabilities 能力。 | high |  |
| ACKPSPFSGroup | 限制在集群
