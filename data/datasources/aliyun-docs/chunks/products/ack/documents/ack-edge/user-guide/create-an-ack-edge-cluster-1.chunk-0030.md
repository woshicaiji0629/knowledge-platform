安全组 | 为节点池指定普通安全组或企业级安全组。ACK 默认不会为安全组配置额外的访问规则。需自行管理安全组规则，避免访问异常，请参见 [配置集群安全组](../../ack-managed-and-ack-dedicated/user-guide/configure-security-group-rules-to-enforce-access-control-on-ack-clusters.md) 。 每台 ECS 实例支持加入的安全组存在上限，请确保 [安全组配额](../../../../ecs/documents/user-guide/limitations.md) 充足。 |
| RDS 白名单 | 将节点 IP 添加至 RDS 实例的白名单。 |
| 【废弃】私有池类型 | 配置项已废弃，请切换使用 资源池策略 来指定私有池 当前所选可用区和实例规格下可使用的 [私有池](../../../../ecs/documents/user-guide/private-pools.md) 资源。类型包括： 开放 ：实例将会自动匹配开放类型的私有容量池，如果没有符合条件的私有池，则使用公共池资源启动。 不使用 ：实例不会使用任何私有池容量，直接使用公共池资源启动。 指定 ：需要进一步选择私有池 ID 来指定实例只使用该私有池容量启动。如果该私有池不可用，则实例启动失败。 |
