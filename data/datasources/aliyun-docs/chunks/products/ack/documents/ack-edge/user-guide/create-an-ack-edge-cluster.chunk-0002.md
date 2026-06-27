| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| name | String | 是 | demo-edge-cluster | 集群名称。 命名规则：由数字、汉字、英文字符或短划线（-）组成，长度范围 1~63 个字符，且不能以短划线（-）开头。 |
| cluster_type | String | 是 | ManagedKubernetes | 集群类型。取值 ManagedKubernetes 创建边缘托管版集群。 |
| disable_rollback | Boolean | 否 | true | 【该字段已废弃】 集群创建失败是否回滚。取值： true ：当集群创建失败时，进行回滚操作。 false ：当集群创建失败时，不进行回滚操作。 默认值： false 。 |
| timeout_mins | Long | 否 | 60 | 【该字段已废弃】 集群资源栈创建超时时间，以分钟为单位，默认值 60 分钟。 |
| kubernetes_version | String | 否 | 1.30.1-aliyun.1 | 集群版本，与 Kubernetes 社区基线版本保持一致。建议选择最新版本，若不指定，默认使用最新版本。 目前您可以在 ACK 控制台创建三种最新版本的集群。您可以通过 API 创建其他 Kubernetes 版本集群。关于 ACK 支持的 Kubernetes 版本，请参见 [ACK](../../ack-managed-and-ack-dedicated/user-guide/support-for-kubernetes-versions.md) [版本发布说明](../../ack-managed-and-ack-dedicated/user-guide/support-for-kubernetes-versions.md) 。 |
| runtime | Array of [runtime](../developer-reference/api-cs-2015-12-15-struct-runtime-edge.md) | 否 | {"name": " containerd ", "version": "1.6.20"} | 容器运行时，支持 containerd 和 docker 两种运行时。 包括以下信息： name ：容器运行时名称。 version ：容器运行时版本。 |
| region_id | String | 是 | cn-beijing | 集群所在地域 ID。 |
| key_pair | String | 是 | demo-key | 【该字段已废弃】 密钥对名称，和 login_password 二选一。 |
| logi
