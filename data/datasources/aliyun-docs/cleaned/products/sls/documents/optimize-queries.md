# 提高查询分析日志速度的方法-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/optimize-queries

# 提高查询分析日志速度的方法
您可以使用以下方式，提高日志查询分析的速度。
## 增加Shard数量或开启SQL独享版
增加Shard可以提升读写能力，但只对新写入的数据生效。Shard表示计算资源，Shard越多，计算越快，您需要保证平均每个Shard扫描的数据不多于5000万条。您可以通过分裂Shard，增加Shard数量。具体操作，请参见[分裂](manage-shards.md)[Shard](manage-shards.md)。Shard的计费信息，请参见[活跃](why-am-i-charged-for-active-shards.md)[Shard](why-am-i-charged-for-active-shards.md)[租用费用](why-am-i-charged-for-active-shards.md)。
[SQL](dedicated-sql.md)[独享版](dedicated-sql.md)支持更多的分析操作并发数、更多的扫描数据量。
## 缩减查询的时间范围和数据量
时间范围越大，查询越慢。
适当缩短查询的时间范围可以更快地完成计算。
数据量越大，查询越慢。
请尽量减少查询的数据量。
## 多次重复查询
当查询不精确时，可以尝试多次重复查询。每次查询时，底层加速机制会充分利用已有的结果进行分析，因此多次查询可以使结果更加精确。
## 优化SQL分析语句
计算时间较长的查询分析语句具备如下特点。
使用GROUP BY语法基于字符串列进行分组统计。
使用GROUP BY语法基于多列（大于5列）进行分组统计。
在SQL分析语句中有生成字符串的操作。
您可以通过如下方法优化分析语句。
尽量避免生成字符串的操作。
例如使用date_format函数生成格式化的时间戳，导致查询效率低。针对时间戳的计算，建议使用date_trunc或者time_series函数进行计算。示例如下：
* | select date_format(from_unixtime(__time__) , '%H_%i') as t, count(1) group by t
尽量避免对字符串列进行分组统计。
使用GROUP BY语法基于字符串列进行分组统计，会导致大量的Hash计算，这部分计算量占据整体计算量的50%以上。示例如下：
查询和分析语句（速度快）
* | select count(1) as pv , from_unixtime(__time__-__time__%3600) as time group by __time__-__time__%3600
查询和分析语句（速度慢）
* | select count(1) as pv , date_trunc('hour',__time__) as time group by time
上述两条查询分析语句都是计算每小时的日志条数。第二条语句先把时间戳转化成字符串格式（例如2021-12-12 00:00:00），然后对这个字符串列进行分组统计。第一条语句对时间整点值进行计算，并且通过分组统计后再将时间戳转化为字符串格式。
基于多列进行分组统计时，把字典大的字段放在前面。
例如字段的值有13个，uid字段的值有1亿个，则建议在GROUP BY子句中将uid字段放在前面。示例如下：
查询和分析语句（速度快）
* | select province,uid,count(1) group by uid,province
查询和分析语句（速度慢）
* | select province,uid,count(1) group by province,uid
使用估算函数。
估算函数的性能比精算函数的好。估算会损失一定的精确度，用于达到快速计算的效果。示例如下：
查询和分析语句（速度快）
* |select approx_distinct(ip)
查询和分析语句（速度慢）
* | select count(distinct(ip))
低基数场景，使用多个distinct聚合函数。
多个distinct需要拷贝复制多次原始数据网络开销大，可以开启session开关enable_opt_distinct_aggs。示例如下：
查询和分析语句（速度快）
* | select count(1), count(distinct projectId), count(distinct logstore) from log
查询和分析语句（速度慢）
* | set session enable_opt_distinct_aggs=true; select count(1), count(distinct projectId), count(distinct logstore) from log
在SQL分析语句中指定获取需要的列，尽量不要读取所有列。
在SQL分析语句中，尽量只读取需要参与计算的列。如果要获取所有列，请使用查询语法。示例如下：
查询和分析语句（速度快）
* |select a,b c
查询和分析语句（速度慢）
* |select *
不是用于分组的列，尽量放在聚合函数中。
例如userid与用户名必定是一一对应的，您只需使用GROUP BY语法对userid进行分组统计即可。示例如下：
查询和分析语句（速度快）
* | select userid, arbitrary(username), count(1) group by userid
查询和分析语句（速度慢）
* | select userid, username, count(1) group by userid,username
尽量避免使用IN语法
尽量避免在分析语句中使用IN语法，您可以在查询语句中使用OR语法代替。示例如下：
查询和分析语句（速度快）
key: a or key: b or key: c | select count(1)
查询和分析语句（速度慢）
* | select count(1) where key in ('a','b')
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
