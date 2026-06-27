## 后续操作
应用部署：创建并管理工作负载，包括Deployment、StatefulSet、Job等，请参见[创建工作负载](deploying-workloads.md)。
服务发现与网络管理
[Service](service-management.md)：为一组Pod提供固定的访问入口，实现集群内访问、公网访问等。
[Ingress](ingress-management-2.md)：配置不同的转发规则，例如通过域名或者访问路径来路由到不同的Service上，从而实现负载均衡。
[服务发现](service-discovery-dns-1.md)[DNS](service-discovery-dns-1.md)：为集群内的工作负载提供域名解析服务，使得集群内部的服务可以通过服务名来互相访问，无需知道具体的IP地址。
可观测配置：实现集群日志收集和监控告警，便于集群诊断和状态观测。请参见[可观测性](observability-overview.md)了解ACK在基础设施、容器、工作负载等维度提供的可观测方案。
[存储](csi-overview-1.md)：基于CSI插件实现应用数据持久化存储、敏感和配置数据存储、存储资源动态供应等存储需求。
[弹性伸缩](auto-scaling-overview.md)配置：如业务资源需求不易预测或有周期性变化（例如Web应用、游戏服务、在线教育等），推荐启用弹性伸缩，包括工作负载伸缩（HPA、CronHPA、VPA等）和计算资源伸缩（节点自动伸缩、节点即时弹性等）。
精细化授权
如需对基础资源层（ACK依赖的云产品）和集群内部资源（Kubernetes资源对象）进行更细粒度的权限控制，ACK提供基于阿里云RAM和Kubernetes原生RBAC机制的多种权限管理方案，请参见[授权](authorization-overview.md)。
