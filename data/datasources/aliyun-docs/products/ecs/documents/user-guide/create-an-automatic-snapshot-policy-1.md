# 创建自动快照策略周期性地为云盘创建快照备份数据-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/create-an-automatic-snapshot-policy-1

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

# 创建自动快照策略

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

通过自动快照策略，系统将周期性地为指定的云盘创建快照，避免因人为疏忽忘记创建快照，降低数据丢失风险，提高系统的可靠性和稳定性。同时，支持设置跨地域复制快照，即使发生地域性的灾难或故障，仍可在其他地域快速恢复数据。本文介绍如何创建自动快照策略。

## 前提条件

已开通快照服务。具体操作，请参见[开通快照](products/ecs/documents/user-guide/activate-ecs-snapshot.md)。

## 操作步骤

说明

如果您在当前地域没有任何快照策略，系统将在您首次为云盘指定策略时创建默认策略（default_policy），您可以根据业务需求使用默认策略或者创建自定义策略。

- 

访问[ECS](https://ecs.console.aliyun.com/autoSnapshotPolicy/region)[控制台-自动快照策略](https://ecs.console.aliyun.com/autoSnapshotPolicy/region)。

- 

在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

在自动快照策略页签中单击创建自动快照策略。

- 

在创建自动快照策略页面，设置自动快照策略参数，并单击确定。

策略信息

设置自动快照策略的名称、执行时间、快照保留时间等信息。

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

| 参数 | 说明 |
| --- | --- |
| 策略名称 | 自定义自动快照策略的名称。 |
| 重复日期 | 创建自动快照的日期，支持在周一至周日之间选择一个或多个日期。 |
| 开始时间 | 自动快照的创建时间点。使用 UTC+8 时间，单位为小时。 自动快照将在 开始时间 后的一个小时内进行创建。 当一天内需要创建多次自动快照时，可以在 00:00~23:00 共 24 个整点中选择多个时间点。 重要 创建快照会暂时降低块存储 I/O 性能，一般性能差异在 10%以内，可能会出现短暂瞬间变慢。建议您选择避开业务高峰的时间点。 |
| 保留时间 | 设置自动快照的保留时间。系统默认持续保留，您也可以自定义时长。 自定义时长 ：快照超过自定义的保留时间后，将被系统自动删除。 持续保留，直至快照数量达到额度上限后被自动删除 ：在自动快照数量达到上限后，系统会自动删除最早创建的自动快照。 说明 选择自定义保留时间后，当快照的保留时间还剩 3 天时，快照列表的 保留时间 列会高亮提示 xx 天后自动释放 。您可以根据需要在快照到期前延长快照的保留时间，操作请参见 [延长快照保留时间](products/ecs/documents/user-guide/extend-the-snapshot-retention-period.md) 。 自动快照的额度上限，请参见 [使用限制](products/ecs/documents/user-guide/snapshot-overview.md) 。 快照策略创建完成后，后续您可以通过 [修改自动快照策略](products/ecs/documents/user-guide/modify-an-automatic-snapshot-policy.md) 调整保留时间。调整保留时间不影响已有的快照，只会对新创建的自动快照生效。例如已有快照保留时间是 20 天，修改快照策略后快照保留时间是 10 天，新自动快照策略不会影响已有快照的保留时间。 如果 [设置自动快照随云盘释放](products/ecs/documents/user-guide/enable-or-disable-an-automatic-snapshot-policy.md) 属性，当释放云盘（手动释放云盘、云盘随实例释放或更换系统盘）时，即使快照未到期，自动快照也会随云盘释放而提前删除。 无论快照是自定义保留时间还是永久保留，您可以按需删除快照，避免持续产生快照存储费用。具体操作，请参见 [删除快照](products/ecs/documents/user-guide/delete-a-snapshot-1.md) 。 |


跨地域复制策略

重要

- 

快照复制后，会在目标地域生成一份快照副本，因此会产生跨地域的流量费用。同时，目标地域的快照副本会根据容量与存储时间收取快照存储费用。更多信息，请参见[快照计费](products/ecs/documents/snapshots-1.md)。

- 

关于复制快照更多信息，请参见[复制快照](products/ecs/documents/user-guide/copy-a-snapshot.md)。

- 

- 

| 参数 | 说明 |
| --- | --- |
| 快照跨地域复制 | 启用后，通过该自动快照策略创建的快照将自动复制到目标地域，以实现数据的备份和容灾。 |
| 目标地域 | 选择快照需要复制到的目标地域。 |
| 复制快照的保留时间 | 复制的副本快照在目标地域中的保留时间。 |
| 加密复制 | 不启用：如果您的源端快照为加密快照，系统将会使用密钥管理服务 KMS 在目标地域创建的服务密钥将快照加密复制到目标地域；如果您的源端为非加密快照，则直接复制到目标地域。 启用：无论您的源端快照是否为加密快照，均可以将创建的自动快照基于指定的密钥加密复制到目标地域。 关于 ECS 加密密钥的更多说明，请参见 [加密云盘](products/ecs/documents/user-guide/encryption-overview.md) 。 |


高级配置

| 参数 | 说明 |
| --- | --- |
| 标签 | 选择已有的标签键和标签值，或输入新的标签键和标签值，通过该自动快照策略创建的自动快照默认绑定该标签。关于标签的更多信息，请参见 [标签](products/ecs/documents/user-guide/label-overview.md) 。 自动快照策略的标签创建后支持修改。更多信息，请参见 [编辑自动快照策略标签](products/ecs/documents/user-guide/edit-the-tags-of-an-automatic-snapshot-policy.md) 。 |
| 资源组 | 选择已有的资源组，实现对快照策略的分组管理。关于资源组的更多信息，请参见 [资源组](products/ecs/documents/user-guide/resource-groups.md) 。 |


- 

自动快照策略创建完成后，建议立即为云盘设置该策略，实现云盘自动创建快照备份数据的能力。

具体操作，请参见[为云盘设置自动快照策略](products/ecs/documents/user-guide/enable-or-disable-an-automatic-snapshot-policy.md)。

## 相关文档

- 

您也可以通过API接口完成以下操作：

- 

创建自动快照策略：[CreateAutoSnapshotPolicy](products/ecs/documents/api-createautosnapshotpolicy.md)

- 

查询指定地域下已创建的自动快照策略信息：[DescribeAutoSnapshotPolicyEx](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeautosnapshotpolicyex.md)

- 

后续您可以根据需要修改自动快照策略信息。具体操作，请参见[修改自动快照策略](products/ecs/documents/user-guide/modify-an-automatic-snapshot-policy.md)。

[上一篇：自动快照策略](products/ecs/documents/user-guide/automatically-create-snapshots.md)[下一篇：为云盘设置自动快照策略](products/ecs/documents/user-guide/configure-multiple-automatic-snapshot-policies-for-a-cloud-disk-whitelist.md)

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
