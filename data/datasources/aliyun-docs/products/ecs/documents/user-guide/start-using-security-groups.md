# 使用安全组-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/start-using-security-groups

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 使用安全组

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

[安全组](products/ecs/documents/user-guide/overview-44.md)在ECS的使用中扮演了云上虚拟防火墙的角色，通过管理安全组和规则，可提供精细化的网络安全隔离与访问控制。

下图示例通过配置两条安全组规则，实现仅允许授权IP远程管理实例，并阻止实例访问公网风险站点的场景。

- 

入方向规则：允许特定IP（121.XX.XX.XX）通过SSH（22端口）访问实例。

- 

出方向规则：拒绝实例访问某个已知的风险IP（XX.XX.XX.XX）。

## 为新建实例配置安全组

- 

前往购买实例：前往[ECS](https://ecs-buy.aliyun.com)[控制台-自定义购买](https://ecs-buy.aliyun.com)页面，选择实例配置。

- 

新建安全组：在网络和安全组内新建普通安全组或企业级安全组，并编辑安全组名称。

- 

快捷配置常用规则：购买实例时，控制台提供了常用的端口/协议，勾选后可以允许所有 IP 地址（0.0.0.0/0）来源访问目标端口，或允许遵循目标协议的流量访问创建的实例。

购买实例时新建安全组不支持精细配置新建安全组的规则，可以在实例创建后配置。若在快速配置勾选了管理实例使用的端口（如远程连接实例常用的SSH（22）、RDP（3389）等），建议创建实例后将安全组规则设置为仅允许从安全的IP地址进行访问。

- 

创建后配置安全组规则：购买实例后，可参考[安全组规则](products/ecs/documents/user-guide/security-group-rules.md)的配置信息，为新建的实例[配置安全组规则](products/ecs/documents/user-guide/start-using-security-groups.md)。

可以查看[安全组应用指导和案例](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md)，了解如限制实例访问、数据库安全策略等更多业务情况下的安全组规则配置案例方法。

## 创建安全组

购买 ECS 实例时可一并创建安全组，详见[为新建实例配置安全组](products/ecs/documents/user-guide/start-using-security-groups.md)。如需独立于实例创建安全组并关联至已有实例，按下方控制台或API步骤操作。

控制台

- 

前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)页面，单击创建安全组。

- 

设置安全组名称及专有网络 VPC。

- 

选择安全组类型为普通安全组或企业级安全组。

- 

为安全组配置[安全组规则](products/ecs/documents/user-guide/security-group-rules.md)。安全组规则为有状态规则，只需配置入方向，系统自动放行对应出方向响应流量。常用端口与授权建议见下表，完整示例见[安全组应用指导和案例](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md)。

一键放行 Web 常见端口（22/80/443/8888）

| 端口 | 协议 | 用途 | 授权对象建议 | 延伸阅读 |
| --- | --- | --- | --- | --- |
| 22 | TCP | SSH 远程连接（Linux） | 办公网或固定公网 IP； 不建议 长期使用 0.0.0.0/0 | [案例](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md) [2](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md) |
| 3389 | TCP | RDP 远程桌面（Windows） | 办公网或固定公网 IP； 不建议 长期使用 0.0.0.0/0 | [案例](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md) [2](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md) |
| 80 | TCP | HTTP | 公网建站可使用 0.0.0.0/0 | [案例](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md) [1](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md) |
| 443 | TCP | HTTPS | 公网建站可使用 0.0.0.0/0 | [案例](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md) [1](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md) |
| 8888 | TCP | 宝塔等管理面板（以面板实际端口为准） | 仅管理员 IP；按面板安装提示放行对应端口 | - |
| 3306 等 | TCP | 应用访问 VPC 内数据库 | 在数据库安全组 入方向 授权 源安全组 ，不对公网开放 | [案例](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md) [3](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md) |
| 业务端口 | TCP | 跨安全组内网互访（如 8080、3306） | 在 目标 安全组入方向授权 源安全组 ID | [案例](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md) [5](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md) |


在安全组详情页，选择规则方向后单击增加规则添加规则；已有规则可在访问规则区域编辑或删除。

