# 前缀列表-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/vpc-prefix-lists

# 前缀列表
您可以将常用IP地址段统一管理在前缀列表中，并在当前或其他账号的安全组规则、路由条目中引用。修改前缀列表后，所有引用方的配置会自动同步更新。
前缀列表常见的使用场景：
统一管理公司出口IP：某公司需要通过公网访问多台ECS，传统做法是为每台ECS的安全组规则单独添加公司出口IP。然而，该公司出口IP经常变动，每次变更都需手动更新所有ECS的安全组规则，操作繁琐且易错。改用前缀列表统一管理出口IP后，只需更新前缀列表，所有引用它的安全组规则即可自动生效，配置效率和管理便捷性显著提升。
集中维护合作伙伴IP段：若业务需和合作伙伴IP段互通，通常需要在不同的路由表重复添加路由。此时使用前缀列表统一管理合作伙伴的IP段，可避免重复配置。合作伙伴IP段发生变动时，只需编辑前缀列表，所有引用的路由表自动更新，更易扩展和维护。
## 使用限制
网关路由表和基础版转发路由器无法引用前缀列表。
前缀列表是地域级资源，仅限创建地域内使用，不可跨地域引用或共享。
一个前缀列表不能同时包含 IPv4 和 IPv6 CIDR地址块。
创建前缀列表时必须设置其最大条目数。
前缀列表被引用时，会占用引用方的配额。其中VPC路由表和ECS安全组会按照前缀列表的最大条目数进行配额占用；TR（转发路由器）路由表会按照前缀列表实际包含的条目数进行占用。例如您创建了一个最大条目数为50的前缀列表，实际包含的条目数为20。那么在VPC路由表或安全组引用时，前缀列表会占用50条路由或50条安全组规则的配额。而在TR路由表引用时，会占用20条路由配额。
在某个地域首次为某类云服务[创建网关终端节点](vpc-connection-to-cloud-service.md)时，系统会自动创建1个系统前缀列表，该前缀列表包含对应云服务的IP地址段。系统自动将其引用到VPC路由表中，下一跳指向网关终端节点，实现VPC通过网关终端节点访问特定云服务。您无法引用、修改、删除、共享该系统前缀列表，控制台显示其拥有者为系统账号。
## 管理前缀列表
### 控制台
创建前缀列表
前往专有网络控制台[VPC](https://vpc.console.aliyun.com/vpc/cn-hangzhou/prefix-lists)[前缀列表](https://vpc.console.aliyun.com/vpc/cn-hangzhou/prefix-lists)页面。先在顶部菜单栏左上处选择目标地域，再单击创建VPC前缀列表。
在创建VPC前缀列表面板中：
选择IP版本（IPv4/IPv6）。
设置最大条目数：该数值会占用VPC路由表和安全组的配额，创建后可修改。
例如，即使前缀列表实际只包含20个条目，但只要最大条目数设置为50，在VPC路由表或安全组中引用时，仍会占用50条路由或50条安全组规则的配额。
配额参考：单个VPC路由表支持的自定义路由条目数[默认为](understanding-vpc-quotas-in-alibaba-cloud.md)[200](understanding-vpc-quotas-in-alibaba-cloud.md)，单个安全组支持的规则数[默认为](../../ecs/documents/user-guide/security-faq.md)[200](../../ecs/documents/user-guide/security-faq.md)。
配置前缀列表条目，支持逐条录入、批量录入、从其他前缀列表克隆（支持跨地域克隆，但不支持从来自共享的前缀列表或系统前缀列表进行克隆）。
增加或删除条目
在目标前缀列表的基本信息的条目页签下：
增加条目：单击创建VPC前缀列表条目。
删除条目：在目标条目的操作列单击删除，或多选后单击批量删除。
查看引用前缀列表的资源
在目标前缀列表的基本信息页面，单击关联页签查看。
删除前缀列表
在目标前缀列表的操作列或详情页单击删除。
删除前，请确保前缀列表未被其他资源引用，且未被共享。
### API
调用[CreateVpcPrefixList](developer-reference/api-vpc-2016-04-28-createvpcprefixlist.md)创建前缀列表。
调用[ModifyVpcPrefixList](developer-reference/api-vpc-2016-04-28-modifyvpcprefixlist.md)增加或删除条目。
调用[GetVpcPrefixListAssociations](developer-reference/api-vpc-2016-04-28-getvpcprefixlistassociations.md)查看引用前缀列表的资源。
调用[DeleteVpcPrefixList](developer-reference/api-vpc-2016-04-28-deletevpcprefixlist.md)删除前缀列表。
删除前，请确保前缀列表未被其他资源引用，且未被共享。
### Terraform
Resource:[alicloud_vpc_prefix_list](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_prefix_list)# 指定地域 provider "alicloud" { region = "cn-hangzhou" } # 创建前缀列表 resource "alicloud_vpc_prefix_list" "example_pl" { prefix_list_name = "example_pl_name" ip_version = "IPV4" # IP版本 max_entries = 50 # 最大条目数 entrys { cidr = "10.0.1.0/24" # 条目1 } entrys { cidr = "10.0.2.0/24" # 条目2 } }
## 引用前缀列表
您可在VPC路由表、TR（转发路由器）路由表、ECS安全组引用前缀列表。一旦您修改了前缀列表中的内容，引用前缀列表的资源将自动同步更新修改，从而帮助您提升配置效率。
### VPC路由表引用
在VPC路由表中添加自定义路由条目时，您可以引用前缀列表。引用时需注意：
避免与VPC现有路由条目发生路由冲突，否则无法引用。如果引用后发生了冲突，请参考[处理引用后出现的条目冲突](vpc-prefix-lists.md)。
前缀列表的最大条目数（注意不是实际包含的条目数），会占用VPC路由表自定义路由条目数配额。您可尝试通过调低最大条目数、合并相邻IP段、清理无用条目等方式来降低配额超限风险。
控制台
前往路由表基本信息页面，在路由条目列表>自定义路由条目页签下，单击添加路由条目进行配置：
目标网段：左侧下拉框选择VPC前缀列表，右侧选择目标前缀列表，
下一跳类型：选择对应的类型及实例。
API
调用[CreateRouteEntry](developer-reference/api-vpc-2016-04-28-createrouteentry.md)，DestinationCidrBlock参数填入前缀列表的实例 ID。
TerraformResources：[alicloud_route_entry](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_entry)# 指定地域 provider "alicloud" { region = "cn-hangzhou" } # 增加1条VPC路由条目，目标网段为前缀列表 resource "alicloud_route_entry" "example" { route_table_id = "vtb-bp1pa1mwgfd6rqxfxxxxx" # VPC路由表ID destination_cidrblock = "pl-bp1fnjzxkk2m6qrwxxxxx" # 目标网段，填前缀列表ID nexthop_type = "Ecr" # 下一跳类型 nexthop_id = "ecr-assoc-stwhaft9a371nxxxxx" # 下一跳实例ID }
### TR路由表引用
您可以在企业版TR的路由表中引用前缀列表，引用后，系统将在企业版TR路由表中自动添加前缀列表中所有网段的路由。引用时需注意：
如果TR已开启路由同步功能，那么在引用前缀列表之后，系统会自动将前缀列表对应的路由条目[传播到其他网络实例](../../cen/documents/user-guide/prefix-lists.md)。
前缀列表对应的路由条目，不能和TR路由表中已有的路由条目发生冲突。请参考[路由兼容性说明](../../cen/documents/user-guide/prefix-lists.md)，判断是否会发生路由冲突（不兼容即为冲突），如有冲突，则无法引用。如果引用后发生了冲突，请参考[处理引用后出现的条目冲突](vpc-prefix-lists.md)。
前缀列表中的实际条目数，会占用TR路由表路由条目数配额。建议通过合并相邻IP段、清理无用条目等方式来降低配额超限风险。
控制台
绑定前缀
前往目标TR路由表的基本信息页面，切换到路由前缀页签，单击绑定路由前缀：
路由前缀ID：选择要引用的前缀列表。
是否为黑洞路由：
是：系统将匹配前缀列表的流量直接丢弃。
否：系统将匹配前缀列表的流量，引导至下一跳连接。
筛选前缀列表对应的路由条目
前往目标TR路由表的基本信息页面，切换到路由条目页签，通过路由前缀ID来过滤，筛选出属于通过前缀列表添加的路由条目明细。
解绑前缀
警告
解绑前缀列表后，系统将自动撤销已添加在企业版TR路由表中前缀列表相关的所有路由条目。因此解绑前缀列表前，请确保您已经迁移业务流量，否则会造成网络中断。
前往目标TR路由表的基本信息页面，切换到路由前缀页签，在目标前缀列表的操作列，单击删除。
API
绑定前缀：调用[CreateTransitRouterPrefixListAssociation](../../cen/documents/developer-reference/api-cbn-2017-09-12-createtransitrouterprefixlistassociation.md)，在企业版转发路由器路由表中引用前缀列表。
筛选前缀列表对应的路由条目：调用[ListTransitRouterPrefixListAssociation](../../cen/documents/developer-reference/api-cbn-2017-09-12-listtransitrouterprefixlistassociation.md)，在返回的结果中通过PrefixListId过滤通过前缀列表添加的路由条目。
删除前缀：调用[DeleteTransitRouterPrefixListAssociation](../../cen/documents/developer-reference/api-cbn-2017-09-12-deletetransitrouterprefixlistassociation.md)，删除企业版转发路由器路由表中已引用的前缀列表。
Terraform
Resources：[alicloud_cen_transit_router_prefix_list_association](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cen_transit_router_prefix_list_association)# 指定地域 provider "alicloud" { region = "cn-hangzhou" } # 在云企业网的转发路由器中，引用前缀列表 resource "alicloud_cen_transit_router_prefix_list_association" "example" { prefix_list_id = "pl-bp1fnjzxkk2m6qrwxxxxx" # 前缀列表ID transit_router_id = "tr-bp1czv20pflygguoxxxxx" # 转发路由器ID transit_router_table_id = "vtb-bp1v7079o4dwrkgpxxxxx" # 转发路由器路由表ID next_hop_type = "BlackHole" # 下一跳类型 next_hop = "BlackHole" # 下一跳实例ID }
### ECS安全组引用
配置安全组入方向或出方向规则时，您可以引用前缀列表。
控制台
以添加安全组入方向规则为例，前往ECS控制台目标安全组详情页面，在访问规则的入方向页签下，单击增加规则进行配置：
访问来源：左侧下拉列表选择前缀列表，右侧选择目标前缀列表。
其他配置项：请按需配置。
API
调用[AuthorizeSecurityGroup](../../ecs/documents/developer-reference/api-ecs-2014-05-26-authorizesecuritygroup.md)增加安全组入方向规则时，SourcePrefixListId参数填入前缀列表ID。
调用[AuthorizeSecurityGroupEgress](../../ecs/documents/developer-reference/api-ecs-2014-05-26-authorizesecuritygroupegress.md)增加安全组出方向规则时，DestPrefixListId参数填入前缀列表ID。
TerraformResources：[alicloud_security_group](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/security_group)、[alicloud_security_group_rule](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/security_group_rule)# 指定地域 provider "alicloud" { region = "cn-hangzhou" } # 指定安全组 resource "alicloud_security_group" "sg_example" { security_group_name = "sg_example_name" vpc_id = "vpc-bp1d00iurwfx3pcxxxxx" # VPC ID } # 创建安全组规则时，引用前缀列表 resource "alicloud_security_group_rule" "sg_rule_pl_example" { security_group_id = alicloud_security_group.sg_example.id type = "ingress" ip_protocol = "tcp" policy = "accept" port_range = "8080/8080" prefix_list_id = "pl-bp1fnjzxkk2m6qrxxxxxx" # VPC前缀列表ID }
### 处理引用后出现的条目冲突
在VPC路由表或TR路由表引用前缀列表后，若前缀列表变更导致与路由表已有条目冲突，那么最新变更不会生效。
您可在前缀列表基本信息的关联页签下，查看冲突详情：发生冲突的引用方其状态为未关联到最新版本。将鼠标悬浮停在该状态上，查看ErrorMessage获取冲突的具体条目。
您有2种方法解决冲突：
警告
操作前，请您确保要修改的路由条目不会影响业务。
修改前缀列表：在前缀列表中删除导致冲突的条目，删除后系统自动重新下发前缀列表至所有引用方。
修改路由表：在路由表中删除导致冲突的路由条目，然后手动重新下发前缀列表，直至状态由未关联到最新版本变为下发成功。
下面讲述手动重新下发前缀列表的步骤。
控制台
前往专有网络控制台[VPC](https://vpc.console.aliyun.com/vpc/cn-hangzhou/prefix-lists)[前缀列表](https://vpc.console.aliyun.com/vpc/cn-hangzhou/prefix-lists)页面。先在顶部菜单栏左上处选择目标地域，再单击目标前缀列表的实例ID。
切换到关联页签，找到目标引用方，单击操作列的重试。
API
调用[RetryVpcPrefixListAssociation](developer-reference/api-vpc-2016-04-28-retryvpcprefixlistassociation.md)重新下发前缀列表。
Terraform
在不修改前缀列表条目的情况下，Terraform暂不支持重新下发前缀列表。
## 共享前缀列表
通过共享前缀列表，不同账号可以引用相同的前缀列表来配置安全组或路由，实现对特定IP地址段的统一管理，避免重复维护相同的IP段，从而提升维护效率并减少配置错误。
下面以账号A将前缀列表共享给账号B为例进行说明，此时账号A是前缀列表所有者，账号B是前缀列表使用者。
所有者可将其前缀列表共享给任意阿里云账户，也可以仅在[资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)内共享。
共享前缀列表的权限限制
共享前缀列表后，使用者权限：
查看前缀列表及其条目，例如在控制台前缀列表页可以显示来自共享的前缀列表（“拥有者”列有提示）。
不能操作前缀列表，包括不能修改前缀列表（增删条目）、不能删除前缀列表。
在资源中可以引用该前缀列表。
所有者权限：
查看前缀列表已共享的账号。
查看引用了前缀列表的使用者的资源，只能查看ID，无法操作。
所有者不能删除已被使用者资源引用的前缀列表。
所有者更新了前缀列表后，引用该前缀列表的资源都会更新。
当所有者取消共享前缀列表后：
如果前缀列表已被使用者的资源引用：这些引用将继续正常运行，所有者也可以继续查看这些引用。
未被引用：使用者无法再查看原来共享给自己的前缀列表或其账号中的条目，也无法在其资源中引用。
### 控制台
开启共享此处仅介绍将前缀列表共享给任意账户的方式。针对资源目录方式，请参考[仅在资源目录内共享资源](https://help.aliyun.com/zh/resource-management/resource-sharing/getting-started/share-resources-with-objects-in-a-resource-directory)。
登录前缀列表所有者的账号，前往资源管理控制台的[资源共享-我的共享](https://resourcemanager.console.aliyun.com/resource-shares/cn-hangzhou/owned)页面。先在顶部菜单栏左上处，选择共享资源所在的地域，再单击创建共享单元，在打开的页面中：
第一步：输入共享单元名称，在资源面板的下拉列表中选择VPC前缀列表，然后选中需要共享的前缀列表。
第二步：系统会默认选择AliyunRSDefaultPermissionPrefixList权限。
第三步：资源使用者范围选择允许共享给任意账号，添加方式选择手动添加，使用者ID输入前缀列表使用者的[阿里云账号](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)[ID](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)，并点击添加。
第四步：检查无误后，在页面底部单击确定。
登录前缀列表使用者的账号，接受共享邀请：
前往资源管理控制台的[资源共享-共享给我](https://resourcemanager.console.aliyun.com/resource-shares/cn-hangzhou/shared)页面。
在顶部菜单栏左上处，选择共享资源所在的地域，再单击目标共享单元状态列的接受。
接受后，使用者就可以访问共享的前缀列表，且后续该共享单元新增的共享资源将默认接受共享邀请。
前往专有网络控制台VPC前缀列表页面，在顶部菜单栏选择共享前缀列表所在的地域后，您可以看到收到的前缀列表（拥有者列被标记为来自共享）。
接下来您可以参考[引用前缀列表](vpc-prefix-lists.md)，在VPC路由表、TR路由表、ECS安全组中进行引用。
管理共享前缀列表和使用者
前缀列表所有者可参考如下步骤，查看或增删共享前缀列表及其使用者。
登录前缀列表所有者的账号，前往资源管理控制台的[资源共享-我的共享](https://resourcemanager.console.aliyun.com/resource-shares/cn-hangzhou/owned)页面。在顶部菜单栏左上处，选择已共享的前缀列表所在的地域。
在我的共享页面，您可以：
查看已共享的前缀列表：单击共享的资源页签进行查看。
查看共享前缀列表的使用者：单击资源使用者页签进行查看。
单击共享单元页签，找到目标共享单元，单击共享单元ID。
您可以点击资源或资源使用者页签，分别查看此共享单元内的共享前缀列表和使用者。
如果资源和资源使用者页签的共享状态显示为已关联时，表示共享的资源和资源使用者添加成功。
关联失败的常见原因
如果资源和资源使用者区域的共享状态显示为关联失败，则表示共享失败。共享失败的可能原因如下，请您排查后再添加要共享的前缀列表：
要共享的前缀列表使用者的账号与前缀列表所有者的账号相同，即前缀列表所有者不能将自己的前缀列表共享给自己。
单个前缀列表支持共享给资源使用者的个数超过了配额（默认为10个）。
单个前缀列表使用者接收的共享前缀列表的个数超过了配额（默认为100个）。
在目标共享单元页面，单击右上方编辑共享单元，您可以在此共享单元内：
增加或删除共享前缀列表：在第一步，勾选或取消勾选前缀列表。
增加或删除共享前缀列表的使用者：在第三步，添加或删除账号UID。
检查无误后，在编辑共享单元页面的第四步，单击确定。
### API
开启共享
方式一：共享给任意账户
使用前缀列表所有者的身份凭证，调用[CreateResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-createresourceshare)创建共享单元，并确保将AllowExternalTargets参数设为True。
使用前缀列表使用者的身份凭证，先调用[ListResourceShareInvitations](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-listresourceshareinvitations)查询收到的资源邀请信息，再调用[AcceptResourceShareInvitation](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-acceptresourceshareinvitation)接受资源共享邀请。
方式二：仅在资源目录内共享
操作前，请确保前缀列表所有者和使用者已加入同一个资源目录。
使用资源目录管理账号的身份凭证，调用[EnableSharingWithResourceDirectory](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-enablesharingwithresourcedirectory)启用资源目录组织共享。
使用前缀列表所有者的身份凭证，调用[CreateResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-createresourceshare)创建共享单元，并确保将AllowExternalTargets参数设为False。
管理共享前缀列表和使用者
前缀列表所有者，查看已被共享的共享前缀列表及使用者：
调用[ListSharedResources](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-listsharedresources)查看共享前缀列表。
调用[ListSharedTargets](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-listsharedtargets)查看共享前缀列表的使用者列表。
前缀列表所有者，在共享单元内管理共享前缀列表及使用者：
调用[ListResourceShareAssociations](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-listresourceshareassociations)查看共享单元内的前缀列表或使用者。
调用[AssociateResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-associateresourceshare)在共享单元内增加共享前缀列表或使用者。
调用[DisassociateResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-disassociateresourceshare)在共享单元内删除共享前缀列表或使用者。
### Terraform
当前Terraform不支持将前缀列表共享给任意账户，仅支持在资源目录内共享，请您在操作前确保资源目录管理账号已[启用资源目录组织共享](https://help.aliyun.com/zh/resource-management/resource-sharing/user-guide/enable-resource-sharing)。Resources:[alicloud_resource_manager_resource_share](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/resource_manager_resource_share)、[alicloud_resource_manager_shared_resource](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/resource_manager_shared_resource)、[alicloud_resource_manager_shared_target](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/resource_manager_shared_target)
使用前缀列表所有者的身份凭证，开启共享：
# 指定地域 provider "alicloud" { region = "cn-hangzhou" } # 指定共享单元名称 resource "alicloud_resource_manager_resource_share" "example_unit" { resource_share_name = "example_unit_name" } # 指定共享前缀列表 resource "alicloud_resource_manager_shared_resource" "example_vsw" { resource_share_id = alicloud_resource_manager_resource_share.example_unit.id resource_id = "pl-bp18t4lsc3e4yd6xxxxx" # 要共享的前缀列表ID resource_type = "PrefixList" # 资源类型为前缀列表 } # 指定共享前缀列表的使用者 resource "alicloud_resource_manager_shared_target" "example_target" { resource_share_id = alicloud_resource_manager_resource_share.example_unit.id target_id = "101xxxxxxxxxxxxxxx" # 前缀列表使用者的UID }
## 更多信息
### 计费
前缀列表功能不收取任何费用。
### 支持的地域
| 区域 | 支持前缀列表的地域 |
| --- | --- |
| 亚太-中国 | 华东 1（杭州） 、 华东 2（上海） 、 华东 5 （南京-本地地域-关停中） 、 华北 1（青岛） 、 华北 2（北京） 、 华北 3（张家口） 、 华北 5（呼和浩特） 、 华北 6（乌兰察布） 、 华南 1（深圳） 、 华南 2（河源） 、 华南 3（广州） 、 西南 1（成都） 、 西北 2（中卫） 、 中国香港 、 华中 1（武汉-本地地域） 、 华东 6（福州-本地地域-关停中） |
| 亚太-其他 | 日本（东京） 、 韩国（首尔） 、 新加坡 、 马来西亚（吉隆坡） 、 印度尼西亚（雅加达） 、 菲律宾（马尼拉） 、 泰国（曼谷） 、 马来西亚（柔佛州） |
| 欧洲与美洲 | 德国（法兰克福） 、 英国（伦敦） 、 法国（巴黎） 、 美国（硅谷） 、 美国（弗吉尼亚） 、 墨西哥 |
| 中东 | 阿联酋（迪拜） 、 沙特（利雅得）- 合作伙伴运营 |
### 配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_prefixlist_num | 单个阿里云账号支持创建的前缀列表个数 | 10 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_prefixlist_cidr_num_per_prefixlist | 单个前缀列表支持的 CIDR 条目数 | 50 条 |  |
| vpc_quota_prefixlist_accept_shared_prefixlist_num | 单个资源使用者支持接受的共享前缀列表个数 | 100 个 |  |
| vpc_quota_prefixlist_share_user_num_per_prefixlist | 单个前缀列表支持共享给资源使用者的个数 | 10 个 |  |
关于资源共享的配额，请参见[资源共享使用限制](https://help.aliyun.com/zh/resource-management/product-overview/limits#section-0pk-5ng-g4e)。
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
