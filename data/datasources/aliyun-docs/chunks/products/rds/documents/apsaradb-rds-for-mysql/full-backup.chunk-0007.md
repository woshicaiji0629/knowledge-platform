## 执行备份
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在页面右上角，单击备份实例。
在备份实例对话框中，备份所有库或者特定库表，单击确定。
说明
备份方式的区别，请参见[逻辑备份、物理备份与快照](https://help.aliyun.com/zh/dbs/product-overview/backup-modes#multiTask1034)。

| [实例存储类型](../product-overview/storage-types.md) | 备份所有库 | 备份特定库表 |
| --- | --- | --- |
| 高性能本地盘实例 | 两种方式： 物理备份 （备份与恢复速度比逻辑备份快） 逻辑备份 > 实例备份 | 逻辑备份 > 单库备份 |
| 云盘实例 | 快照备份 | 不支持 |
