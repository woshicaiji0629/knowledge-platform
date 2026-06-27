# 创建ACK专有集群-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/create-an-ack-dedicated-cluster

# 创建ACK专有集群
在ACK专有集群中，您需要创建至少3个Master节点以保证高可用性，以及若干Worker节点，以对集群基础设施进行更细粒度的控制，但需要自行规划、维护、升级集群。本文介绍如何通过控制台、API、Terraform、SDK以及CLI等方式创建ACK专有集群。
重要
容器服务 Kubernetes 版已于2024年08月21日起停止ACK专有集群的创建。推荐您在生产环境中使用具有更高可靠性、安全性和调度效率的ACK托管集群Pro版。
如需创建ACK托管集群Pro版，请参见[创建](create-an-ack-managed-cluster-2.md)[ACK](create-an-ack-managed-cluster-2.md)[托管集群](create-an-ack-managed-cluster-2.md)。
如需将ACK专有集群迁移至ACK托管集群Pro版，请参见[热迁移](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[专有集群至](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[托管集群](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[Pro](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[版](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)。
## 准备工作
创建集群前，请确保您已经开通容器服务ACK、为您的阿里云账号或RAM账号授予了ACK系统服务角色（ACK需要这些权限来调用相关服务或执行集群操作），并且开通了相关云产品（例如VPC、负载均衡、NAT网关等）。具体操作，请参见[快速创建](../getting-started/quick-start-for-first-time-users.md)[ACK](../getting-started/quick-start-for-first-time-users.md)[托管集群](../getting-started/quick-start-for-first-time-users.md)。
说明
创建集群过程中涉及负载均衡CLB等按量资源的购买，请确保您的账户余额充足，避免因为欠费导致停机。
## 创建集群
ACK支持通过控制台、API、SDK、Terraform以及CLI方式创建集群。
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
| 配置项 | 描述 |
| --- | --- |
| IPv6 双栈 | 仅支持 1.22 及以上版本，仅支持 Terway，不支持与 [eRDMA](use-erdma-in-ack-clusters.md) [功能](use-erdma-in-ack-clusters.md) 同时使用 集群同时支持 IPv4 和 IPv6 协议，但 Worker 节点与控制面间的通信仍使用 IPv4 地址。需确保： 集群 VPC 支持 IPv6 双栈。 使用 Terway 共享 ENI 模式时，节点的 [实例规格](../../../../ecs/documents/user-guide/overview-of-instance-families.md) 需支持 IPv6 且支持的 IPv4/IPv6 地址数量相同。 |
| 专有网络 | 集群的专有网络 VPC。为保障高可用，建议选择 2 个及以上不同可用区。 自动创建：ACK 在已选择的可用区下创建对应 vSwitch。 使用已有：选择 vSwitch，指定集群的可用区，可新建或使用已有 vSwitch。 推荐集群 VPC 使用标准私有地址（如 10.0.0.0/8、172.16.0.0/12 和 192.168.0.0/16）。如有特殊需求，请前往 [配额中心](https://quotas.console.aliyun.com/white-list-products/csk/quotas) 申请（ 使用公网网段 VPC 创建集群 ）。 云资源及计费说明： [VPC](../../../../vpc/documents/what-is-vpc.md) |
| 为专有网络配置 SNAT | 使用共享 VPC 时请勿勾选 节点需访问公网（拉取公网镜像或访问外部服务）时勾选此项，ACK 将自动配置 NAT 网关和 SNAT 规则，确保集群内资源可以访问公网。 VPC 中没有 NAT 网关：ACK 自动创建 NAT 网关，新购 EIP，并为集群使用的 vSwitch 配置 SNAT 规则。 VPC 已有 NAT 网关：ACK 判断是否需要额外新购 EIP 以及配置 SNAT 规则。当无可用 EIP 时，将自动新购 EIP；当不存在 VPC 级别的 SNAT 规则时，将为集群使用的 vSwitch 配置 SNAT 规则。 若不勾选，也可在创建集群后自行配置 NAT 网关和 SNAT 规则，请参见 [公网 NAT 网关](../../../../nat-gateway/documents/user-guide/use-internet-nat-gateway-for-public-network-access.md) 。 云资源及计费说明： [NAT](../../../../nat-gateway/documents/nat-gateway-billing.md) [网关](../../../../nat-gateway/documents/nat-gateway-billing.md) 、 [EIP](../../../../eip/documents/billing-overview.md) |
| 交换机 | 在列表中根据可用区选择已有 vSwitch 交换机，或单击 创建虚拟交换机 创建新的 vSwitch。集群控制面与默认节点池将使用此处指定的 vSwitch。推荐选择多个不同可用区的 vSwitch，更好地保障集群高可用。 |
| 安全组 | 使用已有 VPC 时，支持使用 选择已有安全组 此 [安全组](../../../../ecs/documents/user-guide/overview-44.md) 应用于集群控制面、默认节点池和未指定自定义安全组的节点池。 相较于普通安全组，企业级安全组可以容纳更多私网 IP 地址数量，但不支持组内互通功能，详见 [安全组分类](../../../../ecs/documents/user-guide/overview-44.md) 。 自动创建：出方向默认全部允许，入方向基于 [推荐配置](configure-security-group-rules-to-enforce-access-control-on-ack-clusters.md) 放行。后续如需修改，请确保在入方向已放行 100.64.0.0/10 网段。 该网段用于访问阿里云其他服务，以执行镜像拉取、查询 ECS 基础信息等操作。 使用已有：ACK 默认不会为安全组配置额外的访问规则。需自行管理安全组规则，以避免访问异常，请参见 [配置集群安全组](configure-security-group-rules-to-enforce-access-control-on-ack-clusters.md) 。 |
| API server 访问 | ACK 自动新建一个按量付费的私网 CLB 实例作为 API Server 的内网连接端点。该 CLB 实例不可复用且不可删除，删除后 API Server 将无法访问且无法恢复。 若需使用已有 CLB 实例，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 申请。选择 使用已有 的 专有网络 后，可选择 负载均衡来源 为 使用已有 。 可选开启 使用 EIP 暴露 API server 。 开放：为 API Server 私网 CLB 实例绑定 EIP，支持从公网访问 API Server，连接并管理集群。 这并不代表集群内资源可以访问公网。如需让集群内资源访问公网，需勾选 为专有网络配置 SNAT 。 不开放：仅能在 VPC 内使用 KubeConfig 连接并操作集群。 如需后续启用，请参见 [实现从公网访问](control-public-access-to-the-api-server-of-a-cluster.md) [API Server](control-public-access-to-the-api-server-of-a-cluster.md) 。 自 2024 年 12 月 01 日起，新建 CLB 实例 不再支持 包年包月 付费类型，同时 将新增收取实例费，请参见 [【产品公告】关于取消新增集群](../../product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [API Server](../../product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [负载均衡](../../product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [CLB](../../product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [包年包月付费的公告](../../product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) 、 [传统型负载均衡](../../../../slb/documents/product-overview/announcement-on-adjustment-of-traditional-load-balancing-clb-billing-items.md) [CLB](../../../../slb/documents/product-overview/announcement-on-adjustment-of-traditional-load-balancing-clb-billing-items.md) [计费项调整公告](../../../../slb/documents/product-overview/announcement-on-adjustment-of-traditional-load-balancing-clb-billing-items.md) 。 云资源及计费说明： [CLB](../../../../slb/documents/classic-load-balancer/product-overview/billing-overview.md) 、 [EIP](../../../../eip/documents/billing-overview.md) |
| 网络插件 | 网络插件是集群中 Pod 之间网络通信的基础。 关于两者的详细对比，请参见 [容器网络插件](comparison-between-terway-and-flannel.md) [Terway](comparison-between-terway-and-flannel.md) [与](comparison-between-terway-and-flannel.md) [Flannel](comparison-between-terway-and-flannel.md) [对比](comparison-between-terway-and-flannel.md) 。 Flannel ：社区开源的轻量级网络插件，在 ACK 中采用了与阿里云 VPC 深度集成的 VPC 专有网络模式，通过直接管理 VPC 路由表实现 Pod 间通信。 适用场景：配置简单，资源消耗少，适用于节点规模较小（受 VPC 路由表配额限制）、需要简化网络配置、无需对容器网络进行自定义控制的场景。 Terway ：阿里云自研的高性能网络插件，基于弹性网卡 ENI 实现 Pod 间通信。 适用场景：提供基于 eBPF 的网络加速、NetworkPolicy 和 Pod 级别的 vSwitch 及安全组等能力，适用于对节点规模、网络性能和安全等有较高需求的高性能计算、游戏、微服务等场景。 Pod 数量限制：每个 Pod 占用 ENI 的一个辅助 IP 地址，单个 ENI 可分配的 IP 有限（取决于 [实例规格](../../../../ecs/documents/user-guide/overview-of-instance-families.md) ）。因此，节点上可运行的 Pod 数会受到节点的 ENI 和辅助 IP 的配额限制。 使用共享 VPC 时，仅支持 Terway。 Terway 还提供以下能力。 详细能力介绍请参见 [使用](work-with-terway.md) [Terway](work-with-terway.md) [网络插件](work-with-terway.md) 。 DataPath V2 仅支持在创建集群时配置 开启 DataPath V2 加速模式，Terway 将使用 eBPF 技术优化流量转发路径，为网络密集型应用提供更低的延迟和更高的吞吐量。 仅支持 Alibaba Cloud Linux 3（所有版本）、ContainerOS、Ubuntu，且 Linux 内核版本需为 5.10 及以上。详细介绍请参见 [网络加速](work-with-terway.md) 。 NetworkPolicy 支持 公测中，请在 [配额平台](https://quotas.console.aliyun.com/white-list-products/csk/quotas) 申请 支持 Kubernetes 原生的 NetworkPolicy ，以实现 Pod 间的“防火墙”，自定义精细的访问控制规则，以提升集群安全性。 Trunk ENI 支持 允许为 Pod 配置独立的 IP、vSwitch 和安全组，适用于需要固定 IP 或需要对特定 Pod 进行独立网络策略管理的特殊业务场景，请参见 [为](configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md) [Pod](configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md) [配置固定](configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md) [IP](configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md) [及独立虚拟交换机、安全组](configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md) 。 |
| 容器网段 | 仅 Flannel 需要配置 为 Pod 分配 IP 地址的地址池。此网段不能与 VPC 及 VPC 内已有 ACK 集群使用的网段重叠，且不能与 服务网段 重叠。 |
| 节点 Pod 数量 | 仅 Flannel 需要配置 定义单个节点上可容纳的最大 Pod 数量。 |
| Pod 交换机 | 仅在选择使用 Terway 时需要配置。 为 Pod 分配 IP 的虚拟交换机。每个 Pod 虚拟交换机分别对应一个 Worker 节点的虚拟交换机，Pod 虚拟交换机和 Worker 节点的虚拟交换机的可用区需保持一致。 重要 Pod 虚拟交换机的网段掩码建议不超过 19，最大不超过 25，否则集群网络可分配的 Pod IP 地址非常有限，会影响集群的正常使用。 |
| 服务网段 | 即 Service CIDR，为集群内部 Service 分配 IP 地址的地址池。此网段不能与 VPC 及 VPC 内已有集群使用的网段重复，且不能与 容器网段 重复。 |
| IPv6 服务网段 | 需同时开启 IPv6 双栈 为 Service 网段配置 IPv6 地址段。需使用 ULA 地址（ fc00::/7 范围内），地址前缀长度在/112~/120 之间。推荐与 服务网段 的可用地址数量保持一致。 |
集群高级配置
展开高级选项（选填），配置集群服务转发模式。
| 配置项 | 描述 |
| --- | --- |
| 服务转发模式 | 选择 kube-proxy 代理模式，即集群 Service 如何将请求分发至后端 Pod。 iptables：基于 Linux 防火墙规则实现流量转发，使用稳定但性能有限。Service 数量增加时，防火墙规则也会成倍增长，导致请求处理变慢，适用于存在少量 Service 的集群。 IPVS：高性能的流量分发方案，采用哈希表方式快速定位目标 Pod，处理大量 Service 请求时延时更低。适用于大规模生产集群或对网络性能要求较高的场景。 |
展开高级选项（选填），配置集群删除保护、资源组等信息。
展开查看高级选项
| 配置项 | 描述 |
| --- | --- |
| 集群删除保护 | 推荐开启，防止通过控制台或 OpenAPI 误删除集群。 |
| 资源组 | 将集群归属于选择的 [资源组](../../../../ecs/documents/user-guide/resource-groups.md) ，便于权限管理和成本分摊。 一个资源只能归属于一个资源组。 |
| 标签 | 为集群绑定键值对 [标签](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview) ，作为云资源的标识。 |
| 时区 | 集群使用的 [时区](../../product-overview/supported-time-zones.md) 。默认为浏览器配置的时区。 |
| 集群本地域名 | 集群内 Service 使用的顶级域名（标准后缀）。默认为 cluster.local ，也支持自定义域名。自定义本地域名时，请参见 [配置集群本地域名（ClusterDomain）有哪些注意事项？](faq-about-container-networks.md) 。 例如，名为 my-service 的 Service 位于 default 命名空间中，其 DNS 域名为 my-service.default.svc.cluster.local 。 |
| 自定义证书 SAN | API Server 证书中 SAN（Subject Alternative Name）字段默认包括集群本地域名、内网 IP、公网 EIP 等字段。如需通过代理服务器、自定义域名或特殊网络环境访问集群，需将这些访问地址添加到 SAN 字段中。 如需后续启用，请参见 [自定义集群](../security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md) [API Server](../security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md) [证书](../security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md) [SAN](../security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md) 。 |
| 服务账户令牌卷投影 | 传统模式下 Pod 的身份凭证永久有效且多个 Pod 共享，存在安全风险。启用后，每个 Pod 将获得专属的临时身份凭证，且支持配置自动过期和权限限制。 如需后续启用，请参见 [使用](../security-and-compliance/enable-service-account-token-volume-projection.md) [ServiceAccount Token](../security-and-compliance/enable-service-account-token-volume-projection.md) [卷投影](../security-and-compliance/enable-service-account-token-volume-projection.md) 。 |
| 节点服务端口范围 | 创建 NodePort 类型的 Service 时，可用的端口范围。 |
| 集群 CA | 启用后，可以将 CA 证书添加到集群中，加强服务端和客户端之间信息交互的安全性。 |
步骤三：配置Master节点
单击下一步：Master 配置，完成Master节点配置。
| 配置项 | 描述 |
| --- | --- |
| Master 实例数量 | 指定可用区内部署 Master 节点的数量。 |
| 付费类型 | 支持 按量付费 和 包年包月 两种付费类型。选择 包年包月 时，需设置 购买时长 和是否启用 自动续费 。 |
| 实例规格 | 选择 Master 节点的 [实例规格族](../../../../ecs/documents/user-guide/overview-of-instance-families.md) 。您可以参见 [选择](select-ecs-instances-to-create-the-master-and-worker-nodes-of-an-ack-cluster.md) [Master](select-ecs-instances-to-create-the-master-and-worker-nodes-of-an-ack-cluster.md) [节点规格](select-ecs-instances-to-create-the-master-and-worker-nodes-of-an-ack-cluster.md) 获取配置建议。 |
| 系统盘 | 根据业务需求选择 [云盘](../../../../ecs/documents/user-guide/elastic-block-storage-devices.md) 类型，包括 ESSD AutoPL、ESSD 云盘、ESSD Entry 以及上一代云盘（SSD 云盘和高效云盘），配置容量和 IOPS 等。 可用系统盘类型取决于所选的 [实例规格族](../../../../ecs/documents/user-guide/overview-of-instance-families.md) 。未展示的云盘类型即为不支持使用。 ESSD 云盘自定义性能和加密能力 支持自定义性能级别。云盘容量越大，可选择的性能级别越高（460 GiB 容量以上可选 PL2，1260 GiB 以上可选 PL3），详情请参见 [容量范围与性能级别的关系](../../../../ecs/documents/user-guide/essds.md) 。 系统盘中仅 ESSD 云盘支持 加密 。选择密钥时，阿里云默认使用服务密钥（Default Service CMK）进行加密；您也可以选择在 KMS 服务中预先创建的自定义密钥（BYOK）进行加密。 支持选择 配置更多系统盘类型 ，配置与 系统盘 不同的磁盘类型，提高扩容成功率。创建节点时，ACK 将根据指定的磁盘类型顺序，选择第一个匹配的类型。 云资源及计费说明： [ECS](../../../../ecs/documents/block-storage-devices.md) [块存储](../../../../ecs/documents/block-storage-devices.md) |
| 部署集 | 通过 ECS 控制台 [创建部署集](../../../../ecs/documents/user-guide/overview-43.md) 后，为节点池指定部署集，使得节点池弹出的节点可分散部署在不同的物理服务器上，提升高可用性。 部署集默认支持的节点上限为 20 * 可用区数量 （可用区数量由 vSwitch 决定），节点池内最大节点数将受到限制，需确保部署集内配额充足。 后续如需启用，请参见 [节点池部署集最佳实践](best-practices-for-associating-deployment-sets-with-node-pools.md) 。 |
高级选项
| 配置项 | 描述 |
| --- | --- |
| 实例元数据访问模式 | 仅支持 1.28 及以上版本的集群 配置 ECS 实例的元数据访问模式，在 ECS 实例内部通过访问元数据服务（Metadata Service）获取 ECS 实例元数据，包括实例 ID、VPC 信息、网卡信息等实例属性信息，详情请参见 [实例元数据](../../../../ecs/documents/user-guide/view-instance-metadata.md) 。 普通模式和加固模式 ：支持使用普通模式和加固模式两种方式访问实例元数据服务。 仅加固模式 ：仅支持使用加固模式访问实例元数据服务，请参见 [使用仅加固模式访问](../security-and-compliance/secure-access-to-ecs-instance-metadata.md) [ECS](../security-and-compliance/secure-access-to-ecs-instance-metadata.md) [实例元数据](../security-and-compliance/secure-access-to-ecs-instance-metadata.md) 。 |
步骤四：配置节点池
单击下一步：节点池配置，完成节点池基础选项配置和高级选项配置。
节点池基础配置
| 配置项 | 描述 |
| --- | --- |
| 节点池名称 | 自定义节点池名称。 |
| 容器运行时 | 如何选型，请参见 [containerd、安全沙箱、Docker](comparison-of-docker-containerd-and-sandboxed-container.md) [运行时的对比](comparison-of-docker-containerd-and-sandboxed-container.md) 。 containerd（推荐）：社区标准，支持 1.20 及以上版本。 安全沙箱： 提供基于轻量级虚拟化技术的强隔离环境 。使用流程及限制，详见 [创建和管理安全沙箱节点池](node-pool-management-in-sandboxed-containers.md) 。 Docker（停止支持）：仅支持 1.22 及以下版本，目前已不支持创建。 |
实例和镜像配置
| 配置项 | 描述 |
| --- | --- |
| 付费类型 | 节点池扩容节点时默认采用的付费类型。 按量付费 ：可按需启用和释放。 包年包月 ：需配置 购买时长 以及 自动续费 。 抢占式实例 ：目前仅支持具有保护期的 [抢占式实例](../../../../ecs/documents/user-guide/what-is-a-spot-instance.md) 。需同时配置 单台实例上限价格 。 当指定实例规格的实时价格低于单台实例的最高出价时，实例将成功创建。保护期（1 小时）过后，系统将每 5 分钟检查一次实例规格的实时价格与库存。若市场价格高于出价或库存不足，抢占式实例将被释放。使用建议， 请参见 [抢占式实例节点池最佳实践](best-practices-for-preemptible-instance-based-node-pools.md) 。 为保证节点池统一，不支持将 按量付费 、 包年包月 节点池修改为 抢占式实例 节点池，反之亦然。 |
| 实例相关的配置项 | 节点池扩容时，会从配置的 [ECS](../../../../ecs/documents/user-guide/overview-of-instance-families.md) [实例规格族](../../../../ecs/documents/user-guide/overview-of-instance-families.md) 中分配。为提高扩容成功率，请 选择多个可用区下的多种实例规格，避免规格不可用或库存不足 。具体扩容的实例规格由配置的 扩缩容策略 决定。 为确保业务稳定性和资源调度的准确性，请勿在同一个节点池中混合使用 GPU 和非 GPU 实例规格。 可通过以下两种方式配置扩容时使用的实例规格： 具体规格：基于 vCPU、内存、规格族、CPU 架构（实例的 CPU 架构需与 [操作系统镜像架构](overview-of-os-images.md) 一致）等维度指定实例规格。 使用 Terway 时，可在实例规格列表中查看目标实例规格提供的 [节点最大](adjusting-the-number-of-node-pods.md) [Pod](adjusting-the-number-of-node-pods.md) [数](adjusting-the-number-of-node-pods.md) 。 [泛化配置](configure-a-node-pool-using-the-specified-instance-attributes.md) ：根据属性（vCPU、内存等）选择 待使用或需排除的实例规格列表 ，进一步提升扩容成功率。 可参考控制台的弹性强度建议来配置，或在 节点池创建后 [查看节点池弹性强度](check-the-scalability-of-a-node-pool.md) 。 关于 ACK 不支持的实例规格及节点配置建议，请参见 [ECS](select-ecs-instances-to-create-the-master-and-worker-nodes-of-an-ack-cluster.md) [实例规格配置建议](select-ecs-instances-to-create-the-master-and-worker-nodes-of-an-ack-cluster.md) 。 云资源及计费说明： [ECS](../../../../ecs/documents/instance-types.md) [实例](../../../../ecs/documents/instance-types.md) 、 [GPU](https://help.aliyun.com/zh/egs/billing-2) [实例](https://help.aliyun.com/zh/egs/billing-2) |
| 操作系统 | 云市场镜像 处于灰度发布中。 公共镜像 ： 容器服务 Kubernetes 版 提供的 [Alibaba Cloud Linux 3](https://help.aliyun.com/zh/alinux/alibaba-cloud-linux-3-container-optimized-images) [容器优化版](https://help.aliyun.com/zh/alinux/alibaba-cloud-linux-3-container-optimized-images) 、 [Alibaba Cloud Linux 3](use-alibaba-cloud-linux-3.md) 、Red Hat。详情请参见 [操作系统](overview-of-os-images.md) 。 自定义镜像 ：使用基于 Alibaba Cloud Linux 3 或 Red Hat 制作的自定义操作系统镜像，详情请参见 [如何基于创建好的](create-a-node-pool.md) [ECS](create-a-node-pool.md) [实例创建自定义镜像，并使用该镜像创建节点？](create-a-node-pool.md) 。 后续如需升级或更换操作系统，请参见 [更换操作系统](replace-the-operating-system.md) 。 |
| 安全加固 | 创建节点时，ACK 会应用选择的安全基线策略。 不开启 ：不对 ECS 实例进行安全加固。 等保加固 ：阿里云为 Alibaba Cloud Linux 等保 2.0 三级版镜像提供了符合等保合规要求的基线检查标准和扫描工具。在确保原生镜像兼容性和性能的同时，进行了等保合规适配，满足《GB/T22239-2019 信息安全技术网络安全等级保护基本要求》，详情请参见 [ACK](../security-and-compliance/ack-reinforcement-based-on-classified-protection.md) [等保加固使用说明](../security-and-compliance/ack-reinforcement-based-on-classified-protection.md) 。 但在此模式下，Root 用户无法通过 SSH 远程登录。您可以通过 ECS 控制台 [通过](../../../../ecs/documents/user-guide/log-on-to-an-instance-by-using-vnc.md) [VNC](../../../../ecs/documents/user-guide/log-on-to-an-instance-by-using-vnc.md) [连接实例](../../../../ecs/documents/user-guide/log-on-to-an-instance-by-using-vnc.md) ，并创建一个支持 SSH 登录的普通用户。 阿里云 OS 加固 ：仅支持 Alibaba Cloud Linux 2 或 Alibaba Cloud Linux 3。 |
| 登录方式 | 设置密钥 ：阿里云 [SSH](../../../../ecs/documents/user-guide/ssh-key-pairs.md) [密钥对](../../../../ecs/documents/user-guide/ssh-key-pairs.md) 是一种安全便捷的登录认证方式，由公钥和私钥组成，仅支持 Linux 实例。 请同时配置 登录名 （ root 或 ecs-user ）和所需的 密钥对 。 设置密码 ：配置 登录名 （ root 或 ecs-user ）和密码。 |
存储配置
| 配置项 | 描述 |
| --- | --- |
| 系统盘 | 根据业务需求选择 [云盘](../../../../ecs/documents/user-guide/elastic-block-storage-devices.md) 类型，包括 ESSD AutoPL、ESSD 云盘、ESSD Entry 以及上一代云盘（SSD 云盘和高效云盘），配置容量和 IOPS 等。 可用系统盘类型取决于所选的 [实例规格族](../../../../ecs/documents/user-guide/overview-of-instance-families.md) 。未展示的云盘类型即为不支持使用。 ESSD 云盘自定义性能和加密能力 支持自定义性能级别。云盘容量越大，可选择的性能级别越高（460 GiB 容量以上可选 PL2，1260 GiB 以上可选 PL3），详情请参见 [容量范围与性能级别的关系](../../../../ecs/documents/user-guide/essds.md) 。 系统盘中仅 ESSD 云盘支持 加密 。选择密钥时，阿里云默认使用服务密钥（Default Service CMK）进行加密；您也可以选择在 KMS 服务中预先创建的自定义密钥（BYOK）进行加密。 支持选择 配置更多系统盘类型 ，配置与 系统盘 不同的磁盘类型，提高扩容成功率。创建节点时，ACK 将根据指定的磁盘类型顺序，选择第一个匹配的类型。 云资源及计费说明： [ECS](../../../../ecs/documents/block-storage-devices.md) [块存储](../../../../ecs/documents/block-storage-devices.md) |
| 数据盘 | 根据业务需求选择 [云盘](../../../../ecs/documents/user-guide/elastic-block-storage-devices.md) 类型，包括 ESSD AutoPL、ESSD 云盘、ESSD Entry 以及上一代云盘（SSD 云盘和高效云盘），配置容量和 IOPS 等。 可用数据盘类型取决于所选的 [实例规格族](../../../../ecs/documents/user-guide/overview-of-instance-families.md) 。未展示的云盘类型即为不支持使用。 ESSD AutoPL 支持 预配置性能：在存储容量大小不变的情况下，可根据实际业务需求灵活配置云盘的预配置性能，从而实现云盘容量与性能的解耦。 性能突发：当业务面临突发的数据读写压力时，云盘会临时提升性能 以应对峰值需求 ，直至业务恢复平稳。 ESSD 云盘支持 支持自定义性能级别。云盘容量越大，可选择的性能级别越高（460 GiB 容量以上可选 PL2，1260 GiB 以上可选 PL3），详情请参见 [容量范围与性能级别的关系](../../../../ecs/documents/user-guide/essds.md) 。 挂载数据盘时，所有云盘类型均支持 加密 。选择密钥时，阿里云默认使用服务密钥（Default Service CMK）进行加密；您也可以选择在 KMS 服务中预先创建的自定义密钥（BYOK）进行加密。 节点创建过程中，将自动格式化最后一块数据盘，并将 /var/lib/container 挂载到该数据盘，将 /var/lib/kubelet 、 /var/lib/containerd 挂载到 /var/lib/container 。 如需自定义挂载目录，请调整数据盘的初始化配置，最多可选择一块数据盘作为容器运行时占用目录，详情请参见 [ACK](faq-about-node-management.md) [节点池中数据盘可以自定义目录挂载吗？](faq-about-node-management.md) 在需要容器镜像加速、大模型快速加载等场景下，还可以使用快照创建数据盘，提升系统的响应速度和处理能力。 可选择 配置更多数据盘类型 ，配置与 数据盘 不同的磁盘类型，提高扩容成功率。创建节点时，ACK 将根据指定的磁盘类型顺序，选择第一个匹配的类型。 一台 ECS 实例最多可挂载 64 块数据盘，具体可挂载数量上限因实例规格而异。可调用 [DescribeInstanceTypes](../../../../ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstancetypes.md) 查询对应实例规格的云盘数量上限（ DiskQuantity ）。 云资源及计费说明： [ECS](../../../../ecs/documents/block-storage-devices.md) [块存储](../../../../ecs/documents/block-storage-devices.md) |
| 弹性临时盘 | 白名单功能， [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 申请 [弹性临时盘](../../../../ecs/documents/user-guide/elastic-ephemeral-disks.md) 为 ECS 实例提供高性能、高性价比的临时数据存储空间，适用于存放临时数据（如临时计算中间结果、缓存数据、临时文件等）、高性能计算（对 IOPS 和吞吐量要求较高）等场景。 仅支持在部分地域和部分 ECS 实例规格中使用，请参见 [地域限制](../../../../ecs/documents/user-guide/elastic-ephemeral-disks.md) 、 [实例规格限制](../../../../ecs/documents/user-guide/elastic-ephemeral-disks.md) 。 您可以选择是否对弹性临时盘进行 [初始化](../../../../ecs/documents/user-guide/overview-27.md) 设置，自定义其挂载目录。 云资源及计费说明： [ECS](../../../../ecs/documents/block-storage-devices.md) [块存储](../../../../ecs/documents/block-storage-devices.md) |
实例数量配置
| 配置项 | 描述 |
| --- | --- |
| 期望节点数 | 节点池应该维持的总节点数量。建议至少配置 2 个节点，以确保集群组件正常运行。您可以通过调整期望节点数，达到扩容或缩容节点池的目的，请参见 [扩缩容节点池](../developer-reference/scale-a-node-pool-1.md) 。 如无需创建节点，可填写为 0，后续再手动调整或 [添加已有节点](add-existing-ecs-instances-to-an-ack-cluster.md) 。 |
节点池高级配置
展开高级选项（选填），配置节点扩缩容策略。
| 配置项 | 描述 |
| --- | --- |
| 扩缩容策略 | 配置节点池在节点扩缩容时如何选择实例。 优先级策略 ：按集群配置的 vSwitch 优先级（vSwitch 顺序由上到下优先级递减）扩缩容。优先级较高的 vSwitch 所在可用区无法创建实例时，自动使用下一优先级 vSwitch。 成本优化策略 ：按 vCPU 单价从低到高扩缩容。 节点池使用 抢占式实例 时，则抢占式实例优先。支持同时配置 按量实例所占比例（% ），当抢占式实例规格因库存等原因无法创建时，自动使用按量付费实例来补充。 均衡分布策略 ：在且仅在多可用区场景下将 ECS 实例均匀分配至多可用区。如果由于库存不足等原因造成可用区分布不平衡，可再次进行均衡操作。 |
| 使用按量实例补充抢占式容量 | 需同时选择付费类型为抢占式实例。 开启后，如果因价格或库存等原因无法创建足够的抢占式实例，ACK 将自动尝试创建按量实例作为补充。 云资源及计费说明： [ECS](../../../../ecs/documents/instance-types.md) [实例](../../../../ecs/documents/instance-types.md) |
| 开启抢占式实例补偿 | 需同时选择付费类型为抢占式实例。 开启后，当收到抢占式实例将被回收的系统消息时（即抢占式实例被回收前 5 分钟），ACK 将尝试扩容新实例进行补偿。 补偿成功：ACK 对旧节点执行排水并从集群中移除。 补偿失败：ACK 不会对旧节点执行排水，到期实例仍然会在 5 分钟后被回收释放。当库存恢复或满足价格条件时，ACK 将自动购买实例以保证期望节点数，详情请参见 [抢占式实例节点池最佳实践](best-practices-for-preemptible-instance-based-node-pools.md) 。 抢占式实例的主动释放可能导致业务异常，为提高补偿成功率，建议同时开启 使用按量实例补充抢占式容量 。 云资源及计费说明： [ECS](../../../../ecs/documents/instance-types.md) [实例](../../../../ecs/documents/instance-types.md) |
展开高级选项（选填），配置ECS标签、污点等信息。
| 置项 | 描述 |
| --- | --- |
| ECS 标签 | 为 ACK 自动创建的 ECS 实例添加标签，作为云资源标识。每台 ECS 最多可绑定 20 个标签。如需提高上限，请到 [配额平台](https://quotas.console.aliyun.com/products/tag/quotas) 提交申请。由于 ACK 和 ESS 会占用部分标签，您最多可为实例指定 17 个自定义标签。 展开查看标签占用说明 ACK 默认占用两个 ECS 标签。 ack.aliyun.com:<您的集群 ID> ack.alibabacloud.com/nodepool-id:<您的节点池 ID> ESS 默认占用 1 个 ECS 标签： acs:autoscaling:scalingGroupId:<您的节点池伸缩组 ID> 。 开启 [节点自动伸缩](auto-scaling-of-nodes.md) 后， 弹性伸缩将默认占用两个 ECS 标签，因此 节点池会额外占用两个 ECS 标签： k8s.io/cluster-autoscaler:true 和 k8s.aliyun.com:true 。 开启 [节点自动伸缩](auto-scaling-of-nodes.md) 后，组件通过 ECS 标签记录节点的标签和污点，以预检测弹出节点的调度行为。 节点的每个标签会被转为 k8s.io/cluster-autoscaler/node-template/label/<标签键>：<标签值> 。 节点的每个污点会被转为 k8s.io/cluster-autoscaler/node-template/taint/<污点键>/<污点值>：<污点效果> 。 |
| 污点 （Taints） | 为节点添加键值对 [污点](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration?spm=a2c4g.11186623.0.0.76f068derYLXgN) 。有效污点键包含前缀（可选）和名称。如果有前缀，用正斜线（/）分隔。 展开查看详细说明 键 ：名称长度为 1~63 个字符，必须以字母、数字或字符 [a-z0-9A-Z] 开头和结尾，中间可包含字母、数字、短划线（-）、下划线（_）、英文半角句号（.）。 如果指定前缀，必须为 [DNS](https://kubernetes.io/zh-cn/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) [子域](https://kubernetes.io/zh-cn/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) ，即一系列由英文半角句号（.）分隔的 DNS 标签，不超过 253 个字符，并以正斜线（/）结尾。 值 ：污点值可以为空，不超过 63 个字符，必须以字母、数字或字符 [a-z0-9A-Z] 开头和结尾，可包含字母、数字、短划线（-）、下划线（_）、英文半角句号（.）。 Effect ： NoSchedule ：不接受任何新的、不容忍此污点的 Pod 被调度到该节点，但已在运行的 Pod 不受影响。 NoExecute ：不仅不接受任何新的、不容忍此污点的 Pod 被调度到该节点，还会驱逐节点上任何已在运行的、不容忍此污点的 Pod。 PreferNoSchedule ：ACK 会尽量避免将 Pod 调度到存在其不能容忍污点的节点上，但不会强制执行。 |
| 节点标签（Labels） | 为节点添加键值对标签。有效 Key 包含前缀（可选）和名称。如有前缀，前缀和名称之间用正斜线（/）分隔。 展开查看详细说明 Key：名称长度为 1~63 个字符，必须以字母数字字符 [a-z0-9A-Z] 开头和结尾，中间可包含字母、数字、短划线（-）、下划线（_）、英文半角句号（.）。 如果指定前缀，必须为 [DNS](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) [子域](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) ，即一系列由英文半角句号（.）分隔的 DNS 标签，不超过 253 个字符，以正斜线（/）结尾。 以下前缀由 Kubernetes 核心组件保留，不支持指定 kubernetes.io/ k8s.io/ 以 kubernetes.io/ 和 k8s.io/ 结尾的前缀。例如 test.kubernetes.io/ 。 以下除外： kubelet.kubernetes.io/ node.kubernetes.io 以 kubelet.kubernetes.io/ 结尾的前缀。 以 node.kubernetes.io 结尾的前缀。 Value：可以为空，不超过 63 个字符，必须以字母数字字符 [a-z0-9A-Z] 开头和结尾，可包含字母、数字、短划线（-）、下划线（_）和英文半角句号（.）。 |
| 设置为不可调度 | 新添加的节点注册到集群时默认会被设置为不可调度。需在节点列表手动调整 [节点调度状态](overview-of-node-management.md) 。 本配置仅对 1.34 以下版本集群生效，详情请参见 [Kubernetes 1.34](kubernetes-1-34-release-notes.md) [版本说明](kubernetes-1-34-release-notes.md) 。 |
| CPU Policy | 指定 kubelet 节点的 [CPU](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/?spm=5176.2020520152.0.0.49fd16ddxL871D) [管理策略](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/?spm=5176.2020520152.0.0.49fd16ddxL871D) 。 [None](https://kubernetes.io/zh-cn/docs/tasks/administer-cluster/cpu-management-policies/?spm=5176.2020520152.0.0.49fd16ddxL871D#none-policy) ：默认策略。 [Static](https://kubernetes.io/zh-cn/docs/tasks/administer-cluster/cpu-management-policies/?spm=5176.2020520152.0.0.49fd16ddxL871D#static-policy) ：允许为节点上具有某些资源特征的 Pod 赋予增强的 CPU 亲和性和独占性。 推荐使用 [自定义节点池](customize-the-kubelet-configurations-of-a-node-pool.md) [kubelet](customize-the-kubelet-configurations-of-a-node-pool.md) [配置](customize-the-kubelet-configurations-of-a-node-pool.md) 。 |
| 自定义节点名称 | 默认情况下，节点名称自动生成。如需统一命名规则以便于节点管理和运维识别，可启用此配置。启用后，节点名称、ECS 实例名称及 Hostname 均会发生变化。 方式三仅适用于灵骏节点池，灵骏节点池也仅支持使用方式三 方式一：完整 IP 地址 + 前后缀 说明：节点名称由前缀、节点 IP 地址及后缀三部分组成。启用后，节点名称、ECS 实例名称、ECS 实例 Hostname 也将发生变化。 示例：节点 IP 地址为 192.XX.YY.55 ，指定前缀为 aliyun.com ，后缀为 test 。 Linux 节点：节点名称、ECS 实例名称、ECS 实例 Hostname 均为 aliyun.com192.XX.YY.55test 。 Windows 节点：其 Hostname 固定为 IP 地址，使用 - 代替 IP 地址中的 . ，且不包含前缀和后缀。 因此，ECS 实例 Hostname 为 192-XX-YY-55 ，节点名称、ECS 实例名称均为 aliyun.com192.XX.YY.55test 。 方式二：指定位数 IP 地址 + 前后缀 白名单功能 说明：节点名称由前缀、指定位数的节点 IP 地址、后缀三部分组成。启用后，节点名称、ECS 实例名称及 ECS 实例 Hostname 均会相应变化。 示例： 节点 IP 地址为 192.XX.YY.55 ，前缀为 aliyun.com ，后缀为 test ，IP 地址截取位数为 6 ，则节点名称为 aliyun.com0YY055test 。 重要 当自定义节点名称格式依赖于截取部分 IP 地址时，若 VPC 网段范围较大而截取的 IP 位数（ lenOfIP ）不足，可能会导致节点名称冲突，从而造成 [节点即时弹性](instant-elasticity.md) 场景下节点扩容失败。 请根据 VPC 网段，参见以下建议设置 IP 地址的截取位数： 针对 10.0.0.0/8 和 172.16.0.0/12 等大规模网段，建议 lenOfIP 至少为 9。 针对 192.168.0.0/16 网段，建议 lenOfIP 至少为 6。 方式三：同步实例 Hostname（仅灵骏节点池支持） 白名单功能，不适用于非灵骏节点池 说明：将灵骏节点的 Hostname 直接同步为节点的 NodeName。 示例： 实例 Hostname 为 test ，则节点 NodeName 为 test 。 方式四：递增 ID + 前后缀（仅 ECS 节点池支持） 白名单功能 启用此方式后不支持同时开启 [节点伸缩](overview-of-node-scaling.md) （即 扩缩容模式 为 自动 ）；已开启自动伸缩的节点池不支持切换为此方式。 说明：节点名称由前缀、递增 ID 及后缀三部分组成，格式为 auto_increment,name_prefix(AUTO_INCREMENT)[begin_number,bits]name_suffix （ [begin_number,bits] 之间不存在空格）。参数说明如下，规则详见 [固定增长排序](https://help.aliyun.com/zh/auto-scaling/user-guide/configure-naming-rules-for-ecs-instances#section-176-bta-c6q) 。 beginNumber ：起始编号，取值范围 [0, 999999] 。首次扩容时，指定的起始值生效；未设置时，默认为 0 。非首次扩容时，起始值在伸缩组内已有编号最大值的基础上递增。 bits ：编号位数，取值范围 [1, 6] 。当 beginNumber 的位数超过 bits 的取值时， bits 默认为 6；未设置 beginNumber 或 bits 时，两者分别默认为 0 和 6 。建议 bits 至少设置为 3 ，否则容易达到编号上限。达到上限后如仍有扩容需求，扩容将报错并停止，此时需重新设置命名规则。 系统默认依次递增，但若扩容的 ECS 实例无法启动，该实例会在移除后重新扩容，因此编号可能断续递增。 示例： 命名格式为 auto_increment,start(AUTO_INCREMENT)[1,3]end ， beginNumber 为 1 ， bits 为 3 ，则节点名称按顺序生成： 第 1 个实例： start001end 第 2 个实例： start002end …… |
| 实例元数据访问模式 | 仅支持 1.28 及以上版本的集群 配置 ECS 实例的元数据访问模式，在 ECS 实例内部通过访问元数据服务（Metadata Service）获取 ECS 实例元数据，包括实例 ID、VPC 信息、网卡信息等实例属性信息，详情请参见 [实例元数据](../../../../ecs/documents/user-guide/view-instance-metadata.md) 。 普通模式和加固模式 ：支持使用普通模式和加固模式两种方式访问实例元数据服务。 仅加固模式 ：仅支持使用加固模式访问实例元数据服务，请参见 [使用仅加固模式访问](../security-and-compliance/secure-access-to-ecs-instance-metadata.md) [ECS](../security-and-compliance/secure-access-to-ecs-instance-metadata.md) [实例元数据](../security-and-compliance/secure-access-to-ecs-instance-metadata.md) 。 |
| 实例预自定义数据 | 节点加入集群前，将运行指定的实例预自定义 [User-Data](../../../../ecs/documents/user-guide/manage-the-user-data-of-linux-instances.md) [脚本](../../../../ecs/documents/user-guide/manage-the-user-data-of-linux-instances.md) 。 例如，指定预自定义数据为 touch /tmp/pre-script ，则节点上组合后的脚本执行顺序如下。 #!/bin/bash # 输入的实例预自定义数据在此处执行 touch /tmp/pre-script # ACK 节点初始化脚本在此处执行 节点初始化时此配置的生效逻辑，请参见 [节点初始化流程介绍](introduction-to-node-initialization.md) 。 |
| 实例自定义数据 | 节点加入集群后，将运行指定的实例自定义 [User-Data](../../../../ecs/documents/user-guide/manage-the-user-data-of-linux-instances.md) [脚本](../../../../ecs/documents/user-guide/manage-the-user-data-of-linux-instances.md) 。 例如，指定实例自定义数据为 touch /tmp/post-script ，则节点上组合后的脚本执行顺序如下。 #!/bin/bash # ACK 节点初始化脚本在此处执行 # 输入的实例自定义数据在此处执行 touch /tmp/post-script 节点初始化时此配置的生效逻辑，请参见 [节点初始化流程介绍](introduction-to-node-initialization.md) 。 创建集群或扩容节点成功不代表实例自定义脚本执行成功。可登录节点执行 grep cloud-init /var/log/messages 查看执行日志。 |
| 云监控插件 | 可在 [云监控控制台](https://cloudmonitornext.console.aliyun.com/) 查看并 监控节点和应用运行状态。 本配置仅对节点池中新增的节点生效，不对节点池存量节点生效。 已有节点如需启用，请通过 [云监控控制台](https://cloudmonitornext.console.aliyun.com/) 安装。 云资源及计费说明： [云监控](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/billing-overview) |
| 公网 IP | ACK 将为节点分配 IPv4 公网 IP 地址。 本配置仅对节点池中新增的节点生效，不对节点池存量节点生效。已有节点如需访问公网，需配置并绑定 EIP，请参见 [EIP 绑定云资源](../../../../eip/documents/bind-an-eip-to-a-cloud-resource.md) 。 云资源及计费说明： [ECS](../../../../ecs/documents/public-bandwidth.md) [公网](../../../../ecs/documents/public-bandwidth.md) |
| 自定义安全组 | 为节点池指定普通安全组或企业级安全组。ACK 默认不会为安全组配置额外的访问规则。需自行管理安全组规则，避免访问异常，请参见 [配置集群安全组](configure-security-group-rules-to-enforce-access-control-on-ack-clusters.md) 。 每台 ECS 实例支持加入的安全组存在上限，请确保 [安全组配额](../../../../ecs/documents/user-guide/limitations.md) 充足。 |
| RDS 白名单 | 将节点 IP 添加至 RDS 实例的白名单。 |
步骤五：配置组件
单击下一步：组件配置，完成组件配置。
| ALB Ingress | 将流量交由阿里云 [应用型负载均衡](../../../../slb/documents/application-load-balancer/product-overview/what-is-alb.md) [ALB](../../../../slb/documents/application-load-balancer/product-overview/what-is-alb.md) 处理，具备丰富的路由策略，与 WAF 等云产品深度集成，支持弹性伸缩，适用于大规模、高流量生产业务或有企业级可靠性需求的场景。 可新建 ALB 实例，也可使用（仅使用已有 VPC 时）当前 VPC 下未被其他集群关联的 ALB 实例。 如需后续启用，请参见 [创建并使用](create-and-use-alb-ingress-to-expose-services-to-the-public.md) [ALB Ingress](create-and-use-alb-ingress-to-expose-services-to-the-public.md) [对外暴露服务](create-and-use-alb-ingress-to-expose-services-to-the-public.md) 。 云资源及计费说明： [ALB](../../../../slb/documents/application-load-balancer/product-overview/billing-overview.md) [计费概述](../../../../slb/documents/application-load-balancer/product-overview/billing-overview.md) |
| --- | --- |
| Nginx Ingress | 兼容社区版 Nginx Ingress Controller 并进行了优化。 可新建 CLB 实例，也可使用当前 VPC 下未被其他集群关联的 CLB 实例。 如需后续启用，请参见 [创建并使用](create-an-nginx-ingress-1.md) [Nginx Ingress](create-an-nginx-ingress-1.md) [对外暴露服务](create-an-nginx-ingress-1.md) 。 云资源及计费说明： [CLB](../../../../slb/documents/classic-load-balancer/product-overview/billing-overview.md) |
| MSE Ingress | 基于 [MSE](https://help.aliyun.com/zh/mse/product-overview/what-is-cloud-native-gateway) [云原生网关](https://help.aliyun.com/zh/mse/product-overview/what-is-cloud-native-gateway) 实现，提供服务治理、认证鉴权、灰度发布等高级能力，适用于需要对微服务流量进行精细化管控的场景。 可新建 MSE 云原生网关实例，也可使用（仅使用已有 VPC 时）当前 VPC 下未被其他集群关联的实例。 如需后续启用，请参见 [通过](use-mse-ingresses-to-access-applications-in-ack-clusters.md) [MSE Ingress](use-mse-ingresses-to-access-applications-in-ack-clusters.md) [访问容器服务](use-mse-ingresses-to-access-applications-in-ack-clusters.md) 。 云资源及计费说明： [普通实例计费概述](https://help.aliyun.com/zh/mse/product-overview/billing-overview-2#concept-2081040) |
关于三者的详细对比，请参见[Ingress](ingress-management-2.md)[管理](ingress-management-2.md)。
服务发现
安装[NodeLocal DNSCache](configure-nodelocal-dnscache.md)，在节点上缓存DNS解析结果，以提升域名解析性能和稳定性，加速集群内部的服务间调用。
存储插件
基于[CSI](csi-overview-1.md)[存储插件](csi-overview-1.md)实现数据的持久化存储，可使用阿里云云盘、NAS、OSS、CPFS等存储卷资源。
选择默认创建[NAS](https://help.aliyun.com/zh/nas/product-overview/what-is-nas)和CNFS后，ACK会默认创建通用型NAS文件系统并使用[容器网络文件系统](cnfs-overview.md)[CNFS](cnfs-overview.md)进行管理。
如需后续创建CNFS，详见[通过](use-cnfs-to-manage-nas-file-systems.md)[CNFS](use-cnfs-to-manage-nas-file-systems.md)[管理](use-cnfs-to-manage-nas-file-systems.md)[NAS](use-cnfs-to-manage-nas-file-systems.md)[文件系统](use-cnfs-to-manage-nas-file-systems.md)。
云资源及计费说明：[NAS](https://help.aliyun.com/zh/nas/product-overview/overview-1)
容器监控
您可以使用阿里云Prometheus查看集群预先配置的监控大盘和监控性能指标。更多信息，请参见[阿里云](../../serverless-kubernetes/user-guide/enable-prometheus-service.md)[Prometheus](../../serverless-kubernetes/user-guide/enable-prometheus-service.md)[监控](../../serverless-kubernetes/user-guide/enable-prometheus-service.md)。
日志服务
使用已有SLS Project或新建一个SLS Project，用于收集集群应用日志。
同时将启用集群API Server审计功能，收集对Kubernetes API的请求以及请求结果。
如需后续启用，请参见[采集](collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)[ACK](collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)[集群容器日志](collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)、[使用集群](../security-and-compliance/work-with-cluster-auditing.md)[API Server](../security-and-compliance/work-with-cluster-auditing.md)[审计功能](../security-and-compliance/work-with-cluster-auditing.md)。
创建 Ingress Dashboard：在SLS控制台创建Ingress Dashboard，可收集Nginx Ingress访问日志，请参见[Nginx Ingress](analyze-and-monitor-the-access-log-of-nginx-ingress.md)[访问日志分析与监控](analyze-and-monitor-the-access-log-of-nginx-ingress.md)。
安装 node-problem-detector 并创建事件中心：在SLS控制台中添加事件中心，实时收集集群中的所有Kubernetes Event，请参见[创建并使用](../../../../sls/documents/create-and-use-an-event-center.md)[K8s](../../../../sls/documents/create-and-use-an-event-center.md)[事件中心](../../../../sls/documents/create-and-use-an-event-center.md)。
云资源及计费说明：[SLS](../../../../sls/documents/billing-overview.md)
集群巡检
启用智能运维的[集群巡检功能](work-with-the-cluster-inspection-feature.md)，定期扫描集群内配额、资源水位、组件版本等，确保集群配置符合最佳实践，并提前暴露潜在风险。
步骤六：确认配置和计费信息
单击下一步：确认配置。
在确认配置页面，确认集群的配置信息，包括功能配置、资源计费、云产品依赖检查等，并阅读服务协议。
您可以在创建页面下方查看集群涉及的费用总览，也可以查看ACK和各产品的计费文档，请参见[计费概述](../product-overview/ack-pro-cluster-billing.md)、[云产品资源费用](../product-overview/billing-of-cloud-services.md)。
说明
一个包含多节点的集群创建时间约为十分钟。
您还可以在确认配置页面的右上角单击同等代码，生成当前集群配置对应的Terraform或SDK示例参数。
### API
调试入口
[CreateCluster](https://next.api.aliyun.com/api/CS/2015-12-15/CreateCluster)[调试入口](https://next.api.aliyun.com/api/CS/2015-12-15/CreateCluster)
请求示例
创建一个ACK专有集群的请求示例如下，完整的参数说明请参见[创建集群](../developer-reference/api-cs-2015-12-15-createcluster.md)。
POST /clusters <公共请求头> { "cluster_type": "Kubernetes", //指定集群的类型为ACK专有集群。#required "name": "ACK专有集群", "region_id": "cn-hongkong", //集群所属地域为香港地域。#required "kubernetes_version": "1.32.1-aliyun.1", //创建的集群版本，建议选择最新版本。 "snat_entry": true, // 为专有网络配置SNAT规则，以开启集群公网访问。 "endpoint_public_access": false, //集群不开启API server公网访问。 "cloud_monitor_flags": false, //集群不安装云监控组件。 "deletion_protection": false, //未开启集群删除保护。 "proxy_mode": "ipvs", //选择高性能的kube-proxy代理模式IPVS。 "timezone": "Asia/Shanghai", "tags": [], "addons": [ //安装的集群组件。 { "name": "terway-eniip", //集群的网络类型为Terway方式。集群创建后不可修改。 "config": "{\"IPVlan\":\"false\",\"NetworkPolicy\":\"false\",\"ENITrunking\":\"false\"}" }, { "name": "csi-plugin" }, { "name": "csi-provisioner" }, { "name": "storage-operator", "config": "{\"CnfsOssEnable\":\"false\",\"CnfsNasEnable\":\"false\"}" }, { "name": "nginx-ingress-controller", "disabled": true } ], "node_port_range": "30000-32767", "pod_vswitch_ids": [ //Terway网络类型的集群，需要指定Pod所在的虚拟交换，因为Pod独占一个机器IP。 "vsw-j6cwz95vspl56gl******", "vsw-j6c1tgut51ude2v******" ], "login_password": "******", "charge_type": "PostPaid", "master_instance_charge_type": "PostPaid", "cpu_policy": "none", "service_account_issuer": "https://kubernetes.default.svc", "api_audiences": "https://kubernetes.default.svc", "master_count": 3, //设置Master节点数量为3。 "master_vswitch_ids": [ //设置Master节点的交换机列表。 "vsw-j6cwz95vspl56gl******", "vsw-j6c1tgut51ude2v******", "vsw-j6c1tgut51ude2v******" ], "master_instance_types": [ //设置Master节点的实例规格。 "ecs.u1-c1m2.xlarge", "ecs.c7.xlarge", "ecs.c7.xlarge" ], "master_system_disk_category": "cloud_essd", //Master节点系统盘选择ESSD云盘。 "master_system_disk_size": 120, //设置系统盘大小为120 GiB。 "master_system_disk_performance_level": "PL1", //系统盘单盘IOPS性能上限为5万。 "vpcid": "vpc-j6c6njo385se80n******", //集群的专有网络ID须在网络规划时确定，创建后不可修改。#required "worker_vswitch_ids": [ "vsw-j6cwz95vspl56gl******", "vsw-j6c1tgut51ude2v******" ], "is_enterprise_security_group": true, "ip_stack": "ipv4", "service_cidr": "172.16.xx.xx/16", "nodepools": [ { "nodepool_info": { "name": "default-nodepool" }, "scaling_group": { "system_disk_category": "cloud_essd", "system_disk_size": 120, "system_disk_performance_level": "PL0", "system_disk_encrypted": false, "data_disks": [ { "category": "cloud_auto", "size": 200, "encrypted": "false", "bursting_enabled": false } ], "tags": [], "soc_enabled": false, "security_hardening_os": false, "vswitch_ids": [ "vsw-j6cwz95vspl56gl******", "vsw-j6c1tgut51ude2v******" ], "instance_types": [ "ecs.g6.xlarge" ], "instance_patterns": [], "login_password": "******", "instance_charge_type": "PostPaid", "security_group_ids": [], "platform": "AliyunLinux", "image_id": "aliyun_3_x64_20G_alibase_20241218.vhd", "image_type": "AliyunLinux3", "desired_size": 3, //创建一个期望节点数为3的节点池。 "multi_az_policy": "BALANCE" }, "kubernetes_config": { "cpu_policy": "none", "cms_enabled": false, "unschedulable": false, "runtime": "containerd", //设置容器运行时为containerd 1.6.36。集群创建后不可修改。 "runtime_version": "1.6.36" } } ] }重点参数说明
在调用CreateCluster接口创建ACK专有集群时，您需要重点关注如下参数的差异化配置：
| 参数 | 描述 | 配置示例 |
| --- | --- | --- |
| cluster_type | 集群类型。创建 ACK 专有集群 时，该参数必须配置为 Kubernetes 。 | "cluster_type": "Kubernetes" |
### Terraform
具体操作，请参见[通过](../developer-reference/use-terraform-to-create-an-ack-proprietary-cluster.md)[Terraform](../developer-reference/use-terraform-to-create-an-ack-proprietary-cluster.md)[创建](../developer-reference/use-terraform-to-create-an-ack-proprietary-cluster.md)[ACK](../developer-reference/use-terraform-to-create-an-ack-proprietary-cluster.md)[专有集群](../developer-reference/use-terraform-to-create-an-ack-proprietary-cluster.md)。
### SDK
具体操作，请参见[Java SDK](../developer-reference/java-sdk-call-example.md)[调用示例](../developer-reference/java-sdk-call-example.md)。
### CLI
具体操作，请参见[通过](../developer-reference/create-a-cluster-2.md)[CLI](../developer-reference/create-a-cluster-2.md)[创建](../developer-reference/create-a-cluster-2.md)[ACK](../developer-reference/create-a-cluster-2.md)[集群](../developer-reference/create-a-cluster-2.md)。
## 相关操作
查看集群基本信息
在集群列表页面的操作列，单击详情，然后单击基本信息和连接信息页签，查看集群的基本信息和连接信息。其中：
API Server 公网端点：Kubernetes的API Server对公网提供服务的地址和端口，可以通过此服务在用户终端使用kubectl等工具管理集群。
绑定公网IP和解绑公网IP功能：
绑定公网IP：您可以选择在已有EIP列表中绑定EIP或者新建EIP。
绑定公网IP操作会导致API Server短暂重启，请避免在此期间操作集群。
解绑公网IP：解绑公网IP后您将无法通过公网访问API Server。
解绑公网IP操作会导致API Server短暂重启，请避免在此期间操作集群。
API Server 内网端点：Kubernetes的API Server对集群内部提供服务的地址和端口，此IP为负载均衡的地址。
查看集群日志信息
您可以单击操作列的更多>运维管理>查看日志，进入日志中心页面查看集群的日志信息。
查看集群节点信息
您可以[获取集群](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[KubeConfig](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[并通过](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[工具连接集群](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)，执行kubectl get node查看集群的节点信息。
## 配额与限制
如集群规模较大或账号资源较多，请遵循使用ACK集群时涉及的配额与限制。详细信息，请参见[配额与限制](../../product-overview/limits.md)。
使用限制：包括ACK配置限制（例如账号余额等）和单集群容量限制（单集群内不同Kubernetes资源的最大容量）。
配额限制与提升方式：ACK集群配额限制和ACK依赖云产品（例如ECS、VPC等）的配额限制。如需提升配额，请参见文档获取提升方式。
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
