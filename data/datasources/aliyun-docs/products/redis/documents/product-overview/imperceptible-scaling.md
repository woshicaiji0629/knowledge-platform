# 无感扩缩容功能特性注意事项-云数据库Tair-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/imperceptible-scaling

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

# 集群无感扩缩容介绍

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库 Tair（兼容 Redis）集群架构实例在扩容（增加集群分片数量）、缩容（减少集群分片数量）过程中，能够有效消除原生Redis集群可能会产生的-ASK、-TRYAGAIN错误，从而实现无感扩缩容。

## 特性说明

与原生Redis集群扩缩容相比，云数据库 Tair（兼容 Redis）集群架构实例扩缩容具有以下特点：

- 

高效的扩缩容管理：通过中心化的控制组件，实现对集群行为的高效、精准控制。

- 

原子性数据迁移：深入修改内核的数据复制逻辑，保证数据迁移的原子性。在扩缩容期间，数据以Slot为单位进行数据迁移，不会造成Slot分裂，也不会产生业务无法处理的-ASK、-TRYAGAIN错误，大幅度提高了业务的稳定性和用户体验。

说明

- 

在RESP集群协议中，非数据操作类命令例如PING、INFO等，以及特殊命令如PUB/SUB类和BLOCKING类命令，在Slot迁移后无法被自动重定向，需要应用层定时更新路由表来获取扩缩容后的最新拓扑。

- 

为了保证数据迁移前后的数据一致性，在数据迁移的最终阶段，对应Slot的写请求时延会增加，但不会失败。

- 

缩短数据迁移时长：在扩缩容过程中，本方案采用以Slot为单位进行数据迁移，相较于以Key为单位的数据迁移方案，能够显著提高效率，从而有效缩短数据迁移的时长。

- 

弹性资源伸缩：支持弹性伸缩，满足不同业务场景下的资源需求。

## 适用实例

- 

实例部署模式为云原生版。

- 

实例架构为集群架构。

- 

适用下述实例版本：

- 

Redis开源版5.0实例（小版本5.2.0及以上）

- 

Redis开源版6.0实例（小版本6.0.2.0及以上）

- 

Redis开源版7.0实例

- 

Tair（企业版）内存型兼容Redis 5.0版（小版本5.0.34及以上）

- 

Tair（企业版）内存型兼容Redis 6.0版

- 

Tair（企业版）内存型兼容Redis 7.0版

- 

Tair（企业版）持久内存型

- 

Tair（企业版）磁盘型

## 注意事项

- 

客户端要求：

- 

若实例为集群架构直连模式，需要客户端能正确处理MOVED命令。

- 

若实例为集群架构代理模式，在缩容时会释放部分代理节点，产生连接断开，需要客户端具有断线重连能力。

- 

扩缩容期间，可能会有较高的延迟导致客户端命令超时，需要客户端具有超时重连能力。

说明

建议使用[推荐的客户端](products/redis/documents/product-overview/important-notes-for-tair-and-apsaradb-for-redis-clients.md)。

- 

特殊命令影响说明：

- 

在扩缩容期间使用Blocking类命令可能会产生报错。

- 

在扩缩容期间使用Pub/Sub类命令不提供一致性保证，且视客户端实现可能会产生报错。

[上一篇：可观测性能力介绍](products/redis/documents/product-overview/observability.md)[下一篇：Tair（企业版）](products/redis/documents/product-overview/overview-1.md)

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
