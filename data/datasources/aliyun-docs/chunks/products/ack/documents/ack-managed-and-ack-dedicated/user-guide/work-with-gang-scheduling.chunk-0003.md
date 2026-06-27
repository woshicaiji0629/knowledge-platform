## 使用方式
使用Gang scheduling时，在创建的Pod处通过设置labels的形式配置min-available和name。使用这种方式时，调度器会自动创建对应的PodGroup，并将pod-group.scheduling.sigs.k8s.io/name的值作为PodGroup的Name，因此pod-group.scheduling.sigs.k8s.io/name的值必须满足DNS子域名的命名规则。详细要求，请参见[对象名称和](https://kubernetes.io/zh-cn/docs/concepts/overview/working-with-objects/names/#dns-label-names)[ID](https://kubernetes.io/zh-cn/docs/concepts/overview/working-with-objects/names/#dns-label-names)。
labels: pod-group.scheduling.sigs.k8s.io/name: tf-smoke-gpu pod-group.scheduling.sigs.k8s.io/min-available: "3"
name：PodGroup的名称。
min-available：该批Pod满足min-available的数量时，才能被统一创建及调度。
您可以使用以下两种方式使用Gang scheduling策略。对于1.22及以上版本的集群，调度器版本需要高于1.xx.xx-aliyun-4.0。
创建对应的PodGroup自定义资源，通过pod-group.scheduling.sigs.k8s.io或者pod-group.scheduling.sigs.k8s.io/name声明Pod对应的PodGroup，此时Pod与PodGroup处于同一命名空间下。
重要
自1.31版本起，ACK将不再支持scheduling.sigs.k8s.io/v1alpha1版本的PodGroup资源，仅支持scheduling.x-k8s.io/v1alpha1版本的PodGroup资源。
