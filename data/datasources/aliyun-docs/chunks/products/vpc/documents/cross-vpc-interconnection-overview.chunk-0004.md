### 连通多个VPC
使用对等连接连通3个以上的VPC时，因为需要在每个VPC之间两两建立连接并手动配置路由，操作较为繁琐。
此时推荐使用[云企业网](../../cen/documents/getting-started/use-enterprise-edition-transit-routers-to-connect-vpcs-across-regions-and-accounts.md)，只需将每个VPC连接到地域内的TR，即可实现网络互通。
