# 手动执行主备切换实现容灾演练与优化访问延迟-云数据库Tair-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/manually-switch-workloads-from-a-master-node-to-a-replica-node

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

# 手动执行主备切换

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库 Tair（兼容 Redis）实例支持手动执行主备切换，即主动交换主节点与备节点的角色。与系统自动故障转移不同，手动切换为您提供了在非故障场景下主动管控实例的能力。

## 应用场景

- 

容灾演练：在业务低峰期模拟节点故障，验证业务应用在数据库发生切换时的容灾能力和可靠性。

- 

优化访问延迟：当应用与主节点部署在不同可用区时，通过主备切换，将主节点切换至应用所在的可用区，实现就近访问，降低网络延迟。

### 场景示例

在本案例的环境中，应用所属的ECS实例在可用区B，实例的主节点在可用区A，ECS需要跨可用区连接主节点，将导致网络延迟增高，影响实例的性能和业务的运行。

为优化云资源的部署架构，您可以将节点的角色进行互换。在本案例中，执行主备切换，可用区B中的节点角色变更为主节点（仅更改节点的角色，不会改变节点所属的可用区和ID），从而实现ECS和实例同可用区的就近连接，网络延时最小。

## 前提条件

实例类型为高可用。

说明

单副本架构不支持主备切换。

## 切换影响

- 

执行切换的数据节点将出现秒级的连接闪断，同时，为避免主备切换引起潜在的数据丢失风险（例如主备节点数据同步延迟引起数据不一致）、DNS缓存引起的数据双写，该数据节点还会出现30秒内的只读状态。

- 

实例处于切换中状态时，您将无法执行实例级别的操作（例如变更配置、迁移可用区等）。

说明

关于无感切换

当实例和客户端版本满足以下条件时，可实现无感主备切换，从而避免连接闪断和只读状态对业务的影响：

- 

实例版本：7.0.2.9及以上。

- 

客户端版本：Valkey-Java 5.3.0及以上，或Valkey-Go 1.0.67及以上。

## 操作步骤

- 

访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏，单击服务可用性。

- 

在数据节点区域框，选中需要执行切换的数据分片，单击主从切换。

说明

若实例为集群架构，您可以在本页面查看到各数据分片中，主备节点所属的可用区信息。

- 

在右侧弹出的面板中，选择切换的生效时间。

- 

立即生效：立即执行主备切换。

- 

可运维时间内生效：在您设置的可维护时间段内进行切换。关于如何查看和修改可维护时间段，请参见[设置可维护时段](products/redis/documents/user-guide/set-a-maintenance-window.md)。

说明

如果您选择可运维时间内生效，系统会立即开始进行资源申请、数据同步等前置准备工作，此时实例状态将变为切换中，但这并不会影响实例的正常服务。实际的节点角色切换及伴随的业务影响（如连接闪断和只读状态）只会在到达可维护时段时才会发生。

- 

单击确定。

为保障安全，请按界面提示完成二次验证（例MFA），验证后15分钟内免重复验证。

## 相关API

| API 接口 | 说明 |
| --- | --- |
| [SwitchInstanceHA - 切换实例](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-switchinstanceha-redis.md) [HA](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-switchinstanceha-redis.md) | 手动执行主备切换，可应用于容灾演练、多可用区场景下的应用就近连接等需求。 |


## 相关文档

本文介绍的是手动执行的主备切换。作为高可用能力的另一核心，云数据库 Tair（兼容 Redis）也支持自动故障转移。系统会持续监测节点的健康状态，一旦发现主节点不可用，便会自动触发主备切换，将备节点提升为新的主节点，从而保障服务的高可用性。更多信息，请参见[高可用](products/redis/documents/user-guide/master-replica-switchovers.md)。

[上一篇：高可用](products/redis/documents/user-guide/master-replica-switchovers.md)[下一篇：重启或重搭代理节点](products/redis/documents/user-guide/restart-or-rebuild-a-proxy-node.md)

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
