# 将自建数据库迁移至其他账号下的RDS实例-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/migrate-data-to-an-apsaradb-rds-for-mysql-instance-across-alibaba-cloud-accounts

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-mysql/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-mysql/getting-started.md)

- [AI能力中心](products/rds/documents/apsaradb-rds-for-mysql/ai-capability-center.md)

- [自研内核AliSQL](products/rds/documents/apsaradb-rds-for-mysql/proprietary-alisql.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-mysql/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-mysql/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-mysql/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-mysql/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-mysql/support.md)

[首页](https://help.aliyun.com/zh)

# 通过专线、VPN网关或智能接入网关接入的自建MySQL迁移至其他账号下的RDS实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍如何使用数据传输服务DTS（Data Transmission Service），将通过专线、VPN网关、智能接入网关接入的自建MySQL迁移至其他云账号下的RDS MySQL或RDS MySQL Serverless实例。DTS支持结构迁移、全量数据迁移以及增量数据迁移，同时使用这三种迁移类型可以实现在自建应用不停服的情况下，平滑地完成数据库迁移。

## 前提条件

- 

自建MySQL数据库版本为5.1、5.5、5.6、5.7或8.0版本。

- 

RDS MySQL实例的存储空间须大于自建MySQL数据库占用的存储空间。

- 

自建数据库所属的本地网络已通过专线、VPN网关或智能接入网关的方式接入至阿里云，且该阿里云账号和目标RDS MySQL或RDS MySQL Serverless实例所属的阿里云账号不同。

说明

相关接入方案请参见[准备工作概览](https://help.aliyun.com/zh/dts/user-guide/preparation-overview)，本文不做详细介绍。

## 背景信息

本地IDC已通过专线、VPN网关或智能接入网关接入至阿里云，现在需要将本地IDC中的自建MySQL通过专有网络迁移至其他阿里云账号下的RDS MySQL中，详细架构如下图所示。

## 注意事项

- 

DTS在执行全量数据迁移时将占用源库和目标库一定的读写资源，可能会导致数据库的负载上升，在数据库性能较差、规格较低或业务量较大的情况下（例如源库有大量慢SQL、存在无主键表或目标库存在死锁等），可能会加重数据库压力，甚至导致数据库服务不可用。因此您需要在执行数据迁移前评估源库和目标库的性能，同时建议您在业务低峰期执行数据迁移（例如源库和目标库的CPU负载在30%以下）。

- 

如果源库中待迁移的表没有主键或唯一约束，且所有字段没有唯一性，可能会导致目标数据库中出现重复数据。

- 

对于数据类型为FLOAT或DOUBLE的列，DTS会通过ROUND(COLUMN,PRECISION)来读取该列的值。如果没有明确定义其精度，DTS对FLOAT的迁移精度为38位，对DOUBLE的迁移精度为308位，请确认迁移精度是否符合业务预期。

- 

DTS会自动地在阿里云RDS MySQL中创建数据库，如果待迁移的数据库名称不符合阿里云RDS的定义规范，您需要在配置迁移任务之前在阿里云RDS MySQL中创建数据库。

说明

关于阿里云RDS的定义规范和创建数据库的操作方法，请参见[创建数据库](products/rds/documents/apsaradb-rds-for-mysql/create-a-database-for-an-apsaradb-rds-for-mysql-instance.md)。

- 

对于迁移失败的任务，DTS会触发自动恢复。在您将业务切换至目标实例前，请务必先结束或释放该任务，避免该任务被自动恢复后，导致源端数据覆盖目标实例的数据。

## 费用说明

| 迁移类型 | 链路配置费用 | 公网流量费用 |
| --- | --- | --- |
| 结构迁移和全量数据迁移 | 不收费。 | 当目标库的 接入方式 为 公网 IP 时收取公网流量费用。更多信息，请参见 [计费概述](https://help.aliyun.com/zh/dts/product-overview/billing-overview#concept-261679) 。 |
| 增量数据迁移 | 收费，详情请参见 [计费概述](https://help.aliyun.com/zh/dts/product-overview/billing-overview#concept-261679) 。 |  |


## 迁移类型说明

- 

结构迁移

DTS将迁移对象的结构定义迁移到目标实例，目前DTS支持结构迁移的对象为表、视图、触发器、存储过程和存储函数。

说明

- 

在结构迁移时，DTS会将视图、存储过程和函数中的DEFINER转换为INVOKER。

- 

由于DTS不迁移USER信息，因此在调用目标库的视图、存储过程和函数时需要对调用者授予读写权限。

- 

全量数据迁移

DTS会将自建MySQL数据库迁移对象的存量数据，全部迁移到目标RDS MySQL实例数据库中。

说明

由于全量数据迁移会并发INSERT导致目标实例的表存在碎片，全量迁移完成后目标库的表空间会比源库的表空间大。

- 

增量数据迁移

在全量迁移的基础上，DTS会读取自建MySQL数据库的binlog信息，将自建MySQL数据库的增量更新数据同步到目标RDS MySQL实例中。通过增量数据迁移可以实现在自建应用不停服的情况下，平滑地完成MySQL数据库的迁移上云。

## 增量数据迁移支持同步的SQL操作

- 

- 

- 

- 

- 

| 操作类型 | SQL 操作语句 |
| --- | --- |
| DML | INSERT、UPDATE、DELETE、REPLACE |
| DDL | ALTER TABLE、ALTER VIEW CREATE FUNCTION、CREATE INDEX、CREATE PROCEDURE、CREATE TABLE、CREATE VIEW DROP INDEX、DROP TABLE RENAME TABLE TRUNCATE TABLE |


## 数据库账号的权限要求

| 数据库 | 结构迁移 | 全量迁移 | 增量迁移 |
| --- | --- | --- | --- |
| 自建 MySQL 数据库 | SELECT 权限 | SELECT 权限 | REPLICATION SLAVE、REPLICATION CLIENT、SHOW VIEW 和 SELECT 权限 |
| RDS MySQL 或 RDS MySQL Serverless 实例 | 读写权限 | 读写权限 | 读写权限 |


数据库账号创建及授权方法：

- 

自建MySQL数据库请参见[为自建](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)[MySQL](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)[创建账号并设置](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)[binlog](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)。

- 

RDS MySQL或RDS MySQL Serverless实例请参见[创建账号](products/rds/documents/apsaradb-rds-for-mysql/create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)和[修改账号权限](products/rds/documents/apsaradb-rds-for-mysql/modify-the-permissions-of-a-standard-account-on-an-apsaradb-rds-for-mysql-instance.md)。

## 准备工作

- 

[为自建](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)[MySQL](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)[创建账号并设置](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)[binlog](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)。

- 

使用专线所属的阿里云账号登录[控制台](https://homenew.console.aliyun.com/)，允许DTS访问专线所属的网络，详情请参见[通过](https://help.aliyun.com/zh/dts/user-guide/connect-a-data-center-to-dts-using-vpn-gateway#concept-227432)[VPN](https://help.aliyun.com/zh/dts/user-guide/connect-a-data-center-to-dts-using-vpn-gateway#concept-227432)[网关实现本地](https://help.aliyun.com/zh/dts/user-guide/connect-a-data-center-to-dts-using-vpn-gateway#concept-227432)[IDC](https://help.aliyun.com/zh/dts/user-guide/connect-a-data-center-to-dts-using-vpn-gateway#concept-227432)[与](https://help.aliyun.com/zh/dts/user-guide/connect-a-data-center-to-dts-using-vpn-gateway#concept-227432)[DTS](https://help.aliyun.com/zh/dts/user-guide/connect-a-data-center-to-dts-using-vpn-gateway#concept-227432)[云服务互通](https://help.aliyun.com/zh/dts/user-guide/connect-a-data-center-to-dts-using-vpn-gateway#concept-227432)。

- 

创建RAM角色并授权其访问专线所属的阿里云账号下的相关云资源，详情请参见[跨阿里云账号传输专有网络下的自建数据库时如何配置](https://help.aliyun.com/zh/dts/user-guide/configure-ram-authorization-for-data-migration-or-synchronization-from-a-self-managed-database-in-a-vpc-across-different-alibaba-cloud-accounts#task-2332989)[RAM](https://help.aliyun.com/zh/dts/user-guide/configure-ram-authorization-for-data-migration-or-synchronization-from-a-self-managed-database-in-a-vpc-across-different-alibaba-cloud-accounts#task-2332989)[授权](https://help.aliyun.com/zh/dts/user-guide/configure-ram-authorization-for-data-migration-or-synchronization-from-a-self-managed-database-in-a-vpc-across-different-alibaba-cloud-accounts#task-2332989)。

## 操作步骤

- 

使用目标RDS实例所属的阿里云账号登录[数据传输控制台](https://dts.console.aliyun.com/)。

说明

若数据传输控制台自动跳转至数据管理DMS控制台，您可以在右下角的中单击，返回至旧版数据传输控制台。

- 

在左侧导航栏，单击数据迁移。

- 

在迁移任务列表页面顶部，选择迁移的目标集群所属地域。

- 

单击页面右上角的创建迁移任务。

- 

选择实例类型为通过专线/VPN网关/智能接入网关接入的自建数据库，然后单击其他阿里云账号下的专有网络。

- 

配置迁移任务的源库及目标库信息。

| 类别 | 配置 | 说明 |
| --- | --- | --- |
| 无 | 任务名称 | DTS 会自动生成一个任务名称，建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| 源库信息 | 实例类型 | 选择 通过专线/VPN 网关/智能接入网关接入的自建数据库 。 |
| 实例地区 | 选择自建数据库接入的专有网络所属地域。 |  |
| 所属阿里云账号 ID | 填入自建数据库接入的阿里云账号 ID。 说明 您可以使用自建数据库接入的阿里云账号（主账号）登录 [安全设置](https://account.console.aliyun.com/#/secure) 页面来获取 账号 ID 。 |  |
| 角色名称 | 填入 [准备工作](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-to-an-apsaradb-rds-for-mysql-instance-across-alibaba-cloud-accounts.md) 中步骤 3 创建的 RAM 角色名称。 |  |
| 对端专有网络 | 选择自建数据库接入的专有网络。 |  |
| 数据库类型 | 选择 MySQL 。 |  |
| IP 地址 | 填入自建 MySQL 数据库的访问地址。 |  |
| 端口 | 填入自建 MySQL 数据库的服务端口，默认为 3306 。 |  |
| 数据库账号 | 填入自建 MySQL 的数据库账号，权限要求请参见 [数据库账号的权限要求](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-mysql-database-connected-over-express-connect-vpn-gateway-or-smart-access-gateway-to-an-apsaradb-rds-for-mysql-instance#section-31k-oq1-w0z) 。 |  |
| 数据库密码 | 填入该数据库账号的密码。 说明 源库信息填写完毕后，您可以单击 数据库密码 后的 测试连接 来验证填入的源库信息是否正确。源库信息填写正确则提示 测试通过 ；如果提示 测试失败 ，单击 测试失败 后的 诊断 ，根据提示调整填写的源库信息。 |  |
| 目标库信息 | 实例类型 | 选择 RDS 实例 。 |
| 实例地区 | 选择目标 RDS 实例所属地域。 |  |
| RDS 实例 ID | 选择目标 RDS 实例 ID。 |  |
| 数据库账号 | 填入目标 RDS 实例的数据库账号，权限要求请参见 [数据库账号的权限要求](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-a-self-managed-mysql-database-connected-over-express-connect-vpn-gateway-or-smart-access-gateway-to-an-apsaradb-rds-for-mysql-instance#section-31k-oq1-w0z) 。 |  |
| 数据库密码 | 填入该数据库账号的密码。 说明 目标库信息填写完毕后，您可以单击 数据库密码 后的 测试连接 来验证填入的目标库信息是否正确。目标库信息填写正确则提示 测试通过 ；如果提示 测试失败 ，单击 测试失败 后的 诊断 ，根据提示调整填写的目标库信息。 |  |
| 连接方式 | 根据需求选择 非加密连接 或 SSL 安全连接 。如果设置为 SSL 安全连接 ，您需要提前开启 RDS 实例的 SSL 加密功能，详情请参见 [设置](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) [SSL](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) [加密](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) 。 |  |


- 

配置完成后，单击页面右下角的授权白名单并进入下一步。

如果源或目标数据库是阿里云数据库实例（例如RDS MySQL、云数据库MongoDB版等），DTS会自动将对应地区DTS服务的IP地址添加到阿里云数据库实例的白名单；如果源或目标数据库是ECS上的自建数据库，DTS会自动将对应地区DTS服务的IP地址添加到ECS的安全规则中，您还需确保自建数据库没有限制ECS的访问（若数据库是集群部署在多个ECS实例，您需要手动将DTS服务对应地区的IP地址添加到其余每个ECS的安全规则中）；如果源或目标数据库是IDC自建数据库或其他云数据库，则需要您手动添加对应地区DTS服务的IP地址，以允许来自DTS服务器的访问。DTS服务的IP地址，请参见[DTS](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)[服务器的](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)[IP](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)[地址段](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)。

警告

DTS自动添加或您手动添加DTS服务的公网IP地址段可能会存在安全风险，一旦使用本产品代表您已理解和确认其中可能存在的安全风险，并且需要您做好基本的安全防护，包括但不限于加强账号密码强度防范、限制各网段开放的端口号、内部各API使用鉴权方式通信、定期检查并限制不需要的网段，或者使用通过内网（专线/VPN网关/智能网关）的方式接入。

- 

选择迁移类型和迁移对象。

- 

- 

- 

- 

- 

- 

- 

| 配置 | 说明 |
| --- | --- |
| 迁移类型 | 如果只需要进行全量迁移，则同时选中 结构迁移 和 全量数据迁移 。 如果需要进行不停机迁移，则同时选中 结构迁移 、 全量数据迁移 和 增量数据迁移 。 说明 如果未选中 增量数据迁移 ，为保障数据一致性，数据迁移期间请勿在源库中写入新的数据。 |
| 迁移对象 | 在 迁移对象 框中单击待迁移的对象，然后单击 图标将其移动至 已选择对象 框。 说明 迁移对象选择的粒度为库、表、列。 默认情况下，迁移对象在目标库中的名称与源库保持一致。如果您需要改变迁移对象在目标库中的名称，需要使用对象名映射功能，详情请参见 [库表列映射](https://help.aliyun.com/zh/dts/user-guide/object-name-mapping#concept-610481) 。 如果使用了对象名映射功能，可能会导致依赖这个对象的其他对象迁移失败。 |
| 映射名称更改 | 如需更改迁移对象在目标实例中的名称，请使用对象名映射功能，详情请参见 [库表列映射](https://help.aliyun.com/zh/dts/user-guide/object-name-mapping#concept-610481) 。 |
| 源、目标库无法连接重试时间 | 当源、目标库无法连接时，DTS 默认重试 720 分钟（即 12 小时），您也可以自定义重试时间。如果 DTS 在设置的时间内重新连接上源、目标库，迁移任务将自动恢复。否则，迁移任务将失败。 说明 由于连接重试期间，DTS 将收取任务运行费用，建议您根据业务需要自定义重试时间，或者在源和目标库实例释放后尽快释放 DTS 实例。 |
| 源表 DMS_ONLINE_DDL 过程中是否复制临时表到目标库 | 如源库使用 [数据管理](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582) [DMS（Data Management）](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582) 执行 Online DDL 变更，您可以选择是否迁移 Online DDL 变更产生的临时表数据。 是 ：迁移 Online DDL 变更产生的临时表数据。 说明 Online DDL 变更产生的临时表数据过大，可能会导致迁移任务延迟。 否 ：不迁移 Online DDL 变更产生的临时表数据，只迁移源库的原始 DDL 数据。 说明 该方案会导致目标库锁表。 |


- 

上述配置完成后，单击页面右下角的预检查并启动。

说明

- 

在迁移任务正式启动之前，会先进行预检查。只有预检查通过后，才能成功启动迁移任务。

- 

如果预检查失败，单击具体检查项后的，查看失败详情。

- 

您可以根据提示修复后重新进行预检查。

- 

如无需修复告警检测项，您也可以选择确认屏蔽、忽略告警项并重新进行预检查，跳过告警检测项重新进行预检查。

- 

预检查通过后，单击下一步。

- 

在弹出的购买配置确认对话框，选择链路规格并选中数据传输（按量付费）服务条款。

- 

单击购买并启动，迁移任务正式开始。

- 

结构迁移+全量数据迁移

请勿手动结束迁移任务，否则可能会导致数据不完整。您只需等待迁移任务完成即可，迁移任务会自动结束。

- 

结构迁移+全量数据迁移+增量数据迁移

迁移任务不会自动结束，您需要手动结束迁移任务。

重要

请选择合适的时间手动结束迁移任务，例如业务低峰期或准备将业务切换至目标集群时。

- 

观察迁移任务的进度变更为增量迁移，并显示为无延迟状态时，将源库停写几分钟，此时增量迁移的状态可能会显示延迟的时间。

- 

等待迁移任务的增量迁移再次进入无延迟状态后，手动结束迁移任务。

- 

将业务切换至目标RDS MySQL。

[上一篇：从通过专线、VPN网关或智能接入网关接入的自建MySQL迁移至RDS实例](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-connected-over-express-connect-vpn-gateway-or-smart-access-gateway-to-an-apsaradb-rds-for-mysql-instance.md)[下一篇：从自建Db2迁移至RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-db2-database-to-an-apsaradb-rds-for-mysql-instance.md)

该文章对您有帮助吗？

反馈

### 为什么选择阿里云

[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)

### 大模型

[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)

### 产品和定价

[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)

### 技术内容

[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)

### 权益

[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)

### 服务

[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)

### 关注阿里云

关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务

联系我们：4008013260

[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)

### 友情链接

[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)

© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
