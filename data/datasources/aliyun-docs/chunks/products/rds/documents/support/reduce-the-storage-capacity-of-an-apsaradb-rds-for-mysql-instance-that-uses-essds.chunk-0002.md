## 使用限制
缩容频率限制：每天最多手动缩容2次存储空间，请避免频繁缩容导致服务受损。
缩容条件与计算公式：
仅支持在同一系列、同一架构下缩容。
缩容后的最小存储空间需满足公式min{使用量*1.3，使用量+400 GB}，且不能低于当前规格允许的最小存储空间，存储空间调整步长为5 GB。
各级别云盘允许的最小存储空间+缩容示例
各级别云盘（ESSD云盘、高性能云盘）允许的最小存储空间为：
ESSD PL1：20 GB
ESSD PL2：500 GB
ESSD PL3：1500 GB
高性能云盘：10 GB
缩容示例
假设RDS MySQL实例的存储类型为ESSD PL1（允许最小存储空间为20 GB），原存储空间为2000 GB。根据不同的空间使用量，缩容后的最小空间如下：
空间使用量为10 GB：根据公式计算得13 GB，小于20 GB，则最小可缩容至20 GB。
空间使用量为500 GB：根据公式计算得650 GB，则最小可缩容至650 GB。
空间使用量为1500 GB：根据公式计算得1900 GB，则最小可缩容至1900 GB。
主实例与只读实例关系：只读实例的存储空间必须大于或等于其所属主实例的存储空间。建议先缩容主实例存储空间，再缩容只读实例的存储空间。
缩容时间与业务流量：缩容时间取决于云盘使用量和业务流量。高业务流量时，建议调整本地日志保留策略（增加日志保留时间和个数），以提高缩容效率和成功率。
Binlog日志要求：当实例Binlog产生较快时，需确保本地保留足够多的日志才能进行缩容。日志备份的开启方法，请参见[修改](../apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)[RDS](../apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)[备份策略](../apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)。
备份任务注意事项：缩容过程中可能会取消正在运行的备份任务，建议等备份完成后再进行缩容。
