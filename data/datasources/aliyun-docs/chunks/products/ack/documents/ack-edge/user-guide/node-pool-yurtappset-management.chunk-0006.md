rator: In values: - np47832359db2e4843aa13e8b76f83**** replicas: 2 tolerations: - effect: NoSchedule key: apps.openyurt.io/taints operator: Exists
相关字段的解释如下表所示：

| 字段 | 含义 |
| --- | --- |
| spec.workloadTemplate | 代表支持的 Workload 模板，目前节点池支持 deploymentTemplate/statefulSetTemplate 两种模板。 |
| spec.topology.subsets | 指定多个节点池。 |
| spec.topology.subsets[*].name | 节点池的名称。 |
| spec.topology.pools[*].nodeSelectorTerm | 节点池的主机亲和性配置若需与节点池 NodePool 相对应，Key 使用 apps.openyurt.io/nodepool ，Values 使用节点池 ID。 说明 您可以在 节点池 页面，在对应云端和边缘侧的节点池 名称 的下方查看节点池 ID。 |
| spec.topology.pools[*].tolerations | 节点池的主机容忍性配置。 |
| spec.topology.pools[*].replicas | 每个节点池下 Pod 的实例数。 |
