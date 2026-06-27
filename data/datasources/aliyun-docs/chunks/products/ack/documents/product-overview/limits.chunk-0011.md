| 产品类型 | 限制项 | 默认限制 | 配额提升方式 |
| --- | --- | --- | --- |
| [云服务器](../../../ecs/documents/user-guide/limitations.md) [ECS](../../../ecs/documents/user-guide/limitations.md) | 阿里云资源编排服务 ROS（Resource Orchestration Service）配额 | 100 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) |
| 按量实例 vCPU 限额 | 500 核 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) |  |
| 按量实例购买高配规格（大于 16c 的实例） | vCPU 核数少于 16（不含 16）的实例规格 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) |  |
| 抢占实例 vCPU 限额 | 800 核 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) |  |
| 按量付费转包年包月 | 不支持的实例规格（族）：t1、s1、s2、s3、c1、c2、m1、m2、n1、n2、e3 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) |  |
| ESS 单个伸缩组可以设置的组内最大 ECS 实例数 | 2,000 | [到配额平台提交申请](https://quotas.console.aliyun.com/products/csk/quotas) |  |
| 操作系统 | ACK 支持添加以下操作系统的节点： Alibaba Cloud Linux ContainerOS CentOS 7.x 说明 不支持 CentOS 8.x 及以上的操作系统。 Windows Server 2019 和 Windows Server Core, version 1809 及以上 说明 Kubernetes 1.28 版本不再支持创建 Windows 节点池。 | 无 |  |
| [网络](../../../vpc/documents/understanding-vpc-quotas-in-alibaba-cloud.md) | 仅适用于 Flannel 网络插件的集群 单个路由表支持创建的自定义路由条目的数量（不包括 [动态传播路由条目