警告

- 

最小权限：80/443可按需对公网开放；SSH（22）、RDP（3389）与面板端口应限定可信 IP，避免使用0.0.0.0/0或::/0。

- 

规则优先级：同优先级下，拒绝规则优先生效。对于[部分特定网络流量](products/ecs/documents/user-guide/security-group-rules.md)，安全组会默认放行。

- 

变更管理：避免直接修改生产环境的安全组，建议先[克隆安全组](products/ecs/documents/user-guide/start-using-security-groups.md)在测试环境验证后再调整线上规则。

- 

单击确定创建。

API

调用[CreateSecurityGroup](products/ecs/documents/developer-reference/api-ecs-2014-05-26-createsecuritygroup.md)，创建安全组。

创建安全组后，调用以下 API 管理安全组规则：

- 

调用[AuthorizeSecurityGroup](products/ecs/documents/developer-reference/api-ecs-2014-05-26-authorizesecuritygroup.md)，添加入方向规则。

- 

调用[AuthorizeSecurityGroupEgress](products/ecs/documents/developer-reference/api-ecs-2014-05-26-authorizesecuritygroupegress.md)，添加出方向规则。

- 

调用[ModifySecurityGroupRule](products/ecs/documents/developer-reference/api-ecs-2014-05-26-modifysecuritygrouprule.md)，修改入方向规则。

- 

调用[ModifySecurityGroupEgressRule](products/ecs/documents/developer-reference/api-ecs-2014-05-26-modifysecuritygroupegressrule.md)，修改出方向规则。

- 

调用[RevokeSecurityGroup](products/ecs/documents/developer-reference/api-ecs-2014-05-26-revokesecuritygroup.md)，删除入方向规则。

- 

调用[RevokeSecurityGroupEgress](products/ecs/documents/developer-reference/api-ecs-2014-05-26-revokesecuritygroupegress.md)，删除出方向规则。

创建的普通安全组若未配置规则时，入方向默认会允许同安全组内其他ECS的流量，拒绝其他所有入方向流量，出方向允许所有流量。

## 为实例关联安全组

当您为ECS实例关联安全组时，实际上是在为ECS实例的主网卡关联安全组。

控制台

- 

前往[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)单击目标实例ID进入实例详情页。

- 

在实例详情页切换至安全组页签，在安全组列表页单击更换安全组，按需将安全组加入实例或者移除实例。关联多个安全组时，安全组规则会合并，且按照优先级排序生效。

API

- 

调用[ModifyInstanceAttribute](products/ecs/documents/developer-reference/api-ecs-2014-05-26-modifyinstanceattribute.md)，为一台ECS实例设置多个安全组。

- 

调用[JoinSecurityGroup](products/ecs/documents/developer-reference/api-ecs-2014-05-26-joinsecuritygroup.md)，将一台ECS实例加入到指定的安全组。

- 

调用[LeaveSecurityGroup](products/ecs/documents/developer-reference/api-ecs-2014-05-26-leavesecuritygroup.md)，将一台ECS实例移出指定的安全组。

## 为辅助弹性网卡关联安全组

安全组实际作用在ECS实例的[弹性网卡](products/ecs/documents/user-guide/eni-overview.md)上。实例有多张弹性网卡时，为弹性网卡关联不同的安全组，并配置差异化的安全组规则，可以实现实例内部网络流量的分级管控与业务隔离。

控制台

- 

