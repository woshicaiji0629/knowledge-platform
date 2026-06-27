# API概览-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/list-of-operations-by-function

# API概览
云数据库RDS提供以下相关API接口。
## 热门API TOP 10
| API | 描述 |
| --- | --- |
| [CreateDBInstance](api-create-an-instance.md) | 创建一个 RDS 实例。 |
| [DescribeDBInstances](api-query-instances.md) | 查询 RDS 实例列表或被 RAM 授权的实例列表。 |
| [DescribeDBInstanceAttribute](api-query-instance-details.md) | 查询 RDS 实例的详细信息。 |
| [DescribeDBInstancePerformance](api-query-performance-metrics.md) | 查询 RDS 实例性能数据。 |
| [DescribeSlowLogRecords](api-query-slow-query-logs.md) | 查询 RDS 实例的慢日志明细。 |
| [DescribeSlowLogs](api-query-the-summary-of-slow-query-logs.md) | 查询 RDS 实例慢日志统计情况。 |
| [DescribeBackups](api-query-data-backup-files.md) | 查询 RDS 实例备份集列表。 |
| [DescribeResourceUsage](api-query-storage-usage.md) | 查询 RDS 实例的空间使用信息。 |
| [CreateAccount](api-create-an-account.md) | 创建管理数据库的账号。 |
| [CreateDatabase](api-create-database.md) | 创建数据库。 |
## 费用
| API | 描述 |
| --- | --- |
| [DescribePrice](api-query-instance-price.md) | 查询实例的价格。 |
| [DescribeRenewalPrice](api-query-renewal-fee.md) | 查询 RDS 实例续费的费用。 |
| [TransformDBInstancePayType](api-change-the-billing-method.md) | 变更 RDS 实例的计费方式。 |
| [RenewInstance](api-manually-renew-an-apsaradb-for-rds-instance.md) | 手动续费 RDS 实例。 |
## 实例
| API | 描述 |
| --- | --- |
| [CreateDBInstance](api-create-an-instance.md) | 创建一个 RDS 实例。 |
| [DeleteDBInstance](api-release-instance.md) | 释放 RDS 实例。 |
| [RestartDBInstance](api-restart-an-apsaradb-for-rds-instance.md) | 重启 RDS 实例。 |
| [StopDBInstance](api-stop-instance.md) | 暂停 RDS 实例。 |
| [StartDBInstance](api-start-instance.md) | 启用 RDS 实例。 |
| [ModifyDBInstanceSpec](api-change-instance-configuration.md) | 变更 RDS 实例（包括常规实例和只读实例，不包括灾备实例和临时实例）的规格或存储空间。 |
| [ModifyDasInstanceConfig](api-configure-automatic-storage-expansion.md) | 设置实例存储空间自动扩容。 |
| [DescribeAvailableZones](api-query-available-zones-and-resources.md) | 查询 RDS 可用区资源。 |
| [DescribeAvailableClasses](api-query-available-specifications.md) | 查询实例可变更规格，包括规格代码和存储空间。 |
| [DescribeDBInstanceAttribute](api-query-instance-details.md) | 查询 RDS 实例的详细信息。 |
| [GetDBInstanceTopology](api-get-dbinstance-topology.md) | 获取 RDS 实例的拓扑结构。 |
| [DescribeDBInstances](api-query-instances.md) | 查询 RDS 实例列表或被 RAM 授权的实例列表。 |
| [ListClasses](api-query-instance-types.md) | 查询 RDS 实例所有规格的详情。 |
| [DescribeDBInstancesByExpireTime](api-query-instances-based-on-expiration-date-and-time.md) | 通过过期时间查询 RDS 实例信息。 |
| [DescribeRegions](api-query-regions.md) | 查询当前可选的 RDS 地域和可用区信息。 |
| [MigrateToOtherZone](api-migrate-an-instance-across-zones.md) | 迁移 RDS 实例至其他可用区。 |
| [ModifyDBInstanceDescription](api-change-instance-name.md) | 修改 RDS 实例的描述。 |
| [ModifyDBInstanceMaintainTime](api-modify-the-maintenance-time.md) | 修改 RDS 实例可维护时间段。 |
| [ModifyResourceGroup](api-t070mo.md) | 将 RDS 实例移动到指定资源组。 |
| [CheckInstanceExist](api-query-whether-an-instance-exists.md) | 查询实例是否存在。 |
| [ModifyHADiagnoseConfig](api-modify-availability-check-method.md) | 修改阿里云对目标 RDS 实例的可用性检测方式。 |
| [DescribeHADiagnoseConfig](api-query-availability-check-method.md) | 查询阿里云对目标 RDS 实例的可用性检测方式。 |
| [DescribeAnalyticdbByPrimaryDBInstance](api-describe-analyticdb-by-primary-dbinstance.md) | 查询 RDS MySQL 实例关联的分析型实例。 |
| [CheckCloudResourceAuthorized](api-check-cloud-resource-authorized.md) | 查询云资源的权限状态。 |
## 升级版本
| API | 描述 |
| --- | --- |
| [UpgradeDBInstanceEngineVersion](api-upgrade-the-major-engine-version-of-an-apsaradb-rds-for-mysql-instance-1.md) | 升级实例数据库版本。 |
| [UpgradeDBInstanceKernelVersion](api-update-minor-engine-version.md) | 升级 RDS 实例的内核小版本。 |
| [ModifyDBInstanceAutoUpgradeMinorVersion](api-change-the-method-to-update-the-minor-version.md) | 修改 RDS 实例升级内核小版本的方式。 |
| [UpgradeDBInstanceMajorVersionPrecheck](api-check-the-compatibility-between-a-new-major-engine-version-and-an-apsaradb-rds-for-postgresql-instance-before-an-upgrade.md) | 执行 RDS PostgreSQL 实例大版本升级前检查。 |
| [DescribeUpgradeMajorVersionPrecheckTask](api-query-the-check-report-for-a-major-engine-version-upgrade-to-an-apsaradb-rds-for-postgresql-instance.md) | 查询 RDS PostgreSQL 实例大版本升级前检查报告。 |
| [UpgradeDBInstanceMajorVersion](api-upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance-2.md) | 发起 RDS PostgreSQL 实例大版本升级。 |
| [DescribeUpgradeMajorVersionTasks](api-query-the-tasks-for-major-engine-version-upgrades.md) | 查询 RDS PostgreSQL 实例大版本升级的历史任务。 |
## 网络与连接地址
| API | 描述 |
| --- | --- |
| [AllocateInstancePublicConnection](api-apply-for-public-endpoint.md) | 申请 RDS 实例的外网地址。 |
| [DescribeDBInstanceNetInfo](api-query-endpoints.md) | 查询 RDS 实例的所有连接地址信息。 |
| [ModifyDBInstanceConnectionString](api-modify-the-endpoint-and-port-of-an-apsaradb-for-rds-instance.md) | 修改 RDS 实例的连接地址和端口。 |
| [ModifyDBInstanceNetworkExpireTime](api-change-the-expiration-time-of-a-classic-network-endpoint.md) | 修改 RDS 实例连接地址过期时间。 |
| [SwitchDBInstanceNetType](api-switch-between-internal-and-public-endpoints.md) | 切换 RDS 实例内外网地址。 |
| [ReleaseInstancePublicConnection](api-release-a-public-endpoint.md) | 释放 RDS 实例的外网连接地址。 |
| [ModifyDBInstanceNetworkType](api-change-the-network-type-of-an-apsaradb-for-rds-instance.md) | 切换 RDS 实例网络类型。 |
| [SwitchDBInstanceVpc](api-change-vpc-or-vswitch.md) | 切换 RDS 实例的专有网络 VPC 或交换机。 |
| [DescribeVSwitches](api-query-details-about-a-vswitch.md) | 查询专有网络 VPC 下虚拟交换机的详细信息。 |
## 主备高可用和数据复制方式
| API | 描述 |
| --- | --- |
| [ModifyDBInstanceHAConfig](api-change-the-high-availability-mode-and-data-replication-mode.md) | 修改 RDS 实例的高可用模式和数据复制方式。 |
| [DescribeDBInstanceHAConfig](api-query-high-availability-mode.md) | 查询 RDS 实例高可用模式和数据复制方式。 |
| [SwitchDBInstanceHA](api-switch-services-between-a-primary-apsaradb-for-rds-instance-and-its-secondary-instance.md) | 切换 RDS 实例的主备实例。 |
| [ModifyHASwitchConfig](api-enable-or-disable-automatic-primary-or-secondary-switchovers.md) | 开启或关闭 RDS 实例的主备自动切换功能。 |
| [DescribeHASwitchConfig](api-query-settings-of-automatic-primary-or-secondary-switchover.md) | 查询 RDS 实例主备自动切换设置。 |
## 历史事件
| API | 描述 |
| --- | --- |
| [DescribeEvents](api-query-events-of-apsaradb-for-rds-instances-in-a-region.md) | 查询 RDS 事件记录列表。 |
| [DescribeActionEventPolicy](api-query-status-of-the-event-history-feature.md) | 查询 RDS 历史事件功能开启情况。 |
| [ModifyActionEventPolicy](api-enable-or-disable-the-event-history-feature.md) | 开启或关闭 RDS 历史事件功能。 |
## 通知
| API | 描述 |
| --- | --- |
| [QueryNotify](api-querynotify.md) | 查询 RDS 通知列表。 |
| [ModifyActionEventPolicy](api-enable-or-disable-the-event-history-feature.md) | 开启或关闭 RDS 历史事件功能。 |
## CloudDBA数据库性能优化
| API | 描述 |
| --- | --- |
| [CreateDiagnosticReport](api-creatediagnosticreport.md) | 创建诊断报告。 |
| [DescribeDiagnosticReportList](api-describediagnosticreportlist.md) | 获取诊断报告列表。 |
## 账号
| API | 描述 |
| --- | --- |
| [CreateAccount](api-create-an-account.md) | 创建管理数据库的账号。 |
| [DeleteAccount](api-delete-an-account.md) | 删除数据库账号。 |
| [ResetAccountPassword](api-reset-account-password.md) | 重置账号密码。 |
| [LockAccount](api-lock-account.md) | 锁定 RDS PostgreSQL 实例的账号。 |
| [UnlockAccount](api-unlock-account.md) | 解锁 RDS PostgreSQL 实例的账号。 |
| [DescribeAccounts](api-query-accounts.md) | 查询 RDS 实例的账号信息。 |
| [ModifyAccountDescription](api-modify-the-description-of-a-database-account.md) | 修改数据库账号的描述。 |
| [DescribeInstanceKeywords](api-query-reserved-keywords.md) | 查询 RDS 实例的保留关键字，即创建数据库或账号时禁用的关键字。 |
| [ModifyPGHbaConfig](api-modifies-the-pg-hba-conf-file-of-an-apsaradb-rds-for-postgresql-instance.md) | 修改 RDS PostgreSQL 实例的 pg_hba.conf 文件配置。 |
| [DescribePGHbaConfig](api-query-the-configuration-of-the-pg-hba-conf-file-of-an-apsaradb-rds-for-postgresql-instance.md) | 查询 RDS PostgreSQL 实例的 pg_hba.conf 文件的配置。 |
| [DescribeModifyPGHbaConfigLog](api-query-the-modification-history-of-the-pg-hba-conf-file-of-an-apsaradb-rds-for-postgresql-instance.md) | 查询 RDS PostgreSQL 实例的 pg_hba.conf 文件的修改记录。 |
| [GrantAccountPrivilege](api-grant-permissions-to-account.md) | 授权账号访问数据库。 |
| [GrantOperatorPermission](api-grant-permissions-to-a-service-account.md) | 授予服务账号权限。 |
| [RevokeOperatorPermission](api-revoke-permissions-from-a-service-account.md) | 撤销服务账号权限。 |
| [RevokeAccountPrivilege](api-revoke-database-access-permissions-of-an-account.md) | 撤销账号对数据库的访问权限。 |
| [ResetAccount](api-reset-permissions-of-the-privileged-account.md) | 重置高权限账号的权限。 |
## 数据库
| API | 描述 |
| --- | --- |
| [CreateDatabase](api-create-database.md) | 创建数据库。 |
| [DeleteDatabase](api-delete-database.md) | 删除 RDS 实例下的某个数据库。 |
| [ModifyDBDescription](api-modify-the-database-description.md) | 修改数据库备注。 |
| [CopyDatabaseBetweenInstances](api-copy-database.md) | 在 RDS 实例间复制数据库。 |
| [DescribeDatabases](api-query-databases.md) | 查询 RDS 实例下的数据库信息。 |
| [CheckDBNameAvailable](api-query-database-name-availability.md) | 检查数据库名称是否可用。 |
| [DescribeCollationTimeZones](api-query-character-set-collations-and-time-zones.md) | 查询支持的字符集排序规则和时区。 |
| [DescribeCharacterSetName](api-query-supported-character-sets.md) | 查询 RDS 实例支持的字符集。 |
## 只读实例
| API | 描述 |
| --- | --- |
| [CreateReadOnlyDBInstance](api-create-a-read-only-instance.md) | 为某个 RDS 实例创建一个只读实例。 |
| [DescribeReadDBInstanceDelay](api-query-data-replication-latency.md) | 查询 RDS 只读实例的延迟信息。 |
| [ModifyReadonlyInstanceDelayReplicationTime](api-modify-replication-latency-of-read-only-rds-instance.md) | 修改 RDS 只读实例的延迟复制时间。 |
## 集群版实例
| API | 描述 |
| --- | --- |
| [CreateDBNodes](api-create-an-instance-node.md) | 新增集群版实例节点。 |
| [DeleteDBNodes](api-delete-an-instance-node.md) | 删除集群版实例节点。 |
| [DescribeDBInstanceEndpoints](api-query-the-endpoint-information-of-an-instance.md) | 查询实例的 Endpoint 信息。 |
| [CreateDBInstanceEndpoint](api-the-endpoint-of-the-created-instance.md) | 创建实例的 Endpoint。 |
| [DeleteDBInstanceEndpoint](api-delete-the-endpoint-of-an-instance.md) | 删除实例的 Endpoint。 |
| [ModifyDBInstanceEndpoint](api-modify-the-endpoint-information-of-an-instance.md) | 修改实例 Endpoint 信息。 |
| [CreateDBInstanceEndpointAddress](api-create-an-external-network-connection-address-of-an-instance.md) | 创建实例外网连接地址。 |
| [DeleteDBInstanceEndpointAddress](api-delete-the-external-network-connection-address-of-the-instance.md) | 删除实例的外网连接地址。 |
| [ModifyDBInstanceEndpointAddress](api-modify-the-connection-address-of-an-instance.md) | 修改实例的 Endpoint 连接地址。 |
## 数据库共享代理（下线中）
| API | 描述 |
| --- | --- |
| [AllocateReadWriteSplittingConnection](api-apply-for-read-only-routing-endpoint1.md) | 申请读写分离地址。 |
| [ReleaseReadWriteSplittingConnection](api-release-read-or-write-splitting-endpoint1.md) | 释放读写分离地址。 |
| [CalculateDBInstanceWeight](api-query-read-weights1.md) | 查询系统权重分配值。 |
| [ModifyReadWriteSplittingConnection](api-modify-read-weights-and-latency-threshold1.md) | 修改读写分离链路的延迟阈值和各个实例的读权重。 |
| [DescribeDBInstanceProxyConfiguration](api-query-shared-proxy-settings.md) | 查询数据库代理设置。 |
## 数据库独享代理（读写分离）
| API | 描述 |
| --- | --- |
| [ModifyDBProxy](api-enable-or-disable-the-dedicated-proxy-feature.md) | 开启或者关闭 RDS 实例的数据库独享代理功能。 |
| [UpgradeDBProxyInstanceKernelVersion](api-upgrades-dedicated-proxy-version.md) | 升级独享代理内核小版本。 |
| [ModifyDBProxyInstance](api-modify-settings-of-a-dedicated-proxy.md) | 修改 RDS 数据库独享代理数量。 |
| [ModifyDBProxyEndpoint](api-modify-proxy-terminal-settings.md) | 修改 RDS 实例数据库独享代理的连接地址配置（读写分离、事务拆分、连接池）。 |
| [DescribeDBProxy](api-query-dedicated-proxy-details.md) | 查询 RDS 实例的数据库独享代理详情。 |
| [DescribeDBProxyEndpoint](api-query-proxy-endpoint.md) | 查询 RDS 实例独享代理的连接地址信息。 |
| [DescribeDBProxyPerformance](api-query-performance-metrics-of-a-dedicated-proxy.md) | 查询独享代理的性能数据。 |
| [CreateDBProxyEndpointAddress](api-create-proxy-endpoint.md) | 创建 RDS 实例独享代理的连接地址。 |
| [ModifyDBProxyEndpointAddress](api-modify-proxy-endpoint.md) | 修改 RDS 实例独享代理的连接地址。 |
| [DeleteDBProxyEndpointAddress](api-delete-proxy-endpoint.md) | 删除 RDS 实例独享代理的连接地址。 |
| [ModifyDbProxyInstanceSsl](api-configure-ssl-encryption-for-dedicated-proxy-endpoint.md) | 设置 RDS 实例独享代理连接地址 SSL 加密。 |
| [GetDbProxyInstanceSsl](api-query-ssl-encryption-settings-of-dedicated-proxy-endpoint.md) | 查询 RDS 实例独享代理连接地址 SSL 加密信息。 |
## 安全加密
| API | 描述 |
| --- | --- |
| [DescribeSecurityGroupConfiguration](api-query-ecs-security-groups-to-which-an-apsaradb-for-rds-instance-is-added.md) | 查询指定 RDS 实例和 ECS 安全组的关联信息。 |
| [ModifySecurityGroupConfiguration](api-change-the-ecs-security-group-for-an-apsaradb-for-rds-instance.md) | 修改指定 RDS 实例和 ECS 安全组的关联信息。 |
| [DescribeDBInstanceIPArrayList](api-query-ip-address-whitelists.md) | 查询 RDS 实例 IP 白名单。 |
| [ModifySecurityIps](api-modify-ip-address-whitelist.md) | 修改 IP 白名单。 |
| [DescribeDBInstanceSSL](api-query-ssl-encryption-settings.md) | 查询 RDS 实例 SSL 设置。 |
| [ModifyDBInstanceSSL](api-modify-ssl-encryption-settings.md) | 修改 RDS 实例 SSL 链路。 |
| [DescribeDBInstanceTDE](api-query-settings-of-tde.md) | 查询 RDS 实例数据加密状态。 |
| [ModifyDBInstanceTDE](api-enable-tde.md) | 开启 RDS 实例透明数据加密功能。 |
| [MigrateSecurityIPMode](api-switch-the-network-isolation-mode-from-standard-whitelist-to-enhanced-whitelist.md) | 白名单从通用模式切换为高安全模式。 |
| [DescribeDBInstanceIpHostname](api-query-the-hostname-of-an-apsaradb-for-rds-instance.md) | 查询 RDS 实例的底层 ECS 实例的 hostname。 |
| [DescribeDTCSecurityIpHostsForSQLServer](api-query-distributed-transaction-whitelists.md) | 查询 RDS 实例的分布式事务白名单信息。 |
| [ModifyDTCSecurityIpHostsForSQLServer](api-configure-a-distributed-transaction-whitelist.md) | 设置分布式事务白名单。 |
| [DescribeDBInstanceEncryptionKey](api-query-the-status-and-key-of-disk-encryption.md) | 查询 RDS 实例的云盘加密状态及密钥详情。 |
| [CreateServiceLinkedRole](api-createservicelinkedrole.md) | 创建服务关联角色（SLR）。 |
| [ModifyDBInstanceDeletionProtection](api-modify-delection-protection.md) | 开启或关闭 RDS 实例的释放保护功能。 |
## 日志
| API | 描述 |
| --- | --- |
| [ModifySQLCollectorPolicy](api-enable-or-disable-sql-explorer.md) | 开启或关闭实例的 SQL 洞察（SQL 审计）功能。 |
| [DescribeSQLCollectorPolicy](api-query-sql-explorer-status.md) | 查询 RDS 实例的 SQL 审计或 SQL 洞察功能是否开启。 |
| [DescribeSQLLogRecords](api-query-logs-generated-by-sql-explorer.md) | 查询 RDS 实例的 SQL 洞察（SQL 审计）日志。 |
| [DescribeSQLLogFiles](api-query-audit-log-files-generated-by-sql-explorer-and-audit.md) | 查询 SQL 洞察（SQL 审计）文件列表。 |
| [ModifySQLCollectorRetention](api-modify-retention-period-of-sql-explorer-logs.md) | 修改 RDS 实例的 SQL 洞察日志保存时长。 |
| [DescribeSQLCollectorRetention](api-query-the-log-retention-period-allowed-for-the-sql-explorer-feature.md) | 查询 RDS 实例的 SQL 洞察日志保存时长。 |
| [DescribeSlowLogs](api-query-the-summary-of-slow-query-logs.md) | 查询慢日志统计情况。 |
| [DescribeSlowLogRecords](api-query-slow-query-logs.md) | 查询 RDS 实例的慢日志明细。 |
| [DescribeErrorLogs](api-query-error-logs.md) | 查询 RDS 实例某段时间内的错误日志。 |
| [PurgeDBInstanceLog](api-delete-local-log-backup-files.md) | 清理或收缩 RDS 实例日志。 |
| [DescribeSQLLogReports](api-query-sql-log-reports-1.md) | 查询实例的 SQL 日志运行报告。 |
| [DescribeSQLLogReportList](api-query-sql-log-reports-2.md) | 查看实例的 SQL 日志运行报告列表。 |
## 备份
| API | 描述 |
| --- | --- |
| [CreateBackup](api-create-a-backup-task.md) | 创建一个备份集。 |
| [DescribeBackups](api-query-data-backup-files.md) | 查询备份集列表。 |
| [DescribeDetachedBackups](api-query-data-backup-files-of-a-deleted-instance.md) | 查看已删除实例的备份集列表。 |
| [DescribeBackupPolicy](api-query-backup-settings.md) | 查询 RDS 实例备份设置。 |
| [ModifyBackupPolicy](api-modify-backup-settings.md) | 修改备份设置。 |
| [DeleteBackup](api-delete-backup-sets.md) | 删除数据备份文件。 |
| [DescribeBackupTasks](api-query-backup-tasks.md) | 查询 RDS 实例的备份任务列表。 |
| [DescribeBinlogFiles](api-query-log-backup-files.md) | 查询 Binlog 日志。 |
## 恢复
| API | 描述 |
| --- | --- |
| [RecoveryDBInstance](api-restore-databases.md) | 恢复数据库。 |
| [CloneDBInstance](api-restore-data-to-a-new-apsaradb-rds-instance.md) | 将历史数据恢复至一个新实例（称为克隆实例）。 |
| [CreateTempDBInstance](api-create-a-temporary-instance.md) | 创建临时实例。 |
| [DescribeLocalAvailableRecoveryTime](api-query-the-time-range-for-restoration.md) | 查询 RDS 实例备份可恢复的时间范围。 |
| [RestoreTable](api-restore-individual-databases-or-tables.md) | 恢复 RDS 实例的某些数据库或表到原实例。 |
| [DescribeMetaList](api-query-data-backup-file-for-databases-and-tables.md) | 查询目标备份集中可恢复的库表信息。 |
## 跨地域备份恢复
| API | 描述 |
| --- | --- |
| [CheckCreateDdrDBInstance](api-check-cross-region-backup.md) | 预检查某 RDS 实例是否可以用跨地域备份集进行跨地域恢复。 |
| [CreateDdrInstance](api-restore-data-to-a-new-instance-across-regions.md) | 跨地域恢复数据到新实例。 |
| [RestoreDdrTable](api-restore-data-to-an-existing-instance-across-regions.md) | 跨地域恢复数据到已有实例。 |
| [ModifyInstanceCrossBackupPolicy](api-modify-cross-region-backup-settings.md) | 修改 RDS 跨地域备份设置。 |
| [DescribeInstanceCrossBackupPolicy](api-query-cross-region-backup-settings.md) | 查询跨地域备份设置。 |
| [DescribeCrossBackupMetaList](api-query-databases-and-tables-included-in-a-cross-region-backup-set.md) | 查询跨地域备份的库表信息。 |
| [DescribeCrossRegionBackups](api-query-cross-region-data-backup-files.md) | 查询某 RDS 实例跨地域数据备份文件列表。 |
| [DescribeCrossRegionLogBackupFiles](api-query-cross-region-log-backup-files.md) | 查询跨地域日志备份文件列表。 |
| [DescribeAvailableCrossRegion](api-query-regions-that-support-cross-region-backup.md) | 查询所选地域当前可以进行跨地域备份的目的地域。 |
| [DescribeAvailableRecoveryTime](api-query-the-time-range-to-which-you-can-restore-data-by-using-a-cross-region-backup-set.md) | 查询某跨地域备份文件可恢复哪个时间段的数据。 |
| [DescribeCrossRegionBackupDBInstance](api-query-apsaradb-for-rds-instances-on-which-cross-region-backup-is-enabled.md) | 查询所选地域的哪些实例开启了跨地域备份，以及这些实例的跨地域备份设置。 |
## 监控
| API | 描述 |
| --- | --- |
| [DescribeResourceUsage](api-query-storage-usage.md) | 查询实例的空间使用信息。 |
| [DescribeDBInstancePerformance](api-query-performance-metrics.md) | 查询实例性能数据。 |
| [DescribeDBInstanceMonitor](api-query-the-monitoring-frequency-of-an-apsaradb-rds-instance.md) | 查询监控频率。 |
| [ModifyDBInstanceMonitor](api-modify-monitoring-frequency.md) | 修改监控频率。 |
| [DescribeAvailableMetrics](api-query-available-enhanced-monitoring-metrics.md) | 获取 RDS PostgreSQL 实例支持的所有增强监控指标。 |
| [ModifyDBInstanceMetrics](api-modify-displayed-enhanced-monitoring-metrics.md) | 变更 RDS PostgreSQL 实例需要展示的增强监控指标。 |
| [DescribeDBInstanceMetrics](api-query-enabled-enhanced-monitoring-metrics.md) | 查询 RDS PostgreSQL 实例已开启的增强指标。 |
## 参数
| API | 描述 |
| --- | --- |
| [DescribeParameters](api-query-parameter-configurations.md) | 查询实例当前的参数配置。 |
| [ModifyParameter](api-modify-parameters-of-an-apsaradb-for-rds-instance.md) | 修改实例参数。 |
| [DescribeModifyParameterLog](api-query-parameter-configuration-logs.md) | 查询 RDS 实例的参数修改日志。 |
| [DescribeParameterTemplates](api-query-the-parameter-template-of-an-apsaradb-for-rds-instance.md) | 查询数据库参数模板。 |
| [CreateParameterGroup](api-create-a-parameter-template.md) | 创建 RDS 参数模板。 |
| [ModifyParameterGroup](api-modify-a-parameter-template.md) | 修改 RDS 参数模板。 |
| [CloneParameterGroup](api-copy-a-parameter-template.md) | 复制 RDS 参数模板到当前地域或其他地域内。 |
| [DescribeParameterGroups](api-query-parameter-templates.md) | 查询目标地域的参数模板列表。 |
| [DescribeParameterGroup](api-query-information-of-a-parameter-template.md) | 查询指定的 RDS 参数模板信息。 |
| [DeleteParameterGroup](api-delete-a-parameter-template.md) | 删除 RDS 参数模板。 |
## 数据迁移
| API | 描述 |
| --- | --- |
| [ImportDatabaseBetweenInstances](api-migrate-data-across-instances.md) | 从其它 RDS 实例迁入数据。 |
| [CancelImport](api-cancel-migration-task.md) | 取消 RDS SQL Server 实例迁移任务。 |
## MySQL备份文件上云
| API | 描述 |
| --- | --- |
| [ImportUserBackupFile](api-import-a-full-backup-file.md) | 将自建库 MySQL 的备份数据导入至 RDS。 |
| [UpdateUserBackupFile](api-modify-a-full-backup-file.md) | 变更用户备份的备注信息和保留时长。 |
| [ListUserBackupFiles](api-query-full-backup-files.md) | 查询所有已导入至 RDS 的用户备份的详情。 |
| [DeleteUserBackupFile](api-delete-a-full-backup-file.md) | 删除目标用户备份。 |
## SQL Server备份文件上云
| API | 描述 |
| --- | --- |
| [CreateMigrateTask](api-create-a-migration-task.md) | 将 OSS 上的备份文件还原到 RDS 实例，实现数据上云。 |
| [DescribeMigrateTasks](api-query-backup-data-migration-tasks.md) | 查询备份数据上云任务列表。 |
| [DescribeOssDownloads](api-query-backup-data-files-of-migration-task.md) | 查询备份数据上云任务的文件详情。 |
| [CreateOnlineDatabaseTask](api-open-the-database-to-which-backup-data-is-migrated.md) | 打开 RDS SQL Server 备份数据上云任务的数据库。 |
| [DescribeMigrateTaskById](api-query-a-single-migration-task.md) | 查询 SQL Server 的某个 OSS 备份上云任务的信息。 |
| [TerminateMigrateTask](api-terminate-migration-task.md) | 终止 RDS 实例迁移任务。 |
## SQL Server AD域
| API | 描述 |
| --- | --- |
| [ModifyADInfo](api-modify-ad-domain-information.md) | 修改 RDS SQL Server 实例的 AD 域信息。 |
| [DeleteADSetting](api-delete-ad-settings.md) | 移除 RDS SQL Server 实例的 AD 域信息。 |
| [DescribeADInfo](api-query-the-ad-domain-information.md) | 查询 RDS SQL Server 实例的 AD 域信息。 |
## SQL Server集群管理
| API | 描述 |
| --- | --- |
| [AllocateReadWriteSplittingConnection](api-apply-for-read-only-routing-endpoint.md) | 申请 RDS 实例的读写分离地址。 |
| [ReleaseReadWriteSplittingConnection](api-release-read-or-write-splitting-endpoint.md) | 释放 RDS 实例的读写分离地址。 |
| [CalculateDBInstanceWeight](api-query-read-weights.md) | 查询系统权重分配值。 |
| [ModifyReadWriteSplittingConnection](api-modify-read-weights-and-latency-threshold.md) | 修改读写分离链路的延迟阈值和各个实例的读权重。 |
## PostgreSQL一键上云
| API | 描述 |
| --- | --- |
| [CreateCloudMigrationPrecheckTask](api-create-rds-postgresql-check-task-before-going-to-the-cloud.md) | 创建 RDS PostgreSQL 一键上云前检查任务。 |
| [DescribeCloudMigrationPrecheckResult](api-query-rds-postgresql-check-report-before-going-to-the-cloud.md) | 查询一键上云前检查报告。 |
| [CreateCloudMigrationTask](api-create-a-cloud-migration-task-for-rds-postgresql.md) | 创建 RDS PostgreSQL 迁移上云任务。 |
| [ActivateMigrationTargetInstance](api-rds-postgresql-cloud-switching.md) | 执行 RDS PostgreSQL 上云切换，将 RDS PostgreSQL 提升为主库，正式提供服务。 |
| [DescribeCloudMigrationResult](api-query-cloud-migration-task-details.md) | 查询 RDS PostgreSQL 迁移上云任务详情。 |
## 全球多活数据库集群
| API | 描述 |
| --- | --- |
| [DescribeGadInstances](api-query-the-list-of-global-replica-clusters.md) | 查询 RDS 全球多活数据库集群列表或目标集群的详细信息。 |
| [CreateGADInstance](api-create-a-global-replica-db-cluster.md) | 创建 RDS 全球多活数据库集群。 |
| [CreateGadInstanceMember](api-add-a-global-replica-database-node.md) | 在 RDS 全球多活数据库集群中添加单元节点。 |
| [DeleteGadInstance](api-delete-a-global-replica-db-cluster.md) | 删除 RDS 全球多活数据库集群。 |
| [DetachGadInstanceMemer](api-remove-a-global-replica-database-node.md) | 移除 RDS 全球多活数据库集群中的单元节点。 |
## 标签
| API | 描述 |
| --- | --- |
| [TagResources](api-create-and-bind-tags.md) | 为指定的 RDS 实例创建并绑定标签。 |
| [UntagResources](api-unbind-tags.md) | 为指定的 RDS 实例解绑标签。 |
| [ListTagResources](api-query-tags.md) | 查询一个或多个 RDS 实例已经绑定的标签列表。 |
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
