| 类别 | 配置 | 说明 |
| --- | --- | --- |
| 无 | 任务名称 | DTS 会自动生成一个任务名称，建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| 源库信息 | 数据库类型 | 选择 Oracle 。 |
| 接入方式 | 根据源库的部署位置进行选择，本文以 有公网 IP 的自建数据库 为例介绍配置流程。 说明 当自建数据库为其他实例类型时，您还需要执行相应的准备工作，详情请参见 [准备工作概览](https://help.aliyun.com/zh/dts/user-guide/preparation-overview#concept-2364477) 。 |  |
| 实例地区 | 选择源 Oracle 数据库所属地域。 |  |
| 主机名或 IP 地址 | 填入自建 Oracle 数据库的访问地址。 |  |
| 端口 | 填入自建 Oracle 数据库的服务端口，默认为 1521 。 说明 本案例中，该服务端口需开放至公网。 |  |
| Oracle 类型 | 非 RAC 实例 ：选择该项后，您还需要填写 SID 信息。 RAC 或 PDB 实例 ：选择该项后，您还需要填写 ServiceName 信息。 本案例选择为 非 RAC 实例 。 |  |
| 数据库账号 | 填入源 Oracle 数据库的账号，权限要求请参见 [准备工作](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-oracle-database-to-an-apsaradb-rds-for-mysql-instance-1#section-twr-1es-5w6) 。 |  |
| 数据库密码 | 填入该数据库账号对应的密码。 |  |
| 目标库信息 | 数据库类型 | 选择 MySQL 。 |
| 接入方式 | 选择 云实例 。 |  |
| 实例地区 | 选择目标 RDS MySQL 实例所属地域。 |  |
| RDS 实例 ID | 选择目标 RDS MySQL 实例 ID。 |  |
| 数据库账号 | 填入目标 RDS 实例的数据库账号，权限要求请参见 [准备工作](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-oracle-database-to-an-apsaradb-rds-for-mysql-instance-1#section-twr-1es-5w6) 。 |  |
| 数据库密码 | 填入该数据库账号对应的密码。 |  |
| 连接方式 | 根据数据库实际情况选择 非加密连接 或 SSL 安全连接
