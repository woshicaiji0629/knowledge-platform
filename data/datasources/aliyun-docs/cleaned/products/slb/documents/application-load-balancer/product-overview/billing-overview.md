# ALB计费概述-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/product-overview/billing-overview

# ALB计费概述
通过阅读本文，您可以快速了解ALB的计费信息。
## 付费方式
应用型负载均衡 ALB（Application Load Balancer）支持按量付费（后付费）和资源包（预付费）两种付费方式。
按量付费（后付费）：按照各计费项的实际用量结算费用，先使用，后付费，适用于业务用量经常有变化的场景。
资源包（预付费）：预先购买资源包，在费用结算时，优先从资源包抵扣用量，先购买，后抵扣，适用于业务用量相对稳定的场景。
说明
相较于按量付费，资源包具有一定的优惠折扣。
超出资源包抵扣额度的用量，将自动转为按量付费，会产生后付费账单，请根据您的业务量购买适合业务额度的资源包。
## 计费组成
按量付费ALB计费组成如下：
## 计费周期
ALB的实例费和性能容量单位LCU费均为按小时计费，并按照使用量结算产生的费用。账单出账时间通常在当前计费周期结束后一小时，具体出账时间以系统为准。
公网ALB会被收取公网网络费用，公网ALB通过弹性公网IP（EIP）提供公网能力，ALB实例关联的EIP产生的公网网络费用由EIP收取，因此公网网络费用的计费周期、扣费及出账时间与按量付费EIP的计费周期、扣费及出账时间一致。更多信息，请参见[计费周期](../../../../eip/documents/billing-overview.md)。
## 产品定价
ALB产品目录价请参见[ALB](alb-billing-rules.md)[计费规则](alb-billing-rules.md)和[ALB](introduction-to-alb-resource-plans.md)[资源包](introduction-to-alb-resource-plans.md)。实际购买价格请以[购买页](https://common-buy.aliyun.com/?commodityCode=slb_ealb_public_cn)为准。
您可以使用[ALB LCU](https://www.aliyun.com/price/product#/commodity/slb_ealb_public_cn)[估算器](https://www.aliyun.com/price/product#/commodity/slb_ealb_public_cn)来预估LCU的消耗。
## 更多信息
### 欠费说明
欠费原因
未购买资源包，且绑定的账号余额不足。
已购买资源包，但资源包并不能抵扣所有费用。
欠费说明
| 状态 | 资源状态 | 如何操作 |
| --- | --- | --- |
| 欠费预警 | 系统根据服务最近 7 小时的账单应付金额的平均值来判断您的账户余额是否足以支付三个账期的费用。如果不足以支付，系统将以短信或邮件的方式提醒您。 警告 出现欠费后有停机风险，系统会通知您及时续费，避免对您的服务造成影响。 | 给阿里云账号 [充值](https://usercenter2.aliyun.com/finance/fund-management/recharge) ，实例立即恢复正常。 |
| 欠费后 | 阿里云账号欠费后，该账号下所有按量付费实例将会进入欠费状态。 欠费后如果在延停权益额度内，实例不会停止服务。在此期间，您每天会收到一次短信提醒。 说明 阿里云提供延期免停权益，即当按量付费的资源发生欠费后，提供一定额度或时长继续使用云服务的权益，延停期间正常计费。具体使用说明和规则，请参见 [延期免停权益](https://help.aliyun.com/zh/user-center/exemption-of-suspension-after-delinquency) 。 欠费期间无法释放实例。 欠费后如果超出了延停权益额度，ALB 实例会立即停机，阿里云将停止对实例计费。 如果您在 ALB 实例停机 7 天内充值并补足欠费，ALB 服务会自动开启，您可以继续使用 ALB 实例。 |  |
| 欠费停机 7 天后，ALB 实例将被释放，实例相关的配置和数据会被删除且不可恢复。 | 无法找回。 |  |
查看欠费金额
登录[费用与成本](https://usercenter2.aliyun.com/home)控制台。
在首页的总览区域，查看欠费金额。
### 查看用量明细
登录[费用与成本](https://billing-cost.console.aliyun.com/home)控制台。在左侧导航栏，选择账单管理>账单详情。
单击查看用量明细页签。选择产品为负载均衡，计量规格为应用型负载均衡ALB，配置需要查看用量明细的使用时间和计量粒度后，单击导出CSV。
打开用量明细文件后，可根据业务起止时间、实例ID等查看LCU用量的详细信息。
### 账单和消费明细查询
登录[费用与成本的账单详情页面](https://usercenter2.aliyun.com/finance/expense-report/expense-detail)。
在账单详情页面，您可以单击明细账单、用量明细页签，查看相应的消费情况和账单信息。详情请参见[账单详情](https://help.aliyun.com/zh/user-center/billing-details-1)。
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
