方向）的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向路由器接口（专有网络方向）的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向专线网关的路由条目 | VPC | 否 | 不支持 | 不支持 |
| 指向网关型负载均衡终端节点的路由条目 | VPC | 否 | 支持 | 支持 |

动态路由条目使用限制：
VPC路由表同一时刻仅接收单一路由动态源的动态路由。
例如，VPC关联ECR后，再连接企业版TR，在TR上针对VPC开启[路由同步](../../cen/documents/user-guide/route-synchronization.md)将会失败；创建VPN网关并[开启路由传播](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/user-guide/manage-destination-based-routes#2ca2a1f525mlq)后，VPN网关学习到的BGP路由将会自动传播到VPC的系统路由表中，此时无法将VPC关联至ECR。
如果接收的动态路由，与路由表中已有的路由条目网段重叠时，请查看[路由优先级](vpc-route-table.md)了解路由生效规则。
仅绑定交换机的路由表支持接收动态路由，绑定网关的路由表不支持动态路由。
单个路由表来自 ECR 动态传播的最大生效路由条目数量默认为 200 条。超过配额后，动态路由条目仍会接收，但状态为超限暂不生效。配额提升后，新配额将在 ECR 动态传播路由下次变化时生效，超限的路由将按照配置的先后顺序生效。
