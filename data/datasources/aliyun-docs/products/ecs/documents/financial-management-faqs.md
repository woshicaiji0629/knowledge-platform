# 购买支付与账务FAQ-云服务器 ECS-阿里云-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/financial-management-faqs

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

# 财务管理常见问题

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

## 对公汇款常见问题

### 企业用户如何申请续费合同用于公司请款？

可以在实例列表页单击续费，生成未支付订单后，在[合同管理](https://usercenter2.aliyun.com/contract/manage)页面，申请续费合同，选择该未支付的订单。具体操作，请参见[查询和管理合同](https://help.aliyun.com/zh/user-center/contract-management#h2-u5408u540Cu7533u8BF72)。

### 对公汇款一般多久到账？

汇款到账时间一般为：招行汇款1~2个工作日，跨行汇款3~5个工作日（具体到账时间以银行的实际到账时间为准）。

### 汇款成功后ECS为什么没有续费成功？

银行汇款成功后，对应汇款资金只会充值至您的阿里云账户余额中，您需要对ECS实例进行续费操作，并且使用余额进行抵扣。

更多信息请参见[对公汇款常见问题](https://help.aliyun.com/zh/user-center/support/make-offline-remittances-to-a-corporate-account)。

### 续费成功后如何开发票？

续费成功后，在[发票管理](https://billing-cost.console.aliyun.com/invoice/home/main)页面，申请开发票时，选择一笔或多笔续费订单。具体操作，请参见[开具发票](https://help.aliyun.com/zh/user-center/request-an-invoice)。

### 续费成功后，发现续费周期或续费实例选择错误，该如何操作？

您可以前往[费用与成本控制台](https://billing-cost.console.aliyun.com/home)，选择订购订单>我的订单，单击目标续费订单操作列的详情，根据订单的起止时间查看是否已生效。

- 

若续费订单未生效，可以核实该订单是否支持退款，若支持退款，可进行退款操作后重新下单。

- 

若续费订单已生效，则不支持单独退续费。只能将整台ECS实例退订退款，请您谨慎考虑后进行操作。

### 如何申请ECS延期？

如您因财务流程等情况，导致无法在实例到期前续费，可以申请延期1天。

### 为什么我不能购买ECS实例？

不能购买ECS实例的常见原因如下：

- 

未完成实名认证：如果您打算购买中国内地地域的ECS实例，必须首先完成[实名认证](https://account.console.aliyun.com/#/auth/home)。

- 

vCPU核数超出配额：您选择的实例规格所占的总vCPU核数可能已经超出了您账号的配额限制。

- 

地域售卖量达到上限：您选中的地域云服务器ECS的售卖量可能已经达到上限，导致该地域的交易暂时关闭。请您隔段时间再尝试购买，您也可以前往[ECS](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)[实例可购买地域](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)，查看实例的可购买情况。

### 没有通过实名认证能不能购买ECS实例？

不能。下单购买前，您需要先完成实名认证。

### ECS实例怎么开具发票？

申请发票时将基于月结算单开具发票，月结算单不可拆分开票。请您前往阿里云控制台[发票管理](https://usercenter2.aliyun.com/invoice/list/aliyun)申请发票。

申请发票时将基于月结算单开具发票，月结算单不可拆分开票。请您前往阿里云控制台[费用中心](https://billing.console.aliyun.com/)申请发票。

### 如果我的账号余额不足，系统会提醒我吗？什么时候提示？

如果您账户的可用额度（含阿里云账户余额和代金券）小于待结算的账单，即被判定为账户欠费。

提醒规则如下：

- 

余额不足提醒（即，可用额度预警）。如果您账户的可用额度（含阿里云账户余额、代金券、优惠券等）小于您设置的预警阈值，会收到余额不足的短信或邮件提醒。

- 

实例释放通知。因到期或者欠费引起的实例释放，阿里云会给您发送短信和邮件通知。

如果您设置了自动续费，自动续费的扣款行为通常发生在资源到期前第9天的08:00开始，若首次扣款因余额不足失败，系统会在之后的每一天尝试扣款，直至扣款成功或资源到期前一天。因此，及时关注账户余额和预警通知，确保账户资金充足，可以避免因欠费导致的服务中断。

重要

- 

确保您的联系方式准确无误，以便接收提醒通知。

- 

即使设置了自动续费，账户余额不足仍会导致扣款失败，影响服务连续性。

### 账号余额不足时，按量付费实例上的数据会受到影响吗？

如果您账户的可用额度（含阿里云账户余额和代金券）小于待结算的账单，即被判定为账户欠费。

账户欠费时，如果未在规定时间内充值结清欠费账单并重启，您将不能正常使用ECS资源。欠费后立即停机，欠费停机期间相关ECS资源暂停计费，按量付费实例上的数据保留情况和资源类型有关。具体说明，请参见[欠费说明](products/ecs/documents/overdue-payments.md)。

说明

阿里云提供延期免停权益，即当按量付费的资源发生欠费后，提供一定额度或时长继续使用云服务的权益，延停期间正常计费。具体使用说明和规则，请参见[延期免停权益](https://help.aliyun.com/zh/user-center/exemption-of-suspension-after-delinquency)。

### 是否支持百倍赔偿？

不支持。有关赔偿的条款请参见[云服务器](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud201909241949_62160.html)[ECS](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud201909241949_62160.html)[服务等级协议](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud201909241949_62160.html)。

### 购买ECS实例后第一时间提出了退款，为什么还是扣了费用？

如果您的ECS实例未满足五天无理由退款规则，会按照剩余时间退还余款，规则详情请参见[退款规则及退款流程](https://help.aliyun.com/zh/document_detail/37096.html)。

[上一篇：欠费、释放、退订及续费](products/ecs/documents/billing-and-subscription-management-faqs.md)[下一篇：动态与公告](products/ecs/documents/announcements-and-updates.md)

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
