# VPC路由表-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/vpc-route-table/

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

# VPC路由表

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

专有网络（VPC）中的网络流量，其转发路径由路由表决定。可将路由表视为网络中的交通指示牌，通过在其中配置路由条目，引导数据包从源头（如ECS实例）流向目的地。

## 功能说明

### 路由表

创建VPC时，系统自动创建一张系统路由表，默认绑定VPC内所有交换机，控制VPC的流量。

当VPC内不同ECS访问相同的目标网段时，若需要通过不同的网络路径转发流量，可以使用自定义路由表。通过将ECS实例分别部署在不同的交换机下，并为每个交换机单独绑定自定义路由表，可实现精细化的流量控制。

当需要对进入VPC的公网流量通过自建防火墙防护时，可以使用网关路由表（绑定边界网关的自定义路由表）。通过将网关路由表与IPv4/IPv6网关绑定，可将进入VPC的公网流量定向到自建防火墙，实现对流量的统一过滤、审计和安全策略管控。

每种路由表的具体区别：

| 对比项 | 系统路由表 | 自定义路由表 |  |
| --- | --- | --- | --- |
| 绑定对象 | 交换机 | 交换机 | IPv4/IPv6 网关 |
| 示意图 |  |  |  |
| 使用场景 | 默认绑定所有新建的交换机， 统一控制交换机的流量 | 单独绑定目标交换机， 控制目标交换机流量流向 | 绑定 IPv4/IPv6 网关，进行 入方向公网流量安全引流 |
| 创建方式 | 创建 VPC 时， 系统自动创建 | 由您手动创建 ，创建路由表时选择交换机类型 | 由您手动创建 ，创建路由表时选择边界网关类型 |
| 是否可删除 | 无法删除 | 可删除， 需要先与交换机解绑 | 可删除，需要先与 IPv4/IPv6 网关解绑 |
| 配额 | 一个 VPC 只有一个系统路由表 | 一个 VPC 默认支持创建 9 个绑定交换机的自定义路由表，可 [提升配额](https://vpc.console.aliyun.com/quota) | 一个 VPC 只能创建一个绑定 IPv4/IPv6 网关的路由表 |


每个交换机必须绑定路由表，且只能绑定1张路由表。1张路由表可绑定多个交换机。

### 路由条目

路由条目是路由表中的每一行规则。它定义了当流量要访问某个目标网段时，应该从哪个下一跳设备（例如NAT网关、ECS等）转发出去。

VPC中路由条目分为2种：

[1. 静态路由条目](products/vpc/documents/vpc-route-table.md)：由系统自动添加或由您手动添加的路由条目。

[2. 动态路由条目](products/vpc/documents/vpc-route-table.md)：由TR、VPN等其他网络实例传播至VPC的路由条目。

1. 静态路由条目

系统自动添加或您手动添加的路由条目，为静态路由条目。包括2种：

- 

系统路由条目：由系统在创建VPC和交换机时自动添加、下一跳为Local的路由条目，用于VPC内部实例间通信或访问云服务。

- 

自定义路由条目：由您手动添加的路由条目，用于自定义流量转发路径。

如下图所示，2个VPC通过对等连接连通，其中VPC1的系统路由表包含如下静态路由条目：

- 

创建VPC和交换机后，系统自动添加下一跳为Local的系统路由条目：

- 

云服务路由：目标网段100.64.0.0/10，用于VPC1内部实例访问云服务。

- 

交换机网段路由：目标网段10.0.0.0/24，用于VPC1内交换机私网之间相互通信。

- 

创建VPC对等连接后，您需要手动添加的自定义路由条目：

目标网段172.16.0.0/16，下一跳对等连接，用于将前往VPC2的流量转发至对等连接。

VPC2的系统路由表中的路由条目与VPC1原理相同，此处不再赘述。

系统路由条目与自定义路由条目对比

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 对比项 | 系统路由条目 | 自定义路由条目 |
| --- | --- | --- |
| 定义 | 下一跳为 Local 的路由条目，由系统在创建 VPC 和交换机时自动添加。 | 由您手动添加的路由条目。 |
| IPv4 路由 | 系统自动在 VPC 内的所有路由表中添加： 交换机网段路由：以路由表所属 VPC 内的所有交换机网段为目标网段的路由条目，用于交换机内实例相互通信。 云服务路由：以 100.64.0.0/10 为目标网段的路由条目，用于 VPC 内实例访问云服务。 您可以创建比云服务系统路由 100.64.0.0/10 网段更明细的自定义路由，但不支持和该网段相同。建议您谨慎配置更明细的路由，如果配置错误将导致部分云产品服务无法正常访问和使用。 | 您可以手动添加如下路由： 目标网段：自定义的 IPv4 网段 ，或使用 [VPC](products/vpc/documents/vpc-prefix-lists.md) [前缀列表](products/vpc/documents/vpc-prefix-lists.md) 。 下一跳：可选 IPv4 网关 、 NAT 网关 、 VPC 对等连接 、 转发路由器 、 VPN 网关 、 ECS 实例 、 弹性网卡 、 高可用虚拟 IP 、 路由器接口（边界路由器方向） 、 路由器接口（专有网络方向） 、 专线网关 、 网关型负载均衡终端节点 。 您可查看 [配置示例](products/vpc/documents/vpc-route-table.md) ，了解不同类型的下一跳对应的典型场景。 |
| IPv6 路由 | 若 VPC 已 [开启](products/vpc/documents/vpc-and-vswitch.md) [IPv6](products/vpc/documents/vpc-and-vswitch.md) ，则系统会在交换机所属 VPC 的所有路由表中自动添加如下条目： 交换机网段路由：以交换机 IPv6 网段为目标网段的路由条目，用于交换机内实例通过 IPv6 相互通信。 | 若 VPC 已 [开启](products/vpc/documents/vpc-and-vswitch.md) [IPv6](products/vpc/documents/vpc-and-vswitch.md) ，可添加如下路由： 目标网段：自定义的 IPv6 网段 ，或使用 [VPC](products/vpc/documents/vpc-prefix-lists.md) [前缀列表](products/vpc/documents/vpc-prefix-lists.md) 。 下一跳：可选 ECS 实例 、 IPv6 网关 、 弹性网卡 、 路由器接口（边界路由器方向） 、 专线网关 、 VPC 对等连接 、 网关型负载均衡终端节点 、 转发路由器 。 您可查看 [配置示例](products/vpc/documents/vpc-route-table.md) ，了解不同类型的下一跳对应的典型场景。 |
| 是否可更改下一跳 | 系统路由表中的系统路由条目：不支持修改下一跳。 自定义路由表中的系统路由条目： 支持修改下一跳，可指向 ECS 实例 、 弹性网卡 和 网关型负载均衡终端节点 。修改后路由条目类型将变为自定义路由条目。 | [支持修改下一跳](products/vpc/documents/vpc-route-table.md) 若自定义路由条目是由系统路由条目修改下一跳而来，那么这种类型的条目仅支持修改为 Local、ECS 实例、弹性网卡或网关型负载均衡终端节点。 |
| 是否支持自行创建 | 您不能自行创建系统路由条目，也不能删除系统路由条目。 | 可自行创建和删除 |


2. 动态路由条目

动态路由是其他网络实例传播至VPC的路由条目，无需像静态路由那样手动在VPC路由表中配置，而是自动从路由动态源接收和更新。

2.1 路由动态源

自动向VPC传播路由的网络实例，包括企业版TR（转发路由器）、基础版TR（转发路由器）、VPN网关、专线网关ECR。您可在控制台路由表详情页的路由条目列表>动态路由条目页签下，查看动态路由条目来源和明细。

从企业版TR接收的路由条目明细，需从路由条目列表>自定义路由条目页签下查看。

2.2 开启/关闭动态路由接收

所有路由表默认开启动态路由接收。若需采用纯静态路由配置，可针对路由表粒度[关闭动态路由接收](products/vpc/documents/vpc-route-table.md)，按需规划业务路由表，方便用户灵活便捷地管理路由配置。

2.3 动态路由使用限制

- 

VPC路由表同一时刻仅接收单一路由动态源的动态路由。

例如，VPC关联ECR后，再连接企业版TR，在TR上针对VPC开启[路由同步](products/cen/documents/user-guide/route-synchronization.md)将会失败；创建VPN网关并[开启路由传播](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/user-guide/manage-destination-based-routes#2ca2a1f525mlq)后，VPN网关学习到的BGP路由将会自动传播到VPC的系统路由表中，此时无法将VPC关联至ECR。

- 

如果接收的动态路由，与路由表中已有的路由条目网段重叠时，请查看[路由优先级](products/vpc/documents/vpc-route-table.md)了解路由生效规则。

- 

仅绑定交换机的路由表支持接收动态路由，绑定网关的路由表不支持动态路由。

- 

单个路由表来自 ECR 动态传播的最大生效路由条目数量默认为 200 条。超过配额后，动态路由条目仍会接收，但状态为超限暂不生效。配额提升后，新配额将在 ECR 动态传播路由下次变化时生效，超限的路由将按照配置的先后顺序生效。

### 路由优先级

VPC路由表中的路由条目，按照如下规则匹配优先级：

- 

存在目标网段重叠的路由条目时：

IPv4 和 IPv6 流量路由彼此独立，按照最长前缀匹配规则，选择与目的网段与目的IP地址匹配的最明确路由，确定下一跳并进行转发。

最长前缀匹配：当有多条路由条目的目标网段都能匹配上数据包的目的IP地址时，系统会采用掩码最长（即网段范围最精确）的那条路由。例如，去往192.168.1.100的流量，会优先匹配192.168.1.0/24而非192.168.0.0/16。

- 

新增路由条目与已有路由条目的目标网段重叠时：

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

| 操作 | 已有系统路由 | 已有自定义路由 | 已有动态路由 |
| --- | --- | --- | --- |
| 创建交换机 | 交换机的网段，不支持和已有系统路由重叠 | 交换机的网段，不支持： 和已有自定义路由目标网段相同 包含自定义路由目标网段范围 | 交换机的网段，不支持： 和已有动态路由目标网段相同 包含动态路由目标网段范围 |
| 新增自定义路由 | 新增自定义路由的目标网段，不支持： 和已有系统路由条目的网段相同 比已有系统路由更明细 | 新增自定义路由的目标网段，不支持和已有自定义路由的目标网段相同 如果 下一跳类型 为 路由器接口（边界路由器方向） ，支持配置主备或负载路由，详情见 [路由到路由器接口](products/vpc/documents/vpc-route-table.md) 。 | 新增自定义路由时，不支持和已有动态路由目标网段相同。 新增自定义路由下一跳是 VPN 网关或路由器接口类型时，对于已有来自 CEN 的目标网段相同的动态路由：动态路由撤销，自定义路由生效。 |
| 接收动态路由 | 不支持和已有系统路由目标网段相同。 比已有系统路由的目标网段更明细时，动态路由不生效： 路由动态源为 ECR 时，动态路由会展示在 VPC 路由表中但状态为 候选 ，暂不参与转发。 路由动态源为 VPN 网关、企业版 TR 或基础版 TR 时，动态路由不会传播到 VPC 路由表。 | 和已有自定义路由目标网段相同时，动态路由不生效。 路由动态源为 ECR 时，动态路由会展示在 VPC 路由表中但状态为 候选 ，暂不参与转发。 路由动态源为 VPN 网关、企业版 TR 或基础版 TR 时，动态路由不会传播到 VPC 路由表。 自定义路由删除后，动态路由自动生效。 | 不支持，当前 VPC 路由表 [只有单一路由传播源](products/vpc/documents/vpc-route-table.md) 。 |


## 管理路由表

创建VPC时，系统自动创建一张系统路由表，默认绑定所有交换机，来统一控制所有交换机的流量。

要单独控制VPC中特定交换机的流量，您需要先创建一张交换机类型的自定义路由表，再绑定到目标交换机。

要控制从公网进入VPC的流量，您需要创建一张边界网关类型的自定义路由表，再绑定IPv4/IPv6网关。

### 创建/删除路由表

您需要先创建一张自定义路由表，才能绑定到目标交换机或IPv4/IPv6网关。

## 控制台

创建路由表

- 

前往VPC控制台[路由表](https://vpc.console.aliyun.com/vpc/cn-hangzhou/route-tables)页面，单击创建路由表。

- 

选择目标专有网络，输入名称，并选择绑定对象类型：

- 

交换机：后续将此路由表[绑定到交换机](products/vpc/documents/vpc-route-table.md)后，可控制特定交换机的流量路径。

- 

边界网关：后续将此路由表[绑定到](products/vpc/documents/vpc-route-table.md)[IPv4/IPv6](products/vpc/documents/vpc-route-table.md)[网关](products/vpc/documents/vpc-route-table.md)后，可控制从公网进入VPC的流量路径。

创建自定义路由表后，系统会自动为其添加以下系统路由条目：

- 

交换机网段路由：以路由表所属VPC内的所有交换机网段为目标网段的路由条目，用于交换机内实例相互通信。

- 

云服务路由：以100.64.0.0/10为目标网段的路由条目，用于VPC内实例访问云服务。

删除路由表

在目标路由表的操作列或详情页单击删除。删除前需确保路由表已[解绑](products/vpc/documents/vpc-route-table.md)，且已[删除所有自定义路由条目](products/vpc/documents/vpc-route-table.md)。

仅自定义路由表可删除，系统路由表不可删除。

## API

- 

调用[CreateRouteTable](products/vpc/documents/developer-reference/api-vpc-2016-04-28-createroutetable.md)新建路由表。

- 

调用[DeleteRouteTable](products/vpc/documents/developer-reference/api-vpc-2016-04-28-deleteroutetable.md)删除自定义路由表。

## Terraform

Resources：[alicloud_route_table](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_table)variable "name" { default = "terraform-example" } resource "alicloud_vpc" "defaultVpc" { vpc_name = var.name } resource "alicloud_route_table" "default" { description = "test-description" vpc_id = alicloud_vpc.defaultVpc.id route_table_name = var.name associate_type = "VSwitch" }

### 绑定/解绑路由表

新建的自定义路由表默认不绑定任何资源，您需要将其绑定到交换机或IPv4/IPv6网关后，路由表才会生效。

## 控制台

绑定路由表

前往VPC控制台[路由表](https://vpc.console.aliyun.com/vpc/cn-hangzhou/route-tables)页面，在目标路由表的绑定资源列，单击立即绑定：

- 

路由表绑定对象类型为交换机：单击绑定交换机，在打开的对话框中选择目标交换机。

交换机绑定自定义路由表后，会自动解绑系统路由表。

- 

路由表绑定对象类型为边界网关：单击绑定边界网关，在打开的对话框中选择目标IPv4网关或IPv6网关。

关于绑定边界网关的路由表的使用教程，请查看[使用网关路由表控制进入](products/vpc/documents/use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md)[VPC](products/vpc/documents/use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md)[的流量](products/vpc/documents/use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md)。

解绑路由表

前往目标路由表的详情页面：

- 

路由表绑定对象类型为交换机：在已绑定交换机页签下，勾选要解绑的交换机，然后单击解绑。解绑后交换机会绑回系统路由表。

- 

路由表绑定对象类型为边界网关：在已绑定的边界网关页签下，在目标IPv4/IPv6网关的操作列单击解绑。

警告

解绑路由表前，请充分评估路由条目变化带来的相关业务影响，避免导致业务受损。

## API

- 

调用[AssociateRouteTable](products/vpc/documents/developer-reference/api-vpc-2016-04-28-associateroutetable.md)将路由表和交换机绑定。

- 

调用[AssociateRouteTableWithGateway](products/vpc/documents/developer-reference/api-vpc-2016-04-28-associateroutetablewithgateway.md)将路由表和IPv4/IPv6网关绑定。

警告

解绑路由表前，请充分评估路由条目变化带来的相关业务影响，避免导致业务受损。

- 

调用[UnassociateRouteTable](products/vpc/documents/developer-reference/api-vpc-2016-04-28-unassociateroutetable.md)将路由表和交换机解绑。

- 

调用[DissociateRouteTableFromGateway](products/vpc/documents/developer-reference/api-vpc-2016-04-28-dissociateroutetablefromgateway.md)将路由表和IPv4/IPv6网关解绑。

## Terraform

将路由表和交换机绑定Resources：[alicloud_route_table_attachment](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_table_attachment)Data Sources：[alicloud_zones](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/zones)variable "name" { default = "terraform-example" } resource "alicloud_vpc" "foo" { cidr_block = "172.16.0.0/12" vpc_name = var.name } data "alicloud_zones" "default" { available_resource_creation = "VSwitch" } resource "alicloud_vswitch" "foo" { vpc_id = alicloud_vpc.foo.id cidr_block = "172.16.0.0/21" zone_id = data.alicloud_zones.default.zones[0].id vswitch_name = var.name } resource "alicloud_route_table" "foo" { vpc_id = alicloud_vpc.foo.id route_table_name = var.name description = "route_table_attachment" } resource "alicloud_route_table_attachment" "foo" { vswitch_id = alicloud_vswitch.foo.id route_table_id = alicloud_route_table.foo.id }

将路由表和IPv4网关/IPv6网关绑定Resources：[alicloud_vpc_gateway_route_table_attachment](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_gateway_route_table_attachment)resource "alicloud_vpc" "example" { cidr_block = "172.16.0.0/12" vpc_name = "terraform-example" } resource "alicloud_route_table" "example" { vpc_id = alicloud_vpc.example.id route_table_name = "terraform-example" description = "terraform-example" associate_type = "Gateway" } resource "alicloud_vpc_ipv4_gateway" "example" { ipv4_gateway_name = "terraform-example" vpc_id = alicloud_vpc.example.id enabled = true } resource "alicloud_vpc_gateway_route_table_attachment" "example" { ipv4_gateway_id = alicloud_vpc_ipv4_gateway.example.id route_table_id = alicloud_route_table.example.id }

## 管理路由条目

### 添加/删除路由条目

针对绑定交换机的路由表，可通过手动添加路由条目来控制交换机的流量路径。自行添加的路由条目会被归类为自定义路由条目。

在IPv4/IPv6网关绑定的路由表中，不支持自行添加路由条目，但您可以[更改路由条目下一跳](products/vpc/documents/vpc-route-table.md)。

## 控制台

添加路由条目

- 

前往目标路由表的详情页面，在路由条目列表>自定义路由条目页签下，单击添加路由条目。

- 

在添加路由条目对话框中，配置目标网段和下一跳类型。您可查看[配置示例](products/vpc/documents/vpc-route-table.md)，了解不同类型的下一跳对应的典型场景。

如果在添加路由条目时报错，请查看是否符合[路由优先级](products/vpc/documents/vpc-route-table.md)要求。

删除路由条目

在目标路由条目的操作列单击删除。

警告

删除路由条目前，请充分评估相关业务影响，避免因删除操作导致业务受损。

## API

- 

调用[CreateRouteEntry](products/vpc/documents/developer-reference/api-vpc-2016-04-28-createrouteentry.md)添加单个路由条目；调用[CreateRouteEntries](products/vpc/documents/developer-reference/api-vpc-2016-04-28-createrouteentries.md)批量添加路由条目。

警告

删除路由条目前，请充分评估相关业务影响，避免因删除操作导致业务受损。

- 

调用[DeleteRouteEntry](products/vpc/documents/developer-reference/api-vpc-2016-04-28-deleterouteentry.md)删除单个自定义路由条目；调用[DeleteRouteEntries](products/vpc/documents/developer-reference/api-vpc-2016-04-28-deleterouteentries.md)批量删除自定义路由条目。

## Terraform

Resources：[alicloud_route_entry](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_entry)resource "alicloud_route_entry" "foo" { route_table_id = "rt-12345xxxx" # 填写路由表id destination_cidrblock = "172.16.1.1/32" nexthop_type = "Instance" # 填写下一跳类型 nexthop_id = "i-12345xxxx" # 填写下一跳实例id }

### 更改路由条目下一跳

可通过更改路由条目的下一跳，来改变目标网段的流量路径。

- 

系统路由条目：仅自定义路由表（包含网关路由表）中的系统路由条目支持更改下一跳，更改后条目类型会变为自定义路由条目，删除后变回系统路由条目。

- 

自定义路由条目：无路由表类型限制，系统路由表和自定义路由表的自定义路由条目均支持修改下一跳。

您可在[系统路由条目与自定义路由条目对比](products/vpc/documents/vpc-route-table.md)中查看目标网段和下一跳支持的类型。

警告

更改路由条目下一跳前，请充分评估相关业务影响，避免因更改操作导致业务受损。

## 控制台

在目标路由条目的操作列单击编辑，在打开的对话框中单击下一跳类型对应的下拉列表，选择目标下一跳。

您可查看[配置示例](products/vpc/documents/vpc-route-table.md)，了解不同类型的下一跳对应的典型场景。

## API

- 

调用[ModifyRouteEntry](products/vpc/documents/developer-reference/api-vpc-2016-04-28-modifyrouteentry.md)更改已绑定交换机的路由表的路由条目下一跳。

- 

调用[UpdateGatewayRouteTableEntryAttribute](products/vpc/documents/developer-reference/api-vpc-2016-04-28-updategatewayroutetableentryattribute.md)更改已绑定IPv4/IPv6网关的路由表的路由条目下一跳。

## Terraform

Resources：[alicloud_route_entry](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_entry)resource "alicloud_route_entry" "foo" { route_table_id = "rt-12345xxxx" # 填写路由表id destination_cidrblock = "172.16.1.1/32" nexthop_type = "Instance" # 更改下一跳类型 nexthop_id = "i-12345xxxx" # 填写下一跳实例id }

### 发布/撤回静态路由

路由表中的路由可传播至专线网关（ECR）或转发路由器（TR），结合动态路由接收，简化路由配置复杂度。

- 

静态路由发布至专线网关ECR：静态路由发布到ECR后，可实现从云上ECR到云下IDC的动态路由传播。在不存在路由冲突的情况下，ECR关联的本地IDC均可学习到该路由。

单击查看静态路由发布至ECR的工作原理、使用限制、场景示例

工作原理

- 

VPC与ECR关联后，VPC系统路由条目默认发布至ECR。

- 

静态路由发布至ECR后：

- 

ECR会将路由传播到与其关联的VBR。若VBR开启了BGP，则路由会进一步传播到本地IDC。

- 

ECR不会将路由传播给与其关联的其他VPC。

- 

如果发布的静态路由存在路由冲突，可在ECR的路由条目页签查看到目标路由条目，其状态显示为冲突，且不会生效。

使用限制

- 

VPC自定义路由表配置的路由条目不支持发布至ECR。

- 

目标网段是前缀列表的路由条目不支持发布至ECR。

- 

下一跳是路由器接口（边界路由器方向）的主备路由和负载路由不支持发布到ECR；VPC路由发布至ECR后，不再支持配置负载路由或主备路由。

- 

VPC路由发布至ECR后，若要对发布的路由进行修改，目标路由的下一跳仅可设置为支持发布操作的路由类型（见下表）。

- 

下表列出了VPC实例各类型路由条目在ECR中的默认发布状态以及是否支持发布和撤回操作。

单击查看表格

| 路由类型 | 路由条目所属实例 | 是否默认发布 | 是否支持发布操作 | 是否支持撤回操作 |
| --- | --- | --- | --- | --- |
| VPC 系统路由条目 | VPC | 是 | 支持 | 仅 马来西亚（吉隆坡） 支持 |
| 指向 IPv4 网关的路由条目 | VPC | 否 | 支持 | 支持 |
| 指向 IPv6 网关的路由条目 | VPC | 否 | 支持 | 支持 |
| 指向 NAT 网关的路由条目 | VPC | 否 | 支持 | 支持 |
| 指向 VPC 对等连接的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向转发路由器的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向 VPN 网关的路由条目 | VPC | 否 | 支持 | 支持 |
| 指向 ECS 实例的路由条目 | VPC | 否 | 支持 | 支持 |
| 指向弹性网卡的路由条目 | VPC | 否 | 支持 | 支持 |
| 指向高可用虚拟 IP 的路由条目 | VPC | 否 | 支持 | 支持 |
| 指向路由器接口（边界路由器方向）的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向路由器接口（专有网络方向）的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向专线网关的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向网关型负载均衡终端节点的路由条目 | VPC | 否 | 支持 | 支持 |


场景示例

某企业在阿里云华东1（杭州）地域拥有本地IDC，并创建了VPC，该企业希望实现云上云下平稳互通且保证本地IDC中部署的服务能够与公网通信。

该企业可以将VPC和边界路由器VBR连接至ECR，创建绑定了EIP的公网NAT网关后，使用路由发布至ECR的能力，在不存在路由冲突的情况下，ECR关联的本地IDC可通过BGP学习到指向NAT网关的路由，从而实现本地IDC对公网的访问。

- 

[静态路由发布至转发路由器](products/cen/documents/user-guide/advertise-routes-to-a-transit-router.md)[TR](products/cen/documents/user-guide/advertise-routes-to-a-transit-router.md)：静态路由发布到转发路由器后，在没有路由冲突，且TR开启路由同步的情况下，TR连接的网络实例均可以接收到该路由。

如果您的VPC同时连接了ECR和TR，那么将VPC路由发布到ECR和发布到TR这两个动作独立，互不影响。

控制台

发布静态路由条目

在目标路由条目的专有网络路由发布状态列单击发布。

只有VPC连接到TR或ECR后，控制台的路由条目才会显示专有网络路由发布状态列。

撤回已发布的静态路由条目

在目标路由条目的专有网络路由发布状态列单击撤回。

只有VPC连接到TR或ECR后，控制台的路由条目才会显示专有网络路由发布状态列。

API

针对ECR：

- 

调用[PublishVpcRouteEntries](products/vpc/documents/developer-reference/api-vpc-2016-04-28-publishvpcrouteentries.md)发布静态路由到ECR。

- 

调用[WithdrawVpcPublishedRouteEntries](products/vpc/documents/developer-reference/api-vpc-2016-04-28-withdrawvpcpublishedrouteentries.md)撤回已发布到ECR的路由。

针对TR：

- 

调用[PublishRouteEntries](products/cen/documents/developer-reference/api-cbn-2017-09-12-publishrouteentries.md)发布静态路由到TR。

- 

调用[WithdrawPublishedRouteEntries](products/cen/documents/developer-reference/api-cbn-2017-09-12-withdrawpublishedrouteentries.md)撤回已发布到TR的路由。

Tab 正文

### 开启/关闭动态路由接收

所有路由表默认开启[动态路由条目](products/vpc/documents/vpc-route-table.md)接收。若需采用纯静态路由配置，可针对路由表粒度关闭动态路由接收，按需规划业务路由表，方便用户灵活便捷地管理路由配置。

- 

支持关闭的情况：动态路由条目来源为路由传播-类型ECR，或没有动态路由传播到VPC。没有动态路由传播到VPC时，路由表详情页面的路由条目列表>动态路由条目页签不显示动态路由条目来源。

这些情况暂不支持关闭：VPC连接到了基础版TR、VPC连接到了企业版TR且TR针对该VPC开启了[路由同步](products/cen/documents/user-guide/route-synchronization.md)、VPC关联了VPN网关且VPN网关开启了[路由自动传播](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/user-guide/configure-bgp-dynamic-routing#77c5049e07fwz)。

- 

关闭后的影响：

- 

VPC路由表不再接收其他网络实例传播的路由。如果路由表中已存在动态路由，将全部删除，请谨慎操作。

- 

不允许VPC连接基础版TR；连接到此VPC的TR无法针对该VPC开启路由同步；关联此VPC的VPN网关无法开启路由自动传播。

- 

关闭后重新开启的影响：

开启后，VPC路由表中的动态路由条目，以当前路由动态源传播过来的路由条目为准。

例如ECR的动态路由条目有4条，那么关闭此开关，VPC路由表内的动态路由会清空。如果ECR新增了2条路由条目后，重新开启了此开关，那么VPC路由表会收到6条来自ECR的动态路由条目。

控制台

前往目标路由表基本信息页面，在是否接受传播路由开关中开启/关闭动态路由接收。

警告

开启/关闭动态路由接收前，请充分评估路由条目变化带来的相关业务影响，避免导致业务受损。

API

调用[ModifyRouteTableAttributes](products/vpc/documents/developer-reference/api-vpc-2016-04-28-modifyroutetableattributes.md)，修改RoutePropagationEnable参数来开启或关闭动态路由接收。

警告

开启/关闭动态路由接收前，请充分评估路由条目变化带来的相关业务影响，避免导致业务受损。

Terraform

警告

开启/关闭动态路由接收前，请充分评估路由条目变化带来的相关业务影响，避免导致业务受损。

Resources：[alicloud_route_table](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_table)variable "name" { default = "terraform-example" } resource "alicloud_vpc" "defaultVpc" { vpc_name = var.name } resource "alicloud_route_table" "default" { description = "test-description" vpc_id = alicloud_vpc.defaultVpc.id route_table_name = var.name associate_type = "VSwitch" route_propagation_enable = true # 修改此参数开启/关闭动态路由接收 }

## 使用网关路由表

通过使用网关路由表，可将公网入向流量导向安全设备进行深度检测与过滤，防止恶意攻击和未经授权的访问，实现安全防护。还可结合自定义路由表，将出向流量引流至安全设备，实现入向和出向的全面安全防护。

使用时，需先创建一张绑定IPv4网关的路由表，再将路由表中交换机网段对应的系统路由下一跳改为：

- 

ECS实例/弹性网卡：用于公网流量安全引流到特定ECS实例或弹性网卡。

- 

网关型负载均衡终端节点：用于网关型负载均衡GWLB场景的第三方安全设备公网流量引流。

仅[这些地域](products/slb/documents/gateway-based-load-balancing-gwlb/product-overview/regions-and-zones-supported-by-gwlb.md)支持修改下一跳为网关型负载均衡终端节点。

使用自建防火墙

可在VPC中通过ECS自建防火墙，并使用网关路由表[将进入](products/vpc/documents/use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md)[VPC](products/vpc/documents/use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md)[的流量引流至防火墙过滤](products/vpc/documents/use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md)。

GWLB高可用架构

可[使用网关型负载均衡](products/slb/documents/gateway-based-load-balancing-gwlb/getting-started/gwlb-quickly-implements-load-balancing-for-ipv4-services.md)[GWLB](products/slb/documents/gateway-based-load-balancing-gwlb/getting-started/gwlb-quickly-implements-load-balancing-for-ipv4-services.md)，将流量分发到不同的安全设备，来提高应用系统的安全性和可用性。

## 配置示例

为路由条目选择不同的下一跳时，会对应不同的场景：

- 

[路由到](products/vpc/documents/vpc-route-table.md)[IPv4](products/vpc/documents/vpc-route-table.md)[网关](products/vpc/documents/vpc-route-table.md)

- 

[路由到](products/vpc/documents/vpc-route-table.md)[IPv6](products/vpc/documents/vpc-route-table.md)[网关](products/vpc/documents/vpc-route-table.md)

- 

[路由到](products/vpc/documents/vpc-route-table.md)[NAT](products/vpc/documents/vpc-route-table.md)[网关](products/vpc/documents/vpc-route-table.md)

- 

[路由到](products/vpc/documents/vpc-route-table.md)[VPC](products/vpc/documents/vpc-route-table.md)[对等连接](products/vpc/documents/vpc-route-table.md)

- 

[路由到转发路由器](products/vpc/documents/vpc-route-table.md)

- 

[路由到](products/vpc/documents/vpc-route-table.md)[VPN](products/vpc/documents/vpc-route-table.md)[网关](products/vpc/documents/vpc-route-table.md)

- 

[路由到](products/vpc/documents/vpc-route-table.md)[ECS](products/vpc/documents/vpc-route-table.md)[实例或弹性网卡](products/vpc/documents/vpc-route-table.md)

- 

[路由到路由器接口](products/vpc/documents/vpc-route-table.md)

- 

[路由到专线网关](products/vpc/documents/vpc-route-table.md)

- 

[路由到网关型负载均衡终端节点](products/vpc/documents/vpc-route-table.md)

路由到IPv4网关

可将[IPv4](products/vpc/documents/ipv4-gateway-overview.md)[网关](products/vpc/documents/ipv4-gateway-overview.md)作为企业VPC与公网之间的统一出入口，结合自定义路由表集中控制公网访问流量，有利于实施统一的安全策略和审计，降低分散接入带来的安全风险。

路由到IPv6网关

VPC[开启](products/vpc/documents/vpc-and-vswitch.md)[IPv6](products/vpc/documents/vpc-and-vswitch.md)后，系统会自动在系统路由表中添加一条自定义路由条目：

- 

目标网段为::/0，下一跳为IPv6网关。

该路由用于将默认IPv6流量路由至IPv6网关，[为](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-dvo-wjp-zcb)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-dvo-wjp-zcb)[地址开通](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-dvo-wjp-zcb)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-dvo-wjp-zcb)[公网带宽](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-dvo-wjp-zcb)后，与系统路由表绑定的交换机将具备公网通信能力。

而绑定了自定义路由表的已开启IPv6的交换机，若需要IPv6公网通信能力，您需要在自定义路由表中手动添加上述路由条目，

下一跳为IPv6网关实例的自定义路由条目，目标网段仅支持配置为::/0。

路由到NAT网关

若主动访问公网的服务器较多，需占用较多的公网IP资源时，可通过[公网](products/nat-gateway/documents/user-guide/public-network-nat-gateway.md)[NAT](products/nat-gateway/documents/user-guide/public-network-nat-gateway.md)[网关](products/nat-gateway/documents/user-guide/public-network-nat-gateway.md)的SNAT功能，实现VPC内的多个ECS实例共享EIP上网，节省公网IP资源。且多个ECS实例无需暴露其私网IP地址即可实现公网访问，降低安全风险。

使用NAT网关时，需要为VPC路由表添加指向公网NAT网关的自定义路由条目，实现公网访问。

- 

当ECS实例所属交换机绑定自定义路由表时：需手动配置目标网段为0.0.0.0/0，下一跳为公网NAT网关的路由条目。

- 

当ECS实例所属交换机绑定系统路由表时：

- 

系统路由表中不存在0.0.0.0/0的路由条目：系统将自动配置指向该公网NAT网关的路由条目。

- 

系统路由表中存在0.0.0.0/0的路由条目：需要先删除现有的路由条目，然后添加指向公网NAT网关的路由条目。

路由到VPC对等连接

不同VPC之间网络隔离，但可使用[VPC](products/vpc/documents/vpc-peer-to-peer-connection.md)[对等连接](products/vpc/documents/vpc-peer-to-peer-connection.md)实现同账号或跨账号、同地域或跨地域的两个VPC间的私网互通。在两个VPC之间建立对等连接后，VPC内部署的云产品资源可以通过私有IPv4地址或IPv6地址互相访问。

路由到转发路由器

当使用[云企业网](products/cen/documents/product-overview/what-is-cen.md)连通VPC时，VPC路由表中需添加指向转发路由器的路由条目，可选如下任一方式添加：

- 

创建VPC连接时，勾选自动为VPC的所有路由表配置指向转发路由器的路由。

开启本功能后，系统将在VPC实例的所有路由表内自动配置目标网段为10.0.0.0/8、172.16.0.0/12、192.168.0.0/16的三条路由条目，其下一跳均指向VPC连接，用于引导VPC实例的IPv4流量进入转发路由器。

- 

在转发路由器中开启[路由学习](products/cen/documents/user-guide/route-learning.md)后：针对每个VPC开启[路由同步](products/cen/documents/user-guide/route-synchronization.md)；或手动在每个VPC路由表中添加指向对端VPC的路由条目。

下图是在转发路由器开启路由学习后，手动在VPC路由表中添加了目标网段为对端VPC网段、下一跳为转发路由器的路由条目示例：

路由到VPN网关

通过VPN网关建立加密隧道，可实现本地数据中心等网络与云上专有网络之间安全可靠的网络连接。

使用VPN网关时，需为VPC配置目标网段为本地IDC网段，下一跳为VPN网关的路由，实现[VPC](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/getting-started/establish-a-connection-between-the-vpc-and-the-on-premises-data)[通过](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/getting-started/establish-a-connection-between-the-vpc-and-the-on-premises-data)[IPsec-VPN](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/getting-started/establish-a-connection-between-the-vpc-and-the-on-premises-data)[连接访问本地数据中心](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/getting-started/establish-a-connection-between-the-vpc-and-the-on-premises-data)。

路由到ECS实例或弹性网卡

VPC内2个交换机进行互访时，可通过调整路由表，将第三方安全设备（如防火墙、WAF等）串联到流量路径中，实现流量检测、分析和保护。

配置时，需将互访的交换机分别绑定自定义路由表，并将系统路由条目对应网段的下一跳改为防火墙对应的ECS实例，或防火墙的弹性网卡ENI：

路由到路由器接口

通过高速通道的[VBR](https://help.aliyun.com/zh/express-connect/user-guide/what-is-a-vbr-to-vpc-connection/)[上连](https://help.aliyun.com/zh/express-connect/user-guide/what-is-a-vbr-to-vpc-connection/)功能，可将本地IDC接入云上网络。

说明

VBR上连功能默认不开放。如需使用，请向商务经理申请。

使用时，需为VPC配置目标网段为本地IDC网段，下一跳类型为路由器接口（边界路由器方向）的路由，实现VPC通过边界路由器，访问本地数据中心。该类型支持负载分担和主备方式，需要配合[健康检查](https://help.aliyun.com/zh/express-connect/user-guide/configure-and-manage-health-checks)使用：

- 

主备方式：仅支持两个实例作为下一跳，主路由下一跳权重为100，备份路由下一跳权重为0。当主路由健康检查失败时，备份路由生效。

- 

负载分担：需要选择2-16个实例作为路由下一跳。每个实例对应的权重需要相同，权重的有效范围为0-255的整数，系统会将流量平均分配给下一跳实例。

主备方式的示意图：

路由到专线网关

通过使用高速通道的[专线网关](https://help.aliyun.com/zh/express-connect/user-guide/ecr/)[ECR](https://help.aliyun.com/zh/express-connect/user-guide/ecr/)，可将本地IDC接入云上网络。

- 

VPC默认接收来自ECR的动态路由，目标网段为本地IDC网段，下一跳为专线网关，使云上VPC与云下IDC互通。

- 

VPC路由表关闭了动态路由接收的情况下，需手动在VPC路由表中配置目标网段为本地IDC网段，下一跳为专线网关的路由，实现云上VPC与云下本地IDC互通。

路由到网关型负载均衡终端节点

仅[这些地域](products/slb/documents/gateway-based-load-balancing-gwlb/product-overview/regions-and-zones-supported-by-gwlb.md)支持网关型负载均衡终端节点，具体使用场景请查看[使用网关路由表-GWLB](products/vpc/documents/vpc-route-table.md)[高可用架构](products/vpc/documents/vpc-route-table.md)。

## 更多信息

### 支持的地域

系统路由表全地域支持，自定义路由表支持的地域如下：

公有云支持的地域

| 区域 | 支持自定义路由表的地域 |
| --- | --- |
| 亚太-中国 | 华东 1（杭州） 、 华东 2（上海） 、 华东 5 （南京-本地地域-关停中） 、 华北 1（青岛） 、 华北 2（北京） 、 华北 3（张家口） 、 华北 5（呼和浩特） 、 华北 6（乌兰察布） 、 华南 1（深圳） 、 华南 2（河源） 、 华南 3（广州） 、 西南 1（成都） 、 西北 2（中卫） 、 中国香港 、 华中 1（武汉-本地地域） 、 华东 6（福州-本地地域-关停中） |
| 亚太-其他 | 日本（东京） 、 韩国（首尔） 、 新加坡 、 马来西亚（吉隆坡） 、 印度尼西亚（雅加达） 、 菲律宾（马尼拉） 、 泰国（曼谷） 、 马来西亚（柔佛州） |
| 欧洲与美洲 | 德国（法兰克福） 、 英国（伦敦） 、 法国（巴黎） 、 美国（硅谷） 、 美国（弗吉尼亚） 、 墨西哥 |
| 中东 | 阿联酋（迪拜） 、 沙特（利雅得）- 合作伙伴运营 |


金融云支持的地域

| 区域 | 支持自定义路由表的地域 |
| --- | --- |
| 亚太 | 华南 1 金融云 、 华东 2 金融云 、 华北 2 金融云（邀测） |


政务云支持的地域

| 区域 | 支持自定义路由表的地域 |
| --- | --- |
| 亚太 | 华北 2 阿里政务云 1 |


### 配额

| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_route_tables_num | 单个 VPC 支持创建的自定义路由表的数量 | 9 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_route_entrys_num | 单个路由表支持创建的自定义路由条目的数量（不包括 [动态传播路由条目](products/vpc/documents/vpc-route-table.md) ） | 200 条 |  |
| vpc_quota_dynamic_route_entrys_num | 单个路由表来自动态传播的路由条目数量 | 200 条 |  |
| vpc_quota_havip_custom_route_entry | 指向一个 HaVip 实例的自定义路由上限 | 5 个 |  |
| vpc_quota_vpn_custom_route_entry | 单个 VPC 内指向 VPN 的自定义路由上限 | 50 个 |  |
| 无 | 单个路由表支持绑定的标签数量 | 20 个 | 无法提升 |
| 单个 VPC 支持创建的路由器的数量 | 1 个 |  |  |
| 单个 VPC 支持指向转发路由器 TR 连接的最大路由条目数量 | 600 条 |  |  |


### 使用限制

路由表使用限制

- 

每个交换机必须绑定路由表，且只能绑定1张路由表。1张路由表可绑定多个交换机。

- 

仅自定义路由表可删除，系统路由表不可删除。

路由条目使用限制

静态路由条目使用限制：

- 

您不能自行创建系统路由条目，也不能删除系统路由条目。

- 

您可以创建比云服务系统路由100.64.0.0/10网段更明细的自定义路由，但不支持和该网段相同。建议您谨慎配置更明细的路由，如果配置错误将导致部分云产品服务无法正常访问和使用。

- 

下一跳为IPv6网关实例的自定义路由条目，目标网段仅支持配置为::/0。

- 

只有VPC连接到TR或ECR后，控制台的路由条目才会显示专有网络路由发布状态列。

- 

新增路由条目与已有路由条目的目标网段重叠时，部分情况下不支持添加新的路由条目，详情见[路由优先级](products/vpc/documents/vpc-route-table.md)。

静态路由发布使用限制：

- 

VPC自定义路由表配置的路由条目不支持发布至ECR。

- 

目标网段是前缀列表的路由条目不支持发布至ECR。

- 

下一跳是路由器接口（边界路由器方向）的主备路由和负载路由不支持发布到ECR；VPC路由发布至ECR后，不再支持配置负载路由或主备路由。

- 

VPC路由发布至ECR后，若要对发布的路由进行修改，目标路由的下一跳仅可设置为支持发布操作的路由类型（见下表）。

- 

下表列出了VPC实例各类型路由条目在ECR中的默认发布状态以及是否支持发布和撤回操作。

单击查看表格

| 路由类型 | 路由条目所属实例 | 是否默认发布 | 是否支持发布操作 | 是否支持撤回操作 |
| --- | --- | --- | --- | --- |
| VPC 系统路由条目 | VPC | 是 | 支持 | 仅 马来西亚（吉隆坡） 支持 |
| 指向 IPv4 网关的路由条目 | VPC | 否 | 支持 | 支持 |
| 指向 IPv6 网关的路由条目 | VPC | 否 | 支持 | 支持 |
| 指向 NAT 网关的路由条目 | VPC | 否 | 支持 | 支持 |
| 指向 VPC 对等连接的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向转发路由器的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向 VPN 网关的路由条目 | VPC | 否 | 支持 | 支持 |
| 指向 ECS 实例的路由条目 | VPC | 否 | 支持 | 支持 |
| 指向弹性网卡的路由条目 | VPC | 否 | 支持 | 支持 |
| 指向高可用虚拟 IP 的路由条目 | VPC | 否 | 支持 | 支持 |
| 指向路由器接口（边界路由器方向）的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向路由器接口（专有网络方向）的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向专线网关的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向网关型负载均衡终端节点的路由条目 | VPC | 否 | 支持 | 支持 |


动态路由条目使用限制：

- 

VPC路由表同一时刻仅接收单一路由动态源的动态路由。

例如，VPC关联ECR后，再连接企业版TR，在TR上针对VPC开启[路由同步](products/cen/documents/user-guide/route-synchronization.md)将会失败；创建VPN网关并[开启路由传播](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/user-guide/manage-destination-based-routes#2ca2a1f525mlq)后，VPN网关学习到的BGP路由将会自动传播到VPC的系统路由表中，此时无法将VPC关联至ECR。

- 

如果接收的动态路由，与路由表中已有的路由条目网段重叠时，请查看[路由优先级](products/vpc/documents/vpc-route-table.md)了解路由生效规则。

- 

仅绑定交换机的路由表支持接收动态路由，绑定网关的路由表不支持动态路由。

- 

单个路由表来自 ECR 动态传播的最大生效路由条目数量默认为 200 条。超过配额后，动态路由条目仍会接收，但状态为超限暂不生效。配额提升后，新配额将在 ECR 动态传播路由下次变化时生效，超限的路由将按照配置的先后顺序生效。

### 计费

VPC路由表功能免费。

[上一篇：高可用虚拟IP（HaVip）](products/vpc/documents/highly-available-virtual-ip-address-havip.md)[下一篇：使用网关路由表控制进入VPC的流量](products/vpc/documents/use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md)

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
