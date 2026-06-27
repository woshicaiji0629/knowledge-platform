置增大而依次降低。当无法根据优先级较高的实例规格创建出实例时，会自动选择下一优先级的实例规格来创建实例。 |
| worker_instance_charge_type | String | 是 | PrePaid | 【该字段已废弃】 Worker 节点付费类型，取值： PrePaid ：包年包月。 PostPaid ：按量付费。 默认值：按量付费。 |
| security_group_id | String | 否 | sg-bp1bdue0qc1g7k**** | 使用已有安全组创建集群时需要指定安全组 ID，和 is_enterprise_security_group 二选一，集群节点会自动加入到此安全组。 |
| is_enterprise_security_group | Boolean | 否 | true | 自动创建企业级安全组，当 security_group_id 为空的时生效。 说明 使用普通安全组时，集群内节点与 Terway Pod 数量之和不能超过 2000。因此，创建 Terway 网络类型集群时，建议使用企业安全组。 true ：创建并使用企业级安全组。 false ：不使用企业级安全组。 默认值： true 。 |
| rds_instances | rds_instances | 否 | rm-2zev748xi27xc**** | 【该字段已废弃】 RDS 实例名称。 |
| cluster_spec | String | 否 | ack.pro.small | 托管版集群类型，面向托管集群。取值： ack.pro.small ：专业托管集群，即： ACK Edge 集群 Pro 版 。 ack.standard ：标准托管集群，即 ACK Edge 集群基础版 。 默认值： ack.standard 。取值可以为空，为空时则创建边缘基础版集群。 更多信息，请参见 ACK Edge 集群 Pro 版 [介绍](../../introduction-to-professional-edge-kubernetes-clusters.md) 。 |
| resource_group_id | String | 否 | rg-acfm3mkrure**** | 集群所属资源组 ID，实现不同资源的隔离。 |
