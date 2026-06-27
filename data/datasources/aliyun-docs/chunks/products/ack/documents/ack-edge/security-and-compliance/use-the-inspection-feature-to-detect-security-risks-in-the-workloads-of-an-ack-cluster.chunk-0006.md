| 检查项 ID | 检查项 | 检查的内容及安全风险 | 修复建议 |
| --- | --- | --- | --- |
| hostNetworkSet | 禁止容器共享主机的网络命名空间 | 通过检查 Workload 的 Pod spec 中是否配置了 hostNetwork: true ，检查是否配置了共享使用主机的网络 namespace。如果配置了，存在 Pod 中容器攻击主机网络、嗅探主机网络数据的风险。 | 修改 Pod spec，删除 hostNetwork 字段。 示例： |
| hostIPCSet | 禁止容器共享主机的 IPC 命名空间 | 通过检查 Workload 的 Pod spec 中是否配置了 hostIPC: true ，检查是否配置了共享使用主机的 IPC namespace。如果配置了，存在 Pod 中容器攻击主机上进程、嗅探主机上进程数据的风险。 | 修改 Pod spec，删除 hostIPC 字段。 示例： |
| hostPIDSet | 禁止容器共享主机的 PID 命名空间 | 通过检查 Workload 的 Pod spec 中是否配置了 hostPID: true ，检查是否配置了共享使用主机的 PID namespace。如果配置了，存在 Pod 中容器攻击主机上进程、采集主机上进程数据的风险。 | 修改 Pod spec，删除 hostPID 字段。 示例： |
| hostPortSet | 禁止容器内进程监听节点主机端口 | 通过检查 Workload 的 Pod spec 中是否配置了 hostPort ，检查是否配置了把容器中监听的端口映射到主机指定端口上。如果配置了，存在挤占主机可用端口以及被非预期的请求方请求容器端口的风险。 | 修改 Pod spec，删除 hostPort 字段。 示例： |
| runAsRootAllowed | 禁止以 root 用户启动容器 | 通过检查 Workload 的 Pod spec 中是否未配置 runAsNonRoot: true ，检查是否未配置使用非 root 用户运行容器。如果未配置，存在被容器中的恶意进程入侵用户应用、入侵主机甚至入侵整个集群的风险。 | 修改 Pod spec，增加 runAsNonRoot: true 。 示例： |
| runAsPrivileged | 禁止以特权模式启动容器 | 通过检查 Workload 的 Pod spec 中是否配置了 privileged: true ，检查是否配置了允许以特权模式运行容器。如果配置了，存在被容器中的恶意进程入侵用户应用、入侵主机甚至入侵集群的风险。 | 修改 Pod spec，删除 privileged 字段。 示例： |
| privilegeEscalationA
