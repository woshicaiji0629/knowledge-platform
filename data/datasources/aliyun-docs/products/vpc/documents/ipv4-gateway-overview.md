# IPv4网关-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/ipv4-gateway-overview

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

# IPv4网关

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

默认情况下，VPC内的资源绑定公网IP后，即可与公网直接进行IPv4通信。企业可能会存在未经运维部门管控的公网访问方式（例如业务部门随意为ECS实例配置公网IP），这为企业网络管理带来安全风险。使用IPv4网关，通过路由表可以控制公网访问流量统一经过IPv4网关，降低分散接入带来的安全风险。

## 为什么使用IPv4网关

| 对比项 | 公网直接访问（VPC 默认情况） | 使用 IPv4 网关集中控制 |
| --- | --- | --- |
| 示例 | 不使用 IPv4 网关，ECS 通过固定公网 IP、弹性公网 IP 或公网 NAT 网关直接访问公网。 | 集中管控公网访问流量。 |
| 适用场景 | 少量 ECS 需具备独立、直接的公网访问能力。 适用于公网访问需求频繁变化的场景。 | 适用于大规模、多层级网络架构。 对网络安全合规性有严格要求的企业级环境。 |
| 操作复杂度 | 操作简便快捷，无需进行路由配置。 | 需要进行网络规划以及路由规则配置。 |
| 灵活性 | 每个实例独立操作，互不影响。 | 网络策略的变更会影响 VPC 内所有实例。 |
| 安全性 | 安全防护主要依赖于实例自身的安全组规则配置。 | IPv4 网关集中管控模式保障网络策略的一致性与整体安全性。 |


### IPv4网关与NAT网关的区别

IPv4 网关和公网 NAT 网关可结合使用。参考[公网访问](products/vpc/documents/public-network-access.md)，详细了解相关网络组件之间的关系。

| 网络组件 | IPv4 网关 | 公网 NAT 网关 |
| --- | --- | --- |
| 功能定位 | VPC 边界上的公网 IPv4 流量控制组件 | VPC 内部的网络地址转换设备 |
| 使用场景 | 集中控制公网访问流量 | 统一公网流量出口 |
| 是否提供公网访问能力 | 不提供，仅控制公网流量 | 通过绑定 EIP 提供公网访问能力 （公网访问能力是由 EIP 提供的，NAT 网关本身不提供公网访问能力） |


创建 IPv4 网关后，交换机可区分为：

- 

公有交换机：绑定的路由表中存在目标网段为0.0.0.0/0，下一跳为IPv4网关的路由，其中的资源绑定公网IP即可访问公网。

- 

私有交换机：绑定的路由表中不存在指向IPv4网关的路由，其中的资源绑定公网IP后无法直接访问公网。

结合公网NAT网关使用时，需要将公网NAT网关部署在公有交换机，部署在私有交换机的ECS实例配置路由指向公网NAT网关，将访问公网的流量路由至公网NAT网关，再使用公网NAT网关绑定的公网IP访问公网。需注意：

- 

确保公网NAT网关的EipBindMode为NAT模式，兼容IPv4网关。

- 

控制台创建的公网NAT网关默认为NAT模式，调用[CreateNatGateway](products/nat-gateway/documents/developer-reference/api-vpc-2016-04-28-createnatgateway-natgws.md)创建时，EipBindMode需传入NAT。创建完成后，可以调用[ModifyNatGatewayAttribute](products/nat-gateway/documents/developer-reference/api-vpc-2016-04-28-modifynatgatewayattribute-natgws.md)调整EipBindMode。

- 

如果已创建EipBindMode为MULTI_BINDED模式的公网NAT网关，由于不兼容IPv4网关，将无法创建IPv4网关。

- 

如果已创建IPv4网关，调用[CreateNatGateway](products/nat-gateway/documents/developer-reference/api-vpc-2016-04-28-createnatgateway-natgws.md)创建EipBindMode为MULTI_BINDED模式的公网NAT网关，将无法绑定EIP。

- 

为避免激活IPv4网关后私有交换机中的资源无法访问公网，确保在激活IPv4网关前完成路由配置。

