## 使用限制
您可以在1.28及以上版本的ACK Edge集群中使用虚拟节点，使用前，请先了解其使用限制。
不支持DaemonSet型工作负载。您可以通过将DaemonSet重新配置为Pod的Sidecar容器来运行。
不支持在Podmanifest中指定HostPath和HostNetwork。
不支持Privileged特权容器。您可以使用Security Context为Pod添加Capability。
说明
特权容器功能正在内测中。如需体验，请提交工单申请。
不支持NodePort类型的Service，不支持配置Session Affinity。
不支持深圳金融云，不支持政务云。
