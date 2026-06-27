## 操作步骤
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在基本信息区域，单击配置信息右侧的变更配置。
在跳转的变配实例页面，选择存储类型。您可以选择高性能云盘或ESSD 云盘（PL1、PL2或PL3）。
部分可用区可能资源不足或暂时关闭云盘售卖的情况，因此可能无法选择存储类型为云盘。在这种情况下，请将实例[迁移至支持售卖云盘的可用区](migrate-an-apsaradb-rds-for-mysql-instance-across-zones-in-the-same-region.md)后，再升级至云盘。
说明
三种ESSD云盘的性能说明如下：
性能排序：PL3＞PL2＞PL1。
PL3比PL1最高提升20倍IOPS、11倍吞吐。
PL2比PL1最高提升2倍IOPS和吞吐。
需要注意PL3、PL2、PL1对应的最小磁盘空间不同，PL3为1500 GB、PL2为500 GB、PL1为20 GB。
[高性能云盘](https://help.aliyun.com/zh/document_detail/2545946.html)最小磁盘空间为10 GB。
（可选）选择新的实例规格。
先选择分类（通用或独享）。

| 分类 | 说明 | 特点 |
| --- | --- | --- |
| 通用规格 | 独享：内存和 I/O。 共享：CPU 和存储。 | 价格低，性价比高。 |
| 独享规格 | 独享：CPU、内存、存储和 I/O。 说明 独占型是独享型的顶配，独占整台服务器的 CPU、内存、存储和 I/O。 | 性能更好更稳定。 |
