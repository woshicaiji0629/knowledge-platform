### 备份与恢复
Tair Serverless KV实例支持以下备份与恢复方案。

| 类别 | 实施方案 | 说明 |
| --- | --- | --- |
| 数据备份 | [自动或手动备份](../user-guide/automatic-or-manual-backup.md) | 实例会按照默认的策略自动备份数据，您可以根据业务需求修改自动备份策略，也可以手动发起备份。 |
| 数据恢复 | [从备份集恢复至新实例](../user-guide/restore-data-from-a-backup-set-to-a-new-instance.md) | 支持从指定的备份集创建新实例，新实例中的数据将和该备份集中的数据一致，可用于数据恢复、快速部署业务或数据验证等场景。 |