前往[ECS](https://ecs.console.aliyun.com/networkInterfaces)[控制台-弹性网卡](https://ecs.console.aliyun.com/networkInterfaces)页面，单击目标辅助网卡的ID，进入辅助弹性网卡详情页。

- 

单击更换安全组，勾选要关联的安全组，单击确定。

API

- 

调用[JoinSecurityGroup](products/ecs/documents/developer-reference/api-ecs-2014-05-26-joinsecuritygroup.md)将弹性网卡加入到指定的安全组。

- 

调用[LeaveSecurityGroup](products/ecs/documents/developer-reference/api-ecs-2014-05-26-leavesecuritygroup.md)将弹性网卡移出指定的安全组。

- 

使用[ModifyNetworkInterfaceAttribute](products/ecs/documents/developer-reference/api-ecs-2014-05-26-modifynetworkinterfaceattribute.md)为弹性网卡指定多个安全组。

## 安全组内实例网络互通

默认情况下，同一普通安全组内的ECS实例间内网互通。为提高安全性，可以将组内连通策略调整为组内隔离，禁止实例间的内网互通。

[企业级安全组](products/ecs/documents/user-guide/basic-security-groups-and-advanced-security-groups.md)不支持修改组内连通策略。

- 

当实例关联多个安全组时，只要其中任一安全组的组内连通策略设置为组内互通，实例间即可内网互通。

- 

安全组的组内连通策略设置为组内隔离时，可通过配置安全组规则，允许实例间通信。

控制台

- 

前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)，单击目标安全组ID进入安全组详情页。

- 

在安全组详情页面，页签基本信息区域，单击修改组内网络连通策略。

- 

安全组的组内连通策略已更改为组内隔离。

API

调用[ModifySecurityGroupPolicy](products/ecs/documents/developer-reference/api-ecs-2014-05-26-modifysecuritygrouppolicy.md)，修改普通安全组的组内连通策略。

## 安全组间实例网络互通

将其他安全组设为规则的授权对象时，可允许其他安全组内实例，通过内网访问本安全组内的实例。图中为安全组A设置了入方向的授权对象安全组B后，安全组B内的实例可以通过内网访问安全组A内的实例。

[企业级安全组](products/ecs/documents/user-guide/basic-security-groups-and-advanced-security-groups.md)规则不支持添加授权对象为安全组的规则。

控制台

- 

前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)，单击目标安全组ID进入安全组详情页。

- 

在目标安全组详情页面，选择规则需要控制方向，单击增加规则。

- 

在新建安全组规则页面选择访问来源为安全组或跨账号安全组。

API

- 

调用[AuthorizeSecurityGroup](products/ecs/documents/developer-reference/api-ecs-2014-05-26-authorizesecuritygroup.md)在安全组入方向规则中设置SourceGroupId授权已创建的安全组。

- 

调用[AuthorizeSecurityGroupEgress](products/ecs/documents/developer-reference/api-ecs-2014-05-26-authorizesecuritygroupegress.md)在安全组出方向规则中设置DestGroupId授权已创建的安全组。

## 更多操作

### 使用前缀列表和端口列表

当需对多个IP地址段或端口进行统一授权时，可使用前缀列表和端口列表集中管理，从而简化安全组规则配置，提升批量维护效率。

控制台

- 

创建前缀列表/端口列表：

- 

前往[ECS](https://ecs.console.aliyun.com/prefixList/)[控制台-前缀列表](https://ecs.console.aliyun.com/prefixList/)。

- 

根据需求选择到目标页签，单击创建前缀列表或创建端口列表。

引用前缀/端口列表的安全组，规则数量会根据列表设置的最大条目数计算。

- 

在目标安全组详情页访问规则区域增加或修改规则：

- 

设置访问来源为前缀列表，选择目标前缀列表。

- 

设置访问目的（本实例）为端口列表，选择目标端口列表。

API使用前缀列表

- 

调用[CreatePrefixList](products/ecs/documents/developer-reference/api-ecs-2014-05-26-createprefixlist.md)，创建一个前缀列表。创建完成后，可以通过[DescribePrefixListAttributes](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeprefixlistattributes.md)查询前缀列表的详细信息。

- 

调用[AuthorizeSecurityGroup](products/ecs/documents/developer-reference/api-ecs-2014-05-26-authorizesecuritygroup.md)在安全组入方向规则中，设置SourcePrefixListId授权已经创建的前缀列表。

- 

调用[AuthorizeSecurityGroupEgress](products/ecs/documents/developer-reference/api-ecs-2014-05-26-authorizesecuritygroupegress.md)在安全组出方向规则中，设置DestPrefixListId授权已经创建的前缀列表。

使用端口列表

- 

调用[CreatePortRangeList](products/ecs/documents/developer-reference/api-ecs-2014-05-26-createportrangelist.md)，创建一个端口列表。

- 

调用[DescribePortRangeLists](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeportrangelists.md)查看端口列表信息，并且可以通过[AuthorizeSecurityGroup](products/ecs/documents/developer-reference/api-ecs-2014-05-26-authorizesecuritygroup.md)、[AuthorizeSecurityGroupEgress](products/ecs/documents/developer-reference/api-ecs-2014-05-26-authorizesecuritygroupegress.md)在安全组规则中设置PortRangeListId授权已经创建的端口列表。

### 检查是否存在冗余规则

安全组健康检查功能可以识别冗余规则。当规则A的条件被规则B完全包含，且规则A的优先级不高于规则B时，规则A即为冗余规则。冗余规则会占用安全组规则配额，建议定期清理，以避免因规则数量达到上限而无法添加新规则。

- 

前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)在目标安全组详情页面的访问规则页签中，单击健康检查。

