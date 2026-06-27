# 保留字段的含义列表与使用说明-日log志服务-阿里云-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/reserved-fields

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

# 保留字段

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在采集日志或投递数据到其他云产品时，日志服务会将日志来源、时间戳等信息以Key-Value对的形式添加到日志中。这些字段是日志服务的保留字段。本文介绍日志服务的保留字段。

重要

- 使用API写入日志数据或添加Logtail配置时，请不要将Key即字段名称设置为这些保留字段，否则可能会造成字段名称重复、查询不精确等问题。

- 旧版投递任务不支持投递__tag__前缀的字段。

- 若当前LogStore的计费模式为按写入数据量计费时，日志服务为日志数据增加的字段将不产生费用。具体内容，可参见[按写入数据量计费](products/sls/documents/billing-per-amount-of-data-written.md)。

- 若当前LogStore的计费模式为按使用功能计费时，日志服务为日志数据增加的字段按照按使用功能计费方式正常收费，为其开启索引时也会产生少量索引流量及存储费用。更多信息，请参见[按使用功能计费](products/sls/documents/pay-as-you-go.md)。

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

- 

| 保留字段 | 数据格式 | 索引与统计设置 | 说明 |
| --- | --- | --- | --- |
| __time__ | 整型，Unix 标准时间格式。 | 索引设置： __time__ 通过 API 中的参数 from 和 to 选择，无需添加该字段的索引。 统计设置：当您为任何一列开启统计后，日志服务默认为 __time__ 开启统计。 | 写入日志数据时指定的日志时间。该字段可用于日志投递、查询、分析。 |
| __source__ | 字符串格式。 | 索引设置：开启索引后，日志服务默认为 __source__ 创建索引，索引数据类型为 text 类型，分词字符为空。查询时输入 source:127.0.0.1 或者 __source__:127.0.0.1 。 统计设置：当您为任何一列开启统计后，日志服务默认为 __source__ 开启统计。 | 日志来源设备。该字段可用于日志投递、查询、分析、自定义消费。 |
| __topic__ | 字符串格式。 | 索引设置：开启索引后，日志服务默认为 __topic__ 创建索引，索引数据类型为 text 类型，分词字符为空。查询时输入 __topic__:XXX 。 统计设置：当您为任何一列开启统计后，日志服务默认为 __topic__ 开启统计。 | 日志主题（Topic）。如果您设置了日志主题，日志服务会自动为您的日志添加日志主题字段，Key 为 __topic__ ，Value 为您的主题内容。该字段可用于日志投递、查询、分析、自定义消费。更多信息，请参见 [日志主题](products/sls/documents/log-topics.md) 。 |
| __partition_time__ | 字符串格式。 | 日志内容中不存在该字段，无需设置索引。 | 投递 MaxCompute 的日志分区时间列，由 __time__ 计算得到。该字段可用于日志投递 MaxCompute 时设置日期格式分区列。更多信息，请参见 [投递日志到](products/sls/documents/ship-logs-to-maxcompute.md) [MaxCompute（旧版）](products/sls/documents/ship-logs-to-maxcompute.md) 。 |
| __extract_others__ | 字符串格式，可反序列化成 JSON Map。 | 日志内容中不存在该字段，无需设置索引。 | 日志中投递 MaxCompute 的未配置字段组装为一个 JSON Map。该字段可用于日志投递 MaxCompute 时打包其它未单独配置的字段。更多信息，请参见 [投递日志到](products/sls/documents/ship-logs-to-maxcompute.md) [MaxCompute（旧版）](products/sls/documents/ship-logs-to-maxcompute.md) 。 |
| _extract_others_ | 字符串格式，可反序列化成 JSON Map。 | 日志内容中不存在该字段，无需设置索引。 | 与 __extract_others__ 相同，建议使用 __extract_others__ 。 |
| __tag__:__client_ip__ | 字符串格式。 | 索引设置：开启索引后，日志服务默认为所有字段创建索引，索引数据类型为 text 类型，分词字符为空，在查询时要完全命中，或采用模糊查询。 统计设置：默认没有为该列开启统计。如需开启统计，请手动添加 __tag__:__client_ip__ 的索引，并开启统计功能。 | 日志来源设备的公网 IP。该字段为系统标签（Tag）。开启记录外网 IP 功能后，服务端接收日志时为原始日志追加该字段。可用于日志查询、分析、自定义消费。对该字段进行 SQL 分析时，需要给该字段加上双引号。更多信息，请参见 [标签（Tags）](products/sls/documents/log.md) 和 [记录外网](products/sls/documents/manage-a-logstore.md) [IP](products/sls/documents/manage-a-logstore.md) 。 |
| __tag__:__receive_time__ | 字符串，可转换为整型的 Unix 标准时间格式。 | 索引设置：开启索引后，日志服务默认为所有标签（Tag）创建索引，索引数据类型为 text 类型，分词字符为空，在查询时要完全命中，或采用模糊查询。 统计设置：默认没有为该列开启统计。如需开启统计，请手动添加 __tag__:__receive_time__ 的索引，并开启统计功能。 | 日志到达服务端的时间，该字段为系统标签（Tag）。开启记录外网 IP 功能后，服务端接收日志时为原始日志追加该字段。该字段可用于日志查询、分析、自定义消费。更多信息，请参见 [标签（Tags）](products/sls/documents/log.md) 和 [记录外网](products/sls/documents/manage-a-logstore.md) [IP](products/sls/documents/manage-a-logstore.md) 。 |
| __tag__:__path__ | 字符串格式。 | 索引设置：开启索引后，日志服务默认为 __tag__:__path__ 创建索引，索引数据类型为 text 类型，分词字符为空。查询时输入 __tag__:__path__:XXX 。 统计设置：默认没有为该列开启统计。如需开启统计，请手动添加 __tag__:__path__ 的索引，并开启统计功能。 | Logtail 采集的日志文件路径，Logtail 为日志自动填加该字段。可用于日志查询、分析、自定义消费。对该字段进行 SQL 分析时，需要给该字段加上双引号。 |
| __tag__:__hostname__ | 字符串格式。 | 索引设置：开启索引后，日志服务默认为 __tag__:__hostname__ 创建索引，索引数据类型为 text 类型，分词字符为空。查询时输入 __tag__:__hostname__:XXX 。 统计设置：默认没有为该列开启统计。如需开启统计，请手动添加 __tag__:__hostname__ 的索引，并开启统计功能。 | logtail 采集数据的来源机器主机名。Logtail 为日志自动填加该字段。可用于日志查询、分析、自定义消费。对该字段进行 SQL 分析时，需要给该字段加上双引号。 |
| __raw_log__ | 字符串格式。 | 请手动添加并设置该字段的索引，索引数据类型为 text，并根据需求选择是否开启统计。 | 解析失败的原始日志。关闭丢弃解析失败日志功能后，Logtail 在解析日志失败时上传原始日志。其中 Key 为 __raw_log__ 、Value 为日志内容。该字段可用于日志投递、查询、分析、自定义消费。更多信息，请参见 [丢弃解析失败日志](products/sls/documents/overview-10.md) 。 |
| __raw__ | 字符串格式。 | 请手动添加并设置该字段的索引，索引数据类型为 text，并根据需求选择是否开启统计。 | 解析成功的原始日志。开启上传原始日志功能后，Logtail 会将原始日志作为 __raw__ 字段，和解析后的日志一并上传。该字段可用于审计、合规审查等场景。该字段可用于日志投递、查询、分析、自定义消费。更多信息，请参见 [上传原始日志](products/sls/documents/overview-10.md) 。 |


[上一篇：重建索引](products/sls/documents/reindex-logs-for-a-logstore.md)[下一篇：扫描模式查询与分析（Scan）](products/sls/documents/query-and-analyze-logs-in-scan-mode.md)

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
