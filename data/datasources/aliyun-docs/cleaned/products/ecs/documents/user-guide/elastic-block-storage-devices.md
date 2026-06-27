# 块存储类型以及如何使用块存储-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/elastic-block-storage-devices

# 块存储概述
块存储具有高性能、低时延的特性，包括云盘、本地盘和弹性临时盘，可像使用物理硬盘一样存储数据。
## 云盘
云盘基于分布式存储架构，为ECS实例提供高数据可靠性保证。
不同类型[云盘性能](block-storage-performance.md)有所不同，可根据实际的工作负载和应用程序需求选择合适的云盘。可查看[云盘计费](../block-storage-devices.md)，了解不同云盘类型的定价和计费规则。
### 按用途分类
| 云盘类型 | 说明 |
| --- | --- |
| 系统盘 | ECS 实例的启动盘，用于存储操作系统和程序文件等系统相关的数据。只能随 ECS 实例创建，生命周期与挂载的 ECS 实例相同。 |
| 数据盘 | 用于存储用户数据、日志和其他应用程序等非系统相关的数据。可以随 ECS 实例创建，也可以单独创建。 |
### 按存储冗余情况分类
云盘提供同城冗余存储和本地冗余存储两种存储冗余类型，覆盖从单可用区到多可用区的数据冗余机制，以保证数据的持久性和可用性。
同城冗余存储（ZRS）
同城冗余云盘采用多可用区的数据冗余存储机制，将用户的数据冗余存储在同一地域的3个或以上可用区，IDC、机柜及电力等均物理隔离，为ECS实例提供99.9999999999%（12个9）数据可靠性保证。当某个可用区不可用时，仍然能够保障数据的正常访问。
同城冗余云盘类型：[ESSD 同城冗余云盘](regional-essd-disks.md)。
典型应用场景：
数据库、大数据、中间件、ERP/CRM等核心系统同城容灾。
容器多可用区部署和漂移。
重要
数据由于需要同步写入同一地域的多个可用区，因此写时延可能高于本地冗余云盘，具体性能对比参见[云盘性能](block-storage-performance.md)。
当该地域不可用时，相关数据将不可访问。若业务需要跨地域的可用性保障，建议[创建自动快照策略](create-an-automatic-snapshot-policy-1.md)，定期创建快照并将其复制至其他地域。
本地冗余存储（LRS）
本地冗余云盘采用单可用区内的数据冗余存储机制，将用户的数据冗余存储在同1个可用区内多个设施的多个设备上，为ECS实例提供99.9999999%（9个9）数据可靠性保证。本地冗余存储能确保硬件失效时的数据持久性和可用性。
本地冗余云盘类型：、ESSD云盘、ESSD AutoPL云盘、ESSD PL-X云盘（邀测）、ESSD Entry云盘等。
典型应用场景：
[ESSD](essds.md)[云盘](essds.md)：
OLTP数据库（如MySQL、PostgreSQL、Oracle等）、NoSQL数据库（如MongoDB、HBase、Cassandra等）、Elasticsearch分布式日志。
作为操作系统的启动盘使用或替换上一代云盘中的高效云盘和普通云盘。
[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)：
容量与性能解耦，适用于业务所需的云盘容量固定，但需要更高的云盘性能的场景。
具备性能突发，适用于业务波动较大，波峰高频出现，需应对突发业务。
替换上一代云盘中的SSD 云盘。
[ESSD PL-X](essd-pl-x-cloud-disk.md)[云盘（邀测）](essd-pl-x-cloud-disk.md)：对云盘IOPS、吞吐量和时延有更高要求的OLTP数据库和KV数据库。
ESSD Entry云盘：
仅通用算力型（U实例）和经济型实例规格族e支持挂载ESSD Entry云盘。
开发与测试业务。
替换上一代云盘中的高效云盘和普通云盘。
重要
数据冗余存放在某个特定的可用区内。当该可用区不可用时，会导致相关数据不可访问。如果业务需要更高的可用性保障，建议使用ESSD 同城冗余云盘存储和使用数据。
以对比ESSD 同城冗余云盘与ESSD PL1云盘为例：
| 对比项 | ESSD 同城冗余云盘 | ESSD PL1 云盘 |
| --- | --- | --- |
| 存储冗余 | 同城冗余存储（ZRS） | 本地冗余存储（LRS） |
| 可靠性 | 99.9999999999%（12 个 9） | 99.9999999%（9 个 9） |
| 单盘最大 IOPS（Input/Output Operations Per Second） | 50,000 | 50,000 |
| 单盘最大吞吐量（MB/s） | 350 | 350 |
| 单路随机写平均时延（ms），Block Size=4K | 毫秒级 | 0.2 |
| 挂载范围 | 可挂载至 同地域任意可用区 的实例使用。 | 仅能挂载至 与云盘相同可用区 的实例使用。 |
| 单可用区故障影响 | 读写服务不受影响 | 无法提供读写服务 |
| 包月价格（以杭州地域为例） | 1.5 元/GB/月 | 1 元/GB/月 |
### 按性能分类
按云盘性能不同，分为ESSD系列云盘和上一代云盘。
ESSD系列云盘
| 云盘类型 | 特点 | 应用场景 | 数据可靠性保证 | 计费 |
| --- | --- | --- | --- | --- |
| [ESSD](essds.md) [云盘](essds.md) | 高 IOPS 低延迟 | 时延敏感的应用或者 I/O 密集型业务场景： 大型 OLTP 数据库 NoSQL 数据库 Elasticsearch 分布式日志 | 99.9999999% | 云盘容量费 |
| [ESSD AutoPL](essd-autopl-disks.md) [云盘](essd-autopl-disks.md) | 容量与性能可解耦 支持预配置云盘性能（允许在存储容量不变的情况下，根据业务需求灵活配置预配置性能） 支持性能突发（波动性业务在面临突发的数据读写压力时，ESSD AutoPL 云盘会根据业务实际情况临时提升云盘性能） | ESSD 云盘所适用的场景 云盘容量固定，云盘性能要求高 业务波动较大，波峰高频出现，需应对突发业务 | 99.9999999% | 云盘容量费 预配置性能费（开启后按量收费） 突发性能费（开启后按量收费） |
| [ESSD](regional-essd-disks.md) [同城冗余云盘](regional-essd-disks.md) | 高 IOPS（Input/Output Operations per Second） 同城冗余 | ESSD 云盘所适用的场景 数据库多可用区容灾 跨可用区的容器部署 自建或在云上部署 SaaS 服务 | 99.9999999999% | 云盘容量费 |
| [ESSD PL-X](essd-pl-x-cloud-disk.md) [云盘（邀测）](essd-pl-x-cloud-disk.md) | 超高 IOPS 超高吞吐量 超低时延 支持预配置云盘性能 | 对云盘 IOPS、吞吐量和时延有更高要求的 OLTP 数据库和 KV 数据库 | 99.9999999% | 云盘容量费 预配置性能费（默认开启，开启后收费） |
| ESSD Entry 云盘 仅 [通用算力型（U](general-work-force.md) [实例）](general-work-force.md) 和 [经济型实例规格族](shared-instance-families.md) [e](shared-instance-families.md) 支持挂载 ESSD Entry 云盘。 | 高 IOPS 低延迟 | 开发与测试业务 作为系统盘 | 99.9999999% | 云盘容量费 |
上一代云盘
SSD云盘、高效云盘和普通云盘属于上一代云盘产品，已在部分地域及可用区逐步停止售卖。在选择云盘时，建议选用ESSD PL0云盘或ESSD Entry云盘替换高效云盘和普通云盘，选用ESSD AutoPL云盘替换SSD云盘。
| 云盘类型 | 特点 | 应用场景 | 计费 |
| --- | --- | --- | --- |
| SSD 云盘 | 高随机读写性能 高可靠性 | I/O 密集型应用 中小型关系数据库和 NoSQL 数据库 | 云盘容量费 |
| 高效云盘 | 高性价比 高可靠性 | 开发与测试业务 作为系统盘 | 云盘容量费 |
| 普通云盘 | 高性价比 | 成本较低，适用于对存储性能要求不高的开发与测试业务 | 云盘容量费 |
## 弹性临时盘
[弹性临时盘](elastic-ephemeral-disks.md)（Elastic Ephemeral Disk）是一款可灵活随实例创建或单独创建的、由用户自定义选择容量大小的块存储设备，作为临时数据存储使用，为ECS实例提供临时数据存储空间，具备高性能、高性价比等特点。
## 本地盘
[本地盘](local-disks.md)无存储冗余能力，数据仅存放在ECS实例所在物理机上的本地硬盘设备中，可为ECS实例提供本地存储访问能力，适用于对存储I/O性能、海量存储性价比有极高要求的业务场景。阿里云提供以下两种本地盘：
| 类型 | 搭配的实例规格 | 应用场景 |
| --- | --- | --- |
| NVMe SSD 本地盘 | 以下实例规格族搭配使用了 NVMe SSD 本地盘： 本地 SSD 型 i4、i4g、i4r、i3、i3g、i2、i2g、i2ne、i2gne、i1 GPU 计算型 gn5 | 以本地 SSD 型实例规格族为例，NVMe SSD 本地盘适用于以下场景： 网络游戏、电商、视频直播、媒体等在线业务。满足 I/O 密集型应用对块存储的低时延和高 I/O 性能需求。 对存储 I/O 性能有较高要求，同时具备应用层高可用架构的业务场景。例如，NoSQL 非关系型数据库（例如 Cassandra、MongoDB、HBase 等）、MPP 数据仓库和分布式文件系统等。 |
| SATA HDD 本地盘 | 搭配使用的实例规格族包括大数据型 d3s、d2c、d2s、d1ne 和 d1。 | 适用于互联网行业、金融行业等有大数据计算与存储分析需求的行业，进行海量数据存储和离线计算的业务场景。充分满足以 Hadoop 为代表的分布式计算业务类型对 ECS 实例存储性能、存储容量和内网带宽的多方面要求。 |
可查看[实例规格族](overview-of-instance-families.md)，了解有关本地SSD型实例规格和大数据型实例规格的性能详情。
## 块存储的数据安全
除数据擦除机制外，其他内容仅适用于云盘，不适用于本地盘和弹性临时盘。
读写稳定性
在同一可用区中，业务数据以多副本的形式分布存储在块存储集群中，保证读写过程中的数据稳定性，保障数据的持久性和完整性。更多信息，请参见[ESSD 云盘数据可靠性](essd-cloud-disk-data-reliability.md)。
主动备份
可以定期[手动创建单个快照](create-a-snapshot.md)，提高业务数据的安全性。快照是阿里云备份产品，为云盘提供数据备份能力，确保日志和客户交易等信息有备份可查询。
数据擦除机制
删除的数据不会被其他用户通过任何途径访问，分布式块存储系统中已删除的数据一定会被完全擦除。主要通过以下机制保证数据擦除的完整性：
云盘底层基于顺序追加写实现，该设计充分利用物理盘顺序写高带宽低时延的特性。基于追加写的特性，删除云盘逻辑空间的操作会被作为元数据记录，一切对该逻辑空间的读操作，存储系统会确保返回全零。同理，对逻辑空间的覆盖写不会立即覆盖物理磁盘上对应空间，存储系统通过修改逻辑空间与物理空间之间的映射关系来实现云盘的覆盖写，确保无法读取被覆盖的数据。一切删除或者覆盖写操作形成的物理磁盘上的遗留数据，会从底层物理磁盘上强制永久删除。
当释放块设备（云盘）时，存储系统立即销毁元数据，确保无法继续访问数据。同时，该云盘对应的物理存储空间会被回收。物理空间再次被分配前一定是清零过的，在首次写入数据前，所有新建的云盘的读取返回全部是零。
数据加密
对于数据敏感型应用，建议加密存储设备。ECS云盘加密采用行业标准的AES-256算法，利用密钥[加密云盘](encryption-overview.md)以及云盘快照。从ECS实例传输到云盘的数据会被自动加密，并在读取数据时自动解密。
## 相关文档
有关块存储的使用限制及配额，请参见[块存储使用限制](limitations.md)。
有关云盘的常用操作介绍，请参见[创建并使用云盘指引](quickly-create-and-use-disks.md)。
阿里云除了提供ECS块存储以外，还提供对象存储OSS、文件存储NAS等存储产品，满足不同场景下的业务需求。更多信息，请参见[如何选用](https://help.aliyun.com/zh/nas/product-overview/comparison-of-nas-oss-and-ebs)[NAS、OSS](https://help.aliyun.com/zh/nas/product-overview/comparison-of-nas-oss-and-ebs)[和](https://help.aliyun.com/zh/nas/product-overview/comparison-of-nas-oss-and-ebs)[EBS？](https://help.aliyun.com/zh/nas/product-overview/comparison-of-nas-oss-and-ebs)。
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
