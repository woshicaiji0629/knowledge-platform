# 使用标签限制 RAM 用户管理 VPC-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/use-tags-to-restrict-ram-users-ability-to-manage-vpcs

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

# 使用标签限制 RAM 用户管理 VPC

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以为 VPC 绑定标签，通过 RAM 的自定义策略指定授权的标签，利用标签限制 RAM 用户只能在指定的 VPC 中创建和管理交换机、网络ACL等资源。

## 工作原理

基于标签的 RAM 鉴权（标签鉴权）可以精细控制 RAM 用户对 VPC 资源的操作权限。在VPC场景下，标签鉴权常用于以下需求：

- 

限制 RAM 用户只能在特定VPC下创建资源（如交换机、网络ACL）。

- 

限制 RAM 用户创建资源时必须携带指定标签。

- 

限制 RAM 用户只能管理（修改、删除）带有特定标签的资源。

### 鉴权流程

标签鉴权的核心流程如下图所示：当RAM用户发起API请求时，RAM会根据主账号授予的权限策略中的Condition条件，同时检查请求中携带的标签（acs:RequestTag）和目标资源上已绑定的标签（acs:ResourceTag），只有所有条件均满足时，操作才会被允许。

### Condition Key 说明

标签鉴权通过权限策略中的条件（Condition）实现，支持以下两种Condition Key：

| 对比维度 | acs:ResourceTag | acs:RequestTag |
| --- | --- | --- |
| 检查对象 | 被操作的资源上已绑定的标签 | API 请求中传递的标签信息 |
| 典型场景 | 控制 可以操作哪些资源 | 控制 调用 API 操作资源时必须带什么标签 |
| 效果 | 限制操作范围（只能操作特定资源） | 限制操作行为（调用 API 时，请求参数里面必须携带的标签） |


通过组合使用acs:ResourceTag和acs:RequestTag，可以同时控制在哪个资源下操作和调用 API 操作资源时必须带什么标签，实现更精细的权限管理。

### 支持的资源

- 

网络基础资源：专有网络（VPC）、交换机（VSwitch）、路由器（VRouter）、路由表（RouteTable）、预留网段（VSwitchCidrReservation）、高可用虚拟 IP（HaVip）、DHCP 选项集（DHCPOptionsSet）

- 

弹性公网 IP 与带宽：弹性公网 IP（EIP）、共享带宽（BandwidthPackage、CombandwidthPackage）、公网 IP 地址池（PublicIpAddressPool）、连续公网 IP 地址段（PublicIpAddressRange）

- 

NAT 网关：NAT 网关（NatGateway）

- 

IPv4/IPv6：IPv4 网关（IPv4Gateway）、IPv6 网关（IPv6Gateway）、IPv6 地址（IPv6Address）、IPv6 公网带宽（IPv6Bandwidth）

- 

安全与访问控制：网络 ACL（NetworkAcl）、前缀列表（PrefixList）、网关终端节点（GatewayEndpoint）

- 

流量监控与镜像：流日志（FlowLog）、流量镜像筛选条件（TrafficMirrorFilter）、流量镜像会话（TrafficMirrorSession）

## 隔离 VPC 各租户创建/删除交换机

### 场景示例

企业有不同的部门（如财务部、人事部），需要通过 RAM（访问控制）实现按部门隔离 VPC 资源的管理权限，并且要求特定部门（财务部）在创建资源时必须符合特定的规范（如打上生产环境标签）。

- 

资源划分（部门隔离）：

- 

VPC-A （财务部）：绑定标签department:finance

- 

VPC-B （人事部）：绑定标签department:hr

- 

权限分配与标签鉴权

- 

跨部门隔离（按 VPC，使用 ResourceTag）：只能在 VPC-A (department:finance) 下操作。

- 

资源创建合规（按请求参数，使用 RequestTag）：在 VPC-A 下创建交换机或网络 ACL 时，必须携带env:prod标签。

- 

生命周期安全管理（按子资源，使用 ResourceTag）：只能修改或删除自身带有env:prod标签的交换机和网络 ACL。

### 操作步骤

控制台

使用阿里云主账号（管理员）完成：

- 

前往[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)，[创建](products/ram/documents/user-guide/create-a-ram-user.md)[RAM](products/ram/documents/user-guide/create-a-ram-user.md)[用户](products/ram/documents/user-guide/create-a-ram-user.md)。

- 

