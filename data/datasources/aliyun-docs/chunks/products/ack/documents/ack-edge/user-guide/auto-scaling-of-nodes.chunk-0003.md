pressions: - key: "k8s.aliyun.com" operator: "NotIn" values: ["true"]
cluster-autoscaler 组件更新或部署时需要占用一定的节点资源；若资源不足，可能导致更新或部署失败，引发扩缩容异常。请确保节点资源充足。
本功能涉及以下流程：
[步骤一：为集群开启节点自动伸缩功能](auto-scaling-of-nodes.md)：先基于集群维度开启节点自动伸缩功能后，节点池设置的自动扩缩容策略才会生效。
[步骤二：配置开启弹性的节点池](auto-scaling-of-nodes.md)：节点自动伸缩功能仅对设置了自动扩缩容的节点池生效，因此，还需要将指定节点池的扩缩容模式配置为自动模式。
