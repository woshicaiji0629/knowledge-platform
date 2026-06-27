| 类别 | 配置 | 说明 |
| --- | --- | --- |
| 无 | 任务名称 | DTS 会自动生成一个任务名称，建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| 源库信息 | 选择 DMS 数据库实例 | 您可以按实际需求，选择是否使用已有实例。 如使用已有实例，下方数据库信息将自动填入，您无需重复输入。 如不使用已有实例，您需要配置下方的数据库信息。 说明 在 DMS 控制台，您可以单击 新增 DMS 数据库实例 录入数据库实例。更多信息，请参见 [云数据库录入](https://help.aliyun.com/zh/dms/register-an-apsaradb-instance-1) 和 [他云/自建数据库录入](https://help.aliyun.com/zh/dms/register-a-database-hosted-on-a-third-party-cloud-service-or-a-self-managed-database) 。 在 DTS 控制台，您可以在 数据连接管理 页面或新版配置页面，将数据库录入 DTS。更多信息，请参见 [数据连接管理](https://help.aliyun.com/zh/dts/user-guide/database-connection-management) 。 |
| 数据库类型 | 选择 MySQL 。 |  |
| 接入方式 | 选择 公网 IP 。 |  |
| 实例地区 | 选择 Amazon RDS MySQL 数据库所属地域。 说明 若选项中没有 Amazon RDS MySQL 数据库所属的地域，您可以选择一个该数据库距离最近的地域。 |  |
| 域名或 IP 地址 | 填入 Amazon RDS MySQL 的访问地址 。 说明 您可以在 Amazon RDS MySQL 实例的 连接和安全性 页签，获取数据库的访问地址（即 终端节点 和 端口 ）。 |  |
| 端口 | 填入 Amazon RDS MySQL 的服务端口，默认为 3306 。 |  |
| 数据库账号 | 填入 Amazon RDS MySQL 的数据库账号，权限要求请参见 [数据库账号的权限要求](migrate-mysql-from-aws-rds-to-alibaba-cloud-rds.md) 。 |  |
| 数据库密码 | 填入该数据库账号对应的密码。 |  |
| 连接方式 | 请根据实际情况选择 非加密连接 或 SSL 安全连接 。 若 Amazon RDS MySQL 未开启 SSL 加密，请选择 非加密连接 。 若 Amazon RDS MySQL 已开启 SSL 加密，请选择 SSL 安全连接 。同时，您还需要上传 CA 证书 并填写 CA 证书密
