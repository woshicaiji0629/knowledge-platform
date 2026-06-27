# ECS如何计费及包年包月和按量付费方式对比-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/overview-of-billing-methods

# 计费方式概述
对于不同的ECS资源，您可以根据需要选择合适的计费方式。本文汇总了各类计费方式，给出了包年包月和按量付费这两种主要计费方式的对比说明，并介绍抢占式实例、节省计划等优惠的计费方式。
## 基础计费方式
一台ECS实例包括计算资源（vCPU和内存）、镜像、块存储等资源，计费方式主要分为包年包月、按量付费和抢占式实例，各计费方式适用的资源和场景如下表所示。
| 计费方式 | 适用资源 | 说明 | 计费规则 |
| --- | --- | --- | --- |
| 包年包月 | 计算资源（vCPU 和内存） 镜像 云盘 公网带宽 | 一种预付费模式，即先付费再使用。一般适用于固定的 7*24 服务，例如 Web 服务。您需要先结清包年包月资源账单，才能开始使用包年包月资源。 | [包年包月](subscription.md) |
| 按量付费 | 计算资源（vCPU 和内存） 镜像 云盘 公网带宽 快照 | 一种后付费模式，即先使用再付费。一般适用于有爆发业务量的应用或服务，例如临时扩展、临时测试、科学计算。您可以先开通并使用按量付费资源，系统在每个结算周期生成账单并从账户中扣除相应费用。 | [按量付费](pay-as-you-go-1.md) |
| 抢占式实例 | 计算资源（vCPU 和内存） | 一种先使用后付费的按需实例，相对于按量付费实例价格有一定的折扣，价格随供求波动，按实际使用时长进行收费。 | [抢占式实例](spot-instance.md) |
包年包月实例、按量付费实例和抢占式实例支持的功能点存在差别，下表列出了具体功能区别。
| 功能点 | 包年包月 | 按量付费 | 抢占式实例 |
| --- | --- | --- | --- |
| 释放实例 | 到期前，您需要在 费用与成本 的 费用 > 订购订单 > 资源退订 页面发起退订申请，或者将实例转换为按量付费实例后再释放。 到期后，如果未在指定时间内续费，实例将自动释放。 | 您随时可以释放实例。 请尽快释放不再使用的按量付费实例，否则 ECS 资源会持续扣费，直至因账号欠费停机而自动释放。 | 您随时可以释放实例，但系统也可能因为市场价格变化或实例规格库存不足而自动释放实例。 |
| 变更实例规格 | 支持。 | 支持。 | 不支持。 |
| 变更带宽配置 | 支持。 | 支持。 | 不支持。 |
| 转换计费方式 | 支持。 | 支持。 | 不支持。 |
| 使用云市场镜像的包年包月镜像 | 支持。 | 不支持。 | 不支持。 |
| 中国内地地域的 ECS 实例备案域名（ICP） | 支持。 购买时长不少于 3 个月的包年包月实例可以用于备案。 说明 需购买公网带宽。 | 不支持。 | 不支持。 |
| 通过 API 创建实例 | 支持。 | 支持。 | 支持。 |
| 免费使用云安全中心免费版、基础云监控 | 支持。 | 支持。 | 支持。 |
## 优化成本的计费方式组合
除包年包月、按量付费和抢占式实例外，针对不同的ECS资源还提供了一些优惠的计费方式可以组合使用，以优化资源使用成本。您可以根据实际业务情况按需购买。
| 计费方式 | 适用资源 | 说明 | 相关文档 |
| --- | --- | --- | --- |
| 预留实例券 | 计算资源（vCPU 和内存） 镜像 | 一种抵扣券，可以抵扣按量付费实例的账单。 | [什么是预留实例券](reserved-instances.md) |
| 节省计划 | 计算资源（vCPU 和内存） 系统盘 固定公网带宽 | 一种折扣权益计划，通过承诺一定的消费金额来获取较低的按量价格折扣，并按折扣价格计算抵扣按量付费实例的账单。 | [什么是节省计划](savings-plans.md) |
| 存储容量单位包 | 云盘 快照 | 一种预付费的存储容量资源包，可以抵扣多种不同类型云存储产品的按量付费账单等。 | [存储容量单位包](storage-capacity-units-1.md) [SCU](storage-capacity-units-1.md) |
| OSS 存储包 | 快照 | 一种预付费的资源包，可以抵扣快照的存储费用。 | [OSS](oss-storage-bag.md) [资源包](oss-storage-bag.md) |
| 流量包 | 公网带宽 | 一款流量套餐产品，可以自动抵扣按流量计费实例产生的 IPv4 流量费用。 | [共享流量包](https://help.aliyun.com/zh/dtp/) |
## 转换计费方式
在购买ECS资源后，如果发现当前计费方式无法满足业务需求，您可以转换计费方式。支持转换的ECS资源如下表所示。
| ECS 资源 | 转换说明 | 相关文档 |
| --- | --- | --- |
| 实例 | 转换实例计费方式会同时转换计算资源（vCPU 和内存）、系统盘等资源的计费方式。 将实例的计费方式从包年包月转为按量付费，可以回收部分成本，更加灵活地使用 ECS。 说明 阿里云会根据您的云服务器使用情况，通过计算动态得出您的实例的计费方式是否支持转换操作。您可以前往云服务器控制台查看是否存在相应的操作入口，如果不存在，则说明不支持。 将实例的计费方式从按量付费转为包年包月，可以享受一定程度的价格优惠。 | [包年包月转按量付费](change-the-billing-method-of-an-instance-from-subscription-to-pay-as-you-go-1.md) [按量付费转包年包月](change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md) |
| 云盘 | 包年包月实例上挂载的数据盘可以单独转换计费方式。 实例系统盘以及按量付费实例上挂载的数据盘需随实例一起转换计费方式。 | [转换云盘计费方式](switch-the-billing-method-of-a-disk.md) [包年包月转按量付费](change-the-billing-method-of-an-instance-from-subscription-to-pay-as-you-go-1.md) [按量付费转包年包月](change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md) |
| 公网带宽 | 使用固定公网 IP 的实例，可以通过升降配功能转换带宽的计费方式。 | [转换固定公网](change-the-billing-method-for-network-usage-1.md) [IP](change-the-billing-method-for-network-usage-1.md) [的带宽计费方式](change-the-billing-method-for-network-usage-1.md) |
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
