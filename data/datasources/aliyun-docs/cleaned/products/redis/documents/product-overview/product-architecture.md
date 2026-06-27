# 实例架构类型与选择指南-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/product-architecture/

# 产品架构
云数据库 Tair（兼容 Redis）支持集群架构、标准架构，同时还支持动态开启智能读写分离功能。标准架构、集群架构都有单节点和多节点两种类型。您可根据业务场景选用不同架构的实例。
## 架构概览
如需了解以下实例架构的详细信息，请单击架构名称跳转到相应的文档。
警告
单节点（副本）架构不能保障数据可用性和服务连续性，选用前请务必确认风险，不建议您在生产环境中使用该架构的实例。
### 集群架构
| 实例架构 | 架构图 | 适用场景 |
| --- | --- | --- |
| [集群架构](cluster-master-replica-instances.md) 每个分片均采用主备（master-replica）多节点架构。 |  | 数据量较大的场景。 QPS 压力较大的场景。 吞吐密集型应用场景。 |
| [集群架构（开启读写分离）](read-or-write-splitting-instances-1.md) 每个分片均采用读写分离架构。 |  | 适用读请求流量超过主节点性能上限时，通过增加只读节点来提升实例的读性能。 |
| [集群架构（单节点）](cluster-master-replica-instances.md) 每个分片均采用单节点（副本）架构。 |  | 无数据可靠性要求的纯缓存场景。 数据量较大的场景。 QPS 压力较大的场景。 吞吐密集型应用场景。 |
### 标准（未启用集群）架构
| 实例架构 | 架构图 | 适用场景 |
| --- | --- | --- |
| [标准架构](standard-master-replica-instances.md) 采用主备（master-replica）双节点架构，提供高可用切换。 |  | Redis 作为持久化数据存储使用的业务。 单个 Redis 性能压力可控的场景。 数据量较少的场景。 |
| [标准架构（开启读写分离）](read-or-write-splitting-instances-1.md) 由代理服务器（Proxy servers）、主备（master-replica）节点组成。 |  | 读取请求 QPS 压力较大的场景。 Redis 作为持久化数据存储使用的业务场景。 |
| [标准架构（单节点）](standard-master-replica-instances.md) 采用单节点架构。 |  | 无数据可靠性要求的纯缓存场景。 单个 Redis 性能压力可控的场景。 数据量较少的场景。 |
## 文档适用性说明
实例架构与产品版本（开源版和企业版）、系列类型（如内存型）、引擎版本（Redis版本号，如4.0或5.0）均为不同的概念，上表中涉及的文档适用于各产品版本、系列类型和引擎版本。例如实例若属于标准架构，就可以在[标准架构](standard-master-replica-instances.md)中查看其架构相关介绍，集群架构和读写分离功能同理。
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
