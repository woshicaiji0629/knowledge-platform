n-event-center.md) 。 开启事件中心：[{"name":"ack-node-problem-detector","config":"{\"sls_project_name\":\" your_sls_project_name\"}"}]。 |
| tags | Array of [tag](../developer-reference/api-cs-2015-12-15-struct-tag-edge.md) | 否 | [{"key": "env", "value": "prod"}] | 给集群打 tag 标签： key：标签名称。 value：标签值。 |
| vpcid | String | 是 | vpc-2zeik9h3ahvv2zz95**** | 集群使用的专有网络，创建集群时必须为集群提供。 说明 vpc_id 和 vswitch_ids 只能同时为空或者同时都设置对应的值。 |
| worker_data_disks | Array of [data_disk](../developer-reference/api-cs-2015-12-15-struct-data-disk-edge.md) | 否 |  | 【该字段已废弃】 Worker 节点数据盘类型、大小等配置的组合。 |
| deletion_protection | Boolean | 否 | true | 集群删除保护，防止通过控制台或 API 误删除集群。取值： true ：启用集群删除保护，将不能通过控制台或 API 删除集群。 false ：不启用集群删除保护，则能通过控制台或 API 删除集群。 默认值： false 。 |
| node_cidr_mask | String | 否 | 25 | 节点 IP 数量，通过指定网络的 CIDR 来确定 IP 的数量，只对于 Flannel 网络类型集群生效。 默认值： 25 。 |
| worker_instance_types | Array of String | 是 | ecs.n4.large | 【该字段已废弃】 Worker 节点实例规格，至少要指定一个实例规格。更多信息，请参见 [实例规格族](../../../../ecs/documents/user-guide/overview-of-instance-families.md) 。 说明 实例规格优先级随着在数据中的位置增大而依次降低。当无法根据优先级较高的实例规格创建出实例时，会自动选择下一优先级的实例规格来创建实例。 |
| worker_instance_charge_type | String | 是 | PrePaid | 【该字段已废弃】 Worker 节点付费类型，取值： PrePaid ：包年包月。 PostPaid
