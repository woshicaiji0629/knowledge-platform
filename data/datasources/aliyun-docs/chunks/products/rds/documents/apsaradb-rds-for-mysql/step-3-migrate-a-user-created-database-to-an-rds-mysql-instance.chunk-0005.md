## 配置源库参数
本教程中的源库指您的原业务数据库，即ECS实例中的自建数据库。
数据库类型：选择MySQL。
接入方式：选择ECS自建数据库。根据部署位置的不同，自建数据库可以划分为部署在ECS的自建数据库与部署在本地的自建数据库。针对不同场景，DTS提供了多种接入方式满足数据库迁移需求，详情请参见[各接入方式准备工作](https://help.aliyun.com/zh/dts/user-guide/preparation-overview)：

| 自建库部署位置 | 公网访问 | DTS 接入方式（同迁移任务配置） |
| --- | --- | --- |
| ECS（已在云上） | 均可 | ECS 自建数据库 |
| 本地（未上云） | 具备公网地址 | 公网 IP |
| 不具备公网地址 | 云企业网 CEN 、 数据库网关 DG 、 专线/VPN 网关/智能网关 |  |

实例地区：选择ECS实例所在地域。
ECS实例ID：在下拉列表中选择待迁移的ECS实例。
端口：默认为3306。
数据库账号和数据库密码：填写ECS自建数据库中用于数据迁移或拥有相关权限的账号和密码。如未准备，您可以新建账号并授予相关权限，详细步骤请参见[为自建](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)[MySQL](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)[创建账号](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)。
连接方式：如果自建数据库未开启SSL加密，选择非加密连接；如果已开启SSL加密，选择SSL安全连接，并上传CA 证书和CA 密钥。
