# 专有网络VPC的产品功能动态和对应的文档-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/release-notes

# 新功能发布记录
本文介绍了专有网络VPC（Virtual Private Cloud）的产品功能动态和相关文档。
## 2026年2月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 路由目标组 | 新增 | 路由目标组支持以主备模式配置两个同 VPC、不同可用区的下一跳实例（如 GWLBe），系统自动检测实例健康状态，在主实例异常时自动将流量切换至备实例，实现可用区级别的容灾切换，缩短故障恢复时间（RTO）。 | [路由目标组](route-target-group.md) |
| 流日志 | 更新 | 流日志支持投递到 NIS 流量分析器。 | [流日志-分析和投递配置](vpc-flow-logs.md) |
## 2026年1月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 网络 ACL | 更新 | 网络 ACL 规则支持引用前缀列表，简化配置。用户将常用 IP 地址段统一管理在前缀列表，在网络 ACL 规则中引用。修改前缀列表后，网络 ACL 规则会自动同步更新。 | [配置网络](network-acl-overview.md) [ACL](network-acl-overview.md) [规则](network-acl-overview.md) |
## 2025年12月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| IPAM | 更新 | IPAM 支持在资源目录内 [委派管理员](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/manage-a-delegated-administrator-account) 。IPAM 作为资源目录的可信服务，支持委派管理员账号统一查看企业多个账号下的 VPC、交换机的地址使用信息。 | [多账号地址资源管理](shared-resource-discovery-for-multi-account-address-resource-conflict-management.md) |
## 2025年9月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 对等连接 | 更新 | 创建同账号 VPC 对等连接时，可勾选 VPC 系统路由表添加对端 VPC CIDR 路由，将由系统配置双向路由。 | [对等连接](vpc-peer-to-peer-connection.md) |
## 2025年7月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| IPAM | 更新 | IPAM 支持公网 IPv6 地址池，允许使用阿里云 IPv6 地址段，用于业务规划和 IPv6 地址分配。 | [IPAM](ip-address-management-ipam.md) |
## 2025年5月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 路由表 | 更新 | 您可以在控制台，按照 目标网段 对路由条目进行模糊搜索，提升路由管理效率。 | [路由表](vpc-route-table.md) |
## 2025年4月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 专有网络 | 更新 | 删除 VPC 和交换机时，系统将展示依赖资源信息，您可以按照指引释放对应资源。 | [删除专有网络](user-guide/create-and-manage-a-vpc.md) [删除交换机](user-guide/create-and-manage-vswitch.md) |
| 网络 ACL | 更新 | 您可以在控制台，通过协议名称或协议号模糊搜索，选择协议类型，配置网络 ACL 规则。 | [网络](network-acl-overview.md) [ACL](network-acl-overview.md) |
| 流日志 | 更新 | 流日志支持采集 IPv6 流量，进行分析审计或问题排查。支持的地域有 华北 1（青岛） 、 华北 5（呼和浩特） 、 美国（硅谷） 、 美国（弗吉尼亚） 。 | [流日志](vpc-flow-logs.md) |
## 2025年3月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 网关路由表 | 更新 | 网关路由表支持绑定 IPv6 网关，您可以修改网关路由表系统路由条目的下一跳，控制进入 VPC 的 IPv6 流量。 | [使用网关路由表控制进入](use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md) [VPC](use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md) [的流量](use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md) |
## 2025年2月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| IP 地址管理（IPAM） | 更新 | 企业多账号场景中，业务账号可以将创建的资源发现，共享给网络管理员进行地址资源的统一管理。 | [地址资源管理](shared-resource-discovery-for-multi-account-address-resource-conflict-management.md) |
## 2025年1月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 对等连接 | 更新 | 跨地域 对等连接，支持铂金、金两种链路类型，分别提供不同质量的流量传输服务。 | [VPC](vpc-peer-to-peer-connection.md) [对等连接](vpc-peer-to-peer-connection.md) |
## 2024年12月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| IP 地址管理（IPAM） | 更新 | 您可以使用资源目录的管控策略，限制业务账号只能从共享的 IPAM 地址池中分配地址来创建 VPC，统一网络地址的使用方式，便于管理。 | [基于资源目录管控策略强制使用](use-control-policies-to-restrict-vpc-creation-from-an-ipam-address-pool-in-a-multi-account-system.md) [IPAM](use-control-policies-to-restrict-vpc-creation-from-an-ipam-address-pool-in-a-multi-account-system.md) [地址池统一创建](use-control-policies-to-restrict-vpc-creation-from-an-ipam-address-pool-in-a-multi-account-system.md) [VPC](use-control-policies-to-restrict-vpc-creation-from-an-ipam-address-pool-in-a-multi-account-system.md) |
## 2024年11月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 网络 ACL | 更新 | 您可以通过批量导入/导出网络 ACL 规则，保证数据的一致性，提升配置效率。 | [创建和管理网络](work-with-network-acls.md) [ACL](work-with-network-acls.md) |
| 对等连接 | 更新 | 您可以使用私网连接 PrivateLink 在 VPC 内通过私网访问 VpcPeer OpenAPI 服务。 | [使用](create-and-manage-vpc-peering-connection.md) [VPC](create-and-manage-vpc-peering-connection.md) [对等连接实现](create-and-manage-vpc-peering-connection.md) [VPC](create-and-manage-vpc-peering-connection.md) [私网互通](create-and-manage-vpc-peering-connection.md) |
## 2024年10月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 路由 | 更新 | 自定义路由条目下一跳类型支持网关型负载均衡终端节点。 | [路由表](vpc-route-table.md) [使用自定义路由表进行网络流量管理](network-traffic-management-using-custom-routing-tables.md) |
| 更新 | 您可以修改自定义路由条目的下一跳，动态调整网络流量。 |  |  |
| 专有网络 | 更新 | VPC 中的 DNS 主机名控制 ECS 实例私网域名解析功能。只有当 VPC 启用 DNS 主机名，ECS 实例的私网域名才能生效，VPC 禁用 DNS 主机名，ECS 实例的私网域名将失效。 | [创建和管理专有网络](user-guide/create-and-manage-a-vpc.md) [VPC](user-guide/enable-dns-hostname-for-ecs-private-domain-name-access-in-vpc.md) [私网域名](user-guide/enable-dns-hostname-for-ecs-private-domain-name-access-in-vpc.md) |
| VPC 流日志 | 更新 | 您可以根据具体场景选择采集对应路径的流量信息，包括：采集全部场景、通过 IPv4 网关访问公网的流量、通过 NAT 网关的流量、通过 VPN 网关的流量、通过转发路由器（TR）的流量、通过网关终端节点访问云服务的流量、通过边界路由器（VBR）访问专线的流量。 | [流日志](vpc-flow-logs.md) |
## 2024年09月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| IP 地址管理（IPAM） | 更新 | 当您创建 IPAM 后，系统为您默认创建 IPAM 资源发现并与创建的 IPAM 进行关联，您可通过资源发现管理 VPC 和交换机地址资源。 | [IP](ip-address-management-ipam.md) [地址管理（IPAM）](ip-address-management-ipam.md) [创建和管理](create-and-manage-ipam.md) [IPAM](create-and-manage-ipam.md) |
| 更新 | 您可以监控 IP 地址利用率等相关指标，进行 IP 地址容量管理，针对高利用率的资源及时扩容，保障网络的稳定性与安全性。 | [IP](ip-address-management-ipam.md) [地址管理（IPAM）](ip-address-management-ipam.md) [创建和管理](create-and-manage-ipam.md) [IPAM](create-and-manage-ipam.md) [创建和管理](create-and-manage-address-pools.md) [IPAM](create-and-manage-address-pools.md) [地址池](create-and-manage-address-pools.md) |  |
| 更新 | IPAM 地址池的资源所有者可以将地址池共享给其他阿里云账号（资源使用者），资源使用者可以在创建 VPC 时选择从共享的地址池分配。 | [共享](use-resource-management-to-share-ipam-address-pools.md) [IPAM](use-resource-management-to-share-ipam-address-pools.md) [地址池实现多账号下地址统一规划管理](use-resource-management-to-share-ipam-address-pools.md) |  |
| 路由 | 更新 | VPC 支持静态路由发布至专线网关 ECR。您可以将 VPC 系统路由表配置的自定义路由条目发布至 ECR，实现动态路由传播。在不存在路由冲突的情况下，ECR 关联的本地 IDC 均可学习到该路由。 | [路由表](vpc-route-table.md) [使用静态路由发布至](use-static-route-publishing-to-enable-local-idc-access-to-the-public-network.md) [ECR](use-static-route-publishing-to-enable-local-idc-access-to-the-public-network.md) [实现动态路由传播](use-static-route-publishing-to-enable-local-idc-access-to-the-public-network.md) |
| 网络 ACL | 更新 | IPv6 网络 ACL 支持的地域新增 华东 1（杭州） 、 华东 2（上海） 、 华北 1（青岛） 、 华南 1（深圳） 、 美国（硅谷） 。 | [网络](network-acl-overview.md) [ACL](network-acl-overview.md) |
| VPC IPv6 功能 | 更新 | VPC IPv6 功能支持的地域新增 英国（伦敦） 。 | [创建和管理专有网络](user-guide/create-and-manage-a-vpc.md) |
## 2024年08月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| VPC 前缀列表 | 更新 | VPC 前缀列表支持关联安全组的地域新增 华东 1（杭州） 、 华东 2（上海） 、 华东 5 （南京-本地地域-关停中） 、 华北 1（青岛） 、 华北 2（北京） 、 华北 6（乌兰察布） 、 华南 1（深圳） 、 华南 2（河源） 、 华南 3（广州） 、 西南 1（成都） 、 中国香港 、 华中 1（武汉-本地地域） 、 华东 6（福州-本地地域-关停中） 、 韩国（首尔） 、 新加坡 、 泰国（曼谷） 、 阿联酋（迪拜） 、 沙特（利雅得）- 合作伙伴运营 。 | [前缀列表使用示例](user-guide/prefix-list-use-cases.md) |
| 网络 ACL | 更新 | IPv6 网络 ACL 支持的地域新增 华北 2（北京） 、 华北 5（呼和浩特） 、 华北 6（乌兰察布） 、 华南 3（广州） 、 西南 1（成都） 、 中国香港 、 韩国（首尔） 、 泰国（曼谷） 、 阿联酋（迪拜） 、 沙特（利雅得）- 合作伙伴运营 。 | [网络](network-acl-overview.md) [ACL](network-acl-overview.md) |
## 2024年07月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| IPv4 网关 | 更新 | IPv4 网关删除支持选择公网模式，允许用户回退到公网 IP 直接访问，优化产品能力，减少用户使用后公网无法访问的体验问题。 | [IPv4](ipv4-gateway-overview.md) [网关](ipv4-gateway-overview.md) [创建和管理](user-guide/create-and-manage-an-ipv4-gateway.md) [IPv4](user-guide/create-and-manage-an-ipv4-gateway.md) [网关](user-guide/create-and-manage-an-ipv4-gateway.md) |
| VPC 前缀列表 | 更新 | VPC 前缀列表支持关联安全组的地域新增 华北 5（呼和浩特） 、 日本（东京） 、 印度尼西亚（雅加达） 、 菲律宾（马尼拉） 、 德国（法兰克福） 、 英国（伦敦） 、 美国（硅谷） 、 美国（弗吉尼亚） 。 | [前缀列表使用示例](user-guide/prefix-list-use-cases.md) |
| VPC 流量镜像 | 更新 | VPC 流量镜像支持的地域新增 华北 6（乌兰察布） 。 | [流量镜像](traffic-mirroring-overview.md) |
| 网络 ACL | 更新 | IPv6 网络 ACL 支持的地域新增 日本（东京） 、 马来西亚（吉隆坡） 、 印度尼西亚（雅加达） 、 美国（弗吉尼亚） 。 | [网络](network-acl-overview.md) [ACL](network-acl-overview.md) |
| 更新 | 网络 ACL 支持快速添加多网段网络 ACL 规则，如果您需要对多个 IP 地址段进行统一的网络访问控制时，使用该功能可以简化业务配置并确保一致的安全策略。 | [创建和管理网络](work-with-network-acls.md) [ACL](work-with-network-acls.md) |  |
## 2024年06月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| VPC 流日志 | 更新 | VPC 流日志支持的地域新增 泰国（曼谷） 、 华北 2 金融云（邀测） 。 | [流日志](vpc-flow-logs.md) |
| VPC IPv6 功能 | 更新 | VPC 支持 IPv6 功能新增 华东 5 （南京-本地地域-关停中） 。 | [创建和管理专有网络](user-guide/create-and-manage-a-vpc.md) |
| 路由表 | 更新 | VPC 路由表支持开启或关闭接收 ECR 动态路由传播。 | [创建和管理路由表](user-guide/create-and-manage-route-table.md) |
| VPC 路由表中支持查看路由条目的来源。 | [路由表](vpc-route-table.md) |  |  |
| IP 地址管理（IPAM） | 新增 | IPAM 是一个 IP 地址管理工具，您可以使用阿里云的 IPAM 地址管理功能，该功能可以自动化分配或跟踪 IP 地址，从而让您更轻松地规划和管理工作中的 IP 地址。 | [IP](ip-address-management-ipam.md) [地址管理（IPAM）](ip-address-management-ipam.md) [创建和管理专有网络](user-guide/create-and-manage-a-vpc.md) |
## 2024年04月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| VPC 前缀列表 | 更新 | VPC 前缀列表支持关联 ECS 的安全组。 | [前缀列表使用示例](user-guide/prefix-list-use-cases.md) |
| 网关终端节点 | 更新 | 网关终端节点支持的地域新增 新加坡 、 英国（伦敦） 、 印度尼西亚（雅加达） 、 日本（东京） 、 德国（法兰克福） 、 美国（硅谷） 、 美国（弗吉尼亚） 。 | [VPC](regions-that-support-vpc-features.md) [特性支持的地域](regions-that-support-vpc-features.md) [VPC](vpc-connection-to-cloud-service.md) [私网访问云服务](vpc-connection-to-cloud-service.md) |
| VPC 对等连接 | 更新 | VPC 对等连接支持的地域新增 华中 1（武汉-本地地域） 。 | [VPC](regions-that-support-vpc-features.md) [特性支持的地域](regions-that-support-vpc-features.md) [VPC](vpc-peer-to-peer-connection.md) [对等连接](vpc-peer-to-peer-connection.md) |
| 网络 ACL | 更新 | IPv6 类型的网络 ACL 支持的地域新增 德国（法兰克福） 。 | [网络](network-acl-overview.md) [ACL](network-acl-overview.md) [创建和管理网络](work-with-network-acls.md) [ACL](work-with-network-acls.md) |
## 2024年03月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 路由表 | 更新 | 自定义路由条目下一跳类型支持专线网关。 | [路由表](vpc-route-table.md) [创建和管理路由表](user-guide/create-and-manage-route-table.md) |
| 网络 ACL | 更新 | 网络 ACL 区分 IPv4 和 IPv6 配额。 | [创建和管理网络](work-with-network-acls.md) [ACL](work-with-network-acls.md) |
| VPC 高级特性 | 更新 | VPC 取消高级特性页签，且 VPC 高级功能不受 ECS 规格族限制。 | [限制与配额](understanding-vpc-quotas-in-alibaba-cloud.md) [查看专有网络](user-guide/create-and-manage-a-vpc.md) [创建和管理路由表](user-guide/create-and-manage-route-table.md) [创建和管理](user-guide/create-and-manage-an-ipv4-gateway.md) [IPv4](user-guide/create-and-manage-an-ipv4-gateway.md) [网关](user-guide/create-and-manage-an-ipv4-gateway.md) [DHCP](dhcp-option-set-and-dns-hostname.md) [选项集与](dhcp-option-set-and-dns-hostname.md) [DNS](dhcp-option-set-and-dns-hostname.md) [主机名](dhcp-option-set-and-dns-hostname.md) [创建和管理网络](work-with-network-acls.md) [ACL](work-with-network-acls.md) |
| VPC 对等连接 | 新增 | VPC 对等连接实例出现访问不通的问题时，您可以通过路径分析功能检测两个 VPC 之间的连通性，诊断网络配置错误引起的连接问题。 | [使用路径分析进行问题排查](path-analysis-of-vpc-peer-to-peer-connection.md) |
| 更新 | VPC 对等连接上线同地域和跨地域配额。 | [限制与配额](understanding-vpc-quotas-in-alibaba-cloud.md) [VPC](vpc-peer-to-peer-connection.md) [对等连接](vpc-peer-to-peer-connection.md) |  |
| 更新 | VPC 对等连接支持的地域新增 阿联酋（迪拜） 、 华北 2 阿里政务云 1 。 | [VPC](regions-that-support-vpc-features.md) [特性支持的地域](regions-that-support-vpc-features.md) [VPC](vpc-peer-to-peer-connection.md) [对等连接](vpc-peer-to-peer-connection.md) |  |
| 流日志 | 更新 | VPC 流日志支持的地域新增 华东 6（福州-本地地域-关停中） 、 韩国（首尔） 、 菲律宾（马尼拉） 。 | [VPC](regions-that-support-vpc-features.md) [特性支持的地域](regions-that-support-vpc-features.md) [流日志](vpc-flow-logs.md) |
## 2024年02月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 流量镜像 | 更新 | 流量镜像支持的地域新增 华东 6（福州-本地地域-关停中） 、 华东 1 金融云 、 华东 2 金融云 、 华北 2 阿里政务云 1 。 | [流量镜像](traffic-mirroring-overview.md) |
## 2024年01月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 前缀列表 | 更新 | IPv6 类型的前缀列表功能支持全地域开服。 | [IPv6](vpc-prefix-lists.md) [类型的前缀列表支持的地域](vpc-prefix-lists.md) |
| 专有网络 | 更新 | VPC 开通 IPv6 网段支持的地域新增 美国（硅谷） 、 泰国（曼谷） 。 | [创建专有网络和交换机](user-guide/create-and-manage-a-vpc.md) |
| 流日志 | 更新 | VPC 流日志支持的地域新增 沙特（利雅得）- 合作伙伴运营 。 | [流日志](vpc-flow-logs.md) |
| 流量镜像 | 更新 | 流量镜像支持的地域新增 沙特（利雅得）- 合作伙伴运营 。 | [流量镜像](traffic-mirroring-overview.md) |
## 2023年12月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 前缀列表 | 更新 | 前缀列表支持配置 IPv6 类型的 CIDR。 说明 仅 菲律宾（马尼拉） 地域支持。 | [前缀列表](vpc-prefix-lists.md) [创建和管理前缀列表](user-guide/create-and-manage-prefix-lists.md) |
| 更新 | 前缀列表支持批量导入和实例克隆。 | [创建和管理前缀列表](user-guide/create-and-manage-prefix-lists.md) |  |
| 网络 ACL | 更新 | 网络 ACL 入方向和出方向规则支持配置 IPv6 网段。 说明 仅 菲律宾（马尼拉） 地域支持。 | [创建和管理网络](work-with-network-acls.md) [ACL](work-with-network-acls.md) |
| 专有网络 | 更新 | 专有网络 VPC 的 IPv6 功能支持 华中 1（武汉-本地地域） 、 马来西亚（吉隆坡） 。 | [创建专有网络和交换机](user-guide/create-and-manage-a-vpc.md) |
## 2023年08月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| VPC 对等连接 | 更新 | 开启 IPv6 的 VPC 支持通过 VPC 对等连接互通。 | [VPC](vpc-peer-to-peer-connection.md) [对等连接](vpc-peer-to-peer-connection.md) [使用](create-and-manage-vpc-peering-connection.md) [VPC](create-and-manage-vpc-peering-connection.md) [对等连接实现](create-and-manage-vpc-peering-connection.md) [VPC](create-and-manage-vpc-peering-connection.md) [私网互通](create-and-manage-vpc-peering-connection.md) [VPC](vpc-peering-connection-configuration-example.md) [对等连接配置示例](vpc-peering-connection-configuration-example.md) |
## 2023年04月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 预留网段 | 新增 | 专有网络 VPC 支持为目标交换机添加预留网段。 | [创建和管理交换机](user-guide/create-and-manage-vswitch.md) |
## 2022年09月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| IPv4 网关 | 新增 | IPv4 网关是连接专有网络 VPC 和公网的网络组件。VPC 通过 IPv4 网关访问公网，该 IPv4 网关负责路由转发和私网 IP 到公网 IP 的转换，最终实现对公网的访问。 | [IPv4](ipv4-gateway-overview.md) [网关](ipv4-gateway-overview.md) [创建和管理](user-guide/create-and-manage-an-ipv4-gateway.md) [IPv4](user-guide/create-and-manage-an-ipv4-gateway.md) [网关](user-guide/create-and-manage-an-ipv4-gateway.md) [如何在已有公网](user-guide/create-and-enable-ipv4-gateway-in-vpc-associated-with-internet-nat-gateway.md) [NAT](user-guide/create-and-enable-ipv4-gateway-in-vpc-associated-with-internet-nat-gateway.md) [网关的](user-guide/create-and-enable-ipv4-gateway-in-vpc-associated-with-internet-nat-gateway.md) [VPC](user-guide/create-and-enable-ipv4-gateway-in-vpc-associated-with-internet-nat-gateway.md) [中开启](user-guide/create-and-enable-ipv4-gateway-in-vpc-associated-with-internet-nat-gateway.md) [IPv4](user-guide/create-and-enable-ipv4-gateway-in-vpc-associated-with-internet-nat-gateway.md) [网关](user-guide/create-and-enable-ipv4-gateway-in-vpc-associated-with-internet-nat-gateway.md) [IPv4](user-guide/faq-2.md) [网关](user-guide/faq-2.md) [FAQ](user-guide/faq-2.md) |
## 2022年08月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 前缀列表 | 新增 | 前缀列表是包含一个或多个 CIDR（Classless Inter-Domain Routing）地址块的集合，可用来简化 VPC 路由表或 CEN 路由表的配置和管理。您还可以通过资源共享服务将前缀列表共享给其他阿里云账号（主账号）使用。 | [前缀列表](vpc-prefix-lists.md) [创建和管理前缀列表](user-guide/create-and-manage-prefix-lists.md) [前缀列表使用示例](user-guide/prefix-list-use-cases.md) |
## 2022年05月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| VPC 对等连接 | 新增 | 您可以通过 VPC 对等连接，实现两个同账号或跨账号 VPC 间同地域或跨地域的私网互通。 | [VPC](vpc-peer-to-peer-connection.md) [对等连接](vpc-peer-to-peer-connection.md) [使用](create-and-manage-vpc-peering-connection.md) [VPC](create-and-manage-vpc-peering-connection.md) [对等连接实现](create-and-manage-vpc-peering-connection.md) [VPC](create-and-manage-vpc-peering-connection.md) [私网互通](create-and-manage-vpc-peering-connection.md) [VPC](vpc-peering-connection-configuration-example.md) [对等连接配置示例](vpc-peering-connection-configuration-example.md) [VPC](vpc-peer-to-peer-connection-monitoring-and-operation.md) [对等连接监控与运维](vpc-peer-to-peer-connection-monitoring-and-operation.md) |
## 2021年07月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| DHCP 选项集 | 更新 | 全网发布。 | [DHCP](user-guide/dhcp-option-set.md) [选项集](user-guide/dhcp-option-set.md) |
## 2021年06月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 流量镜像 | 新增 | VPC 流量镜像功能可以镜像经过弹性网卡 ENI（Elastic Network Interface）且符合筛选条件的报文。例如，您可以复制 VPC 中 ECS 实例的网络流量，并将复制后的网络流量转发给指定的弹性网卡或私网传统型负载均衡 CLB（Classic Load Balancer）实例。该功能可用于内容检查、威胁监控和问题排查等场景。 | [流量镜像](traffic-mirroring-overview.md) [创建和管理流量镜像](create-and-manage-traffic-mirror-sources.md) |
| 网络 ACL | 更新 | 全网发布。 | [网络](network-acl-overview.md) [ACL](network-acl-overview.md) |
## 2021年05月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 共享 VPC | 新增 | 支持多个账号在一个集中管理、共享的 VPC 内创建云资源。 | [共享](vpc-sharing.md) [VPC](vpc-sharing.md) |
## 2021年03月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 专有网络 | 新增 | VPC 高级功能支持 VPC 粒度的 ECS 规格限制检查。 |  |
## 2021年01月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 高可用虚拟 IP | 新增 | 高可用虚拟 IP 支持绑定弹性网卡。 | [绑定弹性网卡](highly-available-virtual-ip-address-havip.md) |
## 2020年09月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 专有网络 | 新增 | 新增开通地域。 | [创建和管理专有网络](user-guide/create-and-manage-a-vpc.md) |
## 2020年08月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 网络 ACL | 新增 | 网络 ACL（Network Access Control List）是专有网络 VPC 中的网络访问控制功能。您可以自定义设置网络 ACL 规则，并将网络 ACL 与交换机绑定，实现对交换机中云服务器 ECS 实例流量的访问控制。 | [网络](network-acl-overview.md) [ACL](network-acl-overview.md) [典型应用](typical-applications.md) [创建和管理网络](work-with-network-acls.md) [ACL](work-with-network-acls.md) [使用示例](examples.md) |
## 2019年12月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 专有网络 | 新增 | 支持为 VPC 添加附加 IPv4 网段和 IPv6 网段。 | [创建和管理专有网络](user-guide/create-and-manage-a-vpc.md) |
## 2019年01月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 流日志 | 更新 | 创建流日志时支持开启日志库分析报表功能。 | [创建和管理流日志](user-guide/create-and-manage-flow-log.md) |
## 2018年12月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 交换机 | 更新 | 专有网络控制台交换机列表支持按照可用区查询交换机。 | [创建和管理交换机](user-guide/create-and-manage-vswitch.md) |
| 流日志 | 新增 | 专有网络 VPC 提供流日志功能，可以记录 VPC 网络中弹性网卡 ENI（Elastic Network Interface）传入和传出的流量信息，帮助您检查访问控制规则、监控网络流量和排查网络故障。 | [流日志](vpc-flow-logs.md) [流日志计费说明](user-guide/billing-of-flow-logs.md) [创建和管理流日志](user-guide/create-and-manage-flow-log.md) [使用示例](user-guide/use-cases-for-vpc-flow-logs.md) |
## 2018年09月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 路由表 | 新增 | 在 VPC 内创建自定义路由表，然后将其和交换机绑定来控制该交换机的路由，称之为子网路由。使用子网路由可以更灵活地管理网络。 | [创建和管理路由表](user-guide/create-and-manage-route-table.md) |
| 路由表 | 新增 | 自定义路由的下一跳支持指定弹性网卡。 | [创建和管理路由表](user-guide/create-and-manage-route-table.md) |
## 2018年08月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 专有网络 | 新增 | 专有网络为免费的基础产品，为所有阿里云用户默认开通专有网络服务。 | [创建和管理专有网络](user-guide/create-and-manage-a-vpc.md) |
## 2018年03月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 专有网络 | 更新 | VPC 数量配额由每账号限制调整为每地域限制。 | [管理配额](manage-quotas.md) |
## 2017年07月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| ClassicLink 功能 | 新增 | 专有网络 VPC（Virtual Private Cloud）提供 ClassicLink 功能，使经典网络的 ECS 实例可以和专有网络中的云资源通过内网互通。 | [使用](using-classiclink.md) [ClassicLink](using-classiclink.md) [连通经典网络与](using-classiclink.md) [VPC](using-classiclink.md) |
## 2017年06月
| 功能名称 | 变更类型 | 功能概述 | 相关链接 |
| --- | --- | --- | --- |
| 交换机 | 更新 | 支持调用 API 查看指定地域下所有的交换机实例信息。 | [专有网络和交换机](user-guide/overview-of-vpcs-and-vswitches.md) |
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
