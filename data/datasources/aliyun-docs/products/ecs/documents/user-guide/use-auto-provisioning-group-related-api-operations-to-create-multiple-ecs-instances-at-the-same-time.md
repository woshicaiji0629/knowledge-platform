# 使用CreateAutoProvisioningGroup API在按量付费场景下批量创建ECS实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/use-auto-provisioning-group-related-api-operations-to-create-multiple-ecs-instances-at-the-same-time

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

# 使用弹性供应组API批量创建ECS实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在需要大量创建按量付费实例的情况下，您可以通过调用API接口完成创建操作更为高效。本文主要介绍如何通过编写调用CreateAutoProvisioningGroup API接口的Java代码批量创建ECS按量付费实例，以及对比RunInstances和CreateAutoProvisioningGroup接口的功能、优劣势。

## 背景信息

在业务需要使用按量付费ECS实例的场景下，RunInstances是使用最频繁的API。RunInstances拥有一次调用能够最多创建100台ECS实例的能力，但是在实际的生产环境中，如果需要超过100台的大批量创建ECS实例场景，直接使用RunInstances会存在一定的技术瓶颈。更多信息，请参见[RunInstances](products/ecs/documents/user-guide/use-auto-provisioning-group-related-api-operations-to-create-multiple-ecs-instances-at-the-same-time.md)[创建实例时存在的问题](products/ecs/documents/user-guide/use-auto-provisioning-group-related-api-operations-to-create-multiple-ecs-instances-at-the-same-time.md)。

说明

如果您已了解RunInstances批量创建实例过程中存在的技术瓶颈，可以跳过该章节。

为了解决大批量创建ECS实例的需求场景，阿里云提供了弹性供应组，您可以通过CreateAutoProvisioningGroup创建弹性供应组，一键式地部署跨计费方式、跨可用区、跨实例规格族的实例集群。相较于RunInstances，CreateAutoProvisioningGroup更适合大批量创建ECS实例的业务场景。两者的功能对比与优势分析，请参见[RunInstances](products/ecs/documents/user-guide/use-auto-provisioning-group-related-api-operations-to-create-multiple-ecs-instances-at-the-same-time.md)[与](products/ecs/documents/user-guide/use-auto-provisioning-group-related-api-operations-to-create-multiple-ecs-instances-at-the-same-time.md)[CreateAutoProvisioningGroup](products/ecs/documents/user-guide/use-auto-provisioning-group-related-api-operations-to-create-multiple-ecs-instances-at-the-same-time.md)[功能对比](products/ecs/documents/user-guide/use-auto-provisioning-group-related-api-operations-to-create-multiple-ecs-instances-at-the-same-time.md)以及[弹性供应组的优势](products/ecs/documents/user-guide/use-auto-provisioning-group-related-api-operations-to-create-multiple-ecs-instances-at-the-same-time.md)。

## RunInstances与CreateAutoProvisioningGroup功能对比

本章节对比[RunInstances](products/ecs/documents/api-runinstances.md)与[CreateAutoProvisioningGroup](products/ecs/documents/api-createautoprovisioninggroup.md)两接口的部分功能，使您可以快速了解两者的差异，选择合适的创建实例方式。

- 

- 

- 

- 

- 

- 

- 

| 对比项 | RunInstances | CreateAutoProvisioningGroup |
| --- | --- | --- |
| 单次批量创建实例的数量上限 | 100 台 | 1000 台（vCPU 上限为 10000） |
| 容量交付方式 | 实例数量 | 实例数量、vCPU 核数、实例规格的权重等 |
| 是否支持多可用区 | 否 | 是 |
| 是否支持多个实例规格 | 否 | 是 |
| 是否支持多种磁盘规格 | 否 | 是 |
| 是否提供了创建实例的策略 | 否 | 是。提供了如下策略： 按量付费实例 成本优化策略：从备选实例规格中选取成本最低的实例规格，创建实例。 优先级策略：按照备选实例规格设置的优先级，依次尝试创建实例。 抢占式实例 成本优化策略：从备选实例规格中选取成本最低的实例规格，创建实例。 可用区均衡分布策略：在备选的可用区之间，数量均匀地创建实例。 容量优化分布策略：根据抢占式实例的库存情况，选择最优的实例规格及可用区进行创建实例。 |
| 交付稳定性 | 受资源库存影响较大 | 多可用区、多实例规格的配置组合有效降低了资源库存造成的影响 |
| API 响应格式 | 同步返回创建结果 | 同步返回创建结果 |


