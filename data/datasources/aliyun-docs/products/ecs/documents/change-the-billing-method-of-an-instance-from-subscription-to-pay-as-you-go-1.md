# 包年包月转按量付费-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/change-the-billing-method-of-an-instance-from-subscription-to-pay-as-you-go-1

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

# 包年包月转按量付费

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

将包年包月实例转为按量付费，可退还部分费用，并实现按需启停。为避免欠费导致实例服务中断，请确保转换后账户余额充足。

## 转换影响

- 

计费方式变更：实例规格、系统盘、随实例购买的包年包月数据盘以及绑定的固定公网IP，计费方式都将从包年包月变更为按量付费。

- 

费用与退款：系统将依据[包年包月转按量付费退款规则](https://help.aliyun.com/zh/user-center/description-of-refund-rules-for-transfer-to-pay-as-you-go)计算订单剩余价值，并将相应的实付金额退还至原支付渠道。未生效的续费或升配订单将进行全额退款。

重要

由于备案、故障或机房迁移等原因赠送的包年包月使用时长自动作废，可退金额为0。已生效订单支付时使用的代金券和优惠券不予退回。

- 

优惠失效：原包年包月实例若享有活动折扣，转换后该折扣即失效。未来若从按量付费重新转回包年包月，届时可能无法再次享受相同的折扣。

## 适用范围

- 

不支持转换为按量付费的实例包括：已过期的实例、使用阿里云公共镜像Red Hat Enterprise Linux、SUSE Linux Enterprise Server的实例，以及使用云市场镜像的实例。

- 

当月可用退款额度不足时，无法执行该转换操作。

转换退款会消耗退款额度，额度以转换页面显示为准，当月额度已超可等待次月1日退款消耗额度自动清零后转换。

## 操作步骤

转换前可以通过[ECS](https://ecs-buy.aliyun.com)[控制台-自定义购买](https://ecs-buy.aliyun.com)页面按照当前实例配置预估实例转换后的按量付费价格。

## 控制台

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

找到目标ECS实例，单击实例ID并进入实例详情页，在全部操作中，选择包年包月转按量付费。

- 

仔细阅读弹出的转换须知，确认无误后勾选同意选项，单击确认转换。

- 

操作成功后，返回实例列表页面进行验证。目标实例的付费方式将显示为按量付费。

如需转换多个实例，可使用[在实例列表页执行批量操作](products/ecs/documents/user-guide/batch-operation-of-ecs-instances-through-the-ecs-console.md)功能，单次最多支持转换20台实例。

## API

可以通过API接口[ModifyInstanceChargeType](products/ecs/documents/api-modifyinstancechargetype.md)将包年包月ECS实例转换为按量付费ECS实例。

## 常见问题

开启了“默认启用节省停机模式”的实例，转换为按量付费实例后为什么没有进入节省停机状态？

若实例转换前处于已停机状态且开启了默认启用节省停机模式，切换实例的计费状态后，实例不会自动进入节省停机模式。要启用节省停机模式，需要先手动启动该实例，然后再将其停止。

如何将单独修改随包年包月实例一起购买的数据盘的计费方式？

对于随实例购买的包年包月数据盘，支持单独[转换云盘计费方式](products/ecs/documents/switch-the-billing-method-of-a-disk.md)为按量付费。

如何将或弹性公网IP或固定公网IP转换为按使用流量计费/按固定带宽计费？

固定公网IP及弹性公网IP的带宽计费模式（按固定带宽计费或按使用流量计费）不随ECS实例的计费方式转换而变更。若期望转换计费模式，可参见[转换固定公网](products/ecs/documents/change-the-billing-method-for-network-usage-1.md)[IP](products/ecs/documents/change-the-billing-method-for-network-usage-1.md)[的带宽计费方式](products/ecs/documents/change-the-billing-method-for-network-usage-1.md)及[弹性公网](https://help.aliyun.com/zh/eip/switch-billing-methods#title-kmy-wm6-wbl)[IP](https://help.aliyun.com/zh/eip/switch-billing-methods#title-kmy-wm6-wbl)[按固定带宽计费与按使用流量计费转换方法](https://help.aliyun.com/zh/eip/switch-billing-methods#title-kmy-wm6-wbl)。

如何转换弹性公网IP的计费方式？

弹性公网IP是独立于ECS产品购买的产品，其计费方式不随绑定ECS实例的计费方式转换而变更，可参考[包年包月](https://help.aliyun.com/zh/eip/modify-the-configuration-of-a-subscription-eip)[EIP](https://help.aliyun.com/zh/eip/modify-the-configuration-of-a-subscription-eip)[变配](https://help.aliyun.com/zh/eip/modify-the-configuration-of-a-subscription-eip)，将包年包月的弹性公网IP转换为按量付费计费方式。

[上一篇：转换计费方式](products/ecs/documents/change-the-billing-method.md)[下一篇：按量付费转包年包月](products/ecs/documents/change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md)

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
