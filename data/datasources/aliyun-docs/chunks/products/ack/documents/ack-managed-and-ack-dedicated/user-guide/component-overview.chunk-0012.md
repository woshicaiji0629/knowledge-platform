### 弹性与调度

| 组件名称 | 组件类型 | 描述 |
| --- | --- | --- |
| [ACK GOATScaler](instant-elasticity.md) | 可选组件 | 提供节点即时弹性功能。 |
| [ack-kubernetes-cronhpa-controller](../../product-overview/ack-kubernetes-cronhpa-controller.md) | 可选组件 | 使用 ack-kubernetes-cronhpa-controller 实现应用负载定时伸缩。 |
| [ack-vertical-pod-autoscaler](../../product-overview/ack-vertical-pod-autoscaler.md) | 可选组件 | ack-vertical-pod-autoscaler 组件能够监控 Pod 的资源消耗模式，灵活推荐 CPU 和内存资源分配的配置，并在适当的情况下自动进行调整，而不调整 Pod 的副本数量。这种能力更适用于需要稳定资源配置的有状态应用的扩容等场景。 |
| [AHPA Controller](../../product-overview/application-intelligence-controller.md) | 可选组件 | AHPA 基于应用历史指标预测未来 Pod 实例数量，帮助您解决弹性滞后的问题。AHPA 通过主动预测和被动预测相结合，实时调整资源实例数，并且增加了兜底保护策略，通过设置时间区间的实例数上下界值，实现弹性兜底。 |
| [ack-koordinator（ack-slo-manager）](../../product-overview/ack-koordinator-fka-ack-slo-manager.md) | 可选组件 | ACK 支持差异化 SLO（Service Level Objectives）能力的核心应用，可以在保证应用服务质量的同时，充分提升资源使用效率。 |
