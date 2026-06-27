## 集群生命周期
ACK集群在不同状态下的含义和状态流转如下。
重要
ACK会定时检测集群运行状态。如符合特定异常条件，集群将自动变为不活跃（inactive）或不可用（unavailable）。届时，ACK会通过短信、邮件、站内信的方式发送相关通知。
对于ACK托管集群Pro版，可参见下表了解对应状态的集群是否收取集群管理费用。ACK计费说明，请参见[计费概述](../product-overview/ack-pro-cluster-billing.md)。
集群关联云产品的计费策略以各云产品为准，请参见[云产品资源费用](../product-overview/billing-of-cloud-services.md)。

| 阶段 | 集群状态 | 说明 | 集群管理费 （ ACK 托管集群 Pro 版 ） |
| --- | --- | --- | --- |
| 创建部署 | 初始化中（initial） | 集群创建中。 | 不收取 |
| 创建失败（failed） | 集群创建失败。 |  |  |
| 运行维护 | 运行中（running） | 集群运行中。 | 收取 |
| 升级中（upgrading） | 集群升级中。 |  |  |
| 节点排水中（draining） | 正在将节点上的 Pod 驱逐并在其他节点上重建；完成后该节点将处于不可调度状态。 |  |  |
| 节点移除中（removing） | 正在移除集群中的节点。 |  |  |
| 配置变更中（updating） | 集群元信息更新中。 |  |  |
| 不活跃（inactive） | 特定异常条件下，集群暂时无法使用。详见 [不活跃（inactive）](cluster-abnormal-states.md) 。 | 不收取 |  |
| 不可用（unavailable） | 集群基础云资源异常，集群不再可用。详见 [不可用（unavailable）](cluster-abnormal-states.md) 。 |  |  |
| 删除释放 | 删除中（deleting） | 集群删除中。 | 不收取 |
| 删除失败（delete_failed） | 删除集群失败。 |  |  |
| 已删除（deleted） | 成功删除集群。该状态下集群不再可见。 |  |  |
