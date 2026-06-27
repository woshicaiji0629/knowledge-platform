不添加任何注解。 |
| taints | 污点（Taints） | 表示接入时给节点加上的污点。 | [] |
| nodeIface | 无 | 指定主机网卡，该参数有两个作用： kubelet 从指定的网卡获取节点 IP 信息。 设置容器网络插件 flannel 使用的网卡。 | "" ：如果设为空，kubelet 将按如下顺序获取节点 IP。 在 /etc/hosts 中寻找与主机名同名的记录。 默认路由所在的网络接口的 IP 地址。 flannel 将使用节点默认路由所在的网卡。 |
| runtimeRootDir | 运行时工作目录 | 指定运行时的工作目录，该配置在 manageRuntime 为 true 时才会生效。 | "" ：默认值。 当运行时为 Docker 时，默认路径为 /var/lib/docker 。 当运行时为 Containerd 时，默认路径为 /var/lib/containerd 。 |
| imageRepoType | 组件下载自 | 指定节点上系统组件镜像的下载来源。 | "" ：默认值，表示专线节点池的节点从内网下载镜像，普通节点池的节点从公网下载镜像。 public ：表示从公网下载镜像。 private ：表示从内网下载镜像（节点已接入专线节点池）。 |
| selfHostNtpServer | 自动完成时间同步 | 是否手动完成时间同步。 | false ：默认值，表示由 edgeadm 自动完成时间同步。 true ：表示不需要自动时间同步，已经手动完成时间同步。 |
| flannelIface | 节点网络接口 | flannel 使用的网卡名（不推荐使用，可以使用 nodeIface 参数代替）。 | "" ：默认值，flannel 使用节点默认路由所使用的网卡。 |
| enableIptables | 无 | edgehub 是否开启 iptables 优化（不推荐使用，1.22 后已废弃）。 | false ：表示不启用 iptables。 |
