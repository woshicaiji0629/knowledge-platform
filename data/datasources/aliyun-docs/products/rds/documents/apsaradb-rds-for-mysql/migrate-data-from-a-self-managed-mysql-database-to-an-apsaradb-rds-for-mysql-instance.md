# 将自建MySQL数据库迁移至RDS MySQL-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance

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

# 从自建MySQL迁移至RDS MySQL实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

数据传输服务DTS（Data Transmission Service）支持在不影响业务正常运行的情况下，将部署在本地、ECS或其他云上的MySQL数据库迁移至RDS MySQL实例。DTS支持库表结构迁移、全量迁移以及增量迁移，同时使用这三种迁移类型可以实现在自建应用不停服的情况下，平滑地完成自建MySQL数据库的迁移上云。

## 前提条件

- 

自建MySQL（源库）数据库版本需为MySQL 5.1、5.5、5.6、5.7、8.0、8.4。

- 

目标RDS实例的可用存储空间需大于自建MySQL数据库中已使用的存储空间。

## 迁移方案概述

DTS提供以下三种迁移类型，在自建数据库迁移至RDS MySQL时，建议您同时配置结构、全量和增量迁移，实现自建应用在不停机的情况下平滑迁移上云。

- 

库表结构迁移：迁移库表结构、视图、触发器、存储过程和函数。

- 

全量迁移：迁移源库中的存量数据。

- 

增量迁移：在全量迁移的基础上，将源库的增量数据迁移到目标库中。

### 常见迁移方案

- 

- 

| 迁移方案 | 业务中断时间 | 数据一致性 | 费用 | 适用场景 |
| --- | --- | --- | --- | --- |
| 结构+全量+增量迁移（推荐） | 不停机（业务不中断） | 无论迁移期间是否有数据写入，迁移完成后（增量迁移无延迟）数据一致。 | 收费 | 生产环境迁移，要求不停机或停机时间最短。 |
| 结构+全量迁移 | 较长（需等待全量迁移完成） | 迁移期间有数据写入：数据不一致。 迁移期间无数据写入：数据一致。 | 免费 | 能容忍长时间停机的业务或测试环境。 |


## 计费说明

使用DTS将自建MySQL迁移至RDS MySQL时，库表结构迁移、全量迁移和公网流量均免费，以下内容收费：

- 

增量迁移：当配置迁移任务时选择了增量迁移，则在增量迁移正常运行期间计费（库表结构迁移和全量迁移运行期间、增量迁移暂停或失败期间均不收费）。

- 

