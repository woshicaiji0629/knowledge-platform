| 高危操作 | 影响 | 恢复方案 |
| --- | --- | --- |
| 修改内核参数 net.ipv4.ip_forward=0 。 | 网络不通。 | 修改内核参数为 net.ipv4.ip_forward=1 。 |
| 修改内核参数： net.ipv4.conf.all.rp_filter = 1|2 net.ipv4.conf.[ethX].rp_filter = 1|2 说明 ethX 代表所有以 eth 开头的网卡。 | 网络不通。 | 修改内核参数为： net.ipv4.conf.all.rp_filter = 0 net.ipv4.conf.[ethX].rp_filter = 0 |
| 修改内核参数 net.ipv4.tcp_tw_reuse = 1 。 | 导致 Pod 健康检查异常。 | 修改内核参数为 net.ipv4.tcp_tw_reuse = 0 。 |
| 修改内核参数 net.ipv4.tcp_tw_recycle = 1 。 | 导致 NAT 异常。 | 修改内核参数 net.ipv4.tcp_tw_recycle = 0 。 |
| 修改内核参数 net.ipv4.ip_local_port_range 。 | 导致网络偶发不通。 | 修改内核参数到默认值 net.ipv4.ip_local_port_range="32768 60999" 。 |
| 安装防火墙软件，例如 Firewalld 或者 ufw 等。 | 导致容器网络不通。 | 卸载防火墙软件并重启节点。 |
| 节点安全组配置未放通容器 CIDR 的 53 端口 UDP。 | 集群内 DNS 无法正常工作。 | 按照官网推荐配置放通安全组。 |
| 修改或者删除 ACK 添加的 SLB 的标签。 | 导致 SLB 异常。 | 恢复 SLB 的标签。 |
| 通过负载均衡控制台修改 ACK 管理的 SLB 的配置，包括 SLB、监听及虚拟服务器组。 | 导致 SLB 异常。 | 恢复 SLB 的配置。 |
| 移除 Service 中复用已有 SLB 的 Annotation，即 service.beta.kubernetes.io/alibaba-cloud-loadbalancer-id: ${YOUR_LB_ID} 。 | 导致 SLB 异常。 | 在 Service 中添加复用已有 SLB 的 Annotation。 说明 复用已有 SLB 的 Service 无法直接修改为使用自动创建 SLB 的 Service。您需要重新创建 Service。 |
| 通过负载均衡控制台删除 ACK 创建的 SLB。 | 可能导致集群网络异常。 | 通过删除 Service 的方式删除 SLB。删除 Service 请参见 [删除](../ack