创建实例的方式由RunInstances更换为CreateAutoProvisioningGroup的部分示例场景：

- 

如果您之前使用RunInstances在单可用区、单实例规格的配置下批量创建实例，更换为CreateAutoProvisioningGroup后，您只需配置一组实例规格与可用区的组合，即可实现批量创建实例。

- 

如果您之前使用RunInstances时手动设置了业务部署方案，更换为CreateAutoProvisioningGroup后，将由系统为您提供一键式的多可用区、多实例规格、多磁盘配置的部署能力，并且系统提供了多种创建实例的策略供您选择。

例如：您之前手动设置了遍历多个实例规格及可用区的方案进行RunInstances调用，以提高实例创建的成功率。更换为CreateAutoProvisioningGroup后，您只需要通过参数配置多个实例规格及可用区的组合，选择合适的创建策略，系统将自动完成批量创建实例的操作。

重要

弹性供应组的创建策略存在使用限制，单次最大可创建1000台实例，如果指定了实例规格的权重（WeightedCapacity），则单次创建的最大加权容量为10000。

## RunInstances创建实例时存在的问题

基于RunInstances功能的限制，您在大批量创建实例时，可能遇到下表所示的问题。

- 

- 

- 

- 

- 

- 

- 

- 

| 问题 | 说明 | 解决方案 |
| --- | --- | --- |
| 批量创建的能力有限 | 调用一次 RunInstances 最多可以创建 100 台 ECS 实例。 | 当您需要创建大于 100 台 ECS 实例时，需要通过循环或并发的方式多次调用该接口，以完成业务需求。 |
| 批量创建的稳定性不足 | 调用 RunInstances 只支持设置单可用区、单实例规格。因此，在批量创建 ECS 实例的过程中，可能会出现实例规格的库存不足、停止售卖或使用限制等问题。引发以下情况： 在某一时间段，实例规格的库存不足导致批量创建失败。 在某一时间段，实例规格停止售卖导致无法再创建指定的实例规格。 指定的实例规格只在部分可用区出售。 指定的实例规格只能搭配指定的磁盘类型。 | 库存问题是导致批量创建 ECS 实例失败的主要原因。因此阿里云会推荐您在批量创建 ECS 实例之前，先调用 [DescribeAvailableResource](products/ecs/documents/api-describeavailableresource.md) 查询实例规格与可用区下资源的库存情况，手动确认多个库存充足的可用区与实例规格的组合后，再批量创建 ECS 实例。通过复杂的创建方式，换来了较高的业务交付稳定性。 示例场景：当您确认多个库存充足的可用区与实例规格的组合后，您还需要构建合适的创建 ECS 实例的策略。例如，您可以根据手动确认的多个组合顺序，依次创建 100 台 ECS 实例，如果第一个组合的资源库存只支持创建 50 台 ECS 实例，那么您需要使用第二个组合尝试创建其余 50 台 ECS 实例。 实例规格存在使用限制。您可以通过 [DescribeAvailableResource](products/ecs/documents/api-describeavailableresource.md) 查询限制，并自行建立容错方案，避免因使用限制变更带来的影响。 说明 您也可以根据文档提供的实例规格特点确定相关限制。更多信息，请参见 [实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md) 。 示例场景： ecs.g6e.large 实例规格只支持 ESSD 云盘类型、 cn-beijing-x 可用区下不支持选择 ESSD 云盘类型等。 |
| 创建策略过于单一 | RunInstances 仅支持设置单可用区、单实例规格。如果您的业务需要多可用区部署实现异地容灾，或者需要按照最低成本创建 ECS 实例，则需要您自行构建业务部署方案，以保障实例的成功部署。自行构建的业务部署方案存在以下问题： 开发成本高。自行构建的业务部署方案需要处理一系列的问题。例如，库存不足时如何顺利的创建 ECS 实例、扩容服务器时如何在获取抢占式实例最低成本的同时保证计算能力等 稳定性与专业性不足。对于阿里云提供的资源，您难以用专业的方式自行构建业务部署方案，并无法对方案进行测试，进而将对生产环境造成一定的风险。 | 自行解决或联系阿里云提供帮助。 |


