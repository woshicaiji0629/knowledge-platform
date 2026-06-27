# 写入处理器功能原理限制与计费-日志服务-阿里云-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/sls-write-processor

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 数据写入时处理（写入处理器）

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

如果您需要在日志数据写入LogStore前对数据进行处理，例如数据过滤、字段提取、字段扩展、数据脱敏，可以使用写入处理器（IngestProcessor）。

## 工作原理

- 

通过[Logtail](products/sls/documents/overview-19.md)[采集](products/sls/documents/overview-19.md)、[日志服务](products/sls/documents/developer-reference/overview-of-log-service-sdk.md)[SDK](products/sls/documents/developer-reference/overview-of-log-service-sdk.md)、[Web Tracking](products/sls/documents/use-the-web-tracking-feature-to-collect-logs.md)[功能](products/sls/documents/use-the-web-tracking-feature-to-collect-logs.md)等方式采集日志数据，数据会先经过写入处理器（IngestProcessor），然后写入LogStore。数据处理过程在日志服务中完成，不会占用客户端的资源。

- 

写入处理器、[查询和分析日志](products/sls/documents/use-spl-to-query-and-analyze-logs.md)、[数据加工（新版）](products/sls/documents/data-processing-new-edition-overview.md)都支持[SPL](products/sls/documents/spl-overview.md)[语法](products/sls/documents/spl-overview.md)。

## 使用场景

- 

字段提取：从原始日志字段中通过正则表达式、Key-Value格式、JSON等解析方式提取出新的字段。

- 

扩展字段：为原始日志添加新的字段。

- 

丢弃字段：删除原始日志的部分字段。

- 

数据脱敏：将原始日志的敏感信息进行脱敏处理。

- 

数据过滤：丢弃原始日志的部分数据。

## 使用限制

- 

- 

| 限制项 | 说明 |
| --- | --- |
| 写入处理器个数 | 每个 Project 下最多创建 100 个 IngestProcessor。 |
| 写入处理器配置中 SPL 语句长度 | 每个 SPL 语句长度不超过 4000 个字符。 |
| 写入处理器中 SPL 指令限制 | 仅支持行处理指令，不支持聚合、逻辑判断等指令。 |
| 每个 LogStore 关联的写入处理器个数 | 每个 LogStore 最多只能关联一个写入处理器。 当 LogStore 与写入处理器关联后，所有写入该 LogStore 的数据都会先经过写入处理器进行处理，然后写入 LogStore。 |
| 更新或删除写入处理器后生效时间 | 修改或删除写入处理器配置，或者修改 LogStore 与写入处理器的关联关系，会在一分钟内生效。 |


## 功能计费

写入处理器是按照数据处理过程中消耗的计算资源量进行计费，计费单位为OCU。

可观测资源额度OCU（Observability Capacity Unit）是阿里云云原生可观测推出的新版计费单位，可根据每小时资源使用情况自动统计OCU用量，中国站公共云OCU的定价为0.15元/个。

日志服务计算型功能收费计划逐步通过OCU进行计量，以用户实际消耗的计算资源作为计量的度量维度。在 CPU 场景下一个OCU的性能约等于0.5 Core CPU、2 GB内存、3000 IOPS，在计算OCU的总数时，会按照消耗的CPU核心数、内存大小和IOPS三个维度分别计算三个OCU数量，然后取三个OCU数量的最大值作为OCU的最终值，用于计费。

假设您的计算作业消耗了1 Core CPU，2GB内存，3000 IOPS，则这个作业消耗2个OCU。在一个计量周期（1小时）内，计算平均消耗的OCU可参考：数据写入处理器处理1GB数据，大约消耗1/3个OCU。数据加工（新版）处理1GB数据，大约消耗1/3个OCU。规则消费处理1GB数据，约消耗0.3个OCU。

OCU的计费信息，请参见[按写入数据量计费模式计费项](products/sls/documents/billing-items-in-the-pay-per-data-write-mode.md)和[按使用功能计费模式计费项](products/sls/documents/billable-items.md)。

[上一篇：使用Logtail SPL解析日志](products/sls/documents/use-logtail-spl-to-parse-logs.md)[下一篇：快速入门](products/sls/documents/ingest-processor-quick-start.md)

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
