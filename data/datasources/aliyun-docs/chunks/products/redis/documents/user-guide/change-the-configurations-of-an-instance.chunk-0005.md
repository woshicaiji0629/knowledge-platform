### 高可用（双副本）实例如何变更为单副本实例？
由于单副本无数据可靠性保证，因此不支持将高可用实例变配为单副本实例。
如有需要，请单独购买高可用实例，再通过DTS将高可用实例的数据迁移到单副本实例，更多信息请参见[云数据库](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-apsaradb-for-redis-instances#task-2119264)[Tair（兼容](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-apsaradb-for-redis-instances#task-2119264)[Redis）间的迁移](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-apsaradb-for-redis-instances#task-2119264)。