## 弹性供应组的优势

针对RunInstances批量创建ECS实例存在的问题，阿里云提供了弹性供应组，解决了大批量创建ECS实例的场景下存在的问题。弹性供应组支持一键部署跨计费方式、跨可用区、跨实例规格族的实例集群。您可以通过弹性供应组稳定提供计算力，缓解抢占式实例的回收机制带来的不稳定因素，免去重复手动创建实例的繁琐操作。本章节主要介绍弹性供应组的优势。

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

| 优势 | 说明 |
| --- | --- |
| 批量创建 ECS 实例的数量上限更高 | 弹性供应组支持单次创建最多 1000 台 ECS 实例。 |
| 支持设置多可用区、多实例规格、多种磁盘类型 | 弹性供应组支持您配置最多 10 种实例规格或可用区的组合、最多 5 种磁盘类型的选择，帮助您实现高可用的批量创建 ECS 实例。 示例场景： 当您通过弹性供应组提供的均衡可用区分布策略创建 ECS 实例时，可以配置多个可用区和多个实例规格。按照策略的要求，多个可用区下，创建实例的数量应相对平均，但如果其中某个可用区无法完成创建，弹性供应组会尝试将该可用区待创建的实例数量，转移到其他可用区进行创建。 如果您指定了多种磁盘规格，弹性供应组将按照指定顺序作为各磁盘类型的优先级顺序，当某一种磁盘不可用时，自动更换磁盘类型。 说明 当所有磁盘类型都不可用时，系统将会自动更换其它创建方式，不再尝试该种创建方式。 |
| 支持多种创建实例的策略 | 针对按量付费实例和抢占式实例，分别提供了以下创建策略： 按量付费实例 成本优化策略：从备选实例规格中选取成本最低的实例规格，创建实例。 优先级策略：按照备选实例规格设置的优先级，依次尝试创建实例。 抢占式实例 成本优化策略：从备选实例规格中选取成本最低的实例规格，创建实例。 可用区均衡分布策略：在备选的可用区之间，均匀数量地创建实例。 容量优化分布策略：根据抢占式实例的库存情况，选择最优的实例规格及可用区进行创建实例。 |
| 可提高抢占式实例的可用性 | 抢占式实例因其价格优势使用量越来越高，但是其价格的不稳定性与系统回收的特性，造成管理抢占式实例存在一定的难度。您可以通过弹性供应组，实现在低成本的前提下，提高抢占式实例的可用性。具体方式如下： 创建策略选择默认的成本优化策略，每次的扩容策略将按照实例规格价格从低到高的顺序尝试创建。 抢占式实例对应的不同实例规格与可用区的资源库存情况互相隔离。多个实例规格与多个可用区的配置组合，可以有效降低所有组合都无库存的概率。 创建弹性供应组时，配置多种备选的磁盘类型，保证创建实例的过程中，系统能够自动选取合适的磁盘类型。 配置 SpotInstancePoolsToUseCount 参数，指定抢占式实例在多个最低价格的实例规格及可用区的组合中创建。避免某一种实例规格对应的实例回收，造成计算能力产生雪崩效应。 |


## CreateAutoProvisioningGroup最佳实践

本章节提供CreateAutoProvisioningGroup接口对应的Java代码示例，使您快速了解该接口的使用方式。

- 

安装ECS Java SDK以及阿里云核心库。

具体操作，请参见[SDK](products/ecs/documents/developer-reference/ecs-v2-0-sdk-overview.md)[概览](products/ecs/documents/developer-reference/ecs-v2-0-sdk-overview.md)。

- 

编写调用CreateAutoProvisioningGroup接口的Java代码。

代码示例如下：

