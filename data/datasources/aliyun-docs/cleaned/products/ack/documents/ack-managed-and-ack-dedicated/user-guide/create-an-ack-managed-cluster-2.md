# 使用控制台API等多种方式创建ACK托管集群-容器服务Kubernetes版ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2

# 创建ACK托管集群
创建ACK托管集群时，您只需配置Worker节点，Master节点由阿里云容器服务创建并托管，降低运维成本，让您更聚焦于业务应用。本文介绍如何通过控制台、API、Terraform、SDK以及CLI等方式创建ACK托管集群。
在开始创建ACK集群之前，建议您已了解[Kubernetes](https://kubernetes.io/docs/concepts/)[基础知识](https://kubernetes.io/docs/concepts/)、[容器服务](../../product-overview/product-introduction.md)[ACK](../../product-overview/product-introduction.md)、[ACK](ack-cluster-overview.md)[托管集群](ack-cluster-overview.md)等基础信息。
如果您是首次使用ACK托管集群，可参见[通过](../getting-started/getting-started-with-ack-using-the-ack-console.md)[ACK](../getting-started/getting-started-with-ack-using-the-ack-console.md)[快速搭建魔方游戏应用](../getting-started/getting-started-with-ack-using-the-ack-console.md)开始新手入门体验。体验结束后请及时释放资源，避免产生预期外费用。
## 规划与设计
创建集群前，请根据业务需求规划并设计集群，以确保集群能够稳定、高效且安全地运行。大多数配置项在集群创建后仍可调整，但部分配置项创建后不支持更改，尤其是集群可用性、集群网络相关的配置。规划时，请确保已考虑以下因素。
| 分类 | 说明 |
| --- | --- |
| 部署位置 | 地域：所选地域与 用户和资源部署地域的距离越近，网络时延越低，访问速度越快。 可用区：推荐配置多可用区，以保证集群高可用。 |
| 版本和规格 | [Kubernetes](support-for-kubernetes-versions.md) [版本](support-for-kubernetes-versions.md) ：规划使用的 Kubernetes 版本。建议使用当前的最新版本。 集群规格：提供 [Pro](ack-cluster-overview.md) [版和基础版](ack-cluster-overview.md) 。Pro 版更适用于生产环境，提供 SLA 保障；基础版更适用于测试环境，且资源配额有限。 |
| 网络规划 | 网络插件：选择 Terway 或 Flannel 模式。简单来说，如果对网络安全、IPAM 管理（例如固定 Pod IP、NetworkPolicy 等）等方面有强诉求，建议使用 Terway；如果集群规模较小（例如小于 500 个节点），且对网络无特殊需求，可使用 Flannel。 具体差异，请参见 [容器网络插件](comparison-between-terway-and-flannel.md) [Terway](comparison-between-terway-and-flannel.md) [与](comparison-between-terway-and-flannel.md) [Flannel](comparison-between-terway-and-flannel.md) [对比](comparison-between-terway-and-flannel.md) 。 [网络地址规划](kubernetes-cluster-network-planning.md) ： 根据业务场景和集群规模 规划 VPC 网段（VPC 自身网段和 vSwitch 网段）和 Kubernetes 网段（Pod 地址段和 Service 地址段），定义整个集群的 IP 地址范围以及 Pod 和节点可用的 IP 地址数量。 公网访问：集群节点是否需要访问公网（拉取公共镜像时需开通公网）。 具体配置，请参见 [定义集群网络边界与高可用基础](description-of-configuration-items-for-ack-managed-clusters.md) 中的 为专有网络配置 SNAT 配置项。 IPv6 双栈：集群是否需要同时支持 IPv4 与 IPv6 协议。如需启用，集群所处 VPC 必须支持双栈，且需规划 IPv6 网段。 [安全组](../../../../ecs/documents/user-guide/overview-44.md) ：集群资源所在的安全组，以及使用的安全组类型。 集群本地域名： 集群中所有 Service 使用的顶级域名（标准后缀） ，使得 Pod 和其他资源可以通过名称（而不是 IP 地址）相互访问。 默认为 cluster.local ，如需自定义，请参见 [配置集群本地域名（ClusterDomain）有哪些注意事项？](faq-about-container-networks.md) 。 |
## 准备工作
创建集群前，请确保您已经开通容器服务ACK、为您的阿里云账号或RAM账号授予了ACK系统服务角色（ACK需要这些权限来调用相关服务或执行集群操作），并且开通了相关云产品（例如VPC、负载均衡、NAT网关等）。具体操作，请参见[快速创建](../getting-started/quick-start-for-first-time-users.md)[ACK](../getting-started/quick-start-for-first-time-users.md)[托管集群](../getting-started/quick-start-for-first-time-users.md)。
说明
创建集群过程中涉及负载均衡CLB等按量资源的购买，请确保您的账户余额充足，避免因为欠费导致停机。
## 创建集群
ACK支持通过控制台、API、SDK、Terraform以及CLI方式创建集群。
### 控制台
创建流程
说明
如需使用RAM用户在控制台创建集群，需配置对应的权限后才能正常使用，请参见[容器服务控制台权限依赖](ack-console-permission-dependencies.md)完成精细化授权。
您可以参见控制台指引，基于ACK默认的集群配置创建一个集群。如果您想更细粒度地控制集群配置，请参见[ACK](description-of-configuration-items-for-ack-managed-clusters.md)[托管集群配置项说明](description-of-configuration-items-for-ack-managed-clusters.md)了解并启用对应配置项。下文介绍流程概览。
步骤一：进入创建页面
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在页面左侧顶部，选择目标资源所在的资源组和地域。
在集群列表页面，单击创建集群。在ACK 托管集群页面，按照页面指引完成集群配置、节点池配置、组件配置。
下文步骤未开启智能托管模式。如需使用，请参见[创建](create-ack-managed-clusters-in-auto-mode.md)[ACK](create-ack-managed-clusters-in-auto-mode.md)[托管集群（智能托管模式）](create-ack-managed-clusters-in-auto-mode.md)。
步骤二：配置集群
| 配置类型 | 说明 | 示例样式 |
| --- | --- | --- |
| 基础配置 | 集群的基础信息，包括名称、规格、地域、版本等。支持启用集群版本自动升级，并配置计划执行的维护窗口。 |  |
| 网络配置 | IPv6 双栈开关、VPC 和 vSwitch 配置、是否允许通过公网访问 API Server、安全组、网络插件、网段配置等。 推荐集群 VPC 使用标准私有地址（如 10.0.0.0/8、172.16.0.0/12 和 192.168.0.0/16）。如有特殊需求，请前往 [配额中心](https://quotas.console.aliyun.com/white-list-products/csk/quotas) 申请（ 使用公网网段 VPC 创建集群 ）。 |  |
| 高级配置 | 集群资源管理、集群安全相关的配置。 |  |
详细配置项说明，请参见[集群配置](description-of-configuration-items-for-ack-managed-clusters.md)。
（可选）步骤三：配置节点池
节点池用于对节点进行分组管理，是具有相同属性的一组节点的逻辑集合，本身不计费。简单来说，节点池类似于一个配置模板，后续节点池中扩容出的节点都将使用该模板配置。您在本步骤配置的节点池会作为集群的默认节点池。
您可以按照页面提示跳过节点池的创建和配置。集群创建后，您可以参见[创建和管理节点池](create-a-node-pool.md)创建更多节点池，实现不同类型（例如操作系统、CPU架构、计费类型、实例类型等）节点的混部和隔离，也可以参见[添加已有节点](add-existing-ecs-instances-to-an-ack-cluster.md)将已购买的ECS实例添加到集群中。
| 配置类型 | 说明 | 示例样式 |
| --- | --- | --- |
| 基础配置 | 节点的基础信息，包括名称、运行时。支持启用自动化运维能力。 |  |
| 实例和镜像配置 | 节点的付费类型、使用的实例规格（推荐选择多个）、操作系统等。 |  |
| 存储配置 | 节点使用的系统盘（安装和运行操作系统）和数据盘（持久化存储业务数据）。 |  |
| 实例数量配置 | 节点池期望维持的实例数量、抢占式实例的容量及补偿配置（仅付费类型为抢占式实例时支持）。 |  |
| 高级配置 | ECS 标签、节点标签、污点等进阶配置。 |  |
详细配置项说明，请参见[节点池配置](description-of-configuration-items-for-ack-managed-clusters.md)。
步骤四：配置组件
为进一步拓展集群功能，除系统组件外，ACK还提供多种类型的功能组件，提供集群网络、可观测性、成本优化等功能。
说明
ACK基于最佳实践为您默认安装了一些组件。您可以在此步骤中查看并确认，也可以在集群创建后进行安装、卸载、升级等操作，请参见[管理组件](../../manage-system-components.md)。
| 配置类型 | 说明 | 示例样式 |
| --- | --- | --- |
| 基础组件 | 网络、存储、可观测组件。 |  |
| 更多组件 | 应用管理、日志监控、存储等场景下的组件。 |  |
详细配置项说明，请参见[组件配置](description-of-configuration-items-for-ack-managed-clusters.md)。
步骤五：确认配置和计费信息
在确认配置页面，确认集群的配置信息，包括功能配置、资源计费、云产品依赖检查等，并阅读服务协议。
ACK托管集群涉及集群管理费用（仅Pro版收取）和云产品费用。您可以在创建页面下方查看集群涉及的费用总览，也可以查看ACK和各产品的计费文档，请参见[计费概述](../product-overview/ack-pro-cluster-billing.md)、[云产品资源费用](../product-overview/billing-of-cloud-services.md)。
您还可以在确认配置页面的右上角单击同等代码，生成当前集群配置对应的Terraform或SDK示例参数。
### API
调试入口
[CreateCluster](https://next.api.aliyun.com/api/CS/2015-12-15/CreateCluster)[调试入口](https://next.api.aliyun.com/api/CS/2015-12-15/CreateCluster)
请求示例
创建一个ACK托管集群Pro版的请求示例如下，完整的参数说明请参见[CreateCluster - 创建集群](../developer-reference/api-cs-2015-12-15-createcluster.md)。
POST /clusters <公共请求头> { "name": "ACK托管集群", "cluster_type": "ManagedKubernetes", //和profile、cluster_spec配合使用，指定集群的类型为ACK托管集群Pro版。#required "profile": "Default", "cluster_spec": "ack.pro.small", "kubernetes_version": "1.32.1-aliyun.1", //创建的集群版本，建议选择最新版本。 "region_id": "cn-hongkong", //集群所属地域为香港地域。#required "snat_entry": true, // 为专有网络配置SNAT规则，以开启集群公网访问。 "endpoint_public_access": false, //集群不开启API server公网访问。 "deletion_protection": true, //开启集群删除保护。 "proxy_mode": "ipvs", //选择高性能的kube-proxy代理模式IPVS。 "tags": [], "timezone": "Asia/Shanghai", "addons": [ //安装的集群组件。 { "name": "terway-controlplane", "config": "{\"ENITrunking\":\"true\"}" }, { "name": "terway-eniip", //集群的网络类型为Terway方式。集群创建后不可修改。 "config": "{\"IPVlan\":\"false\",\"NetworkPolicy\":\"false\",\"ENITrunking\":\"true\"}" }, { "name": "csi-plugin" }, { "name": "managed-csiprovisioner" }, { "name": "storage-operator", "config": "{\"CnfsOssEnable\":\"false\",\"CnfsNasEnable\":\"false\"}" }, { "name": "nginx-ingress-controller", "disabled": true }, { "name": "ack-node-local-dns" } ], "enable_rrsa": false, "os_type": "Linux", "platform": "AliyunLinux", "image_type": "AliyunLinux3", "pod_vswitch_ids": [ //Terway网络类型的集群，需要指定Pod所在的虚拟交换，因为Pod独占一个机器IP。 "vsw-j6cht66iul7h61x******", "vsw-j6c5ne6mxgnx3g5******" ], "charge_type": "PostPaid", "vpcid": "vpc-j6cc1ddlp4rzs7v******", //集群的专有网络ID须在网络规划时确定，创建后不可修改。#required "service_cidr": "192.168.xx.xx/16", //集群的Service网段。#required "vswitch_ids": [ //选择多个交换机用于保证集群的高可用。#required "vsw-j6cht66iul7h61x******", "vsw-j6c5ne6mxgnx3g5******" ], "ip_stack": "ipv4", //选择IP栈类型为IPv4。 "logging_type": "SLS", "cpu_policy": "none", "service_account_issuer": "https://kubernetes.default.svc", "api_audiences": "https://kubernetes.default.svc", "is_enterprise_security_group": true, "maintenance_window": { //设置每周四01:00 ~ 04:00为集群的维护窗口。 "enable": true, "duration": "3h", "weekly_period": "Thursday", "maintenance_time": "2025-03-03T01:00:00.000+08:00" }, "operation_policy": { "cluster_auto_upgrade": { "enabled": true, "channel": "stable" } }, "controlplane_log_ttl": "30", "controlplane_log_components": [ "apiserver", "kcm", "scheduler", "ccm", "controlplane-events", "alb" ], "nodepools": [ { "nodepool_info": { //节点池配置。 "name": "default-nodepool" }, "scaling_group": { "system_disk_category": "cloud_essd", //节点池的系统盘选择ESSD云盘。 "system_disk_size": 120, //设置系统盘大小为120 GiB。 "system_disk_performance_level": "PL0", //系统盘单盘IOPS性能上限为1万。 "system_disk_encrypted": false, "data_disks": [], "tags": [], "soc_enabled": false, "security_hardening_os": false, "vswitch_ids": [ "vsw-j6cht66iul7h61x******", "vsw-j6c5ne6mxgnx3g5******" ], "instance_types": [ "ecs.c6.xlarge", "ecs.c7.xlarge" ], "instance_patterns": [], "login_password": "", "instance_charge_type": "PostPaid", "security_group_ids": [], "platform": "AliyunLinux", "image_id": "aliyun_3_x64_20G_alibase_20241218.vhd", "image_type": "AliyunLinux3", "desired_size": 3, //创建一个期望节点数为3的节点池。 "rds_instances": [], "multi_az_policy": "BALANCE" }, "kubernetes_config": { "cpu_policy": "none", "cms_enabled": true, "unschedulable": false, "runtime": "containerd", //设置容器运行时为containerd 1.6.36。集群创建后不可修改。 "runtime_version": "1.6.36" }, "node_config": { "image_acceleration_config": { "enable_image_acceleration": false } }, "management": { "enable": true, "auto_repair": true, "auto_repair_policy": { "restart_node": true }, "auto_upgrade": true, "auto_upgrade_policy": { "auto_upgrade_kubelet": true, "auto_upgrade_os": false }, "auto_vul_fix": true, "auto_vul_fix_policy": { "vul_level": "asap", "restart_node": true }, "rolling_policy": { "max_parallelism": 10 } } } ] }重点参数说明
在调用CreateCluster接口创建ACK托管集群时，您需要重点关注如下参数的差异化配置：
| 参数 | 描述 | 参数组合 |
| --- | --- | --- |
| cluster_type | 集群类型。创建 ACK 托管集群 时，该参数必须配置为 ManagedKubernetes 。 | 创建 ACK 托管集群 Pro 版 "cluster_type": "ManagedKubernetes" "profile": "Default" "cluster_spec": "ack.pro.small" 创建 ACK 托管集群基础版 "cluster_type": "ManagedKubernetes" "profile": "Default" "cluster_spec": "ack.standard" |
| profile | 集群子类型。创建 ACK 托管集群 时，该参数必须配置为 Default 。 |  |
| cluster_spec | 集群规格。 ack.pro.small ：表示创建 ACK 托管集群 Pro 版 。 ack.standard ：表示创建 ACK 托管集群基础版 。 |  |
### Terraform
具体操作，请参见[通过](../developer-reference/use-terraform-to-create-an-ack-managed-cluster.md)[Terraform](../developer-reference/use-terraform-to-create-an-ack-managed-cluster.md)[创建](../developer-reference/use-terraform-to-create-an-ack-managed-cluster.md)[ACK](../developer-reference/use-terraform-to-create-an-ack-managed-cluster.md)[托管集群](../developer-reference/use-terraform-to-create-an-ack-managed-cluster.md)。
### SDK
具体操作，请参见[Java SDK](../developer-reference/java-sdk-call-example.md)[调用示例](../developer-reference/java-sdk-call-example.md)。
### CLI
具体操作，请参见[通过](../developer-reference/create-a-cluster-2.md)[CLI](../developer-reference/create-a-cluster-2.md)[创建](../developer-reference/create-a-cluster-2.md)[ACK](../developer-reference/create-a-cluster-2.md)[集群](../developer-reference/create-a-cluster-2.md)。
## 后续操作
应用部署：创建并管理工作负载，包括Deployment、StatefulSet、Job等，请参见[创建工作负载](deploying-workloads.md)。
服务发现与网络管理
[Service](service-management.md)：为一组Pod提供固定的访问入口，实现集群内访问、公网访问等。
[Ingress](ingress-management-2.md)：配置不同的转发规则，例如通过域名或者访问路径来路由到不同的Service上，从而实现负载均衡。
[服务发现](service-discovery-dns-1.md)[DNS](service-discovery-dns-1.md)：为集群内的工作负载提供域名解析服务，使得集群内部的服务可以通过服务名来互相访问，无需知道具体的IP地址。
可观测配置：实现集群日志收集和监控告警，便于集群诊断和状态观测。请参见[可观测性](observability-overview.md)了解ACK在基础设施、容器、工作负载等维度提供的可观测方案。
[存储](csi-overview-1.md)：基于CSI插件实现应用数据持久化存储、敏感和配置数据存储、存储资源动态供应等存储需求。
[弹性伸缩](auto-scaling-overview.md)配置：如业务资源需求不易预测或有周期性变化（例如Web应用、游戏服务、在线教育等），推荐启用弹性伸缩，包括工作负载伸缩（HPA、CronHPA、VPA等）和计算资源伸缩（节点自动伸缩、节点即时弹性等）。
精细化授权
如需对基础资源层（ACK依赖的云产品）和集群内部资源（Kubernetes资源对象）进行更细粒度的权限控制，ACK提供基于阿里云RAM和Kubernetes原生RBAC机制的多种权限管理方案，请参见[授权](authorization-overview.md)。
## 配额与限制
如集群规模较大或账号资源较多，请遵循使用ACK集群时涉及的配额与限制。详细信息，请参见[配额与限制](../../product-overview/limits.md)。
使用限制：包括ACK配置限制（例如账号余额等）和单集群容量限制（单集群内不同Kubernetes资源的最大容量）。
配额限制与提升方式：ACK集群配额限制和ACK依赖云产品（例如ECS、VPC等）的配额限制。如需提升配额，请参见文档获取提升方式。
## 常见问题
如在使用ACK集群的过程中遇到问题，可参见[故障排除](../support/troubleshooting-10.md)、[常见问题](../support/faq.md)进行自排查。
可以创建一个0节点的集群吗？
可以。如需跳过节点创建，或在集群创建后再将已购买的ECS实例添加到集群中，可在配置过程中将期望节点数配置为0，即配置集群中的实例数量为0，并完成其他必选项的配置，后续再参见[创建和管理节点池](create-a-node-pool.md)完成节点池的配置更新或新建更多节点池。如需将已购买的ECS实例添加到集群，请参见[添加已有节点](add-existing-ecs-instances-to-an-ack-cluster.md)。
已购买的ECS实例如何添加到集群中？
ACK支持将已有ECS实例手动或自动添加到节点池中。自动添加的方式会根据节点池当前的操作系统替换该ECS实例原有的操作系统，原系统盘会被释放。如需保留ECS实例操作系统，请选择手动添加的方式。相关注意事项及操作步骤，请参见[添加已有节点](add-existing-ecs-instances-to-an-ack-cluster.md)。
建议待添加ECS实例与待加入的节点池具有相同或类似配置（例如付费类型、磁盘配置、实例规格等），便于后续节点的统一管理。
已购买的按量付费的ECS实例可以添加到包年包月的节点池中吗？
可以，您可以参见[添加已有节点](add-existing-ecs-instances-to-an-ack-cluster.md)完成操作。但当节点池付费类型为包年包月时，后续节点池扩容出的节点均为包年包月类型。建议您创建不同的节点池，纳管不同类型（例如付费类型、磁盘配置、实例规格等）的节点。具体操作，请参见[创建和管理节点池](create-a-node-pool.md)。
为什么刚创建好的集群就提示Pod数量不足？
可能是以下原因。
组件占用：集群组件会以Pod的形式存在，占用节点资源。部分组件可能会采用多副本形式。如果您创建集群配置组件时启用的功能较多，可能会占用节点较多的Pod数量。
实例规格较小：Terway模式下，单节点支持的最大Pod数依赖于ECS[实例规格族](../../../../ecs/documents/user-guide/overview-of-instance-families.md)所提供的弹性网卡（ENI）数量。虽然节点支持的最大Pod数跟CPU和内存并不是直接的线性关系，但通常较小规格的ECS实例支持的ENI数量较少，单节点的Pod限额也较小。
当节点Pod数量达到上限时，新Pod将调度失败，影响服务性能。您可以通过扩容节点池以增加更多可用的节点、升配节点以提升单节点最大Pod数等方式增加可使用的Pod数，请参见[调整可使用的节点](adjusting-the-number-of-node-pods.md)[Pod](adjusting-the-number-of-node-pods.md)[数量](adjusting-the-number-of-node-pods.md)。
购买后查看节点可用的CPU和内存资源，为什么比购买时的实例规格定义的少？
ACK需要占用一定的节点资源来为kube组件和system进程预留资源，从而保证OS内核和系统服务、Kubernetes守护进程的正常运行。这会导致节点的资源总数（Capacity）与可分配的资源数（Allocatable）之间存在差异。详细信息，请参见[节点资源预留策略](resource-reservation-policy.md)。
## 相关文档
使用ACK集群过程中，操作不当可能会导致业务故障，请参见[使用须知及高危风险操作说明](../../product-overview/before-you-start.md)。
关于如何连接集群，请参见[获取集群](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[KubeConfig](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[并通过](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[工具连接集群](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。
为避免过期版本集群存在的安全和稳定性风险，建议您及时升级集群，请参见[手动升级集群](update-the-kubernetes-version-of-an-ack-cluster.md)、[自动升级集群](automatically-upgrade-an-ack-cluster.md)。
如需在ACK集群中跨域拉取海外源容器镜像，请参见[使用](cross-domain-accelerated-pulling-container-images.md)[GA](cross-domain-accelerated-pulling-container-images.md)[实现](cross-domain-accelerated-pulling-container-images.md)[ACK](cross-domain-accelerated-pulling-container-images.md)[跨域加速拉取容器镜像](cross-domain-accelerated-pulling-container-images.md)。
如有任何产品建议或疑问，请[联系我们](../support/contact-us.md)。
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
