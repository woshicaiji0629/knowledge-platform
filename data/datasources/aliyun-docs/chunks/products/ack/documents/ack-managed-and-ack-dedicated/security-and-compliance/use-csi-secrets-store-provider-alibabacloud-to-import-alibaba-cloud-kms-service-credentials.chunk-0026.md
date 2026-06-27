### kmsEndpoint配置说明
可通过专属网关访问或共享网关访问两种方式访问KMS服务获取凭据，请参考以下要求进行Endpoint配置。关于专属网关访问和共享网关访问的更多差异，请参见[共享网关和专属网关的差异](../../../../kms/documents/key-management-service/developer-reference/classic-kms-sdkclassic-kms-sdk.md)。
KMS Endpoint地址说明

| 网关类型 | 域名类型 | Endpoint 地址 | 使用说明 |
| --- | --- | --- | --- |
| 专属网关 | KMS 私网域名 | {kms-instance-id}.cryptoservice.kms.aliyuncs.com | 要求 KMS 凭据所属实例和集群在同一 Region 及同一 VPC 中。 替换 {kms-instance-id} 为 KMS 凭据所属实例 ID。 KMS 凭据所属实例版本为 3.0 以上。 |
| 共享网关 | VPC 域名 | kms-vpc.{region}.aliyuncs.com | 要求 KMS 凭据和集群在同一 Region。 替换 {region} 为 KMS 凭据所在的 Region。 应用默认配置，使用此地址时无需配置。 |
| 共享网关 | 公网 | kms.{region}.aliyuncs.com | 替换 {region} 为 KMS 凭据所在的 Region。 集群具有公网访问能力。 |
