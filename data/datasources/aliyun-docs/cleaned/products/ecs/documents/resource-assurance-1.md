# 资源保障计费方式与计费示例-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/resource-assurance-1

# 资源保障
资源保障可以帮助您在查询、预定、购买和使用资源时获得更好的体验。主要包括资源供应的实时了解、资源的可靠预订和使用私有池来规划资源。本文主要介绍资源保障的计费方式和计费示例。
## 计费方式
针对不同场景预留资源，购买弹性保障、容量预定-指定时间生效或容量预定-立即生效后，阿里云以私有池的方式预留属性一致的资源。更多信息，请参见[资源管家概述](user-guide/overview-29.md)。
购买资源保障时，支持以下几种计费方式，具体如下表所示。
| 预定方式 | 计费方式 | 说明 | 参考文档 |
| --- | --- | --- | --- |
| 弹性保障-立即生效/指定时间生效 | 弹性保障 | 购买弹性保障后不能手动释放。使用弹性保障过程中，您将在以下两个阶段产生费用： 购买弹性保障时：购买时一次性支付保障费用，在保障期内，您可以随时使用私有池的容量创建按量计费实例。 成功创建按量付费实例后：按整点小时区间产生一条消费明细。 说明 如果您已购买属性相匹配的节省计划、地域级预留实例券，仍然可以用于抵扣按量付费实例产生的费用 | [弹性保障概述](user-guide/overview-of-elasticity-assurance.md) |
| 容量预定-立即生效 | 立即生效容量预定 | 购买立即生效容量预定后，不论是否实际创建了按量计费实例，系统都将自动按照您预定的实例规格遵循按量计费标准计费，直至您手动释放或到期系统自动释放立即生效容量预定。 说明 未实际创建按量计费实例时，仅收取实例规格的费用。实际创建按量计费实例后，才会根据您的实例配置收取实例规格、云盘、公网带宽等相关资源费用。 将已购买的实例加入私有池，已购买实例的容量费用可被实例计算资源（vCPU 和内存）费用所抵扣，抵扣时间从加入私有池的时间开始计算。更多信息，请参见 [为已有实例设置私有池](user-guide/configure-a-private-pool-for-existing-instances.md) 。 | [立即生效容量预定概述](user-guide/overview-of-immediate-capacity-reservation.md) |
| 容量预定-指定时间生效 | 节省计划容量预定 | 购买时：目前仅支持 0 预付节省计划，购买时无需支付费用。 使用时： 支付 0 预付节省计划的费用。 使用节省计划抵扣闲置容量的费用和已创建按量计费实例的费用。 如果已创建按量计费实例包括了计算资源（vCPU 和内存）、系统盘、固定公网带宽的费用以外的资源，节省计划不能抵扣，按实际情况收费。 | [指定时间生效容量预定概述](user-guide/specify-a-time-effective-summary-of-capacity-reservation.md) |
| 包年包月容量预定 | 购买时：无需支付费用。 使用时： 如果有闲置容量，遵循实例规格的按量计费标准计费，仅支付闲置容量的费用。 创建包年包月实例时，支付包年包月实例的费用。 | [指定时间生效容量预定概述](user-guide/specify-a-time-effective-summary-of-capacity-reservation.md) |  |
## 计费示例
以下给出几种计费方式的计费示例。其中，ECS实例单价和保障费用仅用作说明，实际计算时请以[云服务器](https://www.aliyun.com/price/product#/ecs/detail)[ECS](https://www.aliyun.com/price/product#/ecs/detail)[定价](https://www.aliyun.com/price/product#/ecs/detail)中的价格为准。
### 弹性保障
计费场景：某公司用户购买1台弹性保障的ECS实例用于某次促销，具体说明如下：
弹性保障费用：100元
弹性保障指定时间：1个月
ECS实例：1台
ECS实例按量单价：10元/小时
ECS实例使用时长：6小时
计费：费用合计=弹性保障费用+按量资源费用
弹性保障费用：100元
按量资源费用：10*6=60元
费用合计：100+60=160元
说明
弹性保障指定时间内可以无限次创建和释放按量计费实例，提供资源确定性保障。
如果ECS实例使用时间超过弹性保障指定时间，到期后系统自动释放弹性保障。
释放弹性保障不影响已经创建的按量计费实例运行，在按量计费实例运行期间遵循按量计费标准计费。
### 立即生效容量预定
计费场景：某公司购买预留2台ECS实例的立即生效容量预定，用于业务部署，到期释放时间为4小时，先创建了实例A使用3小时后释放，然后创建实例B，使用1小时后释放。具体说明如下：
ECS实例按量单价：10元/小时
立即生效到期时间：4小时
ECS实例A使用时间：3小时
ECS实例B使用时间：1小时
计费：费用合计=立即生效容量预定费用+按量资源费用
立即生效容量预定费用=闲置容量费用+已使用容量费用，其中：已使用容量费用=0（被按量资源费用抵扣）
实例A按量资源费用：10*3=30元
实例A闲置容量费用：10*1=10元
实例B按量资源费用：10*1=10元
实例B闲置容量费用：10*3=30元
立即生效容量费用：10+30=40元
按量资源费用：30+10=40元
费用合计：40+40=80元
### 节省计划容量预定
计费场景：某公司预定了1台ECS实例的节省计划容量预定，在私有池创建ECS实例用于业务部署。具体说明如下：
使用时支付0预付节省计划的费用：1000元
数据盘的使用费用：500元
计费：费用合计=支付0预付节省计划的费用+其他节省计划不能抵扣的费用。
使用时支付0预付节省计划的费用=1000元
其他节省计划不能抵扣的费用：500元
费用合计：1000+500=1500元
说明
节省计划容量预定开始生效的时间，不能早于创建时间后3天或晚于创建时间后1年。
节省计划可以抵扣闲置容量的费用和已创建按量计费实例的费用。
节省计划到期前，若手动释放了容量预定，剩余的节省计划费用可以用来抵扣属性一致的按量实例或立即生效容量预定费用。
### 包年包月容量预定
计费场景：某公司预定了一个10台ECS实例的包年包月容量预定，预定有效期为7天，实际只购买了8台包年包月ECS实例。具体说明如下：
ECS实例按量单价：10元/小时
ECS实例包年包月单价：4800元/月
ECS实例使用时间：1个月
包年包月容量预定有效期：7天
计费：费用合计=包年包月容量预定费用+包年包月资源费用。
包年包月容量预定费用=（10-8）*7*24*10=3360元
包年包月资源费用：4800*8*1=38400元
费用合计：3360+38400=41760元
说明
容量预定失效期间无法取消包年包月容量预定。
若在容量预定有效期内未按预定购买包年包月实例，未购容量仍需收取按量费用，已购容量无需支付容量费用。
## 相关文档
[购买资源预定](user-guide/purchase-a-resource-reservation.md)
[使用私有池容量创建实例](user-guide/use-a-private-pool-to-create-instances.md)
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
