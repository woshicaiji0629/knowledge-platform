# 在ACK中为容器应用配置存储-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/csi-overview-1

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-managed-and-ack-dedicated/product-overview.md)

- [快速入门](products/ack/documents/ack-managed-and-ack-dedicated/getting-started.md)

- [操作指南](products/ack/documents/ack-managed-and-ack-dedicated/user-guide.md)

- [实践教程](products/ack/documents/ack-managed-and-ack-dedicated/use-cases.md)

- [安全合规](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference.md)

- [服务支持](products/ack/documents/ack-managed-and-ack-dedicated/support.md)

[首页](https://help.aliyun.com/zh)

# 存储概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Kubernetes应用通常需要持久化存储来保存数据。ACK通过标准的容器存储接口CSI，集成了多种阿里云存储服务（如云盘、OSS、NAS、CPFS等），并兼容Kubernetes原生存储机制，为不同业务场景提供存储解决方案。

## 存储方案选型

ACK的存储方案分为两类：

- 

Kubernetes原生存储卷：用于临时数据、配置管理或与节点的交互。生命周期通常与Pod绑定，不适用于需要持久化保存应用数据的场景。

- 

阿里云持久化存储卷：通过CSI组件集成，为工作负载提供稳定、可靠的数据持久化能力。生命周期独立于Pod，可用于有状态应用。

使用容器存储功能前，确保已了解相关概念，如存储卷、PV、PVC等，详见[存储基础知识](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/storage-basics.md)。

### Kubernetes 原生存储卷

Kubernetes原生存储卷的生命周期通常与Pod绑定，不适用于需要持久化保存应用数据的场景。

| 类型 | 说明 | 核心特点 |
| --- | --- | --- |
| emptyDir | 与 Pod 生命周期相同的临时空目录。 | Pod 删除后数据即丢失。可用于 Pod 内容器间数据交换或临时缓存。 |
| HostPath | 将节点宿主机上的文件或目录挂载到 Pod 中。可通过 type 字段（如 DirectoryOrCreate ）控制挂载前的检查和创建行为。 详见 [HostPath](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-hostpath-volumes.md) [数据卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-hostpath-volumes.md) | 数据与节点绑定，不随 Pod 迁移。不适用于需要高可用和持久化存储的有状态应用（如数据库、缓存）。 |
| ConfigMap/Secret | 以文件形式挂载配置项或敏感凭据。 | 仅用于存储小体积配置数据，非业务数据。用于将配置与应用解耦。 |


### 阿里云持久化存储卷

对于需要持久化存储数据的有状态应用，应选择由阿里云存储服务提供的持久化存储卷。这些存储卷的生命周期独立于Pod，通过CSI实现与Kubernetes的集成。

方案对比

为便于快速选型，表格中各存储方案的标题下方提供了部分核心属性的快速索引。以云盘为例：

- 

[云盘](products/ecs/documents/user-guide/elastic-block-storage-devices.md)：方案详细说明。单击可查看详情。

- 

[静态](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-a-statically-provisioned-disk-volume.md)/[动态](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-dynamically-provisioned-disk-volumes.md)：方案支持的[存储卷挂载方式](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/storage-basics.md)，包括静态存储卷（PV/PVC）和动态存储卷（StorageClass/PVC）。单击可查看具体操作文档。

- 

RWO：方案支持的[存储卷访问模式](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/storage-basics.md)（accessModes），包括RWO（ReadWriteOnce）、RWX（ReadWriteMany）、ROX（ReadOnlyMany）。

- 

[计费](products/ecs/documents/block-storage-devices.md)：方案计费说明。单击可查看详情。

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

| 存储方案 | 说明 | 权衡与限制 |
| --- | --- | --- |
| [云盘](products/ecs/documents/user-guide/elastic-block-storage-devices.md) [静态](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-a-statically-provisioned-disk-volume.md) / [动态](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-dynamically-provisioned-disk-volumes.md) | RWO（未启用多重挂载） | [计费](products/ecs/documents/block-storage-devices.md) | 说明：提供高数据可靠性（9 个 9）和稳定 I/O 性能的块存储服务，数据在后端采用三副本机制。支持文件系统（ volumeMode: Filesystem ）及块设备模式（ volumeMode: Block ），并提供多种 [性能](products/ecs/documents/user-guide/block-storage-performance.md) 规格（ESSD AutoPL、ESSD 云盘、ESSD Entry 等）和静态加密能力。 场景：适用于数据库（MySQL/PostgreSQL）、中间件（Redis/ES）等对 I/O 性能和数据可靠性要求高的单实例有状态应用。 | accessModes 限制：未开启多重挂载的云盘同一时间只能被单个 Pod 挂载，无法原生满足多实例共享数据的业务需求（如 Web 集群内容共享）。 推荐用于 StatefulSet 或单 Pod，不推荐用于多副本 Deployment，详见操作文档。 可用区绑定：除 ESSD 同城冗余云盘外，其他云盘类型只能挂载到同一可用区下的 Pod。 建议使用 WaitForFirstConsumer 模式的 StorageClass，实现拓扑感知调度。 规格匹配：云盘类型与 ECS 实例规格存在匹配关系，详见 [实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md) 。 |
| [NAS](https://help.aliyun.com/zh/nas/product-overview/what-is-nas) [静态](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-nas-volumes.md) / [动态](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/mount-a-dynamically-provisioned-nas-volume.md) | RWX、RWO、ROX | [计费](https://help.aliyun.com/zh/nas/product-overview/overview-1) | 说明：支持 NFS 协议的共享文件存储，支持多 Pod 并发读写，容量和性能可弹性伸缩。提供回收站、快照、备份等数据保护能力。 场景：Web 集群内容共享、CI/CD 流水线、日志集中存储、以及其他需要多应用实例并发读写同一份数据的场景。 | 网络 I/O 开销：读写均通过网络进行，相比云盘会引入额外的毫秒级延迟，不推荐用于数据库等对 I/O 延迟极其敏感的应用。 “邻居噪声”：在 subpath 和 sharepath 的共享实例模式下，动态供应的 PV 是后端同一个 NAS 的子目录，共享性能（带宽、IOPS）可能引发“邻居噪声”。 协议与网络限制：仅支持 NFS 协议，且不支持跨 VPC 挂载。 |
| [OSS](products/oss/documents/user-guide/what-is-oss.md) 静态 [ossfs 1.0](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md) / [ossfs 2.0](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/mount-oss-volumes-through-ossfs-2-0.md) 动态 [ossfs 1.0](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-dynamically-provisioned-oss-volumes.md) / [ossfs 2.0](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/using-dynamically-provisioned-volumes-with-ossfs-2-0.md) RWX、ROX | [计费](products/oss/documents/billing-overview.md) | 说明：海量、低成本的对象存储服务。通过 ossfs 工具可将 Bucket 模拟成文件系统挂载到 Pod 中，单位存储成本低。提供 ossfs 1.0 （注重 POSIX 兼容性）和 ossfs 2.0 （为高吞吐、大并发场景优化）两种挂载方式。 场景：AI/大数据分析的数据湖、网站图片/视频等静态媒体资源存储、应用数据备份与归档。 | 性能非原生：基于用户态文件系统（FUSE）实现，文件系统操作需转换为 HTTP API 调用，导致高延迟和低随机 I/O 性能，不推荐用于数据库或高频写入场景。 POSIX 兼容性不完整：无法完整支持所有标准文件系统操作，如对根路径执行 chmod 、 chown 受限，可能引发应用兼容性问题。 |
| [CPFS 智算版](https://help.aliyun.com/zh/cpfs/bmcpfs/product-overview/what-is-cpfs-for-lingjun) [静态](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-cpfs-for-lingjun-statically-provisioned-volumes.md) / [动态](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-cpfs-for-lingjun-dynamic-volumes.md) | RWX | [计费](https://help.aliyun.com/zh/cpfs/bmcpfs/product-overview/billing-description) | 说明：专为 AI 与智算领域打造的超高性能并行文件系统，提供高并发吞吐和 IOPS 性能。 场景：AIGC 大模型训练/推理、自动驾驶仿真等对并行 I/O 性能要求高的 AI 智算领域。 | 成本与可用性：成本较高，面向特定高性能场景。处于邀测阶段且仅在 [部分地域](https://help.aliyun.com/zh/cpfs/bmcpfs/product-overview/what-is-cpfs-for-lingjun#cc2c2e40famtq) 可用。 挂载限制：不支持跨 VPC 挂载。 |
| [CPFS 通用版](https://help.aliyun.com/zh/cpfs/cpfsonecs/product-overview/what-is-cpfs) [静态](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/statically-provisioned-cpfs-2-0-volumes-1.md) | RWX | [计费](https://help.aliyun.com/zh/cpfs/cpfsonecs/product-overview/cpfs-billing-overview) | 说明：面向高性能计算（HPC）场景的共享文件系统，提供高于通用 NAS 的 IOPS 和吞吐带宽。 场景：基因计算、大数据分析、数据缓存加速等传统 HPC 领域。 | 成本与可用性：成本高于通用 NAS，且仅在 [部分地域](https://help.aliyun.com/zh/cpfs/cpfsonecs/product-overview/what-is-cpfs#section-5kf-e2e-fit) 可用。 挂载限制：仅支持 NFS 协议，且不支持跨 VPC 挂载。 |


除基础性能外，不同存储方案在故障恢复、容量管理和数据保护等运维场景中也存在差异，可从以下几个问题进一步规划选型。

Pod所在节点故障时，应用和数据如何恢复？

当Pod所在节点发生故障时，应用能否快速恢复、数据是否安全，是高可用架构的核心。

- 

云盘：CSI会自动将云盘从旧节点卸载，并挂载到新节点。

- 

NAS / OSS / CPFS：共享存储，Pod 在新节点启动后可立即重新挂载，无需等待存储卷“漂移”。恢复速度仅取决于应用本身的启动时间。

- 

HostPath：数据固定在特定节点上。如果该节点故障，Pod 将无法在其他节点上启动并访问原有数据。依赖应用自身实现跨节点的数据复制和高可用。

选型建议：如果应用（如单实例数据库）可容忍分钟级中断，可选择云盘。如需实现快速故障切换（如高可用 Web 服务），建议优先使用共享存储并部署多副本。如果应用自身处理数据复制和高可用，可选择本地盘以获得极致性能。

如何规划和管理应用的存储容量？

合理的容量规划能有效控制成本，并防止因存储耗尽导致服务中断。不同存储类型的 PVC 容量声明对实际存储用量的约束效果存在差异。

- 

云盘：PVC 声明的容量与实际分配的云盘容量一一对应，容量限制可实际生效，且支持[在线扩容](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/expand-a-disk-volume-without-service-interruptions.md)。适合容量需求明确、需要严格资源隔离的场景。

- 

OSS：本身无实际容量上限，按实际用量计费。PVC 容量仅用于匹配PV，不限制实际存储用量。

- 

NAS / CPFS：

- 

静态卷：PVC 容量仅用于匹配PV，不对实际存储用量产生限制；实际可用容量取决于后端实例的总容量上限，所有 Pod 共享。

- 

动态卷：NAS（仅subpath方式且[allowVolumeExpansion](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/expand-a-nas-volume.md)为true）及CPFS智算版场景下，PVC 容量将转换为对应目录的配额，限制实际容量；其他场景下行为与静态卷一致。

选型建议：对容量有精确预算和强隔离需求的应用（如多租户环境下的数据库）推荐使用云盘。大量 Pod 共享数据、容量动态变化的场景（如日志、Web 静态文件）推荐使用共享存储。

如何备份应用数据，防止误删或损坏？

- 

云盘：通过[快照](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-volume-snapshots-created-from-disks.md)实现，可对整个数据卷进行秒级创建和快速恢复，也可[创建备份计划或立即备份](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/back-up-and-restore-applications-in-an-ack-cluster.md)，降低数据丢失风险。

- 

NAS：提供[回收站](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/recover-nas-file-data-using-recycle-bin-function.md)（通过CNFS，支持恢复单个文件或目录）和[快照](https://help.aliyun.com/zh/nas/user-guide/manage-snapshots)（部分NAS类型支持）。

- 

OSS：提供[版本控制](products/oss/documents/user-guide/overview-78.md)和[生命周期](products/oss/documents/user-guide/overview-54.md)管理能力，以防止误操作，或进行数据归档。

- 

HostPath：数据保护依赖应用层的高可用和复制机制。

选型建议：需要对整个数据卷进行快速、一致性备份恢复时推荐选择云盘快照。需要长期归档、合规审计或恢复单个文件的场景，推荐使用 NAS或OSS提供的相应功能。使用HostPath则必须确保应用层有完善的数据保护策略。

## 关键组件与概念

- 

CSI组件（csi-plugin、csi-provisioner）

Kubernetes社区推荐的存储插件实现方案，已在集群中默认部署。负责与阿里云存储服务的API进行交互，实现存储卷的自动创建、挂载、卸载等全生命周期管理。详见[管理](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/install-and-upgrade-the-csi-plug-in.md)[CSI](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/install-and-upgrade-the-csi-plug-in.md)[组件](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/install-and-upgrade-the-csi-plug-in.md)。

- 

容器网络文件系统 (CNFS)

ACK托管集群Pro版提供的存储增强功能，将NAS、OSS、CPFS等抽象为Kubernetes CRD对象，提供更精细化的管理能力，如子目录动态创建、配额管理、IO性能监控、回收站、分布式缓存等。详见[容器网络文件系统](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cnfs-overview.md)[CNFS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cnfs-overview.md)。

## 使用说明

使用CSI时需注意以下使用限制。

- 

集群版本：需为1.14及以上。如需升级，请参见[手动升级集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-the-kubernetes-version-of-an-ack-cluster.md)。

- 

集群环境：已在ACK集群中完成全面适配和验证。对于非ACK集群（非阿里环境集群、阿里云自建集群），由于配置、权限、网络等环境差异，CSI无法保证开箱即用。

建议参见[alibaba-cloud-csi-driver](https://github.com/kubernetes-sigs/alibaba-cloud-csi-driver/tree/master)源码并结合自身环境进行适配。

- 

节点配置：kubelet运行参数--enable-controller-attach-detach为true。

- 

操作系统：不支持Windows节点。

- 

RBAC权限：PV是集群级别的资源，PVC是命名空间级别的资源。进行RBAC授权时，需注意不同角色对这两类资源的权限差异。

如果ACK默认提供的预置角色（管理员、运维人员等）无法满足需求，请配置自定义权限。例如，ACK默认的运维人员角色对PVC有读写权限，但对PV仅有只读权限，因此无法手动创建PV。详见[使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[RBAC](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[为集群内资源操作授权](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)。

## FAQ

### 如何判断集群使用的存储插件模式？

可选择以下方式查看。

## 通过控制台查看节点注释

- 

在[ACK](https://cs.console.aliyun.com)[集群列表](https://cs.console.aliyun.com)页面，单击目标集群名称，在集群详情页左侧导航栏，选择节点管理>节点。

- 

在节点列表的操作列，单击详情，在基本信息页签下查看节点注释。

若存在volumes.kubernetes.io/controller-managed-attach-detach: true，表示存储插件为CSI；若不存在，则为Flexvolume。

## 通过命令查看kubelet参数

[登录节点](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/overview-of-node-management.md)，查看kubelet参数。

ps -ef | grep kubelet

预期输出：

--enable-controller-attach-detach=true

- 

true：存储插件为CSI。

- 

false：存储插件为Flexvolume。

### 如何手动为CSI授权？

CSI在执行存储卷的挂载、卸载、创建、删除等操作时，需要被授予访问其他产品资源的相应权限。通常情况下，集群已默认安装CSI且配置相关权限。如需手动授权，可参见以下内容。

- 

使用RAM角色授权（默认）：CSI使用AliyunCSManagedCsiRole角色来访问其他云产品资源，详见[容器服务](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ack-default-roles.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ack-default-roles.md)[服务角色](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ack-default-roles.md)。

- 

ACK托管集群：CSI使用的RAM角色权限的Token被保存在名为addon.csi.token的Secret中。可挂载该Secret，从而实现RAM角色授权。

- 

ACK专有集群：CSI继承其Pod所在节点的RAM角色。

关于如何为RAM角色授权，请参见[管理](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色的权限](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。

- 

使用AccessKey授权

- 

通过环境变量：将AccessKey创建为Kubernetes Secret，再通过环境变量的方式注入到CSI的Pod中，避免在部署模板中明文暴露密钥。

- 

直接写入YAML：直接在CSI的YAML中写入AccessKey信息。不推荐在生产环境使用。

## 附录

### 快速入门视频

关于ACK使用存储卷的快速入门，请参见以下视频：

## 相关文档

- 

启用[存储监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/storage-monitoring.md)，监控集群存储资源或定位客户端IO问题。

- 

ACK Edge集群支持[使用](products/ack/documents/ack-edge/user-guide/use-ens-disks.md)[ENS](products/ack/documents/ack-edge/user-guide/use-ens-disks.md)[云盘](products/ack/documents/ack-edge/user-guide/use-ens-disks.md)。

- 

关于容器存储的最佳实践，请参见[存储最佳实践](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/best-practices-for-storage.md)。

- 

使用容器存储时如遇问题，可参见[存储异常问题排查](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/storage-troubleshooting-1.md)、[存储](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-csi.md)[FAQ-CSI](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-csi.md)排查。

- 

Flexvolume已停止维护，需迁移至CSI，详见[迁移](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/upgrade-from-flexvolume-to-csi.md)[Flexvolume](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/upgrade-from-flexvolume-to-csi.md)[至](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/upgrade-from-flexvolume-to-csi.md)[CSI](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/upgrade-from-flexvolume-to-csi.md)。

[上一篇：网络管理FAQ](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-network-management.md)[下一篇：存储基础知识](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/storage-basics.md)

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
