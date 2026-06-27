# 实例规格计费体系成本优化-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/instance-types

# 实例规格计费
本文介绍实例规格的计费组成和适用的计费方式。
## 费用组成
实例规格费用包括该实例下的计算资源（vCPU、内存、GPU）费用，[本地盘](user-guide/local-disks.md)（实例上不可卸载的存储设备）费用，以及[增强型](user-guide/enhanced-instance-families.md)实例的功能增强组件费用。
## 计费方式
实例规格支持包年包月、按量付费和抢占式实例三种计费方式。
| 计费方式 | [包年包月](subscription.md) | [按量付费](pay-as-you-go-1.md) | [抢占式实例（原竞价计费）](spot-instance.md) |
| --- | --- | --- | --- |
| 特点 | 预付费模式。预先支付 一周 或更长时间的费用，以获取价格折扣。 | 后付费模式。按秒计费，可随时创建和释放，单价高于包年包月。 | 后付费模式。价格随市场供需变化浮动，最低可为按量付费价格的 1 折。当市场价格高于您的出价或资源紧缺时，系统会自动回收实例。 |
| 适用场景 | 需要 7x24 小时运行的线上服务，如公司官网、App 后端、小程序。 业务稳定，对资源需求量可以提前预估。 希望预算固定，成本可控的长期项目。 | 业务需求不确定或变化大的场景，如新功能开发、产品测试。 季节性或周期性的业务高峰，如电商大促期间临时增加服务器。 短期的云计算学习或实验。 | 对中断不敏感的业务，例如电影渲染、科学计算、大数据分析等可以“断点续算”的任务。 |
| 计费公式 实例规格单价因地域而异，具体请参见 [云服务器](https://www.aliyun.com/price/product) [ECS](https://www.aliyun.com/price/product) [定价页](https://www.aliyun.com/price/product) 。 | 实例规格单价 × 计费时长。 | 实例规格单价 × 计费时长。 重要 按量付费计费方式下，实例规格计费项在实例释放的计费周期内存在最短计费时长： 1 vCPU 实例：实例使用不足 10 分钟按 10 分钟计费。 2 vCPU 实例：实例使用不足 5 分钟按 5 分钟计费。 4 vCPU 及以上实例：实例使用不足 2 分钟按 2 分钟计费。 详情请参见 [最短计费时长示例](instance-types.md) 。 | 购买时设定实例使用 1 小时： 计费时长≤1 小时： 成交时的市场价格×计费时长 计费时长>1 小时： 成交时的市场价格×1 小时+∑（各时段市场价格×各时段市场价格的计费时长） 购买时设定无确定使用时长： ∑（各时段市场价格×各时段市场价格的计费时长） 抢占式实例费用受市场成交价格影响，变动的时间周期不定，可参考 [计费示例](spot-instance.md) 核算实际费用。 |
| 计费时长 | 购买时长。 | 从实例创建开始计费，到实例释放结束计费，按秒计量。 即使实例未运行业务，实例规格仍会持续计费。如需在不释放实例的情况下停止计费，可开启 [节省停机模式](user-guide/economical-mode.md) 。 | 从实例创建开始计费，到实例释放结束计费，按秒计量。 |
## 计费示例
以在华东1（杭州）地域下创建ecs.g7.large规格实例为例。
示例价格仅供参考，实际价格以[云服务器](https://www.aliyun.com/price/product)[ECS](https://www.aliyun.com/price/product)[定价页](https://www.aliyun.com/price/product)为准。示例仅展示实例规格费用，不包含镜像、块存储、公网带宽、快照等费用。
| 计费方式 | 计费条件 | 计算过程 | 总费用（ 元 ） |
| --- | --- | --- | --- |
| 包年包月 | ecs.g7.large 实例的包年包月价格是 251.16 元/月 ，购买 1 个月。 | 251.16 元/月 × 1 月 | 251.16 |
| 按量付费 | ecs.g7.large 实例按量付费价格是 0.523 元/小时 ，在一个月（按 30 天算）里持续开机（未开启节省停机或释放）。 | 0.523 元/小时 × 24 小时/天 × 30 天 | 376.56 |
最短计费时长示例
按量付费计费方式下，阿里云会按照整点小时段（如2025年1月1日00:00:00至2025年1月1日01:00:00）统计计费时长，并产出一条消费明细，每个整点小时段即为一个计费周期。如果实例在释放的计费周期内的实际计费时长短于最短计费时长，则该计费周期内按照最短计费时长计算。
| 示例场景 | 实例创建及释放时间 | 按量付费计费时长 |
| --- | --- | --- |
| 同一计费周期创建并释放实例 | 创建：2025 年 1 月 1 日 00:01:00 释放：2025 年 1 月 1 日 00:02:00 | 实例的实际使用时长短于最短计费时长，按最短计费时长计费，计费时长如下： 1 vCPU 实例：10 分钟 2 vCPU 实例：5 分钟 4 vCPU 及以上实例：2 分钟 |
| 跨越计费周期创建并释放实例 | 创建：2025 年 1 月 1 日 00:59:00 释放：2025 年 1 月 1 日 02:00:20 | 在实例创建的计费周期至实例释放的前一个计费周期内，按实际使用时长计费。即 2025 年 1 月 1 日 00:00:00 至 2025 年 1 月 1 日 02:00:00 计费周期内： 1 vCPU 实例：1 小时 1 分钟 2 vCPU 实例：1 小时 1 分钟 4 vCPU 及以上实例：1 小时 1 分钟 在释放的计费周期内，实例的实际使用时长短于最短计费时长，按最短计费时长计费。即 2025 年 1 月 1 日 02:00:00 至 2025 年 1 月 1 日 03:00:00 计费周期内： 1 vCPU 实例：10 分钟 2 vCPU 实例：5 分钟 4 vCPU 及以上实例：2 分钟 |
## 转换计费方式
包年包月和按量付费实例支持相互转换计费方式。抢占式实例不支持转换。转换计费方式可能产生退费，详情请参见[包年包月转按量付费](change-the-billing-method-of-an-instance-from-subscription-to-pay-as-you-go-1.md)及[按量付费转包年包月](change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md)。
## 成本优化
若当前计费方式不再符合业务需求，可以尝试[转换计费方式](instance-types.md)，此外还可通过以下方式优化ECS实例的实例规格费用：
### 释放或退订实例
当确认不再需要某个包年包月实例提供服务时，可以申请退订，阿里云将基于退订规则回收资源并退还相应的款项。退订后资源释放时间与退款规则请参见[退订说明](refund-instructions.md)。
当确认不再需要某个按量付费或抢占式实例提供服务时，可以主动释放该实例。释放后，实例规格不会再产生额外费用，释放实例的操作指引请参见[释放实例](user-guide/release-an-instance.md)。
重要
请注意，释放后的实例数据将永久删除且无法找回，如果仍有数据需要保存，建议在释放之前先创建快照备份数据（会产生[快照费用](snapshots-1.md)）。具体操作请参见[手动创建单个快照](user-guide/create-a-snapshot.md)。
### 开启节省停机模式
仅按量付费实例与抢占式实例支持开启节省停机模式。
普通停机模式下，按量付费实例即使停止运行仍会正常收取实例规格费用。开启[节省停机模式](user-guide/economical-mode.md)后，实例规格和镜像许可证费用将停止计费，但云盘（系统盘和数据盘）、弹性公网IP、快照等资源将继续收费。
### 降低实例规格配置
如果通过[查看实例监控信息](user-guide/view-the-monitoring-information-of-an-ecs-instance.md)判断当前实例规格的性能超出业务需求，可以通过降低实例配置节省成本。
包年包月实例可通过[更改包年包月实例规格](user-guide/change-the-instance-types-of-subscription-instances.md)或[续费降配](downgrade-instance-configurations-during-renewal.md)功能降配实例规格。
按量付费实例可通过[更改按量付费实例规格](user-guide/change-the-instance-type-of-a-pay-as-you-go-instance.md)降配实例规格。
### 使用折扣权益
可以通过以下折扣权益抵扣按量付费计费实例产生的实例规格费用：
[节省计划](savings-plans.md)：类似消费满减承诺，通过承诺每小时消费一定的金额（如每小时消费1元）并预先支付承诺消费费用，即可享受折扣。灵活性高，可抵扣多种实例规格。
[预留实例券](reserved-instances.md)：类似指定商品的会员卡，购买针对特定实例规格族（如ecs.g8i）的特定操作系统下的抵扣券，可以在符合条件的按量付费实例产生费用时进行抵扣。
### 组合使用多种计费方式
当有多台ECS实例时，可通过搭配多种计费方式，更好地优化实例使用成本。推荐的计费方式组合如下图所示。
## 账单查询
可参考[账单查询](view-billing-details.md)步骤查看账单，实例规格在账单详情中的计费项名称如下：
按量付费实例及抢占式实例为云服务器配置。
包年包月实例为实例。
## 常见问题
ECS服务器的总费用只包括实例规格吗？
不是的。一台可用的ECS服务器通常在购买时还包括以下几个部分的费用，您可以在购买实例时查看选购实例的详细计费项，以判断后续产生的费用。
云盘（块存储）：包括系统盘和数据盘的存储及配置费用；本地盘费用已包含在实例规格费用中。
公网带宽：如果您需要服务器能被外网访问，则需配置公网带宽收取出网带宽费用。
镜像：根据镜像类型及使用情况收费，例如使用部分公共镜像、存储自定义镜像或使用云市场镜像等。
若在购买时配置了自动快照策略或购买实例后手动创建了实例快照，则创建快照、复制快照时也会收取快照费用。
如何选择用于备案域名（ICP）的服务器计费方式？
在中国内地，如果您需要为网站进行ICP备案，通常要求云服务器的购买时长不少于3个月。按量付费实例及抢占式实例不支持用于域名备案。
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
