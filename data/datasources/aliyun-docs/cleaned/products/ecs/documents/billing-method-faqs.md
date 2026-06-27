# 实例计费方式与成本优化FAQ-云服务器ECS-阿里云-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/billing-method-faqs

# 计费方式常见问题
## 包年包月实例计费问题
[我的包年包月](billing-method-faqs.md)[ECS](billing-method-faqs.md)[实例为什么会产生按量付费费用？只购买了包年包月](billing-method-faqs.md)[ECS](billing-method-faqs.md)[为什么还没到期就欠费了？](billing-method-faqs.md)
[包年包月实例未到期但提示欠费，是什么原因？](billing-method-faqs.md)
[包年包月和预留实例券和或节省计划对比有什么差异？](billing-method-faqs.md)
## 按量付费实例计费问题
[按量付费实例能使用代金券结算吗？](billing-method-faqs.md)
[按量付费实例能备案吗？](billing-method-faqs.md)
[按量付费实例结算时间怎么算？](billing-method-faqs.md)
[按量付费](billing-method-faqs.md)[ECS](billing-method-faqs.md)[实例停机或欠费停机后，会产生费用吗？](billing-method-faqs.md)
## 计费方式转化问题
### 包年包月转按量付费
[包年包月转按量付费失败时如何处理？](billing-method-faqs.md)
[新创建的包年包月实例在](billing-method-faqs.md)[5](billing-method-faqs.md)[天内转为按量付费，属于](billing-method-faqs.md)[5](billing-method-faqs.md)[天无理由退款吗？](billing-method-faqs.md)
[临时升级包年包月实例的带宽，计费方式是什么？](billing-method-faqs.md)
### 按量付费转包年包月
[按量付费转包年包月时下单失败如何处理？](billing-method-faqs.md)
[我有一个按量付费转包年包月订单，但是还没有支付，这时我升级了实例的配置，转换订单还有效吗？](billing-method-faqs.md)
[为什么无法将按量付费实例转为包年包月实例？](billing-method-faqs.md)
## 节省停机模式问题
[什么类型的](billing-method-faqs.md)[ECS](billing-method-faqs.md)[实例支持节省停机模式？](billing-method-faqs.md)
[打开默认启用节省停机模式后，是否支持单台](billing-method-faqs.md)[ECS](billing-method-faqs.md)[实例关机时不释放计算资源和网络资源？](billing-method-faqs.md)
[在](billing-method-faqs.md)[ECS](billing-method-faqs.md)[实例操作系统内关机能否触发节省停机效果？](billing-method-faqs.md)
[本地盘实例是否支持自动触发节省停机效果？](billing-method-faqs.md)
[ECS](billing-method-faqs.md)[实例触发节省停机效果后，为什么立刻启动时会报错](billing-method-faqs.md)[OperationConflict？](billing-method-faqs.md)
[ECS](billing-method-faqs.md)[实例触发节省停机效果后，为什么](billing-method-faqs.md)[StartInstance](billing-method-faqs.md)[时会报错](billing-method-faqs.md)[OperationDenied.NoStock？](billing-method-faqs.md)
[启用了节省停机模式后，停机再开机时公网](billing-method-faqs.md)[IP](billing-method-faqs.md)[会变化，怎么保持公网](billing-method-faqs.md)[IP](billing-method-faqs.md)[不变？](billing-method-faqs.md)
## 附录
包年包月和预留实例券和或节省计划对比有什么差异？
对于稳定的业务负载，您可以采用包年包月、按量（预留实例券抵扣）或按量（节省计划抵扣），能够获得一定程度的价格优惠。当购买时长相同时，在灵活性上，节省计划>预留实例券>包年包月。三种方式能力对比如下表所示。
| 对比项 | 包年包月 | 预留实例券 | 节省计划 |
| --- | --- | --- | --- |
| 优惠限制 | 仅为购买的某台实例提供优惠。 | 单券可为多台（最多支持 100 台）特定实例提供优惠，抵扣时要匹配实例。 | 直接为账单消费提供优惠，不限制实例数量，抵扣时非常灵活。 |
| 资源预留 | 支持。 | 支持。选择可用区级预留实例券。 | 不支持。 |
| 跨产品 | 不支持。 | 支持。可同时应用于 ECS 和 ECI。 | 支持。可同时应用于 ECS 和 ECI。 |
| 跨地域 | 不支持。 | 不支持。 | 支持。选择通用型节省计划。 |
| 同地域跨可用区 | 不支持。 | 支持。选择地域级预留实例券。 | 支持。 |
| 跨实例规格族 | 不支持。 | 不支持。 | 支持，选择通用型节省计划。 |
| 同规格族内跨规格 | 不支持。 | 支持。 | 支持。 |
| 跨操作系统 | 不支持。 | 不支持。 | 支持。 |
| 跨账号（基于财务云托管） | 不支持。 | 支持。 | 支持。 |
| 分期支持 | 不支持。 | 支持。可选全预付、部分预付或 0 预付。 | 支持。可选全预付、部分预付或 0 预付。 |
### 我的包年包月ECS实例为什么会产生按量付费费用？只购买了包年包月ECS为什么还没到期就欠费了？
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
包年包月转按量付费失败时如何处理？
包年包月转按量付费失败可能由以下原因导致：
实例当前状态不支持转换：例如，实例存在未支付的订单。
实例已过期：处于已过期状态的实例无法转换。
实例信息变更：如果实例配置发生改变，如临时升级了带宽，也可能不允许转换。
针对这些问题，解决办法如下：
检查实例状态：确保没有未支付的订单，并且实例不是已过期状态。
复核实例配置：如果近期对实例进行了任何修改，可能需要撤销这些改动，使实例回到转换前的原始配置状态。
如果根据上述提示调整实例后仍无法解决问题，或者遇到不明确的错误提示，请寻求官方技术支持帮助。
新创建的包年包月实例在5天内转为按量付费，属于5天无理由退款吗？
不属于。包年包月转按量付费后您依旧在使用实例。关于5天无理由退款的规则请参见[5](https://help.aliyun.com/zh/document_detail/37096.html)[天无理由退款说明（ECS）](https://help.aliyun.com/zh/document_detail/37096.html)。
临时升级包年包月实例的带宽，计费方式是什么？
临时升级包年包月实例的带宽时，一次性按包月价格标准收取升级部分的费用。如果升级时长不足1个月，则按实际时长换算。详细的带宽价格信息，请参见[云产品定价页](https://www.aliyun.com/price/product#/commodity/vm)。
说明
如需临时升级包年包月实例的带宽，请确保公网带宽计费方式为按固定带宽。具体操作，请参见[包年包月实例临时升级固定公网带宽（连续时间段）](user-guide/temporary-bandwidth-upgrade.md)和[包年包月实例临时升级固定公网带宽（周期性）](user-guide/temporary-upgrade-bandwidth-on-a-daily-basis.md)。
例如，您持有一台包年包月实例，公网带宽计费方式为按固定带宽，当前带宽为4 Mbit/s。将带宽临时升级到5 Mbit/s，升级时长1天，则提升的1 Mbit/s带宽一次性收取费用，费用为（1 Mbit/s带宽包月价格）/30。
包年包月实例未到期但提示欠费，是什么原因？
购买包年包月实例后，如果您继续使用了涉及后付费的服务，例如快照容量、按使用流量类型公网带宽等，将仍然会产生后付费账单。这类费用并未在购买包年包月实例时收取，因此，当您的账户不能支付后付费账单时会导致欠费。您可以查看消费明细，确认是否有后付费账单，具体操作，请参见[账单查询](view-billing-details.md)。
按量付费实例能使用代金券结算吗？
支持。请确保购买按量付费产品的代金券在有效期内，且适用场景为通用。
按量付费实例能备案吗？
不能。如果您的网站需要备案，请您购买包年包月实例。
按量付费实例结算时间怎么算？
按量付费实例按秒计费，整点结算，以系统自动结算时间为准。例如，01:30创建了ECS实例，到02:00释放，01:00:00~02:00:00为一个结算周期，实际计费时长为 (30 min) × 60 = 1800s。
按量付费ECS实例停机或欠费停机后，会产生费用吗？
欠费停机：指实例因账号欠费而自动停止服务，处于欠费停机状态的实例不计费。但账号欠费后，实例不会一直处于欠费停机状态，详情请参见[按量付费](pay-as-you-go-1.md)。
主动停机：指在实例正常运行期间，您通过ECS管理控制台或StopInstance接口，使实例进入已停止状态。此时，实例的计费情况取决于是否启用了节省停机模式。
启用节省停机模式：从创建开始计费，实例处于已停止状态时部分资源停止计费，实例启动后又重新计费。按量付费实例节省停机模式只适用于实例的计算资源（即vCPU和内存）和固定公网IP地址，但云盘、EIP等其它资源仍然正常计费。更多信息，请参见[节省停机模式](user-guide/economical-mode.md)。
未启用节省停机模式：即使实例停止，也会继续正常计费。
综上所述，欠费停机不产生费用，而主动停机是否计费则依据实例配置和网络类型有所不同。
按量付费转包年包月时下单失败如何处理？
按量付费ECS实例转换为包年包月时下单失败，可能是由以下原因导致的：
实例当前状态不支持转换：例如，存在欠费账单或实例已设置了自动释放时间。
实例信息变动：实例配置发生改变或存在未支付的转换订单。
不满足转换条件：如实例为已停售规格、抢占式实例，或存在未关闭的自动释放设置。
针对这些问题，您可以采取以下措施：
确认并处理账号的欠费问题，关闭自动释放时间设置。
检查实例是否有正在进行的配置变更或未完成的订单，需要先完成或取消这些操作。
确保实例规格不在已停售列表中，且非抢占式实例。
如果根据上述提示调整实例后仍无法解决问题，请寻求官方技术支持帮助。
按量付费转包年包月之后带宽计费方式是否发生变化？
不变。按量付费转包年包月功能只支持转换实例和云盘的计费方式，带宽计费方式的变更方法请参见[升降配方式概述](user-guide/overview-of-instance-configuration-changes.md)。
我有一个按量付费转包年包月订单，但是还没有支付，这时我升级了实例的配置，转换订单还有效吗？
按量付费转包年包月时会创建一个新购订单，如果您在未支付该订单的情况下升级了实例的配置，由于实例的组件已经发生变化，原订单的金额将不再匹配当前实例的配置，因此该订单会被禁止支付，所以该转换订单会失效。
如果您仍希望继续进行计费方式的转换，您需要先在[订单管理](https://usercenter2.aliyun.com/order/list)页面作废这个未支付的订单，然后根据实例升级后的配置重新发起按量付费转包年包月的操作。
为什么无法将按量付费实例转为包年包月实例？
待转换的按量付费ECS实例需要满足以下条件：
实例非[已停售的实例规格](user-guide/retired-instance-types.md)或抢占式实例。
若有未支付的订单，须先支付或作废未支付的订单。
未若为实例设置了自动释放时间，须先[关闭自动释放设置](user-guide/release-an-instance.md)。
实例处于运行中或已停止状态，若实例处于节省停机模式需先启动实例。
若ECS实例处于上述状态时下单成功，但是在支付完成前变更了实例状态，会导致支付和转换失败。需在还原下单时实例状态，并前往订单中心重新支付该订单。
什么类型的ECS实例支持节省停机模式？
支持节省停机模式的ECS实例需要满足以下条件：
网络类型为专有网络
计费方式为按量付费（包括抢占式实例）
实例规格族不包含本地存储
实例规格族不包含持久内存
更多信息，请参见[节省停机模式](user-guide/economical-mode.md)。
打开默认启用节省停机模式后，是否支持单台ECS实例关机时不释放计算资源和网络资源？
打开默认启用节省停机模式后，您在停止单台实例时仍然需要设置单台实例的停止模式，ECS实例不触发节省停机效果就不会释放计算资源和网络资源。
如果需要在短时间内停机再开机，建议您在调用[StopInstance](api-stopinstance.md)时将StoppedMode设置为KeepCharging，或者在控制台上停止ECS实例时选择普通停机模式。
在ECS实例操作系统内关机能否触发节省停机效果？
在实例操作系统内部停止实例不能触发节省停机效果。启用节省停机模式后，实例通过以下方式停机时才能触发节省停机效果。
ECS管理控制台。具体操作，请参见[停止实例](user-guide/stop-an-instance.md)。
通过阿里云CLI或SDK发起的API请求。更多信息，请参见[StopInstance](api-stopinstance.md)。
账号欠费自动停机。
本地盘实例是否支持自动触发节省停机效果？
本地盘实例不支持触发节省停机效果。
ECS实例触发节省停机效果后，为什么立刻启动时会报错OperationConflict？
ECS实例触发节省停机效果后，计算资源（CPU和内存）、固定公网IP会被回收。
如果需要在短时间内停机再开机，建议您在调用[StopInstance](api-stopinstance.md)时将StoppedMode设置为KeepCharging，或者在控制台上停止ECS实例时选择普通停机模式。
ECS实例触发节省停机效果后，为什么StartInstance时会报错OperationDenied.NoStock？
ECS实例触发节省停机效果后，计算资源会被回收。如果库存不足，启动ECS实例时会报错OperationDenied.NoStock。建议您稍后重试启动ECS实例。
启用了节省停机模式后，停机再开机时公网IP会变化，怎么保持公网IP不变？
ECS实例触发节省停机效果后，固定公网IP会被回收，下次启动时自动分配新的固定公网IP，因此会发生变化。
如果需要保持公网IP不变，您可以将ECS实例的固定公网IP转为弹性公网IP，因为ECS实例触发节省停机效果后不会释放弹性公网IP，可以保证公网IP不变。更多信息，请参见[固定公网](user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[转为弹性公网](user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)和[ConvertNatPublicIpToEip](api-convertnatpubliciptoeip.md)。
重要
固定公网IP转成弹性公网IP后，使用弹性公网IP访问公网会收取公网出网带宽费用、EIP配置费（满足特定条件时不收取）和EIP绑定费（满足特定条件时不收取）。具体收费细则，请参见[弹性公网](../../eip/documents/billing-overview.md)[IP](../../eip/documents/billing-overview.md)[计费概述](../../eip/documents/billing-overview.md)。
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
