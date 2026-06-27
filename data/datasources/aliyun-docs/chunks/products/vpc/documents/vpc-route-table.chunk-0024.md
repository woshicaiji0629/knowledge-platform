方向）的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向路由器接口（专有网络方向）的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向专线网关的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向网关型负载均衡终端节点的路由条目 | VPC | 否 | 支持 | 支持 |

场景示例
某企业在阿里云华东1（杭州）地域拥有本地IDC，并创建了VPC，该企业希望实现云上云下平稳互通且保证本地IDC中部署的服务能够与公网通信。
该企业可以将VPC和边界路由器VBR连接至ECR，创建绑定了EIP的公网NAT网关后，使用路由发布至ECR的能力，在不存在路由冲突的情况下，ECR关联的本地IDC可通过BGP学习到指向NAT网关的路由，从而实现本地IDC对公网的访问。
[静态路由发布至转发路由器](../../cen/documents/user-guide/advertise-routes-to-a-transit-router.md)[TR](../../cen/documents/user-guide/advertise-routes-to-a-transit-router.md)：静态路由发布到转发路由器后，在没有路由冲突，且TR开启路由同步的情况下，TR连接的网络实例均可以接收到该路由。
如果您的VPC同时连接了ECR和TR，那么将VPC路由发布到ECR和发布到TR这两个动作独立，互不影响。
控制台
发布静态路由条目
在目标路由条目的专有网络路由发布状态列单击发布。
只有VPC连接到TR或ECR后，控制台的路由条目才会显示专有网络路由发布状态列。
撤回已发布的静态路由条目
在目标路由条目的专有网络路由发布状态列单击撤回。
只有VPC连接到TR或ECR后，控制台的路由条目才会显示专有网络路由发布状态列。
API
针对ECR：
调用[PublishVpcRouteEntries](developer-reference/api-vpc-2016-04-28-publishvpcrouteentries.md)发布静态路由到ECR。
调用[WithdrawVpcPublishedRouteEntries](developer-reference/api-vpc-2016-04-28-withdrawvpcpublishedrouteentries.md)撤回已发布到ECR的路由。
针对TR：
调用[PublishRouteEntries](../../cen/documents/developer-reference/api-cbn-2017-09-12-publishrouteentries.md)发布静态路由到TR。
调用[WithdrawPublishedRouteEntries](../../cen/documents/developer-reference/api-cbn-2017-09-12-withdrawpublishedrouteentries.md)撤回已发布到TR的路由。
Tab 正文