- 

在健康检查对话框中，选中待删除的冗余规则，单击删除上述规则。

### 克隆安全组

当需要批量创建带有相同配置的安全组，或进行跨地域、跨网络类型复制和备份时，可通过克隆安全组功能快速实现。克隆成功后，可在目标地域的安全组列表中看到新安全组。

- 

前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)，在目标安全组的操作栏单击克隆安全组。

- 

设置目标安全组，克隆后，新的安全组显示在目标地域的安全组列表中。

- 

专有网络ID：新安全组所属的专有网络。

- 

保留规则：勾选将保留原安全组中所有规则，优先级大于100的规则将调整为100。

- 

复制本安全组标签到克隆安全组：选择是否需要将原安全组的标签复制到新安全组。

### 导入/导出规则

如果需要备份、恢复和迁移规则，可以使用导入导出功能。

导入规则

导入的安全组规则需遵循以下要求：

- 

文件格式：JSON或CSV。

- 

规则数量：单次导入不超过200条。

- 

规则优先级：1到100之间。优先级高于100的规则将被忽略。

在跨地域导入规则时，不支持安全组规则中授权对象为安全组和前缀列表，不支持安全组规则中端口范围为端口列表。

- 

前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)在目标安全组详情页面访问规则区域，单击导入安全组规则。

- 

在导入安全组规则页面，单击选择文件并选中本地的JSON或CSV文件，单击确认。

导入失败时，将鼠标悬停在警告图标上可查看原因。

导出规则

前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)，在目标安全组详情页访问规则区域，单击导出。导出的规则文件的命名格式：

- 

JSON格式：ecs_${region_id}_${groupID}.json。

示例：如果Region ID为cn-qingdao，安全组ID为sg-123，则导出的文件名为ecs_cn-qingdao_sg-123.json。

- 

CSV格式：ecs_sgRule_${groupID}_${region_id}_${time}.csv。

示例：如果Region ID为cn-qingdao，安全组ID为sg-123，导出日期为2020-01-20，则导出的文件名为ecs_sgRule_sg-123_cn-qingdao_2020-01-20.csv。

### 安全组快照

安全组快照可自动备份安全组规则。当安全组规则发生变更时，系统会自动创建快照。通过快照可恢复指定时间点的安全组规则，防止因误操作导致规则丢失。

重要

- 

安全组规则变更后，系统将在5分钟后创建快照。若5分钟内发生多次变更，系统仅会基于首次变更前的规则创建一次快照。

- 

安全组快照使用对象存储服务（OSS）存储备份数据。OSS为按量计费服务，使用安全组快照会产生相应的OSS存储和请求费用。

创建快照策略

- 

