# 使用资源组进行精细化资源控制-专有网络VPC-阿里云-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/fine-grained-resource-control-using-resource-groups-64

# 使用资源组进行精细化资源控制
当您使用资源组对资源进行分组管理时，可以结合访问控制（RAM），在单个阿里云账号内实现资源的隔离和精细化权限管理。本文总结了专有网络VPC对资源组的支持情况，以及资源组级别的授权操作步骤。
说明
只有[支持资源组的资源类型](fine-grained-resource-control-using-resource-groups-64.md)和支持资源组级别授权的操作，资源组级别授权才能生效。
对于不支持资源组的资源类型，授予资源组范围的权限将无效。在选择资源范围时，请选择账号级别，进行账号级别授权。具体操作，请参见[不支持资源组级别授权的操作](fine-grained-resource-control-using-resource-groups-64.md)。
## 资源组授权的工作原理
您可以使用资源组（Resource Group）对阿里云账号内的资源进行分组管理。例如，为不同的项目创建对应的资源组，并将资源转移到对应的组中，以便集中管理各项目的资源。更多信息，请参见[什么是资源组](https://help.aliyun.com/zh/resource-management/resource-group/product-overview/resource-group-overview)。
在完成资源分组后，您可以为不同的RAM授权主体（RAM用户、RAM用户组或RAM角色）授予指定资源组范围的权限，从而限定这个授权主体只能管理该资源组内的资源。更多信息，请参见[资源分组和授权](https://help.aliyun.com/zh/resource-management/resource-group/use-cases/use-ram-to-create-and-authorize-resource-groups#DAS)。
这种授权方式的优点有：
权限精细化：确保每个身份能获得最准确的资源访问权限，避免账号下的多个项目的资源混合管理。
良好的扩展性：后续新增资源时，只需将其加入该资源组，RAM身份便会自动获得新资源的相应权限，无需再次授权。
## 为RAM用户授予资源组级别的权限
下面以RAM用户为例，介绍授予指定资源组内专有网络VPC资源权限的操作步骤。
### 1. 前置步骤
创建待使用的RAM用户，可参考：[创建](../../ram/documents/user-guide/create-a-ram-user.md)[RAM](../../ram/documents/user-guide/create-a-ram-user.md)[用户](../../ram/documents/user-guide/create-a-ram-user.md)
创建资源组并将已有资源划分到目标资源组，可参考：[创建资源组](https://help.aliyun.com/zh/resource-management/resource-group/user-guide/create-a-resource-group#task-xpl-kjm-4fb)，[资源自动转组](https://help.aliyun.com/zh/resource-management/resource-group/user-guide/automatic-resource-transfer/)及[资源手动转组](https://help.aliyun.com/zh/resource-management/resource-group/user-guide/resource-manual-transfer-group)。
### 2. 进行资源组级别授权
您可以通过以下任一方式进行资源组级别授权。
### 方式一：在资源管理控制台中授权
通过资源组的权限管理功能为指定 RAM 用户授权。详情操作可参见[为](https://help.aliyun.com/zh/resource-management/resource-group/user-guide/add-ram-authorization)[RAM](https://help.aliyun.com/zh/resource-management/resource-group/user-guide/add-ram-authorization)[身份授予资源组范围的权限](https://help.aliyun.com/zh/resource-management/resource-group/user-guide/add-ram-authorization)。
登录[资源组控制台](https://resourcemanager.console.aliyun.com/resource-groups)。
在资源组页面，单击目标资源组操作列的权限管理。
在权限管理页签，单击新增授权。
在新增授权面板，设置授权主体和权限策略。
授权主体：选择已有RAM用户。
权限策略：选择系统策略或已创建的自定义策略，参考[创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)。
单击确认新增授权。
### 方式二：在 RAM 控制台中授权
通过RAM控制台为指定 RAM 用户进行资源组级别授权。详细操作可参见[管理](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
使用阿里云账号（主账号）或RAM管理员登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。
在左侧导航栏，选择身份管理>用户。在用户页面，单击目标RAM用户操作列的添加权限。
在新增授权面板，为RAM用户添加权限。
资源范围：选择资源组级别。
授权主体：选择已有 RAM 用户或前面步骤创建的 RAM 用户。
权限策略：选择系统策略或已创建的自定义策略，参考[创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)。
单击确认新增授权。
## 支持资源组的资源类型
专有网络VPC支持资源组的资源类型如下表所示：
| 云服务 | 云服务代码 | 资源类型 |
| --- | --- | --- |
| 专有网络 VPC | vpc | customergateway : 用户网关 |
| 专有网络 VPC | vpc | dhcpoptionsset : DHCP 选项集 |
| 专有网络 VPC | vpc | gatewayendpoint : 网关终端节点 |
| 专有网络 VPC | vpc | ipam : IPAM 实例 |
| 专有网络 VPC | vpc | ipampool : IPAM 地址池 |
| 专有网络 VPC | vpc | ipamresourcediscovery : IPAM 资源发现 |
| 专有网络 VPC | vpc | ipamscope : IPAM 作用范围 |
| 专有网络 VPC | vpc | ipsecserver : IPsec 服务端 |
| 专有网络 VPC | vpc | ipv4gateway : IPv4 网关 |
| 专有网络 VPC | vpc | ipv6gateway : IPv6 网关 |
| 专有网络 VPC | vpc | natgateway : NAT 网关 |
| 专有网络 VPC | vpc | peerconnection : VPC 对等连接 |
| 专有网络 VPC | vpc | publicipaddresspool : 弹性公网 IP 地址池 |
| 专有网络 VPC | vpc | sslvpnclientcert : SSL 客户端 |
| 专有网络 VPC | vpc | sslvpnserver : SSL 服务端 |
| 专有网络 VPC | vpc | trafficmirrorfilter : 流量镜像筛选条件 |
| 专有网络 VPC | vpc | trafficmirrorsession : 流量镜像会话 |
| 专有网络 VPC | vpc | vpc : 专有网络 |
| 专有网络 VPC | vpc | vpnattachment : IPsec 连接（绑定 CEN） |
| 专有网络 VPC | vpc | vpnconnection : IPsec 连接 |
| 专有网络 VPC | vpc | vpngateway : VPN 网关 |
说明
对于暂不支持资源组的资源类型，如有需要，您可以在[资源组控制台](https://resourcemanager.console.aliyun.com/resource-groups)提交反馈。
## 不支持资源组级别授权的操作
专有网络VPC中不支持资源组级别授权的操作（Action）如下：
| 操作（Action） | 操作描述 |
| --- | --- |
| vpc:AddBandwidthPackageIps | - |
| vpc:AddGlobalAccelerationInstanceIp | 调用 AddGlobalAccelerationInstanceIp 接口添加 EIP 到指定的带宽共享实例中。 |
| vpc:AddIPv6TranslatorAclListEntry | 在访问控制策略组中添加 IP 条目。 |
| vpc:AllocateVpcIpv6Cidr | 预留指定的 IPv6 地址段。 |
| vpc:CancelExpressCloudConnection | - |
| vpc:CheckVpnBgpEnabled | 调用 CheckVpnBgpEnabled 接口查询 IPsec 连接所属的地域是否支持 BGP 功能。 |
| vpc:ConvertBandwidthPackage | - |
| vpc:CreaeNatGateway | - |
| vpc:CreateBandwidthPackage | - |
| vpc:CreateBondRouterInterfaceConnection | - |
| vpc:CreateExpressCloudConnection | 调用 CreateExpressCloudConnection 创建高速上云服务实例。 |
| vpc:CreateGlobalAccelerationInstance | 创建全球加速实例。 |
| vpc:CreateIPv6Translator | 创建 IPv6 转换服务实例。 |
| vpc:CreateIPv6TranslatorAclList | 创建访问控制策略组。 |
| vpc:CreateIPv6TranslatorEntry | 为指定的 IPv6 转换服务实例添加 IPv6 转换映射条目。 |
| vpc:CreateNqa | - |
| vpc:DeleteBandwidthPackage | - |
| vpc:DeleteGlobalAccelerationInstance | 删除全球加速实例。 |
| vpc:DeleteIPv6Translator | 删除 IPv6 转换服务实例。 |
| vpc:DeleteIPv6TranslatorAclList | 删除访问控制策略组。只有当访问控制策略组没有绑定任何 IPv6 转换映射时，才可以删除。 |
| vpc:DeleteIPv6TranslatorEntry | 删除 IPv6 转换映射条目。 |
| vpc:DeleteIpv6EgressOnlyRule | 调用 DeleteIpv6EgressOnlyRule 接口删除仅主动出规则。 |
| vpc:DescribeAccessPoints | - |
| vpc:DescribeBandwidthPackageMonitorData | - |
| vpc:DescribeBandwidthPackagePublicIpMonitorData | - |
| vpc:DescribeGlobalAccelerationInstances | 查询已创建的全球加速实例列表。 |
| vpc:DescribeIPv6TranslatorAclListAttributes | 查询访问控制策略组的详细信息，包括访问控制策略组中的 IP 和关联的 IPv6 转换映射条目的具体信息。 |
| vpc:DescribeIPv6TranslatorAclLists | 查询已创建的访问控制策略组。 |
| vpc:DescribeIPv6TranslatorEntries | 查询 IPv6 转换映射条目。 |
| vpc:DescribeInstances | - |
| vpc:DescribeNetworkQuotas | - |
| vpc:DescribePublicIpAddress | 调用 DescribePublicIpAddress 接口查询指定地域中位于专有网络的公网 IP 地址的范围。 |
| vpc:DescribeRouterInterfacesForGlobal | - |
| vpc:DescribeServerRelatedGlobalAccelerationInstances | 查询指定后端服务器绑定的全球加速实例。 |
| vpc:DescribeVPCs | - |
| vpc:DescribeVpnGatewayAvailableZones | 调用 DescribeVpnGatewayAvailableZones 接口查询指定地域支持部署 IPsec 连接的可用区列表。 |
| vpc:DescribeVrouters | - |
| vpc:DescribeZones | - |
| vpc:DiagnoseVpnConnections | 调用 DiagnoseVpnConnections 接口诊断 IPsec 连接。 |
| vpc:DiagnoseVpnConnectionsHistory | - |
| vpc:DiagnoseVpnGateway | 调用 DiagnoseVpnGateway 接口一键诊断指定的 VPN 网关实例。 |
| vpc:DisableNatGatewayEcsMetric | - |
| vpc:EnableNatGatewayEcsMetric | - |
| vpc:GetBusinessAccessPointDetail | - |
| vpc:GetFlowLogServiceStatus | 调用 GetFlowLogServiceStatus 接口查询流日志功能的开通状态。 |
| vpc:GetNatIpCidrAttribute | - |
| vpc:GetObject | - |
| vpc:GetPhysicalConnectionServiceStatus | 查看当前账号是否已开通出云流量费。 |
| vpc:GetPublicIpAddressPoolServiceStatus | 调用 GetPublicIpAddressPoolServiceStatus 接口查询 IP 地址池功能的开通状态。 |
| vpc:GetTrafficMirrorServiceStatus | 调用 GetTrafficMirrorServiceStatus 接口查询流量镜像功能的状态。 |
| vpc:GetVpcIpamServiceStatus | 查询 IPAM 功能的开通状态。 |
| vpc:GetVpnGatewayDiagnoseResult | 调用 GetVpnGatewayDiagnoseResult 接口查询 VPN 网关实例的一键诊断结果。 |
| vpc:InnerVpcCreateDscp | - |
| vpc:InnerVpcDeleteDscp | - |
| vpc:InnerVpcDescribeCrossBorderRouterInterface | - |
| vpc:InnerVpcDescribeDscp | - |
| vpc:InnerVpcModifyDscp | - |
| vpc:InnerVpcRefreshDscp | - |
| vpc:ListBusinessAccessPointPortUsage | - |
| vpc:ListBusinessAccessPoints | 调用 ListBusinessAccessPoints 接口查询物理专线的接入点信息。 |
| vpc:ListBusinessRegions | 查询专线可购地域列表 |
| vpc:ListGeographicSubRegions | 调用 ListGeographicSubRegions 接口查询地域信息。 |
| vpc:ListNatGatewayEcsMetric | - |
| vpc:ListVpcEndpointServicesByEndUser | 调用 ListVpcEndpointServicesByEndUser 查询可使用的终端节点服务。 |
| vpc:ModifyBandwidthPackageAttribute | - |
| vpc:ModifyBandwidthPackageSpec | - |
| vpc:ModifyBypassToaAttribute | - |
| vpc:ModifyExpressCloudConnectionAttribute | 调用 ModifyExpressCloudConnectionAttribute 修改高速上云服务连接。 |
| vpc:ModifyGlobalAccelerationInstanceAttributes | 修改全球加速实例的名称和描述信息。 |
| vpc:ModifyGlobalAccelerationInstanceSpec | 调用 ModifyGlobalAccelerationInstanceSpec 接口修改全球加速实例的带宽。 |
| vpc:ModifyIPv6TranslatorAclAttribute | 修改访问控制策略组的名称。 |
| vpc:ModifyIPv6TranslatorAclListEntry | 修改访问控制策略组中的 IP 条目。 |
| vpc:ModifyIPv6TranslatorAttribute | 修改 IPv6 转换服务实例的名称和描述信息。 |
| vpc:ModifyIPv6TranslatorBandwidth | 修改 IPv6 转换服务实例的带宽。 |
| vpc:ModifyIPv6TranslatorEntry | 修改 IPv6 转换映射条目。 |
| vpc:OpenFlowLogService | 调用 OpenFlowLogService 接口开通流日志功能。 |
| vpc:OpenPhysicalConnectionService | 调用 OpenPhysicalConnectionService 接口开通出方向流量服务。 |
| vpc:OpenPublicIpAddressPoolService | 调用 OpenPublicIpAddressPoolService 接口开通 IP 地址池功能。 |
| vpc:OpenTrafficMirrorService | 开通流量镜像功能。 |
| vpc:OpenVpcIpamService | 开通 IPAM 功能。 |
| vpc:QueryHighReliablePhysicalConnectionPrice | - |
| vpc:QueryPconnTrafficPrice | - |
| vpc:QueryPhysicalConnectionPrice | - |
| vpc:RejectVpcPeerConnection | 调用 RejectVpcPeerConnection 接口拒绝 VPC 对等连接实例的请求。 |
| vpc:RemoveBandwidthPackageIps | - |
| vpc:RemoveGlobalAccelerationInstanceIp | 调用 RemoveGlobalAccelerationInstanceIp 接口从带宽共享实例中移除 EIP。 |
| vpc:RemoveIPv6TranslatorAclListEntry | 删除访问控制策略组中的 IP 条目。 |
| vpc:RevokeInstanceFromCbn | - |
| vpc:TransformEipSegmentToPublicIpAddressPool | 将连续 EIP 组迁移至 IP 地址池。 |
| vpc:UnAssociateEipAddress | - |
| vpc:UnassociateGlobalAccelerationInstance | 调用 UnassociateGlobalAccelerationInstance 接口解绑与全球加速实例关联的后端服务实例。 |
| vpc:UpdateCrossBoarderStatus | - |
| vpc:associatevpccidrblock | - |
| vpc:createvpc | - |
| vpc:deleteBgpNetwork | - |
| vpc:describeVpcs | - |
| vpc:modifyVpcAttribute | - |
| vpc:releaseIpv6Address | - |
对于不支持资源组授权的操作，授权时资源范围选择资源组级别将无效。如果仍需要RAM用户有上述操作权限，您需要创建自定义权限策略，授权时资源范围选择账号级别。
以下是两个自定义权限策略示例，您可以根据实际需要调整策略内容。
允许不支持资源组级别授权的全部只读操作：Action中列举不支持资源组级别授权的所有只读操作。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "vpc:CheckVpnBgpEnabled", "vpc:DescribeAccessPoints", "vpc:DescribeBandwidthPackageMonitorData", "vpc:DescribeBandwidthPackagePublicIpMonitorData", "vpc:DescribeGlobalAccelerationInstances", "vpc:DescribeIPv6TranslatorAclListAttributes", "vpc:DescribeIPv6TranslatorAclLists", "vpc:DescribeIPv6TranslatorEntries", "vpc:DescribeInstances", "vpc:DescribeNetworkQuotas", "vpc:DescribePublicIpAddress", "vpc:DescribeRouterInterfacesForGlobal", "vpc:DescribeServerRelatedGlobalAccelerationInstances", "vpc:DescribeVPCs", "vpc:DescribeVpnGatewayAvailableZones", "vpc:DescribeVrouters", "vpc:DescribeZones", "vpc:GetBusinessAccessPointDetail", "vpc:GetFlowLogServiceStatus", "vpc:GetNatIpCidrAttribute", "vpc:GetObject", "vpc:GetPhysicalConnectionServiceStatus", "vpc:GetPublicIpAddressPoolServiceStatus", "vpc:GetTrafficMirrorServiceStatus", "vpc:GetVpcIpamServiceStatus", "vpc:GetVpnGatewayDiagnoseResult", "vpc:ListBusinessAccessPointPortUsage", "vpc:ListBusinessAccessPoints", "vpc:ListBusinessRegions", "vpc:ListGeographicSubRegions", "vpc:ListNatGatewayEcsMetric", "vpc:ListVpcEndpointServicesByEndUser" ], "Resource": "*" } ] }
允许不支持资源组级别授权的全部操作：Action中列举不支持资源组级别授权的全部操作。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "vpc:AddBandwidthPackageIps", "vpc:AddGlobalAccelerationInstanceIp", "vpc:AddIPv6TranslatorAclListEntry", "vpc:AllocateVpcIpv6Cidr", "vpc:CancelExpressCloudConnection", "vpc:CheckVpnBgpEnabled", "vpc:ConvertBandwidthPackage", "vpc:CreaeNatGateway", "vpc:CreateBandwidthPackage", "vpc:CreateBondRouterInterfaceConnection", "vpc:CreateExpressCloudConnection", "vpc:CreateGlobalAccelerationInstance", "vpc:CreateIPv6Translator", "vpc:CreateIPv6TranslatorAclList", "vpc:CreateIPv6TranslatorEntry", "vpc:CreateNqa", "vpc:DeleteBandwidthPackage", "vpc:DeleteGlobalAccelerationInstance", "vpc:DeleteIPv6Translator", "vpc:DeleteIPv6TranslatorAclList", "vpc:DeleteIPv6TranslatorEntry", "vpc:DeleteIpv6EgressOnlyRule", "vpc:DescribeAccessPoints", "vpc:DescribeBandwidthPackageMonitorData", "vpc:DescribeBandwidthPackagePublicIpMonitorData", "vpc:DescribeGlobalAccelerationInstances", "vpc:DescribeIPv6TranslatorAclListAttributes", "vpc:DescribeIPv6TranslatorAclLists", "vpc:DescribeIPv6TranslatorEntries", "vpc:DescribeInstances", "vpc:DescribeNetworkQuotas", "vpc:DescribePublicIpAddress", "vpc:DescribeRouterInterfacesForGlobal", "vpc:DescribeServerRelatedGlobalAccelerationInstances", "vpc:DescribeVPCs", "vpc:DescribeVpnGatewayAvailableZones", "vpc:DescribeVrouters", "vpc:DescribeZones", "vpc:DiagnoseVpnConnections", "vpc:DiagnoseVpnConnectionsHistory", "vpc:DiagnoseVpnGateway", "vpc:DisableNatGatewayEcsMetric", "vpc:EnableNatGatewayEcsMetric", "vpc:GetBusinessAccessPointDetail", "vpc:GetFlowLogServiceStatus", "vpc:GetNatIpCidrAttribute", "vpc:GetObject", "vpc:GetPhysicalConnectionServiceStatus", "vpc:GetPublicIpAddressPoolServiceStatus", "vpc:GetTrafficMirrorServiceStatus", "vpc:GetVpcIpamServiceStatus", "vpc:GetVpnGatewayDiagnoseResult", "vpc:InnerVpcCreateDscp", "vpc:InnerVpcDeleteDscp", "vpc:InnerVpcDescribeCrossBorderRouterInterface", "vpc:InnerVpcDescribeDscp", "vpc:InnerVpcModifyDscp", "vpc:InnerVpcRefreshDscp", "vpc:ListBusinessAccessPointPortUsage", "vpc:ListBusinessAccessPoints", "vpc:ListBusinessRegions", "vpc:ListGeographicSubRegions", "vpc:ListNatGatewayEcsMetric", "vpc:ListVpcEndpointServicesByEndUser", "vpc:ModifyBandwidthPackageAttribute", "vpc:ModifyBandwidthPackageSpec", "vpc:ModifyBypassToaAttribute", "vpc:ModifyExpressCloudConnectionAttribute", "vpc:ModifyGlobalAccelerationInstanceAttributes", "vpc:ModifyGlobalAccelerationInstanceSpec", "vpc:ModifyIPv6TranslatorAclAttribute", "vpc:ModifyIPv6TranslatorAclListEntry", "vpc:ModifyIPv6TranslatorAttribute", "vpc:ModifyIPv6TranslatorBandwidth", "vpc:ModifyIPv6TranslatorEntry", "vpc:OpenFlowLogService", "vpc:OpenPhysicalConnectionService", "vpc:OpenPublicIpAddressPoolService", "vpc:OpenTrafficMirrorService", "vpc:OpenVpcIpamService", "vpc:QueryHighReliablePhysicalConnectionPrice", "vpc:QueryPconnTrafficPrice", "vpc:QueryPhysicalConnectionPrice", "vpc:RejectVpcPeerConnection", "vpc:RemoveBandwidthPackageIps", "vpc:RemoveGlobalAccelerationInstanceIp", "vpc:RemoveIPv6TranslatorAclListEntry", "vpc:RevokeInstanceFromCbn", "vpc:TransformEipSegmentToPublicIpAddressPool", "vpc:UnAssociateEipAddress", "vpc:UnassociateGlobalAccelerationInstance", "vpc:UpdateCrossBoarderStatus", "vpc:associatevpccidrblock", "vpc:createvpc", "vpc:deleteBgpNetwork", "vpc:describeVpcs", "vpc:modifyVpcAttribute", "vpc:releaseIpv6Address" ], "Resource": "*" } ] }
重要
获得账号级别权限的RAM用户或RAM角色，能够操作整个账号范围内的相关资源。请务必确认所授予的权限是否符合预期，遵从最小授权原则谨慎分配权限。
## 常见问题
### 如何查看当前资源属于哪个资源组？
方式一：单击资源名称，进入资源的详情页面，即可查看到当前资源的资源组。
方式二：登录[资源管理控制台](https://resourcemanager.console.aliyun.com/)，单击资源中心>资源搜索，在左侧选择目标资源所属账号（默认为当前账号），通过筛选条件定位目标资源，即可查看其所属资源组。
### 如何查看当前产品在某个资源组下的所有资源？
方式一：登录[资源管理控制台](https://resourcemanager.console.aliyun.com/)，单击资源中心>资源搜索，然后在左侧的资源所属账号（默认为当前账号）下选择单击目标资源组名称，最后在右侧的选择资源类型中选择当前产品，即可查看当前产品在某个资源组下的所有资源。
方式二：登录[资源管理控制台](https://resourcemanager.console.aliyun.com/)，单击资源组>资源组，然后找到目标资源组，单击其所在行的操作列下的资源管理，最后在资源管理页面上方的产品下拉框中选择当前产品，即可查看当前产品在某个资源组下的所有资源。
### 如何批量修改多个资源的资源组？
登录[资源管理控制台](https://resourcemanager.console.aliyun.com/)，单击资源组>资源组，在目标资源组所在行的操作列下，单击资源管理以进入资源管理页面。通过筛选条件定位多个目标资源，批量勾选第一列的复选框后单击下方转移资源组，并按页面提示完成资源组修改。
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
