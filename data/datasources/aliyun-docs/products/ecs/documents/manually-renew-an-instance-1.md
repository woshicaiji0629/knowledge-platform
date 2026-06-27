# ECS实例续费规则以及续费ECS实例多种方式-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/manually-renew-an-instance-1

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

# 如何续费包年包月实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

若您试用或购买了包年包月ECS，希望继续使用产品，可在实例到期被释放前，随时续费包年包月ECS实例，延长相关ECS实例的使用时间。本文介绍如何续费ECS实例。

在包年包月ECS实例创建、到期、释放等不同阶段，您可以根据需要选择任意一种方式进行续费。

说明

- 

到期：实例可使用的最后时间，如续费成功，到期时间会顺延。

- 

释放：若实例到期后15天内仍未进行续费，第16天0点起会释放删除实例及实例上的数据。

## 立即续费

- 

通过PC端续费：功能全面，推荐您使用。

- 

通过阿里云App端续费：便捷性强，暂不支持在续费同时开通或取消自动续费。

- 

通过API续费：暂不支持在续费的同时开通或取消自动续费。

### （推荐）通过PC端续费

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，并在顶部菜单栏选择实例所在地域。

- 

在实例列表页选择待续费实例，并进入实例详情页面，在实例信息的到期时间字段下方单击续费，按页面提示选择续费时长并完成支付。

说明

阿里云为您提供了多台实例批量续费功能。

- 

若您想对单一地域下多台实例进行批量续费，您可以在实例列表勾选多台目标实例，并在列表底部选择更多>费用> 续费进行批量操作。

- 

若您想对不同地域下的多台实例进行批量续费，您可以前往[续订管理](https://usercenter2.aliyun.com/renew/manual)页面，在手动续订页签下的列表中勾选一台或多台ECS实例进行续费。请注意，云服务器ECS暂不支持和其他产品一起批量续费。

通过阿里云App续费

- 

登录阿里云App，选择控制台 > 续费管理。

- 

单击云服务器 ECS-包年包月，并选择实例所在地域。

- 

勾选一台或多台实例，单击立即续费。

- 

单击提交订单，并按照页面提示完成支付。

通过API续费

您可以调用[续费实例](products/ecs/documents/developer-reference/api-ecs-2014-05-26-renewinstance.md)API，设置待续费的实例ID，及根据续费场景选择的续费时长参数（Period、PeriodUnit或ExpectedRenewDay的其中一个的值），即可为单个ECS实例完成续费的操作。若您想通过API批量续费多台ECS实例，您可以多次调用此接口实现批量操作。

我们也为您提供了其他包年包月实例续费相关的API接口：

- 

开启自动续费：您可以调用[修改实例的自动续费属性](products/ecs/documents/developer-reference/api-ecs-2014-05-26-modifyinstanceautorenewattribute.md)，通过设置实例IDInstanceId、续费时长Duration、和自动续费状态参数AutoRenew为实例开通自动续费。

- 

查询实例续费价格：您可以调用[查询资源续费价格](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describerenewalprice.md)接口，传入查询实例的地域、规格、续费时长等参数查询实例续费费用。

- 

查询指定范围内到期的云服务器：通过调用[查询实例的详细信息列表](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstances.md)，并设置过滤参数ExpiredStartTime和ExpiredEndTime，查询一定时间范围内到期的实例信息。

- 

查询ECS实例的自动续费状态：您可以调用[查询实例自动续费属性](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstanceautorenewattribute.md)，通过设置实例IDInstanceId和实例自动续费状态RenewalStatus，查询实例的自动续费状态或处于特定自动续费状态下的实例列表。

## 更多续费方式

- 

- 

| 续费方式 | 操作时段限制 | 适用场景 | 新计费周期 |
| --- | --- | --- | --- |
| [自动续费](products/ecs/documents/enable-auto-renewal-for-an-instance-1.md) | 实例到期前 1 日之前 | 仅续费时长，不变更实例配置。 系统将在实例到期前自动续费，避免因忘记手动续费导致 ECS 资源被自动释放影响业务。 重要 如果您的实例将于下一天到期，因扣款时间限制，自动续费可能会不生效，建议您自主 [手动续费](products/ecs/documents/manually-renew-an-instance-1.md) 。 | 自动续费成功后，从原到期日开始计算新的计费周期。 |
| [续费降配](products/ecs/documents/downgrade-instance-configurations-during-renewal.md) | 实例到期前 15 日内至实例被释放前 | 续费的同时，降低实例或带宽等资源配置。 如果您预测下个周期业务需求下降或实例规格过剩，可在续费实例的同时，降低实例规格或公网带宽等配置，节省下个周期的资源成本。 | 实例到期前 15 日： 从原到期日开始计算新的计费周期。 实例到期后 ：从续费日当天开始计算新的计费周期。 |
| [续费变配](products/ecs/documents/a-renewal-variable-2.md) | 实例到期至被释放前 | 续费的同时，升级或降低实例规格。 如果您需要延长实例的使用时间，且需要变更实例的规格，可通过续费变配来实现，灵活应对业务变化。 | 从续费日当天开始计算新的计费周期。 |
| [统一包年包月实例的到期日](products/ecs/documents/synchronize-the-expiration-dates-of-subscription-instances.md) | 实例到期前 | 将多个包年包月实例的到期日，通过续费方式统一延期到各月份的同一天，便于日常管理和续费，避免因忘记续费而导致业务中断风险。 | 从续费日当天开始计算新的计费周期。 |


## 续费提醒及订阅

阿里云消息中心提供了续费提醒功能，默认支持包年包月ECS实例在实例到期前7天、3天、1天，到期当天、释放前一天通过站内信、邮箱、短信来通知提醒您及时续费。您可以在消息中心订阅实例到期前15或30天提醒，以及修改提醒接收手机号。具体操作，请参见[设置续费提醒](products/ecs/documents/set-renewal-reminder.md)。

## 设置到期不续订

如果已确定实例到期后不再使用，您可以参照以下步骤将实例设置为到期不续订，减少您收到的到期提醒次数。

说明

将实例设置为到期不续费后，在到期前您可以随时为其续费。

- 

进入[续订管理](https://usercenter2.aliyun.com/renew/manual?expiresIn=&commodityCode=)页面，设置查询条件。

产品选择云服务器ECS-包年包月，单击手动续订或自动续订页签。

- 

勾选一台或多台目标ECS实例，单击列表顶部的设置为不续订按钮，在弹窗中确认信息后单击确定。

- 

设置完成后，您可以在到期不续订页签查看已设置实例。

已设置为到期不续订的实例，您可以实例到期释放前继续为其续费。在到期不续订页签，找到目标ECS实例，在操作列选择任意一种续订方式均可取消到期不续订状态。

[上一篇：续费包年包月实例](products/ecs/documents/renew-instances.md)[下一篇：自动续费](products/ecs/documents/enable-auto-renewal-for-an-instance-1.md)

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
