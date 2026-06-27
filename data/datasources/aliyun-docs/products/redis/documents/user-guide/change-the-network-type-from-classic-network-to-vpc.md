# 将实例从经典网络切换为专有网络VPC-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/change-the-network-type-from-classic-network-to-vpc

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

# 切换为专有网络VPC

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库 Tair（兼容 Redis）支持将实例从经典网络切换为专有网络，实现客户端与实例间通过同一专有网络互访，获得更高的安全性和更低的网络延迟。

## 前提条件

实例的网络类型为经典网络。

说明

您可以在实例的基本信息页面查看到网络类型。

## 影响

- 

实例切换为专有网络后，无法再切换为经典网络。

- 

实例会出现秒级的连接闪断，请在业务低峰期执行该操作并确保应用具备重连机制。

## 实例的网络类型

| 网络类型 | 说明 |
| --- | --- |
| [专有网络](products/vpc/documents/what-is-vpc.md) （推荐） | 专有网络 VPC（Virtual Private Cloud）是您专有的云上私有网络。不同的专有网络之间二层逻辑隔离，拥有较高的安全性和性能。客户端部署在 [ECS](products/ecs/documents/user-guide/what-is-ecs.md) [实例](products/ecs/documents/user-guide/what-is-ecs.md) 上时，通过专有网络连接至 Tair （以及 Redis 开源版 ） 实例，可获得更高的安全性和更低的网络延迟。 |
| 经典网络 | 经典网络中的云服务在网络上不进行隔离，只能依靠云服务自身的安全组或白名单策略来阻挡非法访问。 |


说明

客户端为专有网络，实例为经典网络时，客户端无法连接至实例。将实例切换至与客户端相同的专有网络后，可快速实现相互通信。

## 操作步骤

- 

访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。

- 

在连接信息区域框的右侧，单击切换为专有网络。

- 

在右侧弹出的面板中完成设置。

- 

- 

| 配置 | 说明 |
| --- | --- |
| 专有网络 | 选择目标专有网络和交换机。 说明 如果下拉框中没有可选的专有网络或交换机，说明实例所在的地域和可用区没有可用的专有网络或交换机。具体操作请参见 [创建和管理专有网络](products/vpc/documents/user-guide/create-and-manage-a-vpc.md) 和 [创建和管理交换机](products/vpc/documents/user-guide/create-and-manage-vswitch.md) 。 例如实例部署在华东 1（杭州）可用区 E，在选择专有网络后，如果没有可选的交换机则表示该专有网络在可用区 E 还未创建交换机（可能在其他可用区已创建）。请您先在华东 1（杭州）可用区 E 创建交换机后重试。 |
| 虚拟交换机： |  |
| 保留经典网络地址 | 根据业务需求选择是否保留经典网络地址： 保留 ：实例将同时拥有经典网络地址和专有网络地址，且经典网络地址不会变更。客户端可以通过这两种连接地址连接至实例，您需要在经典网络地址失效前，将客户端的数据库连接地址更换为专有网络地址。 不保留 ：实例的 VPC 网络地址将沿用原经典网络地址，您无需在客户端中修改连接地址串。但客户端将仅能通过 VPC 网络连接实例，无法继续通过经典网络连接实例。 |
| 保留天数 | 设置经典网络地址的保留天数。完成切换后，您也可以重新修改保留天数，具体操作，请参见 [修改原经典内网地址使用期限](products/redis/documents/user-guide/modify-the-expiration-date-of-a-classic-network-endpoint.md) 。 |


- 

单击确定。

## 常见问题

- 

Q：切换专有网络时，无法选择交换机，是什么原因？

A：如果下拉框中没有可选的专有网络或交换机，说明实例所在的地域和可用区没有可用的专有网络或交换机。具体操作请参见[创建和管理专有网络](products/vpc/documents/user-guide/create-and-manage-a-vpc.md)和[创建和管理交换机](products/vpc/documents/user-guide/create-and-manage-vswitch.md)。

例如实例部署在华东1（杭州）可用区E，在选择专有网络后，如果没有可选的交换机则表示该专有网络在可用区E还未创建交换机（可能在其他可用区已创建）。请您先在华东1（杭州）可用区E创建交换机后重试。

- 

Q：ECS实例与云数据库 Tair（兼容 Redis）在同一专有网络中，但位于不同的交换机（或不同可用区）时，能否通过专有网络连接云数据库 Tair（兼容 Redis）实例？

A：当ECS实例与云数据库 Tair（兼容 Redis）实例处于同一地域的同一专有网络内，即使它们位于不同交换机或可用区中，网络连通性也不会受到影响。请确保将ECS实例的内网IP地址添加到云数据库 Tair（兼容 Redis）实例的[IP](products/redis/documents/user-guide/configure-whitelists.md)[白名单](products/redis/documents/user-guide/configure-whitelists.md)中。

## 相关API

| API 接口 | 说明 |
| --- | --- |
| [SwitchNetwork](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-switchnetwork-redis.md) | 切换实例的专有网络 VPC。如果实例为经典网络，则会将其切换为专有网络。 |


## 相关文档

- 

[连接问题排查流程](products/redis/documents/support/how-do-i-troubleshoot-connection-issues-in-apsaradb-for-redis.md)

- 

[修改专有网络](products/redis/documents/user-guide/change-the-vpc-or-vswitch-of-an-instance.md)[VPC](products/redis/documents/user-guide/change-the-vpc-or-vswitch-of-an-instance.md)[或交换机](products/redis/documents/user-guide/change-the-vpc-or-vswitch-of-an-instance.md)

[上一篇：修改专有网络VPC或交换机](products/redis/documents/user-guide/change-the-vpc-or-vswitch-of-an-instance.md)[下一篇：修改连接地址或端口](products/redis/documents/user-guide/change-the-endpoint-or-port-number-of-an-instance.md)

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
