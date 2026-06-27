### spec.machineGroups
指定哪些机器组可以应用此采集配置。
默认行为：安装LoongCollector时，系统会自动创建的名为k8s-group-${clusterId}的机器组。若未显式设置machineGroups，将默认关联该机器组。
同步机制：loongcollector-operator会确保采集配置所关联的机器组严格等于machineGroups中定义的列表。任何不在该列表中的机器组都会被自动解除关联。
自动创建支持：如果指定的机器组不存在，系统会自动创建同名的[标识型机器组](create-a-user-defined-identity-machine-group.md)，并将其与当前采集配置绑定。

| 参数 | 数据类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 否 | 要关联的机器组名称。 |
