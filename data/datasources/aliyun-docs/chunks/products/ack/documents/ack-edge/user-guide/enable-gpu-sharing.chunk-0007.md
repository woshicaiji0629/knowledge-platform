## 云端节点池
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。
在节点池页面，单击创建节点池。参见[创建和管理节点池](../../ack-managed-and-ack-dedicated/user-guide/create-a-node-pool.md)完成相关配置。
在创建节点池页面，设置创建节点池的配置项，然后单击确认配置。重要配置项及其说明如下：

| 配置项 | 说明 |
| --- | --- |
| 期望节点数 | 设置节点池初始节点数量。如无需创建节点，可以填写为 0。 |
| 节点标签 | 标签的值需根据您的业务需求添加。关于节点标签的详细说明，请参见 [开启调度功能](../../ack-managed-and-ack-dedicated/user-guide/enable-scheduling.md) 。 下文以标签值 cgpu 为例，该值表示节点开启共享 GPU 调度能力，每个 Pod 仅需申请 GPU 显存资源，多个 Pod 在一张卡上实行显存隔离和算力共享。 单击 节点标签 的 ，设置 键 为 ack.node.gpu.schedule ， 值 为 cgpu 。 重要 关于 cGPU 隔离功能注意事项，请参见 [cGPU FAQ](../../ack-managed-and-ack-dedicated/user-guide/usage-notes-for-memory-isolation-capability-of-cgpu.md) 。 添加共享 GPU 调度标签后，请勿通过 kubectl label nodes 命令切换节点 GPU 调度属性标签值或使用控制台 节点 页面的标签管理功能更改节点标签，以避免引发潜在的问题，请参见 [开启调度功能](../../ack-managed-and-ack-dedicated/user-guide/enable-scheduling.md) 。推荐您 [开启调度功能](../../ack-managed-and-ack-dedicated/user-guide/enable-scheduling.md) 。 |
