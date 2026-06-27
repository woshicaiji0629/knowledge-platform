# 通过数据按时间点恢复功能恢复数据-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/use-data-flashback-to-restore-data-by-point-in-time

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/redis/documents/product-overview.md)

- [快速入门](products/redis/documents/getting-started.md)

- [Tair AI能力](products/redis/documents/tair-ai-ability.md)

- [操作指南](products/redis/documents/user-guide.md)

- [实践教程](products/redis/documents/use-cases.md)

- [安全合规](products/redis/documents/security-compliance.md)

- [开发参考](products/redis/documents/developer-reference.md)

- [服务支持](products/redis/documents/support.md)

- [视频专区](products/redis/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 按时间点恢复数据

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

开启数据按时间点恢复后，在备份文件的保存期内（最长7天），您可以将实例整体或指定Key的数据恢复至某个秒级的时间点（PITR，point-in-time recovery），同时支持选择将数据恢复至新实例或当前实例。数据按时间点恢复功能提供方便快捷、更精细化的数据恢复能力，能最大程度地降低误操作带来的数据损失，保护您的数据安全。您可以将Tair（企业版）实例作为持久化存储引擎。

## 数据按时间点恢复功能概述

为保护您在云上的业务数据，Tair（企业版）除支持通过RDB快照执行数据备份和恢复以外，提供了数据按时间点恢复功能，优化基于AOF（Append-only-file）的持久化机制，将AOF增量归档，提升了实例的运维便捷性。

开启数据按时间点恢复功能：Tair（企业版）会先创建一个全量备份，并记录每一个写操作的时间戳。随着实例不断触发AOF Rewrite操作，Tair（企业版）会连续备份每个AOF文件。

执行数据按时间点恢复：Tair（企业版）会获取距离指定时间点最近的全量备份，然后通过回放连续的AOF文件至您要求恢复的指定时间点（秒级）。

- 

当选择恢复全量数据时，仅支持恢复至新实例中。

- 

当选择恢复指定Key时，支持恢复至原实例中，但仅经典版实例支持该功能。实例会删除指定Key，再根据备份集将指定Key恢复至指定时间点，对实例中其他Key数据不产生影响。

## 前提条件

- 

实例的部署模式为云原生版，产品系列为Tair（企业版）[内存型](products/redis/documents/product-overview/dram-based-instances.md)、[持久内存型](products/redis/documents/product-overview/persistent-memory-optimized-instances-1.md)或[磁盘型](products/redis/documents/product-overview/essd-based-instances-1.md)[SSD](products/redis/documents/product-overview/essd-based-instances-1.md)[型](products/redis/documents/product-overview/essd-based-instances-1.md)。

- 

实例的部署模式为经典版，产品系列为Tair（企业版）[内存型](products/redis/documents/product-overview/dram-based-instances.md)，并且实例架构为标准架构或集群架构。

说明

您可以在控制台查看实例的实例规格信息，确认实例架构。

## 使用限制

- 

由于开启数据按时间点恢复功能后，系统需要上传相关的数据与日志，请勿在开启后立即使用，如需使用此功能请提前开启。

- 

可恢复的时间范围为当前时间点至数据按时间点恢复功能开启的时间点（最长为7天）。

- 

开启数据按时间点恢复功能后，如下操作会关闭数据按时间点恢复功能或影响可恢复的时间点。

- 

若变配实例的架构（例如从标准架构变配至集群架构等）、迁移可用区操作，数据按时间点恢复功能将关闭，如需继续使用请重新配置。

- 

若新增或删减了集群架构的分片数，数据按时间点恢复功能备份的新、老节点数据可能会不一致，如需继续使用请重新配置。

- 

若执行了变更配置、升级小版本等操作，可恢复的时间点将以完成变更配置的时间点为起点。

- 

云原生版实例仅支持恢复全量数据至新实例中，不支持恢复指定Key。

- 

当实例的写入速率超过20MB/s时，可能会导致AOF文件归档不及时或者归档失败。若AOF文件归档失败，从AOF文件归档失败到下一次完成全量备份开始之前，这段时间段无法进行数据按时间点恢复。

- 

默认情况下，实例会在备库上进行数据备份，但实例若开启了本功能，则会在实例主库进行数据备份。

## 费用说明

数据按时间点恢复功能处于试用期，目前可免费恢复7天内的数据，正式推出后将根据恢复的时间点收取费用，请关注本文或官网公告。

说明

执行数据按时间点恢复时，如果选择恢复至新实例，系统将创建一个新的实例并将数据恢复至该实例（可选择付费类型为按量付费，验证完成后释放），您需要为新实例支付相关费用，详情请参见[计费项](products/redis/documents/product-overview/billable-items.md)。

## 开启数据按时间点恢复

- 

访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏，单击备份与恢复。

- 

在备份与恢复页面，单击数据闪回页签。

- 

单击马上开启。

由于系统需要上传相关的数据与日志，开启数据按时间点恢复功能需要一定时间，控制台将显示预计完全开启的时间点。

重要

在数据按时间点恢复功能完全开启后，写入的数据才能被按时间点恢复。

## 执行数据按时间点恢复

- 

访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏，单击备份与恢复。

- 

在备份与恢复页面，单击数据闪回页签。

- 

单击马上闪回，在弹出的界面中完成按时间点恢复配置。

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

| 参数 | 说明 |
| --- | --- |
| 闪回数据 | 全量数据 ：恢复实例中的所有数据。 指定 Key ：指定要恢复的 Key，每行填写 1 个 Key 名，支持正则表达式，例如： 英文句号（.）：匹配除 '\r\n' 之外的任何单个字符。 星号（*）：匹配前面子表达式任意次，例如 h.*llo 将匹配 hllo 或 heeeello 等。 英文问号（?）：表示匹配前面子表达式零次或 1 次，例如 h.?llo 将匹配 hllo 或 hello 。 字符集合[characters]：匹配方括号内任意一个字符，例如 h[ae]llo 将匹配 hallo 或 hello 。 负值字符集合[^characters]：不匹配方括号内任意一个字符，例如 h[^ae]llo 将匹配 hcllo 或 hdllo ，但不匹配 hallo 或 hello 。 字符范围[character1-character2]：匹配 character1-character2 范围内的字符，例如 h[a-b]llo 将匹配 hallo 和 hbllo 。 说明 为避免影响数据恢复的速度，推荐指定的 Key 不超过 10 个，如果是带正则表达式的 Key，不超过 3 个。 |
| 恢复模式 | 新建实例 ：将数据恢复至新实例。 原实例 ：将数据恢复至当前实例。 |
| 闪回时间点 | 指定按时间点恢复时间点（即数据要恢复到的时间点）。 |
| 过期 KEY 时间处理方式 | 当恢复 经典 版实例时，不论您选择恢复全量数据或指定 Key，您都可以对 Key 的过期时间进行偏移处理。 默认 ：对 Key 的过期时间不进行处理，若 Key 在提交本次恢复任务时已过期，将无法被恢复。 时间偏移 ：对 Key 的过期时间进行偏移处理，同时您还需 设置过期偏移时间 。实例会在设置的过期偏移时间点开始计算 Key 在指定 闪回时间点 剩余的过期时长。 例如按时间点恢复时，指定某 Key 的 闪回时间点 为 2022 年 12 月 12 日 10:00:00，设置其过期偏移时间为 2022 年 12 月 12 日 10:30:00。若在 2022 年 12 月 12 日 10:00:00 时该 Key 的剩余过期时长为 10s，则该 Key 将于 2022 年 12 月 12 日 10:30:10 过期。 说明 该功能仅支持偏移 Key 级别的过期时间，不支持偏移 Tair 自研数据结构中 Key 内部的过期时间，例如 exHash 的 Field、TS 的 Skey 等。 设置过期偏移时间 不能早于指定的 闪回时间点 ，也不能晚于提交恢复任务的时间点。 |


- 

单击确定。

- 

选择恢复模式为原实例时，当前实例将进入备份恢复中状态，等待实例状态变更为运行中即可。

- 

选择恢复模式为新建实例时，您需要在跳转到的克隆实例，选择备份时间点（即数据要恢复到的时间点）和新实例的配置。

说明

新实例的架构需选择为标准版或集群版，且实例规格的容量需大于等于原实例，关于创建实例的各参数的解释，请参见[创建](products/redis/documents/getting-started/step-1-create-an-apsaradb-for-redis-instance.md)[Redis](products/redis/documents/getting-started/step-1-create-an-apsaradb-for-redis-instance.md)[实例](products/redis/documents/getting-started/step-1-create-an-apsaradb-for-redis-instance.md)。

## 相关API

| API 接口 | 说明 |
| --- | --- |
| [ModifyBackupPolicy](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-modifybackuppolicy-redis.md) | 修改实例的自动备份策略，可通过 EnableBackupLog 参数开启或关闭数据按时间点恢复功能。 同时，您还需确保已在实例的参数设置中开启 AOF 持久化（appendonly 为 yes），开启后才能使用数据按时间点恢复功能，更多信息请参见 [Tair](products/redis/documents/user-guide/parameter-support.md) [企业版配置参数列表](products/redis/documents/user-guide/parameter-support.md) 。 |
| [RestoreInstance](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-restoreinstance-redis.md) | 将备份文件中的数据恢复到当前实例中，结合数据按时间点恢复更可实现将指定的 Key 恢复至某个秒级时间点。 |


[上一篇：从备份集恢复至新实例](products/redis/documents/user-guide/restore-data-from-a-backup-set-to-a-new-instance.md)[下一篇：下载备份集](products/redis/documents/user-guide/download-a-backup-file.md)

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
