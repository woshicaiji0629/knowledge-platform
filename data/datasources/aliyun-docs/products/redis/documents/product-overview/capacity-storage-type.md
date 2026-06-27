# Tair磁盘型的实例规格-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/product-overview/capacity-storage-type

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

# 磁盘型实例规格

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍Tair（企业版）磁盘型的规格，包含内存容量、连接数、带宽等信息。

## 实例规格

下表为单个分片的规格。

- 

标准架构的整体性能为：分片规格性能。

- 

集群架构的整体性能为：单个分片的性能 * 分片数。

说明

- 

自2024年05月08日起，在创建新实例或升级实例规格时，磁盘型实例的每分片最大连接数将提升至60,000及以上，具体信息请参见下表。

- 

自2025年03月14日起，Tair（企业版）对ESSD型32C - 128GB及以上规格（tair.essd.standard.8xlarge、tair.essd.standard.13xlarge、tair.essd.standard.16xlarge）、SSD型32C-256GB规格（tair.localssd.c1m8.8xlarge、tair.localssd.c1m8.with.proxy.8xlarge）进行升级。在创建新实例或升级实例规格时，每分片最大连接数提升至100,000。

- 

不同地域、可用区可创建的实例规格以实际库存为准。

### ESSD型分片规格

ESSD型实例仅支持[标准架构](products/redis/documents/product-overview/standard-master-replica-instances.md)，暂不支持集群架构。

| 规格名称 | 规格代码（API 使用） | CPU 核数 | 内存（GB） | 可选存储性能级别与容量（GB） | 最大连接数 | 带宽 |
| --- | --- | --- | --- | --- | --- | --- |
| 4C - 16GB | tair.essd.standard.xlarge | 4 | 16 | PL1：60~250 | 60,000 | 1,500 Mbps（187.5 MB/s） |
| 8C - 32GB | tair.essd.standard.2xlarge | 8 | 32 | PL1：60~500 PL2：470~1000 | 60,000 | 2,000 Mbps（250 MB/s） |
| 16C - 64GB | tair.essd.standard.4xlarge | 16 | 64 | PL1：60~1000 PL2：470~2000 PL3：1270~4000 | 60,000 | 3,000 Mbps（375 MB/s） |
| 32C - 128GB | tair.essd.standard.8xlarge | 32 | 128 | PL2：470~4000 PL3：1270~8000 | 100,000 | 5,000 Mbps（625 MB/s） |
| 64C - 256GB | tair.essd.standard.16xlarge | 64 | 256 | PL2：470~8000 PL3：1270~16000 | 100,000 | 8,000 Mbps（1,000 MB/s） |


说明

ESSD PL3（Performance Level 3）的性能优于PL2与PL1，更多信息请参见[ESSD](products/ecs/documents/user-guide/essds.md)。

### SSD型标准架构与集群架构直连模式的分片规格

以下规格适用于标准架构与集群架构直连模式的磁盘（SSD）型实例，更多信息关于SSD的信息请参见[本地盘](products/ecs/documents/user-guide/local-disks.md)。

| 规格名称 | 规格代码（API 使用） | CPU 核数 | 内存（GB） | 存储容量（GB） | 最大连接数 | 带宽 |
| --- | --- | --- | --- | --- | --- | --- |
| 4C-32GB | tair.localssd.c1m8.xlarge | 4 | 32 | 640 | 60,000 | 1,500 Mbps（187.5 MB/s） |
| 8C-64GB | tair.localssd.c1m8.2xlarge | 8 | 64 | 1,280 | 60,000 | 2,500 Mbps（312.5 MB/s） |
| 16C-128GB | tair.localssd.c1m8.4xlarge | 16 | 128 | 2,560 | 60,000 | 5,000 Mbps（625 MB/s） |
| 32C-256GB | tair.localssd.c1m8.8xlarge | 32 | 256 | 5,120 | 100,000 | 10,000 Mbps（1,250 MB/s） |


### SSD型集群架构代理模式的分片规格

以下规格适用于集群架构代理模式的磁盘（SSD）型实例。

| 规格名称 | 规格代码（API 使用） | CPU 核数 | 内存（GB） | 存储容量（GB） | 最大连接数 | 带宽 |
| --- | --- | --- | --- | --- | --- | --- |
| 4C-32GB | tair.localssd.c1m8.with.proxy.xlarge | 4 | 32 | 640 | 60,000 | 1,500 Mbps（187.5 MB/s） |
| 8C-64GB | tair.localssd.c1m8.with.proxy.2xlarge | 8 | 64 | 1,280 | 60,000 | 2,500 Mbps（312.5 MB/s） |
| 16C-128GB | tair.localssd.c1m8.with.proxy.4xlarge | 16 | 128 | 2,560 | 60,000 | 5,000 Mbps（625 MB/s） |
| 32C-256GB | tair.localssd.c1m8.with.proxy.8xlarge | 32 | 256 | 5,120 | 100,000 | 10,000 Mbps（1,250 MB/s） |


