## 相关术语
首次使用节点池前，建议了解节点池相关的概念术语。
伸缩组：当对节点池进行扩容和缩容时，ACK通过[弹性伸缩](https://help.aliyun.com/zh/auto-scaling/product-overview/what-is-auto-scaling)[ESS](https://help.aliyun.com/zh/auto-scaling/product-overview/what-is-auto-scaling)服务下发扩容和移除节点的操作。节点池与弹性[伸缩组](https://help.aliyun.com/zh/auto-scaling/user-guide/scaling-group-overview#concept-25880-zh)实例为一一对应的关系。一个伸缩组是一个或多个ECS实例（Worker节点）的合集。
伸缩配置：节点池底层使用伸缩配置管理节点配置。ESS伸缩配置是弹性伸缩时ECS实例使用的模板。当弹性伸缩触发弹性扩张活动后，弹性伸缩以该伸缩配置为模板自动创建ECS实例。
伸缩活动：节点池的每次扩缩容、添加节点、移除节点都会触发伸缩活动。触发伸缩活动后，所有扩容和缩容动作都交由系统自动完成，并留下相关记录。可通过节点池的伸缩活动查看节点池的历史伸缩活动记录。
替换系统盘：节点池的某些操作，例如自动添加已有节点、更换容器运行时等，会通过替换节点系统盘（替盘升级）的方式初始化节点。该节点的实例属性不发生改变，例如节点名称、实例ID、IP等，但节点系统盘上的数据将被删除。额外挂载到该节点上的数据盘不受影响。
ACK执行替盘时会进行节点排水操作，遵循[Pod Disruption Budget（PDB）](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#pod-disruption-budgets)的前提下将节点上的Pod驱逐至其他可用节点。为确保服务高可用性，建议采用多副本部署策略，将工作负载分散在多个节点上，同时为关键业务配置PDB，控制同时中断的Pod数量。
原地升级：与替盘升级对应的一种升级方式，直接在原节点上更新替换所需的组件。原地升级不会替换系统盘，也不会重新初始化节点，原节点的数据不受影响。
