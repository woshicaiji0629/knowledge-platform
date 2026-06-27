# 块存储计费项计费方式与规则-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/block-storage-devices

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

# 块存储计费

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍块存储的计费，包括云盘、本地盘和弹性临时盘的购买与定价、计费规则、云盘变配后的计费说明、计费示例等。

## 购买与定价

块存储分为云盘（包括ESSD系列云盘、上一代云盘）、本地盘和弹性临时盘。

- 

本地盘不支持单独购买（与特定实例规格绑定），费用已计入实例规格费用。

- 

云盘

云盘购买入口：[前往云盘购买页](https://ecs-buy.aliyun.com/disk/#/cloudDisk)。 定价：同一类型的云盘在不同地域的价格均可能不同，具体请参见[块存储价格](https://www.aliyun.com/price/product#/disk/detail)。

- 

弹性临时盘

弹性临时盘购买入口：[前往弹性临时盘购买页](https://ecs-buy.aliyun.com/diskNext#/elasticEphemeralDisk/cn-hangzhou)定价：同一类型的弹性临时盘在不同地域的价格均可能不同，具体请参见[块存储价格](https://www.aliyun.com/price/product#/disk/detail)。

说明

块存储的相关介绍，您可参见[块存储介绍](products/ecs/documents/user-guide/block-storage-overview.md)。

## 云盘计费

### 计费规则

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 计费项 | 涉及云盘类型 | 计费规则 | 计费方式 |
| --- | --- | --- | --- |
| 云盘容量费用 | 所有云盘 | 云盘创建成功后开始计费，与是否挂载使用或云盘用途无关。 | [包年包月](products/ecs/documents/subscription.md) ：云盘容量（GiB） × 云盘单价 × 购买时长 说明 如果实际使用时长小于购买时长，您可以申请退订云盘。更多信息，请参见 [退订说明](products/ecs/documents/refund-instructions.md) 。 [按量付费](products/ecs/documents/pay-as-you-go-1.md) ：云盘容量（GiB） × 云盘单价 × 计费时长 [存储容量单位包](products/ecs/documents/storage-capacity-units-1.md) [SCU](products/ecs/documents/storage-capacity-units-1.md) ：支持按抵扣系数抵扣云盘容量的按量付费账单，超出部分按量付费，抵扣示例请参见 [存储容量单位包](products/ecs/documents/storage-capacity-units-1.md) [SCU](products/ecs/documents/storage-capacity-units-1.md) |
| 预配置性能费用 | 仅 ESSD AutoPL 云盘 、ESSD PL-X 云盘 | 针对 ESSD AutoPL 云盘 、ESSD PL-X 云盘 ，如果开启了预配置性能（配置 IOPS），还会收取预配置性能费。 按秒计费，每整点小时按资源用量计算一次费用。计算完成后会生成一条消费明细（可能存在延迟）。 说明 如果预配置 IOPS 的费用计算结果小于 0.001 元，则控制台配置费用显示为 0 元/小时，最终付费请您以实际账单为准。 | [按量付费](products/ecs/documents/pay-as-you-go-1.md) ：预配置性能单价 × 预配置 IOPS × 计费时长 |
| 性能突发费用 | 仅 ESSD AutoPL 云盘 | 针对 ESSD AutoPL 云盘，如果开启了性能突发（默认开启），在使用 ESSD AutoPL 云盘过程中发生了性能突发，还会收取突发性能费用，按小时计费，每整点小时按资源用量计算一次费用，计算完成后会生成一条消费明细（可能存在延迟）。 突发 IO 总量 按小时统计 ，折算规则为： 说明 突发性能=总性能-（基准性能+预配置性能），下文的突发 IOPS/吞吐量指的是超出基准性能和预配置性能之和的 IOPS/吞吐量。 如果仅 IOPS 突发，吞吐量未突发：突发 IO 量=∑ 突发 IOPS × 突发持续时间 。 示例：仅 IOPS 突发 5s。第 1-2s 的突发 IOPS 为 10,000 IO/s，第 3-5s 的突发 IOPS 为 8,000 IO/s，则突发 IO 量=10,000 IO/s × 2s+8,000 IO/s × 3s=44,000 IO，最终向上万取值 50,000 IO 来计费。 如果仅吞吐量突发，IOPS 未突发：突发 IO 量=∑ 突发的吞吐量/16 KB × 突发持续时间 。 示例：仅吞吐量突发 2s，2s 内突发吞吐量均为 1 GB/s，按 IO 折算后是（1 × 1024 × 1024 KB/s）/16 KB × 2s=131,072 IO，最终向上万取值 140,000 IO 来计费。 如果 IOPS 和吞吐量均突发，以突发 IO 量更大的计费。 示例：IOPS 和吞吐量均突发 2s，2s 内突发 IOPS 均为 8,000 IO/s（突发 IO 量=8,000 IO/s × 2s=16,000 IO），2s 内突发吞吐量均为 1 GB/s（突发 IO 量=（1 × 1024 × 1024 KB/s）/16 KB × 2s =131,072 IO），最终向上万取值 140,000 IO 来计费。 | [按量付费](products/ecs/documents/pay-as-you-go-1.md) ： 每小时突发 IO 总量小于等于 10 万：享受 10 万 IO 免费额度，不收取性能突发费用。 每小时突发 IO 总量大于 10 万：采用费用封顶规则，确保在享受高性能的同时，无需担心费用超支的风险。详情请参见 [性能突发费用封顶规则](products/ecs/documents/user-guide/essd-autopl-disks.md) 。 |


### 计费方式说明

通过不同方式创建的云盘，支持的计费方式不同：

- 

创建ECS实例时创建并挂载云盘：计费方式和ECS实例相同，支持包年包月和按量付费。

- 

为已有ECS实例创建并挂载云盘：

- 

包年包月ECS实例：支持挂载包年包月和按量付费的云盘。

- 

按量付费ECS实例：仅支持挂载按量付费的云盘。

- 

单独创建云盘且不挂载到ECS实例：仅支持按量付费的云盘。

### 转换云盘计费方式

如果云盘当前的计费方式不满足您的需求，您可以转换计费方式。具体操作，请参见[转换云盘计费方式](products/ecs/documents/switch-the-billing-method-of-a-disk.md)。

### 云盘变配后计费说明

云盘在变配过程中也可能会产生费用，具体说明如下表所示。

| 变配操作 | 计费说明 | 参考文档 |
| --- | --- | --- |
| 扩容云盘 | 扩容后会收取新增的容量部分费用。 说明 扩容时，不支持修改云盘计费方式。 | [云盘扩容指引](products/ecs/documents/user-guide/overview-19.md) |
| 变更云盘类型 | 云盘变配后，根据新的云盘类型计费。 | [变更云盘类型](products/ecs/documents/user-guide/change-the-category-of-a-disk.md) |
| 修改 ESSD 云盘性能级别 | 升级 ESSD 云盘性能级别后，系统会按照新性能级别来计费。 | [修改](products/ecs/documents/user-guide/modify-the-performance-levels-of-essds.md) [ESSD](products/ecs/documents/user-guide/modify-the-performance-levels-of-essds.md) [云盘性能级别](products/ecs/documents/user-guide/modify-the-performance-levels-of-essds.md) |
| 修改 ESSD AutoPL 云盘性能配置 | 开启预配置性能和性能突发或者修改预配置 IOPS，系统会按照新性能级别来计费。 | [修改](products/ecs/documents/user-guide/modify-the-performance-configurations-of-an-essd-autopl-disk.md) [ESSD AutoPL](products/ecs/documents/user-guide/modify-the-performance-configurations-of-an-essd-autopl-disk.md) [云盘性能配置](products/ecs/documents/user-guide/modify-the-performance-configurations-of-an-essd-autopl-disk.md) |


## 本地盘计费

指与特定实例规格绑定的本地盘，不支持单独购买，费用已计入实例规格费用。有关本地盘的更多信息，请参见[本地盘](products/ecs/documents/user-guide/local-disks.md)。

## 弹性临时盘计费

### 计费规则

弹性临时盘创建成功后按容量开始计费。

- 

[包年包月](products/ecs/documents/subscription.md)：弹性临时盘（GiB） × 弹性临时盘单价 × 购买时长

- 

[按量付费](products/ecs/documents/pay-as-you-go-1.md)：弹性临时盘容量（GiB） × 弹性临时盘单价 × 计费时长

### 计费方式说明

通过不同方式创建的弹性临时盘，支持的计费方式不同：

- 

创建ECS实例时创建并挂载弹性临时盘：计费方式和ECS实例相同，支持包年包月和按量付费。

- 

为已有ECS实例创建并挂载弹性临时盘：

- 

包年包月ECS实例：支持挂载包年包月和按量付费的弹性临时盘。

- 

按量付费ECS实例：仅支持挂载按量付费的弹性临时盘。

- 

单独创建弹性临时盘且不挂载到ECS实例：仅支持按量付费的弹性临时盘。

## 计费示例

### 示例一：ESSD云盘

假设在华东1（杭州）地域，创建实例时购买了2块云盘（1块系统盘和1块数据盘），规格如下：

- 

系统盘：ESSD PL0云盘，容量为50 GiB。

- 

数据盘：ESSD PL1云盘，容量为100 GiB。

则云盘的收费情况如下表所示。

说明

示例仅用作说明价格计算规则，实际和定价费用以账单显示为准。

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

| 计费方式 | 计费条件 | 费用（元） |
| --- | --- | --- |
| 包年包月 | 系统盘：ESSD PL0 云盘单价为 0.50 元/1 GiB/月 数据盘：ESSD PL1 云盘单价为 1.00 元/1 GiB/月 购买时长：1 个月 | 系统盘费用=云盘单价*云盘容量*购买时长=0.5 * 50 * 1 = 25.00 数据盘费用=云盘单价*云盘容量*购买时长=1 * 100 * 1 = 100.00 总费用：25 + 100 = 125.00 |
| 按量付费 | 系统盘：ESSD PL0 云盘单价 0.00105 元/1 GiB/小时 数据盘：ESSD PL1 云盘单价 0.00210 元/1 GiB/小时 计费时长：24 小时 | 系统盘费用=云盘单价*云盘容量*计费时长=0.00105 * 50 * 24 = 1.26 数据盘费用=云盘单价*云盘容量*计费时长=0.00210 * 100 * 24 = 5.04 总费用：1.26 + 5.04 = 6.30 |


### 示例二：ESSD AutoPL云盘

ESSD AutoPL云盘的计费示例请参见[ESSD AutoPL](products/ecs/documents/user-guide/essd-autopl-disks.md)[云盘计费示例](products/ecs/documents/user-guide/essd-autopl-disks.md)。

[上一篇：镜像计费](products/ecs/documents/images.md)[下一篇：公网带宽计费](products/ecs/documents/public-bandwidth.md)

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
