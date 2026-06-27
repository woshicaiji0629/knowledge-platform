# 容器服务Kubernetes版的使用配额和限制-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/product-overview/limits

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/product-overview.md)

- [操作指南](products/ack/documents/ack-user-guide.md)

- [服务支持](products/ack/documents/support.md)

[首页](https://help.aliyun.com/zh)

# 容器服务Kubernetes版的使用配额和限制

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍使用阿里云容器服务 Kubernetes 版过程中涉及的配额与限制，包括产品与集群配置限制、单集群容量限制、集群配额和依赖底层云产品配额。

## 限制

### 产品与集群配置限制

开通容器服务 Kubernetes 版前以及使用ACK集群过程中，有以下使用限制。

- 

- 

- 

- 

- 

- 

- 

| 限制项 | 说明 |
| --- | --- |
| 账号认证 | 创建 ACK 集群前，需已完成实名认证并已开通容器服务 ACK，详见 [开通容器服务](products/ack/documents/ack-managed-and-ack-dedicated/getting-started/quick-start-for-first-time-users.md) [ACK](products/ack/documents/ack-managed-and-ack-dedicated/getting-started/quick-start-for-first-time-users.md) 。 |
| 账户余额 | ACK 集群创建时，账户余额和代金券总值需不少于 100 元，才可创建按量计费的阿里云资源。 如计划在创建 ACK 托管集群 或 ACK 专有集群 时，在 集群配置 页面选择 付费类型 为 包年包月 ，并指定至少 1 台 ECS 实例，请确保账户余额足够支付包年包月 ECS 实例费用以及其他产品费用。如余额不足，集群创建后节点数量会少于预期，续费后将恢复正常。 |
| 集群配置 | ACK 集群创建后，以下配置不可更改，请注意。 集群 VPC 不可变更。 集群类型不可直接变更，例如 ACK 专有集群 不可直接变更为 ACK 托管集群 。 目前支持 [热迁移](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md) [ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md) [专有集群至](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md) [ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md) [托管集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md) [Pro](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md) [版](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md) 。 集群规格不可直接变更，例如 ACK 托管集群 Pro 版 不可变更为 ACK 托管集群基础版 。 目前支持 [热迁移](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [托管集群基础版至](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [托管集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [Pro](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [版](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) 。 网络插件（Terway、Flannel）不支持相互转换。 |
| ECS 实例（节点实例）配置 | 支持按量付费、包年包月以及抢占式实例三种付费模式。可在 [ECS](https://ecs.console.aliyun.com) [管理控制台](https://ecs.console.aliyun.com) 将 [按量付费实例转换为包年包月实例](products/ecs/documents/change-the-billing-method.md) 。 由于 ECS 等底层依赖产品有配额及库存限制，创建、扩容集群或自动弹性扩容集群时，可能只有部分节点创建成功。 节点规格为 4 核 8 GB 及以上。详见 [ECS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/select-ecs-instances-to-create-the-master-and-worker-nodes-of-an-ack-cluster.md) [实例规格配置建议](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/select-ecs-instances-to-create-the-master-and-worker-nodes-of-an-ack-cluster.md) 。 |
| 集群管控组件访问流量 | 当通过 API 或命令行访问集群管控组件（API Server、etcd）时，由于访问带宽的限制，当一次性读取大量的集群事件时，可能触发限流从而导致读取失败。建议使用事件中心查询集群事件，或者在 API、命令行中添加分页参数以降低单次请求量（例如： --chunk-size=500 ）。详见 [场景一：使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/event-monitoring.md) [NPD](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/event-monitoring.md) [结合](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/event-monitoring.md) [SLS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/event-monitoring.md) [的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/event-monitoring.md) [Kubernetes](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/event-monitoring.md) [事件中心监控集群事件](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/event-monitoring.md) 。 此外，如果在 ACK 托管集群基础版 中频繁遇到限流问题，请迁移至 ACK 托管集群 Pro 版 。详见 [热迁移](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [基础版集群至](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [ACK Pro](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [版集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) 。 |


### 单集群容量限制

ACK托管集群Pro版和ACK托管集群基础版适用场景不同，支持容量也不同。

- 

ACK托管集群Pro版：适用于企业生产环境（推荐使用）。

在ACK托管集群Pro版中配置网络插件为Terway网络插件，并启用IPvlan时，5000节点规模下，Pod上限为50000，Service和Pod总的映射上限为64000。

- 

ACK托管集群基础版：仅供个人测试或学习使用。

下表介绍单集群内不同资源类型的最大容量。

- 

- 

| 类型 | ACK 托管集群 Pro 版 | ACK 托管集群基础版 |
| --- | --- | --- |
| etcd 存储容量 | 8 GB | 2 GB |
| 每种资源类型 etcd 对象总大小 | 800MB | 200MB |
| Node | Flannel：默认支持 200 个，最大支持 1,000 个 Terway：默认支持 5,000 个，最大支持 15,000 个 | 10 个 |
| Pod | 150,000 个 具体取决于网络插件和可用 Pod 网段配置 | 300 个 |
| Namespace | 10,000 个 | 100 个 |
| ConfigMap | 30,000 个 | 300 个 |
| Secret | 100,000 个 | 1000 个 |
| PVC | 100,000 个 | 1,000 个 |
| PV | 100,000 个 | 1,000 个 |
| Service | 10,000 个 | 100 个 |
| Role | 50,000 个 | 500 个 |
| RoleBinding | 50,000 个 | 500 个 |
| CRD | 100,000 个 | 1,000 个 |
| 每种 CRD 类型 CR 资源数 | 100,000 个 | 1,000 个 |


## 配额（Quota）

### 集群配额

- 

下表仅展示各限制项的默认配额。关于本产品支持调整的配额项以及支持调整的配置上限，可以前往[配额中心](https://quotas.console.aliyun.com)查看和申请。配额中心现已支持多个云产品，具体信息，请参见[配额中心支持的云产品](https://help.aliyun.com/zh/quota-center/product-overview/alibaba-cloud-services-that-support-quota-center#topic-2622763)。

- 

①：如需使申请提高的单集群最大节点池数配额生效，还需同时申请弹性伸缩ESS的伸缩组总数配额，请登录[配额平台提交申请](https://quotas.console.aliyun.com/products/csk/quotas)。

- 

②：单节点最大Pod数受集群网络插件影响。

- 

Flannel：受集群创建时网段规划影响。可参考下表，且不支持申请提高。

- 

Terway：依赖[ECS](products/ecs/documents/user-guide/overview-of-instance-families.md)[实例规格](products/ecs/documents/user-guide/overview-of-instance-families.md)所提供的弹性网卡数量，建议选择较高规格和较新类型的ECS机型。

## ACK托管集群

- 

- 

- 

- 

| 维度 | 基础版 | Pro 版 |
| --- | --- | --- |
| 单阿里云账号最大集群数 | 2 | 100 |
| 单集群最大节点池数 ① | 10 | 100 |
| 单集群最大节点数 | 10 | 使用 Flannel 容器网络插件：默认支持 200 个，最大支持 1000 个节点 使用 Terway 容器网络插件：默认支持 5,000 个，最大支持 15,000 个节点 |
| 单集群最大 Serverless Pod 数 | 1,000 | 50,000 重要 在 Pod 大量关联 Service 的情况下，建议保持在 20,000 个以内。 |
| 单节点最大 Pod 数 ② | 使用 Flannel 容器网络插件：256 使用 Terway 容器网络插件：单节点 Pod 限额由节点规格决定。详见 [节点](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) [Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) [限额计算方法](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) |  |
| 配额提升方式 | 不可申请 | [到配额平台提交申请](https://quotas.console.aliyun.com/products/csk/quotas) |


## ACK专有集群

- 

单阿里云账号最大集群数：0（[已停止创建](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-dedicated-cluster.md)）

- 

单集群最大节点池数①：100

- 

单集群最大节点数：

- 

使用Flannel容器网络插件：默认支持200个，最大支持1000个节点

- 

使用Terway容器网络插件：默认支持5,000个，最大支持15,000个节点

- 

单节点最大Pod数②：

- 

使用Flannel容器网络插件：256

- 

使用Terway容器网络插件：单节点Pod限额由节点规格决定。详见[节点](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-terway.md)[Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-terway.md)[限额计算方法](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-terway.md)

- 

配额提升方式：

[到配额平台提交申请](https://quotas.console.aliyun.com/products/csk/quotas)

## ACK Serverless集群

| 维度 | 基础版 | Pro 版 |
| --- | --- | --- |
| 单阿里云账号最大集群数 | 2 | 100 |
| 单集群最大 Pod 数 | 1,000 | 50,000 重要 在 Pod 大量关联 Service 的情况下，建议保持在 20,000 个以内。 |
| 配额提升方式 | [到配额平台提交申请](https://quotas.console.aliyun.com/products/csk/quotas) |  |


## ACK Edge集群

| 维度 | 基础版 | Pro 版 |
| --- | --- | --- |
| 单阿里云账号最大集群数 | 2 | 100 |
| 单集群最大节点池数 ① | 10 | 100 |
| 单集群最大节点数 | 10 | 1,000 |
| 单节点最大 Pod 数 ② | 256 | 256 |
| 配额提升方式 | 不可申请 | [到配额平台提交申请](https://quotas.console.aliyun.com/products/csk/quotas) |


## 注册集群

- 

单阿里云账号最大集群数：5

- 

单集群最大节点池数①：100

- 

单节点最大Pod数②：256

- 

配额提升方式：

[到配额平台提交申请](https://quotas.console.aliyun.com/products/csk/quotas)

### 依赖底层云产品配额

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 产品类型 | 限制项 | 默认限制 | 配额提升方式 |
| --- | --- | --- | --- |
| [云服务器](products/ecs/documents/user-guide/limitations.md) [ECS](products/ecs/documents/user-guide/limitations.md) | 阿里云资源编排服务 ROS（Resource Orchestration Service）配额 | 100 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) |
| 按量实例 vCPU 限额 | 500 核 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) |  |
| 按量实例购买高配规格（大于 16c 的实例） | vCPU 核数少于 16（不含 16）的实例规格 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) |  |
| 抢占实例 vCPU 限额 | 800 核 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) |  |
| 按量付费转包年包月 | 不支持的实例规格（族）：t1、s1、s2、s3、c1、c2、m1、m2、n1、n2、e3 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) |  |
| ESS 单个伸缩组可以设置的组内最大 ECS 实例数 | 2,000 | [到配额平台提交申请](https://quotas.console.aliyun.com/products/csk/quotas) |  |
| 操作系统 | ACK 支持添加以下操作系统的节点： Alibaba Cloud Linux ContainerOS CentOS 7.x 说明 不支持 CentOS 8.x 及以上的操作系统。 Windows Server 2019 和 Windows Server Core, version 1809 及以上 说明 Kubernetes 1.28 版本不再支持创建 Windows 节点池。 | 无 |  |
| [网络](products/vpc/documents/understanding-vpc-quotas-in-alibaba-cloud.md) | 仅适用于 Flannel 网络插件的集群 单个路由表支持创建的自定义路由条目的数量（不包括 [动态传播路由条目](products/vpc/documents/vpc-route-table.md) ） | 200 条 | 请参见 [通用配额](products/vpc/documents/understanding-vpc-quotas-in-alibaba-cloud.md) 。 |
| 单个 VPC 支持创建的交换机的数量 | 150 个 |  |  |
| 单个地域支持创建的 VPC 的数量 | 10 个 |  |  |
| 单个阿里云账号在特定地域下单个专有网络 VPC 类型的安全组能容纳的私网 IP 地址数量 | 普通安全组：6,000 企业级安全组：65,535 | 普通安全组可前往 [配额中心](https://quotas.console.aliyun.com/products/ecs/quotas?spm=a2c4g.11186623.0.0.376656addmG73f) 申请。 |  |
| 单个阿里云账号在特定地域下的安全组总数量上限 | 请根据配额 ID q_security-groups 查看或申请提升对应配额。具体操作请参见 [查看或提升云服务器 ECS](products/ecs/documents/user-guide/quota-management.md) [配额](products/ecs/documents/user-guide/quota-management.md) 。 |  |  |
| 单个阿里云账号在特定地域下能创建的弹性网卡（辅助网卡）的最大数量 | 请根据配额 ID q_elastic-network-interfaces 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS](products/ecs/documents/user-guide/quota-management.md) [配额](products/ecs/documents/user-guide/quota-management.md) 。 | [查看或提升云服务器 ECS](products/ecs/documents/user-guide/quota-management.md) [配额](products/ecs/documents/user-guide/quota-management.md) |  |
| 单个账号可申请的 EIP 数量 | 20 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com) 提升配额。 |  |
| [负载均衡](products/slb/documents/classic-load-balancer/product-overview/limits-1.md) | 一个阿里云账号（主账号）可创建的 CLB 实例数量 | 60 个 | 按需选择一种方式： 前往 [负载均衡配额管理页面](https://slb.console.aliyun.com/slb/quota) ，提升 slb_quota_instances_num 配额。具体操作，请参见 [配额管理](products/slb/documents/classic-load-balancer/user-guide/quota-management.md) 。 前往 [配额中心](https://quotas.console.aliyun.com/products/slb/quotas?query=slb_quota_instances_num) 提升配额。具体操作，请参见 [管理](products/slb/documents/classic-load-balancer/user-guide/manage-clb-quotas.md) [CLB](products/slb/documents/classic-load-balancer/user-guide/manage-clb-quotas.md) [配额](products/slb/documents/classic-load-balancer/user-guide/manage-clb-quotas.md) 。 |
| 一个 CLB 实例可添加的后端服务器数量 | 200 个 | 按需选择一种方式： 前往 [负载均衡配额管理页面](https://slb.console.aliyun.com/slb/quota) ，提升 slb_quota_backendservers_num 配额。具体操作，请参见 [配额管理](products/slb/documents/classic-load-balancer/user-guide/quota-management.md) 。 前往 [配额中心](https://quotas.console.aliyun.com/products/slb/quotas?query=slb_quota_backendservers_num) 提升配额。具体操作，请参见 [管理](products/slb/documents/classic-load-balancer/user-guide/manage-clb-quotas.md) [CLB](products/slb/documents/classic-load-balancer/user-guide/manage-clb-quotas.md) [配额](products/slb/documents/classic-load-balancer/user-guide/manage-clb-quotas.md) 。 |  |
| 一个 CLB 实例可添加的监听数量 | 50 个 | 按需选择一种方式： 前往 [负载均衡配额管理页面](https://slb.console.aliyun.com/slb/quota) ，提升 slb_quota_listeners_num 配额。具体操作，请参见 [配额管理](products/slb/documents/classic-load-balancer/user-guide/quota-management.md) 。 前往 [配额中心](https://quotas.console.aliyun.com/products/slb/quotas?query=slb_quota_listeners_num) 提升配额。具体操作，请参见 [管理](products/slb/documents/classic-load-balancer/user-guide/manage-clb-quotas.md) [CLB](products/slb/documents/classic-load-balancer/user-guide/manage-clb-quotas.md) [配额](products/slb/documents/classic-load-balancer/user-guide/manage-clb-quotas.md) 。 |  |
| 同一台服务器可以重复添加为 CLB 后端服务器的次数 | 50 次 | 无 |  |
| [块存储](products/ecs/documents/user-guide/limitations.md) | 一个账号在所有地域的按量付费云盘数量配额 | 账号下所有地域的实例数量*5。每个账号最少可以创建 10 块按量付费云盘。 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) |
| 一个账号用作数据盘的按量付费云盘容量配额 | 和云服务器使用情况、地域、云盘类型有关，您可以在权益配额页面查看，更多信息，请参见 [块存储](products/ecs/documents/user-guide/limitations.md) 。 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) |  |


## 相关文档

- 

不同集群类型有针对不同功能的注意事项和高危风险操作，请仔细阅读，详见[使用须知及高危风险操作说明](products/ack/documents/product-overview/before-you-start.md)。

- 

为保证集群应用稳定可靠，请参见[工作负载推荐配置](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/recommended-configurations-for-high-reliability.md)合理配置集群、工作负载和组件。

- 

可通过添加更多节点来增加支持的Pod数量。但集群规模过大可能对集群的可用性及性能产生影响，请合理设计和使用。详见[大规模集群使用建议](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/suggestions-on-how-to-work-with-large-ack-pro-clusters.md)。

[上一篇：使用须知及高危风险操作说明](products/ack/documents/product-overview/before-you-start.md)[下一篇：开源项目](products/ack/documents/product-overview/open-source-projects.md)

该文章对您有帮助吗？

反馈

### 为什么选择阿里云

[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)

### 大模型

[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)

### 产品和定价

[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)

### 技术内容

[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)

### 权益

[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)

### 服务

[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)

### 关注阿里云

关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务

联系我们：4008013260

[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)

### 友情链接

[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)

© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
