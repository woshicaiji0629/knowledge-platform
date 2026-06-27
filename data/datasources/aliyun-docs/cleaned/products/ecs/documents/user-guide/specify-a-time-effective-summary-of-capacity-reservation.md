# 指定时间生效容量预定包括哪些-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/specify-a-time-effective-summary-of-capacity-reservation

# 指定时间生效容量预定概述
指定时间生效容量预定用于在未来的某个时间点开始保障资源供应确定性，以私有池的形式预留资源，保障届时可以顺利开展业务。
## 使用流程
根据保障交付的资源类型进行区分。指定时间生效的容量预定分为两种：节省计划容量预定和包年包月容量预定。
### 节省计划容量预定使用流程
节省计划容量预定用于保障成功创建按量付费实例，使用流程如下：
您购买节省计划容量预定，指定可用区、实例规格、生效时间等属性。
节省计划容量预定在指定的时间开始生效，在保障期内随时可以使用私有池容量创建按量付费实例，按量付费实例的小时账单由关联的节省计划抵扣。
说明
节省计划抵扣实例的计算资源（vCPU和内存）、镜像、系统盘、数据盘（包括容量费用、预配置性能费用、性能突发费用）、固定公网带宽的费用，其他资源则按实际情况收费。更多信息，请参见[什么是节省计划](what-is-savings-plan.md)。
已生效的节省计划容量预定被手动释放，或者到期自动释放，停止预留资源。
说明
节省计划容量预定被释放后，已创建按量付费实例可以正常运行，但会停止使用关联的节省计划抵扣实例账单，继续运行的按量付费实例遵循按量付费标准计费。
以购买预留2台实例的节省计划容量预定为例，流程示意图如下所示。
### 包年包月容量预定使用流程
包年包月容量预定用于保障成功创建包年包月实例，使用流程如下：
您购买包年包月容量预定，指定可用区、实例规格、生效时间等属性，等待备货。
阿里云收到包年包月容量预定订单，开始备货，并在备货完毕后向您发送生效通知。
您收到生效通知，在提货期内使用私有池容量创建包年包月实例，并预支包年包月实例的费用。
说明
包年包月容量预定用于保障首次创建包年包月实例，不能保障已创建包年包月实例的变配、续费等操作，且包年包月实例的购买时长至少为1个月。
私有池容量使用完毕，或者超过提货期，停止预留资源。
以购买预留2台实例的包年包月容量预定为例，流程示意图如下所示。
## 计费
| 时间段 | 节省计划容量预定 | 包年包月容量预定 |
| --- | --- | --- |
| 购买时 | 目前仅支持 0 预付节省计划，购买时无需支付费用。 | 购买时无需支付费用。 |
| 使用时 | 支付 0 预付节省计划的费用。 节省计划抵扣闲置容量的费用、已创建按量付费实例的费用。 如果已创建按量付费实例包括了计算资源（vCPU 和内存）、系统盘、固定公网带宽的费用以外的资源，节省计划不能抵扣，按实际情况收费。 | 如果有闲置容量，遵循实例规格的按量付费标准计费，支付闲置容量的费用。 创建包年包月实例时，预支包年包月实例的费用。 |
## 使用限制
部分地域、实例规格支持指定时间生效容量预定，支持情况以售卖页显示为准。
不支持手动释放包年包月容量预定和未生效的节省计划容量预定。
## 应用示例
公司规模持续扩大，内部服务平台需要不断为更多员工提供服务，计划将该平台迁移上云。
需求如下：
项目还在准备中，但已经制定明确的项目计划，必须保证未来执行迁移时创建足够的实例承载服务。
该平台需要定期进行系统升级，升级过程中需要释放部分实例然后重新创建，必须保证实例可以成功创建。
方案如下：
规划所需资源，例如所需的实例规格、私有池容量大小、是否需要跨地域等。
购买节省计划容量预定，按照项目计划设置生效时间。
执行迁移时，节省计划容量预定如期生效，使用私有池容量创建实例可以保障创建成功。
迁移完成后，节省计划容量预定在保障期内保障资源供应确定性。进行自动化升级时，释放实例后对应的私有池容量会闲置，再创建实例时可以继续使用这些容量保障创建成功。
如果临时需要更多资源，您可以使用公共池的资源，充分利用云上资源的弹性。如果需要稳定使用更多资源，您可以再购买立即生效容量预定，为这些资源保障供应确定性。
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
