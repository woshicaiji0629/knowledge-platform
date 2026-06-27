# ECS公网带宽计费-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/public-bandwidth

# 公网带宽计费
配置固定公网IP后，阿里云仅对出方向流量计费，入方向不计费。出方向指数据流出 ECS 服务器的方向，如ECS对外提供访问，或响应用户的文件下载请求。
本文仅介绍固定公网IPv4的两种计费模式。如果实例通过其他方式（如IPv6，EIP，NAT等）访问公网，请查看[对应产品的计费规则](public-bandwidth.md)。
## 选择计费模式
购买ECS实例时，若为ECS实例勾选分配公网IPv4地址，系统会自动分配固定公网IP，实现实例与公网通信。固定公网IP的支持按固定带宽计费和按使用流量计费。
| 计费模式 | 计费原理 | 推荐使用场景 |
| --- | --- | --- |
| 按固定带宽 | 按 ECS 实例的计费时长计算时间用量，根据配置带宽值的单位时间价格计算费用。 | 业务流量稳定，对带宽稳定性有较高要求。 |
| 按使用流量 | 按 ECS 实例运行期间实际产生的出网流量计算流量用量，根据出网流量的单位价格计算费用。 | 业务流量不确定，流量时高时低，或有突发。 |
## 计费规则
### 按固定带宽计费
计费公式
| 包年包月实例 | 按量付费实例、抢占式实例 |
| --- | --- |
|  |  |
如果实例地域为中国香港，且有需要香港本地、香港和海外之间的互联网访问需求，可以选择BGP（多线）精品优化回国时延。线路类型选择为BGP（多线）精品时，每1Mbps固定带宽单价为232元/月。
使用时长
关联实例为包年包月计费：使用时长为实例购买时长。若在实例购买后为实例开通按固定带宽计费的固定公网IP，则使用时长为实例剩余到期时长。
关联实例为按量付费计费：使用时长同实例的实际使用时长，按秒计算。若使用时长不足最低阈值时按最短计费时长计算。
重要
当实例为按量付费计费方式时，若使用时长较短，阿里云会按照实例规格对应的最短计费时长进行计算：
1 vCPU规格实例：若单个计费周期内使用时间不足10分钟，按10分钟计算。
2 vCPU规格实例：若单个计费周期内使用时间不足5分钟，按5分钟计算。
4 vCPU及以上规格实例：若单个计费周期内使用时间不足2分钟，按2分钟计算。
计费示例
假设您的公司需要为宣传某个大型活动搭建一个官方网站，网站需要运行30天。您计划将部署网站的ECS实例开通在华东1（杭州）地域，并希望使用固定带宽计费模式。经过业务评估预计带宽值需要设置为10Mbps。参考计算公式，此时实例按照包年包月方式计费、按量付费方式及抢占式实例计费的公网带宽费用计算方式如下：
说明
价格仅为示例，实际计算时请以云服务器ECS定价页面的价格为准。
| 实例计费方式 | 配置参数及单价 | 费用计算 |
| --- | --- | --- |
| 包年包月 | 带宽值：10Mbps 使用时长：1 个月 单位时长带宽值价格： 525 元/月 参考 [如何计算单位时长不同带宽值的单价](public-bandwidth.md) | 公网带宽费用为 525 * 1 = 525 元 |
| 按量付费、抢占式实例 | 带宽值：10Mbps 使用时长：1 个月（720 小时） 单位时长带宽值价格： 1.5625 元/小时 参考 [如何计算单位时长不同带宽值的单价](public-bandwidth.md) | 公网带宽费用为 1.5625 * 720 = 1125 元 |
### 按使用流量计费
ECS实例为按量付费、包年包月、抢占式实例计费方式时，按使用流量计费均按照实例实际使用的出网流量后付费。可以通过设置带宽峰值，限制一定时间内出网流量的使用上限。
重要
按使用流量计费模式下的带宽峰值仅为上限限制，不作为业务承诺指标。当网络资源繁忙出现争抢时，实际带宽可能会受限。如果对带宽稳定性有高要求，请选择按固定带宽计费模式。
中国香港地域下的BGP精品（多线）不支持按使用流量计费。
包年包月实例选择该计费模式会按计费周期产生按量费用，您需要关注账户余额避免欠费影响业务。
计费公式
| 公式参数 | 参数说明 |
| --- | --- |
| 出网流量 | ECS 使用时实际的出网流量，可按照计费周期维度 [查看云服务器](billing-faq.md) [ECS](billing-faq.md) [公网流量的使用量](billing-faq.md) ，精确到 Byte，转换为 GB 单位计算时会取整，请以账单最终显示为准。 |
| 每 GB 流量单价 | 不同地域的流量单价不同，您可以参见 [云服务器](https://www.aliyun.com/price/product#/ecs/detail) [ECS](https://www.aliyun.com/price/product#/ecs/detail) [定价](https://www.aliyun.com/price/product#/ecs/detail) 中的 带宽价格 页签。 |
计费示例
假设您的公司需要为宣传某个短期活动搭建了一台ECS，并在活动结束后被释放或停止续费。部署网站的ECS实例开通在华东1（杭州）地域，公司的相关负责人员查询到实例从创建至释放，总计使用了15.5GB出网流量。参考计算公式，此时实例的公网带宽费用计算方式如下：
说明
价格仅为示例，实际计算时请以云服务器ECS定价页面的价格为准。
| 参数配置及单价 | 费用计算 |
| --- | --- |
| 出网流量：15.5GB 每 GB 流量单价： 0.8 元/GB | 公网带宽费用为 15.5 * 0.8 = 12.4 元 |
## 成本优化
按使用流量计费时，可以选择购买或开通其他产品优惠使用流量。
按固定带宽计费时，定期[监控网络带宽](user-guide/network-bandwidth.md)，根据业务情况评估并灵活调整带宽值是节省成本的关键方法。
| 计费模式 | 成本优化方案 | 方案优势及适用场景 |
| --- | --- | --- |
| 按使用流量计费 | 开通 [云数据传输](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt) [CDT](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt) 升级 CDT 后，查询产品账单时请产品名称为 云数据传输 。 | 可以获得一定的免费流量额度。 采用阶梯计费，使用流量越多，单价越优惠。 |
| [购买共享流量包](https://help.aliyun.com/zh/dtp/product-overview/what-is-a-data-transfer-plan) | 可以以较低的流量单价结算多实例、多地域、多产品的流量费用。 |  |
| 按固定带宽计费 | 闲置带宽较多时 [降低公网带宽配置](user-guide/modify-the-bandwidth-configurations.md) | 业务的实际带宽峰值长期远低于您购买的带宽值，降低带宽规格可以直接减少固定的带宽费用，避免为大量闲置的带宽资源付费。 |
| 带宽升配需求时采用临时升配替代长期升配 该方案当前仅适用于包年包月实例。 | 在带宽升配需求可预期时间时，可以通过 [临时升级固定公网带宽](user-guide/temporary-bandwidth-upgrade.md) ，及时帮临时升配后回落至常态的带宽值，避免为大量闲置的带宽资源付费。 如果需要周期性重复临时升级操作，可以通过 [自动化运维](user-guide/temporary-upgrade-bandwidth-on-a-daily-basis.md) [OOS](user-guide/temporary-upgrade-bandwidth-on-a-daily-basis.md) [便捷实现](user-guide/temporary-upgrade-bandwidth-on-a-daily-basis.md) 。 |  |
### 转换计费模式
建议在业务变化后，定期[监控网络带宽](user-guide/network-bandwidth.md)的情况。您可以结合[推荐使用场景](public-bandwidth.md)，重新评估当前的计费模式是否仍然适用于您的业务场景。若评估后判断需要更换计费方式，可以参考[转换固定公网](change-the-billing-method-for-network-usage-1.md)[IP](change-the-billing-method-for-network-usage-1.md)[的带宽计费方式](change-the-billing-method-for-network-usage-1.md)操作。
## 查询账单和用量
### 查询明细账单
您可以在用户中心查看固定公网带宽的相关的费用账单和消费明细，以了解消费情况。
登录[费用与成本控制台](https://usercenter2.aliyun.com/home)。
在左侧导航栏，选择账单>账单详情。
选择相应的页签，筛选产品名称为云服务器 ECS，查看产生的公网流量账单。
如果您已升级CDT，请筛选产品名称为云数据传输。
### 查询按使用流量计费模式下的出网流量
登录[费用与成本控制台](https://usercenter2.aliyun.com/home)。
在左侧导航栏，选择账单>账单详情后，单击查看用量明细。
选择需要查询的使用时间（当前仅支持查询导出单个自然月内的数据），设置商品名称为云服务器 ECS-按量付费或云服务器 ECS-包年包月，计费项名称为流出流量。
单击导出CSV。在打开的导出记录页面中，等待导出文件的状态变更为导出成功后，单击操作列的下载。待下载完成后，可以通过下载的CSV文件，查看云服务器ECS公网流量的使用量。
当前仅支持查询ECS实例开通固定公网IP按流量计费模式的出网流量查询，不支持按固定带宽计费模式下的实例按此方式查询出网流量。
## 退订固定公网带宽
不需要使用固定公网带宽时，可以通过将固定公网带宽值调整为0 Mbit/s的方式，实现固定公网IP的释放，进而实现实例公网带宽停止计费，操作步骤请参见[修改固定公网带宽](user-guide/modify-the-bandwidth-configurations.md)。
在退订包年包月实例的按固定带宽计费的带宽时，会涉及到退订金额，退订金额仅指用户以现金方式支付的订单款项，不包含用户通过代金券、优惠券抵扣的部分。退款的具体金额计算请参见[退订规则](https://help.aliyun.com/zh/user-center/cancel-subscription/#h2-22z-njp-iq0)。
## 欠费影响说明
如果阿里云账号的可用额度（含阿里云账户余额，代金券与信控额度）小于待结算的账单，账号会进入欠费状态。
账号欠费后：
包年包月实例：仍可以使用已有的包年包月ECS资源，但无法执行涉及费用的操作，例如新购、升级或续费实例等。
按量付费实例：欠费后15天内保留固定公网IP地址，如果实例停机前已默认启用节省停机模式，则实例欠费停机后，公网IP地址可能被回收，重启后，公网IP地址可能变更。欠费15天后释放固定公网IP地址。
账号欠费会导致按量付费ECS实例停机，请及时结清欠费账单，避免对您的服务造成影响。具体操作，请参见[在线充值](https://help.aliyun.com/zh/user-center/use-alipay-online-banking-to-recharge-online)。
## 常见问题
如果使用IPv6、EIP、NAT网关方式访问公网，怎么查看计费规则？
使用IPv6地址：请参见[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/)[计费说明](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/)。
绑定了弹性公网IP（EIP）：请参见[EIP](../../eip/documents/billing-overview.md)[计费概述](../../eip/documents/billing-overview.md)。
使用NAT网关：请参见[NAT](../../nat-gateway/documents/nat-gateway-billing.md)[网关计费说明](../../nat-gateway/documents/nat-gateway-billing.md)。
开通公网后，哪些常见场景消耗的流量是不计费的？
ECS通过内网地址访问同VPC的RDS/SLB/OSS产品或传输数据、通过公网上传文件到ECS服务器等。
重要
通过公网地址从阿里云相关产品下载文件到ECS，可能会在相关产品侧产生流量费用，请仔细阅读相关计费说明。
包年包月实例开通固定公网IP为什么会有额外费用？
当包年包月实例开通按流量计费的固定公网IP时，可能会在ECS实例使用过程中根据实际使用的出网流量产生后付费费用。具体计费情况如下：
包年包月实例：购买实例时无需对固定公网IP配置额外预付费，但使用过程中会在实际产生出网流量的计费周期内，产生相关费用。
按量付费、抢占式实例：与实例其他配置费用一起按计费周期产生账单，在实际产生出网流量的计费周期内，产生相关费用。
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
