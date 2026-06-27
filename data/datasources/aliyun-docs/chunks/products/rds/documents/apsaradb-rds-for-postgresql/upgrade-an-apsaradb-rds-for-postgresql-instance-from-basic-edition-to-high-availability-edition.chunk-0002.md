## 操作步骤
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在基本信息页面的配置信息，单击变更配置。
（仅包年包月实例需要执行此步骤）在弹出的对话框中，选择立即升配，单击下一步。
设置如下参数。

| 参数名称 | 说明 |
| --- | --- |
| 产品系列 | 选择 高可用系列 。 |
| 存储类型 | 选择实例的存储类型。详情请参见 [存储类型介绍](storage-types-of-apsaradb-rds-for-postgresql.md) 。 说明 仅当原实例的存储类型为 ESSD 云盘时，支持此参数。 |
| 实例规格 | 选择实例规格。每种规格都有对应的 CPU 核数、内存、最大连接数和最大 IOPS。详情请参见 [主实例规格列表](../product-overview/primary-apsaradb-rds-instance-types.md) 。 |
| 存储空间 | 设置存储空间。存储空间只能增加，不能降低。 |
| 切换时间 | 选择升级的切换时间： 立即执行 可维护时间内进行切换 |

阅读服务协议后，单击确认下单并完成支付。
