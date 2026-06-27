# 共享VPC-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/vpc-sharing

# 共享VPC
对于非默认 VPC，您可以通过资源共享将 VPC 内的交换机共享给其他阿里云账号（主账号），以支持各个账号在共享交换机内创建ECS、RDS等资源。交换机使用者只能查看和管理自己创建的资源，无法查看、修改或删除其他账号的资源。
## 工作原理
账号A将自己拥有的交换机共享给账号B、C、D后，每个账号可以在已共享的交换机内创建云资源，这些云资源共用交换机的IP地址空间，默认网络互通。交换机所有者（账号A）也可以通过配置网络ACL或安全组，实现交换机或云资源之间的网络隔离。
共享VPC的典型应用场景：
企业网络集中管理：网络运维团队集中规划、配置和管理VPC，并将VPC的交换机共享给业务部门。业务部门可以根据业务需求在共享交换机中创建管理ECS等资源，无需关注网络配置和管理。
简化多账号网络运维：将VPC的交换机共享给多个账号，不用为每个账号单独配置VPC网络，从而极大减少了VPC的使用数量，降低多账号场景下的网络运维复杂度。
## 使用限制
默认VPC不支持共享，您需要先创建自定义VPC，再使用VPC共享功能。如果默认VPC中已有存量云资源，您可以考虑将这些云资源迁移或重建到非默认VPC。
使用共享VPC实现存量云资源的网络互通时，请先参考[支持在共享交换机下创建的云资源类型](vpc-sharing.md)和[交换机所有者和使用者的权限](vpc-sharing.md)，判断是否适用。如果适用，建议优先在共享VPC中重建存量云资源；若云资源本身支持跨VPC迁移，也可直接迁移至共享VPC。如果不适用或重建、迁移不可行，请使用[VPC](create-and-manage-vpc-peering-connection.md)[对等连接](create-and-manage-vpc-peering-connection.md)或[云企业网](../../cen/documents/getting-started/use-enterprise-edition-transit-routers-to-connect-vpcs-across-regions-and-accounts.md)[CEN](../../cen/documents/getting-started/use-enterprise-edition-transit-routers-to-connect-vpcs-across-regions-and-accounts.md)实现跨账号网络互通。
### 支持在共享交换机下创建的云资源类型
ECS实例
SLB实例
RDS实例
容器服务Terway组件
MongoDB实例
Redis实例
Kafka实例
Elasticsearch
ACR实例
PolarDB MySQL集群
RocketMQ实例
MSE注册配置中心
### 交换机所有者和使用者的权限
针对已共享的交换机：
| 目标 | 交换机所有者的权限 | 交换机使用者的权限 |
| --- | --- | --- |
| 云资源（ECS、RDS 等） | 每个账号只能查看和管理自身创建的云资源，无法查看和管理其他账号创建的云资源。 |  |
| 安全组 | 每个账号只能查看和管理自身创建的安全组，无法查看和管理其他账号创建的安全组。 |  |
| 弹性网卡 | 可以使用 [DescribeNetworkInterfaces](../../ecs/documents/developer-reference/api-ecs-2014-05-26-describenetworkinterfaces.md) 查看使用者创建的弹性网卡，无法管理使用者创建的弹性网卡。 | 只可查看和管理自身创建的弹性网卡，无法查看其他账号的弹性网卡。 |
| VPC、交换机、路由表、网络 ACL、附加网段 | 全部权限 | 仅可查看 |
| 预留网段 | 全部权限 | 无权限 |
| IPv6 网关 | 全部权限 | 为 ECS、弹性网卡、NLB 等资源分配/删除 IPv6 私网地址 可查看自己账号下的 IPv6 地址 可为自己账号下的 IPv6 地址开通/关闭公网带宽、设置/删除仅主动出规则。公网带宽费由交换机使用者支付。 |
| 流日志 | 支持创建 VPC、交换机粒度的流日志，仅对交换机所有者的弹性网卡生效。 支持创建弹性网卡粒度的流日志，仅对交换机所有者的弹性网卡生效。 | 只能创建弹性网卡粒度的流日志，且仅对交换机使用者的弹性网卡生效。 |
| NAT 网关、VPN 网关、云企业网、VPC 对等连接 | 全部权限 | 无查看和管理权限，但可以通过所有者创建的这些网络资源，实现与 VPC 外部网络互通。 |
| 标签 | 共享行为不影响交换机所有者为资源配置的标签。交换机所有者与交换机使用者都可以为各自的资源配置标签，且标签互不可见也互不影响。 |  |
交换机取消共享后：
| 目标 | 交换机使用者的权限 |
| --- | --- |
| 云资源（ECS、RDS 等） | 可以继续使用和管理（查看、修改、删除）自身已创建的云资源，但无法继续创建资源。 |
| 交换机及其关联资源 | 无法查看共享交换机，也无法查看共享交换机相关联的资源（例如 VPC、路由表、私网网段、网络 ACL）。 |
| 标签 | 系统会删除交换机使用者在该共享交换机上配置的标签。 |
## 在共享交换机中创建云资源
交换机所有者可以将交换机共享给任意阿里云账户，也可以仅在[资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)内共享。交换机所有者开启共享后，使用者就可在共享交换机中创建云资源。
### 控制台
一、开启共享此处仅介绍将交换机共享给任意账户的方式。针对资源目录方式，请参考[仅在资源目录内共享资源](https://help.aliyun.com/zh/resource-management/resource-sharing/getting-started/share-resources-with-objects-in-a-resource-directory)。
登录交换机所有者的账号，前往资源管理控制台的[资源共享-我的共享](https://resourcemanager.console.aliyun.com/resource-shares/cn-hangzhou/owned)页面。先在顶部菜单栏左上处，选择共享资源所在的地域，再单击创建共享单元，在打开的页面中：
第一步：输入共享单元名称，然后选中需要共享的交换机。
第二步：系统会默认选择AliyunRSDefaultPermissionVSwitch权限。
第三步：资源使用者范围选择允许共享给任意账号，添加方式选择手动添加，使用者ID输入交换机使用者的[阿里云账号](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)[ID](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)，并点击添加。
第四步：检查无误后，在页面底部单击确定。
登录交换机使用者的账号，接受共享邀请：
前往资源管理控制台的[资源共享-共享给我](https://resourcemanager.console.aliyun.com/resource-shares/cn-hangzhou/shared)页面。
在顶部菜单栏左上处，选择共享资源所在的地域，再单击目标共享单元状态列的接受。
接受后，交换机使用者就可以访问共享的交换机，且后续该共享单元新增的共享资源将默认接受共享邀请。
二、在共享交换机创建云资源
登录交换机使用者的账号：
前往专有网络控制台[交换机](https://vpc.console.aliyun.com/vpc/cn-hangzhou/switches)页面，在顶部状态栏选择共享交换机的地域后，您可以看到共享交换机（被标记为来自共享）。
针对ECS、RDS、SLB实例，您可以在目标共享交换机的操作列，单击添加云产品进行创建。
其他[支持在共享交换机下创建的云资源类型](vpc-sharing.md)，请在创建时选择共享交换机。
### API
一、开启共享
方式一：共享给任意账户
使用交换机所有者的身份凭证，调用[CreateResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-createresourceshare)创建共享单元，并确保将AllowExternalTargets参数设为True。
使用交换机使用者的身份凭证，先调用[ListResourceShareInvitations](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-listresourceshareinvitations)查询收到的资源邀请信息，再调用[AcceptResourceShareInvitation](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-acceptresourceshareinvitation)接受资源共享邀请。
方式二：仅在资源目录内共享
使用资源目录管理账号的身份凭证，调用[EnableSharingWithResourceDirectory](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-enablesharingwithresourcedirectory)启用资源目录组织共享。
使用交换机所有者的身份凭证，调用[CreateResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-createresourceshare)创建共享单元，并确保将AllowExternalTargets参数设为False。
二、创建云资源
登录交换机使用者的账号：
调用[DescribeVSwitches](developer-reference/api-vpc-2016-04-28-describevswitches.md)获取交换机列表。
在交换机列表中，过滤出共享交换机（ShareType字段值为Sharing）。
调用云资源的创建接口（例如ECS的[RunInstances](../../ecs/documents/developer-reference/api-ecs-2014-05-26-runinstances.md)），基于共享交换机创建云资源。
### Terraform
一、开启共享
交换机所有者创建共享单元：
当前Terraform不支持将交换机共享给任意账户，仅支持在资源目录内共享，请您在操作前确保资源目录管理账号已[启用资源目录组织共享](https://help.aliyun.com/zh/resource-management/resource-sharing/user-guide/enable-resource-sharing)。Resources:[alicloud_resource_manager_resource_share](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/resource_manager_resource_share)、[alicloud_resource_manager_shared_resource](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/resource_manager_shared_resource)、[alicloud_resource_manager_shared_target](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/resource_manager_shared_target)# 指定地域 provider "alicloud" { region = "cn-hangzhou" } # 指定共享单元名称 resource "alicloud_resource_manager_resource_share" "example_unit" { resource_share_name = "example_unit_name" } # 指定共享交换机 resource "alicloud_resource_manager_shared_resource" "example_vsw" { resource_share_id = alicloud_resource_manager_resource_share.example_unit.id resource_id = "vsw-bp1omg98fixldnwcxxxxx" # 修改为实际的共享交换机ID resource_type = "VSwitch" # 资源类型为交换机 } # 指定共享交换机的使用者 resource "alicloud_resource_manager_shared_target" "example_target" { resource_share_id = alicloud_resource_manager_resource_share.example_unit.id target_id = "10xxxxxxxxxxxxxx" # 修改为交换机使用者的实际UID }
二、在共享交换机创建云资源
以交换机使用者在共享交换机中创建1台ECS为例：
Resources:[alicloud_security_group](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/security_group)、[alicloud_instance](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/instance)Data Sources:[alicloud_vswitches](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/vswitches)# 指定地域 provider "alicloud" { region = "cn-hangzhou" } # 指定共享交换机 variable "vsw_id" { default = "vsw-bp1omg98fixldnwcxxxxx" # 替换为实际的共享交换机ID } # 获取目标共享交换机的信息 data "alicloud_vswitches" "example_vsw" { ids = [var.vsw_id] } # 创建安全组 resource "alicloud_security_group" "example_sg" { security_group_name = "example_sg_name" vpc_id = data.alicloud_vswitches.example_vsw.vswitches[0].vpc_id } # 创建ECS resource "alicloud_instance" "example_ecs" { instance_name = "example_ecs_name" instance_type = "ecs.e-c1m1.large" security_groups = [alicloud_security_group.example_sg.id] vswitch_id = var.vsw_id image_id = "aliyun_3_x64_20G_alibase_20250117.vhd" system_disk_category = "cloud_essd" }
## 管理共享交换机和使用者
交换机所有者可参考如下步骤，来完成：
查看已共享的交换机
查看共享交换机的使用者
共享更多交换机
将交换机共享给更多账号
### 控制台
前往资源管理控制台的[资源共享-我的共享](https://resourcemanager.console.aliyun.com/resource-shares/cn-hangzhou/owned)页面。在顶部菜单栏左上处，选择共享资源所在的地域。
在我的共享页面，您可以：
查看已共享的交换机：单击共享的资源页签进行查看。
查看共享交换机的使用者：单击资源使用者页签进行查看。
单击共享单元页签，找到目标共享单元，单击共享单元ID。
您可以点击资源或资源使用者页签，分别查看此共享单元内的共享交换机和使用者。
如果资源和资源使用者页签的共享状态显示为已关联时，表示共享的资源和资源使用者添加成功：
关联失败的常见原因
如果资源和资源使用者区域的共享状态显示为关联失败，则表示共享失败。共享失败的可能原因如下，请您排查后再添加要共享的交换机：
要共享的交换机使用者的账号与交换机所有者的账号相同，即交换机所有者不能将自己的交换机共享给自己。
单个VPC共享的交换机使用者的数量超过了配额（默认为50个）。
单个VPC内的单个交换机共享的交换机使用者的数量超过了配额（默认为50个）。
单个交换机使用者接收的共享交换机的数量超过了配额（默认为30个）。
在目标共享单元页面，单击右上方编辑共享单元，您可以在此共享单元内：
增加或删除共享交换机：在第一步，勾选或取消勾选交换机。
增加或删除共享交换机的使用者：在第三步，添加或删除账号UID。
检查无误后，在编辑共享单元页面的第四步，单击确定。
### API
交换机所有者查看已被共享的共享交换机及使用者：
调用[ListSharedResources](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-listsharedresources)查看共享交换机列表。
调用[ListSharedTargets](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-listsharedtargets)查看共享交换机的使用者列表。
交换机所有者在共享单元内管理共享交换机及使用者：
调用[ListResourceShareAssociations](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-listresourceshareassociations)查看共享单元内的交换机或使用者。
调用[AssociateResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-associateresourceshare)在共享单元内增加共享交换机或使用者。
调用[DisassociateResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-disassociateresourceshare)在共享单元内删除共享交换机或使用者。
## 更多信息
### 计费说明
共享 VPC 功能本身不收费。但资源所有者和使用者要为自己创建的云资源（如ECS、RDS等）付费。
### 支持的地域
| 区域 | 支持共享 VPC 的地域 |
| --- | --- |
| 亚太-中国 | 华东 1（杭州） 、 华东 2（上海） 、 华北 1（青岛） 、 华北 2（北京） 、 华北 3（张家口） 、 华北 5（呼和浩特） 、 华北 6（乌兰察布） 、 华南 1（深圳） 、 华南 2（河源） 、 华南 3（广州） 、 西南 1（成都） 、 中国香港 |
| 亚太-其他 | 日本（东京） 、 韩国（首尔） 、 新加坡 、 马来西亚（吉隆坡） 、 印度尼西亚（雅加达） 、 菲律宾（马尼拉） 、 泰国（曼谷） |
| 欧洲与美洲 | 德国（法兰克福） 、 英国（伦敦） 、 美国（硅谷） 、 美国（弗吉尼亚） |
| 中东 | 沙特（利雅得）- 合作伙伴运营 |
### 配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_sharedvpc_share_user_num_per_vpc | 单个 VPC 支持共享的交换机使用者的数量 | 50 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_sharedvpc_share_user_num_per_vswitch | 单个 VPC 内的单个交换机支持共享的交换机使用者的数量 | 50 个 |  |
| vpc_quota_sharedvpc_accept_shared_vswitch_num | 单个交换机使用者支持接收的共享交换机的数量 | 30 个 |  |
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
