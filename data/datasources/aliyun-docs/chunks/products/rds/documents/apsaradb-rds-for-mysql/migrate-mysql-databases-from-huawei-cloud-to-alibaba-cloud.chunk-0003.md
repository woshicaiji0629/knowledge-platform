## 操作步骤
进入目标地域的迁移任务列表页面。
登录[数据传输服务](https://dtsnew.console.aliyun.com/)[DTS](https://dtsnew.console.aliyun.com/)[控制台](https://dtsnew.console.aliyun.com/)。
在左侧导航栏，单击数据迁移。
在页面左上角，选择实例所属地域。
单击创建任务，进入任务配置页面，配置源库及目标库信息。

| 库类别 | 参数 | 说明 |
| --- | --- | --- |
| 源库 | 数据库类型 | 源数据库类型，选择 MySQL 。 |
| 接入方式 | 源库实例接入 DTS 的方式，本示例选择 公网 IP 。 |  |
| 实例地区 | 公网接入，选择目标地域即可，本示例选择 华东 1 （杭州） 。 |  |
| 域名或 IP 地址 | 华为云云数据库 RDS MySQL 实例的 公网地址 。 |  |
| 端口 | 华为云云数据库 RDS MySQL 实例的 数据库端口 。 |  |
| 数据库账号 | 华为云云数据库 RDS MySQL 实例的 高权限账号 。 |  |
| 数据库密码 | 华为云云数据库 RDS MySQL 实例的高权限账号的密码。 |  |
| 目标库 | 数据库类型 | 目标实例的类型，选择 MySQL 。 |
| 接入方式 | 目标实例接入 DTS 的方式，本示例选择 云实例 。 |  |
| 实例地区 | RDS MySQL 实例所在的地域。 |  |
| 是否跨阿里云账号 | 选择 不跨账号 。 |  |
| RDS 实例 ID | RDS MySQL 实例的 ID。 |  |
| 数据库账号 | 目标实例的 高权限账号 。 |  |
| 数据库密码 | 目标实例的高权限账号对应的密码。 |  |
| 连接方式 | 根据数据库实际情况选择 非加密连接 或 SSL 安全连接 。如果设置为 SSL 安全连接 ，您需要提前开启 RDS MySQL 实例的 SSL 加密功能，详情请参见 [使用云端证书快速开启](configure-a-cloud-certificate-to-enable-ssl-encryption.md) [SSL](configure-a-cloud-certificate-to-enable-ssl-encryption.md) [链路加密](configure-a-cloud-certificate-to-enable-ssl-encryption.md) 。 |  |
