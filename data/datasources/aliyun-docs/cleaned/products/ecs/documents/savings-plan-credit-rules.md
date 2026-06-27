# 节省计划抵扣按量付费的规则、范围与优先级-云服务器 ECS-阿里云-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/savings-plan-credit-rules

# 节省计划抵扣项及抵扣规则
节省计划作为您购买的一种折扣权益，购买后不会直接为您提供对应的资源，需要搭配您购买的按量付费资源使用。若您在购买后暂时没有满足条件可以抵扣的按量付费资源，节省计划仍按照您的每小时承诺消费金额持续计费。了解节省计划的抵扣规则可以帮助您更好的利用折扣权益，降低运营成本。本章节将为您介绍节省计划的抵扣规则、抵扣项以及相关抵扣示例。
## 节省计划抵扣规则
您无需手动使用节省计划抵扣按量付费实例。
购买节省计划后，在有效期内节省计划将自动匹配满足条件的按量付费的抵扣项。匹配成功后，节省计划会以每小时维度按照出账时间的先后顺序，对抵扣项按照折扣后单价去抵扣实例的相关费用。
抵扣上限为您设置的每小时承诺消费金额，超出承诺消费金额的部分将按照该计费项原有的按量付费价格进行收费。直至节省计划失效。
若您本小时所有支持抵扣的计费项，按照折扣价格的实际消费金额总额未达到承诺消费金额，该部分抵扣项会被节省计划正常抵扣，但阿里云仍将对您实际收取该小时承诺金额的费用。
## 节省计划的抵扣项
当您开通节省计划后，节省计划将对以下抵扣项进行抵扣，您可以单击链接进入[节省计划总览页面](https://usercenter2.aliyun.com/resource/spn/overview)。在总览页面的操作列中，您可以单击设置抵扣规则开启或者关闭对应节省计划的抵扣项，进行精细化管理。可以参照下表说明对控制台中显示的是否抵扣进行配置。
重要
节省计划的抵扣项间没有固定的抵扣优先级顺序，抵扣逻辑为先出账先抵扣。若您设置的每小时承诺消费金额低于您的可抵扣实际消费时，可能会出现不同小时出账账单中节省计划抵扣的抵扣项不一致的情况，建议您参见[节省计划购买方案测算](purchase-savings-plan.md)，重新计算并升级您的节省计划，以帮助您更好地进行成本优化。
请注意，抵扣规则调整后会立即生效，但由于计费是延迟出账，调整抵扣规则的操作可能会作用到您正在出账的计费周期账单。
| 抵扣项名称 | 抵扣项说明 | ECS 计算型节省计划 | 通用型节省计划 |  |
| --- | --- | --- | --- | --- |
| 云服务器 ECS-按量付费 | 实例规格 | 持有符合抵扣规则的按量付费 ECS 实例规格实例时，该项抵扣规则可以对 [实例规格费用](instance-types.md) 进行抵扣。 | 支持 | 支持 |
| 云服务器 ECS-按量付费 | 系统盘 | 持有符合抵扣规则的按量付费 ECS 实例规格实例时，该项抵扣规则可以对云盘系统盘的 [云盘容量费用](block-storage-devices.md) 进行抵扣。 | 支持 | 支持 |
| 云服务器 ECS-按量付费 | 操作系统 | 持有符合抵扣规则的按量付费 ECS 实例规格实例时，该项抵扣规则可以对 [镜像计费](images.md) 中的 非云市场镜像 的 镜像 License 费用 进行抵扣。 | 支持 | 支持 |
| 云服务器 ECS-按量付费 | 公网带宽 | 持有符合抵扣规则的按量付费 ECS 实例规格实例时，该项抵扣规则可以对 [公网带宽计费](public-bandwidth.md) 的按固定带宽计费方式的公网带宽费用进行抵扣。 | 支持 | 支持 |
| 弹性容器实例 ECI | 实例 | 持有 按指定 ECS 规格创建 的 ECI 实例时，该项抵扣规则可以对 [ECI](https://help.aliyun.com/zh/eci/product-overview/elastic-container-instances) [实例费用](https://help.aliyun.com/zh/eci/product-overview/elastic-container-instances) 进行抵扣。 | 支持 | 支持 |
| 弹性容器实例 ECI | vCPU 规格 | 持有 按 vCPU 和内存创建 的 ECI 实例时，该项抵扣规则可以对 [ECI](https://help.aliyun.com/zh/eci/product-overview/elastic-container-instances) [实例费用](https://help.aliyun.com/zh/eci/product-overview/elastic-container-instances) 进行抵扣。 | 不支持 | 支持 |
| 弹性容器实例 ECI | 内存规格 | 不支持 | 支持 |  |
| 云盘性能 | 性能预配置 | 持有 创建成功并配置 预配置性能的 ESSD AutoPL 云盘 、ESSD PL-X 云盘 后，该项抵扣规则可以对云盘的 [预配置性能费用](block-storage-devices.md) 进行抵扣。 | 不支持 | 支持 |
| 云盘 | 数据盘 | 持有 创建成功 的云盘数据盘后，该项抵扣规则可以对云盘数据盘的 [云盘容量费用](block-storage-devices.md) 进行抵扣。 | 不支持 | 支持 |
| 云盘性能 | io_burst | 持有的 开启了性能突发 的 ESSD AutoPL 云盘的实例后，若在使用中发生了性能突发，该项抵扣规则可以对 [性能突发费用](block-storage-devices.md) 进行抵扣。 | 不支持 | 支持 |
| 即时生效容量预定 | 立即生效容量 | 购买立即生效容量预定后，该抵扣规则可以对 [立即生效容量预定](user-guide/overview-of-immediate-capacity-reservation.md) 产生的实例规格费用进行抵扣。 | 支持 | 支持 |
## 抵扣优先级
节省计划、预留实例券、资源包等折扣权益均可抵扣按量付费实例的账单，如果您同时享受多种折扣权益，抵扣优先级从高到低依次为：
预留实例券、存储容量单位包
ECS计算型节省计划
通用型节省计划
优惠券
代金券
说明
节省计划从资金角度抵扣按量付费账单，还遵循以下规则：如果您的按量付费实例相比节省计划具有更低的折扣率，将优先为您使用更低的折扣，且折扣的费用支持从节省计划的承诺消费金额中抵扣。
### 多份节省计划的抵扣优先级
如果您的一个阿里云账号下购买了多份节省计划，且不同计划之间折扣率不一致，则先过期的先抵扣（如果过期时间完全一致，再根据生效时间判断，即先生效先抵扣）不按照折扣率高低调整生效顺序。
例如，先购买全预付3年节省计划，一年后再购买半预付1年节省计划，后者先过期失效，则半预付1年的节省计划先抵扣，按照其折扣率抵扣账单。
## 抵扣规则示例
使用节省计划时，实例有两种计费单价：常规的按量单价（小时价格）和节省计划的折扣后单价。在节省计划可抵扣的金额范围内，按折扣后单价来计费并抵扣；超出节省计划可抵扣的金额范围，仍然按常规的按量单价计费。具体的折扣力度，请参见[节省计划折扣详情页](https://usercenter2.aliyun.com/resource/spn/price)。
通用型节省计划折扣示例
假设，您在华东2（上海）地域持有数台按量付费的ecs.g6.xlarge实例，购买了一份节省计划来优化成本，类型为通用型、付费类型为全预付、购买时长为3年，每小时承诺消费金额为2元/小时。
说明
该示例中的价格仅用于说明，实际的价格和折扣信息，请参见[云服务器](https://www.aliyun.com/price/product)[ECS](https://www.aliyun.com/price/product)[定价页](https://www.aliyun.com/price/product)和[节省计划价格折扣详情页](https://usercenter2.aliyun.com/resource/spn/price)。
假设，ecs.g6.xlarge的常规按量单价为1元/台/小时，华东2（上海）地域ecs.g6规格族的节省计划折扣为4.55折，则折扣后单价为1*0.455 = 0.455元/台/小时。由于每小时承诺消费金额为2元/小时，这份节省计划每小时最多可以抵扣2/0.455 = 4.396台ecs.g6.xlarge实例的按量账单。
分别按常规按量单价与折扣后单价计算，费用对比如下表所示。
| 计费方式 | 第一小时（假设运行 6 台实例） | 第二小时（假设运行 5 台实例） | 第三小时（假设运行 4 台实例） |
| --- | --- | --- | --- |
| 不使用节省计划，按常规按量单价的费用 | 费用合计：6 * 1 = 6 元 | 费用合计：5 * 1 = 5 元 | 费用合计：4 * 1 = 4 元 |
| 使用节省计划，按折扣后单价的费用 | 超过节省计划最多可抵扣台数（4.396 台），费用分为： 每小时承诺消费覆盖 4.396 台的费用。 超出部分需要按常规按量单价计费。 费用合计：2 + 1 * (6 - 2 / 0.455) = 3.604 元 | 超过节省计划最多可抵扣台数（4.396 台），费用分为： 每小时承诺消费覆盖 4.396 台的费用。 超出部分需要按常规按量单价计费。 费用合计：2 + 1 * (5 - 2 / 0.455) = 2.604 元 | 未达到节省计划最多可抵扣台数（4.396 台），每小时承诺消费可以覆盖所有费用。 费用合计：2 元 |
## 多账号共享一份节省计划进行抵扣
如果您是企业用户，阿里云支持一份节省计划共享给多个账号使用。您可以在开通企业账号中心的阿里云账号上开通权益资产共享功能，将节省计划共享到其他阿里云账号使用。
### 使用限制
多账号共享节省计划时存在以下限制：
不支持被共享节省计划的阿里云账号再将此节省计划共享。
单个节省计划最多支持共享到100个阿里云账号。
如果被共享的账号已经购买了节省计划，优先使用自身账号的节省计划进行抵扣。
### 开通节省计划多账号共享
共享节省计划前您需要先开通企业账号中心功能，并邀请企业其他成员账号加入，形成企业的账号组织关系。详细操作请参考[开通企业多账号管理服务](https://help.aliyun.com/zh/account/user-guide/activate-enterprise-account-center)。
如果您已经开通企业账号中心功能，您可以通过手动共享和自动共享两种方式开通节省计划跨账号共享
手动共享：指定具体的资产ID进行共享，可以选择共享到特定账号或组织节点，此设置仅对该资产ID有效。
自动共享：根据资产类型设定自动共享规则，新创建的资产会按照规则自动共享到指定范围。
详细操作指引请参见[权益资产共享](https://help.aliyun.com/zh/user-center/equity-asset-sharing)。
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
