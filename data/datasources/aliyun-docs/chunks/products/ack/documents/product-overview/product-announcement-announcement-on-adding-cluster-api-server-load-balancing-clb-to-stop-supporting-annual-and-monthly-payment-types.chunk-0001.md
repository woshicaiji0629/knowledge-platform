## 变更内容
在2024年12月1日完全停止支持后，在容器服务 Kubernetes 版 ACK（Container Service for Kubernetes）中新建集群时，API Server负载均衡CLB的付费类型不再支持选择包年包月。
重要
存量包年包月类型负载均衡CLB不受影响，但建议您及时转换为按量付费类型。更多信息请参见[传统型负载均衡](../../../slb/documents/product-overview/announcement-of-suspension-of-traditional-load-balancing-clb-package-year-and-month.md)[CLB](../../../slb/documents/product-overview/announcement-of-suspension-of-traditional-load-balancing-clb-package-year-and-month.md)[包年包月停售公告](../../../slb/documents/product-overview/announcement-of-suspension-of-traditional-load-balancing-clb-package-year-and-month.md)。
集群创建接口[CreateCluster - 创建集群](../serverless-kubernetes/developer-reference/api-cs-2015-12-15-createcluster-serverless.md)中描述API Server负载均衡CLB的付费类型字段将会同步下线，将会下线的参数如下：

| 字段名称 | 说明 |
| --- | --- |
| charge_type | 付费类型 |
| period | 购买时长 |
| period_unit | 付费周期 |
| auto_renew | 是否自动续费 |
| auto_renew_period | 自动付费周期 |

该文章对您有帮助吗？
反馈
