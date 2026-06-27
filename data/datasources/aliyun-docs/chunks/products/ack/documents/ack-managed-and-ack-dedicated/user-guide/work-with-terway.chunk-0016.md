| DataPathv2 特点 | 说明 |
| --- | --- |
| 适用 Terway 版本 | Terway V1.8.0 及后续版本中创建的集群。 |
| 网络架构 |  |
| 加速数据链路 | Pod 访问 Service 时，会使用 eBPF 将 Service 地址解析为 Service 后端某个 Pod 的地址。 Pod 访问不同节点的 Pod 时，会使用 eBPF 绕过双方的节点网络协议栈。 Pod 访问同节点的 Pod 时，不但可以绕过节点协议栈，而且访问流量无需离开节点，直接在节点内部完成转发。 |
| 性能优化 | 简化了 Pod 的网络在宿主机上的转发流程，让 Pod 的网络性能几乎与宿主机的性能无异，延迟相对常规模式降低了 30%。 Service 的网络采用 eBPF 替换原有的 kube-proxy 模式，绕过节点上的 iptables 或者 IPVS 转发，请求延迟大幅降低。网络性能在大规模集群中受到的影响更小，扩展性更优。 Pod 的网络策略（ NetworkPolicy ）也采用 eBPF 替换掉原有的 iptables 的实现，不需要在宿主机上产生大量的 iptables 规则，降低网络策略对网络性能的影响。 |
| 使用方法 | 在创建集群时， 网络插件 选择 Terway 后，勾选 DataPath V2 选项。 |
| 注意事项 | 内核版本≥5.10，推荐使用 Alibaba Cloud Linux 操作系统镜像。 尚未支持安全沙箱运行时。 网络策略（ NetworkPolicy ）使用限制： CIDR 选择器不支持 Pod 网段控制。如果需控制 Pod 访问，需要使用 Pod 标签选择器。 对 CIDR 选择器中的 except 关键字支持不佳，不建议使用 except 关键字。 使用 Egress 类型的 NetworkPolicy 会导致访问集群中 Host 网络类型的 Pod 和集群中节点的 IP 失败。 集群内部访问对外暴露的 LoadBalancer 类型 Service 对应的 SLB 时可能存在回环问题而导致网络不通。更多信息，请参见 [为什么无法访问负载均衡](../../../../slb/documents/why-am-i-unable-to-access-an-slb-instance.md) 。 IPv6 hairpin 访问不受支持。 NodePort 使用限制： 如果通过 ExternalTrafficPolicy=Local 访问服务时，访问流量可能不通，请修改为 ExternalTrafficPolicy=Cluster 。 使用 ExternalTrafficPolicy=Cluster 情况下，需要对来源地址进行 SNAT，可用端口范围在 32768-65535
