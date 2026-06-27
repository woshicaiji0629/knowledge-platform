# 查看云盘监控信息-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/view-the-monitoring-data-of-a-disk

# 查看云盘监控信息
本文将指导您如何查看ECS实例的云盘监控信息，以帮助您有效确保系统性能和稳定性。
## 背景信息
衡量云盘性能的主要指标含义如下：
IOPS：指Input/Output Operations per Second，即每秒能处理的I/O个数，用于表示块存储处理读写（输出/输入）的能力。如果要部署事务密集型应用，需要关注IOPS性能。
吞吐量：是指单位时间内可以成功传输的数据数量，单位为MBps（即MB/s）。如果要部署大量顺序读写的应用，需要关注吞吐量。
延迟：是指块存储处理一个I/O需要的时间，单位为s、ms或者μs。过高的时延会导致应用性能下降或报错。
云盘的使用率：是指云盘当前已使用的容量占此块云盘容量的比例。它是衡量云盘资源使用情况的重要指标，以百分比表示。过高的使用率可能会导致应用性能下降或报错。
inode使用率：inode是Linux文件系统中用于管理文件元数据（如文件名、时间戳等）的数据结构，其使用率表示已使用的inode数量占总inode数量的比例，如果inode耗尽，即使云盘空间未满，也无法创建新文件。
Burst IO：针对ESSD AutoPL云盘，如果开启（默认开启）并发生了性能突发，则会收取突发性能费用，费用与每小时的Burst IO总量有关，计算详情请参见[性能突发费用封顶规则](essd-autopl-disks.md)。
关于不同类型的云盘的性能，请参见[块存储性能](block-storage-performance.md)。
## 查看云盘的IOPS、吞吐量以及延迟指标
## 分钟级监控
您可以通过ECS控制台查看单块云盘分钟级的IOPS、吞吐量和延迟等监控信息。
访问[ECS](https://ecs.console.aliyun.com/disk/)[控制台-块存储-云盘](https://ecs.console.aliyun.com/disk/)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
找到目标云盘，单击云盘ID，进入云盘基本信息页面。
单击监控页签。
在自定义时间区域，单击图标，设置监控信息的起止时间。
鼠标悬浮至图表中的时间节点可以查看单个指标的信息。
## 秒级监控
相较于ECS为单块云盘提供的分钟级数据监控，[块存储数据洞察](what-is-a-piece-of-data-is-stored-insight.md)（CloudLens for EBS）针对云盘性能提供了秒级数据监控能力，您可以通过块存储控制台的[云盘分析](cloud-disk-analysis.md)监控到更细粒度的云盘性能变化。
说明
首次使用块存储数据洞察时，需要根据页面提示[开通](cloud-disk-analysis.md)[CloudLens for EBS](cloud-disk-analysis.md)。
登录[块存储](https://ebs.console.aliyun.com/home)[EBS](https://ebs.console.aliyun.com/home)[控制台](https://ebs.console.aliyun.com/home)。
说明
首次登录EBS控制台时，请根据页面提示创建一个EBS服务关联角色。更多信息，请参见[块存储](service-linked-role-for-ebs.md)[EBS](service-linked-role-for-ebs.md)[服务关联角色](service-linked-role-for-ebs.md)。
在左侧导航栏，选择数据洞察(EBS Lens)>云盘分析。
在顶部菜单栏左上角处，选择地域。
在云盘分析页面，找到待查看监控数据的云盘，在操作列单击监控。
在秒级监控页面，在查询时间范围内查看目标云盘的监控数据。
说明
秒级监控数据会有1分钟到5分钟的延迟。因此在查询时，最近1分钟到5分钟的数据有可能是零，表示数据值还没有获取到。
指标说明
| 数据指标 | 说明 |
| --- | --- |
| 吞吐量 | 当前云盘在查询时间内成功传输的数据数量统计，单位为 MBps。如果要部署大量顺序读写的应用，需要关注吞吐量。 如果是 ESSD AutoPL 云盘，秒级监控会展示云盘吞吐量的基准值和预配置值指标。关于 ESSD AutoPL 云盘的更多信息，请参见 [ESSD AutoPL](essd-autopl-disks.md) [云盘](essd-autopl-disks.md) 。 |
| IOPS | 当前云盘在单位时间内处理的 I/O 个数统计，用于表示块存储处理读写（输出/输入）的能力，单位为次/秒。如果要部署事务密集型应用，需要关注 IOPS 性能。 如果是 ESSD AutoPL 云盘，秒级监控会展示云盘 IOPS 的基准值和预配置值指标。ESSD AutoPL 云盘的更多信息，请参见 [ESSD AutoPL](essd-autopl-disks.md) [云盘](essd-autopl-disks.md) 。 |
| IO 平均大小读/写 | 当前云盘进行读/写操作读取的数据量大小，单位为 Bytes。IO 大小影响着存储系统的吞吐量和效率。一些系统可能优化了大块数据的传输，而另一些则可能对小块数据的操作有更好的性能。根据应用的不同，理解和优化 IO 大小可以提高整体的系统性能。 |
| BPS 水位线 | 当前云盘的吞吐量占云盘吞吐量上限的比例。当这个比例接近 100%时，表示云盘正在以接近其最大能力进行数据传输，进一步增加负载可能会导致性能瓶颈，影响应用响应速度。因此，监控这个比例可以帮助您及时调整云盘配置或优化应用程序，以避免潜在的性能问题。 |
| IOPS 水位线 | 当前云盘的 IOPS 占云盘 IOPS 上限的比例。当这个比例接近 100%时，表示云盘在处理并发请求方面接近其极限，可能导致延迟增加或请求失败。因此，监控这个比例可以帮助您判断云盘是否能满足应用的实时性能需求，并据此做出调整，以保持应用运行的高效稳定。 |
指标值说明
秒级监控支持查询最近5分钟、15分钟、1小时、6小时、1天内的监控数据，各项数据指标值均为云盘5秒内监控数据的最大值。
时间范围为5分钟、15分钟
仅支持查询云盘监控数据的最大值，数据指标窗口展示的最小粒度是5秒。
时间范围为1小时、6小时、1天
支持查询云盘监控数据的最大值、最小值、平均值及总和，不同时间范围数据指标窗口展示的最小粒度不同。例如您查询的是近1小时内的监控数据，数据指标窗口展示的最小粒度是10秒。
最大值：表示1小时内每10秒指标值（2个指标值）中的最大值。
最小值：表示1小时内每10秒指标值（2个指标值）中的最小值。
平均值：表示1小时内每10秒指标值（2个指标值）的平均值。
总和：表示1小时内每10秒指标值（2个指标值）的累加值。
## 查看云盘的使用率、读写字节数、读写请求数及Inode使用率指标
说明
请确保您已在ECS实例上[安装云监控插件](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/install-and-uninstall-the-cloudmonitor-agent-for-cpp#task-1950491)。
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
进入目标云盘所在的实例详情页面。
选择监控>操作系统监控。
在磁盘监控指标中查看指标信息。
说明
操作系统监控指标的数据采集频率为15秒/次。更多指标解释，请参见[操作系统监控](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/operating-system-monitoring#concept-gdq-tgc-5db)。
（可选）如果您想为云盘设置报警规则，请参见[监控主机](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/monitoring-host#task-1962984)。
说明
您可以根据业务实际场景设置对应的报警规则。如果云盘的监控指标达到报警条件，云监控自动发送报警通知，帮助您及时得知异常监控数据，并快速处理。
## 查看ESSD AutoPL云盘的Burst IO
## 通过EBS控制台
说明
首次使用块存储数据洞察时，需要根据页面提示[开通](cloud-disk-analysis.md)[CloudLens for EBS](cloud-disk-analysis.md)。
登录[块存储](https://ebs.console.aliyun.com/home)[EBS](https://ebs.console.aliyun.com/home)[控制台](https://ebs.console.aliyun.com/home)。
说明
首次登录EBS控制台时，请根据页面提示创建一个EBS服务关联角色。更多信息，请参见[块存储](service-linked-role-for-ebs.md)[EBS](service-linked-role-for-ebs.md)[服务关联角色](service-linked-role-for-ebs.md)。
在左侧导航栏，选择数据洞察(EBS Lens)>云盘分析。
在顶部菜单栏左上角处，选择地域。
在云盘分析页面，找到待查看的ESSD AutoPL云盘，在操作列单击监控。
在左侧导航栏单击AutoPL Burst IO页签。
在AutoPL Burst IO页面，查看ESSD AutoPL云盘的突发详情，包括Burst时间、Burst数量等。
说明
Burst事件查询、Burst详细查询的延迟时间小于1小时，即最新数据为1小时之前的数据。
## 通过ECS控制台
您可以通过ECS控制台查看在特定时间内ESSD AutoPL云盘的突发IO数量。
访问[ECS](https://ecs.console.aliyun.com/disk/)[控制台-块存储-云盘](https://ecs.console.aliyun.com/disk/)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
找到目标云盘，单击云盘ID，进入云盘基本信息页面。
单击监控页签。
在EBS数据洞察的自定义时间区域，单击图标，设置监控信息的起止时间。
说明
支持设置的起止时间间隔不超过6小时。
鼠标悬浮至图表中的时间节点可以查看突发IO数量。
## 相关文档
您也可以通过API接口[DescribeDiskMonitorData](../api-describediskmonitordata.md)查询指定时间内云盘的读写IOPS、读写带宽、读写时延等。
如果您的应用程序或工作负载的性能需求发生了变化，或出现云盘存储容量不足等情况，您可以[变更云盘类型](change-the-category-of-a-disk.md)或[扩容云盘容量](overview-19.md)来满足当前的业务需求，以提供更好的性能。
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