数据校验：当配置迁移任务时选择了数据校验，可能会产生[数据校验费用](https://help.aliyun.com/zh/dts/user-guide/billing-method-of-data-verification#task-2314652)。

## 注意事项

- 

主键限制：所有待迁移的表必须包含主键或唯一约束，且约束内的字段值具有唯一性，否则可能导致目标库出现数据重复。

- 

DDL限制：在库表结构迁移和全量迁移阶段，请勿执行DDL操作（如库表结构变更），否则数据迁移任务会失败。

- 

DML限制：如果仅执行全量迁移任务（无增量迁移），请勿向源实例中写入新的数据，否则会导致源端和目标端数据不一致。

- 

表数量限制：若迁移对象为表级别且需编辑列名映射，单次任务最多支持1000张表。超出此限制时提交任务会报错，请拆分为多个子任务。

- 

字符集限制：若待迁移的数据中包含四字节存储的内容（例如生僻字、表情等信息），则目标端接收数据的数据库和表必须使用utf8mb4字符集。若您使用DTS迁移库表结构，则还需将目标库中实例级别的参数character_set_server设置为utf8mb4。

- 

账号迁移限制：如需将源库账号迁移至目标库，还需满足额外的[账号迁移条件和注意事项](https://help.aliyun.com/zh/dts/user-guide/permissions-for-database-accounts-to-migrate-account-information)。

- 

主备切换限制：如果源库有主备结构且在迁移时发生了主备切换，则会导致迁移失败。

- 

MySQL 8.0隐藏列限制：若源库为MySQL 8.0.23及以上版本，且数据包含不可见的隐藏列（包括无主键表自动生成的隐藏主键），必须先将其设置为可见 (ALTER TABLE ... ALTER COLUMN ... SET VISIBLE;)，否则会导致数据丢失。

- 

不支持迁移以下内容：

- 

使用注释语法定义的解析器（Parser）。

- 

不记录Binlog的操作（如物理备份恢复、外键级联）所产生的数据。

点击展开查看详细注意事项

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
| 源库限制 | 带宽要求：源库所属的服务器需具备足够出口带宽，否则将影响数据迁移速率。 待迁移的表需具备主键或唯一约束，且字段具有唯一性，否则可能会导致目标数据库中出现重复数据。 如迁移对象为表级别，且需进行编辑（如表列名映射），则单次迁移任务仅支持迁移至多 1000 张表。当超出数量限制，任务提交后会显示请求报错，此时建议您拆分待迁移的表，分批配置多个任务，或者配置整库的迁移任务。 如需进行增量迁移，Binlog 日志： 需开启，并且 binlog_format 为 row、binlog_row_image 为 full。否则预检查阶段提示报错，且无法成功启动数据迁移任务。 重要 如源实例自建 MySQL 是双主集群（两者互为主从），为保障 DTS 能获取全部的 Binlog 日志，则您需开启参数 log_slave_updates。 RDS MySQL 实例的本地 Binlog 日志需保留 3 天及以上（建议保留 7 天），自建 MySQL 数据库的本地 Binlog 日志需保留 7 天及以上。否则 DTS 可能会因无法获取 Binlog 而导致任务失败，极端情况下甚至可能会导致数据不一致或数据丢失。由于您所设置的 Binlog 日志保存时间低于 DTS 要求的时间而导致的问题，不在 DTS 的 SLA 保障范围内。 说明 RDS MySQL 实例的本地 Binlog 日志 保留时长 的设置方法，请参见 [自动删除本地日志](products/rds/documents/apsaradb-rds-for-mysql/view-and-delete-the-binary-log-files-of-an-apsaradb-rds-for-mysql-instance.md) 。 源库的操作限制： 在库表结构迁移和全量迁移阶段，请勿执行库或表结构变更的 DDL 操作，否则数据迁移任务会失败。 说明 在全量迁移阶段，DTS 将对源库进行查询，这将产生元数据锁，从而可能阻碍源数据库的 DDL 操作执行。 若仅执行全量数据迁移，请勿向源实例中写入新的数据，否则会导致源和目标数据不一致。为实时保持数据一致性，建议选择结构迁移、全量数据迁移和增量数据迁移。 在迁移实例运行期间，不记录 Binlog 的变更操作所产生的数据（例如通过物理备份功能恢复、级联操作等产生的数据），不会被迁移到目标库。 说明 若有该情况，您可以在业务允许的前提下，重新迁移全量数据。 若源库为 8.0.23 及以后版本的 MySQL 数据库，且待迁移的数据中包含不可见的隐藏列，则可能会因为无法获取该列的数据而导致数据丢失。 说明 您可以使用 ALTER TABLE <table_name> ALTER COLUMN <column_name> SET VISIBLE; 命令，将该隐藏列设置为可见。更多信息，请参见 [Invisible Columns](https://dev.mysql.com/doc/refman/8.0/en/invisible-columns.html) 。 |
| 其他限制 | 建议源和目标库的 MySQL 版本保持一致，以保障兼容性。 若源库有临时表模式的 Online DDL 变更操作（包括但不限于多表合并场景）或对唯一键列添加函数索引，则可能导致目标库数据丢失或迁移实例运行失败。 不支持迁移使用注释语法定义的解析器（Parser）。 若在迁移实例运行时遇到主键或唯一键冲突： 表结构一致的情况下，在目标库遇到与源库主键的值相同的记录： 全量期间，DTS 会保留目标集群中的该条记录，即源库中的该条记录不会迁移至目标数据库中。 增量期间，DTS 不会保留目标集群中的该条记录，即源库中的该条记录会覆盖至目标数据库中。 表结构不一致的情况下，可能导致只能迁移部分列的数据或迁移失败，请谨慎操作。 若目标库为 8.0.23 及以后版本的 MySQL 数据库，且接收数据的列中包含不可见的隐藏列，则可能会因为无法找到写入数据的目标列，导致 DTS 实例运行失败或数据丢失。 说明 您可以使用 ALTER TABLE <table_name> ALTER COLUMN <column_name> SET VISIBLE; 命令，将该隐藏列设置为可见。更多信息，请参见 [Invisible Columns](https://dev.mysql.com/doc/refman/8.0/en/invisible-columns.html) 。 若您迁移数据时未使用 DTS 提供的库表结构迁移，则需要自行确保字段的兼容性，否则可能会导致实例失败或数据丢失。例如，当源表的字段为 text 类型，而接收数据的目标字段的类型为 varchar(255) 时，若源表中存在大字段，则可能会导致数据截断。 若待迁移的数据中包含需要四字节存储的内容（例如生僻字、表情等信息），则目标端接收数据的数据库和表必须使用 utf8mb4 字符集。 说明 若您使用 DTS 迁移库表结构，则需将目标库中实例级别的参数 character_set_server 设置为 utf8mb4。 执行数据迁移前需评估源库和目标库的性能，同时建议业务低峰期执行数据迁移。否则全量数据迁移时 DTS 占用源和目标库一定读写资源，可能会导致数据库的负载上升。 由于全量数据迁移会并发执行 INSERT 操作，导致目标数据库的表产生碎片，因此全量迁移完成后目标数据库的表存储空间会比源实例的表存储空间大。 请确认 DTS 对数据类型为 FLOAT 或 DOUBLE 的列的迁移精度是否符合业务预期。DTS 会通过 ROUND(COLUMN,PRECISION) 来读取这两类列的值。如果没有明确定义其精度，DTS 对 FLOAT 的迁移精度为 38 位，对 DOUBLE 的迁移精度为 308 位。 DTS 会尝试恢复七天之内迁移失败任务。因此，在业务切换至目标实例前，请务必结束或释放该任务，或者使用 revoke 命令回收 DTS 访问目标实例账号的写权限。避免该任务被自动恢复后，源端数据覆盖目标实例的数据。 若目标库的 DDL 写入失败，DTS 任务会继续运行，您需要在任务日志中查看执行失败的 DDL。查看任务日志的方法，请参见 [查询任务日志](https://help.aliyun.com/zh/dts/user-guide/view-task-logs-1) 。 若您将列名仅大小写不同的字段写入到目标 MySQL 数据库的同一个表中，可能会因为 MySQL 数据库列名大小写不敏感，导致迁移结果不符合预期。 在数据迁移完成后（实例的 运行状态 为 已完成 ），建议使用 analyze table <表名> 命令以确认数据均已写入目标表。例如，在目标 MySQL 数据库触发 HA 切换机制后，可能会导致数据只写到了内存，从而造成数据丢失。 若 RDS MySQL 实例已开通全密态（EncDB）功能，则不支持全量数据迁移。 说明 开启透明数据加密 TDE（Transparent Data Encryption）功能的 RDS MySQL 实例支持库表结构迁移、全量数据迁移和增量数据迁移。 若您需要迁移源库中的账号，则还需满足相应的前提条件，并了解相关注意事项。更多信息，请参见 [迁移数据库账号](https://help.aliyun.com/zh/dts/user-guide/permissions-for-database-accounts-to-migrate-account-information) 。 若实例运行失败，DTS 技术支持人员将在 8 小时内尝试恢复该实例。在恢复失败实例的过程中，可能会对该实例进行重启、调整参数等操作。 说明 在调整参数时，仅会修改 DTS 实例的参数，不会对数据库中的参数进行修改。 可能修改的参数，包括但不限于 [修改实例参数](https://help.aliyun.com/zh/dts/user-guide/modify-the-parameters-of-a-dts-instance#section-ys2-2c2-wzo) 中的参数。 |
| 特殊情况 | 当源库为自建 MySQL 时： 迁移时源库进行主备切换，会导致迁移任务失败。 由于 DTS 的延迟时间是根据迁移到目标库最后一条数据的时间戳和当前时间戳对比得出，源库长时间未执行 DML 操作可能导致延迟信息不准确。如果任务显示的延迟时间过大，您可以在源库执行一个 DML 操作来更新延迟信息。 说明 如果迁移对象选择为整库，您还可以创建心跳表，心跳表每秒定期更新或者写入数据。 DTS 会在源库定时执行 CREATE DATABASE IF NOT EXISTS `test` 命令以推进 Binlog 位点。 若源库为 Amazon Aurora MySQL 或其他集群模式的 MySQL 实例，请确保任务配置的域名或 IP 地址及其解析结果为始终为 RW（读写）节点地址，否则可能会导致迁移任务无法正常运行。 当源库为 RDS MySQL 时： 若您需要迁移增量数据，则不记录事务日志的 RDS MySQL 实例（如 RDS MySQL 5.6 版本的只读实例）不支持作为源库。 DTS 会在源库定时执行 CREATE DATABASE IF NOT EXISTS `test` 命令以推进 Binlog 位点。 当目标库为 RDS MySQL 时： DTS 会自动在 RDS MySQL 中创建数据库，如果待迁移的数据库名称不符合 RDS MySQL 的定义规范，您需要在配置迁移任务之前在 RDS MySQL 中创建数据库。相关操作，请参见 [管理数据库](products/rds/documents/apsaradb-rds-for-mysql/create-a-database-for-an-apsaradb-rds-for-mysql-instance.md) 。 |


## 阶段一：准备工作

### 授权DTS访问云资源

- 

使用阿里云账号（主账号）访问[快速授权](https://ram.console.aliyun.com/role/authorization?spm=a2c4g.11186623.0.0.10d26adb3cmjiD&request=%7B%22Services%22%3A%5B%7B%22Service%22%3A%22DTS%22%2C%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunDTSDefaultRole%22%2C%22TemplateId%22%3A%22DefaultRole%22%7D%5D%7D%5D%2C%22ReturnUrl%22%3A%22https%3A%2F%2Fdts.console.aliyun.com%2F%22%7D)页面，单击确认授权。

- 

在执行完授权操作后，如果页面出现提示EntityAlreadyExists.Role和EntityAlreadyExists.Role.Policy，则表明当前阿里云账号已授予DTS访问云资源的权限，您可以继续完成后续准备工作。

### 创建数据库账号并授权

使用DTS进行数据迁移时，源库账号和目标库账号必须具备如下权限：

- 

- 

- 

| 数据库账号 | 库表结构迁移 | 全量迁移 | 增量迁移 |
| --- | --- | --- | --- |
| 自建 MySQL 账号 | SELECT 权限 | 待迁移对象的 SELECT 权限。 REPLICATION CLIENT、REPLICATION SLAVE、SHOW VIEW 权限。 建库建表的权限，以允许 DTS 创建库 test ，用于推进 Binlog 位点。 |  |
| RDS MySQL 账号 | 读写权限 |  |  |


您可以使用已有数据库账号（需具备相关权限）完成迁移任务，也可以通过以下方式分别在源库和目标库创建并授权用于迁移的数据库账号：

## 自建MySQL账号

-- 创建迁移专用账号（dts_user和Your_Password123需修改为您自己的数据库账号和密码） CREATE USER 'dts_user'@'%' IDENTIFIED BY 'Your_Password123'; -- 授予SELECT权限（用于结构迁移、全量迁移） GRANT SELECT ON *.* TO 'dts_user'@'%'; -- 授权增量迁移所需额外权限 GRANT REPLICATION CLIENT, REPLICATION SLAVE, SHOW VIEW ON *.* TO 'dts_user'@'%'; -- 允许DTS创建心跳表，用于推进Binlog位点，监控增量同步延迟 GRANT CREATE ON *.* TO 'dts_user'@'%'; FLUSH PRIVILEGES;

## RDS MySQL账号

建议使用RDS MySQL[高权限账号](products/rds/documents/apsaradb-rds-for-mysql/create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)，您可以通过如下方式创建：

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏单击账号管理，然后单击创建账号。

- 

账号类型选择高权限账号，其他参数（如账号名称和密码）按控制台要求填写。

### 确认源库接入方式并添加白名单

您需要根据自建MySQL数据库类型选择合适的接入方式。同时，若您的自建数据库只允许与特定IP地址建立连接，您需要将DTS服务器的IP地址段加入到相应数据库的安全设置（防火墙、白名单、安全组等）中，以允许DTS服务器的访问。

- 

- 

- 

- 

- 

| 自建数据库类型 | 推荐接入方式 | 白名单与配置 |
| --- | --- | --- |
| 本地自建数据库 （有公网地址） | 公网 IP | 需手动 [添加](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases) [DTS](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases) [服务器](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases) [IP](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases) [地址白名单](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases) 。 |
| 本地自建数据库 （无公网地址） | 云企业网 CEN 数据库网关 DG 专线/VPN 网关/智能网关 | 需手动 [添加](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases) [DTS](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases) [服务器](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases) [IP](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases) [地址白名单](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases) 。 需额外完成对应接入方式的 [配置工作](https://help.aliyun.com/zh/dts/user-guide/preparations/) 。 |
| ECS 自建数据库 | ECS 自建数据库 | 系统自动添加 DTS 服务 IP 地址段。 |


RDS MySQL（目标库）实例的接入方式为云实例，系统会自动添加DTS服务IP地址段进RDS实例白名单中，无需您手动配置。

### （如需增量迁移）配置源库Binlog

如果您需要使用增量迁移，源库Binlog需完成以下配置并重启MySQL使配置生效：

- 

源库需开启本地Binlog日志，且Binlog日志需保留7天及以上。

- 

源库binlog_format参数需设置为row，binlog_row_image参数需设置为full。

- 

如果自建MySQL是双主集群（两者互为主从），为保障DTS能获取全部的Binlog日志，您需开启参数log_slave_updates。

您可以通过以下命令配置源库Binlog：

Linux命令

- 

使用vim命令，修改配置文件my.cnf中的如下参数。

log_bin=mysql_bin binlog_format=row # MySQL 8.0以下版本通过expire_logs_days设置binlog保存时长，默认为0（永不过期） # MySQL 8.0以上版本通过binlog_expire_logs_seconds设置binlog保存时长，默认为2592000秒（30天） # 如果您修改过MySQL中Binlog保留时长且小于7天，可以通过以下参数重新设置Binlog保存时长为7天及以上 # expire_logs_days=7 # binlog_expire_logs_seconds=604800 # 建议设置为大于1的整数 server_id=2 # 当自建MySQL的版本大于5.6时，则必须设置该项。 binlog_row_image=full # 当自建数据库为双主集群时，需打开此参数 # log_slave_updates=ON

- 

修改完成后，重启MySQL进程。

/etc/init.d/mysqld restart

Windows命令

- 

修改配置文件my.ini中的如下参数。

log_bin=mysql_bin binlog_format=row # MySQL 8.0以下版本通过expire_logs_days设置binlog保存时长，默认为0（永不过期） # MySQL 8.0以上版本通过binlog_expire_logs_seconds设置binlog保存时长，默认为2592000秒（30天） # 如果您修改过MySQL中Binlog保留时长且小于7天，可以通过以下参数重新设置Binlog保存时长为7天及以上 # expire_logs_days=7 # binlog_expire_logs_seconds=604800 # 建议设置为大于1的整数 server_id=2 # 当自建MySQL的版本大于5.6时，则必须设置该项。 binlog_row_image=full # 当自建数据库为双主集群时，需打开此参数 # log_slave_updates=ON

- 

修改完成后，重启MySQL服务。 您可以通过Windows中的服务管理器重启服务，或使用如下命令重启服务：

net stop mysql net start mysql

## 阶段二：配置迁移任务

- 

登录[数据传输服务](https://dtsnew.console.aliyun.com/migrate/cn-hangzhou)[DTS](https://dtsnew.console.aliyun.com/migrate/cn-hangzhou)[控制台](https://dtsnew.console.aliyun.com/migrate/cn-hangzhou)，在左侧导航栏选择数据迁移，然后单击创建任务。

- 

配置源库及目标库信息

## 源库配置

- 

- 

| 配置项 | 说明 |
| --- | --- |
| 数据库类型 | 选择 MySQL 。 |
| 接入方式 | 选择准备工作中确认的源库接入方式，本文以本地自建数据库（有公网地址）为例，对应接入方式为 公网 IP 。 |
| 实例地区 | 选择源 MySQL 数据库所属地域。如果源库地域不在可选地域范围内，就近选择即可。 |
| 域名或 IP 地址 | 填入源库外网地址或 IP。如源库地址具有公共 DNS 可解析的域名，推荐优先以域名方式接入。 |
| 端口 | 填入源库的服务端口（需开放至公网），默认为 3306 。 |
| 数据库账号 | 填入准备工作中新建的账号或符合权限要求的已有账号。 |
| 数据库密码 | 填入该数据库账号对应的密码。 |
| 连接方式 | 请根据实际情况选择 非加密连接 或 SSL 安全连接 。 若自建 MySQL 未开启 SSL 加密，请选择 非加密连接 。 若自建 MySQL 已开启 SSL 加密，请选择 SSL 安全连接 。同时，您还需要上传 CA 证书 并填写 CA 证书密码 。 |


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
| 连接方式 | 根据数据库实际情况选择 非加密连接 或 SSL 安全连接 。如果设置为 SSL 安全连接 ，您需要提前开启 RDS MySQL 实例的 SSL 加密功能，详情请参见 [使用云端证书快速开启](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) [SSL](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) [链路加密](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) 。 |


- 

测试源库与目标库连接

在页面下方单击测试连接以进行下一步，并在弹出的DTS服务器访问授权对话框单击测试连接。若测试不通过，请根据错误提示检查网络、账号或权限配置。

- 

配置任务对象

您需要依次完成以下对象配置、高级配置和数据校验配置内容。

## 对象配置

在对象配置页面中，您可以参考下表描述，结合业务实际情况配置迁移类型、待迁移的库表、触发器和事件迁移、目标库大小写策略及已存在表的处理模式等内容。在配置完成后，单击下一步高级配置。

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

| 配置 | 说明 |
| --- | --- |
| 迁移类型 | 如果只需要进行全量迁移，建议同时选中 库表结构迁移 和 全量迁移 。 如果需要进行不停机迁移，建议同时选中 库表结构迁移 、 全量迁移 和 增量迁移 。 说明 若未选中 库表结构迁移 ，请确保目标库中存在接收数据的数据库和表，并根据实际情况，在 已选择对象 框中使用库表列名映射功能。 若未选中 增量迁移 ，为保障数据一致性，数据迁移期间请勿在源实例中写入新的数据。 |
| 源库触发器迁移方式 | 请根据实际情况选择迁移触发器的方式，若您待迁移的对象不涉及触发器，则无需配置。更多信息，请参见 [配置同步或迁移触发器的方式](https://help.aliyun.com/zh/dts/user-guide/synchronize-or-migrate-triggers-from-the-source-database#task-2288139) 。 说明 仅当 迁移类型 同时选择了 库表结构迁移 和 增量迁移 时才可以配置。 |
| 开启迁移评估 | 评估源库和目标库的结构（如索引长度、存储过程、依赖的表等）是否满足要求，您可以根据实际情况选择 是 或者 否 。 说明 仅当 迁移类型 选择了 库表结构迁移 时才可以配置。 若选择 是 ，则可能会增加预检查时间。您可以在预检查阶段查看 评估结果 ，评估结果不影响预检查结果。 |
| 目标已存在表的处理模式 | 预检查并报错拦截 ：检查目标数据库中是否有同名的表。如果目标数据库中没有同名的表，则通过该检查项目；如果目标数据库中有同名的表，则在预检查阶段提示错误，数据迁移任务不会被启动。 说明 如果目标库中同名的表不方便删除或重命名，您可以更改该表在目标库中的名称，请参见 [库表列名映射](https://help.aliyun.com/zh/dts/user-guide/map-object-names#task-2101588) 。 忽略报错并继续执行 ：跳过目标数据库中是否有同名表的检查项。 警告 选择为 忽略报错并继续执行 ，可能导致数据不一致，给业务带来风险，例如： 表结构一致的情况下，在目标库遇到与源库主键的值相同的记录： 全量期间，DTS 会保留目标集群中的该条记录，即源库中的该条记录不会迁移至目标数据库中。 增量期间，DTS 不会保留目标集群中的该条记录，即源库中的该条记录会覆盖至目标数据库中。 表结构不一致的情况下，可能导致只能迁移部分列的数据或迁移失败，请谨慎操作。 |
| 是否迁移 Event | 请根据实际情况选择是否迁移源库中的事件（Event）。若您选择 是 ，则还需遵循相关要求并进行后续操作。更多信息，请参见 [同步或迁移事件](https://help.aliyun.com/zh/dts/user-guide/synchronize-or-migrate-events-from-the-source-database) 。 |
| 目标库对象名称大小写策略 | 您可以配置目标实例中迁移对象的库名、表名和列名的英文大小写策略。默认情况下选择 DTS 默认策略 ，您也可以选择与源库、目标库默认策略保持一致。更多信息，请参见 [目标库对象名称大小写策略](https://help.aliyun.com/zh/dts/user-guide/specify-the-capitalization-of-object-names-in-the-destination-instance-2#concept-2045083) 。 |
| 源库对象 | 在 源库对象 框中选择待迁移对象，然后单击 将其移动至 已选择对象 框。 说明 迁移对象选择的粒度为库、表、列。若选择的迁移对象为表或列，其他对象（如视图、触发器、存储过程）不会被迁移至目标库。 |
| 已选择对象 | 如需更改单个迁移对象在目标实例中的名称，请右击 已选择对象 中的迁移对象，设置方式，请参见 [库表列名单个映射](https://help.aliyun.com/zh/dts/user-guide/map-object-names#section-g21-1wy-98l) 。 如需批量更改迁移对象在目标实例中的名称，请单击 已选择对象 方框右上方的 批量编辑 ，设置方式，请参见 [库表列名批量映射](https://help.aliyun.com/zh/dts/user-guide/map-object-names#section-2wn-exv-fib) 。 说明 如果使用了对象名映射功能，可能会导致依赖这个对象的其他对象迁移失败。 如需设置 WHERE 条件过滤数据，请在 已选择对象 中右击待迁移的表，在弹出的对话框中设置过滤条件。设置方法请参见 [设置过滤条件](https://help.aliyun.com/zh/dts/user-guide/use-sql-conditions-to-filter-data-1#concept-610729) 。 如需按库或表级别选择迁移的 SQL 操作，请在 已选择对象 中右击待迁移对象，并在弹出的对话框中选择所需迁移的 SQL 操作。 |


## 高级配置（可选）

高级配置是基于正常DTS迁移任务上的微调（如断连重试时间、迁移速率限制、监控告警等）及特殊情况的处理（如DTS专属集群、源表Online DDL工具执行过程的临时表）。如无以下高级配置需求，可不修改此页面，保持默认值，单击下一步数据校验。

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

| 配置 | 说明 |
| --- | --- |
| 选择调度该任务的专属集群 | DTS 默认将任务调度到共享集群上，您无需选择。若您希望任务更加稳定，可以购买 [专属集群](https://help.aliyun.com/zh/dts/user-guide/what-is-a-dts-dedicated-cluster#concept-2183964) 来运行 DTS 迁移任务。 |
| 复制源表 Online DDL 工具执行过程的临时表到目标库 | 若源库使用 [数据管理](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582) [DMS（Data Management）](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582) 或 gh-ost 执行 Online DDL 变更，您可以选择是否迁移 Online DDL 变更产生的临时表数据。 重要 DTS 任务暂不支持使用 pt-online-schema-change 等类似工具执行 Online DDL 变更，否则会导致 DTS 任务失败。 各阶段处理方式如下：由于 库表结构迁移 与 全量迁移 阶段不允许执行库或表结构变更的 DDL 操作，因此不受 Online DDL 策略控制。 库表结构迁移 ：不受 Online DDL 策略控制，会创建相关临时表。 全量迁移 ：不受 Online DDL 策略控制，全量迁移对象中将不包括临时表的迁移，凡是表名满足正则表达式（ ^_(.+)_(?:gho|new)$ 或 ^_(.+)_(?:ghc|del|old)$ ）的表都会被过滤。 增量迁移 ：受 Online DDL 策略控制。 是 ：会迁移 Online DDL 操作产生的临时表（例如 _表名_gho ）的数据变更。 否，适配 DMS Online DDL 与 否，适配 gh-ost ：根据正则表达式规则过滤掉 gh-ost 等工具产生的临时表（例如 _表名_gho ）的数据变更。 是 ：迁移 Online DDL 变更产生的临时表数据。 说明 Online DDL 变更产生的临时表数据过大，可能会导致迁移任务延迟。 否，适配 DMS Online DDL ：不迁移 Online DDL 变更产生的临时表数据，只迁移源库使用 [数据管理](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582) [DMS（Data Management）](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582) 执行的原始 DDL 语句。 说明 该方案会导致目标库锁表。 否，适配 gh-ost ：不迁移 Online DDL 变更产生的临时表数据，支持自定义过滤规则。DTS 将根据正则表达式规则过滤掉 gh-ost 等工具产生的临时表（例如 _表名_gho ）的数据变更。您可以根据需要，修改用于匹配影子表和无用表的默认正则表达式： 影子表： ^_(.+)_(?:gho|new)$ 无用表： ^_(.+)_(?:ghc|del|old)$ 说明 该方案会导致目标库锁表。 |
| 是否迁移账号 | 请根据实际情况选择是否迁移源库的账号信息。若您选择迁移 是 ，还需要选择待迁移的账号并确认账号权限。 |
| 源库、目标库无法连接后的重试时间 | 在迁移任务启动后，若源库或目标库连接失败则 DTS 会报错，并会立即进行持续的重试连接，默认重试 720 分钟，您也可以在取值范围（10~1440 分钟）内自定义重试时间，建议设置 30 分钟以上。如果 DTS 在设置的时间内重新连接上源、目标库，迁移任务将自动恢复。否则，迁移任务将失败。 说明 针对同源或者同目标的多个 DTS 实例，网络重试时间以后创建任务的设置为准。 由于连接重试期间，DTS 将收取任务运行费用，建议您根据业务需要自定义重试时间，或者在源和目标库实例释放后尽快释放 DTS 实例。 |
| 源库、目标库出现其他问题后的重试时间 | 在迁移任务启动后，若源库或目标库出现非连接性的其他问题（如 DDL 或 DML 执行异常），则 DTS 会报错并会立即进行持续的重试操作，默认持续重试时间为 10 分钟，您也可以在取值范围（1~1440 分钟）内自定义重试时间，建议设置 10 分钟以上。如果 DTS 在设置的重试时间内相关操作执行成功，迁移任务将自动恢复。否则，迁移任务将会失败。 重要 源库、目标库出现其他问题后的重试时间 的值需要小于 源库、目标库无法连接后的重试时间 的值。 |
| 是否限制全量迁移速率 | 在全量迁移阶段，DTS 将占用源库和目标库一定的读写资源，可能会导致数据库的负载上升。您可以根据实际情况，选择是否对全量迁移任务进行限速设置（设置 每秒查询源库的速率 QPS 、 每秒全量迁移的行数 RPS 和 每秒全量迁移的数据量(MB)BPS ），以缓解目标库的压力。 说明 仅当 迁移类型 选择了 全量迁移 ，才有此配置项。 您也可以在迁移实例运行后， [调整全量迁移的速率](https://help.aliyun.com/zh/dts/user-guide/enable-throttling-for-data-migration) 。 |
| 是否限制增量迁移速率 | 您也可以根据实际情况，选择是否对增量迁移任务进行限速设置（设置 每秒增量迁移的行数 RPS 和 每秒增量迁移的数据量(MB)BPS ），以缓解目标库的压力。 说明 仅当 迁移类型 选择了 增量迁移 ，才有此配置项。 您也可以在迁移实例运行后， [调整增量迁移的速率](https://help.aliyun.com/zh/dts/user-guide/enable-throttling-for-data-migration) 。 |
| 环境标签 | 您可以根据实际情况，选择用于标识实例的环境标签。本示例无需选择。 |
| 是否去除正反向任务的心跳表 SQL | 根据业务需求选择是否在 DTS 实例运行时，在源库中写入心跳 SQL 信息。 是 ：不在源库中写入心跳 SQL 信息，DTS 实例可能会显示有延迟。 否 ：在源库中写入心跳 SQL 信息，可能会影响源库的物理备份和克隆等功能。 |
| 配置 ETL 功能 | 根据业务需求选择是否配置 [ETL](https://help.aliyun.com/zh/dts/user-guide/what-is-etl#task-2101705) [功能](https://help.aliyun.com/zh/dts/user-guide/what-is-etl#task-2101705) ，对数据进行加工处理。 是 ：配置 ETL 功能，您还需要在文本框中输入 [数据处理语句](https://help.aliyun.com/zh/dts/user-guide/configure-etl-in-a-data-migration-or-data-synchronization-task#task-2189872) 。 否 ：不配置 ETL 功能。 |
| 监控告警 | 根据业务需求选择是否设置告警并接收告警通知。 不设置 ：不设置告警。 设置 ：设置告警。您还需要设置 [告警阈值](https://help.aliyun.com/zh/dts/user-guide/configure-monitoring-and-alerting-1#section-r6s-w5c-kmz) 和 告警联系人 ，当迁移失败或延迟超过阈值后，系统将进行告警通知。 |


## 数据校验（可选）

数据校验用于监控源库与目标库数据差异，支持在不停服的情况下对源库和目标库进行校验，帮助您及时发现数据和结构不一致的问题。数据校验类型分为以下三类：

| 数据校验方式 | 费用 | 说明 |
| --- | --- | --- |
| 全量校验 | 收费 | 对全量任务中需要校验的数据进行校验。 |
| 增量校验 | 对增量任务的数据进行校验。 |  |
| 结构校验 | 免费 | 对需要校验的对象进行结构校验。 |


如需使用数据校验功能，可以在配置迁移任务时配置数据校验，也可以在迁移任务完成后单独配置数据校验任务。如无需数据校验，可直接进行后续步骤。

点击展开数据校验配置详情

- 

设置数据校验方式：可根据业务实际需求选择一种或多种数据校验方式。

### 全量校验

若您勾选了全量校验，您还需要设置如下表所示参数。

- 

- 

- 

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 全量校验模式 | 按行抽样进行全字段校验 ：配置抽样百分比，对抽中的数据进行全字段校验，取值为 10~100 的整数。 按表行数进行校验 ：对全量任务数据的行数进行校验，不会对具体的数据内容进行校验。 说明 按表行数进行校验 的全量校验模式不收费； 按行抽样进行全字段校验 的全量校验模式按实际校验数据量收费。 |
| 全量校验时间规则 | 当前仅支持 立即开始 。 |
| 全量校验超时设置 | 不设置 ：全量校验任务超时不会强制结束。 设置 ：设置全量校验任务结束的延迟时间。在全量校验任务启动后开始计时，若校验任务未在指定时间完成则强制结束。取值为 1~72 的整数。 |
| 全量校验基准 | 默认 ：以源库和目标库的合集为基准，校验源库和目标库数据的一致性。 源库 ：以源库为基准，校验目标库与源库数据的一致性（不校验目标库比源库多的数据）。 目标库 ：以目标库为基准，校验源库与目标库数据的一致性（不校验源库比目标库多的数据）。 |
| 全量校验每秒读取的最大数据行数 RPS | 全量数据校验会占用数据库一定的读取资源，您可以根据实际情况对全量校验任务进行限速设置（每秒读取的数据行数和数据量），以缓解数据库的压力。 说明 参数值为 0 时表示无限制，当 全量校验每秒读取的最大数据行数 RPS 和 全量校验每秒读取的最大数据量 MBps 均为 0 时，表示不限速。 |
| 全量校验每秒读取的最大数据量 MBps |  |


### 增量校验

若您勾选了增量校验，您还需要设置如下表所示参数。

| 参数 | 说明 |
| --- | --- |
| 增量校验基准 | 您可以根据实际情况，筛选需要校验的 DML 操作。 |


- 

设置校验对象。

您可以在已选择对象框中勾选不需要进行数据校验的对象，然后单击进行移除。

说明

DTS默认已将待同步或迁移的对象移动至已选择对象框。

- 

配置校验告警。

根据业务需求，选择配置如下表所示参数。

说明

您也可以在DTS实例运行后，[设置或修改数据校验告警](https://help.aliyun.com/zh/dts/user-guide/configure-monitoring-and-alerting-1#section-zli-j1g-nrn)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 全量校验告警 | 不设置 ：不设置告警。 设置 ：设置告警，您还需要选择和配置告警规则。告警规则如下： 当全量校验任务失败时触发告警。 设置数据不一致的阈值，当全量校验任务不一致数据大于等于设置的阈值时触发告警。 |
| 增量校验告警 | 不设置 ：不设置告警。 设置 ：设置告警，您还需要选择和配置告警规则。告警规则如下： 当增量校验任务失败时触发告警。 设置数据不一致的周期数、统计周期和不一致数量阈值，当增量校验任务累计在设置的若干个周期，数据不一致记录量均大于等于设置的阈值时触发告警。 设置数据延迟的周期数、统计周期和延迟时间阈值，当增量校验任务累计在设置的若干个周期，延迟均大于等于设置的阈值时触发告警。 |


说明

若您设置了校验告警，您还需要输入告警联系人的手机号码。当校验任务触发告警时，将以短信的形式通知告警联系人。

## 阶段三：预检查与启动

- 

在完成阶段二的配置后，单击下一步保存任务并预检查。DTS将检查源库和目标库的环境、权限、配置等是否满足迁移要求。

- 

等待预检查完成。

- 

预检查通过率显示为100%：则说明环境已准备就绪，可以进行后续购买和启动。

- 

预检查失败或出现不可忽略的警告：请单击失败检查项后的查看详情，并根据提示修复后重新进行预检查。

- 

出现可忽略的警告项：请仔细阅读警告内容，确认无相关风险后（如数据不一致等问题）可选择忽略。

- 

预检查完全通过后，单击下一步购买。

- 

选择资源组配置（默认为default resource group）和合适的链路规格（规格越高，迁移速度越快）。

- 

阅读并选中《数据传输（按量付费）服务条款》，单击购买并启动，并在弹出的确认对话框，单击确定，任务将自动开始执行。

## 阶段四：数据验证与业务切换

- 

等待DTS迁移任务完成

- 

未包含增量迁移的任务：在全量迁移完成后自动结束，任务运行状态变为已完成。

- 

包含增量迁移的任务：任务不会自动结束，增量迁移会持续进行（任务运行状态为运行中）。当增量迁移显示无延迟时，表示源库与目标库数据一致，可以进行数据验证。

- 

数据验证

当迁移任务结束或增量迁移无延迟（低延迟）时，可以进行源库和目标库的数据验证：

- 

自动校验：在DTS中[配置数据校验任务](https://help.aliyun.com/zh/dts/user-guide/enable-data-verification#task-2249288)，自动对比源库和目标库的数据。

- 

手动抽样校验：您可以从多种维度手动校验数据（如对比源库和目标库的表行数、核心业务数据等），抽样验证数据一致性。以下为示例代码：

-- 示例1：在源库和目标库分别执行，对比表行数 SELECT COUNT(*) FROM your_table; -- 示例2：在源库和目标库分别执行，对比关键业务指标，如某时间段内的订单总金额 SELECT SUM(amount) FROM orders WHERE create_time >= '2024-01-01';

- 

业务切换

数据验证完成后，建议您选择业务低峰期，将应用服务内的自建数据库连接地址修改为[RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/view-and-change-the-internal-and-public-endpoints-and-port-numbers-of-an-apsaradb-rds-for-mysql-instance.md)[实例的连接地址](products/rds/documents/apsaradb-rds-for-mysql/view-and-change-the-internal-and-public-endpoints-and-port-numbers-of-an-apsaradb-rds-for-mysql-instance.md)，完成业务切换。如果DTS迁移任务中包含增量迁移，请在切换完成后及时释放该任务，避免迁移任务持续计费。

## 附录1：迁移类型说明

- 

- 

- 

| 迁移类型 | 说明 |
| --- | --- |
| 库表结构迁移 | 将源库中待迁移对象的结构定义迁移到目标库： 当前仅支持表、视图、触发器、存储过程和函数的迁移，且迁移过程中不会修改视图的 select_statement 、存储过程的 routine_body 和函数的 routine_body 。 在迁移结构时，DTS 会将待迁移视图、存储过程和函数中的 DEFINER 转换为 INVOKER （即将安全验证方式 SQL SECURITY 的值转换为 INVOKER ），并将 DEFINER 设置为迁移任务中使用的目标库账号，不会修改源库的安全验证方式和 DEFINER 。 由于 DTS 不迁移 USER 信息，因此在调用目标库的视图、存储过程和函数时，需要对调用者授予读写权限。 |
| 全量迁移 | 将源库中待迁移对象的存量数据，全部迁移到目标库中。 |
| 增量迁移 | 在全量迁移的基础上，将源库的增量更新数据迁移到目标库中。通过增量数据迁移可以实现在自建应用不停机的情况下，平滑地完成数据迁移。 |


## 附录2：增量迁移时支持的SQL操作

- 

- 

- 

- 

- 

| 操作类型 | SQL 操作语句 |
| --- | --- |
| DML | INSERT、UPDATE、DELETE |
| DDL | ALTER TABLE、ALTER VIEW CREATE FUNCTION、CREATE INDEX、CREATE PROCEDURE、CREATE TABLE、CREATE VIEW DROP INDEX、DROP TABLE RENAME TABLE 重要 RENAME TABLE 操作可能导致迁移数据不一致。例如迁移对象只包含某个表，如果迁移过程中源实例对该表执行了重命名操作，那么该表的数据将不会迁移到目标库。为避免该问题，您可以在数据迁移配置时将该表所属的整个数据库作为迁移对象，且确保 RENAME TABLE 操作前后的表所属的数据库均在迁移对象中。 TRUNCATE TABLE |


## 常见问题

- 

Q1：测试连接报错“JDBC: [conn_error, cause: null, message from server: "Host 'XXX' is not allowed to connect to this MySQL server"]; PING: []; TELNET: []; requestId=[XXX]”

该报错为JDBC异常，请您检查JDBC的账号、密码及权限问题，或使用高权限账号测试连接。

- 

Q2：创建迁移任务，为什么无法选择福州地域的RDS实例？

目前DTS不支持福州地域的实例。您可以将[MySQL 5.7、8.0](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[自建数据库备份上云](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)。

[上一篇：从自建数据库迁移至RDS](products/rds/documents/apsaradb-rds-for-mysql/data-migration-from-a-user-created-database-to-an-apsaradb-rds-mysql-instance.md)[下一篇：MySQL 5.7、8.0自建数据库全量上云](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)

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
