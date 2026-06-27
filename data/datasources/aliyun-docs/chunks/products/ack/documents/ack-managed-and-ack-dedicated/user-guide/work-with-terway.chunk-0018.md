在更早创建的集群中，您可能选择了IPvlan+eBPF加速模式，您可以参照下方的说明了解其特点。
IPvlan+eBPF加速模式

| IPvlan+eBPF 特点 | 说明 |
| --- | --- |
| 适用 Terway 版本 | Terway V1.7.0 及更早版本中创建的集群。 |
| 网络架构 |  |
| 加速数据链路 | Pod 访问 Service 时，会使用 eBPF 在 Pod 网络命名空间内将 Service 地址解析为 Service 后端某个 Pod 的地址。 Pod 访问其他 Pod 时，会利用 IPvlan 虚拟网络技术，绕过双方的节点网络协议栈。 |
| 使用方法 | 在创建集群时， 网络插件 选择 Terway 后，勾选 Pod IPvlan 选项。 |
| 注意事项 | 内核版本≥4.19，推荐使用 Alibaba Cloud Linux 操作系统镜像。 尚未支持安全沙箱运行时。 网络策略（ NetworkPolicy ）使用限制： CIDR 选择器不支持 Pod 网段控制。如果需控制 Pod 访问，需要使用 Pod 标签选择器。 对 CIDR 选择器中的 except 关键字支持不佳，不建议使用 except 关键字。 使用 Egress 类型的 NetworkPolicy 会导致访问集群中 Host 网络类型的 Pod 和集群中节点的 IP 失败。 集群内部访问对外暴露的 LoadBalancer 类型 Service 对应的 SLB 时可能存在回环问题而导致网络不通。更多信息，请参见 [为什么无法访问负载均衡](../../../../slb/documents/why-am-i-unable-to-access-an-slb-instance.md) 。 IPv6 hairpin 访问不受支持。 NodePort 使用限制： 如果通过 ExternalTrafficPolicy=Local 访问服务时，访问流量可能不通，请修改为 ExternalTrafficPolicy=Cluster 。 使用 ExternalTrafficPolicy=Cluster 情况下，需要对来源地址进行 SNAT，可用端口范围在 32768-65535 之间。 eBPF 加速功能和默认的 Linux 实现有所不同，根据不同业务流量规模需要调整组件配置，请务必参考 [Datapath V2](datapath-v2-best-practices.md) [下最佳实践](datapath-v2-best-practices.md) 进行监控配置、eBPF map 上限调整。 |
