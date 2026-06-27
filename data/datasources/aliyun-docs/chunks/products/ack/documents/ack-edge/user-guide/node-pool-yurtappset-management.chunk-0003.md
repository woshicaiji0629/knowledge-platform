| 字段 | 含义 | 是否必选 |
| --- | --- | --- |
| spec.pools | 指定需要部署应用的节点池名称列表（slice 类型，推荐优先使用 nodepoolSelector 指定 nodepool）。 | 否 |
| spec.nodepoolSelector | 通过 labelSelector 选择需要部署应用的节点池（当与 pools 同时指定时，取并集）。 nodepoolSelector 通过匹配 NodePool 资源的标签（metadata.Labels）来选择节点池。如需修改这些标签，请在集群控制台的自定义资源页面，找到并编辑相应 NodePool 的 YAML。 | 否 |
| spec.workload.workloadTemplate | 指定管理的 Workload 模板，目前支持 deploymentTemplate 和 statefulSetTemplate 模板。 | 是 |
| spec.workload.workloadTweaks | 指定对 Workload 的定制修改。 | 否 |
| spec.workload.workloadTweaks[*].pools | 指定该项修改应用在哪些节点池上（slice 类型）。 | 否 |
| spec.workload.workloadTweaks[*].nodepoolSelector | 通过 labelSelector 选择哪些节点池将会被修改。 | 否 |
| spec.workload.workloadTweaks[*].tweaks.replicas | 指定被修改的 workload 的 replicas 数。 | 否 |
| spec.workload.workloadTweaks[*].tweaks.containerImages | 指定被修改的 workload 的容器镜像。 | 否 |
| spec.workload.workloadTweaks[*].tweaks.patches | 通过 patch 字段可以修改 workloadTemplate 的任意字段。 | 否 |
| spec.workload.workloadTweaks[*].tweaks.patches[*].path | 指定需要修改的字段在 workloadTemplate 中的路径。 | 否 |
| spec.workload.workloadTweaks[*].tweaks.patches[*].operation | 指定需要在 path 上执行的操作（目前支持：add/remove/replace）。 | 否 |
| spec.workload.workloadTweaks[*].tweaks.patches[*].value | 指定修改
