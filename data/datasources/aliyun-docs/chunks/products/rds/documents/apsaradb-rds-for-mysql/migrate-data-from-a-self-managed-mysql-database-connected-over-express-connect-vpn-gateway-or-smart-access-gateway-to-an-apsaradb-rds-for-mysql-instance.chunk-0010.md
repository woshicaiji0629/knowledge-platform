| 类别 | 配置 | 说明 |
| --- | --- | --- |
| 无 | 任务名称 | DTS 会自动生成一个任务名称，建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| 源库信息 | 实例类型 | 选择 通过专线/VPN 网关/智能接入网关接入的自建数据库 。 |
| 实例地区 | 选择专线、VPN 网关或智能接入网关接入的专有网络所属的地域。 |  |
| 对端专有网络 | 选择专线、VPN 网关或智能接入网关接入的专有网络。 |  |
| 数据库类型 | 选择 MySQL 。 |  |
| IP 地址 | 填入自建 MySQL 数据库的访问地址。 |  |
| 端口 | 填入自建 MySQL 数据库的服务端口，默认为 3306 。 |  |
| 数据库账号 | 填入自建 MySQL 的数据库账号，权限要求请参见 [数据库账号的权限要求](migrate-data-from-a-self-managed-mysql-database-connected-over-express-connect-vpn-gateway-or-smart-access-gateway-to-an-apsaradb-rds-for-mysql-instance.md) 。 |  |
| 数据库密码 | 填入该数据库账号对应的密码。 说明 源库信息填写完毕后，您可以单击 数据库密码 后的 测试连接 来验证填入的源库信息是否正确。源库信息填写正确则提示 测试通过 ；如果提示 测试失败 ，单击 测试失败 后的 诊断 ，根据提示调整填写的源库信息。 |  |
| 目标库信息 | 实例类型 | 选择 RDS 实例 。 |
| 实例地区 | 选择目标 RDS 实例所属地域。 |  |
| RDS 实例 ID | 选择目标 RDS 实例 ID。 |  |
| 数据库账号 | 填入目标 RDS 实例的数据库账号，权限要求请参见 [数据库账号的权限要求](migrate-data-from-a-self-managed-mysql-database-connected-over-express-connect-vpn-gateway-or-smart-access-gateway-to-an-apsaradb-rds-for-mysql-instance.md) 。 |  |
| 数据库密码 | 填入该数据库账号对应的密码。 说明 目标库信息填写完毕后，您可以单击 数据库密码 后的 测试连接 来验证填入的目标库信息是否正确。目标库信息填写正确则提示 测试通过 ；如果提示 测试失败 ，单击 测试失败 后的 诊断 ，根据提示调整填写的目标库信息。 |  |
| 连接方式 | 根据需求选择 非加密连接 或 SSL 安全连接 。如果设置为 SSL 安全连接 ，您需要提前开启
