# 什么是立即生效容量预定-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/overview-of-immediate-capacity-reservation

# 立即生效容量预定概述
立即生效容量预定为按量付费实例保障资源供应确定性，预定成功后对应的容量立即被锁定，适用于资源使用量较高的弹性需求。
## 简介
您可以随时购买立即生效容量预定，预订成功后立即生效，即容量被锁定。无论是否使用预定容量创建了实例，生效后即开始按照按量实例费率收费，直至立即生效容量预定被释放。
购买立即生效容量预定时设置可用区、实例规格、操作系统类型等属性，系统会以私有池的方式预留属性相匹配的资源。在创建按量付费实例时选择使用私有池的容量，即可提供资源确定性保障。
说明
仅支持为创建按量付费实例提供保障，不支持为创建抢占式实例提供保障。
立即生效容量预定的使用流程如下所示：
购买立即生效容量预定，购买成功后即开始遵循按量付费标准计费。
在保障期内，随时可以使用私有池的容量创建按量付费实例。
手动释放立即生效容量预定，或者等到期系统自动释放立即生效容量预定。
说明
释放立即生效容量预定不影响已经创建的按量付费实例运行，在按量付费实例运行期间遵循按量付费标准计费。
以购买预留2台实例的立即生效容量预定为例，流程示意图如下所示。
## 计费
购买立即生效容量预定后，实例规格即开始遵循按量付费标准计费，不论是否实际创建了按量付费实例，直至您自行手动释放或到期系统自动释放立即生效容量预定。
说明
未实际创建按量付费实例时，仅收取实例规格的费用。实际创建按量付费实例后，才会根据您的实例配置收取实例规格、云盘、公网带宽等相关资源费用。
立即生效容量预定的关联实例支持通过节省计划、地域级预留实例券抵扣小时账单，但不支持通过可用区级预留实例券抵扣小时账单。
## 使用限制
部分地域、实例规格支持立即生效容量预定，以售卖页显示为准。
使用关联私有池容量创建按量付费实例时，立即生效容量预定和按量付费实例的实例规格、可用区、操作系统属性必须匹配。
使用关联私有池容量创建按量付费实例后，不能用可用区级预留实例券抵扣小时账单。
## 应用场景
资源使用量较高的弹性需求：购买立即生效容量预定后，实例规格即开始遵循按量付费标准计费，因此在预定的周期内持续使用、使用量较高时，才能保证不浪费成本。
已购买节省计划、地域级预留实例券时预留资源：节省计划、地域级预留实例券可以有效降低成本，但是不能保障资源供应确定性。如果您在购买节省计划、地域级预留实例券后需要预留资源，可以搭配立即生效容量预定。
## 应用示例
手动释放示例
需求如下：
使用已购买的1张地域级预留实例券抵扣按量付费实例的小时账单，地域级预留实例券的地域为华东1（杭州）、实例规格为ecs.g6.large、实例数量为10台、操作系统为Linux。
需要立即在当前地域下的可用区H、可用区I预留资源。
可能随业务需求改在其他可用区创建实例。
方案如下：
在可用区H、可用区I分别创建1个可手动释放的立即生效容量预定，请注意参考地域级预留实例券的实例规格、实例数量、操作系统属性。
需要在其他可用区预留资源时，手动释放可用区H、可用区I中的立即生效容量预定，并在目标可用区创建立即生效容量预定。
定时释放示例
需求如下：
使用已购买的1份通用型节省计划抵扣按量付费实例的小时账单。
需要在固定周期预留资源，月初至月中使用ecs.c6e.large，月中至月末使用ecs.c6.large。
方案如下：
月初购买定时释放的立即生效容量预定，保障ecs.c6e.large的资源供应。
月中购买定时释放的立即生效容量预定，保障ecs.c6.large的资源供应。
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
