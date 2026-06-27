# 使用离线全量Key分析大Key与内存占用-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/offline-key-analysis

# 离线全量Key分析
通过离线全量Key分析功能来分析云数据库 Tair（兼容 Redis）的备份文件，可以快速发现实例中的大Key，帮助您掌握Key在内存中的占用和分布、Key过期时间等信息，为您的优化操作提供数据支持，帮助您避免因Key倾斜引发的内存不足、性能下降等问题。
该功能由CloudDBA的[缓存分析](https://help.aliyun.com/zh/das/user-guide/cache-analysis#multiTask1165)提供。
## 适用范围
单副本实例不支持该功能。
[磁盘型](../product-overview/essd-based-instances-1.md)实例在小版本2.7.0之前不支持此功能，可[升级小版本](update-the-minor-version.md)至最新版本使用此功能。
如果实例规格已发生变更，则不支持分析实例变更前的备份文件。
离线全量Key分析功能只支持分析Redis开源版数据结构和以下Tair自研数据结构：TairString、TairHash、TairGIS、TairBloom、TairDoc、TairCpc、TairZset，若存在其他Tair自研数据结构会导致分析任务失败。
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击CloudDBA>离线全量Key分析。
离线全量Key分析页签默认展示最近一天缓存分析结果列表，您可以根据需求选择其他时间段。
在离线全量Key分析页签，单击页面右侧的立即分析。
在弹出的对话框中，设置分析的节点与方式。
| 参数 | 说明 |
| --- | --- |
| 选择分析节点 | 选择需要执行缓存分析的节点 ID。 说明 您可以选择分析整个实例，也可以只选中某个节点进行分析。 |
| 分析方式 | 您可以按照界面提示，选择不同的备份文件。 使用上一个备份文件 ：分析当前最新的备份文件。 选择历史备份文件 ：允许选择并分析任意历史备份文件。 新建备份, 并使用最新的备份进行分析 ：立即新建一次备份，待备份完成后对其进行分析，该方式可分析实例当前的状态。 说明 在分析已存在的备份文件时，请确认备份文件的时间点，是否符合预期。 |
| 分隔符 | 根据需要，输入用于识别 Key 前缀的分隔符。当分隔符为默认的 :;,_-+@=|# 时，不需要输入。 |
单击确定。
系统执行分析并展示分析状态，您可以单击刷新以更新分析状态。
找到已完成的分析任务，单击其操作列的详情展示详细的分析结果。
基本信息：展示实例基本属性和缓存分析方法等信息。
相关节点：展示实例内各节点的内存情况和Key统计信息。
说明
当实例为集群或读写分离架构，且选择的分析节点为整个实例时，详情页才会展示相关节点信息并提供节点选择的功能。
详情：展示实例或节点的Key内存占有情况、Key数量分布情况、Key中元素的内存占用和分布情况、Key过期时间分布、大Key排名等信息。
## 常见问题
Q：分析出大量已过期的Key怎么办？
A：当业务中数据设置了过期时间，且实例在同一时间（时间段）过期大量Key时，可能会出现该情况。此时，除了依靠实例自动清除过期数据外，您可以通过控制台上的清除数据功能快速清除过期Key，更多信息请参见[如何清除过期](../support/how-do-i-clear-expired-keys.md)[Key](../support/how-do-i-clear-expired-keys.md)。
Q：若使用RAM账号，操作时提示权限不足怎么办？
A：请对RAM账号进行授权并重试，更多信息请参见[常见自定义权限策略场景及示例](../custom-permission-policy-reference.md)。
Q：在同一个实例中，为什么执行离线分析任务的速度时快时慢？
A：离线分析任务是异步任务，分析速度还与CloudDBA的当前总任务数有关，当总任务数较多时，该离线分析任务需排队等待，分析任务的耗时就会变长。
Q：如何处理报错decode rdbfile error: rdb: unknown object type 116 for key？
A：该报错表示实例中存在非标准的Bloom结构，暂不支持分析。
Q：如何处理报错decode rdbfile error: rdb: invalid file format？
A：该报错表示所选的备份文件无效，请检查实例是否在该备份时间点后进行了变配；或者实例是否开启了透明数据加密TDE（该功能无法分析已加密的信息）。
Q：如何处理报错decode rdbfile error: rdb: unknown module type？
A：该报错表示备份文件中存在Tair自研数据结构，暂不支持分析。
Q：如何处理新建备份, 并使用最新的备份进行分析后报错XXX backup failed？
A：该实例当前存在正在执行的BGSAVE或BGREWRITEAOF命令，导致创建用于缓存分析任务的备份时出现了失败的情况。建议您选择业务低峰期新建备份，并使用最新的备份进行分析或者选择历史备份文件进行分析。
Q：为什么缓存分析结果展示的Key内存占有会比实际使用的内存小？
A：因为缓存分析结果实际只是解析了Key和对应value在RDB中序列化后占用的大小，这个只占用了used_memory中的一部分，used_memory还包含了如下部分：
Key和value所对应的struct和指针大小。在jemalloc分配后，字节对齐部分所占用的大小也没计算在used_memory中，例如在2.5亿Key的数量下，struct、指针、字节对齐这三部分的大小加起来约有2~3 GB。
客户端输出缓冲区、查询缓冲区、AOF重写缓冲区和主从复制的backlog，这些也没计算到缓存分析中。
Q：Redis缓存分析的前缀分隔符是什么？
A：目前Redis缓存分析的前缀分隔符是按照固定的前缀:;,_-+@=|#区分的字符串。
Q：为什么Redis缓存分析中String类型Key的元素数量和元素长度是一样的？
A：在Redis缓存分析中，针对String类型的Key，其元素数量就是其元素长度。
Q：为什么Stream数据结构的缓存分析结果是实际值的数倍？
A：Stream数据结构底层使用基数树（Radix Tree）和紧凑列表（listpack），数据结构复杂。缓存分析功能目前无法精确获得此类复杂数据结构的内存占用情况，只能进行估算，因此缓存分析结果存在偏差。
说明
缓存分析结果的偏差仅为数据统计偏差，不影响数据库实例的功能。
## 相关API
| API 接口 | 说明 |
| --- | --- |
| [CreateCacheAnalysisJob](https://help.aliyun.com/zh/das/api-createcacheanalysisjob#doc-api-DAS-CreateCacheAnalysisJob) | 创建缓存分析任务。 |
| [DescribeCacheAnalysisJob](https://help.aliyun.com/zh/das/api-describecacheanalysisjob#doc-api-DAS-DescribeCacheAnalysisJob) | 查询缓存分析任务详情。 |
| [DescribeCacheAnalysisJobs](https://help.aliyun.com/zh/das/api-describecacheanalysisjobs#doc-api-DAS-DescribeCacheAnalysisJobs) | 查询缓存分析任务列表。 |
## 相关文档
[Top Key](use-the-real-time-key-statistics-feature.md)[统计](use-the-real-time-key-statistics-feature.md)
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
