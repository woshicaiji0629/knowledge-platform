# 什么是节省计划-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/savings-plans

# 什么是节省计划
节省计划是一种用于抵扣长期使用按量付费资源的折扣权益，可以为您抵扣ECS或ECI按量付费实例（不含抢占式实例）的账单。合理的配置您的节省计划可以让您在灵活使用资源的同时，享受较低的折扣。本文将从了解、购买、使用及运维等角度为您介绍节省计划。
## 什么是节省计划
节省计划是一种用于抵扣长期使用按量付费资源的折扣权益，可以抵扣ECS和ECI按量付费实例（不含抢占式实例）的费用。您可以通过承诺一年期、三年期或五年期内每小时的资源消费金额，换取相比于按量付费方式更低的折扣来使用您的资源。相较于同为折扣权益的预留实例券，节省计划在解决您按量使用成本较高的问题基础上，支持多规格、多规格族、多地域及操作系统间的灵活变更。
如果您长期以按量付费的方式使用资源，您可以开通节省计划来获得更低的折扣，降低资源使用成本。
如果您日常以包年包月的方式使用资源，转换为按量付费并开通节省计划后可以提升使用资源的灵活性，让您在业务需求变更时无需额外付费，即可更改当前资源的实例规格、规格族、地域等属性。
由于节省计划只是一种折扣权益，不会影响您的资源状态，因此在无实例的状态下仅购买节省计划并不会帮您购置对应资源，需要您搭配按量付费实例才能真正产生降低资源成本的价值。合理使用节省计划可以让您相比于按量付费方式最多降低83%的资源使用成本。
### 节省计划的优势对比
阿里云根据您期望的资源使用灵活性的不同，为您提供了两种类型的节省计划：ECS计算型或通用型。使用节省计划与其他长期使用资源的付费方式对比参见下图。
### 节省计划抵扣机制
节省计划购买后不会直接为您提供对应的资源，需要搭配您购买的按量付费资源使用。如果您原先仅使用按量付费的方式，开通合适的节省计划可以为您带来成本优化。如图所示，当您开通节省计划来抵扣按量付费资源后，阿里云会根据您设定的承诺消费金额每小时收取费用。在生效期内，节省计划会自动匹配符合条件的资源进行抵扣。匹配成功后，每小时的资源按出账顺序，以折扣后的价格抵扣。对于每小时超出承诺消费金额的部分费用，您仍需按照按量付费的标准价格支付。详细的抵扣规则请参见[节省计划抵扣项及抵扣规则](savings-plan-credit-rules.md)。
重要
若您小时内节省计划的实际抵扣费用低于设置的承诺消费金额，您仍然需要支付承诺消费与实际消费差值（即仍然按照承诺消费金额收费），所以合理的购前测算评估有助于您更好地进行成本管理。阿里云也为您提供了节省计划的购买建议，您可以参见[购买节省计划](purchase-savings-plan.md)进行配置。
### 节省计划的适用场景
在购买节省计划前，您可以从业务类型特征、资源使用成本以及账单运维管理三个角度，了解节省计划带给您的业务收益，以及结合您的业务情况判断是否适合使用节省计划。
- 业务类型特征
由于节省计划需要承诺每小时消费固定的金额，因此适合资源需求相对平稳的业务模型。如果您的业务对资源灵活使用有需求，且业务模型符合以下特点，可优先选择节省计划抵扣长期按量付费的稳定资源需求，搭配按量付费满足短时资源需求波动，降低资源运营成本。若您存在业务负载持续增长，您也可以选择开通使用较低承诺消费的节省计划，并根据您的业务情况进行升级，达到便捷运维管理的效果。
| 共振型业务 各个业务间有关联，流量增长后各业务对资源的诉求同时增长。 优势：相比于包年包月搭配按量付费的方式 ， 灵活性进一步提升 ，所有资源基于按量管理，无需分批维护。生命周期管理大幅简化。可随时对资源进行调整，预算简单，无需做容量预估 | 混部型业务 线上有多个业务，不同业务在不同时间段对资源的诉求不同。 优势：成本最优 ，无需担心包年包月升降配及退款带来额外费用。所有资源基于按量管理，无需分批维护。预算简单，无需做容量预估。 | 平稳型业务 业务相对平稳，在不同时段对资源诉求类似。 优势： 所有资源基于按量管理，无需分批维护。生命周期管理大幅简化。 可随时对资源进行配置变更调整 ，预算简单，无需做容量预估。 | 阶段增长型业务 业务负载整体稳步增长，存在阶段资源需求相对稳定的情况。 优势： 对于持续增长场景，可叠加多个节省计划或升级节省计划支持业务扩展，在 降低业务运营成本的同时简化财务运维工作 。 |
| --- | --- | --- | --- |
|  |  |  |  |
- 使用成本
如果您因为业务的需求，有资源变更的需求，同时希望云上资源的使用成本相对稳定，您可以尝试使用节省计划帮您降低产生额外费用的风险。
| 有资源变更需求 包年包月实例未到期前变更实例配置或地域，可能会产生额外费用，这些费用累积之后可能会造成整体成本超出预算的情况。 使用按量付费方式虽然不会因为实例变更而产生额外费用，但会较大增加总体成本。 使用按量付费并开通节省计划的付费方案，可以有效降低您的变更费用支出，还能获得资源价格折扣，帮您保持整体资源使用成本长期处于稳定状态，降低长期使用总成本。下图展示了一些常见变更操作下的整体费用变化。 | 有资源的种类变更的需求 如果您的业务资源负载有波峰波谷的情况，且存在多种规格的实例的负载曲线在时段上并不完全重合，使用包年包月的方式由于资源存在闲置时间，会导致单一规格资源的单位时间使用成本上升，总体使用成本上升。而 开通节省计划抵扣按量付费，可以享受跨规格族折扣权益，总成本明显降低。 |
| --- | --- |
|  |  |
- 预算和成本管理
包年包月和按量付费的实例都为实例粒度的独立计费，云上预算管理复杂。节省计划不限制实例规格和操作系统，可以灵活变配，并且作为计划出账极大简化了云上预算管理成本。
## 节省计划的测算与购买
当您决定购买节省计划时，首先需要结合业务实际情况进行合理的购前评估测算。您可以参见[购买节省计划](purchase-savings-plan.md)，按照阿里云为您测算的推荐方案进行购买，或者在手动测算评估后前往下单页面进行购买。在进行手动测算购买方案时，需要根据您的业务的预算、交付方式、资源使用时长等因素，查询对应条件下的节省计划折扣，确定开通节省计划的类型、规格、每小时承诺消费金额以及时间等订单信息后，前往[节省计划购买页面](https://common-buy.aliyun.com/?spm=a2c4g.11186623.0.0.638335e6sjWHzg&commodityCode=savingplan_common_public_cn#/buy)配置下单。
说明
如果您想要升级您的节省计划，请参见[升级当前节省计划](analysis-and-optimization-of-saving-plan-effect.md)。
在实际下单页面，调整除承诺消费和购买年限以外的购买项，并不会影响您的实际支付金额（总配置费用），仅会影响您节省计划可以每小时抵扣的实际资源量，强烈建议您参考推荐方案或进行手动购前测算评估后再前往购买页面进行下单。若您有其他优惠折扣，请以最终支付价格为准。
## 购买和使用限制
节省计划的使用和购买存在以下限制：
购买限制：
每个阿里云账号最多购买200份节省计划。
使用限制：
仅支持抵扣ECS及ECI按量付费实例（不含抢占式实例），详细的抵扣项及抵扣规则信息请参见[节省计划抵扣项及抵扣规则](savings-plan-credit-rules.md)。
ECS实例仅支持抵扣：计算资源（vCPU和内存）、镜像、系统盘、数据盘（包括容量费用、预配置性能费用、性能突发费用）、固定公网带宽。关于ECS实例计费详情，请参见[计费概述](billing-overview.md)。
ECI实例（非指定实例规格）仅支持抵扣：计算资源（vCPU和内存），关于ECI实例计费详情，请参见[ECI](https://help.aliyun.com/zh/eci/product-overview/elastic-container-instances)[实例计费](https://help.aliyun.com/zh/eci/product-overview/elastic-container-instances)。
## 节省计划的生命周期
### 生效时间及影响
支付后立即开通：从您支付时间所在小时的0分0秒开始生效抵扣费用。
指定时间开通生效：最长支持下单后一年后开通，支持选择小时单位的生效时间，设置的生效小时的0分0秒开始抵扣费用。
例如，您在2024-10-29 13:45购买了一份立即开通生效的节省计划，有效期为一年，则该节省计划的生效时间为2024-10-29 13:00，失效时间为2025-10-29 13:00。如果您已经持有满足匹配要求的按量付费实例，则从2024-10-29 13:00～14:00（即下单的当前小时）的账单开始抵扣，直至节省计划失效。
### 失效时间及影响
已开通节省计划的失效时间可以通过[费用与成本](https://usercenter2.aliyun.com/home?spm=a2c4g.11186623.0.0.7d916dd4p90FAa)的节省计划列表进行搜索查询。
重要
节省计划按照您的购买时长到期整点失效后，您将不再享受节省计划提供的折扣，您被抵扣的按量实例将恢复正常按量付费价格。被抵扣的按量实例不会释放，不会对您的业务造成影响。
### 欠费停服说明
如果在购买节省计划时付费类型选择了部分预付或者0预付，如果账号欠费导致不能支付小时固定费用，产生欠费后节省计划立即进入欠费受限状态（当您符合延期免停权益时，不受该规则限制。更多信息，请参见[延期免停权益](https://help.aliyun.com/zh/user-center/exemption-of-suspension-after-delinquency)）。节省计划进入欠费受限状态的下个小时开始停止抵扣按量付费账单，当您缴清欠款后，节省计划可立即恢复抵扣按量付费账单。
重要
如果节省计划多次或者长期处于欠费受限状态，会影响您后续使用阿里云相关产品的0预付功能，请尽量保持账号余额充足。
当节省计划进入欠费状态后，虽然会停止抵扣按量付费资源的账单，但是仍然会持续出账。
## 查看账单
您可以在阿里云费用与成本中心的明细账单中，查看节省计划的明细消费信息。
登录[费用与成本](https://usercenter2.aliyun.com/home)控制台，在左侧导航栏，选择账单 > 账单详情。
在明细账单列表中，添加筛选项商品名称为节省计划及其他所需筛选并导出相关数据。如果您需要详细的操作指引信息，请参见[如何查询节省计划账单](https://help.aliyun.com/zh/user-center/how-to-check-the-savings-plan-bill#32c02a707eusr)。
说明
默认展示登录账号的数据，若登录账号为财务主账号，您还可以通过筛选账号的方式查看财务管理子账号的数据，以及通过Owner账号区分财务托管子账号的数据。
## 退订节省计划
自2026年4月3日起，阿里云支持节省计划自助退订。退订条件和限制如下：
| 条件 | 说明 |
| --- | --- |
| 支持退订的类型 | 未使用的节省计划：已购买但尚未产生任何抵扣的节省计划，可全额退款。 未生效的节省计划：购买时选择了未来指定时间生效的节省计划，可在生效日期之前全额退款。 续费的节省计划：续费周期尚未开始的节省计划续费订单，可退订续费部分。 |
| 付费类型限制 | 仅支持 全预付 类型的节省计划自助退订。半预付和无预付类型暂不支持自助退订。 |
| 不支持退订的情况 | 已产生抵扣的节省计划暂不支持自助退订。 |
说明
更多信息请参见[节省计划自助退订能力上线公告](https://www.aliyun.com/notice/118142)。
## 续费节省计划
在节省计划到期之前，您可以随时选择手动续费或设置自动续费，以延长节省计划的使用时间。您可以在[节省计划概览控制台](https://usercenter2.aliyun.com/resource/spn/overview)续费节省计划，或进入费用与成本中心，参见[续订到期资源](https://help.aliyun.com/zh/user-center/renewal-guide-1)指引完成续费或设置自动续费操作。
说明
当前手动续费仅支持您按原订单时长进行续费。例如：原订单的购买时长为1年，则续费时也只能续费1年。
## 查询并优化节省计划使用情况
阿里云建议您日常监测已购买的节省计划使用情况，并根据业务变动及时调整节省计划的配置，以获得更好的成本效益。阿里云为您提供了节省计划使用率和覆盖率报告，您可以结合[查询与优化节省计划使用情况](analysis-and-optimization-of-saving-plan-effect.md)中的指导建议或参见[节省计划购买方案测算页面](https://usercenter2.aliyun.com/resource/spn/recommend)的建议对节省计划进行优化。
## 常见使用问题
如果您在使用节省计划期间遇到了其他问题希望寻求帮助，您可以参考[节省计划](billing-faq.md)[FAQ](billing-faq.md)。
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
