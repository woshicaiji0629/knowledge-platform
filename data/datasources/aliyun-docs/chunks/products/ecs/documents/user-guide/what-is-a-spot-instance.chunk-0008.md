## 进阶使用
考虑到实际资源使用场景，在提升资源自动运维层面，建议您搭配阿里云的弹性伸缩、弹性供应组或者容器服务ACK使用抢占式实例。
弹性伸缩：根据业务需求和策略自动调整计算能力（即实例数量）。请参见[在伸缩组使用抢占式实例降低成本](https://help.aliyun.com/zh/auto-scaling/use-cases/cost-reduction-by-using-preemptible-instances)。
弹性供应组：弹性供应组是一种快速交付ECS实例集群的方案，简单配置后即可自动在多个可用区内交付不同计费方式（按量付费和抢占式实例）、多种实例规格的实例集合，提升批量交付大量实例的效率。请参见[弹性供应组配置示例](configure-an-auto-provisioning-group.md)。
容器服务 ACK：提供高性能可伸缩的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理。请参见以下文档：
[使用抢占式](../../../ack/documents/serverless-kubernetes/use-cases/run-jobs-on-a-preemptible-instance-1.md)[ECI](../../../ack/documents/serverless-kubernetes/use-cases/run-jobs-on-a-preemptible-instance-1.md)[实例运行](../../../ack/documents/serverless-kubernetes/use-cases/run-jobs-on-a-preemptible-instance-1.md)[Job](../../../ack/documents/serverless-kubernetes/use-cases/run-jobs-on-a-preemptible-instance-1.md)[任务](../../../ack/documents/serverless-kubernetes/use-cases/run-jobs-on-a-preemptible-instance-1.md)
[抢占式实例节点池最佳实践](https://help.aliyun.com/zh/document_detail/410889.html)
[基于抢占式实例的弹性训练](../../../ack/documents/cloud-native-ai-suite/user-guide/elastic-training-based-on-preemptive-instances.md)
[抢占式实例节点池最佳实践](../../../ack/documents/ack-managed-and-ack-dedicated/
