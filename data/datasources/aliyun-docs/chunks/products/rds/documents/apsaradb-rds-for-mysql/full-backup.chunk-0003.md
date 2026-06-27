## 注意事项
默认开启：数据备份（全量备份）默认开启且无法关闭，最少保留7天，频率最低每周两次。
内核版本限制：以下内核小版本的实例锁定后无法发起备份。
RDS MySQL 5.1、5.5：所有小版本。
RDS MySQL 5.6、5.7、8.0：20190815之前的小版本。
说明
如需升级实例的大版本或内核小版本，请参见[升级数据库版本](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)或[升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)。
更多详情，请参见[实例状态显示“锁定中”时如何解决](../support/what-do-i-do-if-my-apsaradb-rds-instance-is-in-the-locking-state.md)。
只读实例：仅支持设置[本地日志保留策略](view-and-delete-the-binary-log-files-of-an-apsaradb-rds-for-mysql-instance.md)，不支持设置自动备份策略。
DDL 操作：备份期间不要执行DDL操作，避免锁表导致备份失败。
避免业务高峰期：尽量选择业务低峰期进行备份。
备份恢复异常：备份的表数量超过5万张将无法进行库表恢复，数据库恢复（原克隆实例）功能不受影响。
无法备份：备份的表数量超过60万将无法进行备份。
备份策略修改：会立即触发一次全量备份。
