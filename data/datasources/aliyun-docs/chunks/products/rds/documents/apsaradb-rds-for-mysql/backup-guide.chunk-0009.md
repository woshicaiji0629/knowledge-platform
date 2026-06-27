### 费用说明
如果[备份使用量](view-and-manage-the-size-of-backup-files-of-an-apsaradb-rds-for-mysql-instance.md)未超过免费额度，备份不收费。超出部分将额外按使用量计费，每小时备份费用 = ( 备份使用量 - 免费备份额度 ) × 备份单价。
通用型节省计划或资源包抵扣详情
[存储包](../product-overview/storage-plans.md)可以抵扣包年包月或按量付费的RDS实例超出免费额度的备份空间（不包括高性能云盘和SSD云盘）。
[通用型节省计划](../product-overview/savings-plan-introduction.md)可以抵扣包年包月、按量付费以及ServerlessRDS实例的备份空间费用。
备份单价
常规备份与归档备份空间的单价，请前往[RDS](https://www.aliyun.com/price/product?spm=5176.28228749.J_cBmqkGxzGK2_MpfhV9BAu.5.19c755262b67m4#/commodity/bards)[定价详情](https://www.aliyun.com/price/product?spm=5176.28228749.J_cBmqkGxzGK2_MpfhV9BAu.5.19c755262b67m4#/commodity/bards)页查看。在该页面依次单击走价详情>备份与恢复。
备份计费示例
假设用户在华东1（杭州）地域有一个RDS MySQL 8.0版本的云盘实例，其存储空间为20 GB，当前实例的数据备份量为40 GB，日志备份量为20 GB。备份单价：0.00025 元/GB/小时。备份计费方式如下：
免费备份额度为：20 GB x 200% = 40 GB
当前备份使用量为：40 GB + 20 GB = 60 GB，已超出免费备份额度，超出部分将额外按使用量计费，每小时备份费用（最近730天内的备份）为：( 60 GB - 40 GB ) x 0.00025 = 0.005元/GB
