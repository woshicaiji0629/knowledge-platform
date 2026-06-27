# 实时查找Redis实例的大Key和热Key-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/use-the-real-time-key-statistics-feature

# Top Key统计
当Tair和Redis内存使用率升高或CPU使用率升高时，您可以使用Top Key统计功能快速找到大Key和热Key。本功能支持展示实例中实时和历史的大Key、热Key信息，包括元素数量多的Key、占用内存大的Key、访问频次高的热Key，帮助您有效解决实例性能问题。
## 大Key和热Key的统计排名机制
为避免对数据库造成额外的资源占用，本功能仅会统计客户端操作（读、写）过的Key，并仅保留和展示每种Key类型的Top数量，而不会实时扫描数据库中的所有Key。同时，在实例重启后或HA切换后，原先统计的TopKey信息将被清空，统计将重新开始，因此长时间未操作过的Key可能不会被纳入统计。如需了解数据库中所有Key的内存占用、数量分布等信息，请使用[离线全量](offline-key-analysis.md)[Key](offline-key-analysis.md)[分析](offline-key-analysis.md)功能。
| Key 类型 | 适用版本 | 统计机制 | 展示说明 |
| --- | --- | --- | --- |
| 大 Key（子元素数量） | Redis 开源版 5.0 及以上。 Tair（企业版） 。 | 元素数量（如 Hash 中的 field 数、Set 中的 member 数等）达到阈值（默认 2000）及以上时，被统计为大 Key。可通过 [设置参数](modify-the-values-of-parameters-for-an-instance.md) bigkey-threshold 自定义阈值。 说明 持久内存型实例不支持 bigkey-threshold 参数。 若参数设置未显示此参数，请 [升级小版本](update-the-minor-version.md) 后重试。 | 最多展示每个数据类型排名前 3 的大 Key，当 Key 的元素数量相同时优先展示先写入的 Key。 说明 Tair（企业版） 持久内存型实例仅展示所有 Key 中元素数量前 3 的 Key。 其他实例若总共仅展示 3 个大 Key，请 [升级小版本](update-the-minor-version.md) 后重试。 |
| 大 Key（内存占用） | Tair（企业版） 内存型云原生版且小版本 25.6.0.0 及以上。 | Key 的总内存占用大于阈值（默认 500 MB）时，被统计为大 Key。可通过 [设置参数](modify-the-values-of-parameters-for-an-instance.md) bigkey-mem-threshold 自定义阈值。 Key 的平均子元素内存占用大于 1 MB 时，被统计为大 Key。可通过 [设置参数](modify-the-values-of-parameters-for-an-instance.md) bigkey-field-mem-threshold 自定义阈值。例如：String 类型单个字符串内存占用大于 1 MB；100 个 kv 对的 Hash 类型平均内存占用大于 100 MB。 bigkey-field-mem-threshold 自 2026 年 5 月 26 日起，默认值由 50 MB 调整为 1 MB。 | 最多展示每个数据类型排名前 3 的大 Key，当 Key 的元素数量相同时优先展示先写入的 Key。 |
| 热 Key（QPS） | Redis 开源版 5.0 及以上。 Tair（企业版） 。 | Key 的 QPS 超过 5000 时，被记录为热 Key。可通过 [设置参数](modify-the-values-of-parameters-for-an-instance.md) hotkey-threshold 自定义阈值。 | 在同一时间内，系统最多展示前 50 个热 Key，支持实时展示其精确 QPS。 低版本热 Key 统计支持有限，建议您 [升级至最新小版本](update-the-minor-version.md) 。 因为在 Redis 开源版 7.0.18、6.0.2.9、5.5.2.9 或 Tair 内存型 5.0.50、25.2.0.0 版本之前：热 Key 的 QPS 统计阈值为 3000 且不支持调整，同时仅能展示其大致的 QPS 范围，且 Redis 开源版 仅支持统计 20 个热 Key。 |
| 热 Key（流量） | Tair（企业版） 内存型云原生版且小版本 25.2.0.0 及以上。 | Key 的访问流量超过 1MB/s 时，被记录为热 Key。 默认不开启，可通过 [设置参数](modify-the-values-of-parameters-for-an-instance.md) #no_loose_high-cost-key-enabled 为 yes 开启此项统计。 可通过 [设置参数](modify-the-values-of-parameters-for-an-instance.md) #no_loose_high-cost-key-traffic-bytes-threshold 调整统计阈值（单位 B/s）。 可通过 #no_loose_high-cost-key-parse-hashtag 、 #no_loose_high-cost-key-parse-hashtag 参数 [开启](parameter-support.md) [Hashtag](parameter-support.md) [与前缀统计](parameter-support.md) 。即统计出单个 Key 热度低、但相同 Hashtag 或相同前缀的 Key 聚合后热度超阈值的情况，本功能需升级至 25.9.1.0 及以上版本。 | 在同一时间内，系统最多展示前 50 个热 Key，支持实时展示其精确出、入流量和访问频次。 说明 支持统计不存在的 Key。当数据类型显示 not-exist-key ，代表此 Key 不存在但存在高频访问。 |
本功能支持统计的数据结构如下：
Redis原生数据结构：String、List、Hash、Set、Zset、Stream
Tair自研数据结构：TairString、TairHash、TairGIS、TairBloom、TairDoc、TairCpc、TairZset、TairRoaring、TairTS、TairSearch
说明
Tair（企业版）持久内存型仅支持统计TairHash 和 TairString。
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击CloudDBA>Top Key统计。
根据业务需求，选择查询实时数据或历史数据。
Top Key统计页面包含大Key实时统计、大Key历史统计、热Key实时统计、热Key历史统计四个区域。您可以设置大Key和热Key的判定阈值，通过单击刷新手动获取最新数据，或开启自动刷新自动更新统计结果。
说明
如果实例为集群架构或读写分离架构，您还可以在当前节点下拉框中选择要展示数据的节点。
查询历史数据时，支持查询最近4天的大Key和热Key信息，且最大查询时间范围不能超过3小时。
## 相关API
| [DAS](https://help.aliyun.com/zh/das/product-overview/what-is-das#concept-2419191) 产品的 API 接口 | 说明 |
| --- | --- |
| [DescribeHotBigKeys](https://help.aliyun.com/zh/das/api-describehotbigkeys#doc-api-DAS-DescribeHotBigKeys) | 获取当前内存中实时的热 Key 和大 Key 信息。 |
| [DescribeTopHotKeys](https://help.aliyun.com/zh/das/api-describetophotkeys#doc-api-DAS-DescribeTopHotKeys) | 获取一段时间内排名前 20 的热 Key 信息。 |
| [DescribeTopBigKeys](https://help.aliyun.com/zh/das/api-describetopbigkeys#doc-api-DAS-DescribeTopBigKeys) | 获取一段时间内排名前 20 的大 Key 信息。 |
| [DescribeHotKeys](https://help.aliyun.com/zh/das/api-describehotkeys#doc-api-DAS-DescribeHotKeys) | 获取 Redis 实例的热 Key 信息。 |
## 常见问题
Q：为什么大Key（子元素数量）中会显示String类型Key？
A：在Redis开源版和部分早期Tair版本中会显示String类型长度大于阈值（默认为2000）的Key。
Q：为什么元素很少（如10个以内）的Key也显示为大Key？
A：有以下两种可能原因。
Key的name占用大，可使用memory usage key_name命令查看。
实例小版本过低，小版本低于5.2.7的实例bigkey-threshold（大Key统计阈值）默认值为0，导致内存占用小的Key也展示了出来，建议[升级小版本](update-the-minor-version.md)到最新。
## 相关文档
若业务中存在超过10万个元素的排行榜（采用Zset数据结构），建议考虑使用Tair自研的数据结构[exZset](../developer-reference/tairzset-command.md)。
结合TairJedis客户端，您可以轻松实现[分布式架构排行榜](../use-cases/implementation-of-distributed-architecture-ranking-list-based-on-tairzset.md)。即您只需关注和操作一个Key，而Tair会自动将数据以及计算任务分布至多个子Key中，从而有效避免产生超大Key和热Key的问题。
排查Redis CPU使用率高的原因，请参见[排查实例](troubleshoot-high-cpu-utilization-on-an-apsaradb-for-redis-instance.md)[CPU](troubleshoot-high-cpu-utilization-on-an-apsaradb-for-redis-instance.md)[使用率高的问题](troubleshoot-high-cpu-utilization-on-an-apsaradb-for-redis-instance.md)。
排查Redis内存使用率高的原因，请参见[排查实例内存使用率高的问题](troubleshoot-the-high-memory-usage-of-an-apsaradb-for-redis-instance.md)。
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
