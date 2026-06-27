# 实例规格选型方法与场景推荐-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/user-guide/best-practices-for-instance-type-selection

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# ECS实例规格选型指导

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

购买ECS实例之前，您需要结合性能、价格、工作负载等因素，做出性价比与稳定性最优的决策。本文主要介绍如何结合实际业务场景选购阿里云云服务器ECS。

## 了解实例规格族

在进行规格选型之前，您需要提前了解以下信息：

- 

[实例规格分类与命名](products/ecs/documents/user-guide/instance-specification-naming-and-classification.md)：帮助您更好地理解实例规格族的命名及分类信息。

- 

[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)：了解在售实例规格族的详细信息。

## 实例适用场景

### 企业级实例

### 异构计算实例

## 根据预装软件选型

根据您需要在系统预装软件推荐实例规格族。

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

| 应用类型 | 常用应用 | 选型原则 | 推荐实例规格族 |
| --- | --- | --- | --- |
| 负载均衡 | Nginx | 应用特点：需要支持高频率的新建连接操作。 CPU 计算能力：要求较高。 内存：要求不高。 | c8i、c7、c7nex、g5ne |
| RPC 产品 | SOFA Dubbo | 应用特点：网络链接密集型；进程运行时需要消耗较高的内存。 | g8a、g7nex、g8i、g7 |
| 缓存 | Redis Memcache Solo | CPU 计算能力：要求不高。 内存：要求较高。 | r8i、r8a、r7、r7a |
| 配置中心 | ZooKeeper | 在应用启动协商时会有大量 I/O 读写操作。 CPU 计算能力：要求不高。 内存：要求不高。 | c8a、c7、c8i、u1 |
| 消息队列 | Kafka RabbitMQ | 从消息完整性方面考虑，存储优先选用云盘。 CPU 计算能力：要求不高。 内存和 vCPU 配比通常为 1:1。 存储：要求不高。 | c8a、c7、c8i、u1 |
| 容器编排 | Kubernetes | 通过弹性裸金属服务器和容器的组合，可以最大限度地挖掘计算潜能。 | ebmc6e、ebmg6e、ebmc6、ebmg6、ebmc6a、ebmc7a、ebmg6a、ebmg7a 系列 |
| 大表存储 | HBase | 一般可以选择 d 系列。 如果业务存在超高 IOPS（Input/Output Operations Per Second）需求，可以选择 i 系列。 | d3c、d3s、i4 |
| 数据库 | MySQL NoSQL | 对于存储有弹性扩展的需求，可以选择 ECS 和 ESSD。 对于 I/O 敏感型业务的需求，优先选择 i 系列。 | g8a、g7、g8i、i4, |
| SQLServer | 由于 Windows 的 I/O 单通道特性，对 I/O 读写能力要求较高，优先选择 ESSD。 ECS 的逻辑和物理扇区设置为 4 K。 | g8a、g7、r7、r8i、g8i |  |
| 文本搜索 | Elasticsearch | 选用内存与 vCPU 配比较大的 ECS 规格。 日常需要将数据库数据导出成 ES 文件，对 I/O 读写有要求。 | i4、i4r、i3、i2 |
| 实时计算 | Flink Blink | 基于存储量可以选择 ECS 通用规格和云盘，也可以选择 d 系列。 | i4g、i4、d3c |
| 离线计算 | Hadoop HDFS CDH | 优先选择 d 系列。 | d3s、d3c |
| 视频转码 | 点播 直播 | CPU 计算能力：要求高 内存：要求不高 IO：要求不高 | c8y 、hfc8i |
| 大数据 | Spark Hive | CPU 计算能力：要求高 内存：内存带宽要求高 IO：存储带宽要求高 | g8y、r8y |


## 根据细分业务场景选型

### 通用应用、游戏服务、视频直播场景推荐

在该类场景中，性能需求表现为CPU计算密集型，您需要相对均衡的处理器与内存资源配比，通常选用CPU与内存配比1:2、系统盘和数据盘选用ESSD云盘。如果业务需要更强的网络性能，如视频弹幕等，您可以选用同系列中更高规格的实例规格，提高网络收发包能力（PPS）。

| 场景分类 | 场景细分 | 推荐规格族 | 性能需求 | 处理器与内存比 |
| --- | --- | --- | --- | --- |
| 通用应用 | 均衡性能应用，后台应用 | g 系列，如 g7 | 中主频，计算密集型 | 1:4 |
| 高网络收发包应用 | g 系列，如 g7 | 高网络 PPS，计算密集型 | 1:4 |  |
| 高性能计算 | hfc 系列，如 hfc7 | 高主频，计算密集型 | 1:2 |  |
| 游戏应用 | 高性能端游 | hfc 系列，如 hfc7 | 高主频 | 1:2 |
| 手游、页游 | g 系列，如 g6e | 中主频 | 1:4 |  |
| 视频直播 | 视频转发 | g 系列，如 g7 | 中主频，计算密集型 | 1:4 |
| 直播弹幕 | g 系列，如 g7 | 高网络 PPS，计算密集型 | 1:4 |  |


### Hadoop、Spark、Kafka大数据场景推荐

在该类场景中，由于涉及不同的节点，性能需求表现较为复杂，您需要均衡各个节点的性能表现，包括计算、存储吞吐量、网络性能等。

- 

管理节点：当作通用场景处理，推荐使用g系列。

