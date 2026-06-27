# 兼容Redis的云数据库-倚天版实例-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/cost-efficient-instances

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

# 倚天版实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库 Tair（兼容 Redis）推出Redis倚天版实例，满足您低成本使用Redis的需求。

## 什么是倚天版实例

Redis倚天版实例为云原生部署模式，采用主备（master-replica）架构，兼容Redis 7.0、6.0与5.0版本，支持1~64 GB规格，适用于无需横向扩展集群的场景。您大约仅需付出标准版5~6折的费用，即可享受与标准版相同规格、相同性能的Redis实例。

倚天版实例存在如下使用限制：

- 

架构支持：主备架构。

- 

当前已开通如下地域：华东1（杭州）、华东2（上海）、华北2（北京）、华北3（张家口）、华南1（深圳）。

- 

倚天版实例不支持通过升级变配功能直接转换至标准版实例，但您可以通过DTS将数据迁移至标准版实例，更多信息请参见[实例间的单向数据同步](products/redis/documents/user-guide/configure-one-way-data-synchronization-between-apsaradb-for-redis-instances.md)。

## 倚天版与标准版的差异

| 对比项 | 倚天版 | 标准版 |
| --- | --- | --- |
| 特点 | 高性价比，功能、性能与标准版保持一致。 | 支持在不同架构间不停机切换，满足各种业务需求。 |
| CPU | ARM（倚天） | X86 |
| 支持架构 | 主备。 | 单副本、主备、集群、读写分离。 |
| 适用场景 | 无需横向扩展集群的场景。 | 各种场景。 |
| 规格上限 | 1 GB～64 GB | 256 MB～16 TB |
| 已支持地域 | 华东 1（杭州）、华东 2（上海）、华北 2（北京）、华北 3（张家口）、华南 1（深圳） | 全球共 25 个地域 |
| 命令 | 全部版本支持 CONFIG GET 命令。 | Redis 7.0 版本不支持 CONFIG GET 命令。 |


## 费用说明

倚天版实例为阶梯定价，实例规格越大，单价（单GB的价格）越便宜，下表以北京地域为例：

| 规格 | 实例规格费用（元/月） | 折合单价（元/月/GB） |
| --- | --- | --- |
| 1 GB（ 倚天版 ） | 52.10 | 52.10 |
| 2 GB（ 倚天版 ） | 101.52 | 50.76 |
| 4 GB（ 倚天版 ） | 243.20 | 60.80 |
| 8 GB（ 倚天版 ） | 413.68 | 51.71 |
| 16 GB（ 倚天版 ） | 742.70 | 46.42 |
| 24 GB（ 倚天版 ） | 1,100.58 | 45.86 |
| 32 GB（ 倚天版 ） | 1,458.44 | 45.58 |
| 64 GB（ 倚天版 ） | 2,889.88 | 45.15 |


重要

实际价格以产品购买页面为准。

## 分片规格

倚天版实例仅支持非集群（主备）架构，规格性能如下。

| 规格名称 | 规格代码（API 使用） | CPU 核数 | 内存（GB） | ESSD 云盘（GB） | 带宽 | 最大连接数 | QPS 参考值 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 GB（ 倚天版 ） | redis.shard.small.y.ee | 2 | 1 | 1 | 384 Mbps（48 MB/s） | 10,000 | 100,000 |
| 2 GB（ 倚天版 ） | redis.shard.mid.y.ee | 2 | 2 | 1 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 4 GB（ 倚天版 ） | redis.shard.large.y.ee | 2 | 4 | 1 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 8 GB（ 倚天版 ） | redis.shard.xlarge.y.ee | 2 | 8 | 1 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 16 GB（ 倚天版 ） | redis.shard.2xlarge.y.ee | 2 | 16 | 1 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 24 GB（ 倚天版 ） | redis.shard.3xlarge.y.ee | 2 | 24 | 1 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 32 GB（ 倚天版 ） | redis.shard.4xlarge.y.ee | 2 | 32 | 1 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 64 GB（ 倚天版 ） | redis.shard.8xlarge.y.ee | 2 | 64 | 1 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |


说明

ESSD云盘仅用于实例运行、存储日志，不作为数据存储的介质。

## 创建实例

访问[购买页](https://common-buy.aliyun.com/?commodityCode=kvstore_prepaid_public_cn&request={%22instance_scene%22:%22economical%22,%22region%22:%22cn-beijing%22,%22kvstore_iz%22:%22cn-beijing-l%22,%22kvstore_engineversion_type%22:%225.0%22}#/buy)，选择系列为倚天版，完成购买。

[上一篇：集群版-单副本](products/redis/documents/product-overview/standalone-cluster-instances.md)[下一篇：历史规格](products/redis/documents/product-overview/phased-out-specifications.md)

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
