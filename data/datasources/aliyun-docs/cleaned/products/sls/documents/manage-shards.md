# 分裂、合并、删除分区Shard-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/manage-shards

# 管理Shard
日志服务使用Shard控制LogStore、EventStore、MetricStore的读写数据的能力，数据必定保存在某一个Shard中。通过分裂、合并操作控制活跃的Shard数量来调整日志服务提供的最大读写能力。分裂Shard可以自动触发，但合并Shard必须手动执行。
## 基本概念
### Shard范围
每个Shard均有范围，为MD5左闭右开区间[BeginKey,EndKey)。每个Shard范围不会相互覆盖，且属于整个MD5范围内[00000000000000000000000000000000,ffffffffffffffffffffffffffffffff）。在创建LogStore或MetricStore时指定Shard个数，日志服务将自动平均划分整个MD5范围。
BeginKey：指定Shard范围的起始值，Shard范围中包含该值。
EndKey：指定Shard范围的结束值，Shard范围中不包含该值。
例如LogStore A中包含4个Shard，各个Shard范围如下：
表 1.Shard范围
| Shard ID | 范围 |
| --- | --- |
| Shard0 | [00000000000000000000000000000000,40000000000000000000000000000000) |
| Shard1 | [40000000000000000000000000000000,80000000000000000000000000000000) |
| Shard2 | [80000000000000000000000000000000,c0000000000000000000000000000000) |
| Shard3 | [c0000000000000000000000000000000,ffffffffffffffffffffffffffffffff) |
在Shard读写数据过程中，读数据时必须指定Shard ID，写数据时可通过负载均衡模式或者指定Hash Key的模式。
负载均衡模式：每个数据包随机写入当前可用的Shard中。
如果写入流量大于单Shard的服务能力，建议采用负载均衡模式。
指定Hash Key模式：指定MD5的Key值，数据将被写入包含该Key值的Shard中。
例如[Shard](shard.md)[范围](shard.md)所示，当写入数据时指定MD5的Key值为5F时，则数据将被写入包含5F的Shard1上；当写入数据时指定MD5的Key值为8C时，则数据将被写入包含8C的Shard2上。
### Shard的读写能力
每个Shard提供一定的服务能力，具体请参见[数据读写](data-read-and-write.md)。
根据实际数据流量规划Shard个数。当数据流量超出读写能力时，及时分裂Shard以增加Shard个数，从而达到更大的读写能力。当数据流量远未达到Shard的最大读写能力时，及时合并Shard以减少Shard个数，从而降低活跃Shard租用费用。
重要
当写入数据的API持续报告403或者500错误时，通过LogStore云监控查看流量和状态码判断是否需要增加Shard。
超过Shard服务能力的读写，日志服务会尽可能服务，但不保证服务质量。
### Shard状态
Shard状态包括readwrite（读写）和readonly（只读）。
创建Shard时，所有Shard状态均为readwrite状态。执行分裂或合并操作后，Shard状态变更为readonly，并生成新的readwrite状态的Shard。Shard状态不影响其数据读取的性能。readwrite状态的Shard可保证数据写入性能，readonly状态的Shard不提供数据写入服务。
### 分裂与合并
日志服务支持分裂和合并Shard。
分裂操作是指将一个Shard分裂为另外两个Shard，即分裂后Shard数量增加2。两个新生成的Shard的状态为readwrite，排列在原Shard之后且两个Shard的MD5范围覆盖原Shard的MD5范围。
分裂Shard时，需指定一个处于readwrite状态的Shard。分裂完成后，原Shard状态由readwrite变为readonly，该Shard中的数据仍可被消费，但该Shard不支持写入新数据。
合并操作是指将两个Shard合并为一个Shard。新生成的Shard的状态为readwrite，排列在原Shard之后且其MD5范围覆盖原来两个Shard的MD5范围。
合并Shard时，需指定一个处于readwrite状态且未排列在最后一个的Shard，日志服务自动找到所指定Shard右侧相邻的Shard，并进行合并。合并完成后，原来两个Shard的状态由readwrite变为readonly，这两个Shard中的数据仍可被消费，但这两个Shard不支持写入新数据。
## 分裂Shard
建议您根据实际业务数据流量规划Shard个数。每个Shard支持5MB/s或500次/s的数据写入、10MB/s或100次/s的数据读取。此限制非硬性限制，超出限制时，系统会尽可能提供服务，但是不保证服务质量。当数据读写流量超出Shard读写能力时，需要及时分裂Shard以增加Shard个数，从而提供更高的读写能力。
说明
当写入数据的API持续报告403或者500错误时，您可以通过LogStore云监控查看流量和状态码判断是否需要增加Shard。
### 控制台操作
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
单击日志存储，在日志库中，将鼠标悬浮在目标LogStore上，选择>修改。
在Logstore属性页面中，单击修改。
选择待分裂的Shard，单击分裂。
重要
分裂Shard时，需要选择一个处于readwrite状态的Shard。
在Shard管理页面的列表中，找到目标 readwrite 状态的 Shard，单击其操作列中的分裂。
选择分裂数量，单击确定。
单击保存。
### 命令行操作
您也可以通过日志服务命令行工具CLI一次性分裂Shard到指定数量。更多信息，请参见[使用](https://aliyun-log-cli.readthedocs.io/en/latest/tutorials/tutorial_split_shard.html)[CLI](https://aliyun-log-cli.readthedocs.io/en/latest/tutorials/tutorial_split_shard.html)[配置](https://aliyun-log-cli.readthedocs.io/en/latest/tutorials/tutorial_split_shard.html)[Shard](https://aliyun-log-cli.readthedocs.io/en/latest/tutorials/tutorial_split_shard.html)。
## 查看Shard
### 控制台操作
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
单击日志存储，在日志库中，将鼠标悬浮在目标LogStore上，选择>修改。
在Logstore属性页面中，查看当前LogStore的Shard列表。
该页面展示Shard总数（含读写个数和只读个数），以及各Shard的Id、状态、BeginKey/EndKey和创建时间等信息。
## 自动分裂Shard
日志服务支持自动分裂Shard，帮助您自动处理业务流量超出预估值的场景。自动分裂Shard需要满足以下几个条件。
开启了自动分裂Shard开关。
当写入数据量超出当前Shard的[写入服务能力](data-read-and-write.md)且持续5分钟以上。
LogStore中readwrite状态的Shard数目未超过设定的最大Shard总数。
说明
最近15分钟内分裂出来的新Shard不会自动分裂。
您可以在创建或修改LogStore时开启自动分裂Shard，并设定Shard的最大分裂数。
自动分裂Shard
例如原本存在4个Shard，日志服务会独立判断各个Shard是否满足分裂条件。满足分裂条件的Shard会各自进行分裂，分裂总数不会超过您所设定的最大分裂数。
最大分裂数
Shard自动分裂的最大总数目。开启自动分裂Shard功能后，最多支持自动分裂至256个readwrite状态的Shard。
## 合并Shard
当数据读写流量远达不到Shard的最大读写能力时，建议您合并Shard，降低活跃Shard租用费用。您可以通过合并操作减少Shard数量，日志服务会找到指定Shard右侧相邻的Shard，并将两个Shard合并。合并Shard只支持手动操作，无法自动合并。
重要
合并Shard时，必须指定一个处于readwrite状态的Shard，且不能是最后一个readwrite状态的Shard。
单击日志存储，在日志库中，将鼠标悬浮在目标LogStore上，选择>修改。
在Logstore属性页面中，单击修改。
选择待合并的Shard，单击合并。
在Shard 管理页面，顶部展示 Shard 总数及读写、只读个数统计。下方表格包含Id、状态、BeginKey/EndKey、创建时间、操作列。状态为readwrite的 Shard 支持分裂或合并操作，状态为readonly的 Shard 无可用操作。
单击保存。
合并完成后，所指定的Shard及其右侧相邻Shard的状态变成readonly。同时新生成一个readwrite状态的Shard，新Shard的MD5范围覆盖原来两个Shard的范围。
## 删除Shard
警告
删除Shard后，无法恢复，请谨慎操作。
自动删除
如果您在创建LogStore时设置了数据保存时间，那么Shard及Shard中的数据超出保存时间后会被自动删除。
手动删除
如果您在创建LogStore时开启了永久保存，建议您通过删除LogStore的方式删除LogStore中的Shard和数据。更多信息，请参见[停止计费/删除](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
## Shard接口
| 操作 | 接口 |
| --- | --- |
| 分裂 Shard | [SplitShard](developer-reference/api-sls-2020-12-30-splitshard.md) |
| 合并 Shard | [MergeShard](developer-reference/api-sls-2020-12-30-mergeshard.md) |
| 查询 Shard | [ListShards](developer-reference/api-sls-2020-12-30-listshards.md) |
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
