| 类别 | 配置 | 说明 |
| --- | --- | --- |
| 无 | 任务名称 | DTS 会自动生成一个任务名称，建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| 源库信息 | 选择 DMS 数据库实例 | 您可以按实际需求，选择是否使用已有实例。 如使用已有实例，下方数据库信息将自动填入，您无需重复输入。 如不使用已有实例，您需要输入下方的数据库信息。 |
| 数据库类型 | 选择 MySQL 。 |  |
| 接入方式 | 选择 公网 IP 。 |  |
| 实例地区 | 选择 Google Cloud SQL for MySQL 数据库所属地域。 说明 若选项中没有 Google Cloud SQL for MySQL 数据库所属的地域，您可以选择一个该数据库距离最近的地域。 |  |
| 域名或 IP 地址 | 填入 Google Cloud SQL for MySQL 数据库的访问地址 。 说明 您可以在 Google Cloud SQL for MySQL 数据库实例左侧单击 连接 ，在 摘要 页签的 网络 区域，查看 公共 IP 地址 。 |  |
| 端口 | 填入 Google Cloud SQL for MySQL 数据库的服务端口，默认为 3306 。 |  |
| 数据库账号 | 填入 Google Cloud SQL for MySQL 数据库账号，权限要求请参见 [数据库账号的权限要求](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-an-amazon-rds-for-mysql-instance-to-an-apsaradb-rds-for-mysql-instance#section-2g2-h0v-e69) 。 |  |
| 数据库密码 | 填入该数据库账号对应的密码。 |  |
| 目标库信息 | 选择 DMS 数据库实例 | 您可以按实际需求，选择是否使用已有实例。 如使用已有实例，下方数据库信息将自动填入，您无需重复输入。 如不使用已有实例，您需要输入下方的数据库信息。 |
| 数据库类型 | 选择 MySQL 。 |  |
| 接入方式 | 选择 云实例 。 |  |
| 实例地区 | 选择目标 RDS MySQL 实例所属地域。 |  |
| 是否跨阿里云账号 | 本场景为同一阿里云账号间的迁移，选择 不跨账号 。 |  |
| RDS 实例 ID | 选择目标 RDS MySQL 实例 ID。 |  |
| 数据库账号 | 填入目标 RDS MySQL 实例的数据库账号，权限要求请参见 [数据库账号的权限要求](https://help.aliyun.com/zh/dts/user-guide/migra
