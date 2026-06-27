# 如何多集合操作与无数据告警-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/set-query-statistics-statement

# 设置查询统计语句
日志服务支持联合监控与无数据告警，本文将指导如何配置。
## 监控时效性说明
告警监控原理
基于告警的查询时间范围，根据检查频率定时执行配置的查询语句，并将查询结果作为告警条件的参数进行计算，如果计算结果为true，则触发告警。
监控时效性问题分析
数据索引延迟：数据从写入日志服务到被查询之间存在延时，即便延时很低，也存在数据漏查的风险。
例如：告警执行时间为12:03:30，查询范围为相对一分钟时，检查频率为固定间隔1分钟。则查询时间范围为[12:02:30,12:03:30)，对于12:03:29秒写入的日志，无法保证在12:03:30这个时间点查询到。
查询准确性：写入包含同一分钟不同时间的日志时，由于日志服务的索引构建方式，可能会存在较晚的日志的索引写入较早的日志时间点。
例如：告警执行时间为12:03:30，查询范围为相对一分钟则为[12:02:30,12:03:30)，如果在12:02:50秒写入多条日志，这些日志的时间有12:02:20，12:02:50等，那么这一批日志的索引可能会落入12:02:20这个时间点，导致使用时间范围[12:02:30,12:03:30)查询不到日志。
时效性优化建议
追求准确性：如果您对告警的准确性要求高（不重复报警，不漏报）。
数据索引延迟问题：建议在查询统计时，查询区间的相对起始时间和相对结束时间设置早一点，如70秒前~10s前（相对），通过设置10秒的缓冲时间来避免因为索引速度过低导致漏查。
查询不准确的问题：建议在查询统计时，查询区间选择整点时间，如整点1分钟、整点5分钟和整点1小时等，并且将检查频率设置成一样的时间，如1分钟、5分钟和1小时等。
追求实时性：如果对告警的实时性要求高（第一时间收到告警，能够容忍重复报警）。
数据索引延迟问题：建议在查询统计时，查询区间的相对起始时间往前推移，如70秒（相对）。
查询不准确的问题：建议在查询统计时，查询区间至少需要包含前一分钟，如90秒（相对），同时设置检查频率为1分钟。
## 简介
## 关联多个查询分析结果
日志服务告警监控系统将一个查询和分析结果当作一个集合，并支持多个集合关联监控。
配置界面中，每个查询统计以编号（0、1、2）标识，包含查询语句输入框和时间范围设置。相邻查询统计之间通过集合操作下拉框关联，可通过排序按钮调整顺序或删除。底部设有分组评估选项。
重要
日志服务最多支持3个集合关联监控。
默认只选取查询和统计结果中的前1000条数据用于集合操作。当存在三个查询和分析操作且集合操作不存在不合并选项时，只选取查询和统计结果中的前100条数据。
当存在三个集合时，先对前两个集合进行操作，该操作结果再与第三个集合进行集合操作。例如：
集合A左联集合B左联集合C：集合A和集合B先完成左联操作，该结果再左联集合C。
集合A拼接集合B内联集合C：集合A和集合B完成拼接操作，该结果再内联集合C。
集合A左斥集合B不合并集合C：集合A和集合B完成左斥操作，忽略集合C。
集合操作支持9种配置，具体如下所示：
| 集合操作 | 图示 | 说明 |
| --- | --- | --- |
| [不合并](set-query-statistics-statement.md) |  | 两个集合之间无关联。 集合 A 为查询和分析结果，集合 B 仅在告警信息中作为内容模板的变量被引用。 |
| [笛卡尔积](set-query-statistics-statement.md) | 无 | 集合 A 与集合 B 任意数据互相交叉组合，一般用于过滤评估。 |
| [拼接](set-query-statistics-statement.md) |  | 集合 B 中的数据添加到集合 A 中，根据字段对齐。 |
| [内联](set-query-statistics-statement.md) |  | 集合 A 中仅保留在集合 B 中存在的数据，即集合 B 是集合 A 的白名单。 |
| [左联](set-query-statistics-statement.md) |  | 在集合 A 中补充部分来自集合 B 的信息，即集合 B 是 A 的维表。 |
| [右联](set-query-statistics-statement.md) |  | 在集合 B 中补充部分来自集合 A 的信息，即集合 A 是集合 B 的维表。 |
| [全联](set-query-statistics-statement.md) |  | 集合 A 和集合 B 互相补充信息。 |
| [左斥](set-query-statistics-statement.md) |  | 在集合 A 中删除集合 B 中存在的数据，即集合 B 是集合 A 的黑名单。 |
| [右斥](set-query-statistics-statement.md) |  | 在集合 B 中删除集合 A 中存在的数据，即集合 A 是集合 B 的黑名单。 |
### 不合并
需求
监控Nginx访问日志，每15分钟的5xx错误超过500次则触发告警，并且在告警内容中列出具体的出错的主机信息。
配置如下：查询统计0的查询语句为status > 500 | select count(1) as cnt，集合操作选择不合并；查询统计1的查询语句为status > 500 | select host, count(1) as pv group by host order by pv desc limit 5，分组评估选择不分组，触发条件选择有数据匹配，条件为cnt > 500。
结果
查询统计0的结果
统计15分钟内发生5xx错误的次数。
| cnt |
| --- |
| 1234 |
查询统计1的结果
统计15分钟内发生5xx错误最多的Top5主机及对应的错误次数。
| host | pv |
| --- | --- |
| host1 | 60 |
| host2 | 55 |
| host3 | 47 |
| host4 | 45 |
| host5 | 30 |
集合操作结果
当选择集合操作为不合并时，集合操作结果为查询统计0的结果。
### 笛卡尔积
示例1
需求：
同时监控OSS访问日志和SLB访问日志，每15分钟统计一次OSS的4xx错误和SLB的5xx错误，当总次数达到1000次时触发告警。
配置：查询统计0的查询语句为status >= 400 and status < 500 | select count(1) as pv，集合操作选择笛卡尔积；查询统计1的查询语句为status >= 500 | select count(1) as pv，分组评估选择不分组，触发条件选择有数据匹配，条件为($0.pv + $1.pv) > 1000。
结果：
查询统计0的结果
统计15分钟内出现OSS 4xx错误的次数。
| pv |
| --- |
| 890 |
查询统计1的结果
统计15分钟内出现SLB 5xx错误的次数。
| pv |
| --- |
| 567 |
集合操作结果
当选择集合操作为笛卡尔积时，集合操作结果如下：
| $0.pv | $1.pv |
| --- | --- |
| 890 | 567 |
其他示例
查询统计0结果
| a | b |
| --- | --- |
| a1 | b1 |
| a2 | b2 |
| a5 | b5 |
查询统计1结果
| a | c |
| --- | --- |
| a1 | c1 |
| a3 | c3 |
集合操作结果
当选择集合操作为笛卡尔积时，集合操作结果如下：
| $0.a | b | $1.a | c |
| --- | --- | --- | --- |
| a1 | b1 | a1 | c1 |
| a1 | b1 | a3 | c3 |
| a2 | b2 | a1 | c1 |
| a2 | b2 | a3 | c3 |
| a5 | b5 | a1 | c1 |
| a5 | b5 | a3 | c3 |
### 拼接
示例1
需求
北京和上海地域分别有2个用于存储Nginx访问日志的LogStore，每15分钟统计一次5xx错误超过30次的主机数。当两个LogStore中符合条件的主机数超过10个时，触发告警。
配置如下：查询统计0的查询语句为status > 500 | select host, count(*) as pv group by host having pv > 30，集合操作选择拼接；查询统计1的查询语句为status > 500 | select host, count(*) as pv group by host having pv > 30，分组评估选择不分组，触发条件选择有特定条数据大于10条。
结果
查询统计0的结果
统计15分钟内发生5xx错误超过30次的主机及对应的错误次数。
| host | pv |
| --- | --- |
| host1 | 60 |
| host2 | 55 |
| host3 | 47 |
| host4 | 45 |
| host5 | 31 |
查询统计1的结果
统计15分钟内发生5xx错误超过30次的主机及对应的错误次数。
| host | pv |
| --- | --- |
| hosta | 70 |
| hostb | 45 |
| hostc | 44 |
| hostd | 42 |
集合操作结果
当选择集合操作为拼接时，集合操作结果如下：
| host | pv |
| --- | --- |
| host1 | 60 |
| host2 | 55 |
| host3 | 47 |
| host4 | 45 |
| hosg5 | 31 |
| hosta | 70 |
| hostb | 45 |
| hostc | 44 |
| hostd | 42 |
其他示例
当2个查询统计结果中的字段不完全一致时，进行拼接后，无匹配的字段留空。
查询统计0结果
| a | b |
| --- | --- |
| a1 | b1 |
| a2 | b2 |
查询统计1结果
| b | c |
| --- | --- |
| b1 | c1 |
| b2 | c2 |
集合操作结果
| a | b | c |
| --- | --- | --- |
| a1 | b1 | 无 |
| a2 | b2 | 无 |
| 无 | b1 | c1 |
| 无 | b2 | c2 |
当存在3个查询统计时，查询统计0和查询统计1的结果先完成集合操作，再与查询统计2结果拼接。
查询统计0结果
| a | b |
| --- | --- |
| a1 | b1 |
| a2 | b2 |
查询统计1结果
| a | b |
| --- | --- |
| a1 | b11 |
| a2 | b22 |
| a3 | b33 |
查询统计0结果与查询统计1结果的拼接结果
当选择集合操作为内联，$0.a == $1.a时，集合操作结果如下：
| a | $0.b | $1.b |
| --- | --- | --- |
| a1 | b1 | b11 |
| a2 | b2 | b22 |
查询统计2结果
| a | b |
| --- | --- |
| a3 | b333 |
| a4 | b444 |
集合操作结果
当选择集合操作为拼接时，集合操作结果如下：
说明
查询统计2结果中字段b与字段$0.b对齐。
| a | $0.b | $1.b |
| --- | --- | --- |
| a1 | b1 | b11 |
| a2 | b2 | b22 |
| a3 | b333 | 无 |
| a4 | b444 | 无 |
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
示例2
需求
北京和上海地域分别有2个用于存储Nginx访问日志的LogStore，每15分钟统计一次发生5xx错误超过30次的客户端。北京和上海同时发生5xx错误，且北京的错误次数大于上海时触发告警。
配置如下：查询统计0的查询语句为status >= 500 | select client_ip, count(1) as pv group by client_ip having pv > 30，集合操作选择内联，关联条件为$0.client_ip = $1.client_ip且$0.pv > $1.pv；查询统计1的查询语句为status >= 500 | select client_ip, count(1) as pv group by client_ip having pv > 30，分组评估选择不分组，触发条件选择有数据。
结果
查询统计0结果
统计15分钟内北京地域发生5xx错误超过30次的客户端及对应的错误数。
| client_ip | pv |
| --- | --- |
| 192.0.2.4 | 60 |
| 192.0.2.5 | 55 |
| 192.0.2.6 | 47 |
| 192.0.2.7 | 45 |
| 192.0.2.8 | 31 |
查询统计1结果
统计15分钟内上海地域发生5xx错误超过30次的客户端及对应的错误数。
| client_ip | pv |
| --- | --- |
| 192.0.2.5 | 70 |
| 192.0.2.6 | 45 |
| 192.0.2.7 | 44 |
| 192.0.2.8 | 42 |
| 192.0.2.9 | 42 |
集合操作结果
当选择集合操作为内联，$0.client_ip == $1.client_ip，$0.pv > $1.pv时，集合操作结果如下：
| client_ip | pv |
| --- | --- |
| 192.0.2.6 | 47 |
| 192.0.2.7 | 45 |
其他示例
当2个查询统计结果中的非关联字段存在同名时，集合操作的结果集合自动为字段添加$0、$1前缀。
查询统计0结果
| a | b | c | d |
| --- | --- | --- | --- |
| a1 | b1 | c1 | d1 |
| a2 | b2 | c2 | d2 |
| a3 | b3 | c3 | d3 |
查询统计1结果
| a | b | c |
| --- | --- | --- |
| a1 | b11 | c11 |
| a2 | b22 | c22 |
集合操作结果
当选择集合操作为内联，$0.a == $1.a时，集合操作结果如下：
| a | $0.b | $0.c | d | $1.b | $1.c |
| --- | --- | --- | --- | --- | --- |
| a1 | b1 | c1 | d1 | b11 | c11 |
| a2 | b2 | c2 | d2 | b22 | c22 |
### 左联
查询统计0结果
| a | b |
| --- | --- |
| a1 | b1 |
| a2 | b2 |
| a3 | b3 |
查询统计1结果
| a | b | c |
| --- | --- | --- |
| a1 | b11 | c1 |
| a2 | b22 | c2 |
集合操作结果
当选择集合操作为左联，$0.a == $1.a时，集合操作结果如下：
| a | $0.b | $1.b | c |
| --- | --- | --- | --- |
| a1 | b1 | b11 | c1 |
| a2 | b2 | b22 | c2 |
| a3 | b3 | 无 | 无 |
### 右联
查询统计0结果
| a | b | c |
| --- | --- | --- |
| a1 | b11 | c1 |
| a2 | b22 | c2 |
查询统计1结果
| a | b |
| --- | --- |
| a1 | b1 |
| a2 | b2 |
| a3 | b3 |
集合操作结果
当选择集合操作为右联，$0.a == $1.a时，集合操作结果如下：
| a | $0.b | c | $1.b |
| --- | --- | --- | --- |
| a1 | b11 | c1 | b1 |
| a2 | b22 | c2 | b2 |
| a3 | 无 | 无 | b3 |
### 全联
查询统计0
| a | b | c |
| --- | --- | --- |
| a1 | b1 | c1 |
| a2 | b2 | c2 |
| a5 | b5 | c3 |
查询统计1结果
| a | b | d |
| --- | --- | --- |
| a1 | b11 | d1 |
| a2 | b22 | d2 |
| a3 | b33 | d3 |
集合操作结果
当选择集合操作为全联，$0.a == $1.a时，集合操作结果如下：
| a | $0.b | c | $1.b | d |
| --- | --- | --- | --- | --- |
| a1 | b1 | c1 | b11 | d1 |
| a2 | b2 | c2 | b22 | d2 |
| a5 | b5 | c3 | 无 | 无 |
| a3 | 无 | 无 | b33 | d3 |
### 左斥
需求
监控除指定Bucket外的其他Bucket发生5xx错误的次数，当每15分钟内出现1000次5xx错误时触发告警。此需求中，需添加资源数据，用于维护Bucket黑名单。
配置如下：查询统计0的查询语句为status >=500 | select bucket, count(*) as pv group by bucket having pv > 1000 limit 1000，集合操作选择左斥，关联条件为$0.bucket = $1.bucket；查询统计1选择OSS数据源（user.test），指定bucket_03、bucket_04，分组评估选择不分组，触发条件选择有数据。
结果
查询统计0的结果
统计15分钟内出现5xx错误超过1000次的Bucket。
| bucket | pv |
| --- | --- |
| bucket_01 | 60 |
| bucket_02 | 55 |
| bucket_03 | 47 |
| bucket_04 | 45 |
查询统计1的结果
Bucket的资源数据。
| bucket | desc |
| --- | --- |
| bucket_03 | for dev team |
| bucket_04 | for test team |
集合操作结果
当选择集合操作为左斥，$0.bucket == $1.bucket时，集合操作结果如下：
| bucket | pv |
| --- | --- |
| bucket_01 | 60 |
| bucket_02 | 55 |
### 右斥
需求
监控除指定Bucket外的其他Bucket发生5xx错误的次数，当每15分钟内出现1000次5xx错误时触发告警。此需求中，需添加资源数据，用于维护Bucket黑名单。
配置如下：查询统计0选择OSS数据源（user.test），指定bucket_03、bucket_04，集合操作选择右斥，关联条件为$0.bucket = $1.bucket；查询统计1的查询语句为status > 500 | select bucket, count(*) as pv group by bucket having pv > 1000 limit 1000，分组评估选择不分组，触发条件选择有数据。
结果
查询统计0的结果
Bucket的资源数据。
| bucket | desc |
| --- | --- |
| bucket_03 | for dev team |
| bucket_04 | for test team |
查询统计1的结果
统计15分钟内出现5xx错误超过1000次的Bucket。
| bucket | pv |
| --- | --- |
| bucket_01 | 60 |
| bucket_02 | 55 |
| bucket_03 | 47 |
| bucket_04 | 45 |
集合操作结果
当选择集合操作为右斥，$0.bucket == $1.bucket时，集合操作结果如下：
| bucket | pv |
| --- | --- |
| bucket_01 | 60 |
| bucket_02 | 55 |
## 无数据告警
您可以使用无数据告警功能，避免采集过程中数据丢失无感知问题。例如您创建了一个告警监控规则用于监控各个主机的CPU指标，并希望发生如下情况时，收到告警通知。
CPU使用率超过95%。
查询和分析结果中无数据。
具体配置如下所示：
查询统计：例如统计CPU的使用率。
* | select promql_query_range('cpu_util') from metrics limit 1000
触发条件：有数据匹配，value>95，严重度：中
当查询和分析结果中存在value的值大于95时，触发中级别的告警。
连续触发阈值：当累计触发的告警次数达到该值时，产生一条告警。
无数据告警：打开无数据告警开关，并设置严重度和标注信息。
开启无数据告警功能后，如果查询和分析结果中无数据的次数超过连续触发阈值，将触发告警。
无数据告警具备独立的告警严重度和标注信息。
页面配置展示如下：
分组评估选择标签自动。添加标注中，标题设为${alert_name}告警触发，描述设为${alert_name}告警触发。自动添加标注和恢复通知均关闭。在高级配置中，连续触发阈值设为1；开启无数据告警，严重度设为中，标注标题为${alert_name}:无数据，描述为该告警规则评估时无数据。
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
