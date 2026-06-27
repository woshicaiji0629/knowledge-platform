# VPC对等连接-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/vpc-peer-to-peer-connection

# VPC对等连接
不同VPC默认网络隔离，无法互通。通过创建对等连接，并为两端VPC分别配置路由，可以实现VPC私网互通。对等连接功能支持同账号/跨账号、同地域/跨地域VPC互连，配置前请确保两端VPC的网段不重叠。
## 工作流程
VPC 对等连接通过私网连通两个VPC，使部署在两端 VPC 中的资源可以使用私网 IP 互访。
创建VPC对等连接：同账号VPC，系统会自动接受请求并建立连接。跨账号VPC，需要接收端账号接受连接请求。
双向路由配置：为两端VPC分别配置指向对端VPC的路由，才能实现资源互访。
当有大量 VPC 互连、大带宽、低成本的综合需求时，可同时使用 VPC 对等连接和云企业网。二者区别，可参考[VPC](cross-vpc-interconnection-overview.md)[互连](cross-vpc-interconnection-overview.md)。
## 配置对等连接
控制台
前置检查：
确保两端VPC的网段不重叠。若重叠，需将业务迁移到网段不重叠的VPC中。
如果初次使用VPC对等连接，需要确保两端VPC所属账号都开通CDT功能。
创建对等连接：
前往[专有网络控制台 - VPC](https://vpc.console.aliyun.com/vpcpeer/cn-hangzhou/vpcpeers)[对等连接](https://vpc.console.aliyun.com/vpcpeer/cn-hangzhou/vpcpeers)，在页面上方选择VPC所在的地域，单击创建对等连接。
创建对等连接：根据两端VPC实例所属的账号和地域，选择接收端账号类型和接收端地域类型。
接收端账号类型：
同账号：系统会自动接受请求并建立连接。可勾选VPC系统路由表添加对端VPC CIDR路由，将由系统配置双向路由。
跨账号：需要使用接收端账号前往[专有网络控制台 - VPC](https://vpc.console.aliyun.com/vpcpeer/cn-hangzhou/vpcpeers)[对等连接](https://vpc.console.aliyun.com/vpcpeer/cn-hangzhou/vpcpeers)，在页面上方选择 VPC 所在的地域，在目标对等连接的操作列单击接收。
接收端也可以拒绝或删除连接请求，可以参考[VPC](vpc-peer-to-peer-connection.md)[对等连接的状态机](vpc-peer-to-peer-connection.md)了解完整流程。
接收端地域类型为跨地域时，需配置链路类型和接收端地域。
支持铂金、金两种链路类型，提供不同质量的流量传输服务，对应不同的[计费单价](https://help.aliyun.com/zh/cdt/inter-region-data-transfers#d0450e8c0bzxe)。
铂金（服务可用性承诺：99.995%）：适用于对链路抖动、时延敏感，对链路质量要求较高的业务。例如证券交易、在线语音、视频会议、实时游戏等。
金（服务可用性承诺：99.95%）：适用于对链路质量不敏感的业务。例如数据同步、文件传输等。
双向路由配置：
如需使用IPv6地址互访，需配置指向对端VPC实例的IPv6网段的路由条目。
使用发起端 VPC 所属账号：单击发起端列的配置路由条目，选择该 VPC 中需连通的资源所在交换机绑定的路由表，配置目标网段为接收端网段。
使用接收端 VPC 所属账号：单击接收端列的配置路由条目，选择该 VPC 中需连通的资源所在交换机绑定的路由表，配置目标网段为发起端网段。
验证连通性：
路径分析：分析过程不发送真实数据包，不会影响业务运行。
在目标对等连接实例的诊断列选择发起诊断>路径分析或单击目标对等连接实例ID进入路径分析页签。
配置源与目的，指定具体的协议和端口号来模拟业务访问场景，校验二者的连通性。
系统将检查路由/安全组/网络ACL的配置，并给出诊断结果。
单向路径可达时，需配置反向路径进行连通性校验。
手动验证：在发起端VPC内的ECS，执行ping <对端 ECS 的私网 IP>。
创建跨地域对等连接后，单击实例ID，支持编辑跨地域对等连接的带宽（Mbps）和链路类型。两端账号均可删除VPC对等连接。删除后，私网互访能力将会中断，且删除后无法恢复，需确保在对业务无影响的情况下谨慎操作。
API
创建对等连接
调用[CreateVpcPeerConnection](developer-reference/api-vpcpeer-2022-01-01-createvpcpeerconnection.md)创建VPC对等连接。
两端VPC属于不同账号时，需使用接收端账号调用[AcceptVpcPeerConnection](developer-reference/api-vpcpeer-2022-01-01-acceptvpcpeerconnection.md)接受VPC对等连接。
接收端可以调用[RejectVpcPeerConnection](developer-reference/api-vpcpeer-2022-01-01-rejectvpcpeerconnection.md)拒绝VPC对等连接。
使用两端 VPC 所属账号，分别调用[GetVpcPeerConnectionAttribute](developer-reference/api-vpcpeer-2022-01-01-getvpcpeerconnectionattribute.md)查询两端VPC的网段。
使用两端 VPC 所属账号，分别调用[CreateRouteEntry](developer-reference/api-vpc-2016-04-28-createrouteentry.md)创建指向对等连接的路由条目。
修改跨地域对等连接
调用[ModifyVpcPeerConnection](developer-reference/api-vpcpeer-2022-01-01-modifyvpcpeerconnection.md)修改跨地域VPC对等连接的带宽或链路类型。
删除对等连接
调用[DeleteRouteEntry](developer-reference/api-vpc-2016-04-28-deleterouteentry.md)删除指向对等连接的路由条目。
调用[DeleteVpcPeerConnection](developer-reference/api-vpcpeer-2022-01-01-deletevpcpeerconnection.md)删除VPC对等连接。
路径分析
依次调用以下API来使用路径分析校验连通性。
[创建网络分析路径](https://help.aliyun.com/zh/nis/developer-reference/api-nis-2021-12-16-createnetworkpath)
[创建网络可达性分析任务](https://help.aliyun.com/zh/nis/developer-reference/api-nis-2021-12-16-createnetworkreachableanalysis)
[获取网络可达性分析任务结果](https://help.aliyun.com/zh/nis/developer-reference/api-nis-2021-12-16-getnetworkreachableanalysis)
Terraform
同账号对等连接Resources：[alicloud_vpc_peer_connection](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_peer_connection)、[alicloud_route_entry](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_entry)Data Sources：[alicloud_account](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/account)# VPC所属账号 data "alicloud_account" "default" {} provider "alicloud" { alias = "local" region = "cn-hangzhou" #发起端VPC所属地域。 } provider "alicloud" { alias = "accepting" region = "cn-beijing" #接收端地域。可以和发起端地域相同，需要根据接收端VPC所属地域配置。 } # 发起端VPC ID variable "local_vpc_id" { default = "vpc-bp1c******" } # 接收端VPC ID variable "accepting_vpc_id" { default = "vpc-2zev******" } # 创建VPC对等连接 resource "alicloud_vpc_peer_connection" "example_peer_connection" { provider = alicloud.local peer_connection_name = "example_peer_connection_name" vpc_id = var.local_vpc_id # 发起端VPC ID accepting_ali_uid = data.alicloud_account.default.id # 接收端账号 ID accepting_region_id = "cn-beijing" # 接收端VPC所属地域 accepting_vpc_id = var.accepting_vpc_id # 接收端VPCID bandwidth = 1024 # 带宽，单位：Mbps。仅发起端地域和接收端地域不同时，可以配置。 link_type = "Gold" # 链路类型，仅发起端地域和接收端地域不同时，可以配置。 } # 为发起端VPC配置路由 resource "alicloud_route_entry" "example_local_route" { provider = alicloud.local route_table_id = "vtb-bp1a******" # 发起端实例所属交换机绑定的路由表 destination_cidrblock = "172.16.0.0/12" # 接收端VPC网段 nexthop_type = "VpcPeer" # 下一跳为VPC对等连接 nexthop_id = alicloud_vpc_peer_connection.example_peer_connection.id } # 为接收端VPC配置路由 resource "alicloud_route_entry" "example_acceptor_route" { provider = alicloud.accepting route_table_id = "vtb-2ze1******" # 接收端实例所属交换机绑定的路由表 destination_cidrblock = "10.0.0.0/8" # 发起端VPC网段 nexthop_type = "VpcPeer" # 下一跳为VPC对等连接 nexthop_id = alicloud_vpc_peer_connection.example_peer_connection.id }
跨账号对等连接Resources：[alicloud_vpc_peer_connection](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_peer_connection)、[alicloud_vpc_peer_connection_accepter](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_peer_connection_accepter)、[alicloud_route_entry](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_entry)provider "alicloud" { alias = "local" region = "cn-hangzhou" #发起端地域 } #接收端地域。可以和发起端地域相同，需要根据接收端VPC所属地域配置。 variable "accepting_region" { default = "cn-beijing" } #接收端账号 variable "accepting_uid" { default = "1234******" } #接收端账号AK variable "access_key_id" { description = "The AccessKey ID for operating your infrastructure" } #接收端账号SK variable "access_key_secret" { description = "The AccessKey Secret for operating your infrastructure" } provider "alicloud" { alias = "acceptor" region = var.accepting_region access_key = var.access_key_id secret_key = var.access_key_secret } # 发起端VPC ID variable "local_vpc_id" { default = "vpc-2ze0******" } # 接收端VPC ID variable "accepting_vpc_id" { default = "vpc-wz9e******" } # 创建VPC对等连接 resource "alicloud_vpc_peer_connection" "example_peer_connection" { provider = alicloud.local peer_connection_name = "example_peer_connection_name" vpc_id = var.local_vpc_id # 发起端VPC ID accepting_ali_uid = var.accepting_uid # 接收端账号ID accepting_region_id = var.accepting_region # 接收端地域 accepting_vpc_id = var.accepting_vpc_id # 接收端VPC ID bandwidth = 1024 # 带宽，单位：Mbps。仅发起端地域和接收端地域不同时，可以配置。 link_type = "Gold" # 链路类型，仅发起端地域和接收端地域不同时，可以配置。 } # 接收端接受对等连接请求 resource "alicloud_vpc_peer_connection_accepter" "example_peer_connection_accepter" { provider = alicloud.acceptor instance_id = alicloud_vpc_peer_connection.example_peer_connection.id } # 为发起端VPC配置路由 resource "alicloud_route_entry" "example_local_route" { provider = alicloud.local route_table_id = "vtb-2zel******" # 发送端实例所属交换机绑定的路由表 destination_cidrblock = "192.168.0.0/24" # 接收端VPC网段 nexthop_type = "VpcPeer" # 下一跳为VPC对等连接 nexthop_id = alicloud_vpc_peer_connection.example_peer_connection.id } # 为接收端VPC配置路由 resource "alicloud_route_entry" "example_acceptor_route" { provider = alicloud.acceptor route_table_id = "vtb-wz95******" # 接收端实例所属交换机绑定的路由表 destination_cidrblock = "172.16.0.0/12" # 发起端VPC网段 nexthop_type = "VpcPeer" # 下一跳为VPC对等连接 nexthop_id = alicloud_vpc_peer_connection.example_peer_connection.id }
## 网络连通性排查
建议优先使用[路径分析](vpc-peer-to-peer-connection.md)验证网络连通性。
| 检查项 | 检查内容 | 解决方案 |
| --- | --- | --- |
| 对等连接状态 | 查看目标对等连接实例的 状态 是否为 已激活 。 | 如果状态为对端接收中，需要联系接收端账号接受连接。 |
| 网段配置 | 查看发起端网段和接收端网段： 是否重叠。 是否使用了非 [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) 标准私网网段（如 198.19.0.0/16、30.0.0.0/8 等）。VPC 将这些网段视为公网地址，ECS 绑定公网 IP 时流量默认走公网出口。 当 ECS 实例部署 Docker 时，是否与 Docker 网卡地址冲突。 | 网段重叠时，需将业务迁移到网段不重叠的 VPC，重新建立对等连接。 使用非 RFC 标准私网网段时， [使用](using-ipv4-gateway-for-public-network-private-use.md) [IPv4](using-ipv4-gateway-for-public-network-private-use.md) [网关实现公网私用](using-ipv4-gateway-for-public-network-private-use.md) ，确保流量能够正确地到达目标 VPC。 [修改 Docker 网段](vpc-peer-to-peer-connection.md) 。 |
| 路由配置 | 查看对等连接详情页的 路由条目列表 ： 是否为两端 VPC 都配置了指向对方的路由。 目标网段是否正确填写对端的 VPC 网段。 路由条目是否添加到资源所在交换机绑定的路由表。 | 检查并修正 [双向路由配置](vpc-peer-to-peer-connection.md) 。 |
| 访问规则配置 | 互访 ECS 所在安全组的出入方向规则是否放行对端 IP。 RDS 实例的访问白名单是否添加了对端 IP。 与交换机绑定的网络 ACL 的出入方向规则是否放行对端 IP。 | 确保安全组、网络 ACL、RDS 的访问白名单均放行对端 IP。 |
网段配置导致无法连通的原因
网段重叠：
两端VPC网段重叠时，如果配置对端VPC网段作为目标网段，流量会优先匹配系统路由，在VPC内部转发，无法抵达对端VPC。
如果交换机网段不重叠，可以配置对端交换机网段作为目标网段。但新建交换机需要使用与现有交换机网段不重叠的网段。因此，建议将业务迁移到网段不重叠的VPC中，重新建立对等连接。
交换机网段重叠，由于无法配置比系统路由更明细的路由，只能将业务迁移到网段不重叠的 VPC，重新建立对等连接。
使用非[RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)标准私网网段：
VPC 将[RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)之外的 IP 地址空间（如 198.19.0.0/16、30.0.0.0/16 等）视为公网网段。当 VPC 中的 ECS 绑定了公网 IP 或通过 NAT 网关具备公网访问能力时，访问这些网段的流量会走公网出口，无法通过对等连接到达目标 VPC。需要在 VPC 中[使用](using-ipv4-gateway-for-public-network-private-use.md)[IPv4](using-ipv4-gateway-for-public-network-private-use.md)[网关实现公网私用](using-ipv4-gateway-for-public-network-private-use.md)，将目标公网网段添加为私网路由，确保流量通过对等连接正确路由到目标 VPC。
## 配置示例
### 三个VPC互访
为VPC对等连接配置路由时，可以：
将对端VPC网段设为目标网段，所有实例均可以互相访问，简化管理。
配置更精细的路由，将对端VPC中的交换机网段或特定实例的IP地址设为目标网段，增强安全性。但新增实例需要通信时，须手动更新路由表。
例如，VPC1 配置了指向 VPC2 交换机3网段和 VPC3 中 ECS04 的路由，因此 VPC1 资源仅可与交换机3资源、ECS04 私网通信。VPC2 和 VPC3 配置了指向对端 VPC 网段的路由，资源可完全互访。
### 多个VPC与中心VPC互连
例如，分支VPC均可访问中心VPC部署的服务，但分支VPC间无法互访。典型场景：
多部门隔离：不同业务部门VPC不能互通，但需访问中心VPC的共享服务。
多用户隔离：服务部署在独立VPC内，提供给多个用户。每个用户VPC都与服务VPC互通，但用户VPC之间无法互通。
## 限制未授权的跨账号连接
默认情况下，RAM 用户只要拥有vpc:CreateVpcPeerConnection与vpc:AcceptVpcPeerConnection权限，即可与任意账号建立 VPC 对等连接。如需仅允许 RAM 用户与组织内或指定的对端账号建立连接，避免敏感数据通过未授权的跨账号网络通道泄露，可以在 RAM 自定义策略中使用acs:TargetRDId、acs:TargetRDPath等全局 Condition Key，约束可连接的对端账号。
### Condition Key
鉴权时，RAM 会根据请求中的AcceptingAliUid（创建对等连接时）或RequestingAliUid（接受对等连接时）反查对端账号所属的[资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)，并将以下 Condition Key 注入鉴权上下文，由您自定义策略中的 Condition 进行匹配。
| Condition Key | 类型 | 说明 | 典型场景 |
| --- | --- | --- | --- |
| acs:TargetRDId | String | 对端账号所属的 资源目录 ID ，例如 rd-xxxxxx 。 | 限定对端账号必须属于指定资源目录。 |
| acs:TargetRDPath | String | 对端账号所属的 资源目录路径 ，格式为 {RDId}/{RootFolderId}/{FolderId}/{AccountId} ，支持通配符匹配。 | 限定对端账号必须位于指定资源夹（Folder）下，满足分层治理需求。 |
使用约束：仅vpc:CreateVpcPeerConnection与vpc:AcceptVpcPeerConnection会注入上述 Condition Key，对等连接的查询、修改、删除等其他操作不生效。命中策略后请求返回错误码Forbidden.NoPermission，错误明细中NoPermissionType为ExplicitDeny，可通过 RequestId 在[操作审计](https://help.aliyun.com/zh/actiontrail/product-overview/what-is-actiontrail)中追溯命中过程。
### 选择限制策略
实际配置时，请将示例中的资源目录 ID、路径或账号 ID 替换为您组织实际的取值，资源目录 ID 与路径可在[资源管理控制台](https://resourcemanager.console.aliyun.com/)获取。
基于资源目录 ID
仅允许 RAM 用户与指定资源目录内的账号建立 VPC 对等连接。将rd-xxxxxx替换为您的资源目录 ID。
{ "Version": "1", "Statement": [ { "Effect": "Deny", "Action": [ "vpc:CreateVpcPeerConnection", "vpc:AcceptVpcPeerConnection" ], "Resource": "*", "Condition": { "StringNotEquals": { "acs:TargetRDId": ["rd-xxxxxx"] } } } ] }
基于资源目录路径
仅允许 RAM 用户与指定资源夹（Folder）路径下的账号建立 VPC 对等连接，适用于精细化分层治理。将示例中的路径替换为您的实际路径。
{ "Version": "1", "Statement": [ { "Effect": "Deny", "Action": [ "vpc:CreateVpcPeerConnection", "vpc:AcceptVpcPeerConnection" ], "Resource": "*", "Condition": { "StringNotLike": { "acs:TargetRDPath": ["rd-xxxxxx/r-xxxxxx/fd-xxxxxx/*"] } } } ] }
### 创建并授予策略
控制台
登录[RAM 控制台](https://ram.console.aliyun.com/)，在左侧导航栏选择权限管理>权限策略。
单击创建权限策略，在脚本编辑页签粘贴上方所选方案的策略，并替换其中的资源目录 ID、路径或账号 ID。
单击确定，填写策略名称再确定。
[将策略授权给目标 RAM 用户、用户组或角色](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
API
调用[CreatePolicy](../../ram/documents/developer-reference/api-ram-2015-05-01-createpolicy.md)创建自定义策略，将上方所选方案的策略作为PolicyDocument参数传入。
调用[AttachPolicyToUser](../../ram/documents/developer-reference/api-ram-2015-05-01-attachpolicytouser.md)、[AttachPolicyToGroup](../../ram/documents/developer-reference/api-ram-2015-05-01-attachpolicytogroup.md)或[AttachPolicyToRole](../../ram/documents/developer-reference/api-ram-2015-05-01-attachpolicytorole.md)将策略授予目标 RAM 用户、用户组或角色。
## 监控运维
跨地域对等连接支持查看流量带宽、丢包率等监控信息。结合[云监控服务](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/what-is-cloudmonitor)创建阈值报警规则，可实时监控连接状态，及时发现和解决网络拥堵或故障问题。
同地域对等连接不支持查看监控指标。
监控指标项
| 监控指标项 | 说明 |
| --- | --- |
| 周期内入方向流量 | 在一个统计周期内，VPC 对等连接的发起端发送到接收端的流量。 |
| 周期内出方向流量 | 在一个统计周期内，VPC 对等连接的接收端发送到发起端的流量。 |
| 网络流入带宽 | VPC 对等连接从发起端进入接收端的带宽。 |
| 网络流出带宽 | VPC 对等连接从接收端发往发起端的带宽。 |
| 网络流出限速丢包数 | VPC 对等连接实例出方向因带宽限速，被丢弃的数据包速率。 |
### 控制台
对等连接监控
前往[专有网络控制台 - VPC](https://vpc.console.aliyun.com/vpcpeer/cn-hangzhou/vpcpeers)[对等连接](https://vpc.console.aliyun.com/vpcpeer/cn-hangzhou/vpcpeers)，在页面上方选择VPC所在的地域。
单击目标跨地域VPC对等连接实例监控列的图标，查看流量带宽与丢包情况等监控信息。
云监控告警
前往[云监控控制台 - 报警规则](https://cloudmonitornext.console.aliyun.com/alert/rule)，单击创建报警规则。
为VPC对等连接的监控指标项配置各报警级别的阈值，当相应指标达到阈值后，报警联系人组将接收到报警通知，也可以在目标报警规则的操作列，点击报警历史查看报警时间线。
在目标报警规则的操作列，修改/禁用/删除规则。
### API
参考[对等连接云监控指标](https://cms.console.aliyun.com/metric-meta/acs_vpcpeer/vpcpeer)，调用[PutResourceMetricRules](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/developer-reference/api-cms-2019-01-01-putresourcemetricrules)为VPC对等连接指定监控项设置多条阈值报警规则。
调用[EnableMetricRules](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/developer-reference/api-cms-2019-01-01-enablemetricrules)启用一个或多个报警规则。
调用[DisableMetricRules](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/developer-reference/api-cms-2019-01-01-disablemetricrules)禁用报警规则。
调用[DeleteMetricRules](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/developer-reference/api-cms-2019-01-01-deletemetricrules)删除一个或多个报警规则。
### Terraform
参考[对等连接云监控指标](https://cms.console.aliyun.com/metric-meta/acs_vpcpeer/vpcpeer)配置阈值报警规则。Resources：[alicloud_cms_alarm_contact](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cms_alarm_contact)、[alicloud_cms_alarm_contact_group](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cms_alarm_contact_group)、[alicloud_cms_alarm](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cms_alarm)# 监控的对等连接实例ID variable "vpc_peer_id" { default = "pcc-28cv******" } # 创建报警联系人 resource "alicloud_cms_alarm_contact" "example_cms_alarm_contact" { alarm_contact_name = "example_cms_alarm_contact_name" describe = "example_vpc_peer_alarm" channels_mail = "xxx@xxx.com" # 需修改为实际的Email地址 lifecycle { ignore_changes = [channels_mail] } } # 创建报警联系人组 resource "alicloud_cms_alarm_contact_group" "example_cms_alarm_contact_group" { alarm_contact_group_name = "example_cms_alarm_contact_group" contacts = [alicloud_cms_alarm_contact.example_cms_alarm_contact.id] # 报警联系人 } # 创建报警规则 resource "alicloud_cms_alarm" "example_cms_alarm" { name = "example_cms_alarm_name" project = "acs_vpcpeer" # 云产品的数据命名空间 metric = "IntranetRX" # 监控项名称 period = 60 # 统计周期 contact_groups = [alicloud_cms_alarm_contact_group.example_cms_alarm_contact_group.alarm_contact_group_name] effective_interval = "06:00-20:00" # 生效时间 metric_dimensions = <<EOF [ { "instanceId": "${var.vpc_peer_id}" } ] EOF escalations_critical { # Info级别报警 statistics = "Sum" # 报警统计方法 comparison_operator = ">=" # 阈值比较符 threshold = 104857600 # 阈值 times = 2 # 报警重试次数 } }
## 常见问题
### 对等连接是否支持跨境互连？
支持非跨境、跨境。
非跨境：中国内地地域到中国内地地域、非中国内地地域到非中国内地地域。
跨境：中国内地地域到非中国内地地域。需先完成跨境合规认证。请在[联通跨境云专线在线申请](https://ecommerce.ictsoft.cn/apply/)页面提交资料，申请联通跨境业务资质。
### 创建对等连接时无法选择目标VPC？
请确认选择的地域和账号与目标VPC的地域和拥有者一致。
页面上方显示发起端地域，当前账号为发起端账号。接收端账号和地域在创建对等连接时配置。
### RAM用户创建VPC对等连接时提示缺少CDT权限？
RAM用户已授予AliyunVPCFullAccess权限，但创建VPC对等连接时报错提示缺少cdt:GetCdtServiceStatus权限。这是因为VPC对等连接依赖云数据传输CDT服务，创建对等连接时需要调用CDT相关接口，仅有VPC权限不够。
需要为RAM用户额外授予以下任一权限：
AliyunCDTFullAccess：CDT服务的完全访问权限。
AliyunCDTReadOnlyAccess：CDT服务的只读权限，适用于仅需创建对等连接而无需管理CDT资源的场景。
### 部署 Docker 的 ECS 实例配置对等连接后无法互通？
当路由与安全组配置无误时，通常是由 Docker 网卡地址与访问目的网段冲突导致。可执行ip addr检查 Docker 网卡地址是否与访问目的网段冲突。
二者冲突时，可参考以下步骤修改 Docker 网段，确保与访问目的网段不冲突。
停止 Docker 或者修改 Docker 网段会中断业务，建议业务低峰期进行操作。
修改 Docker 网段时请确保与任何现有容器和应用程序的网络设置兼容，以避免潜在的连接问题。
执行sudo systemctl stop docker停止 Docker 服务。
执行sudo vim /etc/docker/daemon.json编辑 Docker 配置文件并保存，文件内容如下：
Docker 配置文件通常为/etc/docker/daemon.json或/etc/docker/daemon.conf，具体文件名可能有所不同。{ "bip":"新的Docker网段" }
执行sudo systemctl start docker启动 Docker 服务，确保修改生效。
## 更多信息
### 使用限制
以下情况不支持创建 VPC 对等连接：
两端 VPC 归属于不同站点的账号，即中国站账号与国际站账号。
两端 VPC 归属于不同类型的地域，即公有云地域、金融云地域和政务云地域。
VPC对等连接不具备路由传递能力。
例如，VPC 1和VPC 2、VPC 3分别使用对等连接实现私网互通，但VPC 2和VPC 3不能通过VPC 1做中转互通。
多账号共享VPC时，资源所有者可以创建/修改/删除对等连接，而资源使用者没有操作权限。
### 计费说明
同地域VPC对等连接：两端VPC属于同账号或跨账号，均不收取任何费用。
跨地域VPC对等连接：统一由[云数据传输](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt)[CDT](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt)按出向流量收取[流量传输费](https://help.aliyun.com/zh/cdt/inter-region-data-transfers)。
计费单价根据地域到地域粒度、链路类型来确定。支持铂金、金两种链路类型，提供不同质量的流量传输服务。
计费周期为每小时。如果在计费周期内切换链路类型，将按照较高服务等级的单价进行计费。
如图，跨地域跨账号的VPC1和VPC2建立了对等连接。若 VPC1 和 VPC2 通过对等连接流出的流量分别为200GB和100GB，链路类型选择金，华北5（呼和浩特）到华南3（广州）的[跨地域流量费](https://help.aliyun.com/zh/cdt/inter-region-data-transfers)单价为0.48元/GB。依据出向流量计费规则：
账号A需要支付的费用为：0.48元/GB × 200GB = 96元
账号B需要支付的费用为：0.48元/GB × 100GB = 48元
### VPC对等连接的状态机
从发起端发送创建请求开始，VPC对等连接会经过各个阶段。
如果创建的是同账号VPC对等连接，系统会自动发起连接请求并自动接受请求，VPC对等连接变为已激活状态。
VPC对等连接状态说明
| 状态 | 说明 |
| --- | --- |
| 创建中 | 发起端发起 VPC 对等连接请求后的状态。 |
| 对端接收中 | 等待接收端接受 VPC 对等连接请求的状态。 |
| 更新中 | 接收端接受 VPC 对等连接请求后，该 VPC 对等连接的状态。 |
| 已激活 | 接收端接受 VPC 对等连接请求后，发起端和接收端协商激活 VPC 对等连接后的状态。 |
| 已拒绝 | 接收端拒绝 VPC 对等连接请求后，该 VPC 对等连接的状态。 |
| 已过期 | 接收端超过 7 天未接受或者拒绝 VPC 对等连接请求，则该 VPC 对等连接处于已过期状态。 |
| 删除中 | 发起端或者接收端删除 VPC 对等连接后的中间状态。 |
| 已删除 | VPC 对等连接成功删除后的状态。 |
### 支持的地域
公有云支持的地域
| 区域 | 支持 VPC 对等连接的地域 |
| --- | --- |
| 亚太-中国 | 华东 1（杭州） 、 华东 2（上海） 、 华东 5 （南京-本地地域-关停中） 、 华北 1（青岛） 、 华北 2（北京） 、 华北 3（张家口） 、 华北 5（呼和浩特） 、 华北 6（乌兰察布） 、 华南 1（深圳） 、 华南 2（河源） 、 华南 3（广州） 、 西南 1（成都） 、 西北 2（中卫） 、 中国香港 、 华中 1（武汉-本地地域） 、 华东 6（福州-本地地域-关停中） |
| 亚太-其他 | 日本（东京） 、 韩国（首尔） 、 新加坡 、 马来西亚（吉隆坡） 、 印度尼西亚（雅加达） 、 菲律宾（马尼拉） 、 泰国（曼谷） 、 马来西亚（柔佛州） |
| 欧洲与美洲 | 德国（法兰克福） 、 英国（伦敦） 、 美国（硅谷） 、 美国（弗吉尼亚） |
| 中东 | 阿联酋（迪拜） 、 沙特（利雅得）- 合作伙伴运营 |
金融云支持的地域
| 区域 | 支持 VPC 对等连接的地域 |
| --- | --- |
| 亚太 | 华南 1 金融云 、 华东 2 金融云 、 华北 2 金融云（邀测） |
政务云支持的地域
| 区域 | 支持 VPC 对等连接的地域 |
| --- | --- |
| 亚太 | 华北 2 阿里政务云 1 |
### 配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_cross_region_peer_num_per_vpc | 单个 VPC 支持的跨地域 VPC 对等连接数量 | 20 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_intra_region_peer_num_per_vpc | 单个 VPC 支持的同地域 VPC 对等连接数量 | 10 个 |  |
| vpc_quota_peer_num | 单个阿里云账号单地域支持的 VPC 对等连接数量 | 20 个 |  |
| vpc_quota_peer_cross_border_bandwidth | 跨境带宽允许的最大值 | 1024 Mbps |  |
| vpc_quota_peer_cross_region_bandwidth | 跨地域带宽允许的最大值 | 1024 Mbps |  |
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
