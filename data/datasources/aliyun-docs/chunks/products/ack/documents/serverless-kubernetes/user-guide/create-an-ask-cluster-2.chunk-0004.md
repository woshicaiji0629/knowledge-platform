### 基础信息配置

| 配置项 | 描述 |
| --- | --- |
| 集群名称 | 自定义集群名称。 |
| 集群规格 | Pro 版：提供 SLA 保障，适用于企业生产和测试环境。 基础版： [配额](../../product-overview/limits.md) 有限（每个账号支持创建 2 个集群），仅供个人学习与测试。 关于规格对比，请参见 [集群对比](ask-pro-cluster-overview.md) 。 |
| 地域 | 集群资源（ECS 实例、云盘等）所处 [地域](../../product-overview/supported-regions.md) 。地域与 用户和资源部署地域的距离越近，网络时延越低。 |
| Kubernetes 版本 | 仅支持创建最近三个 [次要版本](../../ack-managed-and-ack-dedicated/user-guide/support-for-kubernetes-versions.md) ，推荐使用当前最新版本。请参见 [ACK](../../product-overview/release-notes-for-kubernetes-versions.md) [版本支持概览](../../product-overview/release-notes-for-kubernetes-versions.md) 了解 ACK 的版本支持情况。 |
| 自动升级 | 开启集群的自动升级能力，保持集群控制面的周期性自动升级。ACK 会在集群维护窗口期内执行集群自动升级。关于自动升级的策略介绍和使用方法，请参见 [自动升级集群](automatically-upgrade-an-ack-cluster.md) 。 |
| 集群维护窗口 | ACK 将在维护窗口期内进行集群版本自动升级。您可以单击 设置 ，配置具体的维护策略。 |
