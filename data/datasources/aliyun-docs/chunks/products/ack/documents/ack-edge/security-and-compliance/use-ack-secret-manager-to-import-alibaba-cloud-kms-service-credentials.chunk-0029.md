# 实际Endpoint 地址：字段 kmsEndpoint 指定的 kms.cn-hangzhou.aliyuncs.com name: hangzhou-public versionId: v1 kmsEndpoint: kms.cn-hangzhou.aliyuncs.com
KMS Endpoint配置地址说明

| 网关类型 | 域名类型 | Endpoint 地址 | 使用说明 |
| --- | --- | --- | --- |
| 专属网关 | KMS 私网域名 | {kms-instance-id}.cryptoservice.kms.aliyuncs.com | 要求 KMS 凭据所属实例和集群在同一 Region 及同一 VPC 中。 替换 {kms-instance-id} 为 KMS 凭据所属实例 ID。 KMS 凭据所属实例版本为 3.0 以上。 |
| 共享网关 | VPC 域名 | kms-vpc.{region}.aliyuncs.com | 要求 KMS 凭据和集群在同一 Region。 替换 {region} 为 KMS 凭据所在的 Region。 应用默认配置，使用此地址时无需配置。 |
| 共享网关 | 公网 | kms.{region}.aliyuncs.com | 替换 {region} 为 KMS 凭据所在的 Region。 集群具有公网访问能力。 |
