# 全球多活数据库跨域数据同步-全球多活-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/overview-of-global-distributed-cache-for-tair

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/redis/documents/product-overview.md)

- [快速入门](products/redis/documents/getting-started.md)

- [Tair AI能力](products/redis/documents/tair-ai-ability.md)

- [操作指南](products/redis/documents/user-guide.md)

- [实践教程](products/redis/documents/use-cases.md)

- [安全合规](products/redis/documents/security-compliance.md)

- [开发参考](products/redis/documents/developer-reference.md)

- [服务支持](products/redis/documents/support.md)

- [视频专区](products/redis/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 全球多活

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库 Tair（兼容 Redis）自研的全球多活数据库系统，具备跨域复制（Geo-replication）能力，能够迅速实现异地多个实例的数据同步服务，轻松支持数据的异地多活和灾备。一组全球多活实例最多由三个子实例组成，子实例之间自动进行数据的实时同步。此功能可有效缩短数据与用户之间的物理距离，降低访问延迟、提升程序的响应速度。

## 背景信息

当业务分布较广时，跨地域的远距离访问架构会导致访问延迟显著增加，影响用户体验。借助阿里云的Tair（企业版）全球多活功能，可帮助您解决业务因跨地域访问导致延迟大的问题，全球多活功能具有如下优势：

- 

- 

- 

- 

- 

- 

- 

| 优势 | 说明 |
| --- | --- |
| 高可靠 | 支持断点续传，可容忍天级别的同步中断，避免了原生 Redis 架构在跨机房或地域进行增量同步的局限性。 支持自动处理子实例的主备切换、备份重搭等异常事件。 |
| 高性能 | 高吞吐：标准架构下同步通道单向可达 5 万 QPS，集群架构下会随数据分片或节点的数量线性扩展。 低延迟：同一洲内的地域间同步，在物理网络质量稳定的情况下，时延不超过 1 秒。跨洲地域的平均时延约 1 至 5 秒，该值由链路吞吐和链路的往返时延 RTT（Round-trip time）决定。 |
| 高正确性 | Binlog 按产生的顺序同步到对端。 支持回环控制，避免 Binlog 循环同步。 支持抗重放（exactly once），确保被同步的 Binlog 仅会被执行 1 次。 |


应用场景

此功能可应用于跨地域数据同步场景及多媒体、游戏、电商等行业的全球化业务部署等场景。

| 应用场景 | 说明 |
| --- | --- |
| 异地多活 | 异地多活是指分布在异地的多个站点同时对外提供服务的业务场景，是高可用架构设计的一种，所有站点可同时对外提供服务，可实现应用就近访问等场景。 |
| 数据灾备 | 借助子实例间数据双向同步的特性，可实现同城灾备、两地三中心灾备及三地灾备等多种数据灾备场景。 |
| 负载分摊 | 在某些场景下（例如大型促销），预测可能会有超大 QPS 请求和访问流量，可将流量分摊至多个子实例，突破单个实例的负载限制。 |
| 数据同步 | 实现一组全球多活实例下的子实例双向数据同步，可应用于数据分析或测试等场景。 |


## 功能简介

Tair（企业版）全球多活是所有全球多活子实例（简称子实例）及链路的逻辑集合，所有子实例通过同步通道保持实时数据同步。同步粒度为实例级，即子实例的所有数据都会被同步。架构图如下：

组件介绍说明：

| 组件 | 说明 |
| --- | --- |
| 子实例 | 构成全球多活实例的子实例，即独立的实例，是构成多活实例的基本服务单元。所有子实例均可读写，且各自提供独立的连接地址。子实例之间通过实时双向同步保持数据一致性，数据一次性级别为最终一致性。 说明 子实例需为 Tair（企业版） [内存型](products/redis/documents/product-overview/dram-based-instances.md) 实例，而 Redis 开源版 不支持本功能。 |
| 同步通道 | 负责子实例之间实时数据同步的链路，为单向链路，子实例的双向复制由两个对向的同步通道构成。 Tair（企业版） 全球多活 在原生 Redis AOF 日志的基础上增加了 server-id、opid 等信息，同步通道通过获取 Binlog 实现数据同步。 |
| 通道管理器 | 管理同步通道生命周期，负责子实例上的主备切换、备份重搭等异常事件的处理。 |


说明

暂不支持中国内地与其他地域之间的跨境同步。在一个全球多活实例中，所有的子实例必须全部位于中国内地或全部位于其他地域，更多信息请参见[全球多活使用限制](products/redis/documents/user-guide/limits-of-global-distributed-cache-for-redis.md)。

## 费用说明

该功能免费，仅会根据子实例Tair（企业版）内存型的规格收费，详情请参见[计费项](products/redis/documents/product-overview/billable-items.md)。

## 使用说明

重要

为保障跨地域网络的质量与稳定性，云原生模式的全球多活功能目前采用白名单机制提供。开通前，我们将对您计划使用的地域进行网络能力评估。如需使用，请提交工单申请。

- 

[创建](products/redis/documents/user-guide/create-a-distributed-instance.md)第一个全球多活子实例，您可以转化已有的Tair（企业版）内存型实例或创建一个新的实例。

创建第一个子实例后，全球多活实例也自动被创建。

- 

在全球多活实例中，通过创建新实例的方式，[添加](products/redis/documents/user-guide/add-a-child-instance-to-a-distributed-instance.md)第2或第3个子实例。

- 

在业务代码中，将不同地域的请求指向就近的子实例连接地址，为用户提供更为优质的就近访问服务体验。

## 常见问题

- 

Q：可以同时对全球多活子实例进行小版本升级吗？

A：为了确保业务的连续性和稳定性，建议您将子实例的升级时间错开半小时以上。以避免在升级过程中，实例同时出现服务中断的情况，从而降低对业务的影响。

- 

Q：是否支持变更全球多活子实例的架构，例如将标准架构变更为集群架构？

A：不支持，建议提前进行相应的规划。

- 

Q：是否支持变更全球多活子实例的规格，例如将标准架构8GB升级到16GB？

A：支持，请确保各子实例规格一致。建议对所有子实例均进行相同变配，若各子实例的规格不一致，可能会出现性能或容量问题。

- 

Q：支持全球多活实例支持多写吗？

A：支持在不同子实例写入数据，但业务上应避免多个子实例在同一时刻或相近的时间修改同一个Key，否则可能造成数据不一致，更多信息请参见[数据一致性限制](products/redis/documents/user-guide/limits-of-global-distributed-cache-for-redis.md)。

## 相关文档

- 

[创建分布式实例](products/redis/documents/user-guide/create-a-distributed-instance.md)

- 

[创建分布式子实例](products/redis/documents/user-guide/add-a-child-instance-to-a-distributed-instance.md)

- 

[全球多活使用限制](products/redis/documents/user-guide/limits-of-global-distributed-cache-for-redis.md)

[上一篇：下载备份集](products/redis/documents/user-guide/download-a-backup-file.md)[下一篇：创建分布式实例](products/redis/documents/user-guide/create-a-distributed-instance.md)

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
