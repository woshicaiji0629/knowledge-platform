# 突破内存限制的混合数据存储-混合存储型-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/hybrid-storage-instances

# 混合存储型（已停售）
与Redis开源版不同，Tair混合存储型整合了内存和磁盘二者的优势，在提供高速数据读写能力的同时满足了数据持久化的需求。
说明
混合存储型已停止售卖，更多信息，请参见[【通知】Redis](end-of-sale-for-apsaradb-for-redis-hybrid-storage-instances.md)[混合存储型实例停止售卖](end-of-sale-for-apsaradb-for-redis-hybrid-storage-instances.md)。推荐选择[持久内存型](persistent-memory-optimized-instances-1.md)实例。
## 简介
图 1.混合存储型架构图
Tair（企业版）混合存储型（简称混合存储型）是阿里云自主研发的兼容Redis协议的混合存储产品，使用磁盘存储全量数据，将热数据保存到内存中供应用快速读写。在保证常用数据访问性能不下降的基础上，混合存储型能够大幅度降低用户成本，实现性能与成本的平衡，同时使单个Redis实例的数据量不再受内存大小的限制。
内存数据：内存中存放了热数据的Key和Value，同时为快速确认要操作的Key是否存在，内存中也会缓存所有的Key信息。
磁盘数据：磁盘中存放所有的Key和Value，Redis的数据结构（例如Hash）也会以一定的格式进行存储在磁盘。
## 适用场景
| 适用场景 | 说明 |
| --- | --- |
| 视频直播 | 视频直播类业务往往存在大量热点数据，大部分的请求都来自于热门的直播间。使用混合存储型，内存中保留热门直播间的数据，不活跃的直播间数据被自动存储到磁盘上，可以达到对有限内存的最佳利用效果。 |
| 电子商务 | 电商类应用往往有大量的商品数据。使用混合存储型可以轻松突破内存容量限制，将大量的商品数据都存储到混合存储型中。在正常业务请求中，活跃的商品数据会保留在内存，不活跃的商品数据会逐渐交换到磁盘上，从而解决内存不够的问题。 |
| 在线教育 | 在线教育类的场景有大量的课程、题库以及师生交流信息等数据，通常只有热门课程和最新题库会被频繁访问。使用混合存储型，将所有课程信息存储到磁盘，访问量大的课程和题库数据存储到内存并常驻内存，保证高频访问数据的读写性能，实现高性能与高性价比的有机结合。 |
典型业务场景的示例如下：
场景1：使用开源Redis集群存储了100GB的数据，但高峰期QPS不到2万，其中80%的数据的访问频率很低。
使用32GB内存加128GB磁盘的混合存储型实例后，节省了近70GB的内存空间，存储成本下降50%以上。
场景2：在IDC自建Pika实例来解决Redis存储成本高的问题。总数据量约400GB，其中访问频率高的数据仅占10%左右，并且集群的运维成本居高不下。
使用64GB内存加512GB磁盘的混合存储型实例后，既免除了繁重的运维工作，又保障了服务质量。
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
