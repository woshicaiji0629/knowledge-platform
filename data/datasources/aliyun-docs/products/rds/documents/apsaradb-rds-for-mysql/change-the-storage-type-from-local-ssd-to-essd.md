# 变更高性能本地盘至云盘-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/change-the-storage-type-from-local-ssd-to-essd

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-mysql/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-mysql/getting-started.md)

- [AI能力中心](products/rds/documents/apsaradb-rds-for-mysql/ai-capability-center.md)

- [自研内核AliSQL](products/rds/documents/apsaradb-rds-for-mysql/proprietary-alisql.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-mysql/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-mysql/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-mysql/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-mysql/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-mysql/support.md)

[首页](https://help.aliyun.com/zh)

# 变更高性能本地盘至云盘

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以通过控制台将存储类型从高性能本地盘变更到高性能云盘或ESSD云盘，获取更好的弹性能力。

说明

欢迎您加入RDS存储能力交流钉钉群（121770005512），获取更多RDS存储能力的相关信息，您可以在群内进行咨询、交流和反馈。

## 前提条件

- 

RDS MySQL主实例仅支持如下版本：

- 

RDS MySQL 8.0或5.7高可用系列（高性能本地盘）

说明

RDS MySQL 5.6版本实例仅支持高性能本地盘，不支持其他类型的云盘，因此无法直接将5.6版本的高性能本地盘变更为云盘，但您可以通过其他方案间接实现，详情请参见[本文常见问题](products/rds/documents/apsaradb-rds-for-mysql/change-the-storage-type-from-local-ssd-to-essd.md)。

- 

实例内核小版本不低于20201031，升级方法请参见[升级内核小版本](products/rds/documents/apsaradb-rds-for-mysql/update-the-minor-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)。

- 

实例下没有[只读实例](products/rds/documents/overview-of-read-only-apsaradb-rds-for-mysql-instances.md)或[灾备实例](products/rds/documents/apsaradb-rds-for-mysql/create-a-disaster-recovery-apsaradb-rds-for-mysql-instance.md)。

- 

实例未开启[性能自动扩容](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-scale-up-feature-for-an-apsaradb-rds-for-mysql-instance.md)。

- 

实例未开启[数据库代理](products/rds/documents/apsaradb-rds-for-mysql/enable-and-configure-the-dedicated-proxy-feature-for-an-apsaradb-rds-for-mysql-instance.md)。

- 

实例的网络类型为VPC网络，且实例没有经典网络地址。

- 

实例未使用IPv6网络协议、未创建多个VPC。（正常情况下无需关注，仅针对特殊场景）

- 

实例的状态为运行中。

说明

如果您的实例受上述前提条件所限无法变更存储类型，可以通过创建一个高性能云盘或ESSD云盘的新实例，将旧实例数据迁移到新实例的方式进行变更。更多信息，请参见[RDS](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-between-apsaradb-rds-for-mysql-instances.md)[实例间数据迁移](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-between-apsaradb-rds-for-mysql-instances.md)。

## 高性能本地盘和云盘的区别

- 

- 

- 

- 

- 

- 

| 对比项 | 高性能本地盘 | 高性能云盘 | ESSD 云盘 |
| --- | --- | --- | --- |
| I/O 性能 | ★★★★★ IO 延迟低，性能好： IOPS：由实例规格决定。 IO 延迟：10~50 微秒 | ★★★★★★ 提供了 [Buffer Pool Extension（BPE）功能](products/rds/documents/apsaradb-rds-for-mysql/buffer-pool-extension-bpe.md) 、 [IO](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) [性能突发功能](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) 和 [数据归档功能](products/rds/documents/apsaradb-rds-for-mysql/rds-mysql-data-archiving-function.md) 三种功能。IO 性能如下： IOPS：由磁盘规格及实例规格共同决定。 IO 延迟：100~200 微秒 | ★★★★★ 相对 SSD 云盘有大幅提升： IOPS：由磁盘规格及实例规格共同决定。 IO 延迟：100~200 微秒 |
| 规格配置灵活性 | ★★★★ 可选配置较多，磁盘空间可单独调整。仅部分高性能本地盘实例的磁盘空间大小与实例规格绑定，无法单独调整。 | ★★★★★ 可选配置较多，支持扩容或缩容磁盘空间。 说明 仅 MySQL 部分满足条件的实例支持缩容，具体请参见 [实例变更项概览](products/rds/documents/apsaradb-rds-for-mysql/configuration-items-for-an-apsaradb-rds-for-mysql-instance.md) 和 [变更配置](products/rds/documents/apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md) 。 | ★★★★★ 可选配置较多，支持扩容或缩容磁盘空间。 说明 仅 MySQL 部分满足条件的实例支持缩容，具体请参见 [实例变更项概览](products/rds/documents/apsaradb-rds-for-mysql/configuration-items-for-an-apsaradb-rds-for-mysql-instance.md) 和 [变更配置](products/rds/documents/apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 备份方法 | Xtrabackup 物理备份 | ESSD 云盘快照备份 | ESSD 云盘快照备份 |
| 备份、只读实例创建、实例克隆操作速度 | ★★★ 与磁盘大小相关，耗时为小时级。 | ★★★★★ 耗时为秒级。 | ★★★★★ 耗时为秒级。 |
| 扩容时长 | ★★★★ 需要拷贝数据，可能需要几个小时。 | ★★★★★ 在线升级，秒级扩容。 | ★★★★★ 在线升级，秒级扩容。 |
| 扩容影响 | 有闪断。 | 无影响。 | 无影响。 |
| 数据持久性 | ★★★★ 硬件故障有一定概率导致数据损坏，需要有备库保障。高可用系列本地盘实例 SLA 可达 99.995%。 | ★★★★★ 数据可靠性达到 99.9999999%，支持单节点基础版形态，降低成本。 | ★★★★★ 数据可靠性达到 99.9999999%，支持单节点基础版形态，降低成本。 |


## 费用说明

实例所在地域和所选配置会影响变更存储类型的费用，变配时可查看费用信息。

## 注意事项

- 

仅支持高性能本地盘到高性能云盘或ESSD云盘的单向变更，不支持逆向操作。

- 

高性能本地盘与ESSD云盘支持的实例规格存在差异，部分规格的高性能本地盘实例变更为ESSD云盘时，需要变更实例规格。实例规格列表请参见[RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md)[标准版（原](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md)[X86）主实例规格列表](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md)。

- 

变更存储类型受多种因素影响，无法保证100%升级成功。影响因素请参见[RDS MySQL](products/rds/documents/support/which-factors-affect-the-time-that-is-required-to-change-the-specifications-of-my-apsaradb-rds-for-mysql-instance.md)[实例变配时长受哪些因素影响？](products/rds/documents/support/which-factors-affect-the-time-that-is-required-to-change-the-specifications-of-my-apsaradb-rds-for-mysql-instance.md)。

- 

变更存储类型以增量数据同步的方式实现，若该过程中业务仍在写入大量数据，可能出现目标端数据无法追平源端的情况，导致存储类型变更无法结束。建议在升级期间降低数据写入频率，快速完成存储类型的变更。

- 

变更存储类型前请预留10%以上存储空间，防止磁盘空间写满导致实例锁定。实例锁定的解决方法，请参见[RDS MySQL](products/rds/documents/support/what-do-i-do-if-an-apsaradb-rds-for-mysql-instance-is-in-the-locked-state-because-its-storage-capacity-is-exhausted-by-data-files.md)[数据文件占满磁盘空间导致出现“锁定中”状态](products/rds/documents/support/what-do-i-do-if-an-apsaradb-rds-for-mysql-instance-is-in-the-locked-state-because-its-storage-capacity-is-exhausted-by-data-files.md)。

## 影响

- 

变更存储类型可能涉及底层数据迁移，请耐心等待。迁移完成后会根据设置的切换时间自动切换，此时会有约15秒的闪断。请在业务低峰期升级，并确保应用有自动重连机制。

说明

变更存储类型不会改变实例连接地址，应用侧无需修改。

- 

变更存储类型成功后，原高性能本地盘实例的备份集无法用于恢复升级后的高性能云盘或ESSD云盘实例，如需进行恢复操作，请使用存储类型变更后新生成的备份集。

- 

变更存储类型期间无法对该实例执行升降配、版本升级、跨可用区迁移等实例级别的操作。

- 

由于存储类型底层架构间的差异影响，高性能本地盘变更为云盘将导致实例原有的全量跨地域备份功能失效（自动关闭），建议您在变更完成后，及时重新配置跨地域备份策略，以确保跨地域备份能力的正常进行。如何开启，请参见[跨地域备份](products/rds/documents/apsaradb-rds-for-mysql/use-the-cross-region-backup-feature-of-an-apsaradb-rds-for-mysql-instance.md)。

## 操作步骤

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在基本信息区域，单击配置信息右侧的变更配置。

- 

在跳转的变配实例页面，选择存储类型。您可以选择高性能云盘或ESSD 云盘（PL1、PL2或PL3）。

部分可用区可能资源不足或暂时关闭云盘售卖的情况，因此可能无法选择存储类型为云盘。在这种情况下，请将实例[迁移至支持售卖云盘的可用区](products/rds/documents/apsaradb-rds-for-mysql/migrate-an-apsaradb-rds-for-mysql-instance-across-zones-in-the-same-region.md)后，再升级至云盘。

说明

- 

三种ESSD云盘的性能说明如下：

- 

性能排序：PL3＞PL2＞PL1。

- 

PL3比PL1最高提升20倍IOPS、11倍吞吐。

- 

PL2比PL1最高提升2倍IOPS和吞吐。

- 

需要注意PL3、PL2、PL1对应的最小磁盘空间不同，PL3为1500 GB、PL2为500 GB、PL1为20 GB。

- 

[高性能云盘](https://help.aliyun.com/zh/document_detail/2545946.html)最小磁盘空间为10 GB。

- 

（可选）选择新的实例规格。

- 

先选择分类（通用或独享）。

| 分类 | 说明 | 特点 |
| --- | --- | --- |
| 通用规格 | 独享：内存和 I/O。 共享：CPU 和存储。 | 价格低，性价比高。 |
| 独享规格 | 独享：CPU、内存、存储和 I/O。 说明 独占型是独享型的顶配，独占整台服务器的 CPU、内存、存储和 I/O。 | 性能更好更稳定。 |


- 

然后选择具体规格（CPU核数和内存）。

- 

测试环境：1核或以上。

- 

生产环境：建议4核或以上。

说明

规格列表，请参见[RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md)[标准版（原](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md)[X86）主实例规格列表](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md)。

- 

（可选）根据需求选择增加或减少存储空间。

说明

云盘的存储空间容量不可低于原高性能本地盘实例使用空间的1.2倍。

- 

选择切换时间（指存储类型升级成功后，主备切换的时间）。

- 

立即执行

- 

可维护时间内进行切换：在[可维护时间段](products/rds/documents/apsaradb-rds-for-mysql/set-the-maintenance-window-of-an-apsaradb-rds-for-mysql-instance.md)内执行切换操作。

说明

- 

切换会出现约15秒的闪断，请在业务低峰期进行变配，并确保您的应用有自动重连机制。

- 

如选择可维护时间内进行切换，则实例会一直保持升降配中状态直到完成切换，在此期间无法对该实例执行升降配、版本升级、跨可用区迁移等实例级别的操作。

- 

选中服务条款，单击右下角的去支付并完成支付。

此时实例状态会变更为升降配中，等待实例状态恢复成运行中即表示变更完成。

## 常见问题

如何变更RDS MySQL 5.6高性能本地盘为ESSD云盘或高性能云盘？

由于RDS MySQL 5.6版本实例仅支持高性能本地盘，不支持其他类型的云盘，因此无法直接将5.6版本的高性能本地盘变更为云盘，但您可以选择如下方案间接实现：

- 

先[升级数据库大版本](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-major-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)

在RDS实例详情页的大版本升级页面（先创建升级检查报告再升级实例），将MySQL 5.6高性能本地盘升级为MySQL 5.7高性能本地盘或MySQL 8.0高性能本地盘，更多详情请参见[MySQL5.6](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-major-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)[升级](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-major-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)[MySQL 5.7](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-major-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)[的优势](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-major-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)。

页面提示不支持跨大版本升级（MySQL 5.6需先升级到5.7再到8.0）、升级后不支持降级，且检查失败时不允许执行升级操作。

- 

再[变更存储类型](products/rds/documents/apsaradb-rds-for-mysql/change-the-storage-type-from-local-ssd-to-essd.md)

在RDS实例详情页的基本信息页面，通过变更配置入口将MySQL 5.7高性能本地盘或MySQL 8.0高性能本地盘变更为MySQL 5.7云盘或MySQL 8.0云盘。

为什么我无法选择高性能云盘或者ESSD云盘？

部分可用区可能资源不足或暂时关闭云盘售卖的情况。若您的实例在不支持云盘售卖的可用区，请将实例[迁移至支持售卖云盘的可用区](products/rds/documents/apsaradb-rds-for-mysql/migrate-an-apsaradb-rds-for-mysql-instance-across-zones-in-the-same-region.md)后，再升级至云盘。

变更存储类型时，是否会影响线上业务？

请参见本文的[影响](products/rds/documents/apsaradb-rds-for-mysql/change-the-storage-type-from-local-ssd-to-essd.md)。

变更存储类型后，实例的地址会变化吗？

实例的连接地址（如rm-bpxxxxx.mysql.rds.aliyuncs.com）不会变化，但是对应的IP地址可能会变化。建议在应用程序中使用连接地址，而不是IP地址。

## 相关API

| API | 描述 |
| --- | --- |
| [ModifyDBInstanceSpec](products/rds/documents/api-change-instance-configuration.md) | 变更 RDS 实例配置。 |


[上一篇：升级SSD云盘至ESSD云盘](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md)[下一篇：ESSD云盘变更为高性能云盘](products/rds/documents/apsaradb-rds-for-mysql/essd-changed-to-universal-cloud-disk.md)

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
