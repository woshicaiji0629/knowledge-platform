# RDS MySQL云盘实例存储空间缩容-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/support/reduce-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-that-uses-essds

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/product-overview.md)

- [快速入门](products/rds/documents/getting-started.md)

- [操作指南](products/rds/documents/user-guide.md)

- [实践教程](products/rds/documents/use-cases.md)

- [安全合规](products/rds/documents/security-compliance.md)

- [开发参考](products/rds/documents/developer-reference.md)

- [服务支持](products/rds/documents/support.md)

[首页](https://help.aliyun.com/zh)

# RDS MySQL云盘实例存储空间缩容

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

若您需要减少RDS MySQL云盘实例的存储空间，可参考本文手动缩容，以减少资源浪费并降低成本。缩容的同时，还支持降低RDS ESSD云盘的PL等级和实例规格，优化资源配置。

## 前提条件

- 

RDS MySQL实例需满足以下条件才能缩容，您可前往实例基本信息页面查看实例信息：

- 

数据库版本：

- 

MySQL 8.4

- 

MySQL 8.0、5.7：内核小版本在20210430及以上

- 

存储类型：ESSD云盘、高性能云盘（不支持SSD云盘）

说明

SSD云盘实例请先[升级至](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md)[ESSD](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md)[云盘](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md)后，再缩容存储空间。

- 

实例架构版本：仅支持新架构（kindcode=18）版本。

说明

您可通过API（[DescribeDBInstanceAttribute](products/rds/documents/developer-reference/api-rds-2014-08-15-describedbinstanceattribute.md)）查询实例架构版本，若为旧架构（kindcode=1或3），需先[发起一次内核小版本升级操作](products/rds/documents/apsaradb-rds-for-mysql/update-the-minor-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)升级到新架构后再缩容。

- 

实例运行中，且已开启[日志备份功能](products/rds/documents/support/use-the-log-backup-feature.md)。

- 

您的阿里云账号没有未支付的续费订单。

说明

如果有未支付的续费订单，请您在RDS控制台右上方，将鼠标悬浮至费用，单击订单，在订单列表页面完成支付或作废订单。

- 

云盘版只读实例存储空间缩容时，其所属主实例的状态必须为运行中，且主实例已开启[日志备份功能](products/rds/documents/support/use-the-log-backup-feature.md)。

## 使用限制

- 

缩容频率限制：每天最多手动缩容2次存储空间，请避免频繁缩容导致服务受损。

- 

缩容条件与计算公式：

- 

仅支持在同一系列、同一架构下缩容。

- 

缩容后的最小存储空间需满足公式min{使用量*1.3，使用量+400 GB}，且不能低于当前规格允许的最小存储空间，存储空间调整步长为5 GB。

各级别云盘允许的最小存储空间+缩容示例

各级别云盘（ESSD云盘、高性能云盘）允许的最小存储空间为：

- 

ESSD PL1：20 GB

- 

ESSD PL2：500 GB

- 

ESSD PL3：1500 GB

- 

高性能云盘：10 GB

缩容示例

假设RDS MySQL实例的存储类型为ESSD PL1（允许最小存储空间为20 GB），原存储空间为2000 GB。根据不同的空间使用量，缩容后的最小空间如下：

- 

空间使用量为10 GB：根据公式计算得13 GB，小于20 GB，则最小可缩容至20 GB。

- 

空间使用量为500 GB：根据公式计算得650 GB，则最小可缩容至650 GB。

- 

空间使用量为1500 GB：根据公式计算得1900 GB，则最小可缩容至1900 GB。

- 

主实例与只读实例关系：只读实例的存储空间必须大于或等于其所属主实例的存储空间。建议先缩容主实例存储空间，再缩容只读实例的存储空间。

- 

缩容时间与业务流量：缩容时间取决于云盘使用量和业务流量。高业务流量时，建议调整本地日志保留策略（增加日志保留时间和个数），以提高缩容效率和成功率。

- 

Binlog日志要求：当实例Binlog产生较快时，需确保本地保留足够多的日志才能进行缩容。日志备份的开启方法，请参见[修改](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)[RDS](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)[备份策略](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)。

- 

备份任务注意事项：缩容过程中可能会取消正在运行的备份任务，建议等备份完成后再进行缩容。

## 影响

存储空间手动缩容会造成15秒的闪断，闪断过程中，与数据库、账号、网络等相关的大部分操作都无法执行，请尽量在业务低峰期执行缩容操作，并确保应用具备重连机制（重连机制需在您的应用程序中设置）。

## 费用

涉及费用变更，请参见[变配的计费规则](products/rds/documents/product-overview/specification-changes.md)。

## 操作步骤

## 按量付费和包年包月实例

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，单击目标实例ID。

- 

在配置信息区域，单击变更配置。

- 

（仅包年包月实例需执行此步骤）在弹出的对话框中，单击立即降配，单击下一步。

- 

设置如下缩容涉及的主要参数。

- 

- 

| 参数名称 | 说明 |
| --- | --- |
| 存储类型 | 按需选择（可选）。 |
| 实例规格 | 按需选择（可选）。 |
| 存储空间 | 滑动滑块或单击减号图标，降低存储空间大小。 说明 缩容后的最小存储空间需满足公式 min{使用量*1.3，使用量+400 GB} ，且不能低于当前规格允许的最小存储空间，存储空间调整步长为 5 GB。 |
| 切换时间 | 按需选择切换时间： 数据迁移结束后立即切换 ：立即开始迁移，迁移过程对实例无影响，迁移完成后进行切换，切换会有闪断。 可维护时间内进行切换 ：立即开始迁移，迁移过程对实例无影响，但是迁移完成后不切换，等到 [可维护时间](products/rds/documents/apsaradb-rds-for-mysql/set-the-maintenance-window-of-an-apsaradb-rds-for-mysql-instance.md) 才切换，切换会有闪断。 |


- 

阅读服务协议，单击去支付，在弹出的对话框中确认变配前后的实例信息，单击继续支付完成支付即可。

## Serverless实例

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在实例基本信息页的实例资源区域，单击存储空间右侧的修改。

- 

在弹出的面板中单击减号，缩小存储空间，单击确定，在弹出的对话框中单击确认。

说明

因为缩容需要拷贝数据，故需等待数分钟，比扩容时间稍长。扩容或缩容过程中实例状态为升降配中，完成后实例状态会变为运行中。

## 常见问题

- 

Q：云盘版RDS MySQL实例存储空间手动缩容一般闪断多久？

A：会造成15秒的闪断。闪断过程中，与数据库、账号、网络等相关的大部分操作都无法执行，请尽量在业务低峰期执行缩容操作，并确保应用具备重连机制，重连机制需要在您的应用程序中设置。

- 

Q：SSD云盘版RDS MySQL实例如何缩容？

A：SSD云盘版实例暂不支持缩容，且目前[SSD](products/rds/documents/apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[云盘已停止售卖](products/rds/documents/apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)。您可以将SSD云盘升级到ESSD云盘后，再参见本文操作进行缩容。

## 相关文档

- 

您可以[修改实例的其他配置](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。

- 

您可以通过[ModifyDBInstanceSpec](products/rds/documents/api-change-instance-configuration.md)接口缩容云盘的存储空间，将DBInstanceStorage参数值修改为缩容的目标空间值，其他参数请按需配置即可。

- 

如需缩容高性能本地盘实例的存储空间，请参见[变更配置](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。

[上一篇：只读实例/读写分离](products/rds/documents/support/read-only-instances-and-read-or-write-splitting.md)[下一篇：账号/权限](products/rds/documents/support/account-or-permission.md)

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
