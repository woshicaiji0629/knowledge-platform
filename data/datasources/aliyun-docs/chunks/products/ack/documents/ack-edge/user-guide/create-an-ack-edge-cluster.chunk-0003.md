时名称。 version ：容器运行时版本。 |
| region_id | String | 是 | cn-beijing | 集群所在地域 ID。 |
| key_pair | String | 是 | demo-key | 【该字段已废弃】 密钥对名称，和 login_password 二选一。 |
| login_password | String | 是 | HelloWorld123 | 【该字段已废弃】 SSH 登录密码，和 key_pair 二选一。密码规则为 8~30 个字符，且至少同时包含三项（大小写字母、数字和特殊符号）。 |
| num_of_nodes | Long | 是 | 1 | 【该字段已废弃】 Worker 节点数。范围是[0,100]。 |
| profile | String | 是 | Edge | ACK Edge 集群 标识，默认取值：Edge。 |
| logging_type | String | 否 | SLS | 集群开启日志服务，只针对 ACK Serverless 集群 生效，且取值必须是 SLS 。 |
| snat_entry | Boolean | 否 | true | 是否为网络配置 SNAT： 当已有 VPC 能访问公网环境时，设置为 false 。 当已有 VPC 无法访问公网环境时： 设置为 true ，表示配置 SNAT，此时可以访问公网环境。 设置为 false ，表示不配置 SNAT，此时无法访问公网环境。 如果您的应用需要访问公网，建议配置为 true 。 默认值： false 。 |
| vswitch_ids | Array of String | 是 | vsw-2ze48rkq464rsdts1**** | 交换机 ID。List 长度范围为[1,3]。 |
| worker_system_disk_category | String | 是 | cloud_efficiency | 【该字段已废弃】 Worker 节点系统盘类型，取值： cloud_efficiency ：高效云盘。 cloud_ssd ：SSD 云盘。 默认值： cloud_ssd 。 |
| worker_system_disk_size | Long | 是 | 100 | 【该字段已废弃】 Worker 节点系统盘大小，单位为 GiB。 取值范围：[40,500]。 该参数的取值必须大于或者等于 max{40, ImageSize}。 默认值： 120 。 |
| container_cidr | String | 否 | 172.20.0.0 | Pod 网络地址段，不能和 VPC 网段冲突。当选择系统自动创建 VPC 时，默认使用 172.16.0.0/16 网段。 重要 当创建 Flann
