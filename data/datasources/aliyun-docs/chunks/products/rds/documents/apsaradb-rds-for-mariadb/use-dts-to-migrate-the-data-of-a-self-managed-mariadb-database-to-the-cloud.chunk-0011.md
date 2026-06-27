| 类别 | 配置 | 说明 |
| --- | --- | --- |
| 无 | 任务名称 | DTS 会自动生成一个任务名称，建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| 源库信息 | 选择已有连接信息 | 您可以按实际需求，选择是否使用已有数据库实例。 如使用已有实例，下方数据库信息将自动填入，您无需重复输入。 如不使用已有实例，您需要配置下方的数据库信息。 说明 您可以在 数据连接管理 页面或新版配置页面，将数据库录入 DTS。更多信息，请参见 [数据连接管理](https://help.aliyun.com/zh/dts/user-guide/database-connection-management) 。 DMS 控制台的配置项为 选择 DMS 数据库实例 ，您可以单击 新增 DMS 数据库实例 或在控制台首页将数据库录入 DMS。更多信息，请参见 [云数据库录入](https://help.aliyun.com/zh/dms/register-an-apsaradb-instance-1) 和 [他云/自建数据库录入](https://help.aliyun.com/zh/dms/register-a-database-hosted-on-a-third-party-cloud-service-or-a-self-managed-database) 。 |
| 数据库类型 | 选择 Mariadb 。 |  |
| 接入方式 | 根据源库的部署位置进行选择，本文以 ECS 自建数据库 为例介绍配置流程。 |  |
| 实例地区 | 选择源 MariaDB 数据库所属地域。 |  |
| ECS 实例 ID | 选择目标 ECS 实例 ID。 |  |
| 端口 | 填入源 MariaDB 数据库的服务端口（需开放至公网），默认为 3306 。 |  |
| 数据库账号 | 填入源 MariaDB 数据库的账号，权限要求请参见 [数据库账号的权限要求](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-the-user-created-mariadb-to-rds-mariadb#section-rd0-uc3-3i5) 。 |  |
| 数据库密码 | 填入该数据库账号对应的密码。 |  |
| 连接方式 | 选择 非加密连接 。 |  |
| 目标库信息 | 选择已有连接信息 | 您可以按实际需求，选择是否使用已有数据库实例。 如使用已有实例，下方数据库信息将自动填入，您无需重复输入。 如不使用已有实例，您需要配置下方的数据库信息。 说明 您可以在 数据连接管理 页面或新版配置页面，将数据库录入 DTS。更多信息，请参见 [数据连接管理](http
