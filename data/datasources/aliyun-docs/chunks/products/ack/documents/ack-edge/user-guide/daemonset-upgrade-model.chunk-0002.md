## 配置说明
apiVersion: apps/v1 kind: DaemonSet metadata: annotations: apps.openyurt.io/update-strategy: AdvancedRollingUpdate apps.openyurt.io/max-unavailable: 30% spec: updateStrategy: type: OnDelete

| 参数 | 说明 |
| --- | --- |
| apps.openyurt.io/update-strategy | 启用扩展升级模型，支持 AdvancedRollingUpdate 或 OTA。 |
| apps.openyurt.io/max-unavailable | 此配置仅在 AdvancedRollingUpdate 模式下生效。定义高级滚动升级过程中最大不可用 Pod 的数量，此注解的值与原生 DaemonSet 的 maxUnavailable 配置相同。如果未指定，则默认值为 10% 。 |
| spec.updateStrategy.type | 必须设置为 OnDelete ，即需要手动删除旧的 Pod 以触发新版本的 Pod 的创建。 |