前往[ECS](https://ecs.console.aliyun.com/securityGroupSnapshotPolicy)[控制台-安全组快照](https://ecs.console.aliyun.com/securityGroupSnapshotPolicy)，单击新建安全组快照策略。

- 

在新建快照策略对话框中，配置以下信息：

- 

策略名称：输入快照策略的名称。

- 

策略状态：选择启用或禁用。仅当策略为启用状态时，才会为关联的安全组创建快照。

- 

快照保留时间：设置快照保留天数，范围为1-30天，默认值为1天。超过保留时间的快照将被自动删除。

- 

OSS 存储配置：配置用于存储快照数据的OSS Bucket。若Bucket名称留空，系统将使用默认Bucket。

- 

单击确定。

首次创建快照策略时，系统会提示授权服务关联角色（SLR）ALIYUNSECURITYGROUPSNAPSHOTROLE以访问OSS存储桶。若该角色已存在，则无需重复授权。

关联安全组到快照策略

创建快照策略后，需将其与安全组关联，才能开始备份安全组规则。

关联安全组到快照策略时，系统会立即为该安全组创建一次快照。

- 

前往[ECS](https://ecs.console.aliyun.com/securityGroupSnapshotPolicy)[控制台-安全组快照](https://ecs.console.aliyun.com/securityGroupSnapshotPolicy)，找到目标快照策略，在操作列单击关联安全组。

- 

在关联安全组对话框中，选择要关联的安全组。

一个快照策略最多可关联10个安全组，一个安全组可关联多个策略不同的快照策略。

- 

单击确定完成关联。

从快照恢复规则

重要

恢复操作会立即生效，当前所有规则将被快照中的规则完全覆盖。恢复后无法撤销。

- 

前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)页面，单击目标安全组ID进入安全组详情页。

- 

在安全组详情页，切换至快照列表页签，找到目标快照，在操作列单击恢复快照。

- 

在恢复安全组快照对话框中，确认恢复信息。

- 

在入方向和出方向页签下，对比当前安全组规则和恢复后安全组规则。

- 

确认无误后，单击确定。

### 删除安全组

警告

删除安全组是一个不可逆的操作，将永久删除安全组下所有规则。在执行删除操作前，请确保备份相关配置。

控制台

- 

前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)，在目标安全组的操作栏单击删除。

- 

在删除安全组对话框中，确认信息后，单击确定。

如果安全组没有关联的ECS实例和弹性网卡，在删除安全组对话框中仍提示不可删除时，可以单击尝试强制删除。

API

调用[DeleteSecurityGroup](products/ecs/documents/developer-reference/api-ecs-2014-05-26-deletesecuritygroup.md)，删除安全组。

安全组在以下场景时无法删除：

- 

已关联ECS实例或弹性网卡时无法删除，需先将其移除。

- 

被其他安全组规则授权，需先删除授权规则。

- 

[托管安全组](products/ecs/documents/user-guide/managed-security-groups.md)仅支持查看，不可删除。

- 

开启了删除保护，请先关闭删除保护，然后再尝试操作。如果无法关闭删除保护则无法删除安全组。

在使用[DeleteSecurityGroup](products/ecs/documents/developer-reference/api-ecs-2014-05-26-deletesecuritygroup.md)接口删除安全组时返回错误码InvalidOperation.DeletionProtection，或使用控制台删除安全组看到类似删除保护的提示时，说明该安全组开启了删除保护功能。

## 生产应用建议

- 

安全组规划

- 

职责单一：Web、数据库、缓存等各业务场景下安全组应各自独立。

- 

环境隔离：生产、测试环境的安全组须分离，避免混用。

- 

命名规范：采用环境-应用-用途-sg格式，如prod-mysql-db-sg。

- 

规则配置

- 

最小权限：仅对必要的源开放必要的端口。避免对SSH（22）、RDP（3389）等管理端口开放0.0.0.0/0应始终限定为可信的固定IP。

- 

默认拒绝：默认拒绝所有入方向流量。仅在必要时，添加入方向规则，放行特定端口和来源的访问。

- 

规则优先级冲突：当实例关联多个安全组时，低优先级的允许规则会被高优先级的拒绝规则覆盖。排查网络不通时，需检查所有关联的安全组。

- 

变更管理

- 

避免直接修改生产环境：直接修改生产环境的安全组是高危操作。可以先[克隆安全组](products/ecs/documents/user-guide/start-using-security-groups.md)，在测试环境调试，确保修改后实例流量正常，再对线上环境的安全组规则进行修改。

## 计费规则

安全组免费使用。

## 使用限制

