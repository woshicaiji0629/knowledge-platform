| 方案 | 介绍 | 扩缩依据的指标 | 使用场景 | 相关文档 |
| --- | --- | --- | --- | --- |
| HPA | 在业务负载上升时快速扩容 Pod 副本来缓解压力，在业务负载变小时适当缩容以节省资源，是最常用的应用弹性方案。 | 资源指标（CPU、内存使用率） 其他 [自定义指标](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#scaling-on-custom-metrics) | 服务波动较大、服务数量多且需要频繁扩缩容的在线业务场景，例如电商服务、在线教育、金融服务等。 | [使用容器水平伸缩（HPA）](horizontal-pod-autoscaling.md) |
| CronHPA | 类似 Crontab 的策略，定时对 Pod 进行扩缩容，可配置时区、执行的日期、跳过执行的日期（例如节假日），支持和 HPA 协同使用。 | 定时扩缩容 | 业务流量有明显高峰时段、应用程序需要在特定时间执行任务等场景。 | [使用容器定时水平伸缩（CronHPA）](cronhpa.md) [实现](make-cronhpa-compatible-with-hpa.md) [CronHPA](make-cronhpa-compatible-with-hpa.md) [与](make-cronhpa-compatible-with-hpa.md) [HPA](make-cronhpa-compatible-with-hpa.md) [的协同](make-cronhpa-compatible-with-hpa.md) |
| VPA | 监控 Pod 的资源消耗模式，灵活推荐 CPU 和内存资源分配的配置，并在适当的情况下自动进行调整，而不调整 Pod 的副本数量。 | 推荐并自动调整 Pod 中容器的 CPU 及内存的 Request 和 Limit | 需要稳定资源配置的有状态应用的扩容、大型单体应用等场景，通常是在 Pod 出现异常恢复时生效。 | [使用容器垂直伸缩（VPA）](vertical-pod-autoscaling.md) |
| KEDA | 支持丰富的事件源，为工作负载提供事件驱动的自动伸缩能力。 | 事件数量，例如队列长度 | 需要即时弹性的场景，尤其是基于事件源的离线作业场景，例如音视频离线转码、事件驱动作业、流式数据处理等。 | [事件驱动弹性](ack-keda.md) |
| AHPA | 根据业务历史指标，自动、主动识别弹性周期并对容量进行预测，提前进行弹性规划，解决弹性滞后的问题。 | 资源指标（CPU、内存、GPU 使用率） 流量指标（QPS、RT） 其他自定义指标 | 业务流量有明
