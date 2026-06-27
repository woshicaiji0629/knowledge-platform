高级选项

| 配置项 | 描述 |
| --- | --- |
| 实例元数据访问模式 | 仅支持 1.28 及以上版本的集群 配置 ECS 实例的元数据访问模式，在 ECS 实例内部通过访问元数据服务（Metadata Service）获取 ECS 实例元数据，包括实例 ID、VPC 信息、网卡信息等实例属性信息，详情请参见 [实例元数据](../../../../ecs/documents/user-guide/view-instance-metadata.md) 。 普通模式和加固模式 ：支持使用普通模式和加固模式两种方式访问实例元数据服务。 仅加固模式 ：仅支持使用加固模式访问实例元数据服务，请参见 [使用仅加固模式访问](../security-and-compliance/secure-access-to-ecs-instance-metadata.md) [ECS](../security-and-compliance/secure-access-to-ecs-instance-metadata.md) [实例元数据](../security-and-compliance/secure-access-to-ecs-instance-metadata.md) 。 |

步骤四：配置节点池
单击下一步：节点池配置，完成节点池基础选项配置和高级选项配置。
节点池基础配置

| 配置项 | 描述 |
| --- | --- |
| 节点池名称 | 自定义节点池名称。 |
| 容器运行时 | 如何选型，请参见 [containerd、安全沙箱、Docker](comparison-of-docker-containerd-and-sandboxed-container.md) [运行时的对比](comparison-of-docker-containerd-and-sandboxed-container.md) 。 containerd（推荐）：社区标准，支持 1.20 及以上版本。 安全沙箱： 提供基于轻量级虚拟化技术的强隔离环境 。使用流程及限制，详见 [创建和管理安全沙箱节点池](node-pool-management-in-sandboxed-containers.md) 。 Docker（停止支持）：仅支持 1.22 及以下版本，目前已不支持创建。 |

实例和镜像配置
