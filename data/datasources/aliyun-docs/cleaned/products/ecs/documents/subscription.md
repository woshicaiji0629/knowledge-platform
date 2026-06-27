# 什么是包年包月预付费计费方式-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/subscription

# 包年包月
包年包月是一种预付费的计费方式，您需要预先支付一段时间（如1月、1年）的费用，以获得更低的单价和更大的成本节约，购买时长越长，折扣越大。本文主要介绍包年包月ECS资源的适用场景、到期后影响、退款说明等信息。
## 适用场景
当您的业务具有如下特征时，推荐购买包年包月资源：
可预估资源使用周期。
具有较稳定的业务场景。
需要长期使用资源。
常见场景：例如7 × 24小时的官网页面服务、数据库服务等。
## 计费规则
包年包月为预付费模式，包含实例规格、系统盘、数据盘、镜像及固定带宽公网流量的基础资源费用，若实例购买时配置的资源全部为包年包月计费方式，则购买周期内无额外扣费，到期自动停机。若中途调整实例配置，升级需补差价，降级可依据退款规则退还差额。
说明
购买包年包月实例时，可能会因为配置了按量付费资源或功能在实例使用时产生额外费用。如果您要保持多种计费方式，请关注您的账户余额，以免余额不足导致欠费影响资源使用。您也可以查看[计费](billing-faq.md)[FAQ](billing-faq.md)了解包年包月情况下的按量付费费用产生情况。如果您想将此类按量付费资源转为包年包月计费，请参见[转换计费方式](change-the-billing-method.md)。
阿里云的包年包月服务中的购买、续费时长均指自然年、月。比如您在2025年2月某日购买了1个月的ECS云服务器，到期日为2025年3月同日，而非30天后。
### 基础计费项
假设您计划以包年包月的计费方式购买一台使用付费镜像的ECS云服务器，并同时购买一块数据盘，分配了公网IPv4地址并选择按固定带宽计费。在购买云服务器页面右下角，单击查看明细，您将看到所需费用的明细，如下所示。
| 按照假设情况购买的实例的费用明细将包括以下部分： 实例 ：即 实例规格 费用，包括该实例下的计算资源（vCPU、内存、GPU）费用， [本地盘](user-guide/local-disks.md) （实例上不可卸载的存储设备）费用，以及 [增强型](user-guide/enhanced-instance-families.md) 实例的功能增强组件费用。 系统盘：云盘 容量费用。 数据盘：云盘 容量费用。 带宽：公网带宽（按固定带宽） 费用 ， 根据所选带宽大小计算的费用。 镜像费用：镜像 许可证费用 ， 基于付费镜像的市场价格。 您可以根据购买时的计费明细中显示的计费项对照查看对应计费项的计费规则。 说明 本场景仅作计费项和计费规则说明示例，实际计费项请以您购买时显示为准。 |
| --- |
包年包月的实例购买价格取决于您所购买实例的地域、资源规格及购买时长，具体规则见下表。
| 计费项 | 包年包月价格 | 购买时长 |
| --- | --- | --- |
| [实例规格](instance-types.md) | 同一实例规格在不同地域下的价格可能不同，具体价格请参见 [云服务器](https://www.aliyun.com/price/product) [ECS](https://www.aliyun.com/price/product) [定价页](https://www.aliyun.com/price/product) 。 | 1 周至 5 年 ，具体可购买时长请参见下单购买页面。 说明 如果您的实例用于 Web 服务，中国内地必须完成 ICP 备案，备案实例（含续费）时长需在 3 个月及以上，详细规则请参见 [ICP](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/overview) [备案前准备](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/overview) 。 |
| [云盘](block-storage-devices.md) | 同一类型的云盘在不同地域的价格均可能不同，具体价格请参见 [块存储价格](https://www.aliyun.com/price/product#/disk/detail) 。 | 包年包月实例中的此部分资源仅可随实例一起下单购买，费用计算时购买时长与实例购买时长相同。 |
| [公网带宽（按固定带宽）](public-bandwidth.md) | 不同地域的公网带宽价格请参见 [云服务器](https://www.aliyun.com/price/product#/ecs/detail) [ECS](https://www.aliyun.com/price/product#/ecs/detail) [定价](https://www.aliyun.com/price/product#/ecs/detail) 中的带宽价格页签。 |  |
| [镜像](images.md) | 阿里云公共镜像单价请参见 [镜像计费](images.md) ，云市场镜像价格以创建实例时显示的信息为准。 |  |
### 升级与降配
创建实例后，如果当前实例配置无法满足您的业务需求，您可以修改实例规格、公网带宽配置和数据盘配置，操作和详细介绍请参见[升降配方式概述](user-guide/overview-of-instance-configuration-changes.md)。实例在升降配后会涉及以下费用变动：
升级配置：升级配置时需补缴新配置费用与剩余价值的差额，具体费用以升级时页面上显示的费用信息为准。
降低配置：实例进行降配操作后会发生降配退款，退款金额的计算方式请参见[退订规则说明](https://help.aliyun.com/zh/user-center/cancel-subscription/#12a66a5a513qd)。
## 转换计费方式
### 包年包月转按量付费
创建一台包年包月ECS实例后，您可以将ECS实例的计费方式转为按量付费，回收部分成本，同时更加灵活地按需使用ECS实例。包年包月ECS实例转换为按量付费ECS实例后，请确保支付方式可用额度充足以免发生欠费，影响ECS实例正常运行。具体操作和变更影响，请参见[包年包月转按量付费](change-the-billing-method-of-an-instance-from-subscription-to-pay-as-you-go-1.md)。
### 按量付费转包年包月
将按量付费的实例转换为包年包月，可以提前预留资源，同时享受更大的价格优惠。具体操作和变更影响，请参见[按量付费转包年包月](change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md)。
## 到期及续费说明
在ECS包年包月资源到期前，建议您尽快[续费实例](manually-renew-an-instance-1.md)，或通过快照保存数据，避免造成数据和业务损失。若有其他问题，您可以参见[资源续订常见问题](https://help.aliyun.com/zh/user-center/support/renewal-guide-q-a)。
### 到期提醒
阿里云消息中心提供了续费提醒功能，默认会在实例到期前7天、3天、1天、到期当天及释放前一天通过站内信、邮箱、短信提醒您及时续费。您也可以在消息中心主动订阅实例到期前15天或30天的提醒，或修改提醒接收手机号。具体操作，请参见[设置续费提醒](set-renewal-reminder.md)。
### 到期后影响
| 资源类型 | 到期后 15 天内（已过期） | 到期后 15 天内（过期回收中） | 到期第 16 天 0 点起 |
| --- | --- | --- | --- |
| 实例规格资源 | 保留计算资源（vCPU、GPU 和内存等）。保留本地盘和本地盘数据。 | 在此期间释放计算资源（vCPU、GPU 和内存等）。保留本地盘，但释放本地盘数据。 | 计算资源（vCPU 和内存）已经被释放。释放本地盘和本地盘数据。 |
| 块存储 | 云盘：如果关闭云盘随实例释放属性，自动转换成按量付费云盘并保留下来持续计费。 | 云盘：如果关闭云盘随实例释放属性，自动转换成按量付费云盘并保留下来持续计费。 | 云盘： 释放包年包月云盘和云盘数据。 释放开启了随实例释放属性的按量付费云盘和云盘数据。 说明 如果云盘开启了 自动快照随云盘释放 属性，自动快照会随云盘释放而自动删除。更多信息，请参见 [设置自动快照随云盘释放](user-guide/enable-or-disable-an-automatic-snapshot-policy.md) 。 |
| 公网 IP | 保留固定公网 IP 地址。 绑定的 EIP 地址不受影响。 | 保留固定公网 IP 地址。 绑定的 EIP 地址不受影响。 | 释放固定公网 IP 地址。 解绑 EIP 地址。 |
### 续费操作指引
在实例到期被释放前，您可以查看[如何续费包年包月实例](manually-renew-an-instance-1.md)，延长相关ECS实例的使用时间，或[设置续费提醒](set-renewal-reminder.md)，避免因未及时接收到ECS续费提醒消息而导致未及时续费，对您的业务造成影响。
## 查看账单
当资源出账后，您可在[账单详情](https://billing-cost.console.aliyun.com/finance/split-bill)查看在阿里云上的明细消费信息，并查询对应资源账单。通过这些字段信息，您可以进行用量价格核对和折扣核对，还原费用计算过程。账单功能的使用介绍请参见[账单使用说明](https://help.aliyun.com/zh/user-center/instructions-for-using-the-bill)。
## 退订及欠费说明
包年包月ECS资源除特定场景外支持退订退款，并返还部分资源费用，具体退款条件、退款操作、退款后资源保留情况等，请参见[退订说明](refund-instructions.md)。
如果账号内存在欠费账单，您可以正常使用已有的包年包月ECS资源，但不能进行新购实例、升级实例配置、续费订单等涉及费用的操作。更多信息，请参见[欠费说明](overdue-payments.md)。
## 常见问题
我的包年包月ECS实例为什么会产生按量付费费用？只购买了包年包月ECS为什么还没到期就欠费了？
包年包月实例可能在购买实例时开启了按量付费功能，或者使用过程中变更配置或者绑定了按量付费资源的情况导致产生按量付费费用，常见的情况如下：
购买包年包月ECS实例时进行了如下配置，或使用过程中将实例配置变更为如下配置：
配置公网带宽时选择了按使用流量计费的计费模式。
系统盘、数据盘类型为ESSD AutoPL云盘并配置了预配置性能。
系统盘、数据盘类型为ESSD PL-X云盘时，将以按量付费的方式收取预配置费用。
系统盘、数据盘类型为ESSD AutoPL云盘并配置了性能突发，发生性能突发时，将以按量付费的方式收取突发费用。
为实例配置了自动快照策略，在触发并生成快照时，会产生快照存储费用。
实例为突发性能实例，开启了无性能约束模式，若实例超额使用了CPU积分，则会产生[额外积分费用](user-guide/billing.md)。
使用包年包月实例过程中进行了如下操作：
挂载了按量付费的数据盘。
绑定了按量付费的弹性公网IP（EIP）、负载均衡、NAT网关等按量付费公网产品。
创建自定义镜像或者手动快照。
如果您想将此类按量付费资源转为包年包月计费，请参见[转换计费方式](change-the-billing-method.md)。
更多常见问题可参见[计费常见问题](billing-method-faqs.md)。
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
