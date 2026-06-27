## 目标库配置

| 配置项 | 说明 |
| --- | --- |
| 数据库类型 | 选择 MySQL 。 |
| 接入方式 | 选择 云实例 。 |
| 实例地区 | 选择 RDS MySQL 实例所在地域。 |
| 是否跨阿里云账号 | 选择 不跨账号 。 |
| RDS 实例 ID | 选择目标 RDS MySQL 实例 ID。 |
| 数据库账号 | 填入 RDS MySQL 实例的数据库账号，推荐使用 高权限账号 。 |
| 数据库密码 | 填入该数据库账号对应的密码。 |
| 连接方式 | 根据数据库实际情况选择 非加密连接 或 SSL 安全连接 。如果设置为 SSL 安全连接 ，您需要提前开启 RDS MySQL 实例的 SSL 加密功能，详情请参见 [使用云端证书快速开启](configure-a-cloud-certificate-to-enable-ssl-encryption.md) [SSL](configure-a-cloud-certificate-to-enable-ssl-encryption.md) [链路加密](configure-a-cloud-certificate-to-enable-ssl-encryption.md) 。 |

测试源库与目标库连接
在页面下方单击测试连接以进行下一步，并在弹出的DTS服务器访问授权对话框单击测试连接。若测试不通过，请根据错误提示检查网络、账号或权限配置。
配置任务对象
您需要依次完成以下对象配置、高级配置和数据校验配置内容。