import com.aliyun.ecs20140526.Client; import com.aliyun.ecs20140526.models.CreateAutoProvisioningGroupRequest; import com.aliyun.ecs20140526.models.CreateAutoProvisioningGroupResponse; import com.aliyun.teaopenapi.models.Config; import com.aliyun.teautil.models.RuntimeOptions; import com.google.gson.Gson; public class Test { public static void main(String[] args_) throws Exception { Config config = new Config() .setAccessKeyId(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")) .setAccessKeySecret(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")) .setEndpoint("ecs.cn-heyuan.aliyuncs.com"); Client client = new Client(config); CreateAutoProvisioningGroupRequest.CreateAutoProvisioningGroupRequestLaunchTemplateConfig launchTemplateConfig = new CreateAutoProvisioningGroupRequest.CreateAutoProvisioningGroupRequestLaunchTemplateConfig() .setVSwitchId("vsw-f8zadqudz*********") .setInstanceType("ecs.s6-c1m1.small") .setWeightedCapacity(1.0); CreateAutoProvisioningGroupRequest.CreateAutoProvisioningGroupRequestLaunchConfiguration launchConfiguration = new CreateAutoProvisioningGroupRequest.CreateAutoProvisioningGroupRequestLaunchConfiguration() .setSecurityGroupId("sg-f8zf6vg51*********") .setImageId("aliyun_3_x64_20G_alibase_20250629.vhd") .setSystemDiskCategory("cloud_ssd") .setSystemDiskSize(40); CreateAutoProvisioningGroupRequest createAutoProvisioningGroupRequest = new CreateAutoProvisioningGroupRequest() .setAutoProvisioningGroupType("instant") .setRegionId("cn-heyuan") // 设置抢占式实例的创建策略 .setSpotAllocationStrategy("lowest-price") // 设置按量付费实例的创建策略 .setPayAsYouGoAllocationStrategy("prioritized") .setTotalTargetCapacity("5") .setPayAsYouGoTargetCapacity("3") .setSpotTargetCapacity("2") .setLaunchConfiguration(launchConfiguration) .setLaunchTemplateConfig(java.util.Arrays.asList( launchTemplateConfig )) .setClientToken("0c593ea1-3bea******************"); RuntimeOptions runtime = new RuntimeOptions(); CreateAutoProvisioningGroupResponse response = client.createAutoProvisioningGroupWithOptions(createAutoProvisioningGroupRequest, runtime); System.out.println(new Gson().toJson(response.getBody())); } }

JSON返回值示例如下：

{ "autoProvisioningGroupId": "apg-**************", "launchResults": { "launchResult": [ { "amount": 0, "errorCode": "NoInstanceStock", "errorMsg": "The instanceTypes are out of usage", "instanceType": "ecs.s6-c1m1.small", "spotStrategy": "NoSpot", "zoneId": "cn-heyuan-b" }, { "amount": 2, "instanceIds": { "instanceId": [ "i-f8z8**************icn5", "i-f8z8**************icn6" ] }, "instanceType": "ecs.s6-c1m1.small", "spotStrategy": "SpotAsPriceGo", "zoneId": "cn-heyuan-b" } ] }, "requestId": "CDA21119-7CFD-5B40-A2D0-******8" }

通过CreateAutoProvisioningGroup创建弹性供应组时，您只需要设置批量创建实例的相关配置项，无需关心创建过程，弹性供应组将以尽力交付的方式，完成创建。

说明

尽力交付的方式是指，当您配置的某些资源组合无法创建实例时，将自动切换到其他可用的资源组合继续进行创建。该方式创建实例需要一定的时间，并且可能导致实际创建结果与创建策略存在一定的偏差。

## 相关文档

- 

弹性供应是一种快速交付ECS实例集群的方案，简单配置后即可自动批量创建ECS实例。更多信息，请参见[弹性供应概述](products/ecs/documents/user-guide/overview-46.md)。

- 

有关更多弹性供应组示例信息，请参见[弹性供应组配置示例](products/ecs/documents/user-guide/configure-an-auto-provisioning-group.md)。

[上一篇：使用实例启动模板创建实例](products/ecs/documents/user-guide/create-an-instance-by-using-a-launch-template.md)[下一篇：抢占式实例](products/ecs/documents/user-guide/preemptible-instances.md)

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
