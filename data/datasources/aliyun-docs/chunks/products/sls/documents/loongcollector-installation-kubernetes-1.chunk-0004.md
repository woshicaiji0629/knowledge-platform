## 新建ACK托管集群时安装
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
单击创建集群，在组件配置页面，勾选使用日志服务。支持创建新Project或使用已有Project。
本文只描述日志服务相关配置，关于更多配置项说明，请参见[创建](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。
当您选择创建新 Project时，日志服务会默认创建如下资源，您可登录[日志服务控制台](https://sls.console.aliyun.com/)查看。

| 资源类型 | 资源名称 | 作用 |
| --- | --- | --- |
| Project | k8s-log-${cluster_id} | 资源管理单元，隔离不同业务日志。 |
| 机器组 | k8s-group-${cluster_id} | loongcollector-ds 的机器组，主要用于日志采集场景。 |
| k8s-group-${cluster_id}-cluster | loongcollector-cluster 的机器组，主要用于指标采集场景。 |  |
| k8s-group-${cluster_id}-singleton | 单实例机器组，主要用于部分单实例采集配置。 |  |

重要
LoongCollector 组件中将不会创建名为config-operation-log的LogStore，若已创建的将不再写入日志。
