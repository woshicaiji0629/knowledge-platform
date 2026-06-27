## 常见问题
如何变更RDS MySQL 5.6高性能本地盘为ESSD云盘或高性能云盘？
由于RDS MySQL 5.6版本实例仅支持高性能本地盘，不支持其他类型的云盘，因此无法直接将5.6版本的高性能本地盘变更为云盘，但您可以选择如下方案间接实现：
先[升级数据库大版本](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)
在RDS实例详情页的大版本升级页面（先创建升级检查报告再升级实例），将MySQL 5.6高性能本地盘升级为MySQL 5.7高性能本地盘或MySQL 8.0高性能本地盘，更多详情请参见[MySQL5.6](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)[升级](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)[MySQL 5.7](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)[的优势](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)。
页面提示不支持跨大版本升级（MySQL 5.6需先升级到5.7再到8.0）、升级后不支持降级，且检查失败时不允许执行升级操作。
再[变更存储类型](change-the-storage-type-from-local-ssd-to-essd.md)
在RDS实例详情页的基本信息页面，通过变更配置入口将MySQL 5.7高性能本地盘或MySQL 8.0高性能本地盘变更为MySQL 5.7云盘或MySQL 8.0云盘。
为什么我无法选择高性能云盘或者ESSD云盘？
部分可用区可能资源不足或暂时关闭云盘售卖的情况。若您的实例在不支持云盘售卖的可用区，请将实例[迁移至支持售卖云盘的可用区](migrate-an-apsaradb-rds-for-mysql-instance-across-zones-in-the-same-region.md)后，再升级至云盘。
变更存储类型时，是否会影响线上业务？
请参见本文的[影响](change-the-storage-type-from-local-ssd-to-essd.md)。
变更存储类型后，实例的地址会变化吗？
实例的连接地址（如rm-bpxxxxx.mysql.rds.aliyuncs.com）不会变化，但是对应的IP地址可能会变化。建议在应用程序中使用连接地址，
