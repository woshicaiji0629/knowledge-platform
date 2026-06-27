# 购买资源预定-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/purchase-a-resource-reservation

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 购买资源预定

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

购买资源预定后，阿里云以私有池的方式预留属性一致的资源，使用私有池容量创建实例时可以确保创建成功。

## 背景信息

资源预定服务提供多种预定方式，您需要根据使用场景、资源类型和生效时间，制定合适的预定方案。更多信息，请参见[资源管家概述](products/ecs/documents/user-guide/overview-29.md)。

## 操作步骤

- 

进入资源预定创建页面。

- 

访问[ECS](https://ecs.console.aliyun.com/resourceAssuranceV2/region)[控制台-资源管家](https://ecs.console.aliyun.com/resourceAssuranceV2/region)。

- 

选择购中确定性保障>资源预定。

- 

在资源预定页签，单击创建资源预定。

- 

在输入需求配置页面，配置资源预定的信息。

- 

在所需资源信息区域，配置资源的属性信息。

- 

- 

- 

- 

- 

| 配置项 | 说明 | 示例 |
| --- | --- | --- |
| 地域 / 可用区 | 需要预留资源的地域和可用区。 | 华东 1（杭州）可用区 I 、 华东 1（杭州）可用区 H |
| 资源规格 | 需要预留资源的实例规格。除 vCPU、内存等实例规格自身属性外，建议您同时关注以下指标： 供应健康度：结合充足度、补货能力、热度，反映指定规格的实时供应健康情况。充足度和补货能力高，则供应健康度随之升高；热度高，则供应健康度随之降低。供应健康度的范围为-3 分~6 分，含义如下： 5 分~6 分：供应确定性很高。 1 分~4 分：供应确定性没有保障，资源预定可能创建失败。 -3 分~0 分：供应健康出现预警，建议您选择其他实例规格。您可以在该实例规格的 操作 列，单击 相似推荐 查看推荐信息。 配额：反映您可以购买该规格的实例的数量，建议根据配额合理设置预留数量，避免超出配额导致无法使用预留的资源创建实例。 | ecs.c7.large 、 ecs.g7.large |
| 预留数量 | 需要预留资源的数量。如果选择单个资源规格，单位为 台 ；如果选择多个资源规格，单位为 vCPU 。 | 10 vCPU |


- 

在预定资源方式区域，配置预定方式、生效时间等信息。

下方表格列出了不同预定方式的配置项，各预定方式对应的使用流程，请参见[弹性保障使用流程](products/ecs/documents/user-guide/overview-of-elasticity-assurance.md)、[立即生效容量预定使用流程](products/ecs/documents/user-guide/overview-of-immediate-capacity-reservation.md)、[指定时间生效容量预定使用流程](products/ecs/documents/user-guide/specify-a-time-effective-summary-of-capacity-reservation.md)。

表 1.弹性保障-立即生效/指定时间生效

- 

- 

| 配置项 | 说明 | 示例 |
| --- | --- | --- |
| 预定方式 | 选择 弹性保障-立即生效/指定时间生效 。 | 弹性保障-立即生效/指定时间生效 |
| 实例计费方式 | 不可选择，必须是 按量计费 ，弹性保障仅支持使用私有池容量保障交付按量付费实例。 | 按量计费 |
| 生效时间 | 弹性保障开始生效的时间，可选项如下： 立即生效 ：弹性保障创建成功后立即生效，预留资源以保障交付按量付费实例。 指定时间生效 ：弹性保障创建成功后，在指定的时间才生效，预留资源以保障交付按量付费实例。 | 立即生效 |
| 购买时长 | 支持 1 个月~5 年，具体可选时长以页面显示为准。 | 1 个月 |


表 2.容量预定-指定时间生效

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 配置项 | 说明 | 示例 |
| --- | --- | --- |
| 预定方式 | 选择 容量预定-指定时间生效 。 | 容量预定-指定时间生效 |
| 实例计费+付费方式 | 决定购买容量预定后可保障交付的资源类型，可选项如下： 按量计费+使用节省计划付费 ：即节省计划容量预定，用于保障交付按量付费实例。购买节省计划容量预定时会同步购买节省计划，用于抵扣按量付费实例的账单以优化成本。 包年包月 ：即包年包月容量预定，用于保障交付包年包月实例。购买包年包月容量预定时需要在提货期内使用私有池容量创建包年包月实例，超过提货期后不再预留资源。如果提货期内存在闲置容量，也需要遵循实例规格的按量付费标准计费。 | 按量计费+使用节省计划付费 |
| 如果选择 按量计费+使用节省计划付费 ，需要继续配置： 生效时间 购买时长 SP 类型 付费类型 | 生效时间 ：节省计划容量预定开始生效的时间，不能早于创建时间后 3 天或晚于创建时间后 1 年。 购买时长 ：支持 1 年 和 3 年 。 SP 类型 ：支持 通用型 和 ECS 计算型 。通用型支持跨产品使用，无地域和实例规格族限制；ECS 计算型仅适用于 ECS 实例，限制单个地域和特定的实例规格族，但折扣力度比通用型更大。 付费类型 ：目前仅支持 0 预付 。 更多节省计划的介绍，请参见 [什么是节省计划](products/ecs/documents/user-guide/what-is-savings-plan.md) 。 | 生效时间：2023-05-01 09:00 购买时长：1 年 SP 类型：ECS 计算型 付费类型：0 预付 |
| 如果选择 包年包月 ，需要继续配置： 生效时间 失效时间 | 生效时间 ：包年包月容量预定开始生效的时间，不能早于创建时间后 3 天或晚于创建时间后 1 年。 失效时间 ：自动计算，和生效时间的间隔为 7 天，您只能在此期间使用私有池容量创建包年包月实例。 | 生效时间：2023-05-01 09:00 失效时间：2023-05-08 09:00 |


表 3.容量预定-立即生效

- 

- 

| 配置项 | 说明 | 示例 |
| --- | --- | --- |
| 预定方式 | 选择 容量预定-立即生效 ，即立即生效容量预定。 | 容量预定-立即生效 |
| 实例计费方式 | 不可选择，必须是 按量计费 ，立即生效容量预定仅支持使用私有池容量保障交付按量付费实例。 | 按量计费 |
| 到期方式 | 立即生效容量预定通过以下方式释放： 手动释放 ：立即生效容量预定在购买成功后一直存在，直至您将其手动释放。 到期释放 ：您需要继续设置到期时间，立即生效容量预定在您设定的到期时间自动释放，使用期限最短支持 1 小时。 | 手动释放 |
| 操作系统 | 支持 Linux 和 Windows，仅保障交付使用相同操作系统的实例。如果您需要搭配地域级预留实例券优化成本，也请确保操作系统相同。 | linux |


- 

在私有资源池信息区域，配置构建私有池相关的信息。

下方表格列出了构建私有池时的配置项，私有池的完整构建和使用流程，请参见[资源管家概述](products/ecs/documents/user-guide/overview-29.md)。

- 

- 

- 

- 

- 

| 配置项 | 说明 | 示例 |
| --- | --- | --- |
| 私有资源池类型 | 支持 开放 和 专有 ，您可以根据业务类型规划资源，各准备一定量的开放和专有私有池，例如为关键业务准备专有私有池，为其他业务准备开放私有池。私有池的类型影响其使用方式： 开放私有池的使用方式较为灵活，您可以在创建实例时： 指定开放私有池的 ID。 如果开放私有池启用了标签匹配，选择使用开放私有池但不指定 ID，然后为实例绑定相同的标签，即可自动匹配使用该开放私有池。 如果开放私有池未启用标签匹配，选择使用开放私有池但不指定 ID，系统会自动选择一个无标签的开放私有池。 专有私有池的使用方式较为严格，您只能创建实例时指定专有私有池的 ID。 | 开放 |
| 私有资源池名称 | 私有池的名称，长度为 2~128 个英文或中文字符，必须以大小写字母或中文开头，不能以 http://或 https://开头。可以包含数字、半角句号（.）、半角冒号（:）、下划线（_）或短划线（-）。 | iCR-****-20211021 |
| 描述 | 私有池的描述信息，以便日后维护。长度为 2~256 个字符，不能以 http://或 https://开头。 | 为关键业务 A 保障交付实例。 |


- 

（可选）在标签（非必填）区域，配置标签相关的信息。

标签的常见应用场景包括批量运维、财务分账等，相关的概念和用法，请参见[标签](products/ecs/documents/user-guide/label-overview.md)。

在购买资源预定时绑定标签，还可以为开放私有池启用标签匹配，更精细地使用开放私有池。如果某个开放私有池启用了标签匹配，在创建实例选择使用开放私有池但不指定ID，然后为实例绑定相同的标签，即可自动匹配使用该开放私有池。

说明

资源预定生效后，始终以购买时绑定的标签匹配其私有池，因此建议避免编辑已有资源预定的标签。

- 

在资源规格推荐区域，按需选择资源方案。

除原方案外，阿里云还会从库存优先、多可用区容灾、性能优先等维度给出更多推荐方案，最终以您选择的方案预留资源。

如果未显示方案或者方案不能满足需求，请单击提交需求单进行资源预定。

说明

仅包年包月容量预定支持提交需求单，如您看不到提交需求单入口，请联系您的商务经理进行开通。

- 

单击下一步：确认信息。

- 

在信息确认页面，确认资源预定的相关信息。

- 

在资源预定总览区域，确认资源预定的属性。

包括预留资源的台数、实例的计费方式、私有池类型等信息。

- 

在资源方案区域，确认方案对应资源的详情。

包括预留资源的实例规格名称、可用区、参考价格、规格指标等信息。

说明

一份资源预定仅适用于单实例规格和单可用区。如果您选择的方案中包括了多个实例规格或多个可用区，会自动拆分为多份资源预定。

- 

在预定须知区域，阅读提示信息。如无问题，选中我已确认，然后单击创建预定单。

- 

在完成页面，当资源预定的状态为预定生效中时，说明已购买成功。

## 后续步骤

返回资源预定页签，在资源预定的状态进入预定生效中后，您就可以使用私有池容量保障交付实例。具体操作，请参见[使用私有池容量创建实例](products/ecs/documents/user-guide/use-a-private-pool-to-create-instances.md)。以购买立即生效容量预定为例，显示效果如下图所示。

## 相关文档

- 

您可以调用API[CreateElasticityAssurance](products/ecs/documents/developer-reference/api-ecs-2014-05-26-createelasticityassurance.md)接口创建弹性保障服务。

- 

您可以调用API[PurchaseElasticityAssurance](products/ecs/documents/developer-reference/api-ecs-2014-05-26-purchaseelasticityassurance.md)接口购买一个准备完毕且处于未激活状态的弹性保障服务。

- 

您可以调用API[CreateCapacityReservation](products/ecs/documents/developer-reference/api-ecs-2014-05-26-createcapacityreservation.md)接口创建容量预定服务。

- 

您可以调用API[RenewElasticityAssurances](products/ecs/documents/developer-reference/api-ecs-2014-05-26-renewelasticityassurances.md)接口对一个或多个已购买的弹性保障服务进行续费。

[上一篇：指定时间生效容量预定概述](products/ecs/documents/user-guide/specify-a-time-effective-summary-of-capacity-reservation.md)[下一篇：查看和修改弹性保障](products/ecs/documents/user-guide/view-and-modify-an-elasticity-assurance.md)

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
