### 开启/关闭动态路由接收
所有路由表默认开启[动态路由条目](vpc-route-table.md)接收。若需采用纯静态路由配置，可针对路由表粒度关闭动态路由接收，按需规划业务路由表，方便用户灵活便捷地管理路由配置。
支持关闭的情况：动态路由条目来源为路由传播-类型ECR，或没有动态路由传播到VPC。没有动态路由传播到VPC时，路由表详情页面的路由条目列表>动态路由条目页签不显示动态路由条目来源。
这些情况暂不支持关闭：VPC连接到了基础版TR、VPC连接到了企业版TR且TR针对该VPC开启了[路由同步](../../cen/documents/user-guide/route-synchronization.md)、VPC关联了VPN网关且VPN网关开启了[路由自动传播](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/user-guide/configure-bgp-dynamic-routing#77c5049e07fwz)。
关闭后的影响：
VPC路由表不再接收其他网络实例传播的路由。如果路由表中已存在动态路由，将全部删除，请谨慎操作。
不允许VPC连接基础版TR；连接到此VPC的TR无法针对该VPC开启路由同步；关联此VPC的VPN网关无法开启路由自动传播。
关闭后重新开启的影响：
开启后，VPC路由表中的动态路由条目，以当前路由动态源传播过来的路由条目为准。
例如ECR的动态路由条目有4条，那么关闭此开关，VPC路由表内的动态路由会清空。如果ECR新增了2条路由条目后，重新开启了此开关，那么VPC路由表会收到6条来自ECR的动态路由条目。
控制台
前往目标路由表基本信息页面，在是否接受传播路由开关中开启/关闭动态路由接收。
警告
开启/关闭动态路由接收前，请充分评估路由条目变化带来的相关业务影响，避免导致业务受损。
API
调用[ModifyRouteTableAttributes](developer-reference/api-vpc-2016-04-28-modifyroutetableattributes.md)，修改RoutePropagationEnable参数来开启或关闭动态路由接收。
警告
开启/关闭动态路由接收前，请充分评估路由条目变化带来的相关业务影响，避免导致业务受损。
Terraform
警告
开启/关闭动态路由接收前，请充分评估路由条目变化带来的相关业务影响，避免导致业务受损。
Resources：[alicloud_route_table](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_table)variable "name" { d
