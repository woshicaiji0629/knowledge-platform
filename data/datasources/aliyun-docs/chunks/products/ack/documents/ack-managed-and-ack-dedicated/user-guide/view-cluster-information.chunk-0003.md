an-eip.md) [IP](../../../../ecs/documents/user-guide/associate-or-disassociate-an-eip.md) ，Pod 或节点访问公网时可能不使用 NAT 网关，请以实际情况为准。 安全与审计 ：集群安全与审计信息，例如开启集群审计日志等。 集群资源 ：集群所用 ROS 资源栈、日志服务 Project 等。单击相应的资源 ID 可以跳转至对应控制台。 重要 这些资源由 ACK 进行管理，请勿随意删除或自行修改，避免集群异常，影响集群内应用的正常运行。 标签分组 ：集群的资源组和标签。 |
| 连接信息 | 获取公网和内网环境下的 KubeConfig，用于配置通过 kubectl 客户端访问集群。详情请参见 [连接集群](access-clusters.md) 。 |
| 集群监控 | 对接阿里云可观测监控 Prometheus 版，对集群进行资源监控，支持快速查看负载的 CPU、内存、网络等指标的使用率，提供监控与报警能力和更合适的容器场景指标。详情请参见 [接入与配置阿里云](use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md) [Prometheus](use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md) [监控](use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md) 。 |
| 成本概览 | 启用成本洞察功能后，支持查看指定财务治理周期内，指定集群、部门、应用的成本和资源使用情况，满足多种场景的成本估算、分摊与核算的需求。详情请参见 [成本洞察](cost-analysis-overview.md) 。 |
| 集群日志 | 集群的运行日志。 |
| 集群任务 | 查看集群任务、任务状态、涉及资源、变更时间等。失败任务将提示失败信息，协助问题的排查和诊断。 |
| 运维计划 | 仅针对托管节点池。可参见 [创建和管理节点池](create-a-node-pool.md) 开启，使用其提供的自动化运维能力。 查询 ACK 自动运维任务生成的执行计划，例如 ECS 系统事件自动响应、节点池 kubelet 自动升级、CVE 漏洞自动修复等。您可以单击计划 ID，查看运维任务详细信息和事件记录。关于 ACK 提供的自动化运维能力，请参见 [自动化运维能力](node-pool-overview.md) 。 |
