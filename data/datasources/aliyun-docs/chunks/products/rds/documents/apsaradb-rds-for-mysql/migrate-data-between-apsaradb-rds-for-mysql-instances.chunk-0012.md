| 类别 | 配置 | 说明 |
| --- | --- | --- |
| 无 | 任务名称 | DTS 会自动生成一个任务名称，建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| 源库信息 | 选择已有连接信息 | 本示例无需选择，配置下方的数据库信息即可。 |
| 数据库类型 | 选择 MySQL 。 |  |
| 接入方式 | 选择 云实例 。 |  |
| 实例地区 | 选择源 RDS MySQL 实例所属地域。 |  |
| 是否跨阿里云账号 | 本示例使用当前阿里云账号下的数据库实例，需选择 不跨账号 。 说明 如需进行跨账号迁移，请选择 跨账号 ，具体操作请参见 [配置跨阿里云账号的任务](https://help.aliyun.com/zh/dts/user-guide/synchronize-or-migrate-data-across-alibaba-cloud-accounts#task-2121003) 。 |  |
| RDS 实例 ID | 选择源 RDS MySQL 实例 ID。 说明 源和目标 RDS MySQL 实例可以不同或相同，即您可以使用 DTS 实现两个 RDS MySQL 实例间的数据迁移或同一 RDS MySQL 实例内的数据迁移。 |  |
| 数据库账号 | 填入源 RDS MySQL 实例的数据库账号，权限要求请参见 [数据库账号的权限要求](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-apsaradb-rds-for-mysql-instances#section-j8m-8s8-1so) 。 |  |
| 数据库密码 | 填入该数据库账号对应的密码。 |  |
| 连接方式 | 根据需求选择 非加密连接 或 SSL 安全连接 。如果设置为 SSL 安全连接 ，您需要提前开启 RDS MySQL 实例的 SSL 加密功能，详情请参见 [使用云端证书快速开启](configure-a-cloud-certificate-to-enable-ssl-encryption.md) [SSL](configure-a-cloud-certificate-to-enable-ssl-encryption.md) [链路加密](configure-a-cloud-certificate-to-enable-ssl-encryption.md) 。 |  |
| 目标库信息 | 选择已有连接信息 | 本示例无需选择，配置下方的数据库信息即可。 |
| 数据库类型 | 选择 MySQL 。 |  |
| 接入方式 | 选择 云实例 。 |  |
| 实例地区 | 选择目标 RDS MySQL 实例所属地域。 |  |
|
