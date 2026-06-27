## 操作步骤
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在基本信息页面的实例资源区域单击存储空间自动扩展右侧的设置。
说明
如果未找到设置按钮，请确认实例是否符合[前提条件](configure-automatic-storage-expansion-for-an-apsaradb-rds-for-mysql-instance.md)。
设置如下参数。

| 类别 | 说明 |
| --- | --- |
| 自动存储扩容 | 存储空间自动扩容的开关。 |
| 可用空间<= | 当剩余存储空间百分比达到设定的值时，会触发自动扩容。 说明 扩容的存储空间大小取下列二者中的最大值： 5 GB 存储空间。当实例存储总空间小于 50 GB，并且可用存储空间小于 10%时，扩容步长调整为 10 GB。 当前实例存储空间的 15%（结果取最近的 5 的倍数）。 例如，如果您当前存储总空间为 100 GB，其 15%为 15 GB，大于 5 GB，那么达到阈值触发扩容时将在原来存储空间的基础上扩容 15 GB，扩容成功后的总空间为 115 GB |
| 存储自动扩展上限 | 扩容后 实例总存储空间 的上限，需要大于等于实例当前存储空间总大小。 不同的云盘存储空间上限如下，您可以在此范围内进行设置： ESSD 云盘上限：32000 GB 高性能云盘上限：64000 GB SSD 云盘上限：6000 GB 说明 SSD 云盘已下线，建议升级至 [ESSD](upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md) [云盘](upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md) 。 |

单击确认。
