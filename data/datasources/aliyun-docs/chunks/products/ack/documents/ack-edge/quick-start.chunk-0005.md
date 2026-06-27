| 类别 | 功能 | 描述 | 参考文档 |
| --- | --- | --- | --- |
| 边缘扩展能力 | 边缘网络自治 | 在边缘和云端网络断连状态下，您可以设置边缘网络自治，以确保边缘节点上的业务应用仍然可以持续稳定地运行，而不会被驱逐或者迁移到其他边缘节点。 | [设置边缘节点自治](user-guide/configure-node-autonomy.md) |
| 应用管理 | 在多地域节点和线下 IDC 等边缘场景中，您可以通过节点池应用集管理和 DaemonSet 升级扩展功能，增强边缘场景下的应用管理能力。 节点池应用集管理：通过 YurtAppSet，对多个工作负载（例如 Deployment）进行统一管理。 DaemonSet 升级扩展：通过配置扩展的 DaemonSet 升级模型 AdvancedRollingUpdate 和 OTA 以解决云边网络中断导致的升级阻塞以及 OTA 升级问题。 | [节点池应用集管理](user-guide/node-pool-yurtappset-management.md) [DaemonSet](user-guide/daemonset-upgrade-model.md) [升级模型](user-guide/daemonset-upgrade-model.md) |  |
| 跨地域通信 | 当云边资源不在同一个网络域时，您可以通过跨地域通信组件 Raven，实现多地域高效云边运维。 | [使用跨域运维通信组件](user-guide/using-the-cloud-side-communication-raven-component.md) [Raven](user-guide/using-the-cloud-side-communication-raven-component.md) |  |
| 离线运维 | 当您设置了边缘节点自治时，云端控制面无法对边缘业务做运维变更，在紧急情况下，您可以通过离线运维工具，对离线节点上的业务进行运维操作，例如业务回滚，资源变配，业务配置修改等。 | [边缘节点离线运维](user-guide/edge-node-offline-operation-and-maintenance-tool.md) |  |
| 云上弹性 | ECS 节点以及 ECI 和 ACS 实例弹性能力 | 当本地资源不足时， ACK Edge 集群 可以快速弹性扩容云上节点，支持基于 ECS 的云端节点池的弹性，以及基于 ECI、ACS 实例的弹性能力。 | [云端](user-guide/overview-of-node-scaling.md) [ECS](user-guide/overview-of-node-scaling.md) [节点弹性](user-guide
