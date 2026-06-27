# 计费规则定价与成本管理-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/billing-overview

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

# 计费概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

通过阅读本文，您可以快速了解云服务器ECS的计费项及其计费方式、计费组成、定价等主要计费信息。

## 计费项及其计费方式

一台ECS实例包括计算资源（vCPU和内存）、镜像、块存储等资源，其中涉及计费的ECS资源如下表所示。

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

| 资源类型 | 计费说明 | 计费方式 | 计费规则 |
| --- | --- | --- | --- |
| 计算资源（vCPU 和内存） | 以实例规格的形式提供计算资源，包括 vCPU 和内存，收取实例规格费用。 重要 计算资源为基础配置费用，按量付费的 ECS 实例，即使未运行业务，也会按照计费周期持续计费。除非开启节省停机模式。更多信息，请参见 [节省停机模式](products/ecs/documents/user-guide/economical-mode.md) 。 | 包年包月 按量付费 抢占式实例 按量付费+预留实例券 按量付费+节省计划 | [实例规格（计算资源）计费](products/ecs/documents/instance-types.md) |
| 镜像 | 根据镜像类型以及使用情况决定是否收费。 | 包年包月 按量付费 按量付费+预留实例券（公共镜像） 说明 镜像只能和 ECS 实例搭配使用，Windows 类型的预留实例券在购买时包含了公共镜像费用，可以抵扣公共镜像的账单。 | [镜像计费](products/ecs/documents/images.md) |
| 块存储 | 按云盘容量和使用时长收取费用。 说明 本地盘与特定实例规格绑定，不支持单独购买，费用已计入实例规格费用。 | 包年包月 按量付费 存储容量单位包 SCU 按量付费+节省计划 | [块存储计费](products/ecs/documents/block-storage-devices.md) |
| 公网带宽 | 使用固定公网 IP 访问公网时，仅收取公网出网带宽费用。 说明 如果使用弹性公网 IP（EIP）或 NAT 网关访问公网，计费相关详情参见 [EIP](products/eip/documents/billing-overview.md) [计费概述](products/eip/documents/billing-overview.md) 或 [NAT](products/nat-gateway/documents/nat-gateway-billing.md) [网关计费说明](products/nat-gateway/documents/nat-gateway-billing.md) 。 | 按固定带宽 按使用流量 | [公网带宽计费](products/ecs/documents/public-bandwidth.md) |
| 快照 | 创建快照：根据快照容量收取快照存储费（分地域计费） 复制快照：快照存储费用+复制流量费用 | 按量付费 存储容量单位包 SCU 标准（LRS）存储包 | [快照计费](products/ecs/documents/snapshots-1.md) |


说明

ECS资源的基础计费方式为包年包月和按量付费，针对不同的ECS资源，您可以根据需要结合其他优惠的计费方式来降低使用成本。更多信息请参见[计费方式概述](products/ecs/documents/overview-of-billing-methods.md)。

## 计费组成

ECS的计费项组成如下图：

## 产品定价

