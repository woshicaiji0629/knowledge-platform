### 节点池基础配置

| 配置项 | 描述 |  |
| --- | --- | --- |
| 节点池名称 | 自定义节点池名称。 |  |
| 容器运行时 | 根据 Kubernetes 版本 选择 容器运行时 。 containerd （推荐）：支持所有集群版本。 docker ：支持 1.22 及以下集群版本。 |  |
| 托管节点池相关配置 | 托管节点池 | 启用托管节点池，使用 ACK 提供的 [自动化运维能力](../../ack-managed-and-ack-dedicated/user-guide/node-pool-overview.md) 。 如业务对底层节点的变更比较敏感，无法容忍节点的重启以及业务 Pod 的迁移，不推荐启用。 如需后续启用，可 [编辑节点池](../../ack-managed-and-ack-dedicated/user-guide/create-a-node-pool.md) 开启。 |
| 节点自愈 | ACK 将自动监控节点状态，并在节点发生异常时自动执行自愈任务。如勾选 当节点故障时重启节点 ，节点自愈过程中可能涉及节点排水、替盘等操作。触发条件、相关事件等，请参见 [开启节点自愈](../../ack-managed-and-ack-dedicated/user-guide/auto-repair.md) 。 |  |
| 自动升级规则 | 当有可用 kubelet 版本时，ACK 会自动升级，请参见 [升级节点池](../../ack-managed-and-ack-dedicated/user-guide/node-pool-updates.md) 。 |  |
| 自动修复安全漏洞 | [修复节点池操作系统](../../ack-managed-and-ack-dedicated/user-guide/cve-patching.md) [CVE](../../ack-managed-and-ack-dedicated/user-guide/cve-patching.md) [漏洞](../../ack-managed-and-ack-dedicated/user-guide/cve-patching.md) ，支持配置安全漏洞修复级别。 云资源及计费说明： [云安全中心](https://help.aliyun.com/zh/security-center/product-overview/billing-overview) |  |
| 集群维护窗口 | ACK 会且仅会在定义的维护窗口期内执行托管节点池的自动化运维操作。 |  |
