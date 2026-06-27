### 容器发现原理
LoongCollector容器若要采集其他容器的日志，必须发现和确定哪些容器正在运行，这个过程称为容器发现。
在容器发现阶段，LoongCollector容器不与Kubernetes集群的[kube-apiserver](https://kubernetes.io/zh-cn/docs/reference/command-line-tools-reference/kube-apiserver/)进行通信，而是直接和节点上的容器运行时守护进程（Container Runtime Daemon）进行通信，从而获取当前节点上的所有容器信息，避免容器发现对集群kube-apiserver产生压力。
LoongCollector支持通过访问位于宿主机上容器运行时（Docker Engine/ContainerD）的 sock 获取容器的上下文信息，支持Namespace名称、Pod名称、Pod标签、容器环境变量等条件指定或排除采集相应容器的日志。
