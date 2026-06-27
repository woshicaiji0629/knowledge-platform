和缩容触发时延两个条件，弹性组件则会正常执行缩容。例如，当静默时间为 10 分钟，缩容触发时延为 5 分钟时，弹性组件在最近一次扩容后的 10 分钟内不会缩容节点，但会在静默的 10 分钟内判断节点是否符合缩容条件。等待静默时间结束，节点达到缩容阈值且时间超过缩容触发时延规定的 5 分钟时，弹性组件会继续执行缩容。 |

查看高级配置的配置项说明

| 配置项 | 说明 |
| --- | --- |
| Pod 终止超时时间 | 缩容节点时等待节点上 Pod 终止的最长时间。单位：秒。 若超时后 Pod 仍未排水成功，本次缩容过程中 Pod 所在节点将不会被释放。 |
| Pod 最小副本数 | 为由 ReplicationController 或 ReplicaSet 管理的应用设置一个缩容保护阈值。当这类应用的当前实际副本数小于此值时，运行其 Pod 的节点将不会被缩容。 参数仅对由 ReplicationController 或 ReplicaSet 管理的 Pod 生效，对于 StatefulSet 、 DaemonSet 等其他控制器管理的 Pod 不生效。 |
| 开启 DaemonSet Pod 排水 | 开启 DaemonSet Pod 排水后，节点缩容时会驱逐节点上的 DaemonSet Pod。 |
| 跳过有 kube-system 命名空间下 Pod 所在节点 | 开启后，当集群执行节点自动缩容操作时，可以忽略运行在 kube-system 命名空间下的 Pod 所在的节点，确保这些节点不受缩容的影响。 说明 此功能对 DaemonSet Pod 和 Mirror Pod 不生效。 |
