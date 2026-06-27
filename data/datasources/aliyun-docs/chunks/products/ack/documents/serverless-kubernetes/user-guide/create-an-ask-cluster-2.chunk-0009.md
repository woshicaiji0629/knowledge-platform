### 高级配置

| 配置项 | 描述 |
| --- | --- |
| 集群删除保护 | 推荐开启，防止通过控制台或 OpenAPI 误删除集群。 |
| 资源组 | 将集群归属于选择的 [资源组](../../../../ecs/documents/user-guide/resource-groups.md) ，便于权限管理和成本分摊。 一个资源只能归属于一个资源组。 |
| 标签 | 为集群绑定键值对 [标签](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview) ，作为云资源的标识。 |
| 集群本地域名 | 集群内 Service 使用的顶级域名（标准后缀）。默认为 cluster.local ，也支持自定义域名。自定义本地域名时，请参见 [配置集群本地域名（ClusterDomain）有哪些注意事项？](../../ack-managed-and-ack-dedicated/user-guide/faq-about-container-networks.md) 。 例如，名为 my-service 的 Service 位于 default 命名空间中，其 DNS 域名为 my-service.default.svc.cluster.local 。 |
| 时区 | 集群使用的 [时区](../../product-overview/supported-time-zones.md) 。默认为浏览器配置的时区。 |