## 工作原理

### 使用IPv4网关控制公网访问

VPC创建并激活IPv4网关后，公网访问的流量由IPv4网关集中控制。为交换机关联的路由表配置指向IPv4网关的路由，其中的资源才可以直接访问公网。VPC 详情页可以查看IPv4公网访问模式，确定当前公网流量是否由IPv4网关集中管控。

激活IPv4网关前，VPC内的公网流量不会受到影响。但在激活过程中，可能会因流量路径切换导致短暂的网络中断。

### 删除IPv4网关模式

删除前需要先解绑网关路由表。在目标IPv4网关的操作列单击删除，或调用[DeleteIpv4Gateway](products/vpc/documents/developer-reference/api-vpc-2016-04-28-deleteipv4gateway.md)删除IPv4网关。删除时，选择不同的模式将影响VPC的公网访问形态。

- 

公网模式：系统会自动删除所有指向IPv4网关的路由条目，回退到VPC初始状态，实例绑定公网IP即可访问公网。

- 

私网模式：需要先删除路由表中所有指向IPv4网关的路由条目。删除后，VPC内所有资源将无法访问公网。如需恢复为公网直接访问的形态，需要重新创建IPv4网关并选择公网模式删除。

重要

选择私网模式删除后，VPC内所有资源无论是否绑定公网IP都将无法访问公网。请谨慎操作！

## 集中控制公网访问

企业可能会存在未经运维部门管控的公网访问方式（例如业务部门随意为ECS实例配置公网IP），从而导致运维部门难以实现对公网访问的有效集中管理。使用IPv4网关集中控制公网访问流量，可以降低分散接入带来的安全风险，解决上述问题。

### 控制台

- 

