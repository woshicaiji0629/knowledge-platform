# RDS MySQL实例变配时长影响因素分析-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/support/which-factors-affect-the-time-that-is-required-to-change-the-specifications-of-my-apsaradb-rds-for-mysql-instance

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

# RDS MySQL实例变配时长受哪些因素影响？

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

RDS MySQL实例变更配置（包括系列、规格和存储空间）时，可以根据本页面列举的影响因素预估实例变配的时长。

重要

RDS MySQL实例变更配置的时长受多种因素影响，因此，建议在业务写入量较少时进行，或在变配前停止写入数据。

RDS MySQL高性能本地盘实例变配时可能涉及跨机迁移。如果涉及跨机迁移，变配时长较长，影响变配时长的关键因素如下表所示。

说明

本文所述的跨机迁移是指系统对原RDS MySQL实例进行备份，然后恢复到新RDS MySQL实例中。

| 存储类型 | 是否涉及跨机迁移 | 影响因素 | 补充说明 |
| --- | --- | --- | --- |
| 高性能本地盘存储 | 是 | 全量数据大小 | 全量数据的大小会影响数据迁移的时长，同时迁移的速度受备份速度、网络带宽的影响。 |
| Redo Log 大小 | 当 Redo Log 较大时，会导致实际备份数据量超出预估。此情况下，恢复时的耗时将更久。 |  |  |
| 业务锁 | 数据迁移时，对原库中数据进行备份，期间会对数据对象加锁，因此，也会影响备份的速度。 |  |  |
| 表数量 | - |  |  |
| 增量数据大小 | 当全量备份传输结束后，传输期间产生的增量数据也需要应用到新的节点上，因此，迁移变配时间受增量数据大小影响。 |  |  |
| 增量数据写入速度 | 增量数据的写入速度受业务 SQL 的回放速度、是否单表操作、是否有 DDL 的影响。 |  |  |
| 数据同步延时 | 当增量数据回放结束后，需要建立新库与原库之间的同步链路。在数据库间数据完全同步后，才会进行数据库切换，因此，迁移变配时间受数据同步的延时影响，数据同步的延时与主库的写入压力、是否有 DDL、是否有多表联合查询相关。 |  |  |
| 否 | - | 当高性能本地盘存储类型 RDS MySQL 实例变配不涉及跨机迁移时，变配时间较短，无需关注影响因素。 |  |
| 云盘存储 | 否 | - | 云盘存储类型的 RDS MySQL 实例变配不会涉及跨机迁移，因此，变配时间较短，无需关注影响因素。 |


[上一篇：迁移/同步/订阅](products/rds/documents/support/migration-or-synchronization-or-subscription.md)[下一篇：只读实例/读写分离](products/rds/documents/support/read-only-instances-and-read-or-write-splitting.md)

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
