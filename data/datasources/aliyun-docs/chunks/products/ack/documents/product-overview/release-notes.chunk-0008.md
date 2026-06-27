## 2026年01月

| 产品 | 功能名称 | 功能描述 | 相关文档 |
| --- | --- | --- | --- |
| 容器服务 Kubernetes 版 | 支持使用 CPFS 智算版动态存储卷 | 通过动态卷机制，可为 CPFS 智算版实现自动化按需存储，免去手动管理 PV 的繁琐。该方法支持多应用并行读写，尤其适用于 AI 训练、大数据分析等场景，可高效共享代码、配置文件、计算中间结果等数据。 | [使用](../ack-managed-and-ack-dedicated/user-guide/use-cpfs-for-lingjun-dynamic-volumes.md) [CPFS](../ack-managed-and-ack-dedicated/user-guide/use-cpfs-for-lingjun-dynamic-volumes.md) [智算版动态存储卷](../ack-managed-and-ack-dedicated/user-guide/use-cpfs-for-lingjun-dynamic-volumes.md) |
| 支持将 OSS 数据按需预填充到高性能存储卷 | 在 AI 训练、数据分析等任务开始前，将存储于 OSS 的海量冷数据按需预热到高性能存储卷（如 CPFS 智算版、云盘），计算任务可直接从高性能卷中高速读取数据，任务结束后存储卷自动回收，实现计算加速与成本优化的平衡。 | [将 OSS 数据按需预填充到高性能存储卷](../ack-managed-and-ack-dedicated/user-guide/prefetch-oss-data-into-high-performance-volumes-on-demand.md) |  |
| 支持将应用调度到混合云节点池 | 混合云节点池支持将本地数据中心（IDC）的节点注册到 ACK 集群，实现云上云下资源的统一纳管与协同调度。 | [将应用调度到混合云节点池](../ack-managed-and-ack-dedicated/user-guide/scheduling-applications-to-a-hybrid-cloud-node-pool.md) |  |
| 新增 yurt-hub 组件 | yurt-hub 是为 ACK 集群混合云节点池提供自治能力的节点组件。 | [yurt-hub](yurt-hub.md) |  |
