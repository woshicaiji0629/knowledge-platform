# 分担数据库压力满足大量读取需求-只读实例-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/rds-for-postgresql-read-only-instances/

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-postgresql/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-postgresql/getting-started.md)

- [DuckDB分析加速](products/rds/documents/apsaradb-rds-for-postgresql/duckdb-analytics-acceleration.md)

- [RDS for AI](products/rds/documents/apsaradb-rds-for-postgresql/rds-for-ai.md)

- [自研内核 AliPG](products/rds/documents/apsaradb-rds-for-postgresql/proprietary-alipg.md)

- [插件](products/rds/documents/apsaradb-rds-for-postgresql/plug-ins-1.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-postgresql/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-postgresql/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-postgresql/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-postgresql/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-postgresql/support.md)

[首页](https://help.aliyun.com/zh)

# 只读实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在少量写请求，但有大量读请求场景下，单个实例可能无法承受读取压力。您可以创建一个或多个只读实例来分担数据库压力，满足大量读取需求，增加应用的吞吐量。

## 简介

创建只读实例时会从备实例复制数据，数据与主实例一致。主实例的数据更新会自动同步到所有只读实例。

说明

- 

高性能本地盘主实例最多可创建5个只读实例，云盘主实例最多可创建32个只读实例。

- 

高性能本地盘实例的只读实例为高可用架构。

- 

云盘实例的只读实例为单节点架构，没有备节点，无法保障可用性。建议您购买多个只读实例，并使用libpq或JDBC实现自动故障转移，详情请参见[自动故障转移和读写分离](products/rds/documents/apsaradb-rds-for-postgresql/configure-automatic-failover-and-read-or-write-splitting.md)。您也可以通过数据库代理实现读写自动分离，更多信息，请参见[什么是数据库代理](products/rds/documents/apsaradb-rds-for-postgresql/what-are-database-proxies.md)。

只读实例拓扑图如下图所示。

## 应用场景

- 

单个实例负载过大时，可以创建只读实例，将读请求转发至只读实例，以缓解主实例负载。

- 

主实例因备份或维护等原因暂不可用时，可将读请求转发至只读实例，保证部分业务的正常运行。

- 

报表分析等场景中，使用只读实例查询分析大量数据，不影响主实例。

- 

读写分离场景中，避免读写锁争抢问题，提升系统的性能和吞吐。

## 计费

支持包年包月和按量付费两种方式计费。包年包月费用请以实际购买页为准，按量付费具体费用请参见[只读实例规格列表](products/rds/documents/product-overview/read-only-apsaradb-rds-instance-types.md)。

## 功能特点

- 

地域和可用区：与主实例在同一地域，可以在不同的可用区。

- 

[更改网络类型](products/rds/documents/apsaradb-rds-for-postgresql/change-the-network-type-of-an-apsaradb-rds-for-postgresql-instance.md)：可以与主实例不一致。

- 

账号与数据库管理：不需要维护账号与数据库，全部通过主实例同步。

- 

白名单：只读实例创建时会自动复制其主实例的白名单信息，但两者白名单相互独立。若您需要修改只读实例的白名单，请参见[设置白名单](products/rds/documents/apsaradb-rds-for-postgresql/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance.md)。

- 

监控与报警：提供系统性能指标的监控视图，如磁盘容量、IOPS、连接数、CPU使用率等。

- 

自动读写分离：配合主实例数据库代理功能，可使写请求自动转发到主实例，读请求自动转发到各个只读实例，实现读写请求的自动分流，减轻主实例的压力。若您需要为主实例开通数据库代理功能，请参见[什么是数据库代理](products/rds/documents/apsaradb-rds-for-postgresql/what-are-database-proxies.md)。

- 

只读实例的数量：云盘主实例最多创建32个只读实例，高性能本地盘主实例最多创建5个只读实例。

## 注意事项

- 

实例备份：因主实例已有备份，只读实例暂不支持备份设置以及手动发起备份。

- 

数据迁移：不支持将数据迁移至只读实例。

- 

数据库管理：不支持创建或删除数据库。

- 

账号管理：不支持创建或删除账号，不支持为账号授权以及修改账号密码功能。

- 

规格及存储空间：

- 

云盘：只读实例的存储空间不能低于主实例。如果主实例内存大于只读实例内存，主实例变配时会重启只读实例。

- 

高性能本地盘：只读实例的规格和存储空间不能低于主实例。

- 

只读实例出现内核复制或其他不可预见的错误时，会重搭该只读实例。

- 

主实例被释放后，包年包月只读实例自动退款并释放，按量付费只读实例直接释放。

## 常见问题

- 

Q：只读实例的计费方式可以转化吗？

A：可以。具体操作，请参见[按量付费转包年包月](products/rds/documents/apsaradb-rds-for-postgresql/switch-an-apsaradb-rds-for-postgresql-instance-from-pay-as-you-go-to-subscription.md)或[包年包月转按量付费](products/rds/documents/apsaradb-rds-for-postgresql/package-year-package-month-to-pay-by-volume.md)。

- 

Q：变更只读实例的配置、释放只读实例、转化只读实例计费方式会影响主实例吗？

A：不会。

- 

Q：主实例上创建的账号在只读实例上可以用吗？

A：主实例创建的账号会同步到只读实例，只读实例无法管理账号。账号在只读实例上只能进行读操作，不能进行写操作。

- 

Q：只读实例可以转变为常规实例吗？比如作为容灾实例？

A：暂不支持。

- 

Q：能否对只读实例的数据进行备份？实例的自动备份能否在只读实例上进行？

A：无需对只读实例进行备份，备份在主实例上进行，由于RDS PostgreSQL的备份使用快照备份，对主实例没有性能开销。

- 

Q：只读实例是否支持并行复制？

A：RDS PostgreSQL采用的是物理流复制，基于WAL日志文件同步加回放来实现数据复制能力，效率高，无需使用并行复制。

- 

Q：事务日志的清除机制是怎样的？

A：RDS PostgreSQL的WAL日志备份完成后，由内核在Checkpoint操作中自动清理。

- 

Q：如何通过只读实例延迟时间判断复制是否正常？

A：通常情况下只读实例延迟时间在1秒以内，如果超过1秒，说明数据同步延迟，极端场景下也可能出现断开的场景。

- 

Q：复制延迟通常是什么原因引起的？

A：常见原因及解决办法如下：

- 

原因1：主实例规格大，只读实例规格过小，导致主备延迟过大。

解决方法：升级只读实例规格，更多信息，请参见[变更配置](products/rds/documents/apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)。

- 

原因2：参数max_standby_streaming_delay设置不合理，导致复制延迟较高。参数设置方法，请参见[设置实例参数](products/rds/documents/apsaradb-rds-for-postgresql/modify-the-parameters-of-an-apsaradb-rds-for-postgresql-instance.md)。

解决办法：调整参数max_standby_streaming_delay取值：

- 

该值设置较小时可以减少只读实例与主实例之间数据复制延迟，但过小时可能会导致只读实例的事务被取消。

- 

该值设置过大时可能会造成复制延迟。

[上一篇：实例回收站](products/rds/documents/apsaradb-rds-for-postgresql/manage-apsaradb-rds-for-postgresql-instances-in-the-recycle-bin.md)[下一篇：创建PostgreSQL只读实例](products/rds/documents/apsaradb-rds-for-postgresql/create-a-read-only-apsaradb-rds-for-postgresql-instance.md)

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
