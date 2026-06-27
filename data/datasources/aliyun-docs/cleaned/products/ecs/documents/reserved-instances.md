# 预留实例券-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/reserved-instances

# 什么是预留实例券
预留实例券就像一张云上ECS按量付费实例（不含抢占式实例）的会员卡，和其他会员卡一样，当一些特定属性被满足时产生作用。不同于传统的按量付费实例，您通过购买预留实例券相当于承诺了一定的使用时长。使用预留实例券将会为您的业务带来多项好处，例如可以大幅降低按量付费实例计算资源的账单、为您的业务带来实例的灵活性、资源确定性和业务连续性等。
重要
建议您使用节省计划，而不是预留实例券。节省计划相对于预留实例券，灵活性更好、折扣更有优势。更多信息，请参见[什么是节省计划](savings-plans.md)。
## 预留实例券概述
### 快速了解预留实例券
### 预留实例券类型
预留实例券支持地域级预留实例券和可用区级预留实例券两种类型。
地域级预留实例券
购买时只需指定地域。
可抵扣单地域下所有可用区内符合匹配条件的按量付费实例，且在同规格族内可跨不同规格抵扣。
不支持资源预留。
可用区级预留实例券
购买时必须指定地域及可用区。
仅可抵扣单可用区内实例规格大小相同的按量付费实例。
支持资源预留。在有效期内预留指定数量和指定规格的实例，保证随时可以在指定可用区中成功创建按量付费实例。
预留实例券类型影响匹配条件。更多信息，请参见[预留实例券的抵扣规则](match-between-reserved-instances-and-pay-as-you-go-instances.md)。您也可以在购买预留实例券后修改可用区。具体操作，请参见[修改预留实例券的可用区](split-merge-or-modify-reserved-instances.md)。
## 预留实例券的应用场景
在以下场景中，建议您购买预留实例券抵扣按量付费实例账单，兼顾灵活性和成本。
| 场景 | 选择预留实例券 |
| --- | --- |
| 使用弹性伸缩管理 ECS 实例，持有大量按量付费实例，希望降低成本。 | 使用预留实例券即代表承诺一定的使用时长，可以享受折扣，比只使用按量付费实例的成本低。 |
| 希望分期支出资源费用，减轻成本压力。 | 预留实例券支持按每小时支付（部分预付或 0 预付），避免一次性支付带来的资金链压力。 |
| 业务区域可能发生变更，您需要随之释放 ECS 实例，并在对应可用区创建新的 ECS 实例。 | 支持拆分、合并预留实例券，方便您在更改不同大小的新实例时继续抵扣按量付费账单。 支持随时修改预留实例券的可用区，地域级预留实例券直接支持跨可用区抵扣。 |
| 自动化运维中需要根据业务需求自动调整 ECS 实例数量。 | 使用预留实例券抵扣按量付费实例账单时，交付预留实例券的计算力而非具体的 ECS 实例，按量付费实例符合要求即可匹配，而不是和某一台 ECS 实例绑定，比使用包年包月实例的灵活性更高。 |
## 预留实例券的计费说明
### 付费类型
购买预留实例券时，支持以下几种付费类型：
全预付：购买时一次性预付所有费用，有效期内不再缴纳其他费用。
部分预付：购买时预付部分费用（约50%），有效期内需要继续缴纳每小时费用。
0预付：购买时无需支付，有效期内需要缴纳每小时费用。
说明
如需使用部分预付或0预付，请选择1年及以上时长。
是否支持0预付根据您的云服务器使用情况而定。如果您无法看到0预付的付费类型且需要使用，请联系您的商务经理。
无论预留实例券能否匹配到按量付费实例，在有效期内您都需要按付费类型支付费用，选择全预付可以节省更多成本。
在部分预付或0预付场景下，每小时费用计费时按秒计费，按小时结算。定价详情请参见[详细价格总览](https://www.aliyun.com/price/product#/ecs/detail)。
### 计费规则
预留实例券购买成功后，预留实例券即开始计算有效期，每小时自动匹配按量付费实例，并抵扣实例的计算资源小时账单。预留实例券与按量付费实例的匹配规则，请参见[预留实例券的抵扣规则](match-between-reserved-instances-and-pay-as-you-go-instances.md)。
预留实例券生效时间和失效时间均按整点计算，从生效时间开始计费，结束时间为到期日的0点。例如，您在2024-05-01 22:45:00成功购买了一张立即生效预留实例券，有效期为一年，该预留实例券的生效时间和计费开始时间为2024-05-01 22:00:00，失效时间为2025-05-02 00:00:00。如果您在购买预留实例券时已经持有可匹配的实例，则从2024-05-01 22:00～23:00的小时账单开始抵扣，直至预留实例券失效。
说明
选择指定时间生效时，生效时间和计费开始时间与您指定的时间相同。
### 续费说明
为持续享受预留实例券的抵扣优惠，建议您在预留实例券到期前，及时续费预留实例券以延长预留实例券的使用时间。预留实例券支持手动续费和自动续费两种续费方式。在预留实例券生命周期的不同阶段，您可以根据需要选择一种方式进行续费。
手动续费
在预留实例券失效前，您随时可以在ECS控制台手动为预留实例券进行续费，延长预留实例券的到期日。
登录[ECS](https://ecs.console.aliyun.com/reservedInstance/region)[控制台-预留实例券](https://ecs.console.aliyun.com/reservedInstance/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
找到待续费的预留实例券，在操作列中，单击续费。
在续费页面，选择续费时长（支持1月、1年、3年续费），根据业务需要选择自动续费，然后按照界面提示完成续费。
说明
续费时长是否支持1月续费需根据您的云服务器使用情况而定。如果您无法看到1月的续费时长且需要使用，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。
自动续费
开通预留实例券自动续费后，会在每次到期前自动续费，避免因为忘记手动续费导致预留实例券失效。
注意事项
如果在自动续费前已完成手动续费，则在同一计费周期内不会再自动续费。
如您在扣款日前手动续费，则系统按最新到期时间自动进行续费。
开通预留实例券自动续费后，在预留实例券到期前第9天开始，系统会进行首次扣款，请您务必保证账户可用额度充足。
说明
如果首次自动扣款失败，系统会继续每天尝试一次扣款，直至扣款成功或者实例到期。
操作步骤
访问[ECS](https://ecs.console.aliyun.com/reservedInstance/region)[控制台-预留实例券](https://ecs.console.aliyun.com/reservedInstance/region)。
找到待续费的预留实例券，在操作列中，单击>自动续费。
确认续费提示后，打开开启自动续费开关，选择续费时长，单击确定。
### 退款说明
以下情况下，您可以申请退款：
购买预留实例券的五天内，可以申请无理由退款。
每个阿里云账号每年只有一次五天无理由退款的机会。例如，您同时购买了一台ECS实例和一张预留实例券，如果ECS实例无理由退款，则同年内无法再申请预留实例券无理由退款。
拆分、合并预留实例券或者调整预留实例券范围后，目标地域或可用区下的实例资源库存不足。
## 预留实例券的使用限制
| 限制项 | 描述 |
| --- | --- |
| 预留实例券数量 | 预留实例券数量限制和预留实例券类型有关： 地域级预留实例券：在所有地域下，您最多可以持有 20 张地域级预留实例券。 可用区级预留实例券：可用区级预留实例券的数量单独计算，在每个可用区下，您最多可以各持有 20 张可用区级预留实例券。 如果您需要更多数量的预留实例券，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 申请。 |
| 预留实例券规格 | gn6i、t5 实例规格族不支持地域级预留实例券、也不支持拆分和合并。 说明 购买预留实例券时支持选择的实例规格以实际界面显示为准。 |
| 抵扣的资源类型 | 仅支持抵扣按量付费实例（不含抢占式实例）。 仅支持抵扣计算资源（vCPU 和内存）的费用，不支持抵扣网络、存储等资源的费用。关于 ECS 实例计费详情，请参见 [计费概述](billing-overview.md) 。 Windows 类型的预留实例券还支持抵扣镜像的费用。 说明 Windows 类型的预留实例券在购买时已经包括了 Windows 镜像的费用，可以用于抵扣运行 Windows 系统的按量付费实例镜像部分的账单。 |
## 相关文档
购买预留实例券之前，建议您提前了解预留实例券与按量付费实例之间的抵扣规则，详情请参见[预留实例券的抵扣规则](match-between-reserved-instances-and-pay-as-you-go-instances.md)。
如何购买预留实例券，请参见[购买预留实例券](purchase-reserved-instances.md)。
如果您的工作负载发生变化，可以通过拆分、合并预留实例券或修改预留实例券的可用区，以灵活匹配不同规格和可用区的按量付费实例，详情请参见[拆分、合并或修改预留实例券](split-merge-or-modify-reserved-instances.md)。
您可以查看预留实例券支持抵扣的实例、计算力因子等信息，查看预留实例券的账单明细以及使用率和覆盖率，详情请参见[查看预留实例券](view-reserved-instances.md)。
关于预留实例券的一些常见问题，请参见[实例](user-guide/instance-faq.md)[FAQ](user-guide/instance-faq.md)。
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