说明

集群架构代理模式与读写分离架构实例的最大连接数不直接与分片规格相关，具体计算规则参考[最大连接数计算规则](products/redis/documents/product-overview/capacity-storage-type.md)。

## 性能说明

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

| 架构 | 性能说明 |
| --- | --- |
| [标准架构](products/redis/documents/product-overview/standard-master-replica-instances.md) | 实例整体的性能与实例规格表中对应的性能一致。 |
| [集群架构直连模式](products/redis/documents/product-overview/cluster-master-replica-instances.md) [集群架构代理模式](products/redis/documents/product-overview/cluster-master-replica-instances.md) | 实例整体的性能 = 分片规格的性能 * 分片数。 说明 集群架构代理模式实例的带宽上限为 20Gbps(2.5GB/s)，而最大连接数的计算规则取决于 Proxy 节点数，与分片数无关，上限为 50 万。 例如实例具备 4 个分片，分片规格为 tair.localssd.c1m8.xlarge ，每个分片的性能为： CPU 核数：4 核 内存：32 GB SSD 容量：640 GB 连接数：60,000 带宽：1,500 Mbps（187.5 MB/s） 那么，该实例的整体性能即为： CPU 核数：16 核 内存：128 GB SSD 容量：2,560 GB 分片最大连接数为：240,000 Proxy 最大连接数为：480,000（以该连接数为准）。 带宽：6,000 Mbps（750 MB/s） |


## CPU核数说明

为保障服务稳定运行，系统会保留其中1个CPU用于处理后台任务。如果实例为集群或读写分离架构，每个数据分片或每个只读节点均会保留其中1个CPU用于处理后台任务。

## 带宽说明

- 

上表中的带宽值是单个分片的带宽，集群架构、读写分离架构实例的总带宽为所有分片节点带宽的总和。

- 

集群架构代理模式与读写分离架构的带宽上限为20Gbps(2.5GB/s)，达到该上限后，即使增加分片数量，带宽也不会提高。集群架构直连模式无整体带宽限制。

- 

带宽分别应用于上行带宽和下行带宽，如果某规格的总带宽为768 Mbps（96 MB/s），则该规格实例的上下行带宽都是768 Mbps（96 MB/s）。

- 

Tair和Redis开源版的带宽限制，是指分片节点的带宽，与网络连接类型无关。

更多关于带宽的常见问题请参见[带宽的常见问题](products/redis/documents/user-guide/faq-about-bandwidth.md)。

## 最大连接数计算规则

- 

代理模式：实例最大连接数的计算规则为：min(Proxy节点数*12万, 50万）。因此上限为50万，如业务连接数需求超过此限制，建议采用集群直连模式，连接数可随分片数量线性扩展。

Tair磁盘型的Proxy节点数与分片规格的CPU核心数相关，不同规格达到上限所需的分片数不同。

Proxy节点数计算公式为：

Proxy 节点数 = max( ⌈分片数 × 单分片 CPU 核数 × 0.1875⌉, 2 )

- 

⌈ ⌉ 表示向上取整

- 

0.1875 为 Proxy 线程数与CPU核心数的比值（3:16）

- 

最小 Proxy 节点数为 2

示例

假设实例为4 核、3 分片：

- 

Proxy 节点数 = max(⌈3 × 4 × 0.1875⌉ , 2) = max(⌈2.25⌉ , 2) = 3 个

- 

最大连接数 = min(3 × 4 × 30000 , 500000) = 360000

| 单分片 CPU 核数 | 达到 500,000 上限的最小分片数 |
| --- | --- |
| 4 核 | 7 分片 |
| 8 核 | 4 分片 |
| 16 核 | 2 分片 |


- 

直连模式：实例最大连接数的上限为单分片的最大连接数 * 分片数 。

## 已停售规格

部分规格已经停售，但已购买的实例仍可正常使用。您可以在本章节中查看已停售规格的连接数限制、带宽、QPS参考值等相关信息。

展开查看详情

ESSD型：

| 规格名称 | 规格代码（API 使用） | CPU 核数 | 内存（GB） | 可选存储性能级别与容量（GB） | 最大连接数 | 带宽 |
| --- | --- | --- | --- | --- | --- | --- |
| 52C - 192GB | tair.essd.standard.13xlarge | 52 | 192 | PL2：470~6000 PL3：1270~12000 | 100,000 | 8,000 Mbps（1,000 MB/s） |


## 相关文档

- 

[磁盘（ESSD）型性能白皮书](products/redis/documents/support/performance-white-paper-of-essd-based-instances.md)

- 

[磁盘（SSD）型性能白皮书](products/redis/documents/support/disk-ssd-performance-white-paper.md)

- 

[Tair（企业版）命令支持与限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)

[上一篇：持久内存型实例规格](products/redis/documents/product-overview/persistent-memory-type.md)[下一篇：内存型经典版实例规格](products/redis/documents/product-overview/enhanced-edition.md)

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
