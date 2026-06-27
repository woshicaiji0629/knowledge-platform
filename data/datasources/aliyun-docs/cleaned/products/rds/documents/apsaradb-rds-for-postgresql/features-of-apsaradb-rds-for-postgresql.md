# 各版本与系列功能支持差异-云数据库RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/features-of-apsaradb-rds-for-postgresql

# RDS PostgreSQL功能概览
本文介绍RDS PostgreSQL各版本支持的功能，便于您根据自身需要选购实例或查询已购实例的功能。
## 在售版本功能概览
## PostgreSQL 18
| 功能 | 集群系列 | 高可用系列 | 基础系列 |  |  |
| --- | --- | --- | --- | --- | --- |
| 包年包月/按量付费 | 包年包月/按量付费 | Serverless | 包年包月/按量付费 | Serverless |  |
| [一键上云](cloud-migration.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [数据迁移](data-migration-2.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [数据同步](manage-dataconnectors.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [数据订阅](change-tracking.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [升级数据库大版本](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) | 不涉及 | 不涉及 | 不涉及 | 不涉及 | 不涉及 |
| [升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [创建实例](create-an-apsaradb-rds-for-postgresql-instance-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [变更配置](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [重启实例](restart-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [变更资源扩缩容范围（RCU）](change-the-scaling-range-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| [设置实例自动启停](configure-the-automatic-start-and-stop-feature-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| [变更实例弹性策略](change-the-scaling-policy-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| [暂停实例](suspend-an-rds-instance-2.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [自动或手动主备切换](switch-workloads-over-between-primary-and-secondary-apsaradb-rds-for-postgresql-instances.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ |
| [设置可维护时间段](set-the-maintenance-window-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [设置存储空间自动扩容](configure-automatic-storage-expansion-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [迁移可用区](migrate-an-apsaradb-rds-for-postgresql-instance-across-zones-in-the-same-region.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [释放实例](release-or-unsubscribe-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [开启和关闭实例释放保护](enable-or-disable-the-release-protection-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [设置实例参数](modify-the-parameters-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查询和修改数据复制方式](change-the-data-replication-mode-of-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ✔️ | ✔️ | ❌ | ❌ |
| [实例回收站](manage-apsaradb-rds-for-postgresql-instances-in-the-recycle-bin.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [Babelfish for RDS PostgreSQL](babelfish-for-apsaradb-rds-for-postgresql.md) | ❌ | ❌ | ❌ | ❌ | ❌ |
| [只读实例](rds-for-postgresql-read-only-instances.md) | ❌ | ✔️ | ❌ | ❌ | ❌ |
| [数据库代理（读写分离）](database-proxy.md) | ❌ | ✔️ | ❌ | ❌ | ❌ |
| [创建账号](create-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [重置密码](reset-the-password-of-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [RDS PostgreSQL](connect-an-apsaradb-rds-for-postgresql-instance-to-a-self-managed-ad-domain.md) [接入自建域](connect-an-apsaradb-rds-for-postgresql-instance-to-a-self-managed-ad-domain.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [锁定/删除账号](lock-or-delete-an-account-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [连接](connect-to-an-apsaradb-rds-for-postgresql-instance.md) [PostgreSQL](connect-to-an-apsaradb-rds-for-postgresql-instance.md) [实例](connect-to-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [开通或关闭外网地址](apply-for-or-release-a-public-endpoint-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查看或修改内外网地址和端口](view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [更改网络类型](change-the-network-type-of-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ❌ | ❌ | ❌ |
| [切换虚拟交换机](switch-an-apsaradb-rds-for-postgresql-instance-to-a-different-vswitch.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [创建数据库](create-a-database-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [删除数据库](delete-a-database-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [修改时区](change-the-time-zone-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [插件](extensions-supported-by-apsaradb-rds-for-postgresql.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查看增强监控](view-the-enhanced-monitoring-metrics-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [管理报警](manage-the-alert-rules-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [切换高安全白名单模式](switch-an-apsaradb-rds-for-postgresql-instance-to-the-enhanced-whitelist-mode.md) | ❌ | ❌ | ❌ | ❌ | ❌ |
| [设置白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [SSL](ssl-encryption.md) [链路加密](ssl-encryption.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [云盘加密](configure-disk-encryption-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [全密态云数据库](fully-encrypted-database.md) | ✔️ | 非安全增强型实例：✔️ 安全增强型实例：❌ | ❌ | ✔️ | ❌ |
| [透明数据加密](https://help.aliyun.com/zh/document_detail/465651.html#concept-2272850) [TDE](https://help.aliyun.com/zh/document_detail/465651.html#concept-2272850) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [SQL](../use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) [审计（数据库审计）](../use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [日志管理](view-the-logs-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [任务中心](task-list.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [备份数据](back-up-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [跨地域备份](use-the-cross-region-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [稀疏备份](sparse-backup-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [高频快照备份](use-the-high-frequency-snapshot-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [下载备份](download-the-backup-files-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ❌ | ✔️ |
| [删除备份](delete-backup-files-or-reduce-the-size-of-backup-files.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [恢复数据](restore-data-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [恢复库表](restore-individual-databases-and-tables-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [跨地域恢复](restore-the-data-of-an-apsaradb-rds-for-postgresql-instance-across-regions.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [自治服务](performance-optimization-and-diagnosis-1.md) [DAS](performance-optimization-and-diagnosis-1.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ |
| [创建标签](add-tags-to-apsaradb-rds-instances-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [删除标签](remove-tags-from-an-apsaradb-rds-for-mysql-instance-2.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
## PostgreSQL 17
| 功能 | 集群系列 | 高可用系列 | 基础系列 |  |  |
| --- | --- | --- | --- | --- | --- |
| 包年包月/按量付费 | 包年包月/按量付费 | Serverless | 包年包月/按量付费 | Serverless |  |
| [一键上云](cloud-migration.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [数据迁移](data-migration-2.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [数据同步](manage-dataconnectors.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [数据订阅](change-tracking.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [升级数据库大版本](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) | 不涉及 | 不涉及 | 不涉及 | 不涉及 | 不涉及 |
| [升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [创建实例](create-an-apsaradb-rds-for-postgresql-instance-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [变更配置](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [重启实例](restart-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [变更资源扩缩容范围（RCU）](change-the-scaling-range-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| [设置实例自动启停](configure-the-automatic-start-and-stop-feature-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| [变更实例弹性策略](change-the-scaling-policy-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| [暂停实例](suspend-an-rds-instance-2.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [自动或手动主备切换](switch-workloads-over-between-primary-and-secondary-apsaradb-rds-for-postgresql-instances.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ |
| [设置可维护时间段](set-the-maintenance-window-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [设置存储空间自动扩容](configure-automatic-storage-expansion-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [迁移可用区](migrate-an-apsaradb-rds-for-postgresql-instance-across-zones-in-the-same-region.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [释放实例](release-or-unsubscribe-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [开启和关闭实例释放保护](enable-or-disable-the-release-protection-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [设置实例参数](modify-the-parameters-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查询和修改数据复制方式](change-the-data-replication-mode-of-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ✔️ | ✔️ | ❌ | ❌ |
| [实例回收站](manage-apsaradb-rds-for-postgresql-instances-in-the-recycle-bin.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [Babelfish for RDS PostgreSQL](babelfish-for-apsaradb-rds-for-postgresql.md) | ❌ | ❌ | ❌ | ❌ | ❌ |
| [只读实例](rds-for-postgresql-read-only-instances.md) | ❌ | ✔️ | ❌ | ❌ | ❌ |
| [数据库代理（读写分离）](database-proxy.md) | ❌ | ✔️ | ❌ | ❌ | ❌ |
| [创建账号](create-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [重置密码](reset-the-password-of-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [RDS PostgreSQL](connect-an-apsaradb-rds-for-postgresql-instance-to-a-self-managed-ad-domain.md) [接入自建域](connect-an-apsaradb-rds-for-postgresql-instance-to-a-self-managed-ad-domain.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [锁定/删除账号](lock-or-delete-an-account-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [连接](connect-to-an-apsaradb-rds-for-postgresql-instance.md) [PostgreSQL](connect-to-an-apsaradb-rds-for-postgresql-instance.md) [实例](connect-to-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [开通或关闭外网地址](apply-for-or-release-a-public-endpoint-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查看或修改内外网地址和端口](view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [更改网络类型](change-the-network-type-of-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ❌ | ❌ | ❌ |
| [切换虚拟交换机](switch-an-apsaradb-rds-for-postgresql-instance-to-a-different-vswitch.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [创建数据库](create-a-database-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [删除数据库](delete-a-database-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [修改时区](change-the-time-zone-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [插件](extensions-supported-by-apsaradb-rds-for-postgresql.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查看增强监控](view-the-enhanced-monitoring-metrics-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [管理报警](manage-the-alert-rules-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [切换高安全白名单模式](switch-an-apsaradb-rds-for-postgresql-instance-to-the-enhanced-whitelist-mode.md) | ❌ | ❌ | ❌ | ❌ | ❌ |
| [设置白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [SSL](ssl-encryption.md) [链路加密](ssl-encryption.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [云盘加密](configure-disk-encryption-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [全密态云数据库](fully-encrypted-database.md) | ✔️ | 非安全增强型实例：✔️ 安全增强型实例：❌ | ❌ | ✔️ | ❌ |
| [透明数据加密](https://help.aliyun.com/zh/document_detail/465651.html#concept-2272850) [TDE](https://help.aliyun.com/zh/document_detail/465651.html#concept-2272850) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [SQL](../use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) [审计（数据库审计）](../use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [日志管理](view-the-logs-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [任务中心](task-list.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [备份数据](back-up-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [跨地域备份](use-the-cross-region-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [稀疏备份](sparse-backup-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [高频快照备份](use-the-high-frequency-snapshot-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [下载备份](download-the-backup-files-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ❌ | ✔️ |
| [删除备份](delete-backup-files-or-reduce-the-size-of-backup-files.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [恢复数据](restore-data-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [恢复库表](restore-individual-databases-and-tables-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [跨地域恢复](restore-the-data-of-an-apsaradb-rds-for-postgresql-instance-across-regions.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [自治服务](performance-optimization-and-diagnosis-1.md) [DAS](performance-optimization-and-diagnosis-1.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ |
| [创建标签](add-tags-to-apsaradb-rds-instances-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [删除标签](remove-tags-from-an-apsaradb-rds-for-mysql-instance-2.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
## PostgreSQL 16
| 功能 | 集群系列 | 高可用系列 | 基础系列 |  |  |
| --- | --- | --- | --- | --- | --- |
| 包年包月/按量付费 | 包年包月/按量付费 | Serverless | 包年包月/按量付费 | Serverless |  |
| [一键上云](cloud-migration.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [数据迁移](data-migration-2.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [数据同步](manage-dataconnectors.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [数据订阅](change-tracking.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [升级数据库大版本](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [创建实例](create-an-apsaradb-rds-for-postgresql-instance-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [变更配置](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [重启实例](restart-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [变更资源扩缩容范围（RCU）](change-the-scaling-range-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| [设置实例自动启停](configure-the-automatic-start-and-stop-feature-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| [变更实例弹性策略](change-the-scaling-policy-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| [暂停实例](suspend-an-rds-instance-2.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [自动或手动主备切换](switch-workloads-over-between-primary-and-secondary-apsaradb-rds-for-postgresql-instances.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ |
| [设置可维护时间段](set-the-maintenance-window-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [设置存储空间自动扩容](configure-automatic-storage-expansion-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [迁移可用区](migrate-an-apsaradb-rds-for-postgresql-instance-across-zones-in-the-same-region.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [释放实例](release-or-unsubscribe-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [开启和关闭实例释放保护](enable-or-disable-the-release-protection-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [设置实例参数](modify-the-parameters-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查询和修改数据复制方式](change-the-data-replication-mode-of-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ✔️ | ✔️ | ❌ | ❌ |
| [实例回收站](manage-apsaradb-rds-for-postgresql-instances-in-the-recycle-bin.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [Babelfish for RDS PostgreSQL](babelfish-for-apsaradb-rds-for-postgresql.md) | ❌ | ❌ | ❌ | ❌ | ❌ |
| [只读实例](rds-for-postgresql-read-only-instances.md) | ❌ | ✔️ | ❌ | ❌ | ❌ |
| [数据库代理（读写分离）](database-proxy.md) | ❌ | ✔️ | ❌ | ❌ | ❌ |
| [创建账号](create-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [重置密码](reset-the-password-of-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [RDS PostgreSQL](connect-an-apsaradb-rds-for-postgresql-instance-to-a-self-managed-ad-domain.md) [接入自建域](connect-an-apsaradb-rds-for-postgresql-instance-to-a-self-managed-ad-domain.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [锁定/删除账号](lock-or-delete-an-account-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [连接](connect-to-an-apsaradb-rds-for-postgresql-instance.md) [PostgreSQL](connect-to-an-apsaradb-rds-for-postgresql-instance.md) [实例](connect-to-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [开通或关闭外网地址](apply-for-or-release-a-public-endpoint-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查看或修改内外网地址和端口](view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [更改网络类型](change-the-network-type-of-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ❌ | ❌ | ❌ |
| [切换虚拟交换机](switch-an-apsaradb-rds-for-postgresql-instance-to-a-different-vswitch.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [创建数据库](create-a-database-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [删除数据库](delete-a-database-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [修改时区](change-the-time-zone-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [插件](extensions-supported-by-apsaradb-rds-for-postgresql.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查看增强监控](view-the-enhanced-monitoring-metrics-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [管理报警](manage-the-alert-rules-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [切换高安全白名单模式](switch-an-apsaradb-rds-for-postgresql-instance-to-the-enhanced-whitelist-mode.md) | ❌ | ❌ | ❌ | ❌ | ❌ |
| [设置白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [SSL](ssl-encryption.md) [链路加密](ssl-encryption.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [云盘加密](configure-disk-encryption-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [全密态云数据库](fully-encrypted-database.md) | ✔️ | 非安全增强型实例：✔️ 安全增强型实例：❌ | ❌ | ✔️ | ❌ |
| [透明数据加密](https://help.aliyun.com/zh/document_detail/465651.html#concept-2272850) [TDE](https://help.aliyun.com/zh/document_detail/465651.html#concept-2272850) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [SQL](../use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) [审计（数据库审计）](../use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [日志管理](view-the-logs-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [任务中心](task-list.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [备份数据](back-up-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [跨地域备份](use-the-cross-region-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [稀疏备份](sparse-backup-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [高频快照备份](use-the-high-frequency-snapshot-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [下载备份](download-the-backup-files-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ❌ | ✔️ |
| [删除备份](delete-backup-files-or-reduce-the-size-of-backup-files.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [恢复数据](restore-data-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [恢复库表](restore-individual-databases-and-tables-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [跨地域恢复](restore-the-data-of-an-apsaradb-rds-for-postgresql-instance-across-regions.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [自治服务](performance-optimization-and-diagnosis-1.md) [DAS](performance-optimization-and-diagnosis-1.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ |
| [创建标签](add-tags-to-apsaradb-rds-instances-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [删除标签](remove-tags-from-an-apsaradb-rds-for-mysql-instance-2.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
## PostgreSQL 15
| 功能 | 集群系列 | 高可用系列 | 基础系列 |  |  |
| --- | --- | --- | --- | --- | --- |
| 包年包月/按量付费 | 包年包月/按量付费 | Serverless | 包年包月/按量付费 | Serverless |  |
| [一键上云](cloud-migration.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [数据迁移](data-migration-2.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [数据同步](manage-dataconnectors.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [数据订阅](change-tracking.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [升级数据库大版本](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [创建实例](create-an-apsaradb-rds-for-postgresql-instance-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [变更配置](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [重启实例](restart-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [变更资源扩缩容范围（RCU）](change-the-scaling-range-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| [设置实例自动启停](configure-the-automatic-start-and-stop-feature-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| [变更实例弹性策略](change-the-scaling-policy-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| [暂停实例](suspend-an-rds-instance-2.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [自动或手动主备切换](switch-workloads-over-between-primary-and-secondary-apsaradb-rds-for-postgresql-instances.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ |
| [设置可维护时间段](set-the-maintenance-window-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [设置存储空间自动扩容](configure-automatic-storage-expansion-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [迁移可用区](migrate-an-apsaradb-rds-for-postgresql-instance-across-zones-in-the-same-region.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [释放实例](release-or-unsubscribe-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [开启和关闭实例释放保护](enable-or-disable-the-release-protection-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [设置实例参数](modify-the-parameters-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查询和修改数据复制方式](change-the-data-replication-mode-of-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ✔️ | ✔️ | ❌ | ❌ |
| [实例回收站](manage-apsaradb-rds-for-postgresql-instances-in-the-recycle-bin.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [Babelfish for RDS PostgreSQL](babelfish-for-apsaradb-rds-for-postgresql.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [只读实例](rds-for-postgresql-read-only-instances.md) | ❌ | ✔️ | ❌ | ❌ | ❌ |
| [数据库代理（读写分离）](database-proxy.md) | ❌ | ✔️ | ❌ | ❌ | ❌ |
| [创建账号](create-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [重置密码](reset-the-password-of-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [RDS PostgreSQL](connect-an-apsaradb-rds-for-postgresql-instance-to-a-self-managed-ad-domain.md) [接入自建域](connect-an-apsaradb-rds-for-postgresql-instance-to-a-self-managed-ad-domain.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [锁定/删除账号](lock-or-delete-an-account-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [连接](connect-to-an-apsaradb-rds-for-postgresql-instance.md) [PostgreSQL](connect-to-an-apsaradb-rds-for-postgresql-instance.md) [实例](connect-to-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [开通或关闭外网地址](apply-for-or-release-a-public-endpoint-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查看或修改内外网地址和端口](view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [更改网络类型](change-the-network-type-of-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ❌ | ❌ | ❌ |
| [切换虚拟交换机](switch-an-apsaradb-rds-for-postgresql-instance-to-a-different-vswitch.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [创建数据库](create-a-database-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [删除数据库](delete-a-database-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [修改时区](change-the-time-zone-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [插件](extensions-supported-by-apsaradb-rds-for-postgresql.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查看增强监控](view-the-enhanced-monitoring-metrics-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [管理报警](manage-the-alert-rules-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [切换高安全白名单模式](switch-an-apsaradb-rds-for-postgresql-instance-to-the-enhanced-whitelist-mode.md) | ❌ | ❌ | ❌ | ❌ | ❌ |
| [设置白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [SSL](ssl-encryption.md) [链路加密](ssl-encryption.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [云盘加密](configure-disk-encryption-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [全密态云数据库](fully-encrypted-database.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [透明数据加密](https://help.aliyun.com/zh/document_detail/465651.html#concept-2272850) [TDE](https://help.aliyun.com/zh/document_detail/465651.html#concept-2272850) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [SQL](../use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) [审计（数据库审计）](../use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [日志管理](view-the-logs-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [任务中心](task-list.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [备份数据](back-up-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [跨地域备份](use-the-cross-region-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [稀疏备份](sparse-backup-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [高频快照备份](use-the-high-frequency-snapshot-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [下载备份](download-the-backup-files-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [删除备份](delete-backup-files-or-reduce-the-size-of-backup-files.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [恢复数据](restore-data-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [恢复库表](restore-individual-databases-and-tables-of-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [跨地域恢复](restore-the-data-of-an-apsaradb-rds-for-postgresql-instance-across-regions.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [自治服务](performance-optimization-and-diagnosis-1.md) [DAS](performance-optimization-and-diagnosis-1.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ |
| [创建标签](add-tags-to-apsaradb-rds-instances-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [删除标签](remove-tags-from-an-apsaradb-rds-for-mysql-instance-2.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
## PostgreSQL 14
| 功能 | 集群系列 | 高可用系列 | 基础系列 |  |  |
| --- | --- | --- | --- | --- | --- |
| 包年包月/按量付费 | 包年包月/按量付费 | Serverless | 包年包月/按量付费 | Serverless |  |
| [一键上云](cloud-migration.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [数据迁移](data-migration-2.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [数据同步](manage-dataconnectors.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [数据订阅](change-tracking.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [升级数据库大版本](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [创建实例](create-an-apsaradb-rds-for-postgresql-instance-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [变更配置](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [重启实例](restart-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [变更资源扩缩容范围（RCU）](change-the-scaling-range-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| [设置实例自动启停](configure-the-automatic-start-and-stop-feature-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| [变更实例弹性策略](change-the-scaling-policy-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| [暂停实例](suspend-an-rds-instance-2.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [自动或手动主备切换](switch-workloads-over-between-primary-and-secondary-apsaradb-rds-for-postgresql-instances.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ |
| [设置可维护时间段](set-the-maintenance-window-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [设置存储空间自动扩容](configure-automatic-storage-expansion-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [迁移可用区](migrate-an-apsaradb-rds-for-postgresql-instance-across-zones-in-the-same-region.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [释放实例](release-or-unsubscribe-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [开启和关闭实例释放保护](enable-or-disable-the-release-protection-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [设置实例参数](modify-the-parameters-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查询和修改数据复制方式](change-the-data-replication-mode-of-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ✔️ | ✔️ | ❌ | ❌ |
| [实例回收站](manage-apsaradb-rds-for-postgresql-instances-in-the-recycle-bin.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [Babelfish for RDS PostgreSQL](babelfish-for-apsaradb-rds-for-postgresql.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [只读实例](rds-for-postgresql-read-only-instances.md) | ❌ | ✔️ | ❌ | ❌ | ❌ |
| [数据库代理（读写分离）](database-proxy.md) | ❌ | ✔️ | ❌ | ❌ | ❌ |
| [创建账号](create-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [重置密码](reset-the-password-of-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [RDS PostgreSQL](connect-an-apsaradb-rds-for-postgresql-instance-to-a-self-managed-ad-domain.md) [接入自建域](connect-an-apsaradb-rds-for-postgresql-instance-to-a-self-managed-ad-domain.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [锁定/删除账号](lock-or-delete-an-account-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [连接](connect-to-an-apsaradb-rds-for-postgresql-instance.md) [PostgreSQL](connect-to-an-apsaradb-rds-for-postgresql-instance.md) [实例](connect-to-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [开通或关闭外网地址](apply-for-or-release-a-public-endpoint-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查看或修改内外网地址和端口](view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [更改网络类型](change-the-network-type-of-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ | ❌ | ❌ | ❌ |
| [切换虚拟交换机](switch-an-apsaradb-rds-for-postgresql-instance-to-a-different-vswitch.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [创建数据库](create-a-database-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [删除数据库](delete-a-database-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [修改时区](change-the-time-zone-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [插件](extensions-supported-by-apsaradb-rds-for-postgresql.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查看增强监控](view-the-enhanced-monitoring-metrics-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [管理报警](manage-the-alert-rules-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [切换高安全白名单模式](switch-an-apsaradb-rds-for-postgresql-instance-to-the-enhanced-whitelist-mode.md) | ❌ | ❌ | ❌ | ❌ | ❌ |
| [设置白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [SSL](ssl-encryption.md) [链路加密](ssl-encryption.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [云盘加密](configure-disk-encryption-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [全密态云数据库](fully-encrypted-database.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [透明数据加密](https://help.aliyun.com/zh/document_detail/465651.html#concept-2272850) [TDE](https://help.aliyun.com/zh/document_detail/465651.html#concept-2272850) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [SQL](../use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) [审计（数据库审计）](../use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [日志管理](view-the-logs-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [任务中心](task-list.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [备份数据](back-up-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [跨地域备份](use-the-cross-region-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [稀疏备份](sparse-backup-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [高频快照备份](use-the-high-frequency-snapshot-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [下载备份](download-the-backup-files-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [删除备份](delete-backup-files-or-reduce-the-size-of-backup-files.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [恢复数据](restore-data-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [恢复库表](restore-individual-databases-and-tables-of-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ✔️ | ❌ | ✔️ | ❌ |
| [跨地域恢复](restore-the-data-of-an-apsaradb-rds-for-postgresql-instance-across-regions.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ |
| [自治服务](performance-optimization-and-diagnosis-1.md) [DAS](performance-optimization-and-diagnosis-1.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ |
| [创建标签](add-tags-to-apsaradb-rds-instances-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [删除标签](remove-tags-from-an-apsaradb-rds-for-mysql-instance-2.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
## PostgreSQL 13
| 功能 | 高可用系列 | 基础系列 |
| --- | --- | --- |
| [一键上云](cloud-migration.md) | ✔️ | ✔️ |
| [数据迁移](data-migration-2.md) | ✔️ | ✔️ |
| [数据同步](manage-dataconnectors.md) | ✔️ | ✔️ |
| [数据订阅](change-tracking.md) | ✔️ | ✔️ |
| [升级数据库大版本](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [创建实例](create-an-apsaradb-rds-for-postgresql-instance-1.md) | ✔️ | ✔️ |
| [变更配置](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [重启实例](restart-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [变更资源扩缩容范围（RCU）](change-the-scaling-range-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ |
| [设置实例自动启停](configure-the-automatic-start-and-stop-feature-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ |
| [变更实例弹性策略](change-the-scaling-policy-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ |
| [暂停实例](suspend-an-rds-instance-2.md) | ✔️ | ✔️ |
| [自动或手动主备切换](switch-workloads-over-between-primary-and-secondary-apsaradb-rds-for-postgresql-instances.md) | ✔️ | ❌ |
| [设置可维护时间段](set-the-maintenance-window-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [设置存储空间自动扩容](configure-automatic-storage-expansion-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [迁移可用区](migrate-an-apsaradb-rds-for-postgresql-instance-across-zones-in-the-same-region.md) | ✔️ | ✔️ |
| [释放实例](release-or-unsubscribe-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [开启和关闭实例释放保护](enable-or-disable-the-release-protection-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [设置实例参数](modify-the-parameters-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [查询和修改数据复制方式](change-the-data-replication-mode-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ❌ |
| [实例回收站](manage-apsaradb-rds-for-postgresql-instances-in-the-recycle-bin.md) | ✔️ | ✔️ |
| [Babelfish for RDS PostgreSQL](babelfish-for-apsaradb-rds-for-postgresql.md) | ✔️ | ✔️ |
| [只读实例](rds-for-postgresql-read-only-instances.md) | ✔️ | ❌ |
| [数据库代理（读写分离）](database-proxy.md) | ✔️ | ❌ |
| [创建账号](create-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [重置密码](reset-the-password-of-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [RDS PostgreSQL](connect-an-apsaradb-rds-for-postgresql-instance-to-a-self-managed-ad-domain.md) [接入自建域](connect-an-apsaradb-rds-for-postgresql-instance-to-a-self-managed-ad-domain.md) | ✔️ | ✔️ |
| [锁定/删除账号](lock-or-delete-an-account-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [连接](connect-to-an-apsaradb-rds-for-postgresql-instance.md) [PostgreSQL](connect-to-an-apsaradb-rds-for-postgresql-instance.md) [实例](connect-to-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [开通或关闭外网地址](apply-for-or-release-a-public-endpoint-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [查看或修改内外网地址和端口](view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [更改网络类型](change-the-network-type-of-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ |
| [切换虚拟交换机](switch-an-apsaradb-rds-for-postgresql-instance-to-a-different-vswitch.md) | ✔️ | ✔️ |
| [创建数据库](create-a-database-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [删除数据库](delete-a-database-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [修改时区](change-the-time-zone-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [插件](extensions-supported-by-apsaradb-rds-for-postgresql.md) | ✔️ | ✔️ |
| [查看增强监控](view-the-enhanced-monitoring-metrics-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [管理报警](manage-the-alert-rules-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [切换高安全白名单模式](switch-an-apsaradb-rds-for-postgresql-instance-to-the-enhanced-whitelist-mode.md) | ❌ | ❌ |
| [设置白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance-1.md) | ✔️ | ✔️ |
| [SSL](ssl-encryption.md) [链路加密](ssl-encryption.md) | ✔️ | ✔️ |
| [云盘加密](configure-disk-encryption-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [全密态云数据库](fully-encrypted-database.md) | ✔️ | ✔️ |
| [透明数据加密](https://help.aliyun.com/zh/document_detail/465651.html#concept-2272850) [TDE](https://help.aliyun.com/zh/document_detail/465651.html#concept-2272850) | ✔️ | ✔️ |
| [SQL](../use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) [审计（数据库审计）](../use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [日志管理](view-the-logs-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [任务中心](task-list.md) | ✔️ | ✔️ |
| [备份数据](back-up-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [跨地域备份](use-the-cross-region-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [稀疏备份](sparse-backup-1.md) | ✔️ | ✔️ |
| [高频快照备份](use-the-high-frequency-snapshot-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [下载备份](download-the-backup-files-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [删除备份](delete-backup-files-or-reduce-the-size-of-backup-files.md) | ✔️ | ✔️ |
| [恢复数据](restore-data-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [恢复库表](restore-individual-databases-and-tables-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [跨地域恢复](restore-the-data-of-an-apsaradb-rds-for-postgresql-instance-across-regions.md) | ✔️ | ✔️ |
| [自治服务](performance-optimization-and-diagnosis-1.md) [DAS](performance-optimization-and-diagnosis-1.md) | ✔️ | ❌ |
| [创建标签](add-tags-to-apsaradb-rds-instances-1.md) | ✔️ | ✔️ |
| [删除标签](remove-tags-from-an-apsaradb-rds-for-mysql-instance-2.md) | ✔️ | ✔️ |
## PostgreSQL 12、11
| 功能 | 高可用系列 | 基础系列 |
| --- | --- | --- |
| [一键上云](cloud-migration.md) | ✔️ | ✔️ |
| [数据迁移](data-migration-2.md) | ✔️ | ✔️ |
| [数据同步](manage-dataconnectors.md) | ✔️ | ✔️ |
| [数据订阅](change-tracking.md) | ✔️ | ✔️ |
| [升级数据库大版本](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [创建实例](create-an-apsaradb-rds-for-postgresql-instance-1.md) | ✔️ | ✔️ |
| [变更配置](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [重启实例](restart-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [变更资源扩缩容范围（RCU）](change-the-scaling-range-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ |
| [设置实例自动启停](configure-the-automatic-start-and-stop-feature-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ |
| [变更实例弹性策略](change-the-scaling-policy-of-rcus-for-a-serverless-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ |
| [暂停实例](suspend-an-rds-instance-2.md) | ✔️ | ✔️ |
| [自动或手动主备切换](switch-workloads-over-between-primary-and-secondary-apsaradb-rds-for-postgresql-instances.md) | ✔️ | ❌ |
| [设置可维护时间段](set-the-maintenance-window-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [设置存储空间自动扩容](configure-automatic-storage-expansion-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [迁移可用区](migrate-an-apsaradb-rds-for-postgresql-instance-across-zones-in-the-same-region.md) | ✔️ | ✔️ |
| [释放实例](release-or-unsubscribe-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [开启和关闭实例释放保护](enable-or-disable-the-release-protection-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [设置实例参数](modify-the-parameters-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [查询和修改数据复制方式](change-the-data-replication-mode-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ❌ |
| [实例回收站](manage-apsaradb-rds-for-postgresql-instances-in-the-recycle-bin.md) | ✔️ | ✔️ |
| [Babelfish for RDS PostgreSQL](babelfish-for-apsaradb-rds-for-postgresql.md) | ❌ | ❌ |
| [只读实例](rds-for-postgresql-read-only-instances.md) | ✔️ | ❌ |
| [数据库代理（读写分离）](database-proxy.md) | ✔️ | ❌ |
| [创建账号](create-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [重置密码](reset-the-password-of-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [RDS PostgreSQL](connect-an-apsaradb-rds-for-postgresql-instance-to-a-self-managed-ad-domain.md) [接入自建域](connect-an-apsaradb-rds-for-postgresql-instance-to-a-self-managed-ad-domain.md) | ✔️ | ✔️ |
| [锁定/删除账号](lock-or-delete-an-account-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [连接](connect-to-an-apsaradb-rds-for-postgresql-instance.md) [PostgreSQL](connect-to-an-apsaradb-rds-for-postgresql-instance.md) [实例](connect-to-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [开通或关闭外网地址](apply-for-or-release-a-public-endpoint-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [查看或修改内外网地址和端口](view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [更改网络类型](change-the-network-type-of-an-apsaradb-rds-for-postgresql-instance.md) | ❌ | ❌ |
| [切换虚拟交换机](switch-an-apsaradb-rds-for-postgresql-instance-to-a-different-vswitch.md) | ✔️ | ✔️ |
| [创建数据库](create-a-database-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [删除数据库](delete-a-database-from-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [修改时区](change-the-time-zone-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [插件](extensions-supported-by-apsaradb-rds-for-postgresql.md) | ✔️ | ✔️ |
| [查看增强监控](view-the-enhanced-monitoring-metrics-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [管理报警](manage-the-alert-rules-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [切换高安全白名单模式](switch-an-apsaradb-rds-for-postgresql-instance-to-the-enhanced-whitelist-mode.md) | ❌ | ❌ |
| [设置白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance-1.md) | ✔️ | ✔️ |
| [SSL](ssl-encryption.md) [链路加密](ssl-encryption.md) | ✔️ | ✔️ |
| [云盘加密](configure-disk-encryption-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [全密态云数据库](fully-encrypted-database.md) | ✔️ | ✔️ |
| [透明数据加密](https://help.aliyun.com/zh/document_detail/465651.html#concept-2272850) [TDE](https://help.aliyun.com/zh/document_detail/465651.html#concept-2272850) | ✔️ | ✔️ |
| [SQL](../use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) [审计（数据库审计）](../use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [日志管理](view-the-logs-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [任务中心](task-list.md) | ✔️ | ✔️ |
| [备份数据](back-up-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [跨地域备份](use-the-cross-region-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [稀疏备份](sparse-backup-1.md) | ✔️ | ✔️ |
| [高频快照备份](use-the-high-frequency-snapshot-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [下载备份](download-the-backup-files-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [删除备份](delete-backup-files-or-reduce-the-size-of-backup-files.md) | ✔️ | ✔️ |
| [恢复数据](restore-data-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [恢复库表](restore-individual-databases-and-tables-of-an-apsaradb-rds-for-postgresql-instance.md) | ✔️ | ✔️ |
| [跨地域恢复](restore-the-data-of-an-apsaradb-rds-for-postgresql-instance-across-regions.md) | ✔️ | ✔️ |
| [自治服务](performance-optimization-and-diagnosis-1.md) [DAS](performance-optimization-and-diagnosis-1.md) | ✔️ | ❌ |
| [创建标签](add-tags-to-apsaradb-rds-instances-1.md) | ✔️ | ✔️ |
| [删除标签](remove-tags-from-an-apsaradb-rds-for-mysql-instance-2.md) | ✔️ | ✔️ |
## 历史版本功能概览
PostgreSQL 10
| 功能 | PostgreSQL 10 |  |  |
| --- | --- | --- | --- |
| 高可用系列（高性能本地盘） | 高可用系列（云盘） | 基础系列（云盘） |  |
| 一键上云 | ❌ | ✔️ | ✔️ |
| 数据迁移 | ✔️ | ✔️ | ✔️ |
| 数据同步 | ✔️ | ✔️ | ✔️ |
| 数据订阅 | ✔️ | ✔️ | ✔️ |
| 升级数据库大版本 | ✔️ | ✔️ | ✔️ |
| 升级内核小版本 | ✔️ | ✔️ | ✔️ |
| 创建实例 | ✔️ | ✔️ | ✔️ |
| 变更配置 | ✔️ | ✔️ | ✔️ |
| 重启实例 | ✔️ | ✔️ | ✔️ |
| 变更资源扩缩容范围（RCU） | ❌ | ❌ | ❌ |
| 设置实例自动启停 | ❌ | ❌ | ❌ |
| 变更实例弹性策略 | ❌ | ❌ | ❌ |
| 暂停实例 | ❌ | ✔️ | ✔️ |
| 自动或手动主备切换 | ✔️ | ✔️ | ❌ |
| 设置可维护时间段 | ✔️ | ✔️ | ✔️ |
| 设置存储空间自动扩容 | ❌ | ✔️ | ✔️ |
| 迁移可用区 | ✔️ | ✔️ | ✔️ |
| 释放实例 | ✔️ | ✔️ | ✔️ |
| 开启和关闭实例释放保护 | ✔️ | ✔️ | ✔️ |
| 设置实例参数 | ✔️ | ✔️ | ✔️ |
| 设置实例保护级别 | ❌ | ✔️ | ❌ |
| 实例回收站 | ✔️ | ✔️ | ✔️ |
| Babelfish for RDS PostgreSQL | ❌ | ❌ | ❌ |
| 只读实例 | ✔️ | ✔️ | ❌ |
| 数据库代理（读写分离） | ❌ | ✔️ | ❌ |
| 创建账号 | ✔️ | ✔️ | ✔️ |
| 重置密码 | ✔️ | ✔️ | ✔️ |
| RDS PostgreSQL 接入自建域 | ❌ | ✔️ | ✔️ |
| 锁定/删除账号 | ✔️ | ✔️ | ✔️ |
| 连接 PostgreSQL 实例 | ✔️ | ✔️ | ✔️ |
| 申请或释放外网地址 | ✔️ | ✔️ | ✔️ |
| 查看或修改内外网地址和端口 | ✔️ | ✔️ | ✔️ |
| 更改网络类型 | ✔️ | ❌ | ❌ |
| 切换虚拟交换机 | ❌ | ✔️ | ✔️ |
| 创建数据库 | ✔️ | ✔️ | ✔️ |
| 删除数据库 | ✔️ | ✔️ | ✔️ |
| 修改时区 | ❌ | ✔️ | ✔️ |
| 插件 | ✔️ | ✔️ | ✔️ |
| 查看增强监控 | ✔️ | ✔️ | ✔️ |
| 管理报警 | ✔️ | ✔️ | ✔️ |
| 切换高安全白名单模式 | ✔️ | ❌ | ❌ |
| 设置白名单 | ✔️ | ✔️ | ✔️ |
| SSL 链路加密 | ❌ | ✔️ | ✔️ |
| 云盘加密 | ❌ | ✔️ | ✔️ |
| 全密态云数据库 | ❌ | ✔️ | ❌ |
| 透明数据加密 TDE | ❌ | ✔️ | ✔️ |
| SQL 审计（数据库审计） | ✔️ | ✔️ | ✔️ |
| 日志管理 | ✔️ | ✔️ | ✔️ |
| 任务中心 | ✔️ | ✔️ | ✔️ |
| 备份数据 | ✔️ | ✔️ | ✔️ |
| 跨地域备份 | ✔️ | ✔️ | ✔️ |
| 稀疏备份 | ❌ | ✔️ | ✔️ |
| 高频快照备份 | ❌ | ✔️ | ✔️ |
| 下载备份 | ✔️ | ✔️ | ✔️ |
| 删除备份 | ✔️ | ✔️ | ✔️ |
| 恢复数据 | ✔️ | ✔️ | ✔️ |
| 恢复库表 | ❌ | ✔️ | ✔️ |
| 跨地域恢复 | ✔️ | ✔️ | ✔️ |
| 自治服务 DAS | ✔️ | ✔️ | ❌ |
| 创建标签 | ✔️ | ✔️ | ✔️ |
| 删除标签 | ✔️ | ✔️ | ✔️ |
PostgreSQL 9.4
| 类别 | 功能 | 高可用版（高性能本地盘） |
| --- | --- | --- |
| 数据迁移同步 | 数据迁移同步 | ✔️ |
| RDS PostgreSQL 间数据双向同步 | RDS PostgreSQL 间的双向同步 | ✔️ |
| 数据订阅 | 创建 RDS PostgreSQL 数据订阅任务 | ✔️ |
| 实例管理 | 创建实例 | ✔️ |
| 变更配置 | ❌️ |  |
| 设置实例参数 | ✔️ |  |
| 查询和修改数据复制方式 | ❌️ |  |
| 迁移可用区 | ✔️ |  |
| 切换主备实例 | ✔️ |  |
| 重启实例 | ✔️ |  |
| 设置可维护时间段 | ✔️ |  |
| 升级数据库大版本 | ✔️ |  |
| 释放实例 | ✔️ |  |
| 实例回收站 | ✔️ |  |
| 账号管理 | 创建账号 | ✔️ |
| 重置密码 | ✔️ |  |
| 锁定账号 | ✔️ |  |
| 删除账号 | ✔️ |  |
| 数据库管理 | 创建数据库 | ✔️ |
| 删除数据库 | ✔️ |  |
| 插件 | ✔️ |  |
| 数据库连接 | 连接 PostgreSQL 实例 | ✔️ |
| 设置连接地址 | ✔️ |  |
| 查看连接地址/端口 | ✔️ |  |
| 申请或释放外网地址 | ✔️ |  |
| 监控报警 | 查看资源和引擎监控 | ✔️ |
| 设置监控频率 | ✔️ |  |
| 管理报警 | ✔️ |  |
| 网络管理 | 切换网络类型 | ✔️ |
| 切换虚拟交换机 | ❌️ |  |
| 只读实例 | 创建只读实例 | ❌️ |
| 安全管理 | 设置白名单 | ✔️ |
| 设置 SSL 加密 | ❌️ |  |
| 设置云盘加密 | ❌️ |  |
| 切换高安全白名单模式 | ✔️ |  |
| 全密态云数据库 | ✔️ |  |
| 审计 | SQL 审计（数据库审计） | ✔️ |
| 日志管理 | ✔️ |  |
| 历史事件 | ✔️ |  |
| 数据库备份 | 备份数据 | ✔️ |
| 跨地域备份 | ✔️ |  |
| 免费额度 | ✔️ |  |
| 下载备份 | ✔️ |  |
| 数据库恢复 | 恢复数据 | ❌️ |
| 跨地域恢复 | ❌️ |  |
| 诊断优化 | CloudDBA | ✔️ |
| 逻辑订阅 | 逻辑订阅 | ❌️ |
| 标签管理 | 创建标签 | ✔️ |
| 删除标签 | ✔️ |  |
| 根据标签筛选实例 | ✔️ |  |
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