前往[专有网络控制台-IPv4](https://vpc.console.aliyun.com/ipv4/cn-hangzhou/ipv4s)[网关](https://vpc.console.aliyun.com/ipv4/cn-hangzhou/ipv4s)页面，在页面上方选择VPC所在的地域后，单击创建IPv4网关。

- 

创建IPv4网关：选择需集中控制公网访问的专有网络。

- 

激活IPv4网关：选择公有交换机绑定的路由表，系统自动添加0.0.0.0/0路由指向IPv4网关，确保公有交换机中的资源绑定公网IP后可访问公网。当路由表中存在目标网段为0.0.0.0/0的路由时，需要单击暂不激活，调整对应路由的下一跳为IPv4网关后再激活。激活后，专有网络访问公网的行为切换为IPv4网关集中控制。

- 

当ECS实例使用公网NAT网关绑定的公网IP访问公网时，需要将ECS实例和公网NAT网关部署在不同的交换机中，为NAT网关所在交换机关联的路由表配置0.0.0.0/0路由指向IPv4网关，为ECS实例所在交换机关联的路由表配置路由指向公有交换机中的NAT网关。

- 

当ECS实例使用固定公网IP、绑定的弹性公网IP访问公网时，为ECS实例配置0.0.0.0/0路由指向IPv4网关即可。

### API

- 

调用[CreateIpv4Gateway](products/vpc/documents/developer-reference/api-vpc-2016-04-28-createipv4gateway.md)创建IPv4网关。

- 

调用[EnableVpcIpv4Gateway](products/vpc/documents/developer-reference/api-vpc-2016-04-28-enablevpcipv4gateway.md)激活IPv4网关，指定RouteTableList为公有交换机绑定的路由表；如未指定，需要调用[CreateRouteEntry](products/vpc/documents/developer-reference/api-vpc-2016-04-28-createrouteentry.md)在对应路由表中自行添加0.0.0.0/0路由指向IPv4网关。

### Terraform

与控制台逻辑不同的是，激活IPv4网关时，系统不会自动添加0.0.0.0/0路由指向IPv4网关，需要自行配置路由。

Resource：[alicloud_vpc](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc)、[alicloud_vswitch](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vswitch)、[alicloud_vpc_ipv4_gateway](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_ipv4_gateway)、[alicloud_route_table](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_table)、[alicloud_route_table_attachment](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_table_attachment)、[alicloud_vpc_route_entry](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_route_entry)、[alicloud_instance](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/instance)、[alicloud_security_group](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/security_group)、[alicloud_security_group_rule](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/security_group_rule)、[alicloud_eip_address](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/eip_address)、[alicloud_eip_association](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/eip_association)、[alicloud_nat_gateway](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/nat_gateway)、[alicloud_snat_entry](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/snat_entry)Data Sources：[alicloud_zones](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/zones)# 指定创建IPv4网关的地域 provider "alicloud" { region = "cn-hangzhou" } # 根据数据源自动获取可以创建交换机的可用区列表 data "alicloud_zones" "available_zones" { available_resource_creation = "VSwitch" # 查询VPC内可创建的可用区 } # 创建1个VPC resource "alicloud_vpc" "example_vpc" { vpc_name = "example_vpc_name" cidr_block = "10.0.0.0/16" # 指定网段 } # 定义交换机配置 locals { vswitches = { vsw1 = { name = "example_vsw1_name" cidr_block = "10.0.0.0/24" zone_index = 0 } vsw2 = { name = "example_vsw2_name" cidr_block = "10.0.1.0/24" zone_index = 1 } vsw3 = { name = "example_vsw3_name" cidr_block = "10.0.2.0/24" zone_index = 0 } vsw4 = { name = "example_vsw4_name" cidr_block = "10.0.3.0/24" zone_index = 0 } } # 定义路由表配置 route_tables = { rt1 = { name = "example_rt1_name" vswitch_key = "vsw1" } rt2 = { name = "example_rt2_name" vswitch_key = "vsw2" } rt3 = { name = "example_rt3_name" vswitch_key = "vsw3" } rt4 = { name = "example_rt4_name" vswitch_key = "vsw4" } } # 定义实例配置 instances = { instance1 = { name = "example_instance1_name" vswitch_key = "vsw1" } instance2 = { name = "example_instance2_name" vswitch_key = "vsw3" } instance3 = { name = "example_instance3_name" vswitch_key = "vsw4" } } # 定义EIP配置 eips = { eip1 = { name = "example_eip1_name" } eip2 = { name = "example_eip2_name" } } # 定义SNAT条目配置 snat_entries = { snat1 = { instance_key = "instance2" } snat2 = { instance_key = "instance3" } } } # 创建多个交换机 resource "alicloud_vswitch" "example_vsw" { for_each = local.vswitches vswitch_name = each.value.name cidr_block = each.value.cidr_block vpc_id = alicloud_vpc.example_vpc.id zone_id = data.alicloud_zones.available_zones.zones[each.value.zone_index].id } # 创建多个自定义路由表 resource "alicloud_route_table" "example_route_table" { for_each = local.route_tables route_table_name = each.value.name vpc_id = alicloud_vpc.example_vpc.id } # 将路由表与交换机绑定 resource "alicloud_route_table_attachment" "example_route_table_attachment" { for_each = local.route_tables vswitch_id = alicloud_vswitch.example_vsw[each.value.vswitch_key].id route_table_id = alicloud_route_table.example_route_table[each.key].id } # 指定实例规格 variable "instance_type" { default = "ecs.e-c1m1.large" } # 指定镜像ID variable "image_id" { default = "aliyun_3_x64_20G_alibase_20221102.vhd" } # 创建安全组 resource "alicloud_security_group" "example_security_group" { security_group_name = "example_security_group_name" vpc_id = alicloud_vpc.example_vpc.id } # 创建安全组规则,需按实际访问流量修改协议与端口号 resource "alicloud_security_group_rule" "allow_internet" { type = "ingress" ip_protocol = "icmp" nic_type = "intranet" policy = "accept" port_range = "-1/-1" priority = 1 security_group_id = alicloud_security_group.example_security_group.id cidr_ip = "0.0.0.0/0" } # 创建多个服务器 resource "alicloud_instance" "example_instance" { for_each = local.instances instance_name = each.value.name vswitch_id = alicloud_vswitch.example_vsw[each.value.vswitch_key].id instance_type = var.instance_type image_id = var.image_id system_disk_category = "cloud_essd" security_groups = [alicloud_security_group.example_security_group.id] instance_charge_type = "PostPaid" # 指定付费类型为按量付费 spot_strategy = "SpotWithPriceLimit" # 设置上限价格的抢占式实例 } # 创建多个EIP resource "alicloud_eip_address" "example_eip" { for_each = local.eips address_name = each.value.name isp = "BGP" netmode = "public" bandwidth = "1" payment_type = "PayAsYouGo" } # 绑定ECS和EIP resource "alicloud_eip_association" "example_eip_ecs_association" { allocation_id = alicloud_eip_address.example_eip["eip1"].id instance_type = "EcsInstance" instance_id = alicloud_instance.example_instance["instance1"].id } # 创建公网NAT网关 resource "alicloud_nat_gateway" "example_natgw" { nat_gateway_name = "example_natgw_name" vpc_id = alicloud_vpc.example_vpc.id vswitch_id = alicloud_vswitch.example_vsw["vsw2"].id nat_type = "Enhanced" eip_bind_mode = "NAT" # 指定EIP绑定模式，必须为NAT模式 payment_type = "PayAsYouGo" } # 绑定EIP和公网NAT网关 resource "alicloud_eip_association" "example_eip_natgw_association" { allocation_id = alicloud_eip_address.example_eip["eip2"].id instance_type = "NAT" instance_id = alicloud_nat_gateway.example_natgw.id } # 添加路由指向NAT网关 resource "alicloud_route_entry" "example_rt3_route" { route_table_id = alicloud_route_table.example_route_table["rt3"].id destination_cidrblock = "0.0.0.0/0" nexthop_type = "NatGateway" nexthop_id = alicloud_nat_gateway.example_natgw.id } # 添加路由指向NAT网关 resource "alicloud_route_entry" "example_rt4_route" { route_table_id = alicloud_route_table.example_route_table["rt4"].id destination_cidrblock = "0.0.0.0/0" nexthop_type = "NatGateway" nexthop_id = alicloud_nat_gateway.example_natgw.id } # 创建SNAT条目 resource "alicloud_snat_entry" "example_snat_entry" { for_each = local.snat_entries snat_table_id = alicloud_nat_gateway.example_natgw.snat_table_ids source_cidr = alicloud_instance.example_instance[each.value.instance_key].primary_ip_address snat_ip = alicloud_eip_address.example_eip["eip2"].ip_address } # 创建IPv4网关 resource "alicloud_vpc_ipv4_gateway" "example_ipv4gw" { ipv4_gateway_name = "example_ipv4gw_name" vpc_id = alicloud_vpc.example_vpc.id enabled = true } # 添加路由指向IPv4网关 resource "alicloud_route_entry" "example_rt1_route" { route_table_id = alicloud_route_table.example_route_table["rt1"].id destination_cidrblock = "0.0.0.0/0" nexthop_type = "Ipv4Gateway" nexthop_id = alicloud_vpc_ipv4_gateway.example_ipv4gw.id } # 添加路由指向IPv4网关 resource "alicloud_route_entry" "example_rt2_route" { route_table_id = alicloud_route_table.example_route_table["rt2"].id destination_cidrblock = "0.0.0.0/0" nexthop_type = "Ipv4Gateway" nexthop_id = alicloud_vpc_ipv4_gateway.example_ipv4gw.id }

## 公网网段私用

VPC定义的默认私网转发网段遵循RFC 1918标准，包括10.0.0.0/8、172.16.0.0/12、192.168.0.0/16。当VPC与使用了非RFC 1918标准的私有网段（如30.0.0.0/16）的本地IDC或VPC建立网络连接时，具备公网访问能力的云资源访问非标准私网网段时，请求会直接通过公网转发，而不会按照配置的路由指向本地IDC或VPC。

为VPC创建并激活IPv4网关后，IPv4网关将集中控制公网访问行为，所有流量均按照路由表转发。交换机需要配置指向IPv4网关的0.0.0.0/0路由，其中的资源才可以直接访问公网。而按照最长前缀匹配原则，访问ECS02的流量将匹配30.0.0.0/16路由访问对端VPC。

### 控制台

- 

前往[专有网络控制台-IPv4](https://vpc.console.aliyun.com/ipv4/cn-hangzhou/ipv4s)[网关](https://vpc.console.aliyun.com/ipv4/cn-hangzhou/ipv4s)页面，在页面上方选择VPC所在的地域后，单击创建IPv4网关。

- 

创建IPv4网关：选择需访问非标准私网网段的专有网络。

- 

激活IPv4网关：选择需访问非标准私网网段的交换机绑定的路由表，系统自动添加0.0.0.0/0路由指向IPv4网关，确保交换机中的资源可以按照更明细的路由访问非标准私网网段。

- 

确保绑定的路由表中，不存在目标网段为0.0.0.0/0的路由。如有，需要单击暂不激活，删除路由后再激活。

- 

激活后，IPv4网关集中控制访问公网的流量，所有流量均按照路由表转发。

### API

- 

调用[CreateIpv4Gateway](products/vpc/documents/developer-reference/api-vpc-2016-04-28-createipv4gateway.md)创建IPv4网关。

- 

调用[EnableVpcIpv4Gateway](products/vpc/documents/developer-reference/api-vpc-2016-04-28-enablevpcipv4gateway.md)激活IPv4网关，指定RouteTableList为公有交换机绑定的路由表；如未指定，需要调用[CreateRouteEntry](products/vpc/documents/developer-reference/api-vpc-2016-04-28-createrouteentry.md)在对应路由表中自行添加0.0.0.0/0路由指向IPv4网关。

### Terraform

与控制台逻辑不同的是，激活IPv4网关时，系统不会自动添加0.0.0.0/0路由指向IPv4网关，需要自行配置路由。

Resource：[alicloud_vpc](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc)、[alicloud_vswitch](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vswitch)、[alicloud_vpc_ipv4_gateway](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_ipv4_gateway)、[alicloud_route_table](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_table)、[alicloud_route_table_attachment](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_table_attachment)、[alicloud_vpc_route_entry](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_route_entry)、[alicloud_instance](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/instance)、[alicloud_security_group](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/security_group)、[alicloud_security_group_rule](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/security_group_rule)、[alicloud_eip_address](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/eip_address)、[alicloud_eip_association](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/eip_association)、[alicloud_vpc_peer_connection](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_peer_connection)Data Sources：[alicloud_zones](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/zones)本示例中，建立对等连接的VPC属于同一账号。创建跨账号对等连接时，还需要创建[alicloud_vpc_peer_connection_accepter](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_peer_connection_accepter)确保对端账号接受对等连接。# 指定创建IPv4网关的地域 provider "alicloud" { region = "cn-hangzhou" } # 根据数据源自动获取可以创建交换机的可用区列表 data "alicloud_zones" "available_zones" { available_resource_creation = "VSwitch" # 查询VPC内可创建的可用区 } # 指定实例规格 variable "instance_type" { default = "ecs.e-c1m1.large" } # 指定镜像ID variable "image_id" { default = "aliyun_3_x64_20G_alibase_20221102.vhd" } # 创建VPC resource "alicloud_vpc" "example_vpc1" { vpc_name = "example_vpc1_name" cidr_block = "10.0.0.0/16" # 指定网段 } # 创建VPC resource "alicloud_vpc" "example_vpc2" { vpc_name = "example_vpc2_name" cidr_block = "30.0.0.0/16" # 指定网段 } # 创建交换机 resource "alicloud_vswitch" "example_vsw1" { vswitch_name = "example_vsw1_name" cidr_block = "10.0.1.0/24" vpc_id = alicloud_vpc.example_vpc1.id zone_id = data.alicloud_zones.available_zones.zones.0.id } # 创建交换机 resource "alicloud_vswitch" "example_vsw2" { vswitch_name = "example_vsw2_name" cidr_block = "30.0.1.0/24" vpc_id = alicloud_vpc.example_vpc2.id zone_id = data.alicloud_zones.available_zones.zones.1.id } # 创建安全组 resource "alicloud_security_group" "example_security_group1" { security_group_name = "example_security_group1_name" vpc_id = alicloud_vpc.example_vpc1.id } # 创建安全组规则,需按实际访问流量修改协议与端口号 resource "alicloud_security_group_rule" "allow_internet1" { type = "ingress" ip_protocol = "icmp" nic_type = "intranet" policy = "accept" port_range = "-1/-1" priority = 1 security_group_id = alicloud_security_group.example_security_group1.id cidr_ip = "0.0.0.0/0" } # 创建安全组 resource "alicloud_security_group" "example_security_group2" { security_group_name = "example_security_group2_name" vpc_id = alicloud_vpc.example_vpc2.id } # 创建安全组规则,需按实际访问流量修改协议与端口号 resource "alicloud_security_group_rule" "allow_internet2" { type = "ingress" ip_protocol = "icmp" nic_type = "intranet" policy = "accept" port_range = "-1/-1" priority = 1 security_group_id = alicloud_security_group.example_security_group2.id cidr_ip = "0.0.0.0/0" } # 创建ECS实例 resource "alicloud_instance" "example_instance1" { instance_name = "example_instance1_name" vswitch_id = alicloud_vswitch.example_vsw1.id instance_type = var.instance_type image_id = var.image_id system_disk_category = "cloud_essd" security_groups = [alicloud_security_group.example_security_group1.id] instance_charge_type = "PostPaid" spot_strategy = "SpotWithPriceLimit" } # 创建EIP resource "alicloud_eip_address" "example_eip" { address_name = "example_eip_name" isp = "BGP" netmode = "public" bandwidth = "1" payment_type = "PayAsYouGo" } # 绑定ECS和EIP resource "alicloud_eip_association" "example_eip_ecs_association" { allocation_id = alicloud_eip_address.example_eip.id instance_type = "EcsInstance" instance_id = alicloud_instance.example_instance1.id } # 创建ECS实例 resource "alicloud_instance" "example_instance2" { instance_name = "example_instance2_name" vswitch_id = alicloud_vswitch.example_vsw2.id instance_type = var.instance_type image_id = var.image_id system_disk_category = "cloud_essd" security_groups = [alicloud_security_group.example_security_group2.id] instance_charge_type = "PostPaid" spot_strategy = "SpotWithPriceLimit" } # 创建自定义路由表 resource "alicloud_route_table" "example_route_table1" { route_table_name = "example_route_table1_name" vpc_id = alicloud_vpc.example_vpc1.id } # 将路由表与交换机绑定 resource "alicloud_route_table_attachment" "example_route_table_attachment1" { vswitch_id = alicloud_vswitch.example_vsw1.id route_table_id = alicloud_route_table.example_route_table1.id } # 创建自定义路由表 resource "alicloud_route_table" "example_route_table2" { route_table_name = "example_route_table2_name" vpc_id = alicloud_vpc.example_vpc2.id } # 将路由表与交换机绑定 resource "alicloud_route_table_attachment" "example_route_table_attachment2" { vswitch_id = alicloud_vswitch.example_vsw2.id route_table_id = alicloud_route_table.example_route_table2.id } # 创建VPC对等连接 resource "alicloud_vpc_peer_connection" "example_vpc_peer" { peer_connection_name = "example_vpc_peer_name" vpc_id = alicloud_vpc.example_vpc1.id accepting_ali_uid = "1234****" # 对端VPC所属的账号I，本示例创建同账号对等连接。如果创建跨账号对等连接，需创建alicloud_vpc_peer_connection_accepter，确保对端账号接受对等连接。 accepting_region_id = "cn-hangzhou" accepting_vpc_id = alicloud_vpc.example_vpc2.id } # 配置对等连接的路由 resource "alicloud_route_entry" "example_peer_route1" { route_table_id = alicloud_route_table.example_route_table1.id destination_cidrblock = "30.0.0.0/16" nexthop_type = "VpcPeer" nexthop_id = alicloud_vpc_peer_connection.example_vpc_peer.id } # 配置对等连接的路由 resource "alicloud_route_entry" "example_peer_route2" { route_table_id = alicloud_route_table.example_route_table2.id destination_cidrblock = "10.0.0.0/16" nexthop_type = "VpcPeer" nexthop_id = alicloud_vpc_peer_connection.example_vpc_peer.id } # 创建IPv4网关 resource "alicloud_vpc_ipv4_gateway" "example_ipv4gw" { ipv4_gateway_name = "example_ipv4gw_name" vpc_id = alicloud_vpc.example_vpc1.id enabled = true } # 添加路由指向IPv4网关 resource "alicloud_route_entry" "example_igw_route" { route_table_id = alicloud_route_table.example_route_table1.id destination_cidrblock = "0.0.0.0/0" nexthop_type = "Ipv4Gateway" nexthop_id = alicloud_vpc_ipv4_gateway.example_ipv4gw.id }

## 公网入方向安全引流（第三方安全设备）

IPv4 网关仅能集中控制访问公网的流量。对于进入 VPC 的公网流量，使用IPv4网关绑定的[网关路由表](products/vpc/documents/use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md)，将公网入向流量导向安全设备进行深度检测与过滤，防止恶意攻击和未经授权的访问，实现安全防护。结合自定义路由表，还可将出向流量引流至安全设备，实现出入方向的全面安全防护。

IPv4网关只能绑定网关路由表（即边界网关类型的路由表）。每个VPC仅支持创建1个IPv4网关和1个网关路由表，二者一对一绑定。配置入方向引流路由时，应修改网关路由表中的系统路由条目，将对应交换机网段的下一跳指向安全设备。网关路由表不支持通过添加路由条目来创建自定义路由。

### 单点架构

### GWLB高可用架构

单点架构下，安全设备一旦发生故障，将会影响业务系统的可用性。[使用网关型负载均衡](products/slb/documents/gateway-based-load-balancing-gwlb/getting-started/gwlb-quickly-implements-load-balancing-for-ipv4-services.md)[GWLB](products/slb/documents/gateway-based-load-balancing-gwlb/getting-started/gwlb-quickly-implements-load-balancing-for-ipv4-services.md)，将安全设备进行高可用部署，可以消除单点故障。

| IPv4 公网流量入方向路径 | IPv4 公网流量出方向路径 |
| --- | --- |
| 1. IPv4 流量通过 IPv4 网关进入业务 VPC。 2. 根据网关路由表，将流量发送到 GWLBe。 3. GWLBe 将流量转发至 GWLB，由 GWLB 将流量转发到安全设备。 4. 安全设备完成安全检查后，将流量转回到 GWLB，通过私网连接将流量转到 GWLBe。 5. 根据 GWLBe 子网配置的路由表，将流量发送到业务服务器。 | 1. 根据业务服务器子网配置的路由表，将流量发送到 GWLBe。 2. GWLBe 将流量发往 GWLB，GWLB 将流量转发到安全设备。 3. 安全设备完成安全检查后，将流量转回到 GWLB，通过私网连接将流量转到 GWLBe。 4. 根据 GWLBe 子网配置的路由表，将流量发送到 IPv4 网关。 5. IPv4 网关将流量路由至公网。 |


配置网关路由表时，单击目标交换机网段系统路由操作列的编辑，修改下一跳为网关负载均衡终端节点，修改后，路由条目将出现在自定义路由条目页签下。

### 控制台

绑定网关路由表

在目标IPv4网关详情页，单击立即绑定；或在目标网关路由表详情页的已绑定的边界网关页签下，单击绑定边界网关，勾选目标IPv4网关。

解绑网关路由表

在目标IPv4网关详情页，或目标网关路由表详情页的已绑定的边界网关页签下，单击解绑。

### API

- 

调用[AssociateRouteTableWithGateway](products/vpc/documents/developer-reference/api-vpc-2016-04-28-associateroutetablewithgateway.md)绑定网关路由表。

- 

调用[DissociateRouteTableFromGateway](products/vpc/documents/developer-reference/api-vpc-2016-04-28-dissociateroutetablefromgateway.md)解绑网关路由表。

### Terraform

Resource：[alicloud_vpc_gateway_route_table_attachment](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_gateway_route_table_attachment)# 指定IPv4网关所在的地域 provider "alicloud" { region = "cn-hangzhou" } # 指定IPv4网关的ID variable "ipv4_gateway_id" { default = "ipv4gw-hp3v******" # 修改为IPv4网关的实际ID } # 指定网关路由表的ID variable "route_table_id" { default = "vtb-hp3w******" # 修改为网关路由表的实际ID } # 绑定网关路由表 resource "alicloud_vpc_gateway_route_table_attachment" "example_attachment" { ipv4_gateway_id = var.ipv4_gateway_id route_table_id = var.route_table_id }

## 更多信息

### 使用限制

- 

一个VPC下只支持创建一个IPv4网关，且一个IPv4网关仅能关联一个VPC。

- 

VPC内存在[EIP](products/eip/documents/associate-an-eip-with-a-secondary-eni-1.md)[网卡可见模式](products/eip/documents/associate-an-eip-with-a-secondary-eni-1.md)的资源时，不支持创建IPv4网关。

例如，VPC中的公网NAT网关的EIP绑定模式为多 EIP 网卡可见模式时，不兼容IPv4网关。需要调用[ModifyNatGatewayAttribute](products/nat-gateway/documents/developer-reference/api-vpc-2016-04-28-modifynatgatewayattribute-natgws.md)，修改EipBindMode为NAT模式，使其兼容IPv4网关。

- 

多账号共享VPC场景下，资源所有者可以创建IPv4网关或对已创建的IPv4网关进行修改或删除，而资源使用者对IPv4网关没有操作权限。

- 

通过EIP或者任播弹性公网IP绑定私网传统型负载均衡CLB时：

- 

在英国（伦敦）、日本（东京）、沙特（利雅得）- 合作伙伴运营、马来西亚（吉隆坡）、华北5（呼和浩特）、美国（弗吉尼亚），公网访问流量同样受 IPv4 网关的限制。

支持的地域持续变更中。

- 

部署在公有交换机的私网 CLB，绑定公网 IP 即可实现公网访问。

- 

部署在私有交换机的私网 CLB，即使绑定公网 IP 也无法实现公网访问。可配置路由指向公网 NAT 网关，将访问公网的流量路由至公网 NAT 网关，使用公网NAT网关绑定的公网 IP 实现公网访问。

- 

其他地域，公网访问流量不受 IPv4 网关的限制。

### 计费说明

IPv4网关不收取费用。

公网流量费用由公网 IP 产生，例如EIP或ECS/CLB固定公网IP，详情参考对应产品计费文档。

### 支持的地域

| 区域 | 支持 IPv4 网关的地域 |
| --- | --- |
| 亚太-中国 | 华东 1（杭州） 、 华东 2（上海） 、 华东 5 （南京-本地地域-关停中） 、 华北 1（青岛） 、 华北 2（北京） 、 华北 3（张家口） 、 华北 5（呼和浩特） 、 华北 6（乌兰察布） 、 华南 1（深圳） 、 华南 2（河源） 、 华南 3（广州） 、 西南 1（成都） 、 西北 2（中卫） 、 中国香港 、 华中 1（武汉-本地地域） 、 华东 6（福州-本地地域-关停中） |
| 亚太-其他 | 日本（东京） 、 韩国（首尔） 、 新加坡 、 马来西亚（吉隆坡） 、 印度尼西亚（雅加达） 、 菲律宾（马尼拉） 、 泰国（曼谷） 、 马来西亚（柔佛州） |
| 欧洲与美洲 | 德国（法兰克福） 、 英国（伦敦） 、 法国（巴黎） 、 美国（硅谷） 、 美国（弗吉尼亚） 、 墨西哥 |
| 中东 | 阿联酋（迪拜） 、 沙特（利雅得）- 合作伙伴运营 |


### 配额

| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| 无 | 单个 VPC 支持的 IPv4 网关个数 | 1 个 | 无法提升 |
| 单个 IPv4 网关支持的网关路由表个数 | 1 个 |  |  |


[上一篇：公网访问](products/vpc/documents/public-network-access.md)[下一篇：VPC互连](products/vpc/documents/cross-vpc-interconnection-overview.md)

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
