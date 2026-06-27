# 地址规划-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/address-planning

# 地址规划
使用 IPAM 作用范围和 IPAM 地址池规划可使用的地址段并进行分配，可以避免 CIDR 重叠并降低 IP 地址耗尽的风险。
IPAM 作用范围代表独立的 IP 地址空间。创建不同的作用范围，可以为不同主体创建各自的 IP 地址空间独立管理，不同作用范围可以包含重叠的CIDR块。
在 IPAM 作用范围内，创建 IPAM 地址池并预置 CIDR 后，可以基于地域、部门或业务逐层划分可使用的地址段。
规划的 IPAM 地址池支持共享给多业务账号，业务账号可从中分配地址资源。
## 地址规划设计
### IPAM 地址池的 CIDR 设计
地址池的 CIDR 设计通过将 IP 地址段划分为多个层级（如区域级、部门级或业务线级），实现灵活高效的管理。
逐层规划：先创建大的区域CIDR块，然后进一步细分给不同的部门或业务线，以避免IP地址冲突。这种方法使得网络管理员能够轻松汇总和分配CIDR块，从而简化网络管理和路由配置。
划分逻辑：IPAM地址池分层部署设计不受限于单一方案。可以根据区域、部门、业务线或者产品等多种方式构建多层次、多区域的地址规划方案，配置相应的安全组、网络ACL和防火墙等规则，设计深度不能超过10层。
例如，某公司计划在阿里云上部署多个核心业务，并采用10.0.0.0/8作为云上网络地址空间的总规划范围。业务架构如下：多地域部署、多业务环境部署（各业务包含独立的生产、预发、测试等环境，各环境严格隔离）、部分业务有网络互通需求。可遵照 IPAM 地址池的 CIDR 设计思路，逐层划分地址段并分配。
网络规划设计：
确认规划维度：根据业务架构，确定规划层级为地域、业务线、业务环境。
预留扩展空间：地域（计划使用3个地域、预留5个地域）、业务线（每个地域内6个核心业务线，预留10个）、业务环境（每个业务线包含生产环境、测试环境、开发环境）。
逐层规划 CIDR：
为地域维度划分地址空间：支持8个地域，需划分8个地址段（2^3 = 8）。因此，各地域地址段的网络掩码为/11（/8+ 3）。
分配示例：10.0.0.0/11、10.32.0.0/11、10.64.0.0/11分配给3个使用地域，剩余5个地址段作为预留。
按照上述逻辑，各业务线维度地址段的网段掩码为/15（支持 16 个业务线，/11+ 4）、各业务环境维度地址段的网段掩码为/17（支持 3 个业务环境，/15+2）。
使用 IPAM 实施地址规划：
创建顶级地址池：在默认私网作用范围内创建10.0.0.0/8的顶级地址池。
创建地域地址池：在10.0.0.0/8地址池下，创建代表各个地域的/11子地址池。
创建业务线地址池：在每个地域地址池下，创建代表各个业务线的/15子地址池。
创建业务环境地址池：在每个业务线地址池下，创建用于分配的/17子地址池。这些地址池可共享给业务账号，用于创建 VPC、自定义分配等。
### 独立业务环境
由于收购公司、多租户环境等业务环境需要独立管理或要求更高的隔离性，可以创建多个私有作用范围来管理不同的环境。不同作用范围可以有独立的管理策略和权限设置，且可以包含重叠的CIDR块。但需评估不同环境之间是否有网络互连的需求，重叠的CIDR块可能导致互连的网络发生冲突，需要谨慎规划。
以收购公司场景为例，A公司收购了B公司，两家公司可能有重叠的IP地址范围，需要为两家公司分别创建作用范围，这样即使地址重叠，也不会引起冲突。同时可以通过每个作用范围，了解每家公司的IP地址分配情况，即使IP地址有重叠，也可以利用这些信息设计出合适的网络连接和路由模型，以确保公司被收购后的网络能够有效运行，避免IP地址冲突。
### 混合云组网和多云互联网络设计
当具备混合云组网与多云部署的网络架构时，在IPAM地址池中创建自定义分配CIDR，预留IDC网段、云厂商网段，确保预留的网段不会分配给其他云上资源，从而避免云上VPC和IDC网段、其他云厂商网段冲突。
## 使用IPAM作用范围和地址池进行规划
使用 IPAM 作用范围和 IPAM 地址池，规划可使用的 CIDR 地址段。
创建 IPAM 后，系统默认创建一个公网作用范围和一个私网作用范围，无法删除。
公网作用范围：仅支持分配和使用阿里云默认 IPv6 地址段，用于业务规划以及 IPv6 资源分配。
私网作用范围：支持分配和使用 IPv4 地址段。支持创建不同的私网作用范围，独立管理不同的地址空间。
创建不同的私网作用范围，可以为具有重叠地址范围的不同主体创建各自的 IP 地址空间独立管理，适合于收购公司、多租户环境或者安全隔离场景。
创建 IPAM 地址池，基于地域、部门或业务逐层划分地址段：
将计划管理和使用的 CIDR 地址段预置到顶级池。
不同 IPAM 作用范围的地址池预置的 CIDR 可以重叠。因此，需要评估不同环境之间是否有网络互连的需求。网络互连时，重叠的CIDR块可能会引起访问冲突，需谨慎规划。
同一 IPAM 作用范围内，可以创建多个顶级池，但顶级池预置的 CIDR 不可以重叠。
基于地域或业务，将顶级池已规划的 CIDR 进行划分，创建多个层级的 IPAM 子地址池，确保各环境之间使用不重叠的地址范围，避免冲突。
### 控制台
使用 IPAM 作用范围规划独立的地址空间
前往[IPAM 控制台](https://ipam.console.aliyun.com/cn-hangzhou/ipam)。在顶部菜单栏，选择要创建IPAM的地域（即IPAM托管地域）。
单击创建IPAM，可以在托管地域的基础上增加其他生效地域，IPAM将统一管理生效地域内的地址资源。创建完成后，也可以添加/删除生效地域，但包含的托管地域无法删除。
系统默认创建一个公网作用范围、一个私网作用范围。如需规划其他独立的 IPv4 地址空间，可以在IPAM作用范围页面，单击创建作用范围。
创建 IPAM 地址池规划地址段
前往[IPAM](https://ipam.console.aliyun.com/cn-hangzhou/pool)[控制台 - IPAM](https://ipam.console.aliyun.com/cn-hangzhou/pool)[地址池](https://ipam.console.aliyun.com/cn-hangzhou/pool)，在页面上方选择IPAM的托管地域。单击创建地址池。
归属IPAM作用范围：结合需规划的地址段版本选择。
CIDR范围：
IPAM：创建 IPAM 作用范围中的顶级池。业务首次规划地址段时选择。
IPAM地址池：创建子地址池。使用 IPAM 中另一个池作为源IPAM地址池，从源地址池中选择 CIDR 预置到本地址池。业务需要从已规划地址中继续划分和使用时选择。
IP版本：归属IPAM作用范围决定可规划的地址段类型。
选择公网作用范围时仅支持 IPv6，IPv6网段类型选择分配BGP（多线）。
选择私网作用范围时仅支持 IPv4。
生效地域：资源所属地域与生效地域一致时，才能从地址池中分配地址。
生效地域需在所属 IPAM 生效地域的范围内，且一旦设置不允许修改。
规划IPv6地址段时，必须配置。子地址池将继承源地址池的生效地域。
规划IPv4地址段时，非必须配置。源地址池设置生效地域时，子地址池将继承源地址池的生效地域。如果源地址池未设置，子地址池设置的生效地域需在所属 IPAM 生效地域范围内。
自动导入发现的资源：开启后，IPAM将通过[资源发现](use-ipam-to-create-a-vpc.md)持续查找生效地域内的VPC，将网段在当前地址池范围内且在 IPAM 中未分配的资源纳入地址管理。
该参数仅在设置生效地域后生效，即地址池没有设置生效地域时，无法开启自动导入发现的资源。
如果 IPAM 发现的多个 CIDR 存在重叠关系，IPAM 仅自动导入地址段最大的 CIDR。
如果 IPAM 发现多个相同的 CIDR，IPAM 将只随机导入其中一个。
创建完成后，可以在 IPAM 地址池实例详情页的详细信息页签、实例编辑页面开启/关闭自动导入。
预置CIDR：预置 CIDR 的 IPAM 地址池，才可以从中[为资源分配 CIDR](use-ipam-to-create-a-vpc.md)。
IPv6 顶级池仅能选择地址掩码来预置 1 个 CIDR；IPv4 顶级池仅支持输入地址段，可预置多个 CIDR。
子地址池可通过输入地址段、选择地址掩码或在可视化界面中选择源地址池的可分配部分，预置多个 CIDR。
创建完成后，可以在 IPAM 地址池实例详情页的CIDR页签，预置CIDR。
分配规则：从地址池为资源分配 CIDR 时，掩码范围需在最小到最大网络掩码长度之间。未指定掩码时，使用默认网络掩码长度。
IPv6地址池的最小、默认以及最大网络掩码长度取值范围均为 0 ~ 128，IPv4地址池为0~32。
创建完成后，可以在 IPAM 地址池实例详情页的合规规则页签修改。
已预置 CIDR 的地址池，可以创建该地址池的子地址池、[结合](use-ipam-to-create-a-vpc.md)[IPAM](use-ipam-to-create-a-vpc.md)[规划创建](use-ipam-to-create-a-vpc.md)[VPC](use-ipam-to-create-a-vpc.md)。
取消预置 CIDR
取消前，请确保预置的 CIDR 中没有地址分配给VPC、IPAM 地址池或创建自定义分配。单击目标地址池实例 ID 或在操作列单击管理，在CIDR页签下目标 CIDR的操作列单击取消预置。
删除 IPAM 地址池
删除前，请确保已取消所有的预置CIDR。在目标地址池的操作列或详情页，单击删除。
删除 IPAM 作用范围
系统默认创建的两个作用范围无法删除。在自建作用范围的操作列或详情页单击删除。删除前，请确保已删除该作用范围下的 IPAM 地址池。
删除 IPAM
删除前，请确保已删除IPAM 地址池和自建的作用范围。在目标IPAM的操作列或详情页，单击删除。
### API
使用 IPAM 作用范围规划独立的地址空间
调用[OpenVpcIpamService](developer-reference/api-vpcipam-2023-02-28-openvpcipamservice.md)开通IPAM。
调用[CreateIpam](developer-reference/api-vpcipam-2023-02-28-createipam.md)创建IPAM。
调用[CreateIpamScope](developer-reference/api-vpcipam-2023-02-28-createipamscope.md)创建IPAM私网作用范围。
创建IPAM地址池并预置CIDR
调用[CreateIpamPool](developer-reference/api-vpcipam-2023-02-28-createipampool.md)创建IPAM地址池。
调用[AddIpamPoolCidr](developer-reference/api-vpcipam-2023-02-28-addipampoolcidr.md)为IPAM地址池预置CIDR地址段。
资源清理
调用[DeleteIpamPoolCidr](developer-reference/api-vpcipam-2023-02-28-deleteipampoolcidr.md)删除IPAM地址池预置的CIDR地址段。
调用[DeleteIpamPool](developer-reference/api-vpcipam-2023-02-28-deleteipampool.md)删除IPAM地址池。
调用[DeleteIpamScope](developer-reference/api-vpcipam-2023-02-28-deleteipamscope.md)删除自建的IPAM作用范围。
调用[DeleteIpam](developer-reference/api-vpcipam-2023-02-28-deleteipam.md)删除IPAM。
### Terraform
Resources：[alicloud_vpc_ipam_service](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_ipam_service)、[alicloud_vpc_ipam_ipam](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_ipam_ipam)、[alicloud_vpc_ipam_ipam_scope](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_ipam_ipam_scope)、[alicloud_vpc_ipam_ipam_pool](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_ipam_ipam_pool)、[alicloud_vpc_ipam_ipam_pool_cidr](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_ipam_ipam_pool_cidr)# 指定创建 IPAM 的地域 provider "alicloud" { region = "cn-hangzhou" } # 初次使用，需要开通 IPAM 服务 resource "alicloud_vpc_ipam_service" "example_ipam_service" { } # 创建IPAM resource "alicloud_vpc_ipam_ipam" "example_ipam" { ipam_name = "example_ipam_name" operating_region_list = ["cn-hangzhou"] # 指定IPAM的生效地域 } # 创建IPAM作用范围 resource "alicloud_vpc_ipam_ipam_scope" "example_ipam_scope" { ipam_scope_name = "example_ipam_scope_name" ipam_id = alicloud_vpc_ipam_ipam.example_ipam.id ipam_scope_type = "private" # 私网作用范围 } # 创建IPAM地址池 resource "alicloud_vpc_ipam_ipam_pool" "example_parentIpamPool" { ipam_scope_id = alicloud_vpc_ipam_ipam_scope.example_ipam_scope.id # 指定IPAM地址池的作用范围 ipam_pool_name = "example_parentIpamPool_name" pool_region_id = alicloud_vpc_ipam_ipam.example_ipam.region_id # 指定IPAM地址池的生效地域 ip_version = "IPv4" # 指定IPAM地址池的版本 } # 为IPAM地址池分配CIDR resource "alicloud_vpc_ipam_ipam_pool_cidr" "example_ipamPoolCidr" { cidr = "10.0.0.0/16" # 指定CIDR ipam_pool_id = alicloud_vpc_ipam_ipam_pool.example_parentIpamPool.id # 指定IPAM地址池的ID } # 创建IPAM子地址池 resource "alicloud_vpc_ipam_ipam_pool" "example_childIpamPool" { ipam_pool_name = "example_childIpamPool_name" ipam_scope_id = alicloud_vpc_ipam_ipam_scope.example_ipam_scope.id # 指定IPAM地址池的作用范围 pool_region_id = alicloud_vpc_ipam_ipam.example_ipam.region_id # 指定IPAM地址池的生效地域 source_ipam_pool_id = alicloud_vpc_ipam_ipam_pool.example_parentIpamPool.id # 指定源IPAM地址池的ID ip_version = "IPv4" # 指定IPAM地址池的版本 } # 为IPAM子地址池分配CIDR resource "alicloud_vpc_ipam_ipam_pool_cidr" "example_childIpamPoolCidr" { cidr = "10.0.0.0/24" # 指定CIDR ipam_pool_id = alicloud_vpc_ipam_ipam_pool.example_childIpamPool.id # 指定IPAM地址池的ID }
## 多账号共享规划的地址池
网络管理员可以将创建的地址池共享给业务账号（地址池使用者）。业务账号可以使用共享地址池，为VPC分配地址或创建自定义分配。
共享给任意阿里云主账号：使用者需要接受共享资源的邀请。
在资源目录内共享：使用者无需确认，默认直接接受共享资源的邀请。
地址池所有者和使用者的操作权限
| 功能 | 资源所有者 | 资源使用者 |
| --- | --- | --- |
| 创建 VPC 选择从 IPAM 地址池分配资源 | 支持 | 支持 |
| 从 IPAM 地址池分配 VPC 附加网段 | 支持 | 支持 |
| 删除 IPAM 地址池 | 支持 | 不支持 |
| 修改 IPAM 地址池信息 | 支持 | 支持（仅支持修改名称和描述） |
| 查询 IPAM 地址池 | 支持 | 支持 |
| 查询 IPAM 地址池的 CIDR 信息 | 支持 | 支持 |
| 为 IPAM 地址池预置 CIDR | 支持 | 不支持 |
| 取消预置 CIDR | 支持 | 不支持 |
| 创建自定义分配 | 支持 | 支持 |
| 释放自定义分配 | 支持 | 支持释放使用者创建的自定义分配 |
| 查询自定义分配 | 支持 | 支持 |
| 修改分配规则 | 支持 | 不支持 |
| 开启/关闭自动导入 | 支持 | 不支持 |
| 查询 IPAM 地址池的资源 | 支持 | 不支持 |
### 控制台
此处仅介绍将交换机共享给任意账户的方式。针对资源目录方式，请参考[仅在资源目录内共享资源](https://help.aliyun.com/zh/resource-management/resource-sharing/getting-started/share-resources-with-objects-in-a-resource-directory)。
共享 IPAM 地址池
使用地址池所有者账号，前往[IPAM](https://ipam.console.aliyun.com/cn-hangzhou/pool)[控制台 - IPAM](https://ipam.console.aliyun.com/cn-hangzhou/pool)[地址池](https://ipam.console.aliyun.com/cn-hangzhou/pool)，在页面上方选择目标地址池所在的地域。单击目标地址池实例ID或操作列的管理，在共享管理页签，单击创建资源共享。
在创建共享单元页面，按照步骤指引完成资源共享配置。
将资源修改为IPAM地址池，并选择要共享的IPAM地址池资源。
对于IPAM地址池资源，关联权限为AliyunRSDefaultPermissionIpamPool。
资源使用者范围选择允许共享给任意账号，添加方式选择手动添加，使用者ID输入地址池使用者的[阿里云账号](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)[ID](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)，并点击添加。
检查无误后，在页面底部单击确定。
登录地址池使用者的账号，接受共享邀请：
前往资源管理控制台的[资源共享-共享给我](https://resourcemanager.console.aliyun.com/resource-shares/cn-hangzhou/shared)页面。
在顶部菜单栏左上处，选择共享资源所在的地域，再单击目标共享单元状态列的接受。
共享成功后，地址池使用者可以在IPAM地址池页面共享给我的池页签中查看，可使用该地址池[结合](use-ipam-to-create-a-vpc.md)[IPAM](use-ipam-to-create-a-vpc.md)[规划并创建专有网络](use-ipam-to-create-a-vpc.md)或[结合](use-ipam-to-create-a-vpc.md)[IPAM](use-ipam-to-create-a-vpc.md)[规划并创建专有网络](use-ipam-to-create-a-vpc.md)。
取消共享
使用地址池所有者账号，在IPAM地址池详情页的共享管理页签下，单击目标共享单元进入详情页，选择删除共享单元。
取消共享后，地址池使用者无法再查看该地址池，但使用共享地址池创建的地址分配不受影响。删除创建的VPC时，释放对应的地址池分配。
地址池所有者可以[管理地址池的分配](use-ipam-to-create-a-vpc.md)，包括释放地址池使用者创建的专有网络类型的分配以及自定义分配。
### API
共享 IPAM 地址池
方式一：共享给任意账户
使用地址池所有者的身份凭证，调用[CreateResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-createresourceshare)创建共享单元，并确保将AllowExternalTargets参数设为True。
使用地址池使用者的身份凭证，先调用[ListResourceShareInvitations](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-listresourceshareinvitations)查询收到的资源共享邀请，再调用[AcceptResourceShareInvitation](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-acceptresourceshareinvitation)接受共享。
方式二：仅在资源目录内共享
使用资源目录管理账号的身份凭证，调用[EnableSharingWithResourceDirectory](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-enablesharingwithresourcedirectory)启用资源目录组织共享。
使用地址池使用者的身份凭证，调用[CreateResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-createresourceshare)创建共享单元，并确保将AllowExternalTargets参数设为True。
取消共享
使用地址池所有者的身份凭证，调用[DeleteResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-deleteresourceshare)删除共享单元。
### Terraform
Terraform暂不支持共享IPAM地址池。
## 更多信息
### 计费说明
IP地址管理（IPAM）功能正在进行公测，公测期间免费使用。
### 配额限制
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| ipam_quota_per_region | 每个用户在每个地域支持创建的 IPAM 数量 | 1 个 | 无法提升 |
| ipam_scope_quota_per_ipam | 每个 IPAM 支持创建的 IPAM 作用范围数量 | 5 个 |  |
| ipam_pool_quota_depth | 每个地址池最大深度 | 10 |  |
| ipam_cidr_quota_per_ipam_pool | 每个地址池中允许预置的 CIDR 的数量 | 50 个 |  |
| ipam_sub_pool_quota_per_ipam_pool | 每个地址池允许创建的子地址池的数量 | 50 个 |  |
| ipam_pool_quota_per_scope | 每个 IPAM 私有范围支持创建的地址池的数量 | 500 个 |  |
| resource_share_quota_per_ipam_pool | 每个 IPAM 地址池允许创建的共享资源数量 | 100 个 |  |
| shared_ipam_pool_quota_per_user | 每个用户允许拥有的共享地址池的数量 | 100 个 |  |
| ipam_public_ipv6_top_pool_quota_per_region_isp | 每个用户在每个地域支持创建的每种 ISP 类型的公网 IPv6 IPAM 顶级地址池数量 | 1 个 |  |
| ipam_cidr_quota_per_public_ipv6_top_pool | 每个用户在每个地域支持为公网 IPv6 IPAM 顶级地址池预置的 CIDR 数量 | 1 个 |  |
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
