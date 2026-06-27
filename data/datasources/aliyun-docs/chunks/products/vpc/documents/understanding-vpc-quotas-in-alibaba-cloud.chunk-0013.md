### IP地址管理（IPAM）使用限制与配额

| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| ipam_quota_per_region | 每个用户在每个地域支持创建的 IPAM 数量 | 1 个 | 无法提升 |
| ipam_scope_quota_per_ipam | 每个 IPAM 支持创建的 IPAM 作用范围数量 | 5 个 |  |
| ipam_pool_quota_depth | 每个地址池最大深度 | 10 |  |
| ipam_cidr_quota_per_ipam_pool | 每个地址池中允许预置的 CIDR 的数量 | 50 个 |  |
| ipam_sub_pool_quota_per_ipam_pool | 每个地址池允许创建的子地址池的数量 | 50 个 |  |
| ipam_pool_quota_per_scope | 每个 IPAM 私有范围支持创建的地址池的数量 | 500 个 |  |
| custom_ipam_resource_discovery_quota_per_region | 单地域单账号允许创建的自定义资源发现数量 | 1 个 |  |
| resource_share_quota_per_ipam_resource_discovery | 每个资源发现支持创建的共享资源数量 | 100 个 |  |
| shared_ipam_resource_discovery_quota_per_user | 每个用户允许拥有的共享资源发现的数量 | 100 个 |  |
| resource_share_quota_per_ipam_pool | 每个 IPAM 地址池允许创建的共享资源数量 | 100 个 |  |
| shared_ipam_pool_quota_per_user | 每个用户允许拥有的共享地址池的数量 | 100 个 |  |
| ipam_public_ipv6_top_pool_quota_per_region_isp | 每个用户在每个地域支持创建的每种 ISP 类型的公网 IPv6 IPAM 顶级地址池数量 | 1 个 |  |
| ipam_cidr_quota_per_public_ipv6_top_pool | 每个用户在每个地域支持为公网 IPv6 IPAM 顶级地址池预置的 CIDR 数量 | 1 个 |  |
