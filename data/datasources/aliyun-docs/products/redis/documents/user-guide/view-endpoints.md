# 查看Tair（以及Redis开源版）的连接地址-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/view-endpoints

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

# 查看连接地址

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在连接云数据库 Tair（兼容 Redis）实例前，您需要先获取实例的连接地址。实例的VIP（Virtual IP Address）地址在维护、变配时可能发生变化，因此建议您在业务中使用实例的连接地址（例如r-2vcl6xcftp1nu7****.com），确保连接的可用性。您可以在控制台查看各类型的连接地址。

## 前提条件

已将客户端的IP地址添加至实例的白名单中，更多信息请参见[设置白名单](products/redis/documents/getting-started/step-2-configure-whitelists.md)。

## 操作步骤

- 

访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。

- 

在连接信息区域，可查看到各连接类型的地址和端口号。

说明

- 

如需使用公网连接实例，请先申请该实例的[公网连接地址](products/redis/documents/user-guide/apply-for-a-public-endpoint-for-an-apsaradb-for-redis-instance.md)。

- 

直连模式的集群架构云原生版实例不支持申请公网，更多信息请参见[查看连接地址](products/redis/documents/user-guide/view-endpoints.md)。

接下来，您可以连接实例，更多信息请参见[通过](products/redis/documents/user-guide/use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[redis-cli](products/redis/documents/user-guide/use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[连接实例](products/redis/documents/user-guide/use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)。

## 代理模式与直连模式

云数据库 Tair（兼容 Redis）支持的连接模式：

- 

代理模式

客户端通过代理服务器（Proxy Server）连接实例。

Proxy为阿里云完全自研，承担着路由转发、负载均衡、模式转换与故障转移等职责，同时支持执行[阿里云自研的](https://help.aliyun.com/zh/tair/developer-reference/in-house-commands-for-tair-instances-in-proxy-mode#concept-2353538)[Proxy](https://help.aliyun.com/zh/tair/developer-reference/in-house-commands-for-tair-instances-in-proxy-mode#concept-2353538)[命令](https://help.aliyun.com/zh/tair/developer-reference/in-house-commands-for-tair-instances-in-proxy-mode#concept-2353538)，具有聚合连接、增强读性能、简单易用等优势，有助于您设计更高效的业务系统，更多信息请参见[Tair Proxy](https://help.aliyun.com/zh/tair/product-overview/features-of-proxy-nodes#concept-2334147)[特性说明](https://help.aliyun.com/zh/tair/product-overview/features-of-proxy-nodes#concept-2334147)。

- 

直连模式

若实例为标准架构，客户端将直接连接主节点（Master）。

若实例为集群架构，客户端将直接连接实例，由原生Redis Cluster进行负载均衡等，与原生Redis Cluster连接模式完全一致。

各架构的网络、连接功能矩阵

为便于阅读，约定✔️表示支持该功能，❌表示不支持该功能。

| 部署模式 | 实例架构 | 连接类型 | 专有网络 VPC | 公网 |
| --- | --- | --- | --- | --- |
| 云原生 | 标准架构 | 直连模式 | ✔️ | ✔️ |
| 集群架构 1 | 直连模式 | ✔️ | ❌ |  |
| 代理模式（Proxy） | ✔️ | ✔️ |  |  |
| 读写分离架构 | 代理模式（Proxy） | ✔️ | ✔️ |  |
| 经典 | 标准架构 | 直连模式 | ✔️ | ✔️ |
| 集群架构 2 | 代理模式（Proxy） 直连模式 | ✔️ | ✔️ |  |
| 读写分离架构 | 代理模式（Proxy） | ✔️ | ✔️ |  |


重要

1云原生集群架构实例只能支持直连模式和代理模式的其中一种模式。

2经典集群架构实例可以同时支持直连模式和代理模式。

## 专有网络与公网

云数据库 Tair（兼容 Redis）支持的网络类型：

- 

专有网络

专有网络VPC（Virtual Private Cloud）是私有网络环境，通过底层网络协议，在网络二层完成网络隔离，具备安全可靠、灵活可控、简单易用的特性和较强的可扩展性。更多信息请参见[什么是专有网络](products/vpc/documents/what-is-vpc.md)[VPC](products/vpc/documents/what-is-vpc.md)。

应用场景：[ECS](products/ecs/documents/user-guide/what-is-ecs.md)[实例](products/ecs/documents/user-guide/what-is-ecs.md)与实例属于同一专有网络，并通过专有网络连接至实例，可获得更高的安全性和更低的网络延迟。

- 

公网（Internet）

公网即互联网，更多信息请参见[申请公网连接地址](products/redis/documents/user-guide/apply-for-a-public-endpoint-for-an-apsaradb-for-redis-instance.md)。

通过公网连接实例不会产生阿里云流量费用，但存在一定的安全风险，推荐通过专有网络连接以获取更高的安全性。

应用场景：本地设备、不同专有网络的ECS实例和第三方云产商可通过公网连接实例。

## 常见问题

### 为什么不显示连接地址？

您需要将客户端的IP地址添加至实例的白名单，控制台才会显示连接地址。具体操作请参见[设置白名单](products/redis/documents/getting-started/step-2-configure-whitelists.md)。

### 为什么没有申请公网地址的操作入口？

没有申请公网地址的操作入口，有两个原因：

- 

如果连接信息区域，也不显示专有网络连接地址，说明还未配置实例的白名单，请先配置白名单。具体操作请参见[设置白名单](products/redis/documents/getting-started/step-2-configure-whitelists.md)。

- 

若实例为云原生版集群架构直连模式，则不支持申请公网，无法通过公网连接实例，请通过专有网络连接实例。

说明

确认实例是否为云原生集群架构直连模式，请参见[怎样知道实例是否为云原生集群架构直连模式？](products/redis/documents/user-guide/view-endpoints.md)。

如果应用所在的ECS实例与实例不在同一VPC，或您的应用不在阿里云上，您可以考虑使用云原生集群架构代理模式。由于云原生集群架构直连模式不能直接变配为代理模式，您可以通过的恢复实例功能完成迁移变配，将源实例的备份数据恢复至新实例中，在页面选择为代理模式，具体操作请参见[从备份集恢复至新实例](products/redis/documents/user-guide/restore-data-from-a-backup-set-to-a-new-instance.md)。

警告

变配云原生版实例的集群架构后，需根据所使用的模式对连接代码进行适当修改，否则可能会无法连接，请谨慎操作。

### 怎样知道实例是否为云原生集群架构直连模式？

您可以在[控制台](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)的实例信息页面确认实例的部署模式和实例规格是否为云原生集群架构。在实例信息页面的配置信息区域，确认实例规格为集群版，且部署模式为云原生。

在实例信息页面的连接信息区域，确认是否为直连。

云原生集群架构直连模式不支持申请公网地址。因此，连接信息区域公网访问对应的申请连接地址为置灰状态无法单击。

### 怎样开启代理模式的连接地址？

- 

读写分离架构实例、经典集群架构实例，默认具有代理模式的连接地址，无需手动开启。

- 

云原生集群架构实例，您在创建实例时可以选择代理模式或直连模式。创建实例后，无法将直连模式改为代理模式，也无法将代理模式改为直连模式。

- 

标准架构实例为主备架构（单副本实例只有一个主节点），无需开启代理模式的连接地址。仅集群架构与读写分离架构支持代理模式。

### 是否支持连接备节点？怎么没看到备节点的连接地址？

云数据库 Tair（兼容 Redis）的备节点提供HA高可用服务，用于主备切换。不支持直接连接备节点。

## 相关文档

- 

连接云数据库 Tair（兼容 Redis）的方法：

- 

[通过](products/redis/documents/user-guide/use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[redis-cli](products/redis/documents/user-guide/use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[连接实例](products/redis/documents/user-guide/use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)

- 

[客户端程序连接教程](products/redis/documents/user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance.md)

- 

[使用直连模式连接实例](products/redis/documents/user-guide/use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)

- 

若客户端无法正常连接实例，且产生报错信息，您可以在[常见报错](products/redis/documents/support/common-errors-and-troubleshooting.md)中匹配解决方案。

[上一篇：使用公网地址连接实例](products/redis/documents/user-guide/use-a-public-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)[下一篇：实例的认证方式](products/redis/documents/user-guide/logon-methods.md)

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
