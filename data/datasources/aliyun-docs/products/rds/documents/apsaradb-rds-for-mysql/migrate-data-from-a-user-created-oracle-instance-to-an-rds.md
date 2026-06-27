# 自建Oracle通过DTS迁移至RDS MySQL-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/migrate-data-from-a-user-created-oracle-instance-to-an-rds

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

# 从自建Oracle迁移至阿里云RDS MySQL

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍如何使用数据传输服务DTS（Data Transmission Service），将自建Oracle数据迁移至RDS MySQL实例。DTS支持结构迁移、全量数据迁移以及增量数据迁移，同时使用这三种迁移类型可以实现在本地应用不停服的情况下，平滑地完成Oracle数据库的数据迁移。

## 前提条件

- 

已创建源数据库自建Oracle和目标实例RDS MySQL。

说明

- 

目标实例RDS MySQL的创建方式，请参见[快速创建](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[实例](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)。

- 

源数据库和目标实例支持的版本，请参见[迁移方案概览](https://help.aliyun.com/zh/dts/user-guide/overview-of-data-migration-scenarios#concept-26618-zh)。

- 

自建Oracle数据库已开启ARCHIVELOG（归档模式），设置合理的归档日志保持周期且归档日志能够被访问，详情请参见[ARCHIVELOG](https://docs.oracle.com/database/121/ADMIN/archredo.htm#ADMIN008)。

- 

自建Oracle数据库已开启Supplemental Logging，且已开启supplemental_log_data_pk，supplemental_log_data_ui，详情请参见[Supplemental Logging](https://docs.oracle.com/database/121/SUTIL/GUID-D857AF96-AC24-4CA1-B620-8EA3DF30D72E.htm#SUTIL1582)。

- 

已创建目标RDS MySQL实例，创建方式，请参见[快速创建](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[实例](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)。

- 

建议在执行数据迁移前了解源库为Oracle时DTS支持的能力和限制条件，并使用ADAM（Advanced Database & Application Migration）进行数据库评估，以便您平滑地迁移上云。更多信息，请参见[Oracle](https://help.aliyun.com/zh/dts/user-guide/configure-the-oracle-database-and-create-an-account)[数据库的限制和准备工作](https://help.aliyun.com/zh/dts/user-guide/configure-the-oracle-database-and-create-an-account)和[数据库评估概览](https://help.aliyun.com/zh/dts/user-guide/overview)。

## 注意事项

说明

- 

在库表结构迁移过程中，DTS会将源数据库中的外键迁移到目标数据库。

- 

在全量迁移和增量迁移过程中，DTS会以Session级别暂时禁用约束检查以及外键级联操作。若任务运行时源库存在级联更新、删除操作，可能会导致数据不一致。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 类型 | 说明 |
| --- | --- |
| 源库限制 | 带宽要求：源库所属的服务器需具备足够出口带宽，否则将影响数据迁移速率。 如果源库通过专线的方式接入，那么需要将其中任意 1 个 VIP 配置到连接信息中，实现 Oracle RAC 通过专线接入迁移任务。 如自建 Oracle 为 RAC 架构，且用专线/VPN 网关/智能接入网关、数据库网关 DG、云企业网 CEN 和 ECS 的接入方式，则不支持配置 ScanIP，仅支持将其中任意 1 个 VIP 配置到连接信息中，该方式配置后不支持 RAC 的节点切换。 如果源库存在 varchar2 类型的空字符串（Oracle 会将其处理为 null）且对应的目标库字段有非空约束，将会导致迁移任务失败。 迁移对象要求： 待迁移的表需具备主键或唯一约束，且字段具有唯一性，否则可能会导致目标数据库中出现重复数据。 如果您的自建 Oracle 版本为 12c 及以上，待迁移表的名称长度需不超过 30 个字节。 如迁移对象为表级别，且需进行编辑（如表列名映射），则单次迁移任务仅支持迁移至多 1000 张表。当超出数量限制，任务提交后会显示请求报错，此时建议您拆分待迁移的表，分批配置多个任务，或者配置整库的迁移任务。 如需进行增量迁移，Redo Log、Archive Log： 需开启。 如为增量迁移任务，DTS 要求源数据库的 Redo Log、Archive Log 保存 24 小时以上，如为全量迁移和增量迁移任务，DTS 要求源数据库的 Redo Log、Archive Log 至少保留 7 天以上（您可在全量迁移完成后将 Redo Log、Archive Log 保存时间设置为 24 小时以上），否则 DTS 可能因无法获取 Redo Log、Archive Log 而导致任务失败，极端情况下甚至可能会导致数据不一致或丢失。由于您所设置的 Redo Log、Archive Log 保存时间低于 DTS 要求的时间进而导致的问题，不在 DTS 的 SLA 保障范围内。 源库的操作限制： 在库表结构迁移和全量迁移阶段，请勿执行库或表结构变更的 DDL 操作，否则数据迁移任务失败。 如仅执行全量数据迁移，请勿向源实例中写入新的数据，否则会导致源和目标数据不一致。为实时保持数据一致性，建议选择结构迁移、全量数据迁移和增量数据迁移。 单独更新大文本字段场景不支持，任务会失败。 |
| 其他限制 | 在增量迁移过程中，不支持使用 Oracle Data Pump 向源库导入数据，否则可能会导致数据丢失。 不支持迁移外部表。 若待迁移的数据中包含需要四字节存储的内容（例如生僻字、表情等信息），则目标端接收数据的数据库和表必须使用 utf8mb4 字符集。 说明 若您使用 DTS 迁移库表结构，则需将目标库中实例级别的参数 character_set_server 设置为 utf8mb4。 执行数据迁移前需评估源库和目标库的性能，同时建议业务低峰期执行数据迁移。否则全量数据迁移时 DTS 占用源和目标库一定读写资源，可能会导致数据库的负载上升。 由于全量数据迁移会并发执行 INSERT 操作，导致目标数据库的表产生碎片，因此全量迁移完成后目标数据库的表存储空间会比源实例的表存储空间大。 DTS 会尝试恢复七天之内迁移失败任务。因此业务切换至目标实例前，请务必结束或释放该任务，或者将 DTS 访问目标实例账号的写权限用 revoke 命令回收掉。避免该任务被自动恢复后，源端数据覆盖目标实例的数据。 若目标库的 DDL 写入失败，DTS 任务会继续运行，您需要在任务日志中查看执行失败的 DDL。查看任务日志的方法，请参见 [查询任务日志](https://help.aliyun.com/zh/dts/user-guide/view-task-logs-1) 。 需确保源库和目标库的字符集兼容，否则可能会导致数据不一致或任务失败。 建议使用 DTS 的库表结构迁移功能，否则可能会因为数据类型不兼容而导致任务失败。 源库和目标库的时区必须保持一致。 若您将列名仅大小写不同的字段写入到目标 MySQL 数据库的同一个表中，可能会因为 MySQL 数据库列名大小写不敏感，导致迁移结果不符合预期。 在数据迁移完成后（实例的 运行状态 为 已完成 ），建议使用 analyze table <表名> 命令以确认数据均已写入目标表。例如，在目标 MySQL 数据库触发 HA 切换机制后，可能会导致数据只写到了内存，从而造成数据丢失。 若实例运行失败，DTS 技术支持人员将在 8 小时内尝试恢复该实例。在恢复失败实例的过程中，可能会对该实例进行重启、调整参数等操作。 说明 在调整参数时，仅会修改实例的参数，不会对数据库中的参数进行修改。 可能修改的参数，包括但不限于 [修改实例参数](https://help.aliyun.com/zh/dts/user-guide/modify-the-parameters-of-a-dts-instance#section-ys2-2c2-wzo) 中的参数。 |
| 特殊情况 | 当目标库为 RDS MySQL 时 RDS MySQL 实例对表名的英文大小写不敏感，如果使用大写英文建表，RDS MySQL 会先把表名转为小写再执行建表操作。 如果源 Oracle 数据库中存在表名相同仅大小写不同的表，可能会导致迁移对象重名并在结构迁移中提示“对象已经存在”。如果出现这种情况，请在配置迁移对象的时候，使用 DTS 提供的对象名映射功能对重名的对象进行重命名，将表名转为大写，详情请参见 [库表列映射](https://help.aliyun.com/zh/dts/user-guide/object-name-mapping#concept-610481) 。 DTS 会自动在 RDS MySQL 中创建数据库，如果待迁移的数据库名称不符合 RDS MySQL 的定义规范，您需要在配置迁移任务之前在 RDS MySQL 中创建数据库。相关操作，请参见 [管理数据库](products/rds/documents/apsaradb-rds-for-mysql/create-a-database-for-an-apsaradb-rds-for-mysql-instance.md) 。 |


## 费用说明

| 迁移类型 | 链路配置费用 | 公网流量费用 |
| --- | --- | --- |
| 结构迁移和全量数据迁移 | 不收费。 | 当目标库的 接入方式 为 公网 IP 时收取公网流量费用，详情请参见 [计费概述](https://help.aliyun.com/zh/dts/product-overview/billing-overview#concept-261679) 。 |
| 增量数据迁移 | 收费，详情请参见 [计费概述](https://help.aliyun.com/zh/dts/product-overview/billing-overview#concept-261679) 。 |  |


## 迁移类型

- 

- 

| 迁移类型 | 说明 |
| --- | --- |
| 结构迁移 | DTS 将迁移对象的结构定义迁移到目标库。 目前 DTS 仅支持结构迁移表和索引，且存在以下限制： 表：不支持嵌套表；对于聚簇表和索引组织表，会在目标端转换成普通的表。 索引：不支持 Function-Based Index、Domain Index、Bitmap Index 和 ReverseIndex。 说明 DTS 暂不支持结构迁移视图、同义词、存储过程、存储函数、包、自定义类型等。 警告 此场景属于异构数据库间的数据迁移，DTS 在执行结构迁移时数据类型无法完全对应，请谨慎评估数据类型的映射关系对业务的影响，详情请参见 [异构数据库间的数据类型映射关系](https://help.aliyun.com/zh/dts/user-guide/data-type-mappings-between-heterogeneous-databases#concept-1813831) 。 |
| 全量数据迁移 | DTS 会将自建 Oracle 数据库迁移对象的存量数据，全部迁移至目标库。 |
| 增量数据迁移 | DTS 在全量数据迁移的基础上轮询并捕获自建 Oracle 数据库产生的 redo log，将自建 Oracle 数据库的增量更新数据迁移到目标库。 通过增量数据迁移可以实现在自建应用不停服的情况下，平滑地完成数据迁移。 |


## 支持增量迁移的SQL操作

- 

- 

- 

- 

| 操作类型 | SQL 操作语句 |
| --- | --- |
| DML | INSERT、UPDATE、DELETE |
| DDL | CREATE TABLE 说明 表内定义不能包含函数。 ALTER TABLE、ADD COLUMN、DROP COLUMN、RENAME COLUMN、ADD INDEX DROP TABLE RENAME TABLE、TRUNCATE TABLE、CREATE INDEX 说明 仅支持迁移当前数据库账号下的 CREATE INDEX 操作。 |


## 准备工作

登录待迁移的Oracle数据库，创建用于采集数据的账号并授权。

说明

如您已创建包含下述权限的账号，可跳过本步骤。

| 数据库 | 结构迁移 | 全量迁移 | 增量数据迁移 |
| --- | --- | --- | --- |
| 自建 Oracle 数据库 | Schema 的 Owner 权限 | Schema 的 Owner 权限 | 需要精细化授权 |
| RDS MySQL 实例 | 待迁入数据库的写权限 |  |  |


数据库账号创建及授权方法：

- 

自建Oracle数据库请参见[数据库账号准备](https://help.aliyun.com/zh/dts/user-guide/configure-the-oracle-database-and-create-an-account#546a5ab1643wq)、[CREATE USER](https://docs.oracle.com/cd/B19306_01/server.102/b14200/statements_8003.htm)和[GRANT](https://docs.oracle.com/cd/B19306_01/server.102/b14200/statements_9013.htm)。

- 

RDS MySQL实例请参见[创建账号](products/rds/documents/apsaradb-rds-for-mysql/create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)和[修改账号权限](products/rds/documents/apsaradb-rds-for-mysql/modify-the-permissions-of-a-standard-account-on-an-apsaradb-rds-for-mysql-instance.md)。

重要

如需迁移增量数据，您还需要开启归档和补充日志，以获取数据的增量变更。更多信息，请参见[数据库配置](https://help.aliyun.com/zh/dts/user-guide/configure-the-oracle-database-and-create-an-account#4f5033b1646ss)。

## 数据类型映射关系

详情请参见[异构数据库间的数据类型映射关系](https://help.aliyun.com/zh/dts/user-guide/data-type-mappings-between-heterogeneous-databases#concept-1813831)。

## 操作步骤

- 

进入目标地域的迁移任务列表页面（二选一）。

### 通过DTS控制台进入

- 

登录[数据传输服务](https://dtsnew.console.aliyun.com/)[DTS](https://dtsnew.console.aliyun.com/)[控制台](https://dtsnew.console.aliyun.com/)。

- 

在左侧导航栏，单击数据迁移。

- 

在页面左上角，选择迁移实例所属地域。

### 通过DMS控制台进入

说明

实际操作可能会因DMS的模式和布局不同，而有所差异。更多信息。请参见[极简模式控制台](https://help.aliyun.com/zh/dms/simple-mode#concept-2103267)和[自定义](https://help.aliyun.com/zh/dms/configure-the-dms-console-based-on-your-business-requirements#task-2134256)[DMS](https://help.aliyun.com/zh/dms/configure-the-dms-console-based-on-your-business-requirements#task-2134256)[界面布局与样式](https://help.aliyun.com/zh/dms/configure-the-dms-console-based-on-your-business-requirements#task-2134256)。

- 

登录[DMS](https://dms.aliyun.com/new)[数据管理服务](https://dms.aliyun.com/new)。

- 

在顶部菜单栏中，选择Data + AI>数据传输（DTS）>数据迁移。

- 

在迁移任务右侧，选择迁移实例所属地域。

- 

单击创建任务，进入任务配置页面。

- 

可选：在页面右上角，单击试用新版配置页。

说明

- 

若您已进入新版配置页（页面右上角的按钮为返回旧版配置页），则无需执行此操作。

- 

新版配置页和旧版配置页部分参数有差异，建议使用新版配置页。

- 

配置源库及目标库信息。

警告

选择源和目标实例后，建议您仔细阅读页面上方显示的使用限制，否则可能会导致任务失败或数据不一致。

- 

- 

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
| 连接方式 | 根据数据库实际情况选择 非加密连接 或 SSL 安全连接 。如果设置为 SSL 安全连接 ，您需要提前开启 RDS MySQL 实例的 SSL 加密功能，详情请参见 [使用云端证书快速开启](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) [SSL](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) [链路加密](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) 。 |  |


- 

配置完成后，在页面下方单击测试连接以进行下一步，并在弹出的DTS服务器访问授权对话框单击测试连接。

说明

请确保DTS服务的IP地址段能够被自动或手动添加至源库和目标库的安全设置中，以允许DTS服务器的访问。更多信息，请参见[添加](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[DTS](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[服务器的](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[IP](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[地址段](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)。

- 

配置任务对象。

- 

在对象配置页面，配置待迁移的对象。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 配置 | 说明 |
| --- | --- |
| 迁移类型 | 如果只需要进行全量迁移，建议同时选中 库表结构迁移 和 全量迁移 。 如果需要进行不停机迁移，建议同时选中 库表结构迁移 、 全量迁移 和 增量迁移 。 说明 若未选中 库表结构迁移 ，请确保目标库中存在接收数据的数据库和表，并根据实际情况，在 已选择对象 框中使用库表列名映射功能。 若未选中 增量迁移 ，为保障数据一致性，数据迁移期间请勿在源实例中写入新的数据。 |
| 目标已存在表的处理模式 | 预检查并报错拦截 ：检查目标数据库中是否有同名的表。如果目标数据库中没有同名的表，则通过该检查项目；如果目标数据库中有同名的表，则在预检查阶段提示错误，数据迁移任务不会被启动。 说明 如果目标库中同名的表不方便删除或重命名，您可以更改该表在目标库中的名称，请参见 [库表列名映射](https://help.aliyun.com/zh/dts/user-guide/map-object-names#task-2101588) 。 忽略报错并继续执行 ：跳过目标数据库中是否有同名表的检查项。 警告 选择为 忽略报错并继续执行 ，可能导致数据不一致，给业务带来风险，例如： 表结构一致的情况下，在目标库遇到与源库主键的值相同的记录： 全量期间，DTS 会保留目标集群中的该条记录，即源库中的该条记录不会迁移至目标数据库中。 增量期间，DTS 不会保留目标集群中的该条记录，即源库中的该条记录会覆盖至目标数据库中。 表结构不一致的情况下，可能导致只能迁移部分列的数据或迁移失败，请谨慎操作。 |
| 源库对象 | 在 源库对象 框中单击待迁移的对象，然后单击 将其移动到 已选择对象 框。 |
| 已选择对象 | 如需更改单个迁移对象在目标实例中的名称，请右击 已选择对象 中的迁移对象，设置方式，请参见 [库表列名单个映射](https://help.aliyun.com/zh/dts/user-guide/map-object-names#section-g21-1wy-98l) 。 如需批量更改迁移对象在目标实例中的名称，请单击 已选择对象 方框右上方的 批量编辑 ，设置方式，请参见 [库表列名批量映射](https://help.aliyun.com/zh/dts/user-guide/map-object-names#section-2wn-exv-fib) 。 说明 如果使用了对象名映射功能，可能会导致依赖这个对象的其他对象迁移失败。 如需设置 WHERE 条件过滤数据，请在 已选择对象 中右击待迁移的表，在弹出的对话框中设置过滤条件。设置方法请参见 [设置过滤条件](https://help.aliyun.com/zh/dts/user-guide/use-sql-conditions-to-filter-data-1#concept-610729) 。 如需按库或表级别选择增量迁移的 SQL 操作，请在 已选择对象 中右击待迁移对象，并在弹出的对话框中选择所需增量迁移的 SQL 操作。 |


- 

单击下一步高级配置，进行高级参数配置。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 配置 | 说明 |
| --- | --- |
| 选择调度该任务的专属集群 | DTS 默认将任务调度到共享集群上，您无需选择。若您希望任务更加稳定，可以购买 [专属集群](https://help.aliyun.com/zh/dts/user-guide/what-is-a-dts-dedicated-cluster#concept-2183964) 来运行 DTS 迁移任务。 |
| 源库、目标库无法连接后的重试时间 | 在迁移任务启动后，若源库或目标库连接失败则 DTS 会报错，并会立即进行持续的重试连接，默认重试 720 分钟，您也可以在取值范围（10~1440 分钟）内自定义重试时间，建议设置 30 分钟以上。如果 DTS 在设置的时间内重新连接上源、目标库，迁移任务将自动恢复。否则，迁移任务将失败。 说明 针对同源或者同目标的多个 DTS 实例，网络重试时间以后创建任务的设置为准。 由于连接重试期间，DTS 将收取任务运行费用，建议您根据业务需要自定义重试时间，或者在源和目标库实例释放后尽快释放 DTS 实例。 |
| 源库、目标库出现其他问题后的重试时间 | 在迁移任务启动后，若源库或目标库出现非连接性的其他问题（如 DDL 或 DML 执行异常），则 DTS 会报错并会立即进行持续的重试操作，默认持续重试时间为 10 分钟，您也可以在取值范围（1~1440 分钟）内自定义重试时间，建议设置 10 分钟以上。如果 DTS 在设置的重试时间内相关操作执行成功，迁移任务将自动恢复。否则，迁移任务将会失败。 重要 源库、目标库出现其他问题后的重试时间 的值需要小于 源库、目标库无法连接后的重试时间 的值。 |
| 是否限制全量迁移速率 | 在全量迁移阶段，DTS 将占用源库和目标库一定的读写资源，可能会导致数据库的负载上升。您可以根据实际情况，选择是否对全量迁移任务进行限速设置（设置 每秒查询源库的速率 QPS 、 每秒全量迁移的行数 RPS 和 每秒全量迁移的数据量(MB)BPS ），以缓解目标库的压力。 说明 仅当 迁移类型 选择了 全量迁移 ，才有此配置项。 您也可以在迁移实例运行后， [调整全量迁移的速率](https://help.aliyun.com/zh/dts/user-guide/enable-throttling-for-data-migration) 。 |
| 是否限制增量迁移速率 | 您也可以根据实际情况，选择是否对增量迁移任务进行限速设置（设置 每秒增量迁移的行数 RPS 和 每秒增量迁移的数据量(MB)BPS ），以缓解目标库的压力。 说明 仅当 迁移类型 选择了 增量迁移 ，才有此配置项。 您也可以在迁移实例运行后， [调整增量迁移的速率](https://help.aliyun.com/zh/dts/user-guide/enable-throttling-for-data-migration) 。 |
| 环境标签 | 您可以根据实际情况，选择用于标识实例的环境标签。本示例无需选择。 |
| 实际业务写入编码 | 您可以根据实际情况，选择数据写入目标端的编码类型。 |
| 配置 ETL 功能 | 选择是否配置 ETL 功能。关于 ETL 的更多信息，请参见 [什么是](https://help.aliyun.com/zh/dts/user-guide/what-is-etl#task-2101705) [ETL](https://help.aliyun.com/zh/dts/user-guide/what-is-etl#task-2101705) 。 是 ：配置 ETL 功能，并在文本框中填写数据处理语句，详情请参见 [在](https://help.aliyun.com/zh/dts/user-guide/configure-etl-in-a-data-migration-or-data-synchronization-task#task-2189872) [DTS](https://help.aliyun.com/zh/dts/user-guide/configure-etl-in-a-data-migration-or-data-synchronization-task#task-2189872) [迁移或同步任务中配置](https://help.aliyun.com/zh/dts/user-guide/configure-etl-in-a-data-migration-or-data-synchronization-task#task-2189872) [ETL](https://help.aliyun.com/zh/dts/user-guide/configure-etl-in-a-data-migration-or-data-synchronization-task#task-2189872) 。 否 ：不配置 ETL 功能。 |
| 监控告警 | 根据业务需求选择是否设置告警并接收告警通知。 不设置 ：不设置告警。 设置 ：设置告警。您还需要设置 [告警阈值](https://help.aliyun.com/zh/dts/user-guide/configure-monitoring-and-alerting-1#section-r6s-w5c-kmz) 和 告警联系人 ，当迁移失败或延迟超过阈值后，系统将进行告警通知。 |


- 

单击下一步数据校验，进行数据校验任务配置。

若您需要使用数据校验功能，配置方法请参见[配置数据校验](https://help.aliyun.com/zh/dts/user-guide/enable-data-verification#task-2249288)。

- 

保存任务并进行预检查。

- 

若您需要查看调用API接口配置该实例时的参数信息，请将鼠标光标移动至下一步保存任务并预检查按钮上，然后单击气泡中的预览OpenAPI参数。

- 

若您无需查看或已完成查看API参数，请单击页面下方的下一步保存任务并预检查。

说明

- 

在迁移任务正式启动之前，会先进行预检查。只有预检查通过后，才能成功启动迁移任务。

- 

如果预检查失败，请单击失败检查项后的查看详情，并根据提示修复后重新进行预检查。

- 

如果预检查产生警告：

- 

对于不可以忽略的检查项，请单击失败检查项后的查看详情，并根据提示修复后重新进行预检查。

- 

对于可以忽略无需修复的检查项，您可以依次单击点击确认告警详情、确认屏蔽、确定、重新进行预检查，跳过告警检查项重新进行预检查。如果选择屏蔽告警检查项，可能会导致数据不一致等问题，给业务带来风险。

- 

购买实例。

- 

预检查通过率显示为100%时，单击下一步购买。

- 

在购买页面，选择数据迁移实例的链路规格，详细说明请参见下表。

| 类别 | 参数 | 说明 |
| --- | --- | --- |
| 信息配置 | 资源组配置 | 选择实例所属的资源组，默认为 default resource group 。更多信息，请参见 [什么是资源管理](https://help.aliyun.com/zh/resource-management/product-overview/what-is-resource-management#concept-zyn-3p1-dhb) 。 |
| 链路规格 | DTS 为您提供了不同性能的迁移规格，迁移链路规格的不同会影响迁移速率，您可以根据业务场景进行选择。更多信息，请参见 [数据迁移链路规格说明](https://help.aliyun.com/zh/dts/product-overview/specifications-of-data-migration-instances#concept-26606-zh) 。 |  |


- 

配置完成后，阅读并选中《数据传输（按量付费）服务条款》。

- 

单击购买并启动，并在弹出的确认对话框，单击确定。

您可以在迁移任务列表页面，查看迁移实例的具体进度。

说明

- 

若迁移实例不包含增量迁移任务，则迁移实例会自动结束。迁移实例自动结束后，运行状态为已完成。

- 

若迁移实例包含增量迁移任务，则迁移实例不会自动结束，增量迁移任务会持续进行。在增量迁移任务正常运行期间，迁移实例的运行状态为运行中。

[上一篇：MySQL 5.7、8.0自建数据库全量上云](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[下一篇：从通过专线、VPN网关或智能接入网关接入的自建MySQL迁移至RDS实例](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-connected-over-express-connect-vpn-gateway-or-smart-access-gateway-to-an-apsaradb-rds-for-mysql-instance.md)

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
