## ACK集群
通过容器服务控制台安装LoongCollector，默认将日志发送到当前阿里云账号的日志服务Project中。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
单击目标集群名称，进入集群详情页。
在左侧导航栏，单击组件管理。
切换至日志与监控页签，找到loongcollector，单击安装。
说明
在创建集群时，可在组件配置页面勾选使用日志服务，支持创建新 Project或使用已有 Project。
安装完成后，日志服务会在当前账号下自动创建以下资源，您可登录[日志服务控制台](https://sls.console.aliyun.com/)查看。

| 资源类型 | 资源名称 | 作用 |
| --- | --- | --- |
| Project | k8s-log-${cluster_id} | 资源管理单元，隔离不同业务日志。 如需自行创建 Project 以实现更灵活的日志资源管理，请参考 [创建](manage-a-project.md) [Project](manage-a-project.md) 。 |
| 机器组 | k8s-group-${cluster_id} | 日志采集节点集合。 |

重要
LoongCollector 组件中将不会创建名为config-operation-log的LogStore，若已创建的将不再写入日志。
