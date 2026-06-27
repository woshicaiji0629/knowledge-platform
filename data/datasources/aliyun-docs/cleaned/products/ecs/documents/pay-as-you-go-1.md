# 什么是按量付费计费方式-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/pay-as-you-go-1

# 按量付费
按量付费是一种后付费计费方式，按实例资源的保留时长或实际流量消耗计费。与包年包月相比，该模式更加灵活，支持在业务结束后立即释放资源并停止计费，有效减少资源闲置成本。
## 适用场景
业务波动或爆发，资源使用有临时性和突发性，无法进行准确预测。
资源需随时开通，随时删除。
常见场景：临时扩展、测试、电商抢购等。
## 计费规则
按量付费主要根据两种模式对资源进行计费：
按使用时长计费：根据资源的保留时间长度计费（适用于实例规格、云盘等）。
按使用量计费：根据资源的实际使用总量计费（适用于按使用流量计费模式下的公网带宽）。
当您购买一台按量付费ECS实例，选定实例规格，并配置系统盘后额外配置了付费镜像、数据盘以及按使用流量计费的公网带宽。在购买页面查看费用明细，您会看到类似下表的费用明细：
本场景仅作计费项和计费规则说明示例，实际计费项和价格请以您购买时显示为准。如果您在购买时显示的计费项与实例中不同，请根据您的实际配置参照表格中的计费项与计费规则。
| 实例 ：即 实例规格 费用，包括该实例下的计算资源（vCPU、内存、GPU）费用， [本地盘](user-guide/local-disks.md) （实例上不可卸载的存储设备）费用，以及 [增强型](user-guide/enhanced-instance-families.md) 实例的功能增强组件费用。 系统盘：云盘（系统盘） 容量费用。 数据盘：云盘（数据盘） 容量费用。 镜像费用：镜像 许可证费用 ， 基于付费镜像的市场价格。 公网流量费用：公网带宽（按使用流量） 费用。 |
| --- |
除示例中的计费项外，按量付费的实例可能会基于您的使用配置产生其他按量费用，按量付费下计费项的详细计费规则如下表所示：
### 按使用时长计费
| 计费项 | 主要计费公式 | 计费时长 |
| --- | --- | --- |
| [实例规格](instance-types.md) | 实例规格费用 = 实例规格单价 × 计费时长 同一实例规格在不同地域的价格可能不同，具体请参见 [云服务器](https://www.aliyun.com/price/product) [ECS](https://www.aliyun.com/price/product) [定价页](https://www.aliyun.com/price/product) 。 | 按秒计量，从实例创建开始，到实例释放时终止。 即使实例未运行业务，实例规格仍会在实例释放前持续计费。 |
| [云盘（系统盘/数据盘）](block-storage-devices.md) | 云盘容量费用 = 云盘单价 × 云盘容量× 计费时长 云盘容量为您在购买时的云盘配置容量，同一类型的 云盘 在不同地域的价格均可能不同，具体请参见 [块存储价格](https://www.aliyun.com/price/product#/disk/detail) ESSD AutoPL 云盘 、ESSD PL-X 云盘 若配置预配置性能、开启性能突发会产生额外费用，详见 [块存储计费](block-storage-devices.md) 。 | 按秒计量，从实例创建完成开始，至实例释放时终止。 |
| [镜像](images.md) | 镜像操作系统许可证费用 = 镜像单价 × 计费时长 公共镜像价格请参见 [镜像计费](images.md) 。 | 按秒计量。从使用付费镜像的实例创建完成开始计费，到实例释放或者更换为其他操作系统时结束计费。 |
| [公网带宽（按固定带宽）](public-bandwidth.md) | 公网带宽费用（按固定带宽） = 固定带宽单价 × 固定带宽大小 × 计费时长 不同地域的公网带宽价格请参见 [云服务器](https://www.aliyun.com/price/product#/ecs/detail) [ECS](https://www.aliyun.com/price/product#/ecs/detail) [定价](https://www.aliyun.com/price/product#/ecs/detail) 中的 带宽价格 页签。 | 按秒计量，从实例创建完成开始，至实例释放时或关闭公网带宽（带宽值为 0）后终止计费。 若实例创建后更换镜像，则更换后旧镜像终止计费，新镜像开始计费。 |
| [快照](snapshots-1.md) | 快照存储费用 = 快照单价 × 快照容量 × 计费时长 阿里云根据您使用的快照类型以及对应的快照容量，按每个地域单独结算快照费用，请参见 [ECS](https://www.aliyun.com/price/product#/disk/detail) [定价详情页](https://www.aliyun.com/price/product#/disk/detail) 中 快照服务价格 页签。 | 按小时计量，从快照创建完成开始计费，到快照删除后终止计费。 |
最短计费时长
按量付费计费方式下，阿里云会按照整点小时段（如2025年1月1日00:00:00至2025年1月1日01:00:00）统计计费时长，并产出一条消费明细，每个整点小时段即为一个计费周期。如果实例在释放的计费周期内实例规格、云盘容量、公网带宽（按固定带宽）、快照的实际使用时长短于最短计费时长，则该计费周期内按照最短计费时长计算。
实例规格、云盘容量、公网带宽（按固定带宽）最短计费时长：
1 vCPU实例：不足10分钟按10分钟计费。
2 vCPU实例：不足5分钟按5分钟计费。
4 vCPU及以上实例：不足2分钟按2分钟计费。
快照最短计费时长：不足1小时按1小时计费。
计算示例参见[如何计算最短计费时长？](pay-as-you-go-1.md)
### 按使用量计费
| 计费项 | 按量付费计费公式 | 计费单价 | 流量计量规则 |
| --- | --- | --- | --- |
| [公网带宽（按使用流量）](public-bandwidth.md) | 公网带宽费用（按使用流量） = 出网流量单价 × 流量 | 线性计费，不同地域的公网带宽价格请参见 [云服务器](https://www.aliyun.com/price/product#/ecs/detail) [ECS](https://www.aliyun.com/price/product#/ecs/detail) [定价](https://www.aliyun.com/price/product#/ecs/detail) 中的 带宽价格 页签。 | 按 Byte 计量，实际使用流量转化为 GB 并向下取整保留 6 位小数。 |
## 账单生成与欠费说明
### 账单与结算流程
资源释放前，阿里云将按量实时记录您的资源使用情况。您可在[账单详情](https://billing-cost.console.aliyun.com/finance/expense-report/expense-detail-by-instance)查看在阿里云上按照整点小时产出消费明细信息。当月度账单生成后，您可以进行用量及价格核对，还原费用计算过程。
账单详细数据可能会延迟更新，使用介绍及字段说明请参见[账单使用说明](https://help.aliyun.com/zh/user-center/instructions-for-using-the-bill)。
### 欠费说明
如果您账号的可用额度（含阿里云账户余额和代金券）小于待结算的账单，账号会进入欠费状态。欠费后，您将无法创建新的按量付费资源，且现有实例将面临停机和释放风险。系统会提醒或通知您，请及时结清欠费账单，避免对您的服务造成影响。
欠费后的资源状态变化，请参见[欠费说明](overdue-payments.md)。
## 优化使用成本
### 及时释放闲置资源
按量付费的ECS实例，在未开启节省停机的情况下，主动普通停机仍会正常收取费用。当您确认不再需要某个实例提供服务时，您可以释放该实例，按量付费实例释放后不再会产生额外费用，释放实例的操作指引请参见[释放实例](user-guide/release-an-instance.md)。
重要
请注意，释放后的实例数据将永久删除且无法找回，如果仍有数据需要保存，建议您在释放之前先创建快照备份数据。具体操作请参见[手动创建单个快照](user-guide/create-a-snapshot.md)。
### 启用节省停机模式
下表展示了实例在运行中、普通停机和节省停机三种状态下，各项资源的计费情况。若暂时无需使用实例，可[开启节省停机模式](user-guide/economical-mode.md)，保留实例数据的同时节省部分资源使用成本。实例开启节省停机后，实例规格、固定公网带宽和镜像许可证费用将暂停计费。但云盘、弹性公网IP等资源仍会继续收费。
| 计费项 | 运行中 | 普通停机 | 节省停机模式 |
| --- | --- | --- | --- |
| 实例规格 | 计费 | 计费 | 不计费 |
| 云盘（系统盘及数据盘）容量 | 计费 | 计费 | 计费 |
| 公网带宽（按固定带宽） | 计费 | 计费 | 不计费 |
| 公网带宽（按使用流量） | 计费 按实际使用流量计费 | 不计费 不产生流量及费用 | 不计费 不产生流量及费用 |
| 镜像操作系统许可证 | 计费 | 计费 | 不计费 |
重要
使用节省停机模式可能会在再次启动实例时产生启动失败、公网IP变更、突发性能实例CPU积分清零等风险，详细的风险说明请参见[节省停机模式风险提示](user-guide/economical-mode.md)。
### 使用折扣权益
节省计划：承诺在一定周期内消费固定金额，以换取按量付费资源的折扣。适合用量稳定的场景。详情请参见[什么是节省计划](savings-plans.md)。
预留实例券：预留特定地域和实例规格的计算资源容量，以获得折扣。适合实例规格和地域固定的场景。详情请参见[什么是预留实例券](reserved-instances.md)。
### 转换计费方式
按量付费转包年包月：对于需要长期稳定运行的实例，将其转换为包年包月可享受更大的价格优惠。具体操作请参见[按量付费转包年包月](change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md)。
包年包月转按量付费：当一个长期任务结束，但实例仍需临时使用时，可将其转换为按量付费，以更灵活地控制成本。具体操作请参见[包年包月转按量付费](change-the-billing-method-of-an-instance-from-subscription-to-pay-as-you-go-1.md)。
### 设置费用监控与告警
对已订购的按量付费ECS实例设置消费提醒，可减少因意外的高额消费导致预算超支的情况，操作如下：
在[消息中心](https://notifications2.console.aliyun.com/subscribeMsg)设置账户资金消息的接收人。
登录[费用与成本控制台](https://billing-cost.console.aliyun.com/home)，选择账单 >[账单概览](https://billing-cost.console.aliyun.com/finance/month-bill/account)。
在账单概览页面右上角，点击设置高额消费预警。
在设置页面，选择预警商品，输入预警阈值，并点击增加按钮来增加预警。
详见[设置高额消费预警](https://help.aliyun.com/zh/user-center/set-high-consumption-alert)。
### 组合使用多种计费方式
当有多台ECS实例时，可通过搭配多种计费方式，更好地优化实例使用成本。推荐的计费方式组合如下图所示。
## 常见问题
如何计算最短计费时长？
按量付费计费方式下，阿里云会按照整点小时段（如2025年1月1日00:00:00至2025年1月1日01:00:00）统计计费时长，并产出一条消费明细，每个整点小时段即为一个计费周期。如果实例在释放的计费周期内的实际计费时长短于最短计费时长，则在该计费周期内按照最短计费时长计算。
以下示例实例仅配置了云盘、公网带宽（按固定带宽），在实例释放前未变更实例配置。
| 示例场景 | 实例创建及释放时间 | 按量付费计费时长 |
| --- | --- | --- |
| 同一计费周期创建并释放实例 | 创建：2025 年 1 月 1 日 00:01:00 释放：2025 年 1 月 1 日 00:02:00 | 实例的实际使用时长短于最短计费时长，按最短计费时长计费，计费时长如下： 1 vCPU 实例：10 分钟 2 vCPU 实例：5 分钟 4 vCPU 及以上实例：2 分钟 |
| 跨越计费周期创建并释放实例 | 创建：2025 年 1 月 1 日 00:59:00 释放：2025 年 1 月 1 日 02:00:20 | 在实例创建的计费周期至实例释放的前一个计费周期内，按实际使用时长计费。即 2025 年 1 月 1 日 00:00:00 至 2025 年 1 月 1 日 02:00:00 计费周期内： 1 vCPU 实例：1 小时 1 分钟 2 vCPU 实例：1 小时 1 分钟 4 vCPU 及以上实例：1 小时 1 分钟 在释放的计费周期内，实例的实际使用时长短于最短计费时长，按最短计费时长计费。即 2025 年 1 月 1 日 02:00:00 至 2025 年 1 月 1 日 03:00:00 计费周期内： 1 vCPU 实例：10 分钟 2 vCPU 实例：5 分钟 4 vCPU 及以上实例：2 分钟 |
按量付费ECS实例停机后，会产生费用吗？
ECS实例存在两种停机状态，欠费停机不产生费用，而主动停机是否计费则依据实例配置和网络类型有所不同，具体如下：
欠费停机：指实例因账号欠费而自动停止服务，处于欠费停机状态的实例不计费。账号欠费后，实例不会一直处于欠费停机状态，具体资源状态变化，请参见[欠费说明](overdue-payments.md)。
主动停机：指在实例正常运行期间，您通过ECS管理控制台或StopInstance接口，使实例进入已停止状态。此时，实例的计费情况取决于实例的网络类型和是否启用了节省停机模式。
启用节省停机模式：实例处于已停止状态时实例的计算资源（即vCPU、GPU和内存）、操作系统许可证以及固定公网IP地址不再计费，但云盘、EIP等其它资源仍然正常计费。实例再次启动后开始恢复计算资源、操作系统许可证以及固定公网IP地址的计费。更多信息，请参见[节省停机模式](user-guide/economical-mode.md)。
未启用节省停机模式：即使实例停止，也会继续按照按量付费计费规则计费。
按量付费实例能使用代金券结算吗？
支持。请确保购买按量付费产品的代金券在有效期内，且适用场景为通用。
开通按量付费ECS实例后，对实例配置进行变更，账单会如何变化？
会分段计费。例如，您在11:00:00 创建了一台ecs.g5.large实例，并在11:30升配为ecs.g5.4xlarge。那么在11:30:00这个小时的账单中，会包含两条记录：
一条是ecs.g5.large在11:00:00 - 11:30:00期间的费用。
另一条是ecs.g5.4xlarge在11:30:00 - 12:00:00期间的费用。
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
