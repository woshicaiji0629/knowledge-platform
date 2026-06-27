# 处理插件、写入处理器、数据加工、消费处理器的对比-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/comparison-of-processing-plug-ins-write-processors-data-processing-and-consumer-processors

# 处理插件、写入处理器、数据加工、消费处理器的对比
日志服务提供四种数据处理方案：处理插件、写入处理器、数据加工和消费处理器。本文通过对比分析它们的特性和适用场景，帮助您根据实际需求选择合适的数据处理方案。
## 背景信息
[处理插件配置](customize-logtail-plug-ins-to-process-data.md)：日志服务采集器提供了丰富的处理配置，不仅支持处理插件，还支持以[SPL](use-logtail-spl-to-parse-logs.md)[语句](use-logtail-spl-to-parse-logs.md)在客户端对数据进行处理。
[写入处理器](sls-write-processor.md)：写入处理器可以与LogStore进行关联，写入LogStore的数据会默认由写入处理器在服务端进行处理。
[数据加工](data-processing-new-edition-overview.md)：数据先写入一个源LogStore，然后再根据加工规则进行处理，处理后的数据写入到目标LogStore。
[消费处理器](data-consumption-processor.md)：通过配置消费处理器，支持在消费LogStore时通过SPL实时进行数据处理，消费处理器支持SDK、Flink、DataWorks等三方服务集成。
## 方式对比
处理插件、写入处理器、数据加工和消费处理器基本上贯穿了数据存储前（采集时）、数据存储时（写入时）、数据存储后（写入后）的完整生命周期。它们之间的能力有着一定的相似之处，例如都能够对数据进行特定的处理、都支持 SPL 语言。不过在具体的使用场景和能力上，这几种数据处理方式之间其实仍然存在着一些差异。
| 比较维度 | 处理插件 | 写入处理器 | 数据加工 | 消费处理器 |
| --- | --- | --- | --- | --- |
| 数据处理阶段 | 存储前（采集时）。 | 存储时。 | 存储后。 | 存储后 |
| 写到多个 LogStore | 单个采集配置不支持，但是可以用多个采集配置结合处理插件。 | 不支持。 | 支持。 | 不支持 |
| SPL | 支持。 | 支持。 | 支持。 | 支持 |
| 支持的 SPL 指令 | 支持处理单行数据的指令，即输入一行数据，输出为 0 行或 1 行结果。 | 支持处理单行数据的指令，即输入一行数据，输出为 0 行或 1 行结果。 | 支持完整的 SPL 指令。 | 支持完整的 SPL 指令。 |
| 敏感数据不落盘 | 支持。 | 支持。 | 不支持，数据会经过源 LogStore。 | 不支持，数据会经过源 LogStore。 |
| 资源占用 | 需要消耗一定的客户端资源。 | 服务端自动伸缩，用户不感知。 | 服务端自动伸缩，用户不感知。 | 服务端自动伸缩，用户不感知。 |
| 性能影响 | 根据插件个数和配置的复杂程度对采集性能有少许影响，但不影响数据写入时的性能。 | 根据数据复杂度和 SPL 语句复杂程度，对写入性能有少许影响（根据请求的数据包大小及 SPL 语句的复杂度，单次请求延迟会增加数毫秒到数十毫秒。） | 源 LogStore 写入性能不受影响。 | 源 LogStore 写入性能不受影响。 |
| 需求场景覆盖 | 较多。 | 正常。 | 多。 | 多 |
| 成本 | 无 SLS 数据处理费用，但是会占用一定的客户端资源。 | 数据处理费用。在数据过滤场景下，该项费用一般会低于所减少的数据的流量和存储费用。 | 源 LogStore 费用 + 数据处理费用。可以通过设置源 LogStore 数据保存 1 天以及关闭索引，来减少源 LogStore 的成本。 | 源 LogStore 费用 + 数据处理费用。可以通过设置源 LogStore 数据保存 1 天以及关闭索引，来减少源 LogStore 的成本。 |
| 容错性 | 插件中可以配置处理失败时是否保留原始字段。 | 可配置处理失败后是否保留原始数据。 | 由于源数据已经存储，加工规则失败情况可以选择重新加工。同时，可以创建多个加工任务分别加工。 | 由于源数据已经存储，Flink/Dataworks/SDK 消费组集成 SPL 消费规则对于错误自动重试。 |
根据能力的差异，以下列举了在典型场景下写入处理器、Logtail处理配置及数据加工的方案对比：
| 场景 | Logtail 处理配置 | 写入处理器 | 数据加工 | 消费处理器 |
| --- | --- | --- | --- | --- |
| 简单数据处理，例如只是简单的单行数据处理，且不涉及复杂计算逻辑。 | 推荐 | 推荐 | 推荐 | 推荐 |
| 复杂数据处理，例如涉及复杂的计算逻辑，或者需要多种条件判断、窗口聚合、维表富化等。 | 一般 | 一般 | 推荐 | 推荐 |
| 客户端资源受限，例如 Logtail 能够使用的计算资源比较有限。 | 一般 | 推荐 | 推荐 | 推荐 |
| 客户端管控受限，例如无权限修改采集侧的 Logtail 配置或 SDK 写入逻辑。 | 不推荐 | 推荐 | 推荐 | 推荐 |
| 服务端管控受限，例如无权限修改 LogStore 或加工配置。 | 推荐 | 不推荐 | 不推荐 | 不推荐 |
| 对数据写入延迟和性能比较敏感，例如希望原始数据尽可能快地采集。 | 一般 | 一般 | 推荐 | 推荐 |
| 数据脱敏，且敏感数据可以落盘。 | 推荐 | 推荐 | 推荐 | 推荐 |
| 数据脱敏，且敏感数据不可以落盘。 | 推荐 | 推荐 | 不推荐 | 不推荐 |
| 数据富化（不依赖外部数据源），例如增加一个新的字段，内容为固定值或者从已有字段中提取出来。 | 一般 | 推荐 | 推荐 | 推荐 |
| 数据富化（依赖外部数据源），例如根据日志字段去 MySQL 表中查出其它富化数据。 | 不推荐 | 不推荐 | 推荐 | 推荐 |
| 数据分发，将数据根据不同的条件写入到不同的 LogStore。 | 一般 | 不推荐 | 推荐 | 不推荐 |
| 需要对数据进行过滤，且原始数据可以不需要，希望能够一定程度上节约成本。 | 一般 | 推荐 | 一般 | 一般 |
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
