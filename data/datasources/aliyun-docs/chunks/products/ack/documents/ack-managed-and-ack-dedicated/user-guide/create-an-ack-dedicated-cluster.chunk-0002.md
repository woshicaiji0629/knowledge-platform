### 控制台
步骤一：登录容器服务管理控制台
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在页面左侧顶部，选择目标资源所在的资源组和地域。
在集群列表页面，单击创建集群。
步骤二：配置集群
单击ACK 专有集群页签，完成集群基础信息配置、网络配置和高级选项配置。
基础信息配置

| 配置项 | 描述 |
| --- | --- |
| 集群名称 | 自定义集群名称。 |
| 地域 | 集群资源（ECS 实例、云盘等）所处 [地域](../../product-overview/supported-regions.md) 。地域与 用户和资源部署地域的距离越近，网络时延越低。 |
| Kubernetes 版本 | 仅支持创建最近三个 [次要版本](support-for-kubernetes-versions.md) ，推荐使用当前最新版本。请参见 [ACK](../../product-overview/release-notes-for-kubernetes-versions.md) [版本支持概览](../../product-overview/release-notes-for-kubernetes-versions.md) 了解 ACK 的版本支持情况。 |

网络配置