- 

- 

- 

| 限制项 | 普通安全组限制 | 企业级安全组限制 |
| --- | --- | --- |
| 单个阿里云账号在特定地域下的安全组总数量上限 | 请根据配额 ID q_security-groups 查看或申请提升对应配额。具体操作请参见 [查看或提升云服务器 ECS](products/ecs/documents/user-guide/quota-management.md) [配额](products/ecs/documents/user-guide/quota-management.md) 。 | 与普通安全组相同 |
| 单张弹性网卡可以关联的安全组数量 | 10 | 与普通安全组相同 |
| 单张弹性网卡关联的所有安全组的规则（包括入方向规则与出方向规则）数量之和的上限 | 1,000 | 与普通安全组相同 |
| 单个安全组中，授权对象为安全组的规则数量 | 20 | 0 条，在企业级安全组中，您不能添加授权对象为安全组的规则，也不能将企业级安全组作为其他安全组规则中的授权对象。 |
| 单个专有网络 VPC 类型的安全组能容纳的 VPC 类型 ECS 实例数量 | 不固定，受安全组能容纳的私网 IP 地址数量影响。 | 无限制 |
| 单个阿里云账号在特定地域下单个专有网络 VPC 类型的安全组能容纳的私网 IP 地址数量 | 6,000 说明 IP 占用数按照安全组关联的弹性网卡（包括实例主网卡、辅助网卡）的私网 IP 数量计数，包括主私网 IPv4、IPv6、辅助私网 IPv4、IPv4 前缀、IPv6 前缀等所有类型 IP 地址的数量总和。 如果您有超过 6,000 个私网 IP 需要内网互访，可以将这些私网 IP 的 ECS 实例分配到多个安全组内，并通过互相授权的方式允许互访。 您可以在 [配额中心](https://quotas.console.aliyun.com/products/ecs/quotas?spm=a2c4g.11186623.0.0.376656addmG73f) 根据配额 ID q_vpc-normal-security-group-ip-count 查看专有网络普通安全组内的私网 IP 地址数量上限。 | 65,536 说明 IP 占用数按照安全组关联的弹性网卡（包括实例主网卡、辅助网卡）的数量计数，即关联的所有弹性网卡的数量总和。 |
| 公网访问端口 | 基于安全考虑，ECS 实例 25 端口默认受限，建议您使用 SSL 加密端口（通常是 465 端口）来对外发送邮件。 具体操作，请参见 [使用](https://help.aliyun.com/zh/cloud-web-hosting/use-cases/encrypted-using-ssl-port-465-to-send-email#task-2669194) [SSL](https://help.aliyun.com/zh/cloud-web-hosting/use-cases/encrypted-using-ssl-port-465-to-send-email#task-2669194) [加密](https://help.aliyun.com/zh/cloud-web-hosting/use-cases/encrypted-using-ssl-port-465-to-send-email#task-2669194) [465](https://help.aliyun.com/zh/cloud-web-hosting/use-cases/encrypted-using-ssl-port-465-to-send-email#task-2669194) [端口发送邮件](https://help.aliyun.com/zh/cloud-web-hosting/use-cases/encrypted-using-ssl-port-465-to-send-email#task-2669194) 。 | 与普通安全组相同 |


## 常见问题

实例ping不通怎么办？

无法ping通ECS实例，通常是因为安全组中入方向ICMP协议（ping 命令所使用的协议）的默认规则被移除。可以使用安全组规则诊断工具快速定位问题。

- 

前往[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)找到目标实例并记录实例ID。

- 

单击一键诊断进入自助问题排查页面，并切换至目标地域。

- 

选择安全组规则诊断，单击发起诊断。

- 

选择记录的实例 ID及对应的网卡。单击开始检测。

多数情况下，一台实例只有一张网卡。

- 

查看检测结果。如果结果显示ICMP协议未放行，单击开通端口即可快速开通。

除ICMP外，诊断工具还会检测以下常用端口是否放行：80、443、22、3389和8080。

- 

如果检测后发现还是ping不通可以根据[无法](products/ecs/documents/troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[ping](products/ecs/documents/troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[通](products/ecs/documents/troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[ECS](products/ecs/documents/troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[实例公网](products/ecs/documents/troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[IP](products/ecs/documents/troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[的排查方法](products/ecs/documents/troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)更进一步排查。

实例连不上、服务访问不通怎么办？

服务无法访问，通常是由于安全组未放行端口。可以使用安全组规则诊断工具快速定位问题。

- 

前往[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)找到目标实例并记录实例ID。

- 

单击一键诊断进入自助问题排查页面，并切换至目标地域。

- 

选择安全组规则诊断，单击发起诊断。

- 

选择记录的实例 ID及对应的弹性网卡，并根据服务端口，选择诊断方式后，单击开始检测，查看诊断结果。

- 

一键检测：适用于80、443、22、3389或8080端口。

- 

自定义检测：适用于所有其他端口。需要填写以下信息：

- 

源地址：输入本地或客户端的公网IP地址。

- 

目的端口：输入服务使用的端口号。

- 

协议类型：选择端口对应的协议。

安全组与网络ACL（NACL）有何区别？

| 特性 | 安全组 | 网络 ACL |
| --- | --- | --- |
| 作用层级 | 弹性网卡 | 子网级 |
| 状态 | 有状态 | 无状态 |
| 用途 | 实例的精细化防火墙 | 子网的边界访问控制 |


实例主网卡的安全组如何更换/添加？

安全组实际作用在ECS实例的[弹性网卡](products/ecs/documents/user-guide/eni-overview.md)上。ECS实例详情页面上安全组页签中配置的安全组，即为实例主网卡的安全组。可参考[为实例关联安全组](products/ecs/documents/user-guide/start-using-security-groups.md)更改实例主网卡关联的安全组。

安全组规则设置为全部拒绝后，如何允许阿里云内部服务访问？

添加入方向安全组规则，允许来自100.64.0.0/10地址段的访问。阿里云使用该保留地址段对实例进行健康检查和可用性监控。

## 相关文档

- 

[安全组规则检测](products/ecs/documents/user-guide/safety-set-of-rules-to-detect.md)

- 

[禁止](products/ecs/documents/user-guide/prohibit-ram-users-from-creating-high-risk-security-group-rules.md)[RAM](products/ecs/documents/user-guide/prohibit-ram-users-from-creating-high-risk-security-group-rules.md)[用户创建高危安全组规则](products/ecs/documents/user-guide/prohibit-ram-users-from-creating-high-risk-security-group-rules.md)

- 

[对安全组规则的合规性进行自动审计修复](products/ecs/documents/user-guide/automatically-audit-the-compliance-of-security-group-rules.md)

- 

[安全组应用指导和案例](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md)

- 

[常用端口](products/ecs/documents/user-guide/common-ports.md)

- 

[无法连接](products/ecs/documents/troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)[Linux](products/ecs/documents/troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)[实例的排查方法](products/ecs/documents/troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)

- 

[无法远程连接](products/ecs/documents/solution-to-failure-in-remote-connection-to-windows-instance.md)[Windows](products/ecs/documents/solution-to-failure-in-remote-connection-to-windows-instance.md)[实例的排查方法](products/ecs/documents/solution-to-failure-in-remote-connection-to-windows-instance.md)

- 

[ECS](products/ecs/documents/user-guide/the-security-group-rules-for-the-ecs-instance-are-not-applied.md)[实例的安全组规则未生效问题排查](products/ecs/documents/user-guide/the-security-group-rules-for-the-ecs-instance-are-not-applied.md)

- 

[无法](products/ecs/documents/troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[ping](products/ecs/documents/troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[通](products/ecs/documents/troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[ECS](products/ecs/documents/troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[实例公网](products/ecs/documents/troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[IP](products/ecs/documents/troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[的排查方法](products/ecs/documents/troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)

[上一篇：安全组规则](products/ecs/documents/user-guide/security-group-rules.md)[下一篇：普通安全组与企业级安全组](products/ecs/documents/user-guide/basic-security-groups-and-advanced-security-groups.md)

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
