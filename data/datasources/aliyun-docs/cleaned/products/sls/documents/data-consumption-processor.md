# 数据消费处理器-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/data-consumption-processor

# 消费处理器
日志服务提供基于消费处理器的数据实时消费功能，通过SPL实现服务端数据处理后消费。本文介绍消费处理器的概念、优势、场景、计费规则及消费目标。
## 工作原理
基于消费处理器消费是一种通过设置SPL实时处理日志服务数据的方式，适用于第三方软件、多语言应用、云产品、流式计算框架等多种应用场景。SPL是SLS推出的一种高性能数据处理语言，专门用于处理日志的弱结构化特点。其原理是在服务端使用SPL对日志数据进行预处理和清洗，例如执行行过滤、列裁剪、正则提取等操作。经过处理后，客户端接收到的数据已是规整格式。更多关于SPL语法的详情，请参见[SPL](spl-overview.md)[语法](spl-overview.md)。
## 功能优势
通过公网消费，节省流量费用。
某客户想把日志写入到日志服务后，再通过公网消费日志，过滤后再分发给内部系统。基于SPL消费功能，该客户可以直接在日志服务中实现日志规则过滤，避免将大量无效日志投递给消费者，节省网络流量费用。
节省本地CPU资源，加速计算进程。
某客户想把日志写入到日志服务后，再消费日志到本地机器进行计算。基于SPL消费功能，该客户可以直接在日志服务中实现SPL计算，降低本地资源消耗。
## 计费规则
若LogStore的计费模式为按写入数据量计费，基于消费处理器消费将不产生费用，仅从日志服务公网域名所在接口拉取数据时，会产生外网读取流量（按照压缩后的数据量计算）。具体内容，可参见[按写入数据量计费模式计费项](billing-items-in-the-pay-per-data-write-mode.md)。
若LogStore的计费模式为按使用功能计费，基于消费处理器消费服务会产生服务端计算费用，使用日志服务公网域名可能产生公网流量费用。更多信息，请参见[按使用功能计费模式计费项](billable-items.md)。
## 消费目标
日志服务支持的基于消费处理器消费目标如下表所示。
| 类型 | 目标 | 说明 |
| --- | --- | --- |
| 多语言应用 | 多语言应用 | 基于 Java、Python、Go 等语言的应用基于消费处理器消费组消费日志服务的数据。具体操作，请参见 [通过](log-consumption-through-java-sdk.md) [API](log-consumption-through-java-sdk.md) [消费](log-consumption-through-java-sdk.md) 和 [通过消费组消费日志](log-consumption-by-consumer-group.md) 。 最佳实践： [使用](use-sdk-to-consume-logs-based-on-consumption-processor-spl.md) [SDK](use-sdk-to-consume-logs-based-on-consumption-processor-spl.md) [基于消费处理器（SPL）消费日志](use-sdk-to-consume-logs-based-on-consumption-processor-spl.md) |
| 云产品 | 阿里云 Flink | 您可以通过阿里云 Flink 实时计算消费日志服务的数据。具体操作，请参见 [日志服务](https://help.aliyun.com/zh/flink/realtime-flink/developer-reference/log-service-connector) [SLS](https://help.aliyun.com/zh/flink/realtime-flink/developer-reference/log-service-connector) 。 最佳实践： [Flink SQL](flink-sql-implements-row-filtering-and-column-pruning-based-on-spl.md) [基于](flink-sql-implements-row-filtering-and-column-pruning-based-on-spl.md) [SPL](flink-sql-implements-row-filtering-and-column-pruning-based-on-spl.md) [实现行过滤与列裁剪](flink-sql-implements-row-filtering-and-column-pruning-based-on-spl.md) [Flink SQL](flink-sql-implements-weakly-structured-analysis-based-on-spl.md) [基于](flink-sql-implements-weakly-structured-analysis-based-on-spl.md) [SPL](flink-sql-implements-weakly-structured-analysis-based-on-spl.md) [实现弱结构化分析](flink-sql-implements-weakly-structured-analysis-based-on-spl.md) |
| 流式计算 | Kafka | 如有需求请提 [工单](https://selfservice.console.aliyun.com/ticket/category/sls/today) 申请。 |
## 注意事项
基于消费处理器消费需要在服务端进行复杂计算。由于SPL计算复杂度及数据特征的差异，数据读取的服务端延迟可能会略有增加（例如处理5MB数据，延迟增加10~100ms之间）。然而，一般情况下，尽管服务端延迟有所增加，但整体端到端延迟（即从数据拉取到本地计算完成的总时间）通常会减少。
基于消费处理器消费在SPL语法错误、源数据字段缺失等情况下，可能会导致获取到的数据缺失或失败，具体说明可以参考[错误处理](spl-general-reference.md)。
基于消费处理器消费在配置SPL语句时，SPL语句长度（字符串长度）最大为4KB。
基于消费处理器消费与普通实时消费Shard读取限制相同：其中基于消费处理器消费的Shard读流量是指SPL处理前的原始数据量，具体限制可以参考[数据读写](data-read-and-write.md)。
## 使用限制
| 限制项 | 说明 |
| --- | --- |
| 消费处理器个数 | 每个 Project 下组多创建 100 个 ConsumeProcessor。如果您有更大的使用需求，如有需求请提 [工单](https://selfservice.console.aliyun.com/ticket/category/sls/today) 申请。 |
| 消费处理器配置中 SPL 长度 | 每个 SPL 长度不超过 4000 个字符。 |
| 消费处理器中 SPL 指令限制 | 仅支持行处理指令，不支持聚合、逻辑判断等指令。 |
| 更新或删除消费处理器后生效时间 | 修改或删除消费处理器配置，最多一分钟内生效。 |
## 常见问题
规则消费的ShardReadQuotaExceed错误怎么处理？
这个错误码是由于Shard读流量超过Quota报错，解决方案：
消费客户端程序遇到此错误可以等待（sleep）后重试。
或者手动分裂Shard，对于Shard分裂后的产生的新数据消费，达到降低每个shard读取速度的效果。
规则消费的流量控制是什么样的？
规则消费的流量控制策略等同于普通消费的流量控制，具体可以参考[数据读写](data-read-and-write.md)。规则消费的流量计算是指SPL处理前的原始数据量：
例如原始数据大小为100MB（压缩后），经过SPL语句* | where method = 'POST'过滤后，返回给消费客户端的数据大小为20MB（压缩后），读取流量控制是按照100MB来计算。
使用规则消费后，为什么在[项目监控](project-monitoring.md)中的“流量/分钟”图表中看到的outflow的流量很低？
因为项目监控中显示的“流量/分钟”的outflow是指SPL处理后的数据量，并非原始数据量，如果SPL语句中包含行过滤、列裁剪等减少数据量的指令时，可能会有outflow低情况出现。
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
