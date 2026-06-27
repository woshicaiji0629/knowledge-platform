# 创建、修改、删除事件库EventStore-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/manage-an-eventstore

# 管理EventStore
删除EventStore会永久删除事件数据，删除日志可以通过设置更短的保存时间。本文介绍如何在日志服务控制台上创建、修改和删除EventStore与事件数据等操作。
## 基本概念
事件库（EventStore）是日志服务中事件数据的采集、存储和查询单元。每个EventStore隶属于一个Project，每个Project中可创建多个EventStore。更多信息，请参见[事件库（EventStore）](eventstore.md)。
## 前提条件
已创建Project。具体操作，请参见[管理](manage-a-project.md)[Project](manage-a-project.md)。
## 创建EventStore
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在事件存储>事件库页签中，单击图标。
在创建EventStore面板中，配置如下参数，单击确定。
| 参数 | 说明 |
| --- | --- |
| EventStore 名称 | EventStore 名称在其所属 Project 内必须唯一，创建后不能修改。 重要 EventStore 名称与其所属 Project 内的其他 LogStore 或者 MetricStore 名称也不能重复。 |
| 数据保存时间 | 日志服务采集的事件数据在 EventStore 中的保存时间。 选择数据保存模式为 限定天数 保存，并按需设置数据保存时间。更多信息，请参见 [基础资源（日志保存时间）](basic-resources.md) 。 选择数据保存模式为 永久保存 时，日志服务将永久保存采集到的事件数据。 说明 通过 SDK 方式获取数据保存时间时，如果对应值为 3650 则表示永久保存。 |
| 智能存储分层 | 开通智能存储分层，可按需将数据存储在热存储层、低频存储层或归档存储层。 按需配置热存储数据保存时间，并选择后续 自动转换 为 低频存储 时，数据保存超出配置的保存时间后，将自动转入低频存储层。若配置低频存储时间后选择 自动删除 ，则数据保存在低频存储层超出配置的保存时间后将自动删除。 按需配置热存储数据保存时间，并选择后续 自动转换 为 低频存储 时，数据保存超出配置的保存时间后，将自动转入低频存储层。若配置低频存储时间后选择 自动转换 为 归档存储 时，则数据保存在低频存储层超出配置的保存时间后将自动转入归档存储层。 按需配置热存储数据保存时间，并选择后续 自动转换 为 归档存储 时，数据保存超出配置的保存时间后，将自动转入归档存储层。若配置归档存储时间后选择 自动删除 ，则数据保存在归档存储层超出配置的保存时间后将自动删除。 重要 数据热存储、低频存储及归档存储相关信息，可参见 [管理智能存储分层](data-tiered-storage-overview.md) 。 数据热存储至少 7 天后才能转为低频存储，数据热存储至少 30 天后才能转为归档存储，数据低频存储至少 30 天后才能转为归档存储，详细信息，请参见 [数据存储生命周期管理](user-guide/data-storage-lifecycle-management.md) 。 数据热存储、低频存储及归档存储相关费用，请参见 [计费项](billing-item.md) 。 |
| Shard 数目 | 日志服务使用 Shard 读写数据。一个 Shard 提供的写入能力为 5 MB/s、500 次/s，读取能力为 10 MB/s、100 次/s。 每个 EventStore 中最多创建 10 个 Shard，每个 Project 中最多创建 200 个 Shard。更多信息，请参见 [分区（Shard）](shard.md) 。 |
| 自动分裂 Shard | 打开 自动分裂 Shard 开关后，如果您写入的数据量超过已有 Shard 服务能力，日志服务会自动根据数据量增加 Shard 数量。更多信息，请参见 [管理](manage-shards.md) [Shard](manage-shards.md) 。 |
| 最大分裂数 | 打开 自动分裂 Shard 开关后，最多支持自动分裂至 256 个 readwrite 状态的 Shard。 |
| 记录外网 IP | 打开 记录外网 IP 开关后，日志服务自动把以下信息添加到日志的 Tag 字段中。 __client_ip__ ：日志来源设备的公网 IP 地址。 __receive_time__ ：日志到达服务端的时间，格式为 Unix 时间戳，表示从 1970-1-1 00:00:00 UTC 计算起的秒数。 |
## 修改EventStore
在事件存储>事件库页签中，将鼠标悬浮在目标EventStore上，选择>修改。
在EventStore属性页面中，单击修改。
修改保存时间，参数说明请参见[创建](manage-an-eventstore.md)[EventStore](manage-an-eventstore.md)。
管理Shard。
创建EventStore时，默认为EventStore创建2个Shard。在后续使用中，您可以根据业务需求分裂或合并Shard。具体操作，请参见[管理](manage-shards.md)[Shard](manage-shards.md)。
单击保存。
## 删除EventStore
警告
一旦删除EventStore，其存储的事件数据将会被永久删除，不可恢复，请谨慎操作。
在事件存储>事件库页签中，将鼠标悬浮在目标EventStore上，选择>删除。
在确认对话框中，单击确认。
## 删除事件数据
当事件数据保存时间达到您所设置的保存时间后，事件数据将被删除。因此您可以通过修改数据保存时间，从而删除事件数据。
重要
缩短数据保存时间后，日志服务将在1小时内删除所有已超过保存时间的数据。例如您原本的数据保存时间为5天，现修改为1天，则日志服务将在1小时内删除前4天的数据。
## 索引说明
创建EventStore后，日志服务会自动创建部分必需的字段索引。
| 字段名称 | 类型 |
| --- | --- |
| data | json |
| datacontenttype | text |
| dataschema | text |
| id | text |
| message | text |
| source | text |
| specversion | text |
| status | text |
| subject | text |
| time | text |
| title | text |
| type | text |
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
