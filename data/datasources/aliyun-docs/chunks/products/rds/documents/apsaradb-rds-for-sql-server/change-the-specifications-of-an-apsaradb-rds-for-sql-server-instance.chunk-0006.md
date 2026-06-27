## 常见问题
变更存储类型PL等级操作，是否会造成数据库访问中断？
RDS SQL Server部分实例支持无损扩容能力，在仅变更存储类型等级（PL等级，例如ESSD PL1变更为ESSD PL2）或扩容存储空间时，由于无损扩容不会造成数据库访问中断，因此您无需设置实例的切换时间。但如果您同时更改了实例规格，则仍需配置切换时间。
若您未更改任何配置项但变配实例页面仍显示切换时间选项，则说明您的RDS实例尚不支持无损扩容。您可以[升级实例大版本或小版本](upgrade-the-major-engine-version-and-rds-edition-of-an-apsaradb-rds-for-sql-server-instance.md)后再进行变更配置操作，以实现无损扩容。
可用区和版本可以变更吗？
非SQL Server 2008 R2实例：支持通过API（[ModifyDBInstanceSpec](api-rds-2014-08-15-modifydbinstancespec-sqlserver.md)）升级数据库大版本，并变更实例的可用区和交换机；也支持通过RDS控制台[升级数据库大版本](upgrade-the-major-engine-version-and-rds-edition-of-an-apsaradb-rds-for-sql-server-instance.md)。
SQL Server 2008 R2（高性能本地盘）实例：支持通过RDS控制台[升级版本](upgrade-an-apsaradb-rds-for-sql-server-instance-with-local-disks-from-sql-server-2008-r2-to-sql-server-2012-or-sql-server-2016.md)的同时变更可用区。
说明
您也可以单独[迁移可用区](migrate-an-apsaradb-rds-for-sql-server-instance-across-zones.md)。
仅扩容存储空间，需要迁移数据到新实例吗？
您只需要进行扩容操作即可，不需要手动迁移数据。扩容存储空间时，系统会检查实例所在主机上是否有足够存储空间用于扩容。如果有则直接扩容，不需要迁移数据；如果没有，系统会自动迁移数据到拥有足够存储空间的主机上。
变更配置大概需要多久？
变更配置涉及到数据迁移等，一般90%的变配可以在30分钟内完成。
CPU、内存、磁盘同时升配，会闪断多久？
无论是单独升配CPU、内存、磁盘中的一个，还是三个同时升配，闪断的时间都是一样的，一般是分钟级的。切换过程中，可能会出现业务闪断或实例重启，而且与数据库、账号、网络等相关的大部分操作都无法执行，请选择在可维护时间段内执行变配操作。各变更项的详情，请参见[变更项](ch
