的密码。 |  |
| 连接方式 | 请根据实际情况选择 非加密连接 或 SSL 安全连接 。 若 Amazon RDS MySQL 未开启 SSL 加密，请选择 非加密连接 。 若 Amazon RDS MySQL 已开启 SSL 加密，请选择 SSL 安全连接 。同时，您还需要上传 CA 证书 并填写 CA 证书密码 。 |  |
| 目标库信息 | 选择 DMS 数据库实例 | 您可以按实际需求，选择是否使用已有实例。 如使用已有实例，下方数据库信息将自动填入，您无需重复输入。 如不使用已有实例，您需要配置下方的数据库信息。 说明 在 DMS 控制台，您可以单击 新增 DMS 数据库实例 录入数据库实例。更多信息，请参见 [云数据库录入](https://help.aliyun.com/zh/dms/register-an-apsaradb-instance-1) 和 [他云/自建数据库录入](https://help.aliyun.com/zh/dms/register-a-database-hosted-on-a-third-party-cloud-service-or-a-self-managed-database) 。 在 DTS 控制台，您可以在 数据连接管理 页面或新版配置页面，将数据库录入 DTS。更多信息，请参见 [数据连接管理](https://help.aliyun.com/zh/dts/user-guide/database-connection-management) 。 |
| 数据库类型 | 选择 MySQL 。 |  |
| 接入方式 | 选择 云实例 。 |  |
| 实例地区 | 选择目标 RDS MySQL 实例所属地域。 |  |
| 是否跨阿里云账号 | 本场景为同一阿里云账号间的迁移，选择 不跨账号 。 |  |
| RDS 实例 ID | 选择目标 RDS MySQL 实例 ID。 |  |
| 数据库账号 | 填入目标 RDS MySQL 实例的数据库账号，权限要求请参见 [数据库账号的权限要求](migrate-mysql-from-aws-rds-to-alibaba-cloud-rds.md) 。 |  |
| 数据库密码 | 填入该数据库账号对应的密码。 |  |
| 连接方式 | 根据数据库实际情况选择 非加密连接 或 SSL 安全连接 。如果设置为 SSL 安全连接 ，您需要提前开启 RDS MySQL 实例的 SSL 加密功能，详情请参见 [使用云端证书快速开启](configure-a-cloud-certificate-to-enable-ssl-encryption.md) [SSL](configure-a-cloud-certificate-to-enable-ssl-encrypt
