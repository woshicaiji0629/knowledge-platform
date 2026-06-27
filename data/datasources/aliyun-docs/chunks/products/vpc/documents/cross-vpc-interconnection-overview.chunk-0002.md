ing-to-limit-bandwidth-for-inter-region-connections.md)功能，或不希望手动配置路由，请使用云企业网。
根据成本：若互连的VPC属于相同地域，推荐您使用对等连接，同地域不计费。
根据带宽：若同地域VPC互连需要大带宽，推荐您使用对等连接，同地域不限制带宽。
两者差异：

| 对比项 | VPC 对等连接 | 云企业网 |
| --- | --- | --- |
| 组网连接方式 | Full Mesh 全连接方式，VPC 两两之间建立对等连接。 | Hub-Spoke 连接方式，VPC 以网络连接方式加入转发路由器。 |
| 互连 VPC 数量 | 一个 VPC 默认支持连接 10 个同地域 VPC，20 个跨地域 VPC。 | 一个 TR（转发路由器）默认可连接 1000 个 VPC。 |
| 路由配置 | 必须手动为每个 VPC 配置路由。 | 支持通过 [路由学习](../../cen/documents/user-guide/route-learning.md) 和 [路由同步](../../cen/documents/user-guide/route-synchronization.md) 功能自动配置路由。 |
| 网络扩展性 | 弱 单个 VPC 支持的对等连接数较少，且每次新增 VPC 时都需要两两建立连接并手动配置路由。 | 强 单个 TR 支持连接大量 VPC，且新增 VPC 时直接连接到 TR 即可，不必手动配置路由。 |
| 带宽限制 | 同地域：不限制。 跨地域：默认限制 1024 Mbps。 | 同地域：请查看 [网络实例连接支持的最大带宽](../../cen/documents/product-overview/limits.md) 。 跨地域：带宽分配方式若选择按流量付费，则按 [配额](../../cen/documents/user-guide/cen-quotas.md) 约束；若选择从带宽包分配，则最大带宽为 [带宽包](https://common-buy.aliyun.com/?spm=5176.10692594.0.0.64874ffcQgbWpq&commodityCode=cbn_bwp_pre&request=%7B%22cbn_id%22%3A%22%22%7D) 的带宽值。 |
| 计费 | 同地域不收费，跨地域统一由云数据传输 CDT（Cloud DataTransfer）收取 [出方向流量传输费](https://help.aliyun.com/zh/cdt/inter-region-data-transfers) 。 | 同地域收取连接费、流量处理费；跨地域收取连接费、流量处理费和跨地域带宽费。详情： [云企业网计费说明](../../cen/documents/product-overview/billing-rules.md) 。 |
