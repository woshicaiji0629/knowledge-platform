# 通过配置低频存储、归档存储降低日志存储成本。-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/data-tiered-storage-overview

# 管理智能存储分层
日志服务提供智能分层存储功能，您可以按需将数据进行热存储、低频存储和归档存储。降低您长周期存储的成本，并同时保证日志的查询、分析、可视化、告警、投递和加工等能力不受影响。本文将为您介绍日志服务数据存储生命周期管理。
## 什么是智能存储分层
### 存储类型
| 类型 | 说明 |
| --- | --- |
| 热存储 | 热存储是一种可扩展、高可用的数据存储方案，用于存储经常被访问的数据。 支持数据实时访问，提供高性能的日志查询和分析功能，适用于数据高频查询分析等业务场景。 |
| 低频存储 | 低频存储（原冷存储）是一种能降低您长周期存储的成本的存储类型，同时保证日志的查询、分析、可视化、告警、投递和加工等能力不受影响。 适用于较低查询分析频率，问题回溯等业务场景。 |
| 归档存储 | 归档存储在现有热存储、低频存储的基础上，为您提供更低成本且可查询、分析的长期数据存储方案。 适用于数据审计长期保存的业务场景。 |
### 存储周期说明
重要
热存储数据保存时间、低频存储数据保存时间和归档存储数据保存时间的总和，等于数据保存时间。
数据保存时间3650天表示永久保存，超过3650天的也会继续保存，计入归档存储数据层。查看数据保存时间可参考[删除指定日志/设置日志保存时间](manage-a-logstore.md)。
数据保存时间在3650天以内
场景1：数据保存时间为90天，将热存储数据保存30天后自动转换为归档存储，归档存储数据保存60天后自动删除。
场景2：数据保存时间为97天，将热存储数据保存7天后自动转换为低频存储，低频存储数据保存30天后自动转换为归档存储，归档存储数据保存60天后自动删除。
数据保存时间在3650天及以上
场景3：数据保存时间为3650天，热存储层数据保存时间为30天，全部转换为归档存储，则归档存储数据保存时间需设置为3650 - 30 = 3620天。同时，因为数据保存时间3650天表示永久保存，超过3620天的也会继续保存，计入归档存储数据层。
场景4：数据保存时间为3650天，热存储层数据保存时间为7天，低频存储数据保存时间为30天，则归档存储数据保存时间需设置为3650 - 7- 30 = 3613天。同时，因为数据保存时间3650天表示永久保存，超过3613天的也会继续保存，计入归档存储数据层。
### 存储类型对比
| 存储类型 | 热存储 | 低频存储 | 归档存储 |  |
| --- | --- | --- | --- | --- |
| 适用场景 | 高频、高性能的查询与分析 | 问题回溯定位场景 | 数据审计场景 |  |
| 费用 | 0.0115 元/GB/天 | 0.005 元/GB/天 | 0.0017 元/GB/天 |  |
| 性能 | 时延（十亿级规模） | 十至百毫秒 | 百毫秒至秒 | 分钟 |
| 并发（Project 级别） | 查询并发数：100 分析并发数：2 | 查询并发数：10 分析并发数：2 | 查询并发数：1 分析并发数：1 |  |
| 优势 | 快速高并发查询与分析 | 低频率查询与分析，高性价比 | 偶尔查询与分析，低成本 |  |
| 多种存储类型间可通过数据生命周期管理功能实现数据自动分层： 配置简便，无需编写脚本或手动迁移数据。 低频存储和归档存储数据与热存储数据一样可实时访问，无需手动取回或修改应用，无任何取回费用。 |  |  |  |  |
| 存储时间限制 | [按使用功能计费](pay-as-you-go.md) | 至少需保存 7 天热存储后可转为低频存储。 至少需保存 30 天热存储后可转为归档存储。 | 至少保存 30 天低频存储后可转为归档存储。 | 最少存储时间为 60 天。 |
| [按写入数据量计费](billing-per-amount-of-data-written.md) | 30 天热存储免费权益 |  |  |  |
## 存储分层的转换流程
三种存储类型之间可以互相转换，存储类型转换说明参见下表。
| 序号 | 说明 |
| --- | --- |
| 1 | 热存储数据至少需要保存 7 天才能转换为低频存储。 |
| 2 | 热存储数据至少需要保存 30 天才能转换为归档存储。 |
| 3 | 低频存储数据至少需要保存 30 天才能转换为归档存储。 |
| 4 | 通过修改热存储数据保存时间，将低频存储数据转回热存储中。 |
| 5 | 通过修改低频储数据保存时间，将归档存储数据转回低频存储中。 |
| 6 | 通过修改热存储数据保存时间，实现将归档存储数据转回热存储中。 |
## 管理存储分层
## 控制台
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标LogStore对应的图标，然后单击修改。
在Logstore属性页面，单击修改。配置开启智能存储分层，然后单击保存。
开启智能存储分层功能的相关参数如下表所示，其他参数说明请参见[创建基础](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
| 参数 | 说明 |
| --- | --- |
| 数据保存时间 | 数据保存时间 支持设置为 限定天数 和 永久保存 。 热存储数据保存时间、低频存储数据保存时间和归档存储数据保存时间的总和，等于数据保存时间。 重要 缩短数据保存时间后，会在 1 分钟内生效。 例如您原本的数据保存时间为 5 天，现修改为 1 天，则日志服务将会删除前 4 天的数据。 数据的实际删除时间最多会延迟 7 天，但延迟删除的这部分数据不会计入收费，也不会计入存储容量。 |
| 智能分层存储 | 打开 智能分层存储 开关，开启智能分层存储功能。 |
| 存储策略 | 配置数据在各层的存储时间。 |
| 热存储层数据保存 | 数据在 LogStore 热存储层中的存储时间。 当热存储转为低频存储时，取值范围为 7～3650，单位：天。 当热存储转为归档存储时，取值范围为 30～3650，单位：天。 重要 修改 热存储层数据保存 时间后，日志服务将在 1 分钟内生效。例如您原本的数据的热存储时间为 30 天，现修改为 40 天，则日志服务将在 1 分钟内将低频存储数据或归档存储数据转回热存储。 热存储层数据保存 时间参数值要小于 数据保存时间 参数值。 |
| 低频存储数据保存 | 数据在 LogStore 低频存储层中的存储时间。 当低频存储转为归档存储时，取值范围为 30～3650，单位：天。 重要 修改 低频存储层数据保存 时间后，日志服务将在 1 分钟内生效。例如您原本的数据的低频存储时间为 30 天，现修改为 40 天，则日志服务将在 1 分钟内将归档存储数据转回低频存储。 低频存储层数据保存 时间参数值要小于 数据保存时间 参数值。 |
| 归档存储数据保存 | 数据在 LogStore 归档存储层中的存储时间。取值范围为 60～3650，单位：天。当数据的存储时间超过您所配置的 归档存储数据保存 时间后，数据将自动删除。 重要 归档存储层数据保存 时间参数值要小于 数据保存时间 参数值。 |
## API
您可以在创建LogStore的过程中，通过API调用[创建](developer-reference/api-sls-2020-12-30-createlogstore.md)[LogStore](developer-reference/api-sls-2020-12-30-createlogstore.md)传递ttl（数据保存时间）、hot_ttl（热存储数据保存时间）、infrequentAccessTTL（低频存储数据保存时间）参数来配置存储分层的保留策略。
同样地，对于已经创建的LogStore，您也可以通过调用[更新](developer-reference/api-sls-2020-12-30-updatelogstore.md)[LogStore](developer-reference/api-sls-2020-12-30-updatelogstore.md)接口，更新ttl、hot_ttl和infrequentAccessTTL参数的值，来动态调整存储分层的保留策略，以满足您对数据保留和成本控制的需求。
## 相关文档
管理LogStore相关信息请参见[管理](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
分层存储数据的存储费用按照存储空间计费，数据转换不会产生费用。详细信息请参见[计费概述](billing-overview.md)。
按写入数据量计费模式下，存在30天免费存储额度，当开启智能分层存储后，存储费用将根据具体存储时间及当前存储类型进行计算，更多信息，请参见[计费案例](billing-examples.md)。
按使用功能计费与按写入数据量计费模式具体信息请参见[按量付费](pay-by-volume.md)。
日志服务提供本地冗余存储和同城冗余存储两种存储冗余类型，详细信息请参见[存储冗余](storage-redundancy.md)。
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
