# 转换云盘计费方式-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/switch-the-billing-method-of-a-disk

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

# 转换云盘计费方式

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

如果云盘当前的按量付费或包年包月的计费方式不满足您的需求，您可以依照本文内容转换云盘的计费方式。

## 前提条件

- 

需要转换的块存储设备为云盘，弹性临时盘及本地盘不能单独转换，只能随实例一起转换计费方式。具体操作，请查看[实例包年包月转按量付费](products/ecs/documents/change-the-billing-method-of-an-instance-from-subscription-to-pay-as-you-go-1.md)和[实例按量付费转包年包月](products/ecs/documents/change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md)。

- 

需要转换的计费方式为包年包月或按量付费。抢占式实例的基础计费方式或节省计划、存储容量单位包等优化成本的计费方式不支持转换。

- 

请确保实例状态为运行中（Running）或已停止（Stopped）。

- 

请确保云盘满足以下条件：

- 

云盘状态为使用中（In_use）。

- 

云盘未开启多重挂载功能，开启多重挂载功能的云盘不支持转换云盘计费方式。更多信息，请参见[云盘多重挂载功能](products/ecs/documents/user-guide/enable-multi-attach.md)。

- 

操作前5分钟内未成功修改过云盘基础计费方式。

## 操作步骤

- 

系统盘不能单独转换，只能随实例一起转换计费方式。具体操作，请参见[实例包年包月转按量付费](products/ecs/documents/change-the-billing-method-of-an-instance-from-subscription-to-pay-as-you-go-1.md)和[实例按量付费转包年包月](products/ecs/documents/change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md)。

- 

您可以根据不同的需求选择不同的参考文档转换数据盘的计费方式。

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

- 

- 

- 

- 

| 云盘计费方式转换需求 | 实例计费方式 | 操作步骤 |
| --- | --- | --- |
| 按量付费转包年包月 | 按量付费 | 只能随实例转换计费方式。具体操作，请参见 [实例按量付费转包年包月](products/ecs/documents/change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md) 。 |
| 包年包月 | 选择以下一种方式，转换云盘计费方式。 如果需要转换某一实例上挂载的多个数据盘，建议您在实例页面操作。 访问 [ECS](https://ecs.console.aliyun.com/server/region) [控制台-实例](https://ecs.console.aliyun.com/server/region) 。 在页面左侧顶部，选择目标资源所在的资源组和地域。 选择待转换数据盘的 ECS 实例，并进入实例详情页面，在 全部操作 中，选择 升级配置 。 在 升级配置 页面的 磁盘付费方式 区域，选中要转换的按量付费数据盘。 选中的数据盘的付费方式将会在升配订单中从按量付费转换为包年包月。 如果要转换特定的某个数据盘，建议您在云盘页面操作。 访问 [ECS](https://ecs.console.aliyun.com/disk/) [控制台-块存储-云盘](https://ecs.console.aliyun.com/disk/) 。 在页面左侧顶部，选择目标资源所在的资源组和地域。 找到要转换的数据盘，在 操作 列中，选择 > 按量付费转包年包月 。 在 磁盘付费方式 区域查看已默认选中的云盘。 阅读升配须知，选中 《云服务器 ECS 服务条款》 ，然后单击 确认订单 。 完成支付，确认云盘的付费方式已转换为包年包月。 重要 云盘的付费方式转换为包年包月后，不支持卸载。 |  |
| 包年包月转按量付费 | 包年包月（包年包月云盘只能挂载到包年包月实例上，不存在按量付费的情况） | 说明 使用实时降配功能将包年包月数据盘转为按量付费数据盘的过程中可能产生退款，退款金额是新配置的价格与降配前有效购买剩余价格的差额。 更多信息，请参见 [实时降配退订规则](https://help.aliyun.com/zh/user-center/billing-rules-of-upgrades-and-downgrades) 。 选择以下一种方式，转换云盘的计费方式。 如果需要转换某一实例上挂载的多个数据盘，建议您在实例页面操作。 访问 [ECS](https://ecs.console.aliyun.com/server/region) [控制台-实例](https://ecs.console.aliyun.com/server/region) 。 在页面左侧顶部，选择目标资源所在的资源组和地域。 选择待转换数据盘的 ECS 实例，并进入实例详情页面，在 全部操作 中，选择 降低配置 。 单击 磁盘付费方式 页签，并选中要转换的包年包月数据盘。 如果需要转换某个特定的数据盘，建议您在云盘页面操作。 访问 [ECS](https://ecs.console.aliyun.com/disk/) [控制台-块存储-云盘](https://ecs.console.aliyun.com/disk/) 。 在页面左侧顶部，选择目标资源所在的资源组和地域。 找到需要转换的数据盘，在 操作 列中，选择 > 包年包月转按量付费 。 在 磁盘付费方式 页签查看已默认选中的云盘。 选中 《云服务器 ECS 服务条款》 ，然后单击 立即降配 。 云盘的付费方式转换为按量付费后，默认不随实例释放。您可以在 ECS 控制台更改随实例释放设置，具体操作，请参见 [释放云盘](products/ecs/documents/user-guide/release-a-disk.md) 。 |


## 相关文档

您也可以通过API接口转换云盘计费方式，具体操作，请参见[ModifyDiskChargeType](products/ecs/documents/api-modifydiskchargetype.md)。

[上一篇：按量付费转包年包月](products/ecs/documents/change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md)[下一篇：转换固定公网IP的带宽计费方式](products/ecs/documents/change-the-billing-method-for-network-usage-1.md)

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
