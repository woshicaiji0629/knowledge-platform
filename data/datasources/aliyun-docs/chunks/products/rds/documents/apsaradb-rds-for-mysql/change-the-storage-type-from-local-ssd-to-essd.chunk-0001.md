## 前提条件
RDS MySQL主实例仅支持如下版本：
RDS MySQL 8.0或5.7高可用系列（高性能本地盘）
说明
RDS MySQL 5.6版本实例仅支持高性能本地盘，不支持其他类型的云盘，因此无法直接将5.6版本的高性能本地盘变更为云盘，但您可以通过其他方案间接实现，详情请参见[本文常见问题](change-the-storage-type-from-local-ssd-to-essd.md)。
实例内核小版本不低于20201031，升级方法请参见[升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)。
实例下没有[只读实例](../overview-of-read-only-apsaradb-rds-for-mysql-instances.md)或[灾备实例](create-a-disaster-recovery-apsaradb-rds-for-mysql-instance.md)。
实例未开启[性能自动扩容](enable-the-automatic-scale-up-feature-for-an-apsaradb-rds-for-mysql-instance.md)。
实例未开启[数据库代理](enable-and-configure-the-dedicated-proxy-feature-for-an-apsaradb-rds-for-mysql-instance.md)。
实例的网络类型为VPC网络，且实例没有经典网络地址。
实例未使用IPv6网络协议、未创建多个VPC。（正常情况下无需关注，仅针对特殊场景）
实例的状态为运行中。
说明
如果您的实例受上述前提条件所限无法变更存储类型，可以通过创建一个高性能云盘或ESSD云盘的新实例，将旧实例数据迁移到新实例的方式进行变更。更多信息，请参见[RDS](migrate-data-between-apsaradb-rds-for-mysql-instances.md)[实例间数据迁移](migrate-data-between-apsaradb-rds-for-mysql-instances.md)。
