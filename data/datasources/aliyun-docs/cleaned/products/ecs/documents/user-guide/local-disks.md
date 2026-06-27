# 云服务器实例本地硬盘存储-本地盘-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/user-guide/local-disks

# 本地盘
本地盘是ECS实例所在物理机上的本地硬盘设备，为ECS实例提供本地缓存访问能力。由于本地盘直接连接到物理机上，因此它具有低时延、高随机IOPS、高吞吐量的优势，适用于高性能缓存场景，比如需要大量访问的缓存系统等。本文介绍本地盘的类型以及性能规格等。
警告
本地盘的数据可靠性取决于物理机的可靠性，存在单点故障风险，物理机单点故障可能影响多台实例运行。使用本地盘存储数据有丢失数据的风险，请勿在本地盘上存储需要长期保存的业务数据。
您可以通过以下方式提升本地盘数据的容灾备份能力，但无法完全规避数据丢失风险。
通过云备份服务备份恢复与容灾，云备份作为阿里云统一灾备平台，支持文件或文件目录级别的ECS文件备份与恢复。
定期备份至对象存储OSS，针对存放在对象存储OSS上的数据，阿里云提供多种数据备份方式。
定期备份至云盘，云盘基于异步复制技术实现云盘的跨可用区或跨地域容灾能力，具有更强的容灾备份能力。
具体操作，请参见[备份本地盘文件](backup-local-disk-data.md)。
## 使用限制
本地盘需要先初始化才能正常使用。
购买了本地盘实例后，请先登录ECS实例初始化本地盘。具体操作可以参考云盘初始化操作：[初始化数据盘](initialize-a-data-disk.md)。
本地盘不支持以下操作：
单独创建全新本地盘
使用快照创建本地盘
挂载本地盘
单独卸载并释放本地盘
扩容本地盘
重要
严禁对本地盘进行扩容，扩容本地盘的容量可能会破坏分区表和文件系统结构，影响业务的连续性。
重新初始化本地盘
为本地盘创建快照
使用快照回滚本地盘
## 本地盘类型
说明
本文主要描述当前与ECS实例一起销售的本地盘的信息。有关本地SSD型实例规格和大数据型实例规格的性能详情，请参见[实例规格族](overview-of-instance-families.md)。
本地盘适用于对存储I/O性能、海量存储性价比有极高要求的业务场景。阿里云提供以下两种本地盘：
| 类型 | 搭配的实例规格 | 应用场景 |
| --- | --- | --- |
| NVMe SSD 本地盘 | 以下实例规格族搭配使用了 NVMe SSD 本地盘： 本地 SSD 型 i4、i4g、i4r、i3、i3g、i2、i2g、i2ne、i2gne、i1 GPU 计算型 gn5 | 以本地 SSD 型实例规格族为例，NVMe SSD 本地盘适用于以下场景： 网络游戏、电商、视频直播、媒体等在线业务。满足 I/O 密集型应用对块存储的低时延和高 I/O 性能需求。 对存储 I/O 性能有较高要求，同时具备应用层高可用架构的业务场景。例如，NoSQL 非关系型数据库（例如 Cassandra、MongoDB、HBase 等）、MPP 数据仓库和分布式文件系统等。 |
| SATA HDD 本地盘 | 搭配使用的实例规格族包括大数据型 d3s、d2c、d2s、d1ne 和 d1。 | 适用于互联网行业、金融行业等有大数据计算与存储分析需求的行业，进行海量数据存储和离线计算的业务场景。充分满足以 Hadoop 为代表的分布式计算业务类型对 ECS 实例存储性能、存储容量和内网带宽的多方面要求。 |
## 本地盘性能
有关本地盘的性能说明，请参见[块存储性能](block-storage-performance.md)。
## 计费说明
本地盘的费用包括在本地盘挂载的实例的费用里。更多信息，请参见[包年包月](../subscription.md)和[按量付费](../pay-as-you-go-1.md)。
说明
阿里云提供延期免停权益，即当按量付费的资源发生欠费后，提供一定额度或时长继续使用云服务的权益，延停期间正常计费。具体使用说明和规则，请参见[延期免停权益](https://help.aliyun.com/zh/user-center/exemption-of-suspension-after-delinquency)。
## 磁盘初始化顺序
创建带本地盘的ECS实例时，所有磁盘的初始化顺序遵循以下规则：
规则一：如果指定的镜像不带有数据盘快照，则按照本地盘优先、随ECS实例创建的云盘其次的顺序排列。
规则二：如果指定的镜像带有数据盘快照，由于制作镜像时，会同时记录数据盘设备名，优先保留镜像中的数据盘快照所对应的磁盘顺序，其余排列顺序遵循规则一。
以Linux类型镜像中包含两块数据盘快照的场景为例，为您讲解规则二的排序原理。
假设两块数据盘的原设备名分别是/dev/xvdb和/dev/xvdc：在初始化本地盘实例时，阿里云优先将/dev/xvdb和/dev/xvdc分配给镜像中指定的数据盘使用。则磁盘初始化顺序为系统盘、镜像已指定的数据盘1、镜像已指定的数据盘2、本地盘1、本地盘2、云盘1、云盘2等。如下图所示。
假设两块数据盘的原设备名分别是/dev/xvdc和/dev/xvdd：在初始化本地盘实例时，阿里云优先将/dev/xvdc和/dev/xvdd分配给镜像中指定的数据盘使用。剩下的设备名位置再以本地盘优先的方式填充。则磁盘初始化顺序为系统盘、本地盘1、镜像已指定的数据盘1、镜像已指定的数据盘2、本地盘2、云盘1、云盘2等。如下图所示。
## 生命周期
本地盘的生命周期与它所挂载的本地盘实例相同。更多信息，请参见[实例的生命周期](instance-lifecycle.md)。
## 实例操作对本地盘数据的影响
操作本地盘实例对本地盘数据的影响如下表所示。
| 实例操作 | 保留本地盘数据 | 保留本地盘 |
| --- | --- | --- |
| 操作系统重启/控制台重启/强制重启 | 是 | 是 |
| 操作系统关机/控制台停止/强制停止 | 是 | 是 |
| 实例自动恢复。实例更多的恢复方式请参见 [修改实例维护属性](modify-instance-maintenance-attributes.md) | 否 | 是 |
| [释放实例](release-an-instance.md) | 否 | 否 |
| 包年包月实例到期停机后，实例进入过期回收前 | 是 | 是 |
| 账号欠费后，按量付费实例进入欠费回收前 | 是 | 是 |
| 包年包月实例到期停机后，实例进入过期回收后 | 否 | 是 |
| 账号欠费后，按量付费实例进入欠费回收后 | 否 | 是 |
| 包年包月实例到期停机或账号欠费后，释放实例后 | 否 | 否 |
| 手动续费一台过期的包年包月实例 | 是 | 是 |
| 账号欠费重新充值并重开机一台欠费的按量付费实例 | 是 | 是 |
| 手动续费一台过期回收中的包年包月实例 | 否 | 是 |
| 账号欠费重新充值并重开机一台欠费回收中的按量付费实例 | 否 | 是 |
## 相关文档
您可以根据性能测试文档测试本地盘的带宽、IOPS以及延迟等性能指标，验证阿里云提供的标准性能数据及本地盘服务质量QoS（Quality of Service）。具体操作，请参见[本地盘性能测试命令](test-the-performance-of-block-storage-devices.md)。
如果您使用的是已经停售的上一代本地SSD盘，请参见[上一代磁盘-本地](previous-generation-disks-local-ssds.md)[SSD](previous-generation-disks-local-ssds.md)[盘](previous-generation-disks-local-ssds.md)。
关于如何处理本地盘系统事件，请参见[本地盘实例运维场景和系统事件](operations-and-maintenance-scenarios-and-system-events-for-instances-equipped-with-local-disks.md)。
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
