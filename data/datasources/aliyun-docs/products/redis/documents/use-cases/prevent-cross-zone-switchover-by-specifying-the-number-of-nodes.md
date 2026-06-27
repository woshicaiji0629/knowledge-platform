# 通过自定义节点数规避跨可用区切换-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/use-cases/prevent-cross-zone-switchover-by-specifying-the-number-of-nodes

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

# 通过自定义节点数规避跨可用区切换

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在多可用区部署的云原生版实例中，当主可用区的节点数量大于或等于2（总节点数大于等于3）时，若主节点发生故障，高可用系统（HA）将优先在主可用区内进行切换。该功能可避免因切换到备可用区而导致的业务访问时延增加的问题。

说明

当前云原生版标准架构、集群架构均自动启用该功能，无需您手动干预。本文将以集群架构为例进行说明。

## 背景信息

默认情况下，多可用区部署表示将集群实例中每分片的主备节点分别部署在同一地域内的不同可用区中（电力和网络互相独立的物理区域），这为实例提供了较高的容灾能力。

当某分片的主节点出现故障时，实例会自动触发故障切换，降低故障带来的影响。而客户端通常也部署在主可用区，在未发生实例故障切换时，客户端与集群实例的主节点处于同可用区，此时的访问时延是最低、最健康的。以3分片集群架构为例，如下图所示：

当某分片发生主节点故障切换时，高可用系统（HA）会把分片主节点切换到位于备可用区的备节点上，此时客户端与实例为跨可用区（机房）访问，这会造成访问时延明显增加。

说明

跨可用区访问的时延要远高于同可用区访问，关于阿里云各可用区间访问的平均时延请参见[云网络互访性能](https://nis.console.aliyun.com/performance/netana?type=inner_region)。

由于云数据库 Tair（兼容 Redis）为高性能、低延迟的内存数据库，如果存在较高的网络延迟，这将直接影响到整体业务请求的响应时间。因此，本方案推荐您在集群实例的主可用区额外增加一个备节点，该方案兼顾了高性能稳定性和高容灾能力。

- 

当主节点发生故障切换时，实例会优先在同可用区内切换，切换后主节点仍在主可用区，不会造成访问时延增加。

- 

若主可用区发生可用区级别的故障，实例会进行跨可用区切换，提供较高的容灾能力。

## 方案介绍

云数据库 Tair（兼容 Redis）支持为集群实例的分片自定义2~5个节点。

- 

当节点数为2时，默认为主、备可用区各部署一个节点。

- 

当节点数为3时，默认在主可用区部署2个节点、备可用区部署1个节点。

- 

当节点数为4~5时，您可以自行分配剩余节点部署在主可用区或备可用区。

本示例以3分片、3节点集群架构（主可用区2节点、备可用区1节点）为例进行介绍，如下图所示：

若此时某分片发生主节点故障切换，高可用系统（HA）会优先把分片主节点切换到位于主可用区的备节点上，此时客户端与实例仍为同可用区访问，不会造成访问时延增加，如下图所示：

## 操作指南

- 

若您未创建实例，您仅需创建多可用区、云原生版实例即可，具体操作请参见[创建实例](products/redis/documents/getting-started/step-1-create-an-apsaradb-for-redis-instance.md)。

其中，实例主可用区的节点大于等于2的配置如下所示：在设置页面中，配置智能读写分离（可选关闭或开启，无代理组件的集群架构-直连模式无法启用该功能）。选择节点数（例如3节点表示1主2备，开启读写分离后备节点可读；集群架构下每个分片均为对应节点数）。设置节点分配（主可用区）的节点数量，备可用区节点数 = 节点数 - 主可用区节点数，建议主备可用区节点数均不小于2，总节点数不小于4。

- 

若您已创建了单可用区、云原生版实例，您可以先将实例[迁移成多可用区](products/redis/documents/user-guide/migrate-an-instance-across-zones.md)，并在[增删备节点](products/redis/documents/user-guide/node-management.md)页面中增加主可用区的节点数为大于等于2。

- 

若您已创建了多可用区、云原生版实例，您可以在[增删备节点](products/redis/documents/user-guide/node-management.md)页面中增加主可用区的节点数为大于等于2。在节点分布（可用区）区域，单击主可用区操作列的修改按钮。

- 

若您已创建了经典版部署模式的实例，您可以创建一个符合上述条件的新实例，并通过DTS将数据同步到新实例中，具体操作请参见[同阿里云账号单向同步](products/redis/documents/user-guide/configure-one-way-data-synchronization-between-apsaradb-for-redis-instances.md)。

[上一篇：实践教程](products/redis/documents/use-cases.md)[下一篇：云数据库 Tair（兼容 Redis）开发运维规范](products/redis/documents/use-cases/development-and-o-and-m-standards-for-apsaradb-for-redis.md)

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
