# 读写分离实例的架构图,使用场景-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/product-overview/read-or-write-splitting-instances-1

# 读写分离功能
针对超高读写比的业务场景，云数据库 Tair（兼容 Redis）支持动态开启或关闭读写分离功能，提供高可用、高性能、灵活的读写分离服务，满足热点数据集中及高并发读取的业务需求。读写分离实例由阿里云Tair团队自研的Proxy组件进行全自动智能识别读写请求及路由、故障切换等服务。您无需处理与读写分离相关的业务代码，也无需考虑故障切换的业务层处理，本功能将显著降低接入复杂度。
## 标准架构开启读写分离
标准架构开启读写分离功能的实例主要由主节点、只读节点、代理节点（Proxy）和高可用系统等组成，架构图如下。
图 1.云原生版
图 2.经典版（已停售）
| 组件 | 云原生版读写分离实例 | 经典版读写分离实例（已停售） |
| --- | --- | --- |
| 主节点（Master node） | 承担写请求的处理，同时和只读节点共同承担读请求的处理。 |  |
| 只读节点（Read replicas） | 承担读请求的处理，特点如下： 所有只读节点均具备容灾功能，可作为备节点进行数据备份。 只读节点均从主节点同步数据，为星型复制架构，数据同步延迟远小于 经典 版链式复制架构。 支持自定义只读节点数量，集群架构每分片 1 ~ 4 个，标准架构 1 ~ 9 个。 | 承担读请求的处理，特点如下： 只读节点采取链式复制架构，当只读节点数越多，靠近链路末端的只读节点数据延迟越大。 提供 1 个、3 个、5 个只读节点配置。 |
| 备节点（Replica node） | 任一只读节点均可作为备节点。当主节点发生异常时，高可用系统将选择数据最完整的只读节点作为新的主节点，并在切换完成后立即补充一个新的只读节点。 由于无需该组件，在同样性能下，云原生读写分离实例的价格更低。 | 冷备节点，作为数据备份使用，不对外提供服务。当主节点发生异常时，会将请求切换至该节点。 |
| 代理服务器（Proxy Server） | 客户端和代理服务器建立连接后，代理服务器会自动识别客户端发起的请求类型，按照权重分发流量（各节点权重相同，且不支持自定义权重），将请求转发到不同的数据节点中。例如将写请求转发给主节点，将读请求转发给主节点和只读节点。 说明 客户端只会与代理服务器建立连接，不支持和各节点直接建立连接。 代理服务器会将读请求平均分配到主节点和只读节点，暂不支持自定义控制。例如 3 个只读节点的实例，主节点和 3 个只读节点的读权重均为 25%。 |  |
| 高可用系统（HA system） | 自动监控各节点的健康状态：当各节点异常时，高可用系统将发起主备切换或重建只读节点，并更新相应的路由及权重信息。 故障时选主节点逻辑：数据优先，高可用系统将选取数据最完整的只读节点作为新的主节点。 |  |
关于双可用区读写分离实例的说明
| 云原生读写分离实例（推荐） | 经典读写分离实例（已停售） |
| --- | --- |
| 主、备可用区都提供服务，最小配置： 主可用区：1 个主节点、1 个只读节点。 备可用区：1 个只读节点。 将分别提供主、备可用区的连接地址，均支持读、写操作。主可用区的读请求仅会路由至主可用区的主节点或只读节点，备可用区的读请求也仅会路由至备可用区的只读节点，实现就近访问；而所有的写请求均会路由到主可用区的主节点中。架构图如下： 说明 推荐主、备可用区均配置 2 节点以上： 主可用区：1 个主节点、1 个只读节点。 备可用区：2 个只读节点。 | 主节点与只读节点都部署在主可用区，仅将冷备节点部署在备可用区，作为数据备份，不对外提供服务。当主节点发生异常时，会将请求切换至该节点。 |
特点：
动态开关、简单易用
标准架构能够直接开启读写分离功能。由于客户端请求的读写类型是通过Proxy智能识别与转发，在开启该功能后，您可以直接使用任何支持Redis的客户端访问读写分离实例，从而实现读性能的提升，且无需进行业务改造。读写分离实例兼容Redis协议命令，但存在代理节点的命令限制，更多信息请参见[读写分离实例的命令限制](../developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。
高可用
通过阿里云自研的高可用系统自动监控所有数据节点的健康状态，为整个实例的可用性保驾护航。主节点不可用时自动选择新的主节点并重新搭建复制拓扑。某个只读节点异常时，高可用系统能够自动探知并重新启动新节点完成数据同步，下线异常节点。
代理节点会实时感知每个只读节点的服务状态。在某个只读实例异常期间，代理节点会自动降低该节点的服务权重，发现只读节点连续失败超过一定次数以后，会停止异常节点的服务权利，并具备继续监控后续重新启动节点服务的能力。
高性能
读写分离实例可以通过扩展只读实例个数使整体实例性能呈线性增长，同时基于源码层面对Redis复制流程的定制优化，可以最大程度地提升线性复制的系统稳定性，充分利用每一个只读节点的物理资源。
使用场景：
读取请求QPS（Queries Per Second）压力较大的场景。如果业务为读多写少的场景，标准架构可能无法满足较高的QPS需求。在这种情况下，您可以通过部署多个只读节点来突破单节点的性能瓶颈。开启读写分离后实例可承载的读QPS最高提升9倍。
说明
由于Redis异步同步机制，在写入量较大的情况下可能会发生数据同步延迟。选用此架构时，业务需要能接受一定程度的脏数据。
## 集群架构开启读写分离
集群架构中，仅云原生版、代理模式支持开启读写分离功能，服务架构示例如下。
组件说明：
| 组件 | 说明 |
| --- | --- |
| 代理服务器（Proxy Server） | 当客户端与代理服务器（Proxy Server）建立连接后，Proxy 会自动识别客户端发起的请求，将请求转发到各数据分片以及对应的读写节点上。例如将写请求转发给主节点，将读请求均衡地转发给主节点和只读节点。 |
| 数据分片（Data Shards） | 每个数据分片由 1 个主节点（Master）、最多 4 个只读节点（Read Replicas）组成。 主节点：承担写请求的处理，同时和只读节点共同承担读请求的处理。固定部署在主可用区。 只读节点：承担读请求的处理，只读节点均从主节点同步数据（星型复制架构）。只读节点的数量范围为 1 ~ 4，并且支持动态调整。您也可以选择部署只读节点在备可用区，所以只读节点均具备容灾功能。 |
| 高可用服务（HA） | 自动监控各节点的健康状态：当各节点异常时，高可用系统将发起主备切换或重建只读节点，并更新相应的路由及权重信息。 故障时选主节点逻辑：数据优先，高可用系统将选取数据最完整的只读节点作为新的主节点。 |
说明
若实例为单可用区，则所有节点均在主可用区，实例仅提供主可用区的连接地址。
若实例为双可用区，则实例将分别提供主、备可用区的连接地址，均支持读、写操作。主可用区的读请求会路由至主可用区的主节点或只读节点中，备可用区的读请求也仅会路由至备可用区的只读节点，实现就近访问。而所有的写请求均会路由到主可用区的主节点中。若发生极端情况，备可用区的所有只读节点都不可用，备可用区的读请求也会路由到主节点中，不会影响业务运行。
## 建议与使用须知
当一个只读节点发生故障时，请求会转发到其他节点；如果所有只读节点均不可用，请求会全部转发到主节点。只读节点异常可能导致主节点负载提高、响应时间变长，因此在读负载高的业务场景建议使用多个只读节点。
只读节点发生异常时，高可用系统会暂停异常节点的服务，重新挂载一个可用的只读节点。该过程涉及资源分配、实例创建数据同步以及服务加载，消耗的时间与业务负载及数据量有关。云数据库 Tair（兼容 Redis）不承诺只读节点的恢复时间指标。
由于多可用区读写分离的最低要求是主可用区必须具备1个主节点和1个只读节点，当为多可用区标准架构（主可用区1个主节点、备可用区1个备节点）实例开启读写分离时，请您先为主可用区增加1个备节点，确保主可用区有2个节点，再开启读写分离。
某些场景会触发只读节点的全量同步，例如在主节点触发高可用切换后。全量同步期间只读节点不提供服务并返回-LOADING Redis is loading the dataset in memory\r\n信息。
部分读命令在读写分离架构中有特殊的转发规则。例如SCAN命令会被转发至主节点执行，HSCAN、SSCAN、ZSCAN命令会通过Slot取模计算将请求均匀分配至主节点和只读节点。关于完整的转发规则，请参见[Proxy](features-of-proxy-nodes.md)[的路由转发规则](features-of-proxy-nodes.md)。
## 前提条件
部署模式为云原生。
实例为Redis开源版或Tair（企业版）内存型、持久内存型。
实例规格为1 GB及以上。
实例类型为高可用。
## 操作指南
若未创建实例，可以在[创建实例](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md)时选择开启读写分离。
若您已创建云原生版实例，可直接[开启读写分离](../user-guide/enable-read-write-splitting.md)。
## 常见问题
Q：标准架构开启读写分离后能提升实例整体带宽吗？
A：可以。开启读写分离后，实例的整体带宽理论上可达实例规格的带宽 * 总节点数（例如96 MB/s * 3节点 = 288 MB/s ）。同时，新增的代理节点会将大部分读请求转发到只读节点上，降低主节点的带宽压力。然而，实际带宽受业务请求和客户端等因素的影响，实际带宽以压测结果为准。
Q：标准架构开启读写分离后还能变配至集群架构吗？
A：可以，请先[关闭读写分离](../user-guide/enable-read-write-splitting.md)，再[变配](../user-guide/change-the-configurations-of-an-instance.md)实例架构。
Q：如何确认读写分离是否已启用？
A：您可以访问实例的节点管理页面，查看读写分离选项是否已启用。
Q：为什么只读节点没有收到读请求？
A：在双可用区读写分离架构中，主、备可用区均有独立的连接地址，且读请求仅会路由至本可用区的主节点或只读节点。若您仅使用主可用区连接地址，所有读请求都不会被路由至备可用区的只读节点。因此，需要在业务代码中主动区分主、备可用区连接地址，并将备可用区的请求指向备可用区连接地址，以实现就近访问和负载均衡。
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
