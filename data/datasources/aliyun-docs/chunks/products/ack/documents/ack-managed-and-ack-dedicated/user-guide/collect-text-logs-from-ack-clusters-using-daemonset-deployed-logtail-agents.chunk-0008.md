ane-component-logs-of-ack-managed-cluster.md)。
安装完成后，自动生成名为k8s-log-<YOUR_CLUSTER_ID>的Project，并在该Project下生成如下资源，可登录[日志服务控制台](https://sls.console.aliyun.com)查看资源。

| 资源类型 | 资源名称 | 作用 | 示例 |
| --- | --- | --- | --- |
| 机器组 | k8s-group- <YOUR_CLUSTER_ID> | logtail-daemonset 的机器组，主要用于日志采集场景。 | k8s-group-my-cluster-123 |
| k8s-group- <YOUR_CLUSTER_ID> -statefulset | logtail-statefulset 的机器组，主要用于指标采集场景。 | k8s-group-my-cluster-123-statefulset |  |
| k8s-group- <YOUR_CLUSTER_ID> -singleton | 单实例机器组，主要用于部分单实例采集配置。 | k8s-group-my-cluster-123-singleton |  |
| Logstore | config-operation-log | 用于存储 Logtail 组件中的 alibaba-log-controller 日志。建议不要在此 Logstore 下创建采集配置。该 Logstore 可以删除，删除后不会再采集 alibaba-log-controller 的运行日志。该 Logstore 的收费标准和普通的 Logstore 收费标准是一致的，具体请参见 [按写入数据量计费模式计费项](../../../../sls/documents/billing-items-in-the-pay-per-data-write-mode.md) 。 | 无 |
