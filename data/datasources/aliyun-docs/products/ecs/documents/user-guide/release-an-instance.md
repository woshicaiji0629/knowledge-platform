# 如何释放ECS实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/release-an-instance

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

# 释放实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

对于不再使用或闲置的ECS实例，为避免产生不必要的费用，可通过控制台或API立即或定时释放实例。如需防止ECS实例被意外释放，可开启实例释放保护。

## 影响与风险

- 

数据丢失：释放实例时，本地盘、设置了随实例释放的数据盘及系统盘会一起释放，此外，设置了随云盘释放的自动快照也会一起被删除。

规避方法：提前[手动创建快照](products/ecs/documents/user-guide/create-a-snapshot.md)或[自定义镜像](products/ecs/documents/user-guide/create-a-custom-image-from-a-snapshot-1.md)备份数据。

- 

IP丢失：实例的固定公网IP将被回收，无法找回。

规避方法：[将固定公网](products/ecs/documents/user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](products/ecs/documents/user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[转为弹性公网](products/ecs/documents/user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](products/ecs/documents/user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)。

- 

可能持续计费：未设置随实例释放的云盘、弹性公网IP（EIP）、云盘快照等独立云资源不会被删除，并会继续计费。

规避方法：释放实例后，通过[账单](products/ecs/documents/view-billing-details.md)辅助排查并手动释放其余资源。

## 释放按量付费实例

## 控制台

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，选择目标实例所在地域与资源组。

- 

单击目标实例操作列下的实例状态>释放。

- 

在释放实例对话框中，选择释放设置后单击下一步。

- 

立即释放：在确认后立即开始释放流程。

- 

定时释放：在设定的时间自动执行释放。[取消方法](products/ecs/documents/user-guide/release-an-instance.md)

- 

仔细阅读界面提示，并确认释放与保留的关联资源，确认无误后单击确认。实例会根据释放设置释放实例。

## API

- 

释放一台ECS实例：[删除实例](products/ecs/documents/developer-reference/api-ecs-2014-05-26-deleteinstance.md)。

- 

释放一台或多台ECS实例：[批量删除实例](products/ecs/documents/developer-reference/api-ecs-2014-05-26-deleteinstances.md)。

## 释放包年包月实例

重要

只能释放已过期或已退款停机的包年包月实例，未过期的包年包月实例释放前需先[退订](products/ecs/documents/refund-instructions.md)。

## 控制台

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，选择目标实例所在地域与资源组。

- 

单击目标实例操作列下的实例状态>释放。

- 

在释放实例对话框中，选择释放设置为立即释放，单击下一步。

- 

仔细阅读界面提示，并确认释放与保留的关联资源，确认无误后单击确认释放。

## API

- 

释放一台ECS实例：[删除实例](products/ecs/documents/developer-reference/api-ecs-2014-05-26-deleteinstance.md)。

- 

释放一台或多台ECS实例：[批量删除实例](products/ecs/documents/developer-reference/api-ecs-2014-05-26-deleteinstances.md)。

释放已过期或已退款停机的包年包月实例时，需指定TerminateSubscription=true。

## 实例释放保护

启用后，系统将拒绝所有通过控制台、API或CLI发起的手动释放请求，以防止实例因人为误操作或恶意行为被意外释放。

此功能仅支持按量付费实例，且仅针对手动释放操作，在以下由系统自动触发的释放场景中不会生效：

- 

账号欠费导致实例被回收。

- 

预设的定时释放任务到期。

- 

实例因违反[云平台安全规则](https://help.aliyun.com/zh/document_detail/467859.html)（例如利用ECS经营非法网站）被强制释放。

- 

实例所在的弹性伸缩组触发自动缩容。

开启释放保护

## 控制台

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，选择目标实例所在地域与资源组。

- 

单击目标实例操作列下的实例状态>开启实例释放保护

- 

在弹出的对话框中，单击开启保护。

## API

调用[ModifyInstanceAttribute](products/ecs/documents/developer-reference/api-ecs-2014-05-26-modifyinstanceattribute.md)，设置DeletionProtection=true代表开启实例释放保护。

预期效果：释放实例报错InvalidOperation.DeletionProtection。

关闭释放保护

## 控制台

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，选择目标实例所在地域与资源组。

- 

单击目标实例操作列下的实例状态>关闭实例释放保护

- 

在弹出的对话框中，单击关闭保护。

## API

调用[ModifyInstanceAttribute](products/ecs/documents/developer-reference/api-ecs-2014-05-26-modifyinstanceattribute.md)，设置DeletionProtection=false。

查看释放保护状态

## 控制台

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，选择目标实例所在地域与资源组。

- 

单击目标实例ID进入实例详情页，在其他信息区域查看释放保护状态。

## API

调用[DescribeInstances](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstances.md)，查看Instances.Instance.DeletionProtection，为true则代表已开启实例释放保护。

## 应用于生产环境

在生产环境中，可遵循以下最佳实践，保证资源安全：

- 

强制开启释放保护：为所有生产环境实例强制开启释放保护，防止因人为误操作或恶意行为导致核心资产被意外删除。

- 

权限控制：仅为必要人员授予释放实例的权限（ecs:DeleteInstance和ecs:DeleteInstances）。同时，将修改实例属性（关闭释放保护）的权限（ecs:ModifyInstanceAttribute）与删除实例的权限分离，交由不同角色管理。

- 

操作审计：启用[操作审计](https://help.aliyun.com/zh/actiontrail/product-overview/what-is-actiontrail)服务，记录所有账号内的操作，为DeleteInstance和ModifyInstanceAttribute等高危事件配置告警规则，以便在发生此类操作时立即收到通知，从而进行追踪、审计和快速响应。

## 常见问题

- 为什么实例“释放”按钮是灰色，无法点击？

可能实例是未到期的包年包月实例，此实例释放前需先[退订](products/ecs/documents/refund-instructions.md)。

- “停止”实例和“释放”实例有什么区别？

这是两个完全不同的概念。

- 

停止：类似于关机，可以随时启动实例恢复运行。

- 

释放：类似于删除和销毁。实例、本地盘、系统盘及部分数据盘（开启了随实例释放）将被永久删除，数据无法恢复。操作后，该资源将从实例列表移除。

- 能恢复一台刚刚被误释放的实例吗？

不能。释放实例是永久性、不可撤销操作。系统不会保留已释放实例的任何数据或配置，也无法通过技术手段恢复。请严格遵守先备份、后释放的原则。

- 释放了实例，但为什么还在扣费？

释放实例不等于释放所有关联资源。可通过[账单](products/ecs/documents/view-billing-details.md)排查是否有关联的独立云盘、弹性公网IP（EIP）或快照等资源仍在计费。

- 如何批量释放实例？

- 

控制台：[在实例列表页执行批量操作](products/ecs/documents/user-guide/batch-operation-of-ecs-instances-through-the-ecs-console.md)

- 

API：[批量删除实例](products/ecs/documents/developer-reference/api-ecs-2014-05-26-deleteinstances.md)

- 释放实例时了定时释放，如何取消？

在[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)单击实例ID进入实例详情页，在基本信息>自动释放时间中，单击取消。

[上一篇：续费变配](products/ecs/documents/user-guide/renewal-change.md)[下一篇：镜像](products/ecs/documents/user-guide/images-4.md)

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
