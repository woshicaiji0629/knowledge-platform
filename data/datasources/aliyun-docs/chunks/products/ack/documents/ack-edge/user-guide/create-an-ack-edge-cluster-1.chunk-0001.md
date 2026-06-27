## 使用限制

| 限制项 | 说明 | 配额申请链接/相关文档 |  |
| --- | --- | --- | --- |
| 费用 | 用户账户至少需要有 100 元的余额并通过实名认证，否则无法创建按量付费的 ECS 实例和负载均衡。 | [配额与限制](../../product-overview/limits.md) |  |
| 网络 | ACK 集群仅支持专有网络 VPC。 | [什么是专有网络](../../../../vpc/documents/what-is-vpc.md) [VPC](../../../../vpc/documents/what-is-vpc.md) |  |
| 云资源 | ECS 实例 | 支持按量付费、包年包月和抢占式实例三种付费类型。实例创建后，您可以通过 ECS 管理控制台将按量付费转预付费。 | [按量付费转包年包月](../../../../ecs/documents/change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md) |
| VPC 路由条目 | 每个账户初始默认状况下 VPC 路由条目不超过 200 条，当 ACK 集群的网络模式是 Flannel 时，集群的路由条目最大不能超过 200 个（网络模式是 Terway 则不受该影响）。如集群需要更多路由条目数，您需要对目标 VPC 申请提高配额 。 | [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas) |  |
| 安全组 | 每个账号默认最多可以创建 100 个安全组。 | [安全组](../../../../ecs/documents/user-guide/limitations.md) |  |
| 负载均衡实例 | 每个账号默认最多可以创建 60 个按量付费的负载均衡实例。 | [配额中心](https://quotas.console.aliyun.com/products/slb/quotas) |  |
| EIP | 每个账号默认最多可以创建 20 个 EIP。 | [配额中心](https://quotas.console.aliyun.com/products/eip/quotas) |  |
