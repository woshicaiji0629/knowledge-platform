dpoint](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) [地址](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) 。 参数设置后，会覆盖全局配置和默认配置，该凭据请求的 Endpoint 地址为该参数值。 |
| <SECRET_STORE_NAME> | 选填，替换为对应 SecretStore 的名称，表示使用某个认证配置来导入目标 KMS 凭据。 说明 组件通过 Worker RAM 角色授权时，无需配置该参数。 |
| <SECRET_STORE_NAMESPACE> | 选填，替换为对应 SecretStore 的 Namespace。 说明 组件通过 Worker RAM 角色授权时，无需配置该参数。 |
