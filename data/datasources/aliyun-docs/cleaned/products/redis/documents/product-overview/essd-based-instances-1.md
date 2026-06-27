# 磁盘型实例功能特性与技术架构-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/essd-based-instances-1

# 磁盘型
Tair推出磁盘（ESSD/SSD）型实例，均兼容Redis核心数据结构与接口，可提供大容量、低成本、持久化的数据库服务。适用于兼容Redis、需要大容量且访问性能较高的温冷数据存储场景。
## 背景信息
Redis基于内存属于易失性存储介质，随着业务持续快速的发展，数据量飞速的增长，您可能会遇到如下挑战：
沉淀的数据越来越多但访问量低，数据存储在内存中性价比低，需要低成本存储来满足业务更多数据迭代的需求。
需要搭配其他数据库或存储解决持久化问题。
最大存储容量受限于单机瓶颈及集群规模。
阿里云基于[ESSD](../../../ecs/documents/user-guide/essds.md)[云盘](../../../ecs/documents/user-guide/essds.md)与[SSD](../../../ecs/documents/user-guide/local-disks.md)[本地盘](../../../ecs/documents/user-guide/local-disks.md)存储介质，推出了ESSD型、SSD型产品，成本最低可达到全内存版本的15%，拥有超高性价比；容量可达到百TB级别，在降低成本的同时提升了数据可靠性。
## 功能概述
### 线程模型
Tair磁盘型将服务各阶段的任务进行分离，通过多个线程并行处理各阶段任务，从而提高性能。
主线程：负责建立连接、启动其他线程、分发任务等。
IO线程：负责读取请求、发送响应等。IO线程读取请求并进行解析，之后将解析结果以命令的形式放在队列中发送给Worker线程。
Worker线程：负责解析命令、处理命令等。Worker线程将命令处理完成后生成响应，通过另一条队列发送给IO线程。
辅助（BIO）线程：负责高可用探测、数据持久化、内存惰性回收、保活等。
说明
IO线程的数量会随着规格的提升而增加。IO线程与Worker线程之间通过无锁队列和管道进行数据交换，以提高线程的并行度。
### 特性
高兼容性：兼容Redis 6.0大部分的数据结构和命令，具体限制请参见[Tair（企业版）命令支持与限制](../developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。
低成本：最低为Redis开源版的15%。
性能：约为Redis开源版的60%，更多信息请参见[磁盘（ESSD）型性能白皮书](../support/performance-white-paper-of-essd-based-instances.md)、[磁盘（SSD）型性能白皮书](../support/disk-ssd-performance-white-paper.md)。
同步模式：额外支持[半同步模式](../user-guide/modify-the-synchronization-mode-of-a-persistent-memory-optimized-instance.md)。
磁盘存储：数据分布在ESSD或SSD中，容量可达百TB级别，拥有高数据可靠性。
数据分布：采用阿里云TairDB存储引擎，数据通过磁盘持久化，内存用于请求加速。
使用场景：温数据和冷数据。
## ESSD型与SSD型
ESSD型支持自定义存储容量，支持云盘快照式备份，数据备份与迁移复制速度更快，但仅支持标准架构。
SSD型支持标准架构与集群架构，在同规格情况下性价比更高。
| 对比性 | ESSD 型 | SSD 型 |
| --- | --- | --- |
| 存储介质 | [ESSD](../../../ecs/documents/user-guide/essds.md) [云盘](../../../ecs/documents/user-guide/essds.md) ，支持 PL1-PL3，PL3 的性能优于 PL2 与 PL1。 | [SSD](../../../ecs/documents/user-guide/local-disks.md) [本地盘](../../../ecs/documents/user-guide/local-disks.md) 。 |
| 实例架构 | 标准架构。 | 标准架构、集群架构。 |
| 存储容量 | 支持以 10 GB 为粒度进行自定义。 | 固定规格。 |
| 备份恢复 | 云盘快照式备份，备份、恢复速度更快。 | 数据物理备份，备份、恢复速度取决于数据量。 |
## 常见问题
Q：磁盘型的引擎版本是什么？
A：磁盘型采用的是阿里云自研的引擎版本（兼容Redis 6.0版本）。关于命令支持度的详细信息，请参见[Tair（企业版）命令支持与限制](../developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。
## 相关文档
[磁盘型实例规格](capacity-storage-type.md)
[创建实例](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md)
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
