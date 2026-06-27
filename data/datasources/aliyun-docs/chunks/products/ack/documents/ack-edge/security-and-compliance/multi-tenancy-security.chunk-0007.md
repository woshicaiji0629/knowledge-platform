## 未来方向
Kubernetes社区已经认识到软多租目前的缺点以及硬多租的挑战。多租户特别兴趣小组 (SIG) 正尝试通过几个孵化项目来解决这些问题：
Virtual Cluster提案描述了一种机制，用于为集群中的每个租户（也称为“Kubernetes on Kubernetes”）创建控制平面服务的单独实例，包括API Server、Controller Manage和Scheduler。更多信息，请参见[Virtual Cluster](https://github.com/kubernetes-sigs/cluster-api-provider-nested/tree/main/virtualcluster)。
HNC提案 (KEP) 描述了一种通过策略对象继承以及租户管理员创建子命名空间的能力在命名空间之间创建父子关系的方法。更多信息，请参见[HNC](https://github.com/kubernetes-sigs/hierarchical-namespaces)。
Multi-Tenancy Benchmarks提案提供了使用命名空间进行隔离和分段共享集群的指南，以及命令行工具Kubectl-mtb用于验证是否符合的指南。更多信息，请参见[Multi-Tenancy Benchmarks](https://github.com/kubernetes-sigs/multi-tenancy/tree/master/benchmarks)。
