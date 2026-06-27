# 使用DTS将自建MariaDB不停机迁移至RDS MariaDB-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mariadb/use-dts-to-migrate-the-data-of-a-self-managed-mariadb-database-to-the-cloud

# 使用DTS将自建MariaDB数据库迁移上云
本文介绍如何使用数据传输服务DTS（Data Transmission Service），将自建MariaDB迁移至RDS MariaDB实例。DTS支持结构迁移、全量数据迁移以及增量数据迁移，同时使用这三种迁移类型可以实现在自建应用不停服的情况下，平滑地完成自建MariaDB数据库的迁移上云。
## 前提条件
已创建目标RDS MariaDB实例，创建方式，请参见[快速创建](create-an-apsaradb-rds-for-mariadb-instance.md)[RDS MariaDB](create-an-apsaradb-rds-for-mariadb-instance.md)[实例](create-an-apsaradb-rds-for-mariadb-instance.md)。
目标RDS MariaDB实例的存储空间须大于源自建MariaDB实例占用的存储空间。
## 注意事项
说明
在库表结构迁移过程中，DTS会将源数据库中的外键迁移到目标数据库。
在全量迁移和增量迁移过程中，DTS会以Session级别暂时禁用约束检查以及外键级联操作。若任务运行时源库存在级联更新、删除操作，可能会导致数据不一致。
| 类型 | 说明 |
| --- | --- |
| 源库限制 | 带宽要求：源库所属的服务器需具备足够出口带宽，否则将影响数据迁移速率。 待迁移的表需具备主键或唯一约束，且字段具有唯一性，否则可能会导致目标数据库中出现重复数据。 若迁移对象为表级别，且需进行编辑（如表列名映射），则当单次迁移任务的表数量超过 1000 张时，建议您将待迁移的表分批配置为多个迁移实例，或将其配置为整库的迁移实例。 如需进行增量迁移，数据日志： 需开启 Binlog，并且设置 binlog_row_image 为 full，否则预检查阶段提示报错，且无法成功启动数据迁移任务。 DTS 要求源数据库的数据日志至少保留 7 天以上，否则 DTS 可能因无法获取数据日志而导致任务失败，极端情况下甚至可能会导致数据不一致或丢失。由于您所设置的数据日志保存时间低于 DTS 要求的时间进而导致的问题，不在 DTS 的 SLA 保障范围内。 源库的操作限制： 在全量迁移阶段，请勿执行库或表结构变更的 DDL 操作，否则数据迁移任务会失败。 如仅执行全量数据迁移，请勿向源实例中写入新的数据，否则会导致源和目标数据不一致。为实时保持数据一致性，建议选择全量数据迁移和增量数据迁移。 |
| 其他限制 | 请确保源库待迁移的数据和目标库接收数据的列中均无不可见的隐藏列，否则可能会导致 DTS 实例运行失败或数据丢失。 在全量迁移任务运行时，DTS 将会占用源和目标库一定的读写资源，可能会导致数据库的负载上升。因此建议您在迁移实例运行前评估源库和目标库的性能，并在业务低峰期运行实例（例如源库和目标库的 CPU 负载在 30%以下）。 由于全量数据迁移会并发执行 INSERT 操作，导致目标数据库的表产生碎片，因此全量迁移完成后目标数据库的表存储空间会比源实例的表存储空间大。 在 DTS 迁移期间，若目标库存在非来自 DTS 的数据写入，则可能会导致源库与目标库的数据不一致，甚至会导致迁移实例运行失败。您可以在 DTS 迁移结束后，使用数据管理 DMS（Data Management）来执行在线 DDL 变更，详情请参见 [通过无锁变更工单实现无锁结构变更](https://help.aliyun.com/zh/dms/perform-lock-free-ddl-operations#multiTask4072) 。 若目标库的 DDL 写入失败，DTS 任务会继续运行，您需要在任务日志中查看执行失败的 DDL。查看任务日志的方法，请参见 [查询任务日志](https://help.aliyun.com/zh/dts/user-guide/view-task-logs-1) 。 若实例运行失败，DTS 技术支持人员将在 8 小时内尝试恢复该实例。在恢复失败实例的过程中，可能会对该实例进行重启、调整参数等操作。 说明 在调整参数时，仅会修改实例的参数，不会对数据库中的参数进行修改。 可能修改的参数，包括但不限于 [修改实例参数](https://help.aliyun.com/zh/dts/user-guide/modify-the-parameters-of-a-dts-instance#section-ys2-2c2-wzo) 中的参数。 |
| 特殊情况 | 由于源库 MariaDB 为自建数据库，您还需要注意如下事项： 若源库在迁移时进行主备切换，会导致迁移任务失败。 由于 DTS 的延迟时间是通过对比迁移到目标库最后一条数据的时间戳和当前时间戳得出，源库长时间未执行 DML 操作可能导致延迟信息不准确。如果任务显示的延迟时间过大，您可以在源库执行一个 DML 操作来更新延迟信息。 |
## 费用说明
| 迁移类型 | 链路配置费用 | 公网流量费用 |
| --- | --- | --- |
| 结构迁移和全量数据迁移 | 不收费。 | 本示例不收费。 |
| 增量数据迁移 | 收费，详情请参见 [计费概述](https://help.aliyun.com/zh/dts/product-overview/billing-overview#concept-261679) 。 |  |
## 迁移类型说明
库表结构迁移
DTS将源库中迁移对象的结构定义迁移到目标库。
目前DTS支持结构迁移的对象为表、视图、触发器、存储过程和函数。
说明
不会修改存储过程的routine_body、函数的routine_body、视图的select_statement。
在库表结构迁移时，DTS会将待迁移视图、存储过程和函数中的DEFINER转换为INVOKER（即将安全验证方式SQL SECURITY的值转换为INVOKER），并将定义者（DEFINER）设置为迁移任务中使用的目标库账号。
说明
不会修改源库的安全验证方式和定义者。
由于DTS不迁移USER信息，因此在调用目标库的视图、存储过程和函数时，需要对调用者授予读写权限。
全量迁移
DTS将源库中迁移对象的存量数据，全部迁移到目标库中。
增量迁移
DTS在全量迁移的基础上，将源库的增量更新数据迁移到目标库中。通过增量数据迁移可以实现在自建应用不停机的情况下，平滑地完成数据迁移。
## 支持增量迁移的SQL操作
| 操作类型 | SQL 操作语句 |
| --- | --- |
| DML | INSERT、UPDATE、DELETE |
| DDL | ALTER TABLE、ALTER VIEW CREATE FUNCTION、CREATE INDEX、CREATE PROCEDURE、CREATE TABLE、CREATE VIEW DROP INDEX、DROP TABLE RENAME TABLE 重要 RENAME TABLE 操作可能导致迁移数据不一致。例如迁移对象只包含某个表，如果迁移过程中源实例对该表执行了重命名操作，那么该表的数据将不会迁移到目标库。为避免该问题，您可以在数据迁移配置时将该表所属的整个数据库作为迁移对象，且确保 RENAME TABLE 操作前后的表所属的数据库均在迁移对象中。 TRUNCATE TABLE |
## 数据库账号的权限要求
| 数据库 | 库表结构迁移 | 全量迁移 | 增量迁移 |
| --- | --- | --- | --- |
| 自建 MariaDB 数据库 | SELECT 权限 | SELECT 权限 | 增量数据迁移：待迁移对象的 SELECT 权限 REPLICATION CLIENT、REPLICATION SLAVE、SHOW VIEW 建库建表的权限，以允许 DTS 创建库 test ，用于记录迁移期间的心跳数据 |
| RDS MariaDB 实例 | 读写权限 |  |  |
数据库账号创建及授权方法：
自建MariaDB实例请参见[创建账号](https://mariadb.com/kb/zh-cn/create-user/)和[账号授权](https://mariadb.com/kb/zh-cn/grant/)。
RDS MariaDB实例请参见[创建账号](create-an-account-on-an-apsaradb-rds-for-mariadb-instance.md)和[修改或重置账号权限](modify-the-permissions-of-a-standard-account-on-an-apsaradb-rds-for-mariadb-instance.md)。
## 操作步骤
进入目标地域的迁移任务列表页面（二选一）。
### 通过DTS控制台进入
登录[数据传输服务](https://dtsnew.console.aliyun.com/)[DTS](https://dtsnew.console.aliyun.com/)[控制台](https://dtsnew.console.aliyun.com/)。
在左侧导航栏，单击数据迁移。
在页面左上角，选择迁移实例所属地域。
### 通过DMS控制台进入
说明
实际操作可能会因DMS的模式和布局不同，而有所差异。更多信息。请参见[极简模式控制台](https://help.aliyun.com/zh/dms/simple-mode#concept-2103267)和[自定义](https://help.aliyun.com/zh/dms/configure-the-dms-console-based-on-your-business-requirements#task-2134256)[DMS](https://help.aliyun.com/zh/dms/configure-the-dms-console-based-on-your-business-requirements#task-2134256)[界面布局与样式](https://help.aliyun.com/zh/dms/configure-the-dms-console-based-on-your-business-requirements#task-2134256)。
登录[DMS](https://dms.aliyun.com/new)[数据管理服务](https://dms.aliyun.com/new)。
在顶部菜单栏中，选择Data + AI>数据传输（DTS）>数据迁移。
在迁移任务右侧，选择迁移实例所属地域。
单击创建任务，进入任务配置页面。
可选：在页面右上角，单击试用新版配置页。
说明
若您已进入新版配置页（页面右上角的按钮为返回旧版配置页），则无需执行此操作。
新版配置页和旧版配置页部分参数有差异，建议使用新版配置页。
配置源库及目标库信息。
警告
选择源和目标实例后，建议您仔细阅读页面上方显示的使用限制，否则可能会导致任务失败或数据不一致。
| 类别 | 配置 | 说明 |
| --- | --- | --- |
| 无 | 任务名称 | DTS 会自动生成一个任务名称，建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| 源库信息 | 选择已有连接信息 | 您可以按实际需求，选择是否使用已有数据库实例。 如使用已有实例，下方数据库信息将自动填入，您无需重复输入。 如不使用已有实例，您需要配置下方的数据库信息。 说明 您可以在 数据连接管理 页面或新版配置页面，将数据库录入 DTS。更多信息，请参见 [数据连接管理](https://help.aliyun.com/zh/dts/user-guide/database-connection-management) 。 DMS 控制台的配置项为 选择 DMS 数据库实例 ，您可以单击 新增 DMS 数据库实例 或在控制台首页将数据库录入 DMS。更多信息，请参见 [云数据库录入](https://help.aliyun.com/zh/dms/register-an-apsaradb-instance-1) 和 [他云/自建数据库录入](https://help.aliyun.com/zh/dms/register-a-database-hosted-on-a-third-party-cloud-service-or-a-self-managed-database) 。 |
| 数据库类型 | 选择 Mariadb 。 |  |
| 接入方式 | 根据源库的部署位置进行选择，本文以 ECS 自建数据库 为例介绍配置流程。 |  |
| 实例地区 | 选择源 MariaDB 数据库所属地域。 |  |
| ECS 实例 ID | 选择目标 ECS 实例 ID。 |  |
| 端口 | 填入源 MariaDB 数据库的服务端口（需开放至公网），默认为 3306 。 |  |
| 数据库账号 | 填入源 MariaDB 数据库的账号，权限要求请参见 [数据库账号的权限要求](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-the-user-created-mariadb-to-rds-mariadb#section-rd0-uc3-3i5) 。 |  |
| 数据库密码 | 填入该数据库账号对应的密码。 |  |
| 连接方式 | 选择 非加密连接 。 |  |
| 目标库信息 | 选择已有连接信息 | 您可以按实际需求，选择是否使用已有数据库实例。 如使用已有实例，下方数据库信息将自动填入，您无需重复输入。 如不使用已有实例，您需要配置下方的数据库信息。 说明 您可以在 数据连接管理 页面或新版配置页面，将数据库录入 DTS。更多信息，请参见 [数据连接管理](https://help.aliyun.com/zh/dts/user-guide/database-connection-management) 。 DMS 控制台的配置项为 选择 DMS 数据库实例 ，您可以单击 新增 DMS 数据库实例 或在控制台首页将数据库录入 DMS。更多信息，请参见 [云数据库录入](https://help.aliyun.com/zh/dms/register-an-apsaradb-instance-1) 和 [他云/自建数据库录入](https://help.aliyun.com/zh/dms/register-a-database-hosted-on-a-third-party-cloud-service-or-a-self-managed-database) 。 |
| 数据库类型 | 选择 Mariadb 。 |  |
| 接入方式 | 选择 云实例 。 |  |
| 实例地区 | 选择目标 RDS MariaDB 实例所属地域。 |  |
| RDS 实例 ID | 选择目标 RDS MariaDB 实例 ID。 |  |
| 数据库账号 | 填入目标 RDS 实例的数据库账号，权限要求请参见 [数据库账号的权限要求](https://help.aliyun.com/zh/dts/user-guide/migrate-data-from-the-user-created-mariadb-to-rds-mariadb#section-rd0-uc3-3i5) 。 |  |
| 数据库密码 | 填入该数据库账号对应的密码。 |  |
| 连接方式 | 选择 非加密连接 。 |  |
配置完成后，在页面下方单击测试连接以进行下一步。
说明
请确保DTS服务的IP地址段能够被自动或手动添加至源库和目标库的安全设置中，以允许DTS服务器的访问。更多信息，请参见[添加](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[DTS](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[服务器的](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[IP](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[地址段](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)。
若源库或目标库为自建数据库（接入方式不是云实例），则还需要在弹出的DTS服务器访问授权对话框单击测试连接。
配置任务对象。
在对象配置页面，配置待迁移的对象。
| 配置 | 说明 |
| --- | --- |
| 迁移类型 | 如果只需要进行全量迁移，建议同时选中 库表结构迁移 和 全量迁移 。 如果需要进行不停机迁移，建议同时选中 库表结构迁移 、 全量迁移 和 增量迁移 。 说明 若未选中 库表结构迁移 ，请确保目标库中存在接收数据的数据库和表，并根据实际情况，在 已选择对象 框中使用库表列名映射功能。 若未选中 增量迁移 ，为保障数据一致性，数据迁移期间请勿在源实例中写入新的数据。 |
| 源库触发器迁移方式 | 请根据实际情况选择迁移触发器的方式，若您待迁移的对象不涉及触发器，则无需配置。更多信息，请参见 [配置同步或迁移触发器的方式](https://help.aliyun.com/zh/dts/user-guide/synchronize-or-migrate-triggers-from-the-source-database#task-2288139) 。 说明 仅当 迁移类型 同时选择了 库表结构迁移 和 增量迁移 时才可以配置。 |
| 目标已存在表的处理模式 | 预检查并报错拦截 ：检查目标数据库中是否有同名的表。如果目标数据库中没有同名的表，则通过该检查项目；如果目标数据库中有同名的表，则在预检查阶段提示错误，数据迁移任务不会被启动。 说明 如果目标库中同名的表不方便删除或重命名，您可以更改该表在目标库中的名称，请参见 [库表列名映射](https://help.aliyun.com/zh/dts/user-guide/map-object-names#task-2101588) 。 忽略报错并继续执行 ：跳过目标数据库中是否有同名表的检查项。 警告 选择为 忽略报错并继续执行 ，可能导致数据不一致，给业务带来风险，例如： 表结构一致的情况下，在目标库遇到与源库主键的值相同的记录： 全量期间，DTS 会保留目标集群中的该条记录，即源库中的该条记录不会迁移至目标数据库中。 增量期间，DTS 不会保留目标集群中的该条记录，即源库中的该条记录会覆盖至目标数据库中。 表结构不一致的情况下，可能导致只能迁移部分列的数据或迁移失败，请谨慎操作。 |
| 目标库对象名称大小写策略 | 您可以配置目标实例中迁移对象的库名、表名和列名的英文大小写策略。默认情况下选择 DTS 默认策略 ，您也可以选择与源库、目标库默认策略保持一致。更多信息，请参见 [目标库对象名称大小写策略](https://help.aliyun.com/zh/dts/user-guide/specify-the-capitalization-of-object-names-in-the-destination-instance-2#concept-2045083) 。 |
| 源库对象 | 在 源库对象 框中选择待迁移对象，然后单击 将其移动至 已选择对象 框。 说明 迁移对象选择的粒度为库、表、列。若选择的迁移对象为表或列，其他对象（如视图、触发器、存储过程）不会被迁移至目标库。 |
| 已选择对象 | 如需更改单个迁移对象在目标实例中的名称，请右击 已选择对象 中的迁移对象，设置方式，请参见 [库表列名单个映射](https://help.aliyun.com/zh/dts/user-guide/map-object-names#section-g21-1wy-98l) 。 如需批量更改迁移对象在目标实例中的名称，请单击 已选择对象 方框右上方的 批量编辑 ，设置方式，请参见 [库表列名批量映射](https://help.aliyun.com/zh/dts/user-guide/map-object-names#section-2wn-exv-fib) 。 说明 如果使用了对象名映射功能，可能会导致依赖这个对象的其他对象迁移失败。 如需设置 WHERE 条件过滤数据，请在 已选择对象 中右击待迁移的表，在弹出的对话框中设置过滤条件。设置方法请参见 [设置过滤条件](https://help.aliyun.com/zh/dts/user-guide/use-sql-conditions-to-filter-data-1#concept-610729) 。 如需按库或表级别选择迁移的 SQL 操作，请在 已选择对象 中右击待迁移对象，并在弹出的对话框中选择所需迁移的 SQL 操作。 |
单击下一步高级配置，进行高级参数配置。
| 配置 | 说明 |
| --- | --- |
| 选择调度该任务的专属集群 | DTS 默认将任务调度到共享集群上，您无需选择。若您希望任务更加稳定，可以购买专属集群来运行 DTS 迁移任务。更多信息，请参见 [什么是](https://help.aliyun.com/zh/dts/user-guide/what-is-a-dts-dedicated-cluster#concept-2183964) [DTS](https://help.aliyun.com/zh/dts/user-guide/what-is-a-dts-dedicated-cluster#concept-2183964) [专属集群](https://help.aliyun.com/zh/dts/user-guide/what-is-a-dts-dedicated-cluster#concept-2183964) 。 |
| 源库、目标库无法连接后的重试时间 | 在迁移任务启动后，若源库或目标库连接失败则 DTS 会报错，并会立即进行持续的重试连接，默认重试 720 分钟，您也可以在取值范围（10~1440 分钟）内自定义重试时间，建议设置 30 分钟以上。如果 DTS 在设置的时间内重新连接上源、目标库，迁移任务将自动恢复。否则，迁移任务将失败。 说明 针对同源或者同目标的多个 DTS 实例，网络重试时间以后创建任务的设置为准。 由于连接重试期间，DTS 将收取任务运行费用，建议您根据业务需要自定义重试时间，或者在源和目标库实例释放后尽快释放 DTS 实例。 |
| 源库、目标库出现其他问题后的重试时间 | 在迁移任务启动后，若源库或目标库出现非连接性的其他问题（如 DDL 或 DML 执行异常），则 DTS 会报错并会立即进行持续的重试操作，默认持续重试时间为 10 分钟，您也可以在取值范围（1~1440 分钟）内自定义重试时间，建议设置 10 分钟以上。如果 DTS 在设置的重试时间内相关操作执行成功，迁移任务将自动恢复。否则，迁移任务将会失败。 重要 源库、目标库出现其他问题后的重试时间 的值需要小于 源库、目标库无法连接后的重试时间 的值。 |
| 是否限制全量迁移速率 | 在全量迁移阶段，DTS 将占用源库和目标库一定的读写资源，可能会导致数据库的负载上升。您可以根据实际情况，选择是否对全量迁移任务进行限速设置（设置 每秒查询源库的速率 QPS 、 每秒全量迁移的行数 RPS 和 每秒全量迁移的数据量(MB)BPS ），以缓解目标库的压力。 说明 仅当 迁移类型 选择了 全量迁移 时才可以配置。 |
| 是否限制增量迁移速率 | 您也可以根据实际情况，选择是否对增量迁移任务进行限速设置（设置 每秒增量迁移的行数 RPS 和 每秒增量迁移的数据量(MB)BPS ），以缓解目标库的压力。 说明 仅当 迁移类型 选择了 增量迁移 时才可以配置。 |
| 环境标签 | 您可以根据实际情况，选择用于标识实例的环境标签。本示例无需选择。 |
| 配置 ETL 功能 | 选择是否配置 ETL 功能。关于 ETL 的更多信息，请参见 [什么是](https://help.aliyun.com/zh/dts/user-guide/what-is-etl#task-2101705) [ETL](https://help.aliyun.com/zh/dts/user-guide/what-is-etl#task-2101705) 。 是 ：配置 ETL 功能，并在文本框中填写数据处理语句，详情请参见 [在](https://help.aliyun.com/zh/dts/user-guide/configure-etl-in-a-data-migration-or-data-synchronization-task#task-2189872) [DTS](https://help.aliyun.com/zh/dts/user-guide/configure-etl-in-a-data-migration-or-data-synchronization-task#task-2189872) [迁移或同步任务中配置](https://help.aliyun.com/zh/dts/user-guide/configure-etl-in-a-data-migration-or-data-synchronization-task#task-2189872) [ETL](https://help.aliyun.com/zh/dts/user-guide/configure-etl-in-a-data-migration-or-data-synchronization-task#task-2189872) 。 否 ：不配置 ETL 功能。 |
| 监控告警 | 是否设置告警，当迁移失败或延迟超过阈值后，将通知告警联系人。 不设置 ：不设置告警。 设置 ：设置告警，您还需要设置告警阈值和 告警联系人 。更多信息，请参见 [在配置任务过程中配置监控告警](https://help.aliyun.com/zh/dts/user-guide/configure-monitoring-and-alerting-1#section-r6s-w5c-kmz) 。 |
保存任务并进行预检查。
若您需要查看调用API接口配置该实例时的参数信息，请将鼠标光标移动至下一步保存任务并预检查按钮上，然后单击气泡中的预览OpenAPI参数。
若您无需查看或已完成查看API参数，请单击页面下方的下一步保存任务并预检查。
说明
在迁移任务正式启动之前，会先进行预检查。只有预检查通过后，才能成功启动迁移任务。
如果预检查失败，请单击失败检查项后的查看详情，并根据提示修复后重新进行预检查。
如果预检查产生警告：
对于不可以忽略的检查项，请单击失败检查项后的查看详情，并根据提示修复后重新进行预检查。
对于可以忽略无需修复的检查项，您可以依次单击点击确认告警详情、确认屏蔽、确定、重新进行预检查，跳过告警检查项重新进行预检查。如果选择屏蔽告警检查项，可能会导致数据不一致等问题，给业务带来风险。
购买实例。
预检查通过率显示为100%时，单击下一步购买。
在购买页面，选择数据迁移实例的链路规格，详细说明请参见下表。
| 类别 | 参数 | 说明 |
| --- | --- | --- |
| 信息配置 | 资源组配置 | 选择实例所属的资源组，默认为 default resource group 。更多信息，请参见 [什么是资源管理](https://help.aliyun.com/zh/resource-management/product-overview/what-is-resource-management#concept-zyn-3p1-dhb) 。 |
| 链路规格 | DTS 为您提供了不同性能的迁移规格，迁移链路规格的不同会影响迁移速率，您可以根据业务场景进行选择。更多信息，请参见 [数据迁移链路规格说明](https://help.aliyun.com/zh/dts/product-overview/specifications-of-data-migration-instances#concept-26606-zh) 。 |  |
配置完成后，阅读并选中《数据传输（按量付费）服务条款》。
单击购买并启动，并在弹出的确认对话框，单击确定。
您可在数据迁移界面查看具体进度。
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
