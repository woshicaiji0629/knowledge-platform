# 兼容Redis协议标准的数据库-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/what-is-apsaradb-for-redis

# 什么是云数据库 Tair（兼容 Redis）
云数据库 Tair（兼容 Redis）（Tair (Redis OSS-compatible)）是兼容Redis协议标准的数据库服务，基于双机热备架构及集群架构，可满足高吞吐、低延迟及弹性变配等业务需求。
## 前置概念
阅读本文前，您可能需要了解如下概念：
[什么是](https://www.aliyun.com/getting-started/what-is/what-is-redis)[Redis？](https://www.aliyun.com/getting-started/what-is/what-is-redis)
[什么是缓存？](https://www.aliyun.com/getting-started/what-is/what-is-cache)
[什么是云数据库？](https://www.aliyun.com/getting-started/what-is/what-is-cloud-database)
[什么是云原生？](https://www.aliyun.com/getting-started/what-is/what-is-cloud-native)
您也可以通过学习云数据库 Tair（兼容 Redis）[学习路径](https://help.aliyun.com/product/26340.html)，由浅入深地学习Tair产品知识。
## 为什么选择云数据库 Tair（兼容 Redis）
硬件部署在云端，提供完善的基础设施规划、网络安全保障和系统维护服务，您可以专注于业务创新。
支持String（字符串）、List（链表）、Set（集合）、Sorted Set（有序集合）、Hash（哈希表）、Stream（流数据）等多种数据结构，同时支持Transaction（事务）、Pub/Sub（消息订阅与发布）等高级功能。
在Redis开源版的基础上推出Tair（企业版）内存数据库产品，提供[内存型](dram-based-instances.md)、[持久内存型](persistent-memory-optimized-instances-1.md)、[磁盘型](essd-based-instances-1.md)供您选择。
更多详情请参见[与自建](comparison-between-apsaradb-for-redis-and-self-managed-redis.md)[Redis](comparison-between-apsaradb-for-redis-and-self-managed-redis.md)[的对比](comparison-between-apsaradb-for-redis-and-self-managed-redis.md)和[应用场景](common-scenarios.md)。
## 支持的实例类型与架构
支持Redis开源版、Tair（企业版）和Tair Serverless KV三种实例类型。
| 实例类型 | 简介 |
| --- | --- |
| Redis 开源版 | 兼容 Redis 的高性能内存数据库产品，支持标准（主备）、集群、读写分离等架构。 |
| [Tair（企业版）](overview-1.md) | Tair（企业版） 作为在 Redis 开源版 的基础上开发的强化版 Redis 服务，从访问延时、持久化需求、整体成本这三个核心维度考量，基于 DRAM（Dynamic Random Access Memory）、NVM（Non-Volatile Memory）和 ESSD 云盘等存储介质，推出了多种不同形态的产品，为您提供更强的性能、更多的数据结构和更灵活的存储方式，满足不同场景下的业务需求。 [内存型](dram-based-instances.md) ：采用多线程模型，集成阿里巴巴 Tair 的部分特性，支持多种 Tair 数据结构，对于部分特殊业务有很高的适用性。 [持久内存型](persistent-memory-optimized-instances-1.md) ：基于持久内存技术，为您提供大容量、兼容 Redis 的内存数据库产品。数据持久化不依赖传统磁盘，保证每个操作持久化的同时提供近乎 Redis 开源版 的吞吐和延时，极大提升业务数据可靠性。 [磁盘型](essd-based-instances-1.md) ：基于 ESSD 与 SSD 研发，兼容 Redis 核心数据结构与接口，成本最低为 Redis 开源版 的 15%，性能约为 Redis 开源版 的 60%。可提供大容量、低成本、强持久化的数据库服务，适用于兼容 Redis、需要大容量且较高访问性能的温冷数据存储场景。 |
| [Tair Serverless KV](tair-serverless-kv-redis-compatible-edition.md) | Tair Serverless KV 实例为分布式集群架构，具备自动扩缩容以及按实际用量计费的能力。高峰时自动扩容保障业务平稳，低峰时自动缩容节省成本。全程自动化无缝伸缩，业务无感知，能够显著降低运维的复杂度。 |
支持灵活的多种部署架构，能够满足不同的业务场景。
| 架构类型 | 说明 |
| --- | --- |
| [标准版-单副本](https://help.aliyun.com/zh/document_detail/52685.html#concept-fx3-jrg-tdb) | 适用于纯缓存场景，支持单节点集群弹性变配，满足高 QPS（Queries per Second）场景，提供超高性价比。 |
| [标准架构](standard-master-replica-instances.md) | 系统工作时主节点（Master）和副本（Replica）数据实时同步，若主节点发生故障，系统会快速将业务切换至备节点，全程自动且对业务无影响，保障服务高可用性。 |
| [集群版-单副本](https://help.aliyun.com/zh/document_detail/59201.html#concept-ydy-g24-tdb) | 单副本集群版实例采用集群架构，每个分片服务器采用单副本模式。适用于纯缓存类业务或者 QPS 压力较大的业务场景。 |
| [集群架构](cluster-master-replica-instances.md) | 集群（Cluster）实例采用分布式架构，每个数据分片都支持主备切换（master-replica），能够自动进行容灾切换和故障迁移，保障服务高可用。同时提供多种规格，您可以根据业务压力选择对应规格，还可以随着业务的发展自由变配规格。集群版支持两种连接模式： [代理模式（推荐）](cluster-master-replica-instances.md) ：提供智能的连接管理，降低应用开发成本。 [直连模式](cluster-master-replica-instances.md) ：客户端绕过代理服务器直接访问后端数据分片，可降低网络开销和服务响应时间，适用于对 Redis 响应速度要求极高的业务。 |
| [读写分离功能](read-or-write-splitting-instances-1.md) | 读写分离实例通过主备（Master-Replica）架构实现高可用，主节点挂载只读副本（Read Replica）实现数据复制，支持读性能线性扩展。 只读副本可以有效缓解热点 Key 带来的性能问题，适合高读写比的业务场景。 读写分离实例有两种版本。 读写分离（ 云原生 版）：只读节点均从主节点同步数据，为星型复制架构，支持自定义只读节点数量（集群架构每分片 1 ~ 4 个，标准架构 1 ~ 9 个），适合超大规模高读写比的业务场景。 读写分离（ 经典 版，已停售）：只读节点采取链式复制架构，支持配置 1 个、3 个、5 个只读节点。 |
## 开始使用
免费试用：阿里云免费试用面向符合条件的新用户，提供一定时间段的[免费试用](https://free.aliyun.com/?searchKey=redis)阿里云产品的权益。
创建实例：[创建](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md)[Tair](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md)[实例](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md)。
## 常见问题
Tair与Redis是什么关系？
云数据库 Tair（兼容 Redis）是完全兼容Redis协议的云原生高性能内存数据库。任何兼容Redis的客户端均可与云数据库 Tair（兼容 Redis）建立连接，从而进行数据存储及相应操作。
同时，Tair（企业版）版是强化版Redis服务，提供超高性能、超高性价比等一系列选择，更多信息请参见[Tair（企业版）与](comparison-between-apsaradb-for-redis-enhanced-edition-and-apsaradb-for-redis-community-edition.md)[Redis](comparison-between-apsaradb-for-redis-enhanced-edition-and-apsaradb-for-redis-community-edition.md)[开源版特性对比](comparison-between-apsaradb-for-redis-enhanced-edition-and-apsaradb-for-redis-community-edition.md)。
Tair兼容Redis哪些版本？
Tair（企业版）[内存型](dram-based-instances.md)（兼容Redis 7.0）：完全兼容Redis7.0版本及以下版本接口，额外支持Tair扩展数据结构。
Tair（企业版）[内存型](dram-based-instances.md)（兼容Redis 6.0）：完全兼容Redis6.2版本及以下版本接口，额外支持Tair扩展数据结构。
Tair（企业版）[内存型](dram-based-instances.md)（兼容Redis 5.0）：完全兼容Redis5.0版本及以下版本接口，额外支持Tair扩展数据结构。
Tair（企业版）[持久内存型](persistent-memory-optimized-instances-1.md)：兼容Redis6.0版本及以下版本接口，部分限制请参见[Tair（企业版）命令支持与限制](../developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。
Tair（企业版）[磁盘型](essd-based-instances-1.md)：兼容Redis6.0版本及以下版本接口，部分限制请参见[Tair（企业版）命令支持与限制](../developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。
Redis开源版：可选择7.0、6.0、5.0或4.0，完全兼容社区大版本并向下兼容。
Tair兼容Redis哪些命令和操作？
云数据库 Tair（兼容 Redis）兼容支持绝大部分开源Redis的命令和操作，仅禁用了个别命令。具体请参见：
[Redis](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)
[Tair（企业版）命令支持与限制](../developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)
[Tair Serverless KV](commands-supported-by-tair-serverless-kv-instances.md)[命令支持](commands-supported-by-tair-serverless-kv-instances.md)
Tair是否有CPU、带宽和连接数等限制？
是的。云数据库 Tair（兼容 Redis）实例的CPU处理能力、网络带宽和最大连接数主要由实例类型和架构（集群、非集群等）决定。在相同类型和架构下，实例规格的主要差异体现在内存容量上，而其他性能指标仅存在轻微变化。您可以在[实例规格](overview-4.md)查看每个规格的具体性能。
Tair支持数据持久化吗？
支持。云数据库 Tair（兼容 Redis）采用内存加硬盘的方式存储数据，通过AOF和RDB[持久化策略](../user-guide/backup-and-restoration-solutions.md)将Tair数据保存到硬盘中。
Tair支持修改配置参数吗？
支持，更多信息请参见[设置参数](../user-guide/modify-the-values-of-parameters-for-an-instance.md)。
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
