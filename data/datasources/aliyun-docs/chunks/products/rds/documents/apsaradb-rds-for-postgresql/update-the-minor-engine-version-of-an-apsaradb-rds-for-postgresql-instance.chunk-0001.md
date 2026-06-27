## 注意事项
升级内核小版本会重启实例，RDS服务可能会出现一次30秒的闪断，请您尽量在业务低峰期执行升级操作，或确保您的应用有自动重连机制。
升级内核小版本后无法降级。
小版本升级通常不会出现兼容性问题，但因插件的升级有可能会有兼容性问题，如果涉及到插件升级（如Ganos插件版本升级），建议先使用[恢复](restore-data-of-an-apsaradb-rds-for-postgresql-instance.md)[PostgreSQL](restore-data-of-an-apsaradb-rds-for-postgresql-instance.md)[数据](restore-data-of-an-apsaradb-rds-for-postgresql-instance.md)功能，在恢复的新实例上测试新版本插件的兼容性。
相关插件升级注意事项：
如果您的业务已经使用了PostGIS或Ganos插件，在升级内核小版本后，还需要手动升级PostGIS或Ganos插件，升级方法，请参见[时空引擎插件升级](how-do-i-update-the-plug-ins-of-ganos.md)。
如果您的实例大版本为PostgreSQL 14，在20230330内核小版本前已使用了[TimescaleDB](use-the-timescaledb-extension.md)插件（插件版本小于等于2.5.0），在升级内核小版本到20230330或以上版本后，必须手动执行ALTER EXTENSION timescaledb UPDATE;命令进行手动升级插件后，才能继续使用TimescaleDB插件。
