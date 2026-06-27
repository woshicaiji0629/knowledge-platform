享ENI或独占ENI模式，在创建集群时不再支持勾选。
节点上的主弹性网卡被分配给节点OS，其余弹性网卡会被Terway托管用于配置Pod网络，因此请勿手动配置这些弹性网卡。如果您需要自行管理部分弹性网卡，请参见[为弹性网卡（ENI）配置白名单](configure-a-whitelist-for-an-eni.md)。

| 对比项 | 共享 ENI 模式 | 独占 ENI 模式 |  |
| --- | --- | --- | --- |
| Pod IP 地址管理 | ENI 分配方式 | 多个 Pod 共享一个 ENI。 | 每个 Pod 在其节点上独占一个 ENI。 |
| Pod 部署密度 | Pod 部署密度较高。单个节点可支持数百个 Pod。 | Pod 部署密度较低。常用规格的节点只支持个位数的 Pod。 |  |
| 网络架构 |  |  |  |
| 数据链路 | Pod 访问其他 Pod，或作为 Service 后端被访问时，流量都会经过节点的网络协议栈。 | Pod 访问 Service 时，流量仍旧会经过节点操作系统的协议栈。但当 Pod 访问其他 Pod，或作为 Service 后端被访问时，会直接使用挂载的 ENI 绕过节点网络协议栈，以此获得更高的性能。 |  |
| 适用场景 | 常规的 Kubernetes 使用场景。 | 这种模式中网络性能更接近于传统虚拟机，适合对网络性能有较高要求的场景，比如需要高网络吞吐量或低延迟的应用。 |  |
| 网络加速 | 支持 DataPathv2 网络加速，具体信息请参见 [网络加速](work-with-terway.md) 。 | 不支持网络加速，但 Pod 独占 ENI 资源，已经提供了极佳的网络性能。 |  |
| NetworkPolicy 支持 | 支持 Kubernetes 原生的 NetworkPolicy ，提供了基于策略的访问控制能力，更多信息请参见 [NetworkPolicy](work-with-terway.md) [支持](work-with-terway.md) 。 | 不支持 NetworkPolicy 。 |  |
| 节点维度网络配置 | 支持。请参见 [节点维度的网络配置](configure-network-settings-for-individual-nodes-in-a-terway-cluster.md) 。 | 支持。请参见 [节点维度的网络配置](configure-network-settings-for-individual-nodes-in-a-terway-cluster.md) 。 |  |
| 访问控制 | 开启 Trunk ENI 配置后，支持为 Pod 配置固定 IP、独立的安全组和虚拟交换机，具体信息请参见 [为](work-with-terway.md) [Pod](work-with-terway.md) [配置固定](work-with-terway.md) [IP、独立虚拟交换机与安全组](work-with-terway.md) 。 | 支持为 Pod 配置固定 IP、独立的安全组和虚拟交换机。 |  |
