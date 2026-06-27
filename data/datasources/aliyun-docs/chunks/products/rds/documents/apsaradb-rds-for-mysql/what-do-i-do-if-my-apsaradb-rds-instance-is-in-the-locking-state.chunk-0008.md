### 扩容存储空间
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在基本信息页面的配置信息区域单击变更配置，[扩容实例存储空间](change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。
完成支付后，您可在进入[任务中心](https://rdsnext.console.aliyun.com/jobCenter/cn-hangzhou)查看变配进度。
扩容时长与存储类型相关，具体如下。您可以访问[RDS](https://rdsnext.console.aliyun.com/dashboard/cn-hangzhou)[控制台首页](https://rdsnext.console.aliyun.com/dashboard/cn-hangzhou)，在左侧导航栏的任务中心中查看扩容进度。

| 存储类型 | 扩容时长 | 说明 |
| --- | --- | --- |
| 高性能本地盘 | 以实际情况为准。 | 本地无资源可用的情况下会触发跨机迁移，扩容时长受较多因素影响，推荐在业务低峰期进行扩容。 变配会出现约 15 秒的闪断，请在业务低峰期进行变配，并确保您的应用有自动重连机制。闪断期间，与数据库、账号、网络等相关的大部分操作都无法执行。 |
| 云盘 | 5 分钟左右。 | MySQL、PostgreSQL 云盘实例扩容期间不会发生业务闪断。 SQL Server 云盘实例 [扩容](../apsaradb-rds-for-sql-server/change-the-specifications-of-an-apsaradb-rds-for-sql-server-instance.md) 期间可能会出现一次约 30 秒的闪断，与数据库、账号、网络等相关的大部分操作都无法执行，请尽量在业务低峰期执行变配操作，或确保您的应用有自动重连机制。 目前部分实例已支持无损扩容能力，不会造成数据库访问中断。 |
