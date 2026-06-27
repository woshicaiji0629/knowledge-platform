# 升级或降低ECS的实例规格、公网带宽或转换云盘计费方式-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/overview-of-instance-configuration-changes

# 升降配ECS实例概述
创建实例后，如果当前实例配置无法满足您的业务需求，您可以修改实例规格（vCPU和内存）、公网带宽配置和数据盘计费方式。本文介绍多种升降配的方式，您可以根据需要选择。
## 修改实例规格
一个实例规格已预定义vCPU和内存。修改实例规格时，您需要选择目标实例规格，不能单独修改vCPU或内存。
说明
修改实例规格前，您需要了解以下实例规格信息和变配支持情况，具体可修改的实例规格以变配页面显示为准。
实例规格：请参见[实例规格族](overview-of-instance-families.md)。
实例规格变配支持情况：请参见[规格变更限制与自检](instance-families-that-support-instance-type-changes.md)。
实例计费方式不同升降配的方式不同，您可以参见下表选择合适的方式。
| 实例计费方式 | 操作时段 | 何时生效 | 相关操作 |
| --- | --- | --- | --- |
| 包年包月实例 | 到期前 | 重启实例后生效 | [包年包月实例升配规格](upgrade-the-instance-types-of-subscription-instances.md) [包年包月实例降配规格](downgrade-the-instance-types-of-subscription-instances.md) |
| 到期前 15 日内 | 进入新的计费周期后，7 天内重启实例生效 | [包年包月实例续费降配](../downgrade-instance-configurations-during-renewal.md) |  |
| 到期后释放前 | 重启实例后生效 | [包年包月实例续费变配](../a-renewal-variable-2.md) |  |
| 按量付费实例 | 不涉及 | 重启实例后生效 | [更改按量付费实例规格](change-the-instance-type-of-a-pay-as-you-go-instance.md) |
## 修改公网带宽计费方式
根据使用的公网IP类型，您可以采用不同的方式修改公网带宽计费方式。
| 公网 IP 类型 | 何时生效 | 相关操作 |
| --- | --- | --- |
| 固定公网 IP | 立即生效 | [转换固定公网](../change-the-billing-method-for-network-usage-1.md) [IP](../change-the-billing-method-for-network-usage-1.md) [的带宽计费方式](../change-the-billing-method-for-network-usage-1.md) |
| 弹性公网 IP | 立即生效 | [变更](modify-the-bandwidth-of-an-eip.md) [EIP](modify-the-bandwidth-of-an-eip.md) [带宽](modify-the-bandwidth-of-an-eip.md) |
## 修改公网带宽峰值
根据实例的计费方式以及对带宽的需求不同，您可以采用不同的方式修改公网带宽。
重要
将公网带宽由非0值设置为0 Mbit/s，固定公网IP地址立即释放。
将公网带宽由0 Mbit/s设置为一个非零值：系统会为实例分配固定公网IP地址。
| 公网 IP 类型 | 适用范围 | 何时生效 | 相关文档 |
| --- | --- | --- | --- |
| 固定公网 IP | 包年包月实例修改基础公网带宽 | 立即生效 | [修改固定公网带宽包年包月实例修改带宽](modify-the-bandwidth-configurations.md) |
| 包年包月实例在续费的同时修改基础公网带宽 | 进入新的计费周期后生效 | [包年包月实例续费降配](../downgrade-instance-configurations-during-renewal.md) |  |
| 包年包月实例临时升级公网带宽 | 在设置的时间内生效 | [包年包月实例临时升级固定公网带宽（连续时间段）](temporary-bandwidth-upgrade.md) [包年包月实例临时升级固定公网带宽（周期性）](temporary-upgrade-bandwidth-on-a-daily-basis.md) |  |
| 按量付费实例修改基础公网带宽 | 立即生效 | [按量付费实例修改带宽](modify-the-bandwidth-configurations-of-pay-as-you-go-instances.md) |  |
| 弹性公网 IP | 包年包月实例或按量付费实例变配弹性公网带宽 | 立即生效 | [变更](modify-the-bandwidth-of-an-eip.md) [EIP](modify-the-bandwidth-of-an-eip.md) [带宽](modify-the-bandwidth-of-an-eip.md) |
## 修改数据盘计费方式
按量付费实例只可挂载按量付费数据盘，因此仅包年包月实例可以修改数据盘计费方式。
| 操作时段 | 何时生效 | 相关操作 |
| --- | --- | --- |
| 到期前 | 立即生效 | [转换云盘计费方式](../switch-the-billing-method-of-a-disk.md) |
| 到期前 15 日内或到期后释放前 | 立即生效 | [包年包月实例续费降配](../downgrade-instance-configurations-during-renewal.md) |
## 常见问题
升级ECS实例产生的费用怎么计算？
包年包月ECS实际升级实例规格和配置时会产生费用，具体费用为新配置的费用与升级前有效购买剩余费用的差额。
按量付费ECS实例升级后按照新的实例规格进行周期计费。
具体费用，以升级ECS实例规格和配置时，页面上显示的费用信息为准。您也可以在[费用与成本](https://billing-cost.console.aliyun.com/home)页面查询产生的费用详情。
升降配ECS实例会影响业务运行吗？
不一定。云平台仅保障实例层面的正常启动与资源交付。 请务必在变配前评估业务需求，确认目标规格（包含CPU、内存、网络及存储性能等）能够支撑您的业务运行，以免因资源不足导致业务无法启动。
升降配ECS实例对实例中的业务有什么影响吗？
升降配会导致业务短暂中断，请避开高峰期操作，并提前做好数据备份。
按量付费实例：需预先停止实例才能完成变配操作。
包年包月实例：变配后需重启实例生效。
若涉及以下情况，请务必在操作前通过快照或镜像备份数据，以防范风险：
有状态业务：请提前进行主从切换或配置维护窗口。
使用自定义镜像：请确认目标规格与当前系统兼容性。[检查操作系统兼容性](instance-families-that-support-instance-type-changes.md)
跨代升级（如7代升8代）：涉及NVMe设备名变更，请检查fstab或启动脚本是否存在冲突。[NVMe](nvme-protocol.md)[云盘的设备名称](nvme-protocol.md)
为什么降配时实例预计退款为0？
降配时实例预计退款显示为0，可能是因为您在购买实例时享受了折扣价，降配后的配置按官网原价计算，差价可能会小于等于0元，这时均会显示为0。更多信息，请参见[退订规则](https://help.aliyun.com/zh/user-center/cancel-subscription/#h2-22z-njp-iq0)。
升级订单能够直接取消升级配置，恢复到原先配置吗？
升级订单一旦生效，配置会提升，无法单独退订。如果要恢复原先配置，可以采用降配方式，届时将按照降配方式计费。
更多常见问题请参见[实例](instance-faq.md)[FAQ](instance-faq.md)。
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