为 VPC 绑定标签：前往[VPC 控制台](https://vpc.console.aliyun.com/vpc/)，将鼠标悬停在目标 VPC标签列的图标，单击气泡框中的绑定或编辑。

- 

VPC-A：department:finance。

- 

VPC-B：department:hr。

- 

在[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)，[创建自定义权限策略](products/ram/documents/create-a-custom-policy.md)VpcTagAccessPolicy。

本示例中为 VPC 和交换机使用了不同的标签键：

- 

department:finance用于acs:ResourceTag条件：控制可以在哪个VPC下操作。

- 

env:prod用于acs:RequestTag条件：控制创建子资源时必须携带的标签。

在实际使用中，您也可以为两者使用相同的标签键，根据业务需要灵活配置。

{ "Version": "1", "Statement": [ { // Statement 1：仅允许在绑定了标签 department:finance 的VPC中创建交换机和网络ACL。 // 使用 acs:ResourceTag，检查被操作的VPC（父资源）上是否绑定了指定标签。 "Effect": "Allow", "Action": [ "vpc:CreateVSwitch", "vpc:CreateNetworkAcl" ], "Resource": "acs:vpc:*:*:vpc/*", "Condition": { "StringEquals": { "acs:ResourceTag/department": [ "finance" ] } } }, { // Statement 2：创建交换机时，请求中必须携带标签 env:prod。 // 使用 acs:RequestTag，检查API请求参数中是否包含指定标签。 "Effect": "Allow", "Action": [ "vpc:CreateVSwitch" ], "Resource": "acs:vpc:*:*:vswitch/*", "Condition": { "StringEquals": { "acs:RequestTag/env": [ "prod" ] } } }, { // Statement 3：创建网络ACL时，请求中必须携带标签 env:prod。 // 同样使用 acs:RequestTag。 "Effect": "Allow", "Action": [ "vpc:CreateNetworkAcl" ], "Resource": "acs:vpc:*:*:networkacl/*", "Condition": { "StringEquals": { "acs:RequestTag/env": [ "prod" ] } } }, { // Statement 4：仅允许修改和删除绑定了标签 env:prod 的交换机和网络ACL。 // 使用 acs:ResourceTag，检查被操作的子资源上是否绑定了指定标签。 "Effect": "Allow", "Action": [ "vpc:ModifyVSwitchAttribute", "vpc:DeleteVSwitch", "vpc:ModifyNetworkAclAttributes", "vpc:DeleteNetworkAcl" ], "Resource": "*", "Condition": { "StringEquals": { "acs:ResourceTag/env": [ "prod" ] } } }, { // Statement 5：允许查看VPC相关资源的信息（无条件限制）。 "Effect": "Allow", "Action": [ "vpc:Describe*", "vpc:List*" ], "Resource": "*" }, { // Statement 6：（推荐）显式禁止标签操作。虽然本策略未授予标签权限（隐式拒绝已生效）， // 但显式 Deny 可防止后续添加其他策略（如 vpc:）时意外授予标签修改权限。 // 创建资源时通过 Create 类API的 Tag 参数指定标签，由Statement 2授权允许，不受Statement 6影响。 "Effect": "Deny", "Action": [ "vpc:TagResources", "vpc:UnTagResources" ], "Resource": "*" } ] }

- 

[为](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)： 资源范围选择账号级别，授权主体选择需要添加权限的RAM用户，权限策略选择自定义策略VpcTagAccessPolicy。

API

使用阿里云主账号（管理员）完成：

- 

调用[CreateUser](products/ram/documents/developer-reference/api-ram-2015-05-01-createuser.md)创建 RAM 用户。

- 

调用[TagResources](https://help.aliyun.com/zh/resource-management/tag/developer-reference/api-tag-2018-08-28-tagresources)为 VPC 创建并绑定标签。

- 

调用[CreatePolicy](products/ram/documents/developer-reference/api-ram-2015-05-01-createpolicy.md)创建自定义权限策略。

- 

调用[AttachPolicyToUser](products/ram/documents/developer-reference/api-ram-2015-05-01-attachpolicytouser.md)为 RAM 用户授权。

### 结果验证

使用授权的RAM用户验证标签鉴权是否生效：

- 

前往[VPC](https://vpc.console.aliyun.com/vpc/cn-hangzhou/switches/new)[控制台 - 创建交换机页面](https://vpc.console.aliyun.com/vpc/cn-hangzhou/switches/new)，创建交换机时指定目标专有网络、标签键、标签值。

- 

前往[VPC](https://vpc.console.aliyun.com/vpc/cn-hangzhou/switches)[控制台 - 交换机页面](https://vpc.console.aliyun.com/vpc/cn-hangzhou/switches)，删除绑定指定标签的交换机。

| 验证场景 | 结果 | 原因 |
| --- | --- | --- |
| 在 VPC-A（ department:finance ）中创建交换机，请求中携带标签 env:prod | 成功 | acs:ResourceTag 和 acs:RequestTag 条件均满足 |
| 在 VPC-B（ department:hr ）中创建交换机，请求中携带标签 env:prod | 失败 | VPC 上的 acs:ResourceTag 不满足（ department ≠ finance ） |
| 在 VPC-A 中创建交换机，不携带标签或携带其他标签 | 失败 | acs:RequestTag 不满足（未携带 env:prod ） |
| 在 VPC-B 中创建交换机，不携带标签 | 失败 | acs:ResourceTag 和 acs:RequestTag 条件均不满足 |
| 删除已绑定 env:prod 标签的交换机 | 成功 | 交换机上的 acs:ResourceTag 满足（ env = prod ） |
| 删除未绑定 env:prod 标签的交换机 | 失败 | 交换机上的 acs:ResourceTag 不满足 |


[上一篇：使用专有网络VPC访问控制功能](products/vpc/documents/access-control-1.md)[下一篇：基础设施安全](products/vpc/documents/infrastructure-security.md)

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
