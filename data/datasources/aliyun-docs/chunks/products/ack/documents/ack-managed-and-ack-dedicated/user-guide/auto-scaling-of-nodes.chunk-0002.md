## 注意事项
使用前，请确保[已开通弹性伸缩](https://essnew.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre6.3be916d0JBbHR4#/v3/welcome/)[ESS](https://essnew.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre6.3be916d0JBbHR4#/v3/welcome/)[服务](https://essnew.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre6.3be916d0JBbHR4#/v3/welcome/)。
参见[注意事项](overview-of-node-scaling.md)了解使用节点伸缩的配额、限制等。
节点自动伸缩对某些调度策略的支持存在一定[已知限制](faq-about-node-auto-scaling.md)，可能导致扩缩容结果不符合预期。如果您的工作负载或组件使用了不支持的调度策略，建议采用以下方案进行调整：
方案一：切换使用[节点即时弹性](instant-elasticity.md)。
方案二：将相关工作负载或组件部署在未开启节点伸缩的节点池中。
以[ack-node-local-dns-admission-controller](../../product-overview/ack-nodelocal-dnscache.md)为例，请将该组件部署在未开启节点伸缩的节点池，并在组件配置中声明如下节点亲和性要求。
nodeAffinity: requiredDuringSchedulingIgnoredDuringExecution: nodeSelectorTerms: - matchExpressions: - key: "k8s.aliyun.com" operator: "NotIn" values: ["true"]
cluster-autoscaler 组件更新或部署时需要占用一定的节点资源；若资源不足，可能导致更新或部署失败，引发扩缩容异常。请确保节点资源充足。
本功能涉及以下流程：
[步骤一：为集群开启节点自动伸缩功能](auto-scaling-of-nodes.md)：先基于集群维度开启节点自动伸缩功能后，节点池设置的自动扩缩容策略才会生效。
[步骤二：配置开启弹性的节点池](auto-scaling-of-nodes.md)：节点自动伸缩功能仅对设置了自动扩缩
