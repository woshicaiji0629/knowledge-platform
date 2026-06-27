# 欠费对ECS资源的影响、欠费原因和欠费处理方式-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/overdue-payments

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# ECS欠费说明

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

如果您账号的可用额度（含阿里云账户余额和代金券）小于待结算的账单，账号会进入欠费状态。本文主要介绍欠费对ECS资源的影响、如何结清欠费账单以及如何避免欠费等。

重要

出现欠费后有停机风险，系统会提醒或通知您，请及时结清欠费账单，避免对您的服务造成影响。

## 欠费影响

### 包年包月ECS资源

说明

包年包月ECS资源有使用期限。到期对资源的影响，可参见[包年包月](products/ecs/documents/subscription.md)。

账号欠费后，您仍可以使用已有的包年包月ECS资源，但存在以下限制：

- 

无法执行涉及费用的操作，例如新购、升级或续费实例、扩容云盘等。

- 

如果包年包月ECS实例挂载了按量付费云盘，或使用的公网带宽为按使用流量计费，欠费后无法正常使用对应云盘和公网带宽服务。欠费对按量付费云盘和公网的影响，请参见[按量付费](products/ecs/documents/overdue-payments.md)[ECS](products/ecs/documents/overdue-payments.md)[资源](products/ecs/documents/overdue-payments.md)。

若欠费超过15天，系统会卸载并释放该云盘。根据您的使用方式不同，卸载云盘可能会失败。卸载失败后，该云盘也不会继续产生费用，但存在数据丢失的风险，建议您不再使用这些云盘。

### 按量付费ECS资源

账号欠费后，系统会自动停止服务，欠费停机期间ECS资源暂停计费；持续欠费15天后，系统将释放或解绑所有ECS资源。

重要

- 

如果您的账户欠费，即使已经设置自动释放时间，按量付费实例也不会按照设置的时间释放。

- 

若您的实例已启用节省停机模式，计算资源（vCPU和内存）会被回收。账号欠费后，再次启动该实例时会启动失败。[什么是节省停机模式？](products/ecs/documents/user-guide/economical-mode.md)

欠费停机后，ECS各资源保留情况如下：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 资源类型 | 欠费后 15 天内 | 欠费 15 天后 |
| --- | --- | --- |
| 计算资源（vCPU、GPU 和内存） | 实例因欠费被关机并停止服务后会立即进入 已过期 状态。 实例停止服务后 48 小时内阿里云会释放实例的计算资源，此时，实例会进入 欠费回收中 状态。 若实例状态为 已过期 ，保留计算资源（vCPU、内存和 GPU）。 若实例状态为 欠费回收中 ，释放计算资源（vCPU、内存和 GPU）。 | 计算资源（vCPU、GPU 和内存）已被释放，无法恢复。 |
| 块存储 | 保留云盘和云盘数据。 保留本地盘，但本地盘数据可能随时被释放。 | 释放云盘和云盘数据，数据无法恢复。 释放本地盘，数据无法恢复 。 |
| 公网 IP | 保留固定公网 IP 地址。 EIP 与 ECS 实例的生命周期相互独立，如果您使用了 EIP，账号欠费对 EIP 的影响，请参见 [EIP](products/eip/documents/overdue-payments.md) [欠费说明](products/eip/documents/overdue-payments.md) 。 | 释放固定公网 IP 地址。 EIP 与 ECS 实例的生命周期相互独立，如果您使用了 EIP，账号欠费对 EIP 的影响，请参见 [EIP](products/eip/documents/overdue-payments.md) [欠费说明](products/eip/documents/overdue-payments.md) 。 |
| 快照 | 保留所有快照和自定义镜像，但不允许使用已有快照创建新云盘或自定义镜像。 不允许再手动新建快照、自动快照停止创建、基于实例创建自定义镜像的操作会因为无法创建快照而失败。 如果您充值补足欠款，可以继续使用已有快照、自动快照策略也将自动启用。 | 用户保有的快照资源都会被清理删除（包含快照、快照组、自定义镜像关联的快照等），清理后数据不可恢复。 若快照关联了自定义镜像，关联的自定义镜像也会被删除，不可恢复。 如果您充值补足欠款，自动快照策略将自动启用。 重要 如果存在基于自定义镜像创建的包年包月实例，自定义镜像删除后不影响包年包月实例的正常使用，但无法重新初始化系统盘。 如果自定义镜像已共享给他人，则自定义镜像删除后，被共享者无法再看到并使用该镜像创建 ECS 实例，基于共享镜像创建的 ECS 实例无法重新初始化系统盘。 如果自定义镜像已发布为社区镜像，则自定义镜像删除后，社区镜像会同步删除，无法再用于创建 ECS 实例，已使用该社区镜像创建的 ECS 实例无法重新初始化系统盘。 |


## 结清欠费账单

账号欠费会导致按量付费ECS实例停机，请及时结清欠费账单，避免对您的服务造成影响。具体操作，请参见[在线充值](https://help.aliyun.com/zh/user-center/use-alipay-online-banking-to-recharge-online)。

结清欠费账单后，系统会自动重启因欠费导致停机实例。如果偶尔出现自动重开机失败的情况，您也可以手动启动实例。具体操作，请参见[启动实例](products/ecs/documents/user-guide/start-an-instance.md)。

## 如何避免欠费停服

- 

释放无用资源

若ECS资源不需要再使用，建议您及时备份删除，以免继续扣费。

- 

设置额度预警

基于账户的可用金额，设置预警阈值，当可用额度低于该阈值时，系统自动触发提醒。具体操作，可参见[监控账户余额](https://help.aliyun.com/zh/user-center/monitor-account-balances)。

- 

设置自动释放时间

为按量付费实例开启自动释放功能，避免超出预期开通时长产生不必要的费用或欠费。具体操作，请参见[释放实例](products/ecs/documents/user-guide/release-an-instance.md)。

- 

开启延期免停权益

阿里云提供延期免停权益，即当按量付费的资源发生欠费后，提供一定额度或时长继续使用云服务的权益，延停期间正常计费。具体使用说明和规则，请参见[延期免停权益](https://help.aliyun.com/zh/user-center/exemption-of-suspension-after-delinquency)。

## 查看欠费金额

- 

登录[费用与成本控制台](https://billing-cost.console.aliyun.com/home)

- 

在首页的总览区域，查看欠费金额。

## 常见问题

- 

[如何充值缴费？](https://help.aliyun.com/zh/user-center/use-alipay-online-banking-to-recharge-online)

- 

[如果我的账号余额不足，系统会提醒我吗？什么时候提示？](products/ecs/documents/billing-faq.md)

- 

[账号余额不足时，按量付费实例上的数据会受到影响吗？](products/ecs/documents/billing-faq.md)

- 

[购买](products/ecs/documents/billing-faq.md)[ECS](products/ecs/documents/billing-faq.md)[实例后提出了退款，为什么还是扣了费用？](products/ecs/documents/billing-faq.md)

- 

[为什么我的账户有余额仍然显示欠费了？](https://help.aliyun.com/zh/user-center/support/why-do-overdue-bills-exist-when-my-account-has-a-balance)

[上一篇：账单查询](products/ecs/documents/view-billing-details.md)[下一篇：退订说明](products/ecs/documents/refund-instructions.md)

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
