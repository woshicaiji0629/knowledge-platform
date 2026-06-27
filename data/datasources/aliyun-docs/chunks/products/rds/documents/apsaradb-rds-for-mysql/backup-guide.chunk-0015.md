## 备份的数据保护
防篡改：
RDS MySQL的全量物理备份和日志备份数据存储在OSS，全量快照备份存储在ESSD云盘快照服务，备份系统内部使用两种存储方式，都具备WORM（write once read many）不可篡改的特性。
防恶意/误删除：
用户手动删除：允许用户删除手动备份数据，但不允许用户删除自动备份的数据（参考文档：[删除或减少备份](delete-the-backup-files-or-reduce-the-size-of-backup-files-of-an-apsaradb-rds-for-mysql-instance.md)）
自动过期删除：可删除自动备份的数据。但同时限制了自动备份无法关闭，保留时长最低为7天，每周的备份次数最低为2次。（参考文档：[自动备份](enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)）。因此用户自动备份的全量和日志数据，无法完全删除。
