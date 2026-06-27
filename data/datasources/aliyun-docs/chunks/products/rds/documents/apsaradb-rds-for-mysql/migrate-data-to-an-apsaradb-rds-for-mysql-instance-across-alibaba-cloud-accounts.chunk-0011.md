| 类别 | 配置 | 说明 |
| --- | --- | --- |
| 无 | 任务名称 | DTS 会自动生成一个任务名称，建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| 源库信息 | 实例类型 | 选择 通过专线/VPN 网关/智能接入网关接入的自建数据库 。 |
| 实例地区 | 选择自建数据库接入的专有网络所属地域。 |  |
| 所属阿里云账号 ID | 填入自建数据库接入的阿里云账号 ID。 说明 您可以使用自建数据库接入的阿里云账号（主账号）登录 [安全设置](https://account.console.aliyun.com/#/secure) 页面来获取 账号 ID 。 |  |
| 角色名称 | 填入 [准备工作](migrate-data-to-an-apsaradb-rds-for-mysql-instance-across-alibaba-cloud-accounts.md) 中步骤 3 创建的 RAM 角色名称。 |  |
| 对端专有网络 | 选择自建数据库接入的专有网络。 |  |
| 数据库类型 | 选择 MySQL 。 |  |
| IP 地址 | 填入自建 MySQL 数据库的访问地址。 |  |
| 端口 | 填入自建 MySQL 数据库的服务端口，默认为 3306 。 |  |
| 数据库账号 | 填入自建 MySQL 的数据库账号，权限要求请参见 [数据库账号的权限要求](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-mysql-database-connected-over-express-connect-vpn-gateway-or-smart-access-gateway-to-an-apsaradb-rds-for-mysql-instance#section-31k-oq1-w0z) 。 |  |
| 数据库密码 | 填入该数据库账号的密码。 说明 源库信息填写完毕后，您可以单击 数据库密码 后的 测试连接 来验证填入的源库信息是否正确。源库信息填写正确则提示 测试通过 ；如果提示 测试失败 ，单击 测试失败 后的 诊断 ，根据提示调整填写的源库信息。 |  |
| 目标库信息 | 实例类型 | 选择 RDS 实例 。 |
| 实例地区 | 选择目标 RDS 实例所属地域。 |  |
| RDS 实例 ID | 选择目标 RDS 实例 ID。 |  |
| 数据库账号 | 填入目标 RDS 实例的数据库账号，权限要求请参见 [数据库账号的权限要求](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-se
