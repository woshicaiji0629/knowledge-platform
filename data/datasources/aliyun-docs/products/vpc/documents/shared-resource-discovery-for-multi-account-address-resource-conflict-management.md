# 地址资源管理-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/shared-resource-discovery-for-multi-account-address-resource-conflict-management

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/vpc/documents/vpc-user-guide.md)

- [开发参考](products/vpc/documents/developer-reference.md)

- [产品计费](products/vpc/documents/product-billing.md)

- [常见问题](products/vpc/documents/troubleshooting.md)

- [动态与公告](products/vpc/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 地址资源管理

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在[地址统一规划](products/vpc/documents/address-planning.md)的基础上，IPAM 支持地址资源管理与资源监控：

- 

从地址池分配资源：基于已划分的地址池，为 VPC 分配符合业务规则的 IP 地址，实现企业内部地址的统一分配。

- 

发现全局地址资源：使用资源发现统一发现生效地域内的资源，查看地址利用率和重叠情况。

- 

多账号统一管理：结合资源目录，通过指定 IPAM 的委派管理员启用 IPAM 可信服务，统一管理成员账号的 IP 地址资源。

- 

资源监控：使用 IP 地址监控功能，实现更有效的资源规划与分配，保障网络的稳定性与安全性。

## 从规划的地址池中分配地址

地址规划时，支持将顶级池已规划的CIDR[分配给子地址池](products/vpc/documents/address-planning.md)。还支持：

- 

VPC 网段分配：为 VPC 分配主网段或附加网段时，IPAM 确保分配的网段不重叠，避免VPC互连时出现地址冲突。

- 

混合云/多云地址预留：创建自定义分配预留本地数据中心/其他云厂商的业务地址段，确保不会分配给云上资源，避免连接时发生冲突。

网络管理员将规划的[IPAM](products/vpc/documents/address-planning.md)[地址池共享](products/vpc/documents/address-planning.md)给业务账号（地址池使用者）后，业务账号可以使用共享地址池，为VPC分配地址或创建自定义分配。

### 控制台

请确保已[创建](products/vpc/documents/address-planning.md)[IPAM](products/vpc/documents/address-planning.md)[和](products/vpc/documents/address-planning.md)[IPAM](products/vpc/documents/address-planning.md)[地址池](products/vpc/documents/address-planning.md)。

为 VPC 分配网段

- 

结合 IPAM 创建 VPC：

- 

前往专有网络控制台的[创建专有网络](https://vpc.console.aliyun.com/vpc/cn-hangzhou/vpcs/new)页面。

- 

使用IPAM 分配的 IPv4 地址段，选择IPv4地址池并配置掩码，系统会默认分配指定掩码范围内第一个可用的CIDR，可以在地址池预置CIDR内调整分配的IPv4网段。

- 

需开启IPv6时，可以使用IPAM 分配的 IPv6 地址段，选择IPv6地址池并配置地址掩码或指定CIDR。

- 

为已有 VPC 添加附加网段：

- 

添加IPv4网段：在目标VPC详情页的网段管理页签，单击添加附加IPv4网段，使用IPAM 分配的 IPv4 地址段，选择IPv4地址池并配置掩码。系统会默认分配指定掩码范围内第一个可用的CIDR。

- 

添加IPv6网段：VPC未开启IPv6时，单击开通IPv6；已开启时，单击添加IPv6网段。使用IPAM 分配的 IPv6 地址段，选择IPv6地址池并配置地址掩码或指定CIDR。

创建自定义分配

创建自定义分配前，需确保目标地址池已[预置](products/vpc/documents/address-planning.md)[CIDR](products/vpc/documents/address-planning.md)。

- 

前往[IPAM](https://ipam.console.aliyun.com/cn-hangzhou/pool)[控制台 - IPAM](https://ipam.console.aliyun.com/cn-hangzhou/pool)[地址池](https://ipam.console.aliyun.com/cn-hangzhou/pool)，在页面上方选择目标地址池所在的地域。

- 

单击目标地址池实例ID或操作列的管理，在分配页签，单击创建自定义分配，预留的地址段不会分配给云上资源。

- 

输入CIDR或单击已预置CIDR的可分配区域，支持添加多个CIDR。

释放地址分配

前往目标地址池详情页的分配页签，在目标分配的操作列单击释放。

- 

支持释放专有网络、自定义分配类型的分配。

- 

释放专有网络类型的分配时，仅解除VPC与地址池的分配关系，不会删除VPC。

### API

结合 IPAM 创建 VPC

- 

分配IPv4网段：调用[CreateVpc](products/vpc/documents/developer-reference/api-vpc-2016-04-28-createvpc.md)时传入Ipv4IpamPoolId来指定IPAM地址池，同时传入Ipv4CidrMask来指定掩码从IPAM地址池中分配地址作为新建VPC的IPv4网段。也可以传入CidrBlock来指定VPC使用的网段，而不是通过指定掩码自动分配网段。

- 

分配IPv6网段：在分配IPv4网段的同时，传入Ipv6IpamPoolId和Ipv6CidrMask，将从指定的IPv6地址池中为VPC分配IPv6网段。

为已有 VPC 添加附加网段

- 

添加IPv4网段：调用[AssociateVpcCidrBlock](products/vpc/documents/developer-reference/api-vpc-2016-04-28-associatevpccidrblock.md)，传入IpamPoolId指定IPAM地址池，同时传入SecondaryCidrMask或SecondaryCidrBlock。

- 

添加IPv6网段：调用[AssociateVpcCidrBlock](products/vpc/documents/developer-reference/api-vpc-2016-04-28-associatevpccidrblock.md)，传入IpamPoolId指定IPAM地址池，同时传入Ipv6CidrMask或IPv6CidrBlock。

创建自定义分配

调用[CreateIpamPoolAllocation](products/vpc/documents/developer-reference/api-vpcipam-2023-02-28-createipampoolallocation.md)从IPAM地址池创建自定义分配，预留指定地址段。

释放分配

调用[DeleteIpamPoolAllocation](products/vpc/documents/developer-reference/api-vpcipam-2023-02-28-deleteipampoolallocation.md)释放IPAM地址池的地址分配。

### Terraform

Terraform当前暂不支持结合IPAM为VPC分配IPv6网段。Resources：[alicloud_vpc](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc)、[alicloud_vpc_ipv4_cidr_block](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_ipv4_cidr_block)、[alicloud_vpc_ipam_ipam_pool_allocation](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_ipam_ipam_pool_allocation)# 指定IPAM地址池所在的地域 provider "alicloud" { region = "cn-hangzhou" } # 指定IPAM地址池的ID variable "ipam_pool_id" { default = "ipam-pool-bp10******" # 修改为IPAM地址池的实际ID } # 创建VPC,为VPC分配主网段 resource "alicloud_vpc" "example_ipam_vpc" { vpc_name = "example_ipam_vpc_name" ipv4_ipam_pool_id = var.ipam_pool_id # 指定IPAM地址池的ID ipv4_cidr_mask = 24 # IPv4网络掩码 } # 为 VPC 分配附加网段 resource "alicloud_vpc_ipv4_cidr_block" "example_secondary_cidr_block" { vpc_id = alicloud_vpc.example_ipam_vpc.id #指定VPC的ID ipv4_ipam_pool_id = var.ipam_pool_id # 指定IPAM地址池的ID secondary_cidr_mask = 20 # IPv4网络掩码 } # 创建自定义分配 resource "alicloud_vpc_ipam_ipam_pool_allocation" "example_ipam_pool_allocation" { ipam_pool_allocation_name = "example_ipam_pool_allocation_name" ipam_pool_id = var.ipam_pool_id # 指定IPAM地址池的ID cidr = "10.0.160.0/22" #预留指定的CIDR }

### 限制从IPAM地址池为VPC分配网段

多账号企业中，各业务账号独立创建 VPC 时若随意分配私网网段，VPC互连时易因网段冲突无法连通。使用管理账号创建[管控策略](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/control-policy-overview#DAS)，与资源夹或成员绑定，限制业务账号只能从[共享的](products/vpc/documents/address-planning.md)[IPAM](products/vpc/documents/address-planning.md)[地址池](products/vpc/documents/address-planning.md)中为 VPC 分配网段。IPAM 确保分配的网段不重叠，避免VPC互连时出现地址冲突。

管控策略对所有资源目录成员中的RAM用户和RAM角色生效，但对成员的根用户不生效。同时，资源目录的管理账号位于资源目录外部，不归属于资源目录，所以管控策略对管理账号内的所有身份也不生效。

管控策略一：限定用户从地址池创建VPC和为VPC添加附加网段

{ "Statement": [ { "Action": [ "vpc:CreateVpc", "vpc:AssociateVpcCidrBlock" ], "Resource": "*", "Effect": "Deny", "Condition": { "Null": { "vpc:Ipv4IpamPoolId": "true" } } } ], "Version": "1" }

管控策略二：限定用户从特定地址池创建VPC

用户需要选择与"vpc:Ipv4IpamPoolId"的设定值一致的IPAM地址池，才能够成功创建VPC。

{ "Statement": [ { "Action": [ "vpc:CreateVpc" ], "Resource": "*", "Effect": "Deny", "Condition": { "StringNotEquals": { "vpc:Ipv4IpamPoolId": "ipam-pool-0123456789abcdefg" } } }, { "Action": [ "vpc:CreateVpc" ], "Resource": "*", "Effect": "Deny", "Condition": { "Null": { "vpc:Ipv4IpamPoolId": "true" } } } ], "Version": "1" }

管控策略三：限定用户使用特定地址池创建VPC和为VPC添加附加网段

- 

创建VPC时，选择与"vpc:Ipv4IpamPoolId"的设定值一致的IPAM地址池；

- 

添加附加网段时，选择IPAM 分配的 IPv4 地址段，并使用与"vpc:Ipv4IpamPoolId"的设定值一致的IPAM地址池。

{ "Statement": [ { "Action": [ "vpc:CreateVpc", "vpc:AssociateVpcCidrBlock" ], "Resource": "*", "Effect": "Deny", "Condition": { "ForAllValues:StringNotLikeIfExists": { "vpc:Ipv4IpamPoolId": "ipam-pool-0123456789abcdefg" } } } ], "Version": "1" }

## 使用资源发现查看地址使用情况

使用规划的IPAM地址池分配地址，可以确保为VPC分配符合业务规则的网段。针对存量VPC和交换机资源，以及独立于 IPAM 新建的VPC，可以使用资源发现查看全量VPC和交换机地址段信息。

结合IPAM创建的VPC管理状态为托管，而存量资源和未结合IPAM新建资源管理状态为未托管。符合规则、被导入到地址池的资源，管理状态会转化为托管。

### 使用资源发现纳管地址

资源发现会持续查找并跟踪生效地域内VPC和交换机网段的IP利用率。关联 IPAM 后，IPAM 统一管理被发现的地址段。

1、默认资源发现的生效地域与IPAM保持一致，无法修改。2、资源发现更新频率为5分钟。

- 

创建 IPAM 时，系统创建默认资源发现并与 IPAM 关联。符合以下规则的 VPC 网段会被自动导入到对应地址池进行统一管理。规则如下：

- 

仅导入在地址池预置 CIDR 范围内且未分配的地址段。

- 

仅导入到默认作用范围下开启自动导入发现的资源的地址池。

- 

发现的多个 CIDR 存在重叠关系时，IPAM 仅导入范围最大的 CIDR。

- 

发现多个相同的 CIDR 时，IPAM 将随机导入其中一个。

- 

未创建IPAM时，可创建自定义资源发现，跟踪VPC和交换机网段的IP使用率。在托管地域创建IPAM后，将自动转换为默认资源发现。

### 控制台

创建资源发现

- 

创建 IPAM 时，系统会创建默认资源发现并与IPAM关联。

- 

未创建 IPAM 时，创建自定义资源发现。

- 

前往[IPAM 控制台 - 资源发现](https://ipam.console.aliyun.com/cn-hangzhou/resource)，在页面上方选择创建资源发现的地域（即资源发现的托管地域），单击创建资源发现。

- 

可以在托管地域的基础上增加其他生效地域，资源发现会持续查找生效地域内的VPC和交换机网段。

- 

创建完成后，也可以添加/删除生效地域，但包含的托管地域无法删除。

- 

创建完成后，可以在资源发现详情页的已发现资源页签下查看生效地域内VPC和交换机网段的IP使用情况。

删除资源发现

- 

默认资源发现：只能通过[删除 IPAM](products/vpc/documents/address-planning.md)，来删除默认创建的资源发现。

- 

自定义资源发现：单击自定义资源发现操作列的删除。

### API

未创建 IPAM 时：

- 

调用[CreateIpamResourceDiscovery](products/vpc/documents/developer-reference/api-vpcipam-2023-02-28-createipamresourcediscovery.md)创建自定义资源发现。

- 

调用[DeleteIpamResourceDiscovery](products/vpc/documents/developer-reference/api-vpcipam-2023-02-28-deleteipamresourcediscovery.md)删除自定义资源发现。

### Terraform

未创建 IPAM 时，可以创建自定义资源发现。Resources：[alicloud_vpc_ipam_ipam_resource_discovery](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_ipam_ipam_resource_discovery)# 指定未创建IPAM、可创建自定义资源发现的地域 provider "alicloud" { region = "cn-shanghai" } resource "alicloud_vpc_ipam_ipam_resource_discovery" "example_ipam_resource_discovery" { operating_region_list = ["cn-shanghai"] # 指定IPAM资源发现的生效地域 ipam_resource_discovery_name = "example_ipam_resource_discovery_name" }

### 共享资源发现统一管理地址使用

业务账号使用非规划网段创建资源容易引发地址冲突。网络管理员可以关联IPAM和业务账号共享的资源发现，统一管理多账号下的资源，解决地址冲突。

默认资源发现和自定义资源发现均支持共享。

资源发现所有者和使用者的操作权限

| 功能 | 资源所有者（本例中的业务账号） | 资源使用者（本例中的网络管理员） |
| --- | --- | --- |
| 关联资源发现和 IPAM | 支持 | 支持 |
| 解除资源发现和 IPAM 的关联 | 支持 | 支持 |
| 修改资源发现 | 支持 | 仅支持修改资源发现的名称、描述和所属资源组 资源所有者和资源使用者可各自独立设置资源发现的名称/描述/资源组，默认保留资源所有者设置的名称与描述。 |
| 删除资源发现 | 取消共享后，支持删除 | 不支持 |
| 查询资源发现关联的地址资源 | 支持 | 支持 |
| 查询资源发现关联的账号 | 支持 | 支持 |


共享资源发现的生效地域和网络管理员的IPAM生效地域允许存在不一致，但托管地域（即创建地域）必须保持一致。生效地域存在不一致时：

- 

资源所有者（即本例中的业务账号）和网络管理员可以管理和查看资源发现的生效地域内的全部资源。

- 

网络管理员将资源发现与IPAM关联后，只能管理IPAM生效地域内的资源。

### 控制台

此处仅介绍将交换机共享给任意账户的方式。针对资源目录方式，请参考[仅在资源目录内共享资源](https://help.aliyun.com/zh/resource-management/resource-sharing/getting-started/share-resources-with-objects-in-a-resource-directory)。

共享资源发现

- 

业务账号将[创建的资源发现](products/vpc/documents/use-ipam-to-create-a-vpc.md)共享给网络管理员：

- 

前往[IPAM 控制台 - 资源发现](https://ipam.console.aliyun.com/cn-hangzhou/resource)，在页面上方选择目标资源发现所在地域。单击目标资源发现实例ID或操作列的管理，在共享管理页签，单击创建资源共享。

- 

在创建共享单元页面，按照步骤指引完成资源共享配置。

- 

将资源修改为IPAM资源发现，并选择要共享的IPAM资源发现。

- 

对于IPAM资源发现，关联权限为AliyunRSDefaultPermissionIpamResourceDiscovery。

- 

资源使用者范围选择允许共享给任意账号，添加方式选择手动添加，使用者ID输入地址池使用者的[阿里云账号](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)[ID](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)，并点击添加。

- 

检查无误后，在页面底部单击确定。

- 

登录网络管理员账号，接受共享邀请：

- 

前往资源管理控制台的[资源共享-共享给我](https://resourcemanager.console.aliyun.com/resource-shares/cn-hangzhou/shared)页面。

- 

在顶部菜单栏左上处，选择共享资源所在的地域，再单击目标共享单元状态列的接受。

- 

共享成功后，网络管理员可分别查看各业务账号下的资源与地址利用率等信息。

- 

网络管理员将共享的资源发现与托管地域一致的IPAM关联：

- 

前往[IPAM 控制台 - IPAM](https://ipam.console.aliyun.com/cn-hangzhou/ipam)，在页面上方选择目标IPAM所在地域。单击目标IPAM实例ID或操作列的管理，在关联资源发现页签，单击关联资源发现，选择业务账号共享的资源发现。

- 

关联完成后，网络管理员可统一管理IPAM生效地域内的资源，在IPAM作用范围的资源管理页签查看地址重叠与利用率等信息。

取消关联 IPAM 与资源发现只有主动建立的关联关系可以被取消。创建IPAM时默认创建并关联的资源发现，无法取消关联。

单击目标IPAM的关联资源发现页签下，单击目标资源发现操作列的解除关联。取消关联后，IPAM将无法管理资源发现查找到的地址资源。

取消共享资源发现

使用业务账号，在资源发现详情页的共享管理页签下，单击目标共享单元进入详情页，选择删除共享单元。

即使网络管理员已经将资源发现与IPAM关联，业务账号也可以取消共享。取消后，关联关系将被自动删除。

### API

共享资源发现

- 

将资源发现共享给任意账户

- 

使用业务账号的身份凭证，调用[CreateResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-createresourceshare)创建共享单元，并确保将AllowExternalTargets参数设为True。

- 

使用网络管理员的身份凭证，先调用[ListResourceShareInvitations](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-listresourceshareinvitations)查询收到的资源共享邀请，再调用[AcceptResourceShareInvitation](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-acceptresourceshareinvitation)接受共享。

- 

仅在资源目录内共享资源发现

- 

使用资源目录管理账号的身份凭证，调用[EnableSharingWithResourceDirectory](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-enablesharingwithresourcedirectory)启用资源目录组织共享。

- 

使用业务账号的身份凭证，调用[CreateResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-createresourceshare)创建共享单元，并确保将AllowExternalTargets参数设为True。

- 

使用业务账号的身份凭证，调用[DeleteResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-deleteresourceshare)删除共享单元，取消共享资源发现。

关联资源发现与IPAM

- 

调用[AssociateIpamResourceDiscovery](products/vpc/documents/developer-reference/api-vpcipam-2023-02-28-associateipamresourcediscovery.md)关联资源发现和IPAM。

- 

调用[DissociateIpamResourceDiscovery](products/vpc/documents/developer-reference/api-vpcipam-2023-02-28-dissociateipamresourcediscovery.md)解除资源发现和IPAM的关联。

### Terraform

Terraform暂不支持共享资源发现。

### 查看已发现资源的IP信息

资源发现支持查看已发现的VPC和交换机下所有已使用IPv4私网IP详细信息，包括IP地址、资源ID、资源归属地域、云服务类型等，帮助您全面掌握网络中的IP地址使用情况。

仅支持查询已被资源发现纳管的VPC和交换机下的IP信息。

- 

支持按VPC ID、交换机ID、CIDR进行筛选，其中CIDR支持任意合法IPv4地址段，包括/32精确匹配单个IP地址，且需要与VPC ID或交换机ID组合使用。

- 

支持的查询组合包括：仅VPC ID、仅交换机ID、VPC ID + CIDR、交换机ID + CIDR、VPC ID + 交换机ID + CIDR。

控制台

前往[IPAM](https://ipam.console.aliyun.com/cn-hangzhou/resource)[控制台 - 资源发现](https://ipam.console.aliyun.com/cn-hangzhou/resource)，单击目标资源发现实例ID进入详情页。

- 

在已发现资源页签下，展开VPC或交换机资源树，单击目标资源IP资源信息列的查看，系统将自动跳转到IP资源信息页签并预设过滤条件。

- 

您也可以直接单击IP资源信息页签，手动输入筛选条件查询。

API

调用[ListIpamDiscoveredIpAddresses](products/vpc/documents/developer-reference/api-vpcipam-2023-02-28-listipamdiscoveredipaddresses.md)，指定VpcId、VSwitchId、Cidr参数查询已发现资源的IP地址详细信息。

## 多账号地址资源管理

当企业已使用资源目录搭建多账号体系时，资源目录的管理账号可设置 IPAM[委派管理员](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/manage-a-delegated-administrator-account)。IPAM 委派管理员可统一查看企业多账号下的IP地址资源使用信息。

### 适用范围

IPAM 可信服务只支持资源目录的 IPAM 委派管理员操作，不允许组织管理员或其他成员进行操作。

- 

添加委派：资源目录仅支持添加一个 IPAM 可信服务委派管理员，且委派管理员账号只能是资源目录的成员，不能是组织管理账号。

- 

管理成员：

- 

IPAM 委派管理员添加成员后，将启用所在资源目录的 IPAM 可信服务；移除全部成员时，将关闭 IPAM 可信服务。

- 

IPAM 委派管理员只能选定一个地域的 IPAM 实例管理资源目录成员，如果想更换其他地域的 IPAM 实例进行多账号管理，需要将当前地域的 IPAM 管理成员全部移除后，在其他地域的 IPAM 多账号管理页面添加成员。

- 

不允许 IPAM 委派管理员将资源目录根节点或资源目录根资源夹作为成员进行管理。

- 

不允许 IPAM 所管理的成员账号将自己的资源发现共享给 IPAM 委派管理员。

- 

当 IPAM 可信服务管理的成员账号和配额相等时，如果资源目录中纳管的资源夹成员增加成员账号，IPAM 可信服务的管理范围将不包括超出配额的成员账号。

- 

取消委派：当 IPAM 委派管理员移除全部纳管成员时，即可删除 IPAM 委派管理员账号，或取消委派。

### 控制台

- 

确保[已开通资源目录并创建多账号体系](https://help.aliyun.com/zh/resource-management/resource-directory/getting-started/use-a-resource-directory-to-quickly-establish-a-structure-for-the-accounts-and-resources-of-an-enterprise)。

- 

使用资源目录的管理账号，前往[资源管理-可信服务列表页](https://resourcemanager.console.aliyun.com/resource-directory/services)，单击IP地址管理操作列的管理，在委派管理员账号区域，添加资源目录的成员为 IPAM 委派管理员。

- 

使用 IPAM 委派管理员账号[创建 IPAM](products/vpc/documents/address-planning.md)后，可前往[IPAM - 多账号管理页面](https://ipam.console.aliyun.com/cn-hangzhou/member)添加成员。添加后，委派管理员即可使用资源发现查看 IPAM 生效地域中所有纳管成员账号下的 IP 地址使用情况。

资源发现更新频率为 5 分钟。IPAM 委派管理员纳管成员时，IPAM 会给纳管成员所包含的成员账号创建[服务关联角色](products/ram/documents/user-guide/service-linked-roles.md)，并配置以下权限策略。

为服务关联角色配置的权限策略

{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "ecs:DescribeNetworkInterfaces", "ecs:DescribeSecurityGroups", "vpc:DescribeEipAddresses", "vpc:DescribeHaVips", "vpc:DescribeIpv6Addresses", "vpc:DescribeVpcs", "vpc:DescribeVSwitches" ], "Resource": "*" }, { "Action": "ram:DeleteServiceLinkedRole", "Resource": "*", "Effect": "Allow", "Condition": { "StringEquals": { "ram:ServiceName": "vpcipam.vpc.aliyuncs.com" } } } ] }

### API

- 

调用[EnableResourceDirectory](https://help.aliyun.com/zh/resource-management/resource-directory/developer-reference/api-resourcedirectorymaster-2022-04-19-enableresourcedirectory)开通资源目录。结合[CreateFolder](https://help.aliyun.com/zh/resource-management/resource-directory/developer-reference/api-resourcedirectorymaster-2022-04-19-createfolder)和[CreateResourceAccount](https://help.aliyun.com/zh/resource-management/resource-directory/developer-reference/api-resourcedirectorymaster-2022-04-19-createresourceaccount)创建多账号体系。

- 

资源目录的管理账号，调用[RegisterDelegatedAdministrator](https://help.aliyun.com/zh/resource-management/resource-directory/developer-reference/api-resourcedirectorymaster-2022-04-19-registerdelegatedadministrator)设置 IPAM 委派管理员。

- 

IPAM 委派管理员调用[OpenVpcIpamService](products/vpc/documents/developer-reference/api-vpcipam-2023-02-28-openvpcipamservice.md)开通 IPAM，并调用[CreateIpam](products/vpc/documents/developer-reference/api-vpcipam-2023-02-28-createipam.md)创建IPAM。

- 

IPAM 委派管理员调用[AddIpamMembers](products/vpc/documents/developer-reference/api-vpcipam-2023-02-28-addipammembers.md)添加成员，统一查看 IPAM 生效地域中所有纳管成员账号下的 IP 地址资源使用信息。

## 资源监控

### 监控地址利用率

监控地址利用率，便于对高利用率资源及时进行扩容。

- 

监控地址池的地址利用率：前往[IPAM](https://ipam.console.aliyun.com/cn-hangzhou/pool)[控制台 - IPAM](https://ipam.console.aliyun.com/cn-hangzhou/pool)[地址池](https://ipam.console.aliyun.com/cn-hangzhou/pool)，单击目标地址池ID。

- 

详细信息页签下，可查看地址池的可用 IP 数与分配给资源和子地址池的 IP 数。若目标地址池为子地址池，可同时查看本池与源地址池的地址利用率。

- 

IP空间可视化和分配页签下，可查看地址池的具体分配情况。

- 

监控 VPC 和交换机的地址利用率：

- 

前往[IPAM 控制台 - 资源发现](https://ipam.console.aliyun.com/cn-hangzhou/resource)，单击目标资源发现ID，可查看生效地域下全部 VPC 和交换机的 CIDR 和 IP 使用情况。

- 

前往[IPAM 控制台 - IPAM](https://ipam.console.aliyun.com/cn-hangzhou/scope)[作用范围](https://ipam.console.aliyun.com/cn-hangzhou/scope)，单击目标作用范围ID。

- 

资源管理页签下，可查看该作用范围内 VPC 和交换机的 CIDR 和地址利用率。单击目标 VPC 或交换机 ID，可查看 IP 使用情况。

- 

监控图表页签下，可以从时间维度以折线图形式监控该作用范围内 VPC 和交换机的地址利用率。

### 监控地址重叠情况

监控地址重叠，可以主动发现并解决网络连接中的地址冲突，确保实现网络互连时不会引起访问冲突。

前往[IPAM 控制台 - IPAM](https://ipam.console.aliyun.com/cn-hangzhou/scope)[作用范围](https://ipam.console.aliyun.com/cn-hangzhou/scope)，单击目标作用范围ID。

- 

资源管理页签下，可查看该作用范围内 VPC 和交换机网段的重叠情况。存在网段重叠时，可以单击重叠状态(重叠)>查看，查看与当前资源存在冲突的具体实例。

- 

监控图表页签下，可以从时间维度以折线图形式监控该作用范围内 CIDR 的重叠数量。

### 监控地址段管理状态和合规性

前往[IPAM 控制台 - IPAM](https://ipam.console.aliyun.com/cn-hangzhou/scope)[作用范围](https://ipam.console.aliyun.com/cn-hangzhou/scope)，单击目标作用范围ID，可以在概览、资源管理、监控图表页签，查看资源的 CIDR 是否通过 IPAM 地址池分配（即是否托管）以及是否符合 IPAM 地址池的分配规则（即是否合规）。

## 更多信息

### 计费说明

IP地址管理（IPAM）功能正在进行公测，公测期间免费使用。

### 配额限制

| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| ustom_ipam_resource_discovery_quota_per_region | 单地域单账号允许创建的自定义资源发现数量 | 1 个 | 无法提升 |
| resource_share_quota_per_ipam_resource_discovery | 每个资源发现支持创建的共享资源数量 | 100 个 |  |
| shared_ipam_resource_discovery_quota_per_user | 每个用户允许拥有的共享资源发现的数量 | 100 个 |  |
| ipam_resource_directory_member_detail_quota | IPAM 可信服务管理的成员所包括所有成员账号的最大数量 | 1000 个 |  |


[上一篇：地址规划](products/vpc/documents/address-planning.md)[下一篇：结合IPAM规划并创建专有网络](products/vpc/documents/use-ipam-to-create-a-vpc.md)

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