- 

计算节点：当作通用场景处理，推荐使用g系列。根据集群规模的不同，需要选择的实例规格不同。例如100个节点以下可以选用ecs.g7.4xlage，100个节点以上可以选用ecs.g7.8xlage。

- 

缓存节点：用于存储热数据或部署RSS，侧重磁盘和网络IO性能，推荐使用i4g、i2g。

- 

计算缓存节点：用于计算和缓存，兼备计算性能和IO性能、磁盘容量，推荐使用i4、i4r、d3c。

说明

计算节点在计费模式上可以采用抢占式实例，实现性价比最优化。更多信息，请参见[什么是抢占式实例](products/ecs/documents/user-guide/what-is-a-spot-instance.md)。

- 

数据节点：需要高存储吞吐、高网络吞吐、均衡的处理器与内存配比，推荐您使用大数据型（d系列）规格族。例如MapReduce/Hive可选择ecs.d2s.5xlarge、ecs.d3s.4xlarge等，Spark/Mlib可选择ecs.d2s.10xlarge。

### 数据库、缓存、搜索场景推荐

在该类场景中，实例规格的处理器与内存配比一般要求高于1:4，部分软件对存储I/O读写能力及时延性能较为敏感，建议您选用单位内存性价比较高的规格族。

| 场景分类 | 场景细分 | 推荐规格族 | 处理器与内存比 | 数据盘 |
| --- | --- | --- | --- | --- |
| 关系型数据库 | 高性能，依赖应用层高可用 | i 系列 | 1:4 | 本地 SSD 存储、高效云盘、SSD 云盘 |
| 中小型数据库 | g 系列，或其他内存占比为 1:4 的规格族 | 1:4 | 高效云盘、SSD 云盘 |  |
| 高性能数据库 | i、r 系列 | 1:8 | 高效云盘、SSD 云盘 |  |
| 分布式缓存 | 中内存消耗场景 | g 系列，或其他内存占比为 1:4 的规格族 | 1:4 | 高效云盘、SSD 云盘 |
| 高内存消耗场景 | r 系列、i 系列 | 1:8 | 高效云盘、SSD 云盘 |  |
| NoSQL 数据库 | 高性能，应用层高可用 | i 系列 | 1:4 | 本地 SSD 存储、高效云盘、SSD 云盘 |
| 中小型数据库 | g 系列，或其他内存占比为 1:4 的规格族 | 1:4 | 高效云盘、SSD 云盘 |  |
| 高性能数据库 | i4、i4r 系列 | 1:8 | 高效云盘、SSD 云盘、本地 SSD 存储 |  |
| ElasticSearch | 小集群，靠云盘保证数据高可用 | g 系列，或其他内存占比为 1:4 的规格族 | 1:4 | 高效云盘、SSD 云盘 |
| 大集群，高可用 | d 系列 | 1:4 | 本地 SSD 存储、高效云盘、SSD 云盘 |  |


以数据库为例，在传统方式中，业务系统直接对接OLTP数据库，数据冗余大多通过RAID磁盘阵列实现。选择云服务器ECS，您的轻载、重载数据库都能实现灵活部署。

- 

轻载数据库：采用i4r、i4g系列实例搭配云盘使用，性价比更高。

- 

重载数据库：需要高存储IOPS和低读写延时，推荐您使用本地SSD型i系列实例规格族（搭配了高I/O型本地NVMeSSD本地盘），满足大型重载数据库的要求。

### 深度学习、图像处理场景推荐

在该类场景中，应用需要高性能的GPU加速器，在GPU和CPU配比方面有如下建议。

- 

深度学习训练：GPU与CPU比例推荐为1:8到1:12之间。

- 

通用深度学习：GPU与CPU比例推荐为1:4到1:48之间。

- 

图像识别推理：GPU与CPU比例推荐为1:4到1:12之间。

- 

语音识别与合成推理：GPU与CPU比例推荐为1:16到1:48之间。

常见场景的GPU选型推荐如下图所示。

## 验证与调整

当您完成选型并开始使用云服务器ECS实例后，建议您根据一段时间的性能监控信息，验证所选实例规格是否合适。

假设您选择了ecs.g8i.xlarge，通过监控发现实例CPU使用率一直较低，建议您检查是否是由于实例内存占用率较高所致。查询方法如下：

- 

[通过](products/ecs/documents/user-guide/view-the-monitoring-information-of-an-ecs-instance.md)[ECS](products/ecs/documents/user-guide/view-the-monitoring-information-of-an-ecs-instance.md)[控制台查看监控信息](products/ecs/documents/user-guide/view-the-monitoring-information-of-an-ecs-instance.md)

- 

[查看云盘监控信息](products/ecs/documents/user-guide/view-the-monitoring-data-of-a-disk.md)

如果内存占用较高，您可以将当前实例调整为处理器与内存配比更合适的实例规格。更多信息可参考：

- 

[升降配方式概述](products/ecs/documents/user-guide/overview-of-instance-configuration-changes.md)

- 

[支持变配的实例规格](products/ecs/documents/user-guide/instance-families-that-support-instance-type-changes.md)

[上一篇：实例规格分类与命名](products/ecs/documents/user-guide/instance-specification-naming-and-classification.md)[下一篇：通用型（g系列）](products/ecs/documents/user-guide/general-purpose-instance-families.md)

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
