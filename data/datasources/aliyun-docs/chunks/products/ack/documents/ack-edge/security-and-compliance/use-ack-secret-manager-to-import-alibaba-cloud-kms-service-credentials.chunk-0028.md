### 配置KMS服务Endpoint地址
可以通过专属网关访问或共享网关访问两种方式访问KMS服务获取凭据，请参考以下要求进行Endpoint配置。关于专属网关访问和共享网关访问的更多差异，请参见[共享网关和专属网关的差异](../../../../kms/documents/key-management-service/developer-reference/classic-kms-sdkclassic-kms-sdk.md)。
KMS Endpoint优先级规则

| 类型 | 配置字段 | 用途 | 优先级 | 说明 |
| --- | --- | --- | --- | --- |
| 凭据级配置 | ExternalSecret.spec.data.kmsEndpoint | 为需要导入的每个 KMS 凭据单独指定 Endpoint 地址。 | 最高 | 针对单个凭据优先使用该配置，会覆盖全局配置和默认配置。 |
| 全局配置 | command.kmsEndpoint （启动参数） | 用于所有 KMS 请求。 | 中 | 提供了凭据级配置以外的其他 KMS 凭据使用的 Endpoint 地址 |
| 默认配置 | 无 | 当未明确配置 Endpoint 地址时使用。 | 最低 | 默认使用的 KMS Endpoint 地址 kms-vpc.{region}.aliyuncs.com , 替换 {region} 为 KMS 凭据所在的 Region。 |

apiVersion: "alibabacloud.com/v1alpha1" kind: ExternalSecret metadata: name: esdemo spec: provider: kms data: - key: test-hangzhou # 实际Endpoint 地址：全局配置存在时使用全局配置，否则为默认配置地址：kms-vpc.{region}.aliyuncs.com name: hangzhou-vpc versionId: v1 - key: test-hangzhou # 实际Endpoint 地址：字段 kmsEndpoint 指定的 kms.cn-hangzhou.aliyuncs.com name: hangzhou-public versionId: v1 kmsEndpoint: kms.cn-hangzhou.aliyuncs.com
KMS Endpoint配置地址说明
