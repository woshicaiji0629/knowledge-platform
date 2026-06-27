### 内联
示例1
需求
监控指定Bucket中发生5xx错误的次数，当每15分钟内出现1000次5xx错误时触发告警。此需求中，需添加资源数据，用于维护Bucket白名单。
配置如下：查询统计0的查询语句为status >=500 | select bucket, count(*) as pv group by bucket having pv > 1000 limit 1000，集合操作选择内联，关联条件为$0.bucket = $1.bucket；查询统计1选择OSS数据源（user.test），指定bucket_03、bucket_04、bucket_05、bucket_06，分组评估选择不分组，触发条件选择有数据。
结果
查询统计0的结果
统计15分钟内发生5xx错误次数超过1000次的Bucket。

| bucket | pv |
| --- | --- |
| bucket_01 | 1600 |
| bucket_02 | 1550 |
| bucket_03 | 1470 |
| bucket_04 | 1450 |

查询统计1的结果
Bucket的资源数据。

| bucket | desc |
| --- | --- |
| bucket_03 | for dev team |
| bucket_04 | for test team |
| bucket_05 | for service team |
| bucket_06 | for support team |

集合操作结果
当选择集合操作为内联，$0.bucket == $1.bucket时，集合操作结果如下：

| bucket | pv | desc |
| --- | --- | --- |
| bucket_03 | 1470 | for dev team |
| bucket_04 | 1450 | for test team |
