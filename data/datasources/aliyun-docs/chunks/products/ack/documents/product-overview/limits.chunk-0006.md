## ACK托管集群

| 维度 | 基础版 | Pro 版 |
| --- | --- | --- |
| 单阿里云账号最大集群数 | 2 | 100 |
| 单集群最大节点池数 ① | 10 | 100 |
| 单集群最大节点数 | 10 | 使用 Flannel 容器网络插件：默认支持 200 个，最大支持 1000 个节点 使用 Terway 容器网络插件：默认支持 5,000 个，最大支持 15,000 个节点 |
| 单集群最大 Serverless Pod 数 | 1,000 | 50,000 重要 在 Pod 大量关联 Service 的情况下，建议保持在 20,000 个以内。 |
| 单节点最大 Pod 数 ② | 使用 Flannel 容器网络插件：256 使用 Terway 容器网络插件：单节点 Pod 限额由节点规格决定。详见 [节点](../ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) [Pod](../ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) [限额计算方法](../ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) |  |
| 配额提升方式 | 不可申请 | [到配额平台提交申请](https://quotas.console.aliyun.com/products/csk/quotas) |