不同地域的实例价格请参见[云服务器](https://www.aliyun.com/price/product#/ecs/detail)[ECS](https://www.aliyun.com/price/product#/ecs/detail)[定价](https://www.aliyun.com/price/product#/ecs/detail)中的实例价格页签。

## 转换计费方式

在购买ECS资源后，如果发现当前计费方式无法满足业务需求，您可以转换计费方式。支持转换的ECS资源如下表所示。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| ECS 资源 | 转换说明 | 相关文档 |
| --- | --- | --- |
| 实例 | 转换实例计费方式会同时转换计算资源（vCPU 和内存）、系统盘等资源的计费方式。 将实例的计费方式从包年包月转为按量付费，可以回收部分成本，更加灵活地使用 ECS。 说明 阿里云会根据您的云服务器使用情况，通过计算动态得出您的实例的计费方式是否支持转换操作。您可以前往云服务器控制台查看是否存在相应的操作入口，如果不存在，则说明不支持。 将实例的计费方式从按量付费转为包年包月，可以享受一定程度的价格优惠。 | [包年包月转按量付费](products/ecs/documents/change-the-billing-method-of-an-instance-from-subscription-to-pay-as-you-go-1.md) [按量付费转包年包月](products/ecs/documents/change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md) |
| 云盘 | 包年包月实例上挂载的数据盘可以单独转换计费方式。 实例系统盘以及按量付费实例上挂载的数据盘需随实例一起转换计费方式。 | [转换云盘计费方式](products/ecs/documents/switch-the-billing-method-of-a-disk.md) [包年包月转按量付费](products/ecs/documents/change-the-billing-method-of-an-instance-from-subscription-to-pay-as-you-go-1.md) [按量付费转包年包月](products/ecs/documents/change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md) |
| 公网带宽 | 使用固定公网 IP 的实例，可以通过升降配功能转换带宽的计费方式。 | [转换固定公网](products/ecs/documents/change-the-billing-method-for-network-usage-1.md) [IP](products/ecs/documents/change-the-billing-method-for-network-usage-1.md) [的带宽计费方式](products/ecs/documents/change-the-billing-method-for-network-usage-1.md) |


## 查看费用账单

您可以在费用与成本中查看ECS实例相关的费用账单和消费明细，以了解消费情况。具体操作，请参见[账单查询](products/ecs/documents/view-billing-details.md)。

## 续费实例

包年包月实例到期后会影响实例正常运行。如果您想继续使用实例，需要在指定时间内为实例续费，否则vCPU、内存、云盘等资源会自动释放，数据将会丢失。续费相关的更多信息，请参见[如何续费包年包月实例](products/ecs/documents/manually-renew-an-instance-1.md)。

## 欠费说明

账号的可用额度（含阿里云账户余额和代金券）小于待结算的账单，即被判定为账号欠费。欠费后，可能会影响实例正常运行，请及时充值。

- 

包年包月ECS资源：对于包年包月ECS资源，您已经预先支付了资源费用，因此账号欠费后，您可以正常使用已有的包年包月ECS资源。但对于新购实例、升级实例配置、续费订单等涉及费用的操作，您无法正常进行。

- 

按量付费ECS资源：账号欠费会导致按量付费ECS实例停机，欠费停机期间相关ECS资源暂停计费。如果未在规定时间内充值结清欠费账单并重开机，您将不能正常使用ECS资源。

## 支付与退款

购买ECS资源时，您可以选择以下支付方式：

- 

阿里云账户余额

- 

在线支付

通过API[CreateInstance](products/ecs/documents/api-createinstance.md)创建包年包月实例时，不能使用信用卡支付。

- 

优惠券

优惠券的使用方式与规则请参见[查看并使用优惠券](https://help.aliyun.com/zh/user-center/documentation-about-vouchers#title-agu-sxg-kx8)。

说明

优惠券用于在出账前抵扣消费金额，因此并不涉及实际支付动作。

购买使用ECS资源后，您可以查看账单和消费情况，具体请参见[账单查询](products/ecs/documents/view-billing-details.md)。

如果您想要退订产品，请先了解相关退款规则，具体请参见[退订说明](products/ecs/documents/refund-instructions.md)。

## 成本优化最佳实践

使用云服务器ECS时，成本主要包括拥有成本和运维成本。您可以从归集成本、优化资源、升级换代、具备节约意识、实现自动化运维等方面优化成本。更多详情，请参见[成本优化最佳实践](products/ecs/documents/best-practices-for-cost-optimization.md)。

## 计费常见问题

如果您在购买或使用云服务器ECS过程中遇到某些计费相关问题，请参见[计费](products/ecs/documents/billing-faq.md)[FAQ](products/ecs/documents/billing-faq.md)获取帮助。

[上一篇：了解计费](products/ecs/documents/understanding-billing.md)[下一篇：计费项](products/ecs/documents/billable-items.md)

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
