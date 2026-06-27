| 参数 | 与控制台对应的参数 | 参数说明 | 描述 |
| --- | --- | --- | --- |
| quiet | 启用静默模式 | 是否启用静默模式。在节点接入执行过程中，某些步骤可能需要您介入做出判断，例如是否需要将节点上已存在的运行时重新安装。 | true ：默认值，假设所有的问题回答自动回复 yes ，自动推进流程。 false ：节点接入过程中，可能需暂停以获取您的确认，节点接入过程可能中断。 |
| manageRuntime | 无 | 是否由 edgeadm 检测并安装运行时。 | true ：默认值，检测并安装运行时。 false ：不安装运行时，需要用户在节点上提前安装好运行时。 |
| nodeNameOverride | 无 | 设置节点名。 | "" ：默认值，表示使用主机名。 "XXX" ：表示指定节点名为 XXX。 "*" ：表示随机生成 6 位字符串。 "*.XXX" ：表示随机生成 6 位字符串+XXX 后缀。 |
| allowedClusterAddons | 无 | 需要安装的组件列表。普通节点需要配置为["kube-proxy","flannel","coredns"]。 | ["kube-proxy","flannel","coredns"] ：默认值。 |
| gpuVersion | 无 | 表示要接入的节点是否为 GPU 节点，默认为空。 当前支持的 GPU 版本，请参见 [GPU](add-a-gpu-node.md) [型号](add-a-gpu-node.md) 。 | "" ：默认值，表示不作为 GPU 节点接入。 ACK Edge 集群 从 1.26 版本开始，接入 Nvidia GPU 时，无需配置 gpuVersion 参数直接接入，由接入工具自动检查 GPU 型号并安装相关组件。 |
| labels | 节点标签（Labels） | 表示接入时节点要加的标签。节点池支持给节点池内所有节点添加标签的功能。如果该 label 与节点池上的 label key 名称冲突，节点池上定义的 label 优先级更高。 | {} ：表示不添加任何标签。 |
| annotations | 注释 | 表示接入时给节点加的注解。如果该 annotations 与节点池上的 annotations 名称冲突，节点池上定义的 annotations 优先级更高。 | {} ：表示不添加任何注解。 |
| taints | 污点（Taints） | 表示接入时给节点加上的污点。 | [] |
| nodeIface | 无 | 指定主机网卡，该参数有两个作用： kubelet 从指定的网卡获取节点 IP 信息。 设置容器网络插件 flannel 使用的网卡。 | "" ：如果设为空，kubele
