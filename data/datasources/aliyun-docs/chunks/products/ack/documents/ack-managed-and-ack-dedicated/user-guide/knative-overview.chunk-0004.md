tive服务中实现日志与监控告警、持续交付、事件驱动等能力。
更丰富的功能特性：在社区Knative的基础上，ACK Knative结合实际业务场景提供了开箱即用的、更为丰富的产品方案。例如以下方案。
[保留实例](reserved-instances.md)：为延迟敏感应用保留一个低成本常驻实例，缓解社区Knative“缩容至0”策略带来的冷启动延迟，以提升服务响应速度，有效控制资源成本。
[Knative](knative-auto-scaling.md)[自动伸缩](knative-auto-scaling.md)： 提供开箱即用的基于请求的自动弹性[KPA](enable-automatic-scaling-for-pods-based-on-the-number-of-requests.md)（Knative Pod Autoscaler），同时也支持[HPA](use-hpa-in-knative.md)，您还可以为Knative服务配置AHPA（Advanced Horizontal Pod Autoscaler）弹性能力。如果您的应用所需资源具备周期性变化，推荐您使用AHPA进行弹性预测，提前预热所需的资源，缓解使用Knative时遇到的冷启动问题。
关于ACK Knative和社区Knative对比的更多信息，请参见[阿里云](comparison-between-alibaba-cloud-knative-and-open-source-knative.md)[Knative](comparison-between-alibaba-cloud-knative-and-open-source-knative.md)[和开源](comparison-between-alibaba-cloud-knative-and-open-source-knative.md)[Knative](comparison-between-alibaba-cloud-knative-and-open-source-knative.md)[对比](comparison-between-alibaba-cloud-knative-and-open-source-knative.md)。
