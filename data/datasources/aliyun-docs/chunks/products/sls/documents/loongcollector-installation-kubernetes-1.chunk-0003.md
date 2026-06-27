## ACK集群安装（DaemonSet模式）
通过阿里云ACK容器服务控制台一键安装LoongCollector，默认将集群容器日志采集到同账号同地域的Project，如需跨账号或跨地域采集请参考[自建集群安装（DaemonSet](loongcollector-installation-kubernetes-1.md)[模式）](loongcollector-installation-kubernetes-1.md)。
为已有ACK托管集群安装
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。
在日志与监控页签中，找到loongcollector，单击安装。
安装完成后，日志服务会自动在ACK所属地域下创建如下资源，您可登录[日志服务控制台](https://sls.console.aliyun.com/)查看。

| 资源类型 | 资源名称 | 作用 |
| --- | --- | --- |
| Project | k8s-log-${cluster_id} | 资源管理单元，隔离不同业务日志。 |
| 机器组 | k8s-group-${cluster_id} | loongcollector-ds 的机器组，主要用于日志采集场景。 |
| k8s-group-${cluster_id}-cluster | loongcollector-cluster 的机器组，主要用于指标采集场景。 |  |
| k8s-group-${cluster_id}-singleton | 单实例机器组，主要用于部分单实例采集配置。 |  |

重要
LoongCollector 组件中将不会创建名为config-operation-log的LogStore，若已创建的将不再写入日志。
