# 专有网络与交换机-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/vpc-and-vswitch

# 专有网络与交换机
专有网络VPC是专有的云上私有网络，用户可以完全掌控自己的专有网络。专有网络是地域级别的资源，在专有网络中可以创建与使用阿里云产品资源，如云服务器ECS实例、云数据库RDS实例等。
交换机vSwitch是可用区级别的资源，可以使用交换机来划分子网，同一VPC内的不同交换机之间内网互通。通过在多个不同可用区的交换机中同时部署云产品资源，可以避免应用受到单一可用区故障的影响。
## 网络规划
合理的网络规划需要避免网段冲突并保障网络的可扩展性，网络规划不当将会导致后期极高的重建成本。因此，建议在创建专有网络之前先进行[网络规划](vpc-network-planning.md)。
## 创建/删除专有网络与交换机
### 控制台
创建专有网络和交换机
前往专有网络控制台的[创建专有网络](https://vpc.console.aliyun.com/vpc/cn-hangzhou/vpcs/new)页面。
配置专有网络：
地域：选择计划创建云资源的地域。
IPv4网段：选择控制台提供的建议网段，或根据需要输入自定义网段。在多VPC互通等场景下，建议配置与已有VPC不重叠的网段来避免VPC互通时的网段冲突问题。为了避免网段冲突、保障网络的可扩展性，建议[结合](vpc-and-vswitch.md)[IPAM](vpc-and-vswitch.md)[创建专有网络](vpc-and-vswitch.md)。
1、建议使用[RFC1918](https://www.rfc-editor.org/rfc/rfc1918)中指定的私有IPv4地址作为VPC的网段，网络掩码使用16~28位。如10.0.0.0/16、172.16.0.0/16、192.168.0.0/16。2、不能使用100.64.0.0/10、224.0.0.0/4、127.0.0.0/8或169.254.0.0/16网段作为VPC的IPv4网段。
配置交换机：
可用区：后续用于创建云资源的可用区。需根据所需资源在对应可用区的支持状态及库存情况（是否售罄）来选择可用区。
IPv4网段：选择控制台默认的网段，或根据需要调整网段范围。
添加更多交换机：为了避免应用受到单可用区故障的影响，建议创建分布在不同可用区的多个交换机。可以在创建专有网络的过程中，创建交换机；也可以后续在[专有网络控制台-交换机](https://vpc.console.aliyun.com/vpc/cn-hangzhou/switches)中，添加更多交换机。
删除专有网络和交换机
在目标专有网络和交换机的操作列或详情页单击删除，系统将校验是否存在未删除的云产品资源或关联资源。如有依赖资源时，需要完全释放资源后，才可删除专有网络和交换机。
1、删除交换机前，需要确保交换机未共享、未绑定自定义路由表和网络ACL并且交换机内的云产品资源已释放。2、删除专有网络前，需要确保VPC内资源已释放完成，且已取消与云企业网等网络服务的关联。
## API
与控制台逻辑不同的是，使用CreateVpc仅创建一个空的专有网络，还需要使用CreateVSwitch创建交换机。
依次调用[CreateVpc](developer-reference/api-vpc-2016-04-28-createvpc.md)和[CreateVSwitch](developer-reference/api-vpc-2016-04-28-createvswitch.md)创建专有网络和交换机。
依次调用[DeleteVSwitch](developer-reference/api-vpc-2016-04-28-deletevswitch.md)和[DeleteVpc](developer-reference/api-vpc-2016-04-28-deletevpc.md)删除交换机和专有网络。
1、删除交换机前，需要确保交换机未共享、未绑定自定义路由表和网络ACL并且交换机内的云产品资源已释放。2、删除专有网络前，需要确保VPC内资源已释放完成，且已取消与云企业网等网络服务的关联。
### Terraform
Resources：[alicloud_vpc](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc)、[alicloud_vswitch](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vswitch)Data Sources：[alicloud_zones](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/zones)# 指定创建VPC的地域 provider "alicloud" { region = "cn-hangzhou" } # 根据数据源自动获取可以创建交换机的可用区列表 data "alicloud_zones" "available_zones" { available_resource_creation = "VSwitch" # 查询VPC内可创建的可用区 # available_instance_type = "ecs.g7.large" # 查询VPC内可创建ECS实例的可用区 # available_resource_creation = "slb" # 查询VPC内可创建SLB实例的可用区 } # 创建VPC resource "alicloud_vpc" "example_vpc" { vpc_name = "example_vpc_name" cidr_block = "10.0.0.0/16" #指定网段 } # 创建交换机 resource "alicloud_vswitch" "example_vswitch" { vswitch_name = "example_vswitch_name" cidr_block = "10.0.0.0/24" # 指定网段 vpc_id = alicloud_vpc.example_vpc.id # 指定交换机所属VPC的实例ID zone_id = data.alicloud_zones.available_zones.zones.0.id # 指定交换机所属可用区 }
## 开启/关闭IPv6
为专有网络和交换机开启IPv6后，默认仅支持私网通信。如需公网通信，可[开通](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-dvo-wjp-zcb)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-dvo-wjp-zcb)[公网带宽](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-dvo-wjp-zcb)。
[支持](regions-that-support-vpc-features.md)[IPv4/IPv6](regions-that-support-vpc-features.md)[双栈的地域](regions-that-support-vpc-features.md)。
### 控制台
开启IPv6
创建专有网络和交换机时，可以选择以下方式开启IPv6：
使用系统分配的 IPv6 地址段，并下拉选择分配BGP(多线)，系统将自动创建[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)[网关](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)并分配IPv6网段。
为了统一管理地址资源，可以使用IPAM 分配的 IPv6 地址段，选择预置了IPv6 CIDR的地址池并配置地址掩码或指定CIDR，从地址池中分配IPv6网段。
针对已创建的专有网络，可以在目标专有网络的IPv6网段列单击开通IPv6：
选择系统分配的 IPv6 地址段或IPAM 分配的 IPv6 地址段。
由系统分配时，可以勾选自动开启专有网络内所有交换机IPv6功能。未勾选或由IPAM分配时，需要在目标交换机的IPv6网段列单击开通IPv6，为交换机开启IPv6。
关闭IPv6
在目标专有网络/交换机的IPv6网段列单击关闭IPv6，但关闭专有网络的IPv6，需要所有交换机关闭IPv6，并删除该专有网络下的IPv6网关。
### API
与控制台逻辑不同的是，调用API为专有网络和交换机开启IPv6后，将不会自动创建IPv6网关，需调用[CreateIpv6Gateway](https://help.aliyun.com/zh/ipv6-gateway/developer-reference/api-vpc-2016-04-28-createipv6gateway-ipv6s)自行创建。
创建专有网络和交换机时，调整[CreateVpc](developer-reference/api-vpc-2016-04-28-createvpc.md)和[CreateVSwitch](developer-reference/api-vpc-2016-04-28-createvswitch.md)的EnableIPv6参数开启/关闭IPv6。创建专有网络时，传入Ipv6IpamPoolId和Ipv6CidrMask将从指定的IPv6地址池中为VPC分配IPv6网段。
针对已创建的专有网络和交换机，调整[ModifyVpcAttribute](developer-reference/api-vpc-2016-04-28-modifyvpcattribute.md)与[ModifyVSwitchAttribute](developer-reference/api-vpc-2016-04-28-modifyvswitchattribute.md)的EnableIPv6参数开启/关闭IPv6。如需从指定IPv6地址池中为VPC分配IPv6网段，调用[AssociateVpcCidrBlock](developer-reference/api-vpc-2016-04-28-associatevpccidrblock.md)添加。
### Terraform
Terraform当前仅支持系统分配IPv6地址段，暂不支持从IPAM分配IPv6地址段。Resources：[alicloud_vpc](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc)、[alicloud_vswitch](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vswitch)Data Sources：[alicloud_zones](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/zones)
# 指定创建VPC的地域 provider "alicloud" { region = "cn-hangzhou" } # 根据数据源自动获取可以创建交换机的可用区列表 data "alicloud_zones" "available_zones" { available_resource_creation = "VSwitch" # 查询VPC内可创建的可用区 # available_instance_type = "ecs.g7.large" # 查询VPC内可创建ECS实例的可用区 # available_resource_creation = "slb" # 查询VPC内可创建SLB实例的可用区 } # 创建双栈VPC resource "alicloud_vpc" "example_vpc" { vpc_name = "example_vpc_name" cidr_block = "10.0.0.0/16" enable_ipv6 = true # 开启IPv6，false为关闭IPv6 ipv6_isp = "BGP" # 指定IPv6网段类型 } # 创建双栈交换机 resource "alicloud_vswitch" "example_vswitch" { vswitch_name = "example_vswitch_name" cidr_block = "10.0.0.0/24" vpc_id = alicloud_vpc.example_vpc.id zone_id = data.alicloud_zones.available_zones.zones.0.id enable_ipv6 = true # 开启IPv6，false为关闭IPv6 ipv6_cidr_block_mask = 1 # 指定交换机IPv6网段的最后8比特位 }
## 修改网段
创建专有网络时，为其指定的IPv4网段是专有网络的主网段。控制台不支持修改专有网络的主网段，但可以调整[ModifyVpcAttribute](developer-reference/api-vpc-2016-04-28-modifyvpcattribute.md)接口的CidrBlock参数，在主网段内放大或缩小网段。需确保缩小后的网段包含已经使用的IP地址。
专有网络的IPv6网段、交换机的IPv4/IPv6网段，均不支持修改。
### 使用附加网段扩充网段地址
当专有网络的可用IP地址数不足以满足扩展的业务规模，或者前期网络规划不当导致地址不足时，可以使用附加网段扩充VPC地址空间。
附加网段与主网段同时生效，可用于创建交换机、部署ECS等云产品资源。
1、不能使用100.64.0.0/10、224.0.0.0/4、127.0.0.0/8或169.254.0.0/16网段作为IPv4附加网段。2、附加网段的地址块不能与主网段重叠。3、每个专有网络默认支持添加[5](understanding-vpc-quotas-in-alibaba-cloud.md)[个](understanding-vpc-quotas-in-alibaba-cloud.md)[IPv4](understanding-vpc-quotas-in-alibaba-cloud.md)[附加网段，5](understanding-vpc-quotas-in-alibaba-cloud.md)[个](understanding-vpc-quotas-in-alibaba-cloud.md)[IPv6](understanding-vpc-quotas-in-alibaba-cloud.md)[附加网段](understanding-vpc-quotas-in-alibaba-cloud.md)。
### 控制台
添加附加网段
在目标专有网络的基本信息页面，单击网段管理页签，可以添加IPv4或IPv6附加网段。
针对IPv4附加网段，添加时有3种方式：
推荐网段：在10.0.0.0/16、172.16.0.0/16、192.168.0.0/16中选择其一快速添加。
高级配置网段：自定义配置附加网段。
IPAM 分配的 IPv4 地址段：使用[IPAM](ip-address-management-ipam.md)可以避免分配的网段出现冲突。如果已有预置CIDR的IPAM地址池，建议选择此项。配置时，首先选择地址池，再配置IPv4地址掩码。
针对IPv6附加网段：
如果专有网络未开通IPv6功能，请单击开通IPv6，可以选择系统分配的 IPv6 地址段，并下拉选择分配BGP(多线)。为了统一管理地址资源，可以选择IPAM 分配的 IPv6 地址段，首先选择地址池，再选择地址掩码或指定CIDR。
可以勾选自动开启专有网络内所有交换机IPv6功能；或者在目标交换机的IPv6网段列单击开通IPv6，来单独为交换机开启IPv6功能。
针对已开通IPv6功能的专有网络，请单击添加IPv6网段，选择系统分配的 IPv6 地址段或IPAM 分配的 IPv6 地址段。
删除附加网段
在目标专有网络的基本信息页面，单击网段管理的IPv4网段页签或IPv6网段页签，找到需要删除的附加网段，在操作列单击删除。
## API
调用[AssociateVpcCidrBlock](developer-reference/api-vpc-2016-04-28-associatevpccidrblock.md)添加附加网段。
调用[UnassociateVpcCidrBlock](developer-reference/api-vpc-2016-04-28-unassociatevpccidrblock.md)删除附加网段。
## Terraform
Terraform当前仅支持创建IPv4附加网段，暂不支持创建IPv6附加网段。Resources：[alicloud_vpc_ipv4_cidr_block](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_ipv4_cidr_block)# 指定创建VPC的地域 provider "alicloud" { region = "cn-hangzhou" } # 指定VPC的ID variable "vpc_id" { default = "vpc-xxx" # 修改为VPC的实际ID } # 在VPC中创建附加网段 resource "alicloud_vpc_ipv4_cidr_block" "example_secondary_cidr_block" { vpc_id = var.vpc_id secondary_cidr_block = "192.168.0.0/16" # 指定附加网段 }
## 预留网段
在交换机中预留网段，可以确保此网段不被其他资源的创建所占用。预留的网段，当前仅用于给弹性网卡的辅助私网IP分配[IP](../../ecs/documents/user-guide/ip-prefix.md)[前缀](../../ecs/documents/user-guide/ip-prefix.md)。
1、预留网段内不能包含交换机的[系统保留地址](vpc-and-vswitch.md)。2、单个 VPC 支持创建的 IPv4、IPv6最大预留网段数目均为100个。3、IPv4预留网段的掩码长度最大不超过28，IPv6网段掩码长度且最大不超过80。
### 控制台
创建预留网段
在目标交换机的基本信息页面，单击预留网段页签，添加IPv4或者IPv6的预留网段。添加时有2种方式：
指定地址段：精确控制要预留的地址段。
指定掩码长度：系统自动从可用网段中划分预留网段。
针对IPv6网段，如果交换机未开通IPv6功能，请单击开通IPv6。在弹出的开通IPv6对话框中设置交换机IPv6网段。
如果专有网络未开通IPv6功能，请在弹出的开通IPv6对话框中，先将IPv6网段类型设为默认的分配BGP(多线)，再设置交换机IPv6网段。
查看已占用IP段
在目标交换机的基本信息页面，单击预留网段的IPv4网段页签或IPv6网段页签，找到目标预留网段，在操作列单击查看已占用IP，可查看已占用的IP段及对应的弹性网卡。
删除预留网段
删除预留网段前，请确保预留网段已无IP段占用。
在目标交换机的基本信息页面，单击预留网段的IPv4网段页签或IPv6网段页签，找到需要删除的预留网段，在操作列单击删除。
## API
调用[CreateVSwitchCidrReservation](developer-reference/api-vpc-2016-04-28-createvswitchcidrreservation.md)创建预留网段。
调用[GetVSwitchCidrReservationUsage](developer-reference/api-vpc-2016-04-28-getvswitchcidrreservationusage.md)查看已占用IP段。
调用[DeleteVSwitchCidrReservation](developer-reference/api-vpc-2016-04-28-deletevswitchcidrreservation.md)删除预留网段。
## Terraform
Resources:[alicloud_vpc_vswitch_cidr_reservation](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_vswitch_cidr_reservation)# 指定创建VPC的地域 provider "alicloud" { region = "cn-hangzhou" # 资源所在的地域 } # 指定交换机的ID variable "vsw_id" { default = "vsw-xxx" # 修改为交换机的实际ID } # 创建预留网段 resource "alicloud_vpc_vswitch_cidr_reservation" "example_cidr_reservation" { vswitch_id = var.vsw_id ip_version = "IPv4" cidr_reservation_cidr = "10.0.0.128/26" # 指定预留网段 }
## 结合IPAM创建专有网络
IPAM 是云上 IP 地址管理的工具，可以自动化分配与管理 IP 地址，简化网络管理流程并避免地址冲突。[结合](use-ipam-to-create-a-vpc.md)[IPAM](use-ipam-to-create-a-vpc.md)[规划](use-ipam-to-create-a-vpc.md)，创建IPAM和IPAM地址池后，可以从IPAM地址池为专有网络分配IPv4网段和IPv6网段。
### 控制台
创建专有网络前，请确保已通过[IPAM](https://ipam.console.aliyun.com/cn-hangzhou/ipam)[控制台](https://ipam.console.aliyun.com/cn-hangzhou/ipam)创建IPAM和IPAM地址池。
前往专有网络控制台的[创建专有网络](https://vpc.console.aliyun.com/vpc/cn-hangzhou/vpcs/new)页面。
分配IPv4网段：使用IPAM 分配的 IPv4 地址段，选择IPAM地址池并配置掩码，系统会默认分配指定掩码范围内第一个可用的CIDR，也可以在地址池预置CIDR内，调整IPv4网段。
需开启IPv6时：可以选择IPAM 分配的 IPv6 地址段，首先选择IPv6地址池，再配置地址掩码或指定CIDR。
## API
如已创建过IPAM地址池：
分配IPv4网段：可在调用[CreateVpc](developer-reference/api-vpc-2016-04-28-createvpc.md)时传入Ipv4IpamPoolId来指定IPAM地址池，同时传入Ipv4CidrMask来指定掩码从IPAM地址池中分配地址作为新建VPC的IPv4网段。也可以传入CidrBlock来指定VPC使用的网段，而不是通过指定掩码自动分配网段。
分配IPv6网段：同时传入Ipv6IpamPoolId和Ipv6CidrMask，将从指定的IPv6地址池中为VPC分配IPv6网段。
如未创建过IPAM地址池，可依次调用如下API来创建IPAM地址池，然后参考上述逻辑创建专有网络。
[OpenVpcIpamService-开通](developer-reference/api-vpcipam-2023-02-28-openvpcipamservice.md)[IPAM](developer-reference/api-vpcipam-2023-02-28-openvpcipamservice.md)[功能](developer-reference/api-vpcipam-2023-02-28-openvpcipamservice.md)
[CreateIpam-创建一个](developer-reference/api-vpcipam-2023-02-28-createipam.md)[IPAM](developer-reference/api-vpcipam-2023-02-28-createipam.md)[实例](developer-reference/api-vpcipam-2023-02-28-createipam.md)
[CreateIpamPool-创建](developer-reference/api-vpcipam-2023-02-28-createipampool.md)[IPAM](developer-reference/api-vpcipam-2023-02-28-createipampool.md)[地址池](developer-reference/api-vpcipam-2023-02-28-createipampool.md)
[AddIpamPoolCidr-为](developer-reference/api-vpcipam-2023-02-28-addipampoolcidr.md)[IPAM](developer-reference/api-vpcipam-2023-02-28-addipampoolcidr.md)[地址池预置](developer-reference/api-vpcipam-2023-02-28-addipampoolcidr.md)[CIDR](developer-reference/api-vpcipam-2023-02-28-addipampoolcidr.md)[地址段](developer-reference/api-vpcipam-2023-02-28-addipampoolcidr.md)
### Terraform
Terraform当前仅支持从IPAM地址池分配IPv4地址段，暂不支持分配IPv6地址段。Resources：[vpc_ipam_ipam](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_ipam_ipam)、[alicloud_vpc_ipam_ipam_pool](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_ipam_ipam_pool)、[alicloud_vpc_ipam_ipam_pool_cidr](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_ipam_ipam_pool_cidr)、[alicloud_vpc](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc)# 指定创建IPAM、IPAM 地址池、VPC的地域 provider "alicloud" { region = "cn-hangzhou" } # 创建IPAM resource "alicloud_vpc_ipam_ipam" "example_ipam" { ipam_name = "example_ipam_name" operating_region_list = ["cn-hangzhou"] # 指定IPAM的生效地域 } # 创建IPAM地址池 resource "alicloud_vpc_ipam_ipam_pool" "example_parentIpamPool" { ipam_scope_id = alicloud_vpc_ipam_ipam.example_ipam.private_default_scope_id # 指定IPAM地址池的作用范围 ipam_pool_name = "example_parentIpamPool_name" pool_region_id = alicloud_vpc_ipam_ipam.example_ipam.region_id # 指定IPAM地址池的生效地域 ip_version = "IPv4" # 指定IPAM地址池的版本 } # 为IPAM地址池分配CIDR resource "alicloud_vpc_ipam_ipam_pool_cidr" "example_ipamPoolCidr" { cidr = "10.0.0.0/16" # 指定CIDR ipam_pool_id = alicloud_vpc_ipam_ipam_pool.example_parentIpamPool.id # 指定IPAM地址池的ID } # 创建VPC resource "alicloud_vpc" "example_ipam_vpc" { vpc_name = "example_ipam_vpc_name" ipv4_ipam_pool_id = alicloud_vpc_ipam_ipam_pool.example_parentIpamPool.id # 指定IPAM地址池的ID ipv4_cidr_mask = 24 # IPv4网络掩码 }
## 更多信息
### 默认专有网络与默认交换机
默认专有网络和交换机能快速实现业务验证与部署，但需要长期网络服务支撑或承载核心生产系统时，建议根据业务架构需求，自定义创建专有网络和交换机，通过精细化网络规划实现资源隔离、安全管控及弹性扩展能力，从而构建符合业务需求的云上网络环境。
每个地域只能创建一个默认专有网络，每个可用区只能创建一个默认交换机。默认专有网络和交换机不占用阿里云分配的配额。
在尚未创建任何专有网络的地域创建ECS、CLB、RDS实例时，可以选择由阿里云创建默认专有网络和交换机。此方式创建的默认专有网络网段固定为172.16.0.0/12。
可以在尚未创建默认专有网络的地域，调用[CreateDefaultVpc](developer-reference/api-vpc-2016-04-28-createdefaultvpc.md)和[CreateDefaultVSwitch](developer-reference/api-vpc-2016-04-28-createdefaultvswitch.md)创建默认专有网络和交换机。此方式创建的默认专有网络的网段为172.xx.0.0/16。
除上述方式外，自行创建的专有网络和交换机均为非默认。默认专有网络和交换机可以删除，但无法将默认专有网络和交换机和非默认专有网络和交换机互相转换。
### 系统保留地址
交换机网段的地址空间中存在系统保留地址，无法将系统保留地址分配给ECS等云资源。
针对IPv4，每个交换机的第1个和最后3个IP地址为系统保留地址。
例如，交换机的网段为192.168.1.0/24，则192.168.1.0、192.168.1.253、192.168.1.254和192.168.1.255这4个地址是系统保留地址。
针对IPv6，每个交换机的第1个和最后9个IP地址为系统保留地址。
例如，交换机的IPv6网段为2408:xxxx:xxxx:6eff::/64，则第1个2408:xxxx:xxxx:6eff::和最后9个2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fff7、2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fff8、2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fff9、2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fffa、2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fffb、2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fffc、2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fffd、2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fffe和2408:xxxx:xxxx:6eff:ffff:ffff:ffff:ffff为系统保留IP。
### 跨账号授权
在将VPC连接到跨账号的云企业网CEN、边界路由器VBR、专线网关ECR之前，需要先在VPC中进行跨账号授权。
授权操作可参考：[为跨账号云企业网实例授权](../../cen/documents/user-guide/grant-permissions-on-a-network-instance-that-belongs-to-another-account.md)、[为跨账号边界路由器](https://help.aliyun.com/zh/express-connect/user-guide/attach-a-vbr-to-a-vpc-that-belongs-to-a-different-account#section-71v-2hh-g4h)[VBR](https://help.aliyun.com/zh/express-connect/user-guide/attach-a-vbr-to-a-vpc-that-belongs-to-a-different-account#section-71v-2hh-g4h)[实例授权](https://help.aliyun.com/zh/express-connect/user-guide/attach-a-vbr-to-a-vpc-that-belongs-to-a-different-account#section-71v-2hh-g4h)、[为跨账号专线网关](https://help.aliyun.com/zh/express-connect/user-guide/cross-account-ecr-authorization#02c05250e4t35)[ECR](https://help.aliyun.com/zh/express-connect/user-guide/cross-account-ecr-authorization#02c05250e4t35)[实例授权](https://help.aliyun.com/zh/express-connect/user-guide/cross-account-ecr-authorization#02c05250e4t35)。
授权成功后，对方账号在[创建](../../cen/documents/user-guide/connect-vpcs.md)[VPC](../../cen/documents/user-guide/connect-vpcs.md)[连接](../../cen/documents/user-guide/connect-vpcs.md)、[创建](https://help.aliyun.com/zh/express-connect/user-guide/create-and-manage-a-vbr-to-vpc-connection#title-oiq-5wv-0kl)[VBR](https://help.aliyun.com/zh/express-connect/user-guide/create-and-manage-a-vbr-to-vpc-connection#title-oiq-5wv-0kl)[上连](https://help.aliyun.com/zh/express-connect/user-guide/create-and-manage-a-vbr-to-vpc-connection#title-oiq-5wv-0kl)、[将](https://help.aliyun.com/zh/express-connect/user-guide/create-and-manage-the-leased-line-gateway-ecr#4e746cc312xor)[VPC](https://help.aliyun.com/zh/express-connect/user-guide/create-and-manage-the-leased-line-gateway-ecr#4e746cc312xor)[关联到](https://help.aliyun.com/zh/express-connect/user-guide/create-and-manage-the-leased-line-gateway-ecr#4e746cc312xor)[ECR](https://help.aliyun.com/zh/express-connect/user-guide/create-and-manage-the-leased-line-gateway-ecr#4e746cc312xor)时，才可以选择本账号的VPC实例。
1、此处的账号指的是阿里云账号（主账号），而非RAM用户（子账号）。2、跨账号授权不支持跨站点，即不支持中国站和国际站之间跨账号。
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
