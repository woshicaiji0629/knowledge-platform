# DHCP选项集与DNS主机名-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/dhcp-option-set-and-dns-hostname

# DHCP选项集与DNS主机名
为降低 ECS 实例间通信对固定 IP 的依赖，您可以使用 DHCP 选项集为 ECS 统一配置 DNS 服务器 IP 和搜索域，简化网络管理工作。使用主机名访问 ECS 时，系统将补全搜索域，向指定的 DNS 服务器查询完整域名与 IP 的映射关系。
## 工作原理
DHCP选项集（DHCP Options Set）为关联 VPC 内的 ECS 实例统一配置DNS 域名服务器IP、域名等参数后，实例间可以使用主机名/完整域名互访，无需依赖固定IP。
| 序号 | 说明 |
| --- | --- |
| ① | DHCP 选项集关联至 VPC，VPC 中的 ECS 与 DHCP 服务器交互，获取 DHCP 选项集中的网络配置信息（包括域名、DNS 服务器 IP 等网络相关配置信息），并写入 ECS 的系统配置。 |
| ② | ECS 实例向 DNS 服务器发送查询请求，以获取 DNS 主机名与 IP 地址的映射关系。DNS 服务器将 DNS 主机名解析到对应的 IP 地址。 |
| ③ | 根据解析结果，访问对应的 ECS 实例。 |
### 配置域名：使用主机名通信
完整的私网域名包括主机名（host name）和域名（domain name）两部分，例如host01.host.prvz中，主机名为host01，域名为host.prvz。
在 DNS 服务器中配置 ECS 域名解析记录后，ECS 可通过完整的私网域名被访问。如需简化为仅使用主机名通信，您可以使用vim /etc/resolv.conf修改 ECS 的 DNS 配置文件，添加search host.prvz，将host.prvz设置成 DNS 搜索域（search domain）。
但手动配置每个 ECS，可能存在配置效率低下、配置不统一等问题。在关联的 DHCP 选项集中配置域名后，VPC 内的 ECS 实例可以通过 DHCP 获取 DHCP 选项集中配置的域名，写入/etc/resolv.conf，统一设置 DNS 搜索域。使用主机名访问 ECS 时，系统将补全搜索域，向指定的 DNS 服务器查询完整域名与 IP 的映射关系。
### 配置DNS服务器IP：查询域名解析记录
DNS 服务器维护域名解析记录。当 ECS 执行ping host01.host.prvz时，会向指定的 DNS 服务器发送查询请求，DNS 服务器将返回对应的 IP 地址。
使用官方镜像创建 ECS 时，阿里云会通过[DHCP](https://www.rfc-editor.org/rfc/rfc2131)自动为 ECS 配置默认 DNS 服务器，其 IP 为 100.100.2.136 和 100.100.2.138。
| 对比项 | 启用 DNS 主机名 | 内网 DNS 解析（Private DNS） | 自建 DNS 服务 |
| --- | --- | --- | --- |
| DHCP 选项集类型 | 默认 DHCP 选项集 | 自定义 DHCP 选项集 | 自定义 DHCP 选项集 |
| 域名配置 | ECS 私网域名 [regionID].ecs.internal 默认 DNS 服务器 | 自定义域名 默认 DNS 服务器 | 自定义域名 自建 DNS 服务器 |
| 计费 | 无需支付域名费用 | 结合添加的域名数量、解析请求量 [收取费用](https://help.aliyun.com/zh/dns/product-billing) | 无需支付域名费用 |
| 是否支持跨 VPC、混合云私网域名通信 | 不支持 | 支持 | 支持 |
DNS 查询性能取决于使用的DNS服务器。阿里云默认DNS服务器的查询性能，可参考[内网](https://help.aliyun.com/zh/dns/limits-pvtz#td-sss-vz2-tsl)[DNS](https://help.aliyun.com/zh/dns/limits-pvtz#td-sss-vz2-tsl)[解析服务的使用限制](https://help.aliyun.com/zh/dns/limits-pvtz#td-sss-vz2-tsl)。
## 创建/删除 DHCP 选项集
为降低对固定 IP 的依赖、使用主机名/完整域名互访，您可以使用 DHCP 选项集为关联 VPC 内的 ECS 统一配置 DNS 服务器 IP 和搜索域。ECS 执行ping <hostname>时，系统将补全搜索域（例如hostname.example.com），向指定的 DNS 服务器查询域名与 IP 的映射关系。
一个DHCP选项集可以关联多个同地域VPC，但一个VPC只能关联一个同地域DHCP选项集。
### 控制台
创建 DHCP 选项集
每个地域首次为 VPC 启用 DNS 主机名时，自动创建默认 DHCP 选项集并关联至 VPC。默认 DHCP 选项集不支持修改，您可以前往[专有网络控制台 - DHCP 选项集](https://vpc.console.aliyun.com/dhcp/cn-hangzhou/dhcps)，创建DHCP选项集，配置与 DNS 解析服务对应的域名和DNS 域名服务器IP。
如果 VPC 已关联其他 DHCP 选项集，VPC 启用 DNS 主机名后，将不会关联默认 DHCP 选项集，您需要自行修改关联关系。
关联专有网络
VPC 与 DHCP 选项集的关联关系，可在目标 VPC 详情页的DHCP选项集参数项、目标 DHCP 选项集的操作列或详情页，进行建立、更改或解除。
关联关系变更后，新建 ECS 会自动使用最新配置，存量 ECS 需要通过sudo dhclient -r eth0 && sudo dhclient eth0重启实例中 DHCP 进程，才能使用最新配置；解除关联关系后，阿里云会通过 DHCP 为 ECS 指定默认 DNS 服务器。确保不影响业务的前提下，您也可以通过重启实例或重启网络服务，确保存量 ECS 使用最新配置。
常见操作系统重启网络服务的命令
| 操作系统 | Version | 重启网络服务命令 |
| --- | --- | --- |
| CentOS | 6 | service network restart |
| 7 | systemctl restart network |  |
| 8 | systemctl restart NetworkManager |  |
| Debian | 8 | systemctl restart networking |
| 9 | systemctl restart networking |  |
| 10 | systemctl restart networking |  |
| Ubuntu | 14 | service networking restart |
| 16 | systemctl restart networking |  |
| 18 | systemctl restart systemd-networkd |  |
| 20 | systemctl restart systemd-networkd |  |
| Alibaba Cloud Linux 2 | 2 | systemctl restart network |
| Alibaba Cloud Linux 3 | 3 | systemctl restart NetworkManager |
如果 DHCP 选项集关联的 VPC 开启了[共享](vpc-sharing.md)[VPC](vpc-sharing.md)功能，则 DHCP 选项集也会对共享 VPC 内的 ECS 生效。
修改 DHCP 选项集
默认 DHCP 选项集不支持修改，自定义 DHCP 选项集指定的域名和 DNS 服务器 IP 可修改。
修改 DHCP 选项集后，关联 VPC 内的新建 ECS 会自动使用最新配置，存量 ECS 需要通过重启实例中 DHCP 进程，才能使用最新配置。确保不影响业务的前提下，您也可以通过重启实例或重启网络服务，确保存量 ECS 使用最新配置。
删除 DHCP 选项集
需先确保已解除与 VPC 的关联，在目标 DHCP 选项集的操作列或详情页，单击删除。
### API
每个地域首次为 VPC 启用 DNS 主机名时，自动创建默认 DHCP 选项集并关联至 VPC。修改 DHCP 选项集配置或变更关联关系后，新建 ECS 会自动使用最新配置，存量 ECS 需重启实例、重启实例中 DHCP 进程或重启网络服务，才能使用最新配置。
调用[CreateDhcpOptionsSet](developer-reference/api-vpc-2016-04-28-createdhcpoptionsset.md)创建 DHCP 选项集。
调用[AttachDhcpOptionsSetToVpc](developer-reference/api-vpc-2016-04-28-attachdhcpoptionssettovpc.md)将 DHCP 选项集关联到目标 VPC。
调用[DetachDhcpOptionsSetFromVpc](developer-reference/api-vpc-2016-04-28-detachdhcpoptionssetfromvpc.md)取消 DHCP 选项集与目标 VPC 的关联。
调用[ReplaceVpcDhcpOptionsSet](developer-reference/api-vpc-2016-04-28-replacevpcdhcpoptionsset.md)更改 DHCP 选项集关联的 VPC。
调用[UpdateDhcpOptionsSetAttribute](developer-reference/api-vpc-2016-04-28-updatedhcpoptionssetattribute.md)修改 DHCP 选项集配置信息。
调用[DeleteDhcpOptionsSet](developer-reference/api-vpc-2016-04-28-deletedhcpoptionsset.md)删除 DHCP 选项集。
### Terraform
Resource：[alicloud_vpc_dhcp_options_set](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_dhcp_options_set)、[alicloud_vpc_dhcp_options_set_attachment](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_dhcp_options_set_attachment)# 指定VPC的地域 provider "alicloud" { region = "cn-hangzhou" } # 创建DHCP选项集 resource "alicloud_vpc_dhcp_options_set" "test_dhcp_options_set" { dhcp_options_set_name = "test_dhcp_options_set_name" domain_name = "example.com" # 指定域名 domain_name_servers = "100.100.2.136,100.100.2.138" # 指定DNS服务器IP } # 关联DHCP选项集与VPC resource "alicloud_vpc_dhcp_options_set_attachment" "test_attachment_vpc" { vpc_id = "vpc-8vbg******" # 指定关联的VPC的实例ID dhcp_options_set_id = alicloud_vpc_dhcp_options_set.test_dhcp_options_set.id # 指定关联的DHCP选项集的实例ID }
## 启用 DNS 主机名
为实现同一VPC内通过私网域名进行通信，您可以为 VPC 启用 DNS 主机名，并在 ECS 中配置私网域名解析，由阿里云的内网 DNS 解析自动维护域名解析记录，降低域名解析记录的维护时间与成本。VPC 会关联默认 DHCP 选项集，为 ECS 指定统一的[ECS 云产品内置权威域名 [regionID].ecs.internal](../../ecs/documents/user-guide/ecs-private-domain-resolution.md)。
1、每个地域首次启用 DNS 主机名时，自动创建默认 DHCP 选项集并关联至 VPC。该地域其他 VPC 启用 DNS 主机名时，系统自动将该默认 DHCP 选项集与对应 VPC 关联。2、如果 VPC 已关联其他 DHCP 选项集，VPC 启用 DNS 主机名后，将不会关联默认 DHCP 选项集，您需要自行修改关联关系。3、暂不支持跨 VPC、混合云场景下，使用私网域名通信。
### 控制台
启用 DNS 主机名
前往[专有网络控制台](https://vpc.console.aliyun.com/vpc/cn-hangzhou/vpcs)，在目标 VPC基本信息页面，单击启用DNS 主机名。
前往[ECS](https://ecs.console.aliyun.com/server/region/cn-hangzhou)[实例管理控制台](https://ecs.console.aliyun.com/server/region/cn-hangzhou)，为 ECS 配置私网域名解析，对应 ECS 可通过主机名被同一 VPC 内的 ECS 访问。
创建实例时，展开高级选项配置私网域名解析，选择IP 格式主机名到实例主私网 IPv4 的 DNS 解析或实例 ID 格式主机名到实例主私网 IPv4的 DNS 解析。
实例 ID 无法修改；实例 IP 变化后，域名解析记录将自动更新为新 IP 格式的主机名到新 IP 的映射。实例分配 IPv6 地址后，可选择实例 ID 格式主机名到实例主私网 IPv6的 DNS 解析。
针对已创建的 ECS，在其操作列选择>实例属性>编辑实例属性，选择对应的私网域名和IP地址的映射关系。
禁用 DNS 主机名
在目标 VPC基本信息页面，单击禁用DNS 主机名，阿里云统一分配的域名将失效，无法将 ECS 私网域名解析为对应的 IP。
系统会自动解除与默认 DHCP 选项集的关联，但不会删除 DHCP 选项集。如需删除，确保已解除与所有 VPC 的关联。
### API
与控制台逻辑不同的是，调用[CreateVpc](developer-reference/api-vpc-2016-04-28-createvpc.md)创建 VPC 时，可调整EnableDnsHostname参数，启用/禁用 DNS 主机名。
调整[ModifyVpcAttribute](developer-reference/api-vpc-2016-04-28-modifyvpcattribute.md)的EnableDnsHostname参数，启用/禁用 DNS 主机名。
调用[RunInstances](../../ecs/documents/developer-reference/api-ecs-2014-05-26-runinstances.md)创建实例时，指定PrivateDnsNameOptions相关参数，配置实例的私网域名解析。
调整[ModifyInstanceAttribute](../../ecs/documents/developer-reference/api-ecs-2014-05-26-modifyinstanceattribute.md)的PrivateDnsNameOptions相关参数，配置目标 ECS 的私网域名解析。
### Terraform
ECS 私网域名解析暂不支持使用 Terraform 配置，本示例仅为 VPC 启用 DNS 主机名。Resources：[alicloud_vpc](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc)、[alicloud_vswitch](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vswitch)Data Sources：[alicloud_zones](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/zones)# 指定创建VPC的地域 provider "alicloud" { region = "cn-hangzhou" } # 创建VPC resource "alicloud_vpc" "test_vpc" { vpc_name = "test_vpc_name" cidr_block = "10.0.0.0/16" dns_hostname_status = "ENABLED" # 启用DNS主机名 }
## 使用自定义域名通信
启用 DNS 主机名生成的 ECS 私网域名无法修改，如需使用自定义域名，您可以使用阿里云的内网 DNS 解析或自建 DNS 服务。
### 使用内网 DNS 解析
为统一添加 ECS 的域名解析记录，您可以使用[内网 DNS 解析](https://help.aliyun.com/zh/dns/form-filling-mode)。该服务将结合添加的域名数量、解析请求量[收取费用](https://help.aliyun.com/zh/dns/product-billing)。
控制台
前往[内网 DNS 解析控制台](https://dnsnext.console.aliyun.com/privateDNS/zones)，单击添加域名 (Zone)，配置自定义的内网权威域名 (Zone)，并设置域名生效范围为目标 VPC。
单击目标域名 ID，您可以在ECS主机名页签，单击添加ECS主机名，系统将自动添加所选地域中 ECS 主机名与 IP 的域名解析记录，但主机名修改后，无法同步更新。您可以开启自动同步配置，系统将自动添加所选地域内的域名解析记录，且1分钟同步1次。如需使用自定义域名前缀，您可以选择解析记录页签，添加自定义主机记录。
前往[专有网络控制台 - DHCP 选项集](https://vpc.console.aliyun.com/dhcp/cn-hangzhou/dhcps)，创建DHCP选项集，配置域名为对应的内置权威域名。
在目标 DHCP 选项集的操作列选择关联专有网络，已配置域名解析记录的 ECS 可通过主机名/主机记录被关联 VPC 内的 ECS 访问。
API
依次调用如下 API，使用阿里云的内网 DNS 解析服务：
[AddZone - 添加内置权威域名](https://help.aliyun.com/zh/dns/api-pvtz-2018-01-01-addzone)
[添加解析记录](https://help.aliyun.com/zh/dns/api-pvtz-2018-01-01-addzonerecord)或[UpdateSyncEcsHostTask - 主机名同步](https://help.aliyun.com/zh/dns/api-pvtz-2018-01-01-updatesyncecshosttask)
[CreateDhcpOptionsSet - 创建 DHCP 选项集](developer-reference/api-vpc-2016-04-28-createdhcpoptionsset.md)
[AttachDhcpOptionsSetToVpc - 将 DHCP 选项集关联到 VPC](developer-reference/api-vpc-2016-04-28-attachdhcpoptionssettovpc.md)
Terraform当前不支持自动添加 ECS 主机名解析记录，您需要逐条添加自定义域名解析记录。Resource：[alicloud_pvtz_zone](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/pvtz_zone)、[alicloud_pvtz_zone_attachment](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/pvtz_zone_attachment)、[alicloud_pvtz_zone_record](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/pvtz_zone_record)、[alicloud_vpc_dhcp_options_set](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_dhcp_options_set)、[alicloud_vpc_dhcp_options_set_attachment](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_dhcp_options_set_attachment)# 指定目标VPC所在地域 provider "alicloud" { region = "cn-hangzhou" } # 配置内置权威域名 resource "alicloud_pvtz_zone" "test_pvtz_zone" { zone_name = "example.com" } # 设置域名生效范围 resource "alicloud_pvtz_zone_attachment" "test_pvtz_zone_attachment" { zone_id = alicloud_pvtz_zone.test_pvtz_zone.id vpc_ids = ["vpc-8vba******"] # 指定域名生效的VPC实例ID } # 添加域名解析记录 resource "alicloud_pvtz_zone_record" "test_pvtz_zone_record" { zone_id = alicloud_pvtz_zone.test_pvtz_zone.id rr = "abc" # 指定主机记录 type = "A" # 指定域名解析记录类型 value = "192.168.0.4" # 指定域名解析记录值 } # 创建DHCP选项集 resource "alicloud_vpc_dhcp_options_set" "test_dhcp_options_set" { dhcp_options_set_name = "test_dhcp_options_set_name" domain_name = "example.com" # 指定域名 domain_name_servers = "100.100.2.136,100.100.2.138" # 指定阿里云默认DNS服务器IP } # 关联DHCP选项集与VPC resource "alicloud_vpc_dhcp_options_set_attachment" "test_attachment_vpc" { vpc_id = "vpc-8vba******" # 指定关联的VPC的实例ID dhcp_options_set_id = alicloud_vpc_dhcp_options_set.test_dhcp_options_set.id # 指定关联的DHCP选项集的实例ID }
### 使用自建 DNS 服务
如果业务需要灵活的DNS调度策略，例如根据地理位置、网络质量、服务器负载等因素动态返回最优IP，您可以自建DNS服务器，但需自行维护域名解析记录，并确保服务可靠性。您可以参考以下示例部署自建DNS服务，并使用DHCP选项集为ECS实例指定自建DNS服务器IP和自定义域名。
使用BIND部署自建 DNS 服务示例
执行yum install -y bind bind-utils安装 BIND。
执行vim /etc/named.conf修改主配置文件的配置项。
listen-on port 53 { any; }; # 监听所有网络接口的53端口 allow-query { any; }; # 允许任何IP进行DNS查询
执行vim /etc/named.rfc1912.zones配置区域文件。
// 自定义域名 zone "example.com" IN { type master; file "example.com.zone"; }; zone "0.168.192.in-addr.arpa" IN { type master; file "0.168.192.zone"; };
执行cp -p /var/named/named.localhost /var/named/example.com.zone与vim /var/named/example.com.zone配置正向解析文件。
$TTL 1D @ IN SOA example.com. admin.example.com. ( 1 ; serial 1D ; refresh 1H ; retry 1W ; expire 3H ) ; minimum NS dns.example.com. Web01 A 192.168.0.2; Web02 A 192.168.0.3;
执行cp -p /var/named/named.empty /var/named/0.168.192.zone与vim /var/named/0.168.192.zone配置反向解析文件。
$TTL 3H @ IN SOA 0.168.192.in-addr.arpa. admin.zjq.com. ( 1 ; serial 1D ; refresh 1H ; retry 1W ; expire 3H ) ; minimum NS dns.example.com. 2 PTR Web01.example.com. 3 PTR Web02.example.com.
执行systemctl restart named重启 BIND 服务。
如果您在使用自建 DNS 服务的同时希望使用阿里云 DNS 服务，需要为自建 DNS 服务器配置转发规则，将自定义域名以外的查询请求转发至阿里云默认DNS服务器。
为自建 DNS 服务器配置转发规则
执行vim /etc/named.conf命令，修改配置文件。
// 默认转发：其他请求转发到默认 DNS 服务器 options { forwarders { 100.100.2.136; 100.100.2.138; }; # 阿里云VPC默认DNS forward only; }; // 配置自建 DNS 权威解析，"example.com"需替换为自定义域名 zone "example.com" { type master; file "example.com.zone"; # 域名解析配置文件 };
在自定义 DHCP 选项集中指定 DNS 服务器 IP 时，需注意：1、控制台会自动填入阿里云的默认 DNS 服务器 IP（100.100.2.136 和 100.100.2.138），如果您删除该 IP，可能会导致您无法访问阿里云基础云上服务，请谨慎操作。调用 API 时，确保填入上述 IP。2、确保将自建 DNS 服务器 IP 填写在首位，否则将优先向阿里云默认 DNS 服务器发起查询请求。由于默认 DNS 服务器无法解析自定义域名，将直接返回NXDOMAIN，系统将认为无需继续查询后续服务器，从而无法将私网域名解析为 IP 。3、您需要在关联 VPC 的[安全组](../../ecs/documents/user-guide/manage-security-group-rules.md)和[网络](work-with-network-acls.md)[ACL](work-with-network-acls.md)（如有）中添加允许访问自建 DNS 服务器 IP 的规则，否则可能导致域名无法解析。4、自定义服务器 IP 不支持使用 IPv6 地址。
控制台
前往[专有网络控制台 - DHCP 选项集](https://vpc.console.aliyun.com/dhcp/cn-hangzhou/dhcps)，创建DHCP选项集，配置域名为自建 DNS 服务中使用的域名，单击自定义服务器IP，将自建 DNS 服务器 IP 填写在首位。
在目标 DHCP 选项集的操作列选择关联专有网络，已配置域名解析记录的 ECS 可通过主机名被关联 VPC 内的 ECS 访问。
API
依次调用如下 API，创建自定义 DHCP 选项集指定域名与自建 DNS 服务器 IP，与 VPC 关联。
[CreateDhcpOptionsSet - 创建 DHCP 选项集](developer-reference/api-vpc-2016-04-28-createdhcpoptionsset.md)
[AttachDhcpOptionsSetToVpc - 将 DHCP 选项集关联到 VPC](developer-reference/api-vpc-2016-04-28-attachdhcpoptionssettovpc.md)
TerraformResource：[alicloud_vpc_dhcp_options_set](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_dhcp_options_set)、[alicloud_vpc_dhcp_options_set_attachment](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_dhcp_options_set_attachment)# 指定VPC的地域 provider "alicloud" { region = "cn-hangzhou" } # 创建DHCP选项集 resource "alicloud_vpc_dhcp_options_set" "test_dhcp_options_set" { dhcp_options_set_name = "test_dhcp_options_set_name" domain_name = "example.com" # 指定域名 domain_name_servers = "192.168.0.10,100.100.2.136,100.100.2.138" # 指定DNS服务器IP，首位填写自建DNS服务器IP } # 关联DHCP选项集与VPC resource "alicloud_vpc_dhcp_options_set_attachment" "test_attachment_vpc" { vpc_id = "vpc-8vbg******" # 指定关联的VPC的实例ID dhcp_options_set_id = alicloud_vpc_dhcp_options_set.test_dhcp_options_set.id # 指定关联的DHCP选项集的实例ID }
## 更多信息
### 计费说明
DHCP 选项集功能不收费。
### 支持的地域
公有云支持的地域
| 区域 | 支持 DHCP 选项集的地域 |
| --- | --- |
| 亚太-中国 | 华东 1（杭州） 、 华东 2（上海） 、 华北 1（青岛） 、 华北 2（北京） 、 华北 3（张家口） 、 华北 5（呼和浩特） 、 华北 6（乌兰察布） 、 华南 1（深圳） 、 华南 3（广州） 、 西北 2（中卫） 、 西南 1（成都） 、 中国香港 |
| 亚太-其他 | 日本（东京） 、 韩国（首尔） 、 新加坡 、 马来西亚（吉隆坡） 、 印度尼西亚（雅加达） 、 菲律宾（马尼拉） 、 泰国（曼谷） 、 马来西亚（柔佛州） |
| 欧洲与美洲 | 德国（法兰克福） 、 英国（伦敦） 、 法国（巴黎） 、 美国（硅谷） 、 美国（弗吉尼亚） 、 墨西哥 |
| 中东 | 阿联酋（迪拜） 、 沙特（利雅得）- 合作伙伴运营 |
金融云支持的地域
| 区域 | 支持 DHCP 选项集的地域 |
| --- | --- |
| 亚太 | 华南 1 金融云 、 华东 2 金融云 、 华北 2 金融云（邀测） |
### 配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| 无 | 单个账号支持创建的 DHCP 选项集的数量 默认 DHCP 选项集不占用该配额。 | 10 个 | 无法提升 |
| 单个 DHCP 选项集支持关联的 VPC 的数量 | 10 个 |  |  |
| 单个 VPC 支持关联的 DHCP 选项集的数量 | 1 个 |  |  |
| 单个 DHCP 选项集支持配置的域名的数量 | 1 个 |  |  |
| 单个 DHCP 选项集支持配置的 DNS 服务器 IP 地址的数量 | 4 个 |  |  |
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
