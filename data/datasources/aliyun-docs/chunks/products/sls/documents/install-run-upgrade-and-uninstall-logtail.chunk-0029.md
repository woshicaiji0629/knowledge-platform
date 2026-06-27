创建一个Project来管理采集到的容器日志。其中ClusterID为您新建的Kubernetes集群的唯一标识。
在日志服务区域勾选使用日志服务，选择创建新 Project后，系统将自动创建名称为k8s-log-{ClusterID}的 Project。
安装完成后，在选择的Project下自动创建如下日志服务资源。

| 资源类型 | 资源名称 | 作用 | 示例 |
| --- | --- | --- | --- |
| 机器组 | k8s-group-${your_k8s_cluster_id} | logtail-daemonset 的机器组，主要用于日志采集场景。 | k8s-group-my-cluster-123 |
| k8s-group-${your_k8s_cluster_id}-statefulset | logtail-statefulset 的机器组，主要用于指标采集场景。 | k8s-group-my-cluster-123-statefulset |  |
| k8s-group-${your_k8s_cluster_id}-singleton | 单实例机器组，主要用于部分单实例采集配置。 | k8s-group-my-cluster-123-singleton |  |
| LogStore | config-operation-log | 用于存储 Logtail 组件中的 alibaba-log-controller 日志。建议不要在此 LogStore 下创建采集配置。该 LogStore 可以删除，删除后不会再采集 alibaba-log-controller 的运行日志。该 LogStore 的收费标准和普通的 LogStore 收费标准是一致的，具体请参见 [按写入数据量计费模式计费项](billing-items-in-the-pay-per-data-write-mode.md) 。 | config-operation-log |
