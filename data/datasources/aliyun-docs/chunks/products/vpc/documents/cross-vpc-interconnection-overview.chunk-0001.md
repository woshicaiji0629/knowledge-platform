## 选型
如何选择：
根据规模：若需互连2-3个VPC，推荐使用VPC对等连接；若需互连超过3个VPC，推荐使用云企业网。
根据功能：若需要[云上组播](../../cen/documents/user-guide/multicast-overview.md)、[服务链（Service Chaining）](../../cen/documents/use-cases/use-an-enterprise-edition-transit-router-to-enable-and-secure-network-communication.md)、[跨地域](../../cen/documents/user-guide/use-traffic-scheduling-to-limit-bandwidth-for-inter-region-connections.md)[Qos](../../cen/documents/user-guide/use-traffic-scheduling-to-limit-bandwidth-for-inter-region-connections.md)功能，或不希望手动配置路由，请使用云企业网。
根据成本：若互连的VPC属于相同地域，推荐您使用对等连接，同地域不计费。
根据带宽：若同地域VPC互连需要大带宽，推荐您使用对等连接，同地域不限制带宽。
两者差异：
