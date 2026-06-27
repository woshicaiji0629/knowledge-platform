# 为单块系统盘或数据盘创建快照备份云盘数据-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/create-a-snapshot

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

# 手动创建单个快照

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当您进行回滚云盘、修改关键系统文件、更换操作系统等重要操作之前，建议提前为云盘（系统盘或数据盘）创建快照做好数据备份，如果操作过程中导致了未预期的问题或数据丢失，您可以通过快照来恢复数据，保证业务连续性。

说明

本文主要介绍如何为单块云盘手动创建快照。

- 

如果您需要为多块云盘同时创建快照，以确保云盘数据的一致性，可以通过[快照一致性组](products/ecs/documents/user-guide/snapshot-consistency-group-overview.md)实现。

- 

如果您需要为单块云盘自动周期性地创建快照，可以通过[自动快照策略](products/ecs/documents/user-guide/automatically-create-snapshots.md)实现。

## 前提条件

- 

已开通快照。具体操作，请参见[开通快照](products/ecs/documents/user-guide/activate-ecs-snapshot.md)。

- 

确保云盘处于使用中或待挂载状态。

- 

云盘处于使用中的状态，则实例必须处于运行中或已停止状态。

- 

云盘处于待挂载的状态，则云盘必须有过挂载到ECS实例的历史操作，从未挂载过ECS实例的云盘不支持创建快照。

说明

因为云盘从未挂载过ECS实例，数据无变化，无需创建快照。

- 

确保待创建快照的云盘支持创建快照。

说明

ESSD PL-X云盘、本地盘和弹性临时盘均不支持创建快照。

## 注意事项

创建快照前，请您了解如下注意事项：

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

| 注意项 | 说明 |
| --- | --- |
| 对性能的影响 | 在快照创建的初始瞬间（通常是几秒钟）会影响云盘 I/O 性能，一般不超过 10%。当快照有上传进度后，云盘的读写性能恢复正常，不再受到任何影响。因此建议您在业务低峰期或对 I/O 延迟不敏感的时间段创建快照，以减少对业务的影响。 |
| 创建时长 | 创建快照所需时长与该快照的数据量、其他用户同时在创建的快照数量和快照容量等多个因素有关。 快照创建完成后将默认存储在对象存储 OSS（此 OSS Bucket 用户不可见）中。快照的数据量越大，上传 OSS 所需的时间越长。 说明 云盘的第一份快照为全量快照，耗时较长。后续创建快照均是增量快照，相对耗时较短，但依然取决于和上一份快照之间的数据变化量，变化量越大，耗时越长。 每天凌晨左右一般是自动快照创建的高峰期，上传的快照数量和容量都会增加，每个快照分配到的带宽可能会变小，因此创建快照所需时间会变长。如果业务允许，建议您避开这个时间段创建快照，以获得更好的上传速度。 说明 创建快照初始所需上传时间可能会比较长，但随着时间推移，当系统中正在上传的快照数量减少时，剩余的快照可以享有更多的带宽，从而上传速度加快，预计剩余上传时间将会缩短。 |
| 计费说明 | 创建快照后，系统会在每个地域根据快照容量大小结算快照存储费用。更多信息，请参见 [快照计费](products/ecs/documents/snapshots-1.md) 。 |
| 其他事项 | 创建快照期间，请勿修改 ECS 实例状态（如停止或重启），否则会导致快照创建失败。 创建快照期间，操作云盘产生的增量数据不会备份到快照中。 正在创建快照的云盘不支持扩容。如果您有扩容云盘需求，请等待快照创建完成后再执行扩容操作。 当云盘用于创建逻辑卷或 RAID 阵列时，建议使用快照一致性组并开启应用一致性快照，以保证数据写入时序和崩溃一致性。更多信息，请参见 [快照一致性组](products/ecs/documents/user-guide/snapshot-consistency-group-overview.md) 。 手动快照和自动快照创建过程中会存在以下约束： ESSD 系列云盘（ESSD、ESSD AutoPL、ESSD Entry 和 ESSD 同城冗余） 单块云盘支持手动和自动同时并发创建快照。但是并发创建快照有最大个数限制，详情请参见 [快照使用限制](products/ecs/documents/user-guide/limitations.md) 。如果云盘并发创建的快照个数达到了上限，则后续并发创建快照会失败。 上一代云盘（SSD 云盘、高效云盘和普通云盘） 不支持手动和自动同时并发创建快照。 在自动快照创建时间点，如果云盘正在执行创建快照任务（手动或自动创建快照），则系统不会创建该时间点的自动快照，而是在下一个时间点正常创建自动快照。 如果云盘正在执行创建自动快照任务，您需要等待自动快照完成后，才能手动创建快照。 说明 手动快照和自动快照的其他区别请参见 [手动快照和自动快照有什么区别？](products/ecs/documents/data-protection-and-recovery-faqs.md) 快照创建完成后，将默认自动存储在对象存储 OSS Bucket 中（此 OSS Bucket 用户不可见），您无法选择存储快照的 OSS Bucket 或者查看快照数据。更多信息，请参见 [快照存储位置](products/ecs/documents/user-guide/snapshot-overview.md) 。 |


## 操作步骤

以下操作以在快照页面创建云盘快照为例，您也可以在云盘页面为目标云盘创建快照。

- 

