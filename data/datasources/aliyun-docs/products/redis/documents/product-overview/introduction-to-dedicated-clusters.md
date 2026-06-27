# 专属集群数据库实例管理-云数据库专属集群-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/introduction-to-dedicated-clusters

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

# 云数据库专属集群

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库专属集群是由多台主机（底层服务器，如ECS I2服务器、神龙服务器）组成的集群。相对于全托管数据库，可以实现更灵活的资源调度、更强大的企业级数据库服务、更丰富的权限等。

## 基本功能

MyBase功能是以集群形式批量管理实例。一个地域可以创建多个专属集群，一个专属集群包含多个主机，一个主机可以包含多个实例。

以集群形式，MyBase可提供资源调度、主机管理、实例管理三大功能：

- 

资源调度：您可以通过资源视角配置超配比，充分利用资源。资源分为[CPU](https://www.aliyun.com/getting-started/what-is/what-is-cpu)、内存、存储空间、IOPS、网络流量等多个维度。

- 

主机管理：主机是MyBase的资源载体，管理主机包括添加主机、替换主机、连接主机、设置主机分配实例状态等。

- 

实例管理：管理数据库服务实例，包括主实例、备实例、只读实例和日志实例四种类型。

## 产品优势

使用专属集群MyBase可以实现更加灵活的资源调度、更加强大的企业级数据库服务以及更加丰富的权限，详情请参见[原理优势](https://help.aliyun.com/zh/document_detail/156991.html#concept-2438148)。

## 支持的数据库引擎和实例版本

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

| 引擎 | 支持的系列及其版本 |
| --- | --- |
| MySQL | 高可用版：MySQL 5.6、MySQL 5.7、MySQL 8.0 主从版：MySQL 5.7、MySQL 8.0 |
| SQL Server | 高可用版： SQL Server 2019 标准版 SQL Server 2017 标准版、SQL Server 2017 企业版 SQL Server 2016 标准版、SQL Server 2016 企业版 SQL Server 2012 标准版、SQL Server 2012 企业版 基础版： SQL Server 2019 标准版 SQL Server 2017 标准版、SQL Server 2017 企业版、SQL Server 2017 Web SQL Server 2016 标准版、SQL Server 2016 企业版、SQL Server 2016 Web SQL Server 2012 标准版、SQL Server 2012 企业版、SQL Server 2012 Web 集群版：SQL Server 2017 企业集群版、SQL Server 2019 企业集群版 |
| Redis | 社区版：Redis 5.0、Redis 6.0 企业版性能增强型：Redis 5.0 |


## 计费说明

## 云数据库专属集群MyBase本地盘实例计费方式如下：

购买本地盘主机费用包含计算和存储费用，在创建实例时无需额外支付存储费用。

- 

- 

- 

| 收费项 | 计费方式 | 说明 | 计费公式 | 价格 |
| --- | --- | --- | --- | --- |
| 主机 | 包年包月 | 也称为预付费，即在新建 MyBase 主机时支付费用。 | 主机费用=主机包年包月单价×主机数量×购买时长。 | [MyBase MySQL](https://help.aliyun.com/zh/document_detail/147145.html#topic-1849685) [主机规格及售价](https://help.aliyun.com/zh/document_detail/147145.html#topic-1849685) [MyBase SQL Server](https://help.aliyun.com/zh/document_detail/414521.html#topic-2193954) [主机规格及售价](https://help.aliyun.com/zh/document_detail/414521.html#topic-2193954) [MyBase Redis](https://help.aliyun.com/zh/document_detail/212205.html#topic-2069555) [主机规格及售价](https://help.aliyun.com/zh/document_detail/212205.html#topic-2069555) |


## 云数据库专属集群MyBase云盘实例计费方式如下：

云盘类型的主机仅包含计算费用，在购买实例时需要支付云盘实例存储空间的费用。

- 

- 

- 

- 

- 

| 收费项 | 计费方式 | 说明 | 计费公式 | 价格 |
| --- | --- | --- | --- | --- |
| 主机 | 包年包月 | 也称为预付费，即在新建 MyBase 主机时支付费用。 | 主机费用=主机包年包月单价×主机数量×购买时长。 | [MyBase MySQL](https://help.aliyun.com/zh/document_detail/147145.html#topic-1849685) [主机规格及售价](https://help.aliyun.com/zh/document_detail/147145.html#topic-1849685) [MyBase SQL Server](https://help.aliyun.com/zh/document_detail/414521.html#topic-2193954) [主机规格及售价](https://help.aliyun.com/zh/document_detail/414521.html#topic-2193954) [MyBase Redis](https://help.aliyun.com/zh/document_detail/212205.html#topic-2069555) [主机规格及售价](https://help.aliyun.com/zh/document_detail/212205.html#topic-2069555) |
| 实例 | 按量计费 | 也称为后付费，即每小时生成一个收费订单，并从阿里云账号扣费。 适合短期需求，用完可立即释放 MyBase 实例，节省费用。 | 实例费用=云盘实例存储单价×存储容量×时长。 说明 [存储资源包](https://help.aliyun.com/zh/document_detail/176152.html#task-2559294) 可以抵扣同一地域下云盘实例存储空间的费用，您可以按需购买，降低存储成本。 | [实例存储空间售价](https://help.aliyun.com/zh/document_detail/450544.html#task-2240079) |


关于购买主机计费案例，详情请参见[计费案例](https://help.aliyun.com/zh/document_detail/173901.html#concept-2534434)。

## 典型场景

- 

场景一：满足数据安全合规性要求，在云平台外部和内部的安全威胁下，MyBase能时刻保护您的数据，与其他用户安全隔离。

- 

场景二：满足极致性能要求，如您需要独占物理资源，对接原有监控运维系统，在保持原有数据库运维习惯的情况下，MyBase可以弹性调整实例资源配置应对流量高峰，详情请参见[弹性扩缩容应对流量高峰](https://help.aliyun.com/zh/document_detail/183919.html#task-1951391)。

- 

场景三：在MyBase中提高CPU和存储空间的利用率，降低上云使用数据库成本，详情请参见[设置集群超配降低成本](https://help.aliyun.com/zh/document_detail/183798.html#task-1951393)。

- 

场景四：支持开放主机OS和数据库权限，MyBase可以开放主机的部分OS权限，使用定制化脚本，详情请参见[使用定制化脚本](https://help.aliyun.com/zh/document_detail/184017.html#concept-1951395)。

## 快速入门

- [创建集群](https://help.aliyun.com/zh/document_detail/182324.html#task-2319931)

您需要先创建专属集群MyBase（原主机组），才能使用专属集群MyBase内的各项功能。

说明创建集群后您可以查看、修改、删除专属集群，详情请参见[管理集群](https://help.aliyun.com/zh/document_detail/182328.html#task-2320061)。

- [添加主机](https://help.aliyun.com/zh/document_detail/182325.html#task-2320133)

专属集群MyBase创建后，您需要在专属集群内添加主机，才能在主机上创建实例并使用专属集群MyBase的各项功能。

- [创建实例](https://help.aliyun.com/zh/document_detail/182326.html#task-2320193)

主机创建后，您需要在专属集群MyBase内创建实例才能正常使用专属集群MyBase的各项功能，系统会根据资源分配模式在主机上创建实例。

- [迁移到专属集群](https://help.aliyun.com/zh/document_detail/182327.html#concept-1940531)

实例创建完成后，您可以将数据库迁移到专属集群MyBase的实例上，并且专属集群MyBase创建的实例可被数据传输服务DTS正常读取。

[上一篇：云原生实例和经典实例对比](products/redis/documents/product-overview/comparison-between-tair-instances-that-cloud-native-and-classic.md)[下一篇：应用场景](products/redis/documents/product-overview/common-scenarios.md)

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
