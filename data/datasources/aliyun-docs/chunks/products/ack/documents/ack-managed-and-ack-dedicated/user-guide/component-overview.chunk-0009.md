w/terway.md) | 可选组件 | 阿里云开源的 Terway CNI 插件支持 eBPF 网络加速和 Kubernetes 标准的 NetworkPolicy，用于定义容器间的访问策略。使用 Terway 可以实现 Kubernetes 集群内部的网络互通。创建集群时，选择 Terway 网络插件会默认安装该组件。 |
| [Flannel](../../product-overview/flannel.md) | 可选组件 | 一种容器网络接口 CNI（Container Network Interface）插件，在阿里云上使用的 Flannel 网络模式采用阿里云 VPC 模式。 创建集群时，如果选择 Flannel 网络插件实现集群内部网络互通的话，默认安装该组件。 |
| [Nginx Ingress Controller](../../product-overview/nginx-ingress-controller.md) | 可选组件 | Nginx Ingress Controller 解析 Ingress 的转发规则。Ingress Controller 收到请求，匹配 Ingress 转发规则转发到后端 Service。 |
| [Poseidon](../../product-overview/poseidon.md) | 可选组件 | ACK 自研的容器 NetworkPolicy 插件。支持 Kubernetes 标准的 NetworkPolicy 功能。 针对 ACK Serverless 集群 以及在 ACK 集群中使用 ECI 实例的场景，如需使用 NetworkPolicy 功能，则需安装 Poseidon 组件。 针对 ACK 集群的其他场景，如需使用 NetworkPolicy 功能，则需安装 Terway 组件。 |
| [Sidecar Acceleration using eBPF](../../product-overview/sidecar-acceleration-using-ebpf.md) | 可选组件 | 使用 Sidecar 加速来减少阿里云服务网格中的网络延迟。 |
| [Gateway with Inference Extension](../../product-overview/ack-gateway-with-inference-extension.md) | 可选组件 | 基于 Envoy Gateway 开源项目构建，支持 Kubernetes 四层/七层路由服务，并提供面向 AI 大语言模型（LLM）推理场景的智能负载均衡能力。 |
