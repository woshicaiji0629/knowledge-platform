# 使用DTS将RDS MariaDB数据迁移至RDS MySQL-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mariadb/migrate-data-from-an-apsaradb-rds-for-mariadb-instance-to-an-apsaradb-rds-for-mysql-instance

# 从RDS MariaDB迁移至RDS MySQL
本文介绍如何使用数据传输服务DTS（Data Transmission Service），将RDS MariaDB迁移至RDS MySQL。DTS支持结构迁移、全量数据迁移以及增量数据迁移，同时使用这三种迁移类型可以实现在自建应用不停服的情况下，平滑地完成数据库的迁移。
## 前提条件
已创建目标RDS MySQL实例，详情请参见[创建](../create-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](../create-an-apsaradb-rds-for-mysql-instance.md)[实例](../create-an-apsaradb-rds-for-mysql-instance.md)。
说明
RDS MySQL实例的存储空间须大于RDS MariaDB实例中数据库已占用的存储空间。
## 注意事项
DTS在执行全量数据迁移时将占用源库和目标库一定的读写资源，可能会导致数据库的负载上升，在数据库性能较差、规格较低或业务量较大的情况下（例如源库有大量慢SQL、存在无主键表或目标库存在死锁等），可能会加重数据库压力，甚至导致数据库服务不可用。因此您需要在执行数据迁移前评估源库和目标库的性能，同时建议您在业务低峰期执行数据迁移（例如源库和目标库的CPU负载在30%以下）。
如果源库中待迁移的表没有主键或唯一约束，且所有字段没有唯一性，可能会导致目标数据库中出现重复数据。
对于迁移失败的任务，DTS会触发自动恢复。当您需要将业务切换至目标实例，请务必先结束或释放迁移任务，避免该任务被自动恢复后，使用源端数据覆盖目标实例的数据。
## 费用说明
| 迁移类型 | 链路配置费用 | 公网流量费用 |
| --- | --- | --- |
| 结构迁移和全量数据迁移 | 不收费。 | 当目标库的 接入方式 为 公网 IP 时收取公网流量费用。更多信息，请参见 [计费概述](https://help.aliyun.com/zh/dts/product-overview/billing-overview#concept-261679) 。 |
| 增量数据迁移 | 收费，详情请参见 [计费概述](https://help.aliyun.com/zh/dts/product-overview/billing-overview#concept-261679) 。 |  |
## 迁移类型说明
结构迁移
DTS将待迁移对象的结构定义迁移到目标库，目前DTS支持结构迁移的对象为表、视图、触发器、存储过程、存储函数，不支持event的结构迁移。
说明
在结构迁移时，DTS会将视图、存储过程和函数中的DEFINER转换为INVOKER。
由于DTS不迁移user信息，因此在调用目标库的视图、存储过程和函数时需要对调用者授予读写权限。
全量数据迁移
DTS将迁移对象的存量数据，全部迁移到目标库中。
说明
由于全量数据迁移会并发INSERT导致目标库的表存在碎片，全量迁移完成后目标库的表空间会比源库中的大。
为保障迁移成功，全量数据迁移期间请勿在源库中执行DDL操作。
增量数据迁移
在全量迁移的基础上，DTS会读取源库的Binlog信息，将源库的增量更新数据实时迁移到目标库中。
## 增量数据迁移支持同步的SQL操作
| 操作类型 | SQL 操作语句 |
| --- | --- |
| DML | INSERT、UPDATE、DELETE、REPLACE |
| DDL | ALTER TABLE、ALTER VIEW CREATE FUNCTION、CREATE INDEX、CREATE PROCEDURE、CREATE TABLE、CREATE VIEW DROP INDEX、DROP TABLE RENAME TABLE TRUNCATE TABLE |
## 数据库账号的权限要求
| 数据库 | 结构迁移 | 全量迁移 | 增量迁移 |
| --- | --- | --- | --- |
| RDS MariaDB 实例 | SELECT 权限 | SELECT 权限 | REPLICATION CLIENT、REPLICATION SLAVE、SHOW VIEW 和 SELECT 权限 |
| RDS MySQL 实例 | 读写权限 | 读写权限 | 读写权限 |
数据库账号创建及授权方法：
RDS MariaDB实例：请参见[创建账号](create-a-database-and-an-account-on-an-apsaradb-rds-for-mariadb-instance.md)。
RDS MySQL实例：请参见[创建账号](../apsaradb-rds-for-mysql/create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)和[修改账号权限](../apsaradb-rds-for-mysql/modify-the-permissions-of-a-standard-account-on-an-apsaradb-rds-for-mysql-instance.md)。
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
配置源库及目标库信息。
警告
选择源和目标实例后，建议您仔细阅读页面上方显示的使用限制，否则可能会导致任务失败或数据不一致。
| 类别 | 配置 | 说明 |
| --- | --- | --- |
| 无 | 任务名称 | DTS 会自动生成一个任务名称，建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| 源库信息 | 选择已有连接信息 | 若您需要使用 [已录入系统](https://help.aliyun.com/zh/dts/user-guide/database-connection-management) （新建或保存）的数据库实例，请在下拉列表中选择所需的数据库实例，下方的数据库信息将自动进行配置。 说明 DMS 控制台的配置项为 选择 DMS 数据库实例 。 若您未将数据库实例录入到系统，或无需使用已录入系统的数据库实例，则需要手动配置下方的数据库信息。 |
| 数据库类型 | 选择 Mariadb 。 |  |
| 接入方式 | 选择 云实例 。 |  |
| 实例地区 | 选择源 RDS MariaDB 实例所属地域。 |  |
| 是否跨阿里云账号 | 本示例为同一阿里云账号间的迁移，选择 不跨账号 。 |  |
| 实例 ID | 选择源 RDS MariaDB 实例 ID。 |  |
| 数据库账号 | 填入源 RDS MariaDB 实例的数据库账号，权限要求请参见 [数据库账号的权限要求](migrate-data-from-an-apsaradb-rds-for-mariadb-instance-to-an-apsaradb-rds-for-mysql-instance.md) 。 |  |
| 数据库密码 | 填入该数据库账号对应的密码。 |  |
| 连接方式 | 请选择 非加密连接 。 |  |
| 目标库信息 | 选择已有连接信息 | 若您需要使用 [已录入系统](https://help.aliyun.com/zh/dts/user-guide/database-connection-management) （新建或保存）的数据库实例，请在下拉列表中选择所需的数据库实例，下方的数据库信息将自动进行配置。 说明 DMS 控制台的配置项为 选择 DMS 数据库实例 。 若您未将数据库实例录入到系统，或无需使用已录入系统的数据库实例，则需要手动配置下方的数据库信息。 |
| 数据库类型 | 选择 MySQL 。 |  |
| 接入方式 | 选择 云实例 。 |  |
| 实例地区 | 选择目标 RDS MySQL 实例所属地域。 |  |
| 是否跨阿里云账号 | 本示例为同一阿里云账号间的迁移，选择 不跨账号 。 |  |
| RDS 实例 ID | 选择目标 RDS MySQL 实例的 ID。 |  |
| 数据库账号 | 填入目标 RDS MySQL 实例的数据库账号，权限要求请参见 [数据库账号的权限要求](migrate-data-from-an-apsaradb-rds-for-mariadb-instance-to-an-apsaradb-rds-for-mysql-instance.md) 。 |  |
| 数据库密码 | 填入该数据库账号对应的密码。 |  |
| 连接方式 | 根据需求选择 非加密连接 或 SSL 安全连接 。如果设置为 SSL 安全连接 ，您需要提前开启 RDS MySQL 实例的 SSL 加密功能，详情请参见 [使用云端证书快速开启](../apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) [SSL](../apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) [链路加密](../apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) 。 |  |
配置完成后，在页面下方单击测试连接以进行下一步。
说明
请确保DTS服务的IP地址段能够被自动或手动添加至源库和目标库的安全设置中，以允许DTS服务器的访问。更多信息，请参见[添加](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[DTS](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[服务器的](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[IP](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[地址段](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)。
若源库或目标库为自建数据库（接入方式不是云实例），则还需要在弹出的DTS服务器访问授权对话框单击测试连接。
配置任务对象。
在对象配置页面，配置待迁移的对象。
| 配置 | 说明 |
| --- | --- |
| 迁移类型 | 如果只需要进行全量迁移，建议同时选中 库表结构迁移 和 全量迁移 。 如果需要进行不停机迁移，建议同时选中 库表结构迁移 、 全量迁移 和 增量迁移 。 说明 若未选中 库表结构迁移 ，请确保目标库中存在接收数据的数据库和表，并根据实际情况，在 已选择对象 框中使用库表列名映射功能。 若未选中 增量迁移 ，为保障数据一致性，数据迁移期间请勿在源实例中写入新的数据。 |
| 源库触发器迁移方式 | 请根据实际情况选择迁移触发器的方式，若您待迁移的对象不涉及触发器，则无需配置。更多信息，请参见 [配置同步或迁移触发器的方式](https://help.aliyun.com/zh/dts/user-guide/synchronize-or-migrate-triggers-from-the-source-database#task-2288139) 。 说明 仅当 迁移类型 同时勾选 库表结构迁移 和 增量迁移 时才可以配置。 |
| 目标已存在表的处理模式 | 预检查并报错拦截 ：检查目标数据库中是否有同名的表。如果目标数据库中没有同名的表，则通过该检查项目；如果目标数据库中有同名的表，则在预检查阶段提示错误，数据迁移任务不会被启动。 说明 如果目标库中同名的表不方便删除或重命名，您可以更改该表在目标库中的名称，请参见 [库表列名映射](https://help.aliyun.com/zh/dts/user-guide/map-object-names#task-2101588) 。 忽略报错并继续执行 ：跳过目标数据库中是否有同名表的检查项。 警告 选择为 忽略报错并继续执行 ，可能导致数据不一致，给业务带来风险，例如： 表结构一致的情况下，在目标库遇到与源库主键的值相同的记录： 全量期间，DTS 会保留目标集群中的该条记录，即源库中的该条记录不会迁移至目标数据库中。 增量期间，DTS 不会保留目标集群中的该条记录，即源库中的该条记录会覆盖至目标数据库中。 表结构不一致的情况下，可能导致只能迁移部分列的数据或迁移失败，请谨慎操作。 |
| 源库对象 | 在 源库对象 框中单击待迁移的对象，然后单击 将其移动到 已选择对象 框。 说明 迁移对象选择的粒度为库、表、列。若选择的迁移对象为表或列，其他对象（如视图、触发器、存储过程）不会被迁移至目标库。 |
| 已选择对象 | 如需更改单个迁移对象在目标实例中的名称，请右击 已选择对象 中的迁移对象，设置方式，请参见 [库表列名单个映射](https://help.aliyun.com/zh/dts/user-guide/map-object-names#section-g21-1wy-98l) 。 如需批量更改迁移对象在目标实例中的名称，请单击 已选择对象 方框右上方的 批量编辑 ，设置方式，请参见 [库表列名批量映射](https://help.aliyun.com/zh/dts/user-guide/map-object-names#section-2wn-exv-fib) 。 说明 如果使用了对象名映射功能，可能会导致依赖这个对象的其他对象迁移失败。 如需设置 WHERE 条件过滤数据，请在 已选择对象 中右击待迁移的表，在弹出的对话框中设置过滤条件。设置方法请参见 [设置过滤条件](https://help.aliyun.com/zh/dts/user-guide/use-sql-conditions-to-filter-data-1#concept-610729) 。 如需按库或表级别选择增量迁移的 DML 或 DDL 操作，请在 已选择对象 中右击待迁移对象，并在弹出的对话框中选择所需增量迁移的 DML 和 DDL 操作。 |
单击下一步高级配置，进行高级参数配置。
| 配置 | 说明 |
| --- | --- |
| 选择调度该任务的专属集群 | DTS 默认将任务调度到共享集群上，您无需选择。若您希望任务更加稳定，可以购买 [专属集群](https://help.aliyun.com/zh/dts/user-guide/what-is-a-dts-dedicated-cluster#concept-2183964) 来运行 DTS 迁移任务。 |
| 源库、目标库无法连接后的重试时间 | 在迁移任务启动后，若源库或目标库连接失败则 DTS 会报错，并会立即进行持续的重试连接，默认重试 720 分钟，您也可以在取值范围（10~1440 分钟）内自定义重试时间，建议设置 30 分钟以上。如果 DTS 在设置的时间内重新连接上源、目标库，迁移任务将自动恢复。否则，迁移任务将失败。 说明 针对同源或者同目标的多个 DTS 实例，网络重试时间以后创建任务的设置为准。 由于连接重试期间，DTS 将收取任务运行费用，建议您根据业务需要自定义重试时间，或者在源和目标库实例释放后尽快释放 DTS 实例。 |
| 源库、目标库出现其他问题后的重试时间 | 在迁移任务启动后，若源库或目标库出现非连接性的其他问题（如 DDL 或 DML 执行异常），则 DTS 会报错并会立即进行持续的重试操作，默认持续重试时间为 10 分钟，您也可以在取值范围（1~1440 分钟）内自定义重试时间，建议设置 10 分钟以上。如果 DTS 在设置的重试时间内相关操作执行成功，迁移任务将自动恢复。否则，迁移任务将会失败。 重要 源库、目标库出现其他问题后的重试时间 的值需要小于 源库、目标库无法连接后的重试时间 的值。 |
| 是否限制全量迁移速率 | 在全量迁移阶段，DTS 将占用源库和目标库一定的读写资源，可能会导致数据库的负载上升。您可以根据实际情况，选择是否对全量迁移任务进行限速设置（设置 每秒查询源库的速率 QPS 、 每秒全量迁移的行数 RPS 和 每秒全量迁移的数据量(MB)BPS ），以缓解目标库的压力。 说明 仅当 迁移类型 选择了 全量迁移 ，才有此配置项。 您也可以在迁移实例运行后， [调整全量迁移的速率](https://help.aliyun.com/zh/dts/user-guide/enable-throttling-for-data-migration) 。 |
| 是否限制增量迁移速率 | 您也可以根据实际情况，选择是否对增量迁移任务进行限速设置（设置 每秒增量迁移的行数 RPS 和 每秒增量迁移的数据量(MB)BPS ），以缓解目标库的压力。 说明 仅当 迁移类型 选择了 增量迁移 ，才有此配置项。 您也可以在迁移实例运行后， [调整增量迁移的速率](https://help.aliyun.com/zh/dts/user-guide/enable-throttling-for-data-migration) 。 |
| 环境标签 | 您可以根据实际情况，选择用于标识实例的环境标签。本示例无需选择。 |
| 配置 ETL 功能 | 根据业务需求选择是否配置 [ETL](https://help.aliyun.com/zh/dts/user-guide/what-is-etl#task-2101705) [功能](https://help.aliyun.com/zh/dts/user-guide/what-is-etl#task-2101705) ，对数据进行加工处理。 是 ：配置 ETL 功能，您还需要在文本框中输入 [数据处理语句](https://help.aliyun.com/zh/dts/user-guide/configure-etl-in-a-data-migration-or-data-synchronization-task#task-2189872) 。 否 ：不配置 ETL 功能。 |
| 监控告警 | 根据业务需求选择是否设置告警并接收告警通知。 不设置 ：不设置告警。 设置 ：设置告警。您还需要设置 [告警阈值](https://help.aliyun.com/zh/dts/user-guide/configure-monitoring-and-alerting-1#section-r6s-w5c-kmz) 和 告警联系人 ，当迁移失败或延迟超过阈值后，系统将进行告警通知。 |
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
您可以在迁移任务列表页面，查看迁移实例的具体进度。
说明
若迁移实例不包含增量迁移任务，则迁移实例会自动结束。迁移实例自动结束后，运行状态为已完成。
若迁移实例包含增量迁移任务，则迁移实例不会自动结束，增量迁移任务会持续进行。在增量迁移任务正常运行期间，迁移实例的运行状态为运行中。
## 后续步骤
用于数据迁移的数据库账号拥有读写权限，为保障数据库安全性，请在数据迁移完成后，删除RDS MariaDB实例和RDS MySQL实例中的用于数据迁移的数据库账号。
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