访问[ECS](https://ecs.console.aliyun.com/snapshot)[控制台-快照](https://ecs.console.aliyun.com/snapshot)。

- 

在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

在云盘快照页签中单击创建云盘快照。

- 

在创建快照对话框中，设置快照参数，然后单击确认。

- 

- 

- 

- 

- 

| 参数 | 说明 |  |
| --- | --- | --- |
| 资源类型 | 默认选中 云盘 ，选择为单个云盘创建快照。 说明 您也可以选择 实例 ，从实例中选择一块或多块云盘，创建快照一致性组并在组内为多块云盘创建快照，从而确保多块云盘数据的一致性。具体操作，请参见 [创建快照一致性组](products/ecs/documents/user-guide/create-a-snapshot-consistent-group.md) 。 |  |
| 选择云盘 | 选择需要创建快照的云盘，可以是系统盘或数据盘。 |  |
| 快照名称 | 设置快照的名称。 |  |
| 保留时间 | 设置快照的保留时间，可以选择永久保留或自定义保留天数。 永久保留：在快照数量达到上限后，无法再新建快照。 自定义保留时间：快照超过保留时间后，将被系统自动删除。 说明 手动创建快照的额度上限，请参见 [快照概述](products/ecs/documents/user-guide/snapshot-overview.md) 。 如果选择自定义保留时间，当快照的保留时间还剩 3 天时，快照列表的 保留时间 列会高亮提示 xx 天后自动释放 。您可以根据需要在快照到期前延长快照的保留时间，操作请参见 [延长快照保留时间](products/ecs/documents/user-guide/extend-the-snapshot-retention-period.md) 。 无论是永久保留还是自定义保留时间，如果后续不再使用快照，建议您及时删除快照，避免持续产生快照费用。具体操作，请参见 [删除快照](products/ecs/documents/user-guide/delete-a-snapshot-1.md) 。 |  |
| 高级配置 | 极速可用 | ESSD 系列云盘（ESSD、ESSD AutoPL、ESSD Entry 和 ESSD 同城冗余） 默认开启极速可用功能，其他类型的云盘默认不开启。 说明 快照极速可用能力可实现快照创建后秒级可用，无需等待快照上传至 OSS 完成即可直接使用，例如回滚云盘、创建新云盘或共享快照等。更多信息，请参见 [快照极速可用能力](products/ecs/documents/user-guide/enable-or-disable-the-instant-access-feature.md) 。 |
| 标签 | 设置快照的标签键值对，后续您可以通过标签功能统一管理资源。 |  |
| 资源组 | 设置资源组，对快照进行分级管理。 |  |


- 

（可选）在快照列表中查看快照的创建进度。

创建的快照默认存储在对象存储OSS中。为保障数据的长期安全与灵活恢复，此OSS Bucket不可见。

- 

在进度列查看快照上传至OSS的进度，鼠标悬浮至上传至OSS：xx%时，会显示预计剩余时间。

说明

- 

快照上传预计剩余时间是动态变化的，会随着多个因素的影响而不断更新。更多信息请参考[注意事项](products/ecs/documents/user-guide/create-a-snapshot.md)中的创建时长说明。

- 

您可以通过API接口[DeleteSnapshot](products/ecs/documents/developer-reference/api-ecs-2014-05-26-deletesnapshot.md)取消正在创建的快照任务。

- 

当进度列显示上传至OSS：100%时，表示快照上传至OSS完成，云盘数据备份成功。

## 相关文档

- 

您也可以通过API接口完成以下操作：

- 

[创建快照](products/ecs/documents/developer-reference/api-ecs-2014-05-26-createsnapshot.md)

- 

[查询云盘快照列表](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describesnapshots.md)

- 

快照创建完成后，您可以通过以下几种方式使用快照：

- 

[复制快照](products/ecs/documents/user-guide/copy-a-snapshot.md)

- 

[归档快照](products/ecs/documents/user-guide/archive-snapshots.md)

- 

[共享快照](products/ecs/documents/user-guide/share-a-snapshot.md)

- 

[使用快照回滚云盘](products/ecs/documents/user-guide/roll-back-a-disk-by-using-a-snapshot.md)

- 

[使用快照创建数据盘](products/ecs/documents/user-guide/create-a-disk-from-a-snapshot.md)

- 

[使用快照创建自定义镜像](products/ecs/documents/user-guide/create-a-custom-image-from-a-snapshot-1.md)

- 

快照创建后，您可以在阿里云费用与成本中心的明细账单中，查看各地域的快照账单明细。具体操作，请参见[查看快照明细账单](products/ecs/documents/snapshots-1.md)。

- 

您可以购买[存储容量单位包](products/ecs/documents/storage-capacity-units-1.md)[SCU](products/ecs/documents/storage-capacity-units-1.md)或[OSS](products/ecs/documents/oss-storage-bag.md)[资源包](products/ecs/documents/oss-storage-bag.md)抵扣快照的存储费用。

- 

建议您定期删除不再使用的快照，以降低快照费用。具体操作，请参见[删除快照](products/ecs/documents/user-guide/delete-a-snapshot-1.md)。

- 

支持为创建快照设置事件通知，在云盘创建快照后，云服务器ECS会发送快照创建成功或失败的事件。更多信息，请参见[快照事件通知](products/ecs/documents/user-guide/snapshot-event-notifications.md)。

[上一篇：开通快照](products/ecs/documents/user-guide/activate-ecs-snapshot.md)[下一篇：自动快照策略](products/ecs/documents/user-guide/automatically-create-snapshots.md)

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
