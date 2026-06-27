# 产品功能特性与能力矩阵-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/product-function-node-kvstore-1

# 功能特性
## 云数据库Tair（兼容 Redis）
| 功能集 | 功能 | 功能描述 | 参考文档 |
| --- | --- | --- | --- |
| 架构 | 主从版本 | 1 个主节点、1 个从节点的标准架构。 | [标准版-双副本](standard-master-replica-instances.md) |
| 读写分离 | 支持开启读写分离功能，1 个主节点、1~9 个只读节点（可随时调整）。 | [读写分离版](read-or-write-splitting-instances-1.md) |  |
| 集群版 | 支持原生 Redis Cluster 架构与代理模式集群架构，分片数量为 2~256 分片，分片规格为 1 GB~64 GB，整体容量可达 2 GB~16 TB。 | [集群版](cluster-master-replica-instances.md) |  |
| 单副本 | 仅单个节点，价格为主从版本的 50%，不支持备份与恢复，不保障数据可靠性，无 SLA 保障，仅适合纯缓存场景。 | [标准版-单副本](https://help.aliyun.com/zh/document_detail/52685.html) |  |
| 规格与架构变更 | 升配 | 升级配置，包括扩大分片容量，增加分片数量。 | [变更实例配置](../user-guide/change-the-configurations-of-an-instance.md) |
| 降配 | 降低配置，包括降低分片容量，减少分片数量。 | [变更实例配置](../user-guide/change-the-configurations-of-an-instance.md) |  |
| 跨架构变配 | 支持在单副本、主从、读写分离、集群架构之间相互变配，且无需修改业务代码。 | [变更实例配置](../user-guide/change-the-configurations-of-an-instance.md) |  |
| 版本兼容性 | 兼容 Redis4.0、5.0、6.0、7.0 | 支持 Redis 4.0、5.0、6.0 与 7.0 版本。 | [Redis](../support/new-features-of-apsaradb-for-redis.md) [大版本新特性与兼容性](../support/new-features-of-apsaradb-for-redis.md) |
| 兼容 Memcache | 兼容 Memcache API。 | [什么是云数据库 Memcache 版](https://help.aliyun.com/zh/memcache/product-overview/product-overview) |  |
| 安全能力 | 支持命令动态屏蔽 | 支持动态禁用高风险命令，且无需重启实例。 | [禁用高风险命令](../user-guide/disable-high-risk-commands.md) |
| 多账号管理 | 支持创建多个账号，并为每个账号设置对应权限。 | [创建与管理账号](../user-guide/create-and-manage-database-accounts.md) |  |
| IP 访问控制 | 支持基于 IP 白名单动态限制访问。 | [设置白名单](../user-guide/configure-whitelists.md) |  |
| 关联安全组 | 支持通过安全组动态限制访问。 | [白名单设置](../getting-started/step-2-configure-whitelists.md) |  |
| 写操作审计 | 支持记录每一条写入请求的时间点、客户端 IP、账号与相关 Key 等信息，可助力数据异常分析。 | [审计日志](../audit-logs.md) |  |
| 支持 TDE | 支持透明数据加密 TDE。 | [支持透明数据加密](../user-guide/enable-tde.md) [TDE](../user-guide/enable-tde.md) |  |
| 支持 IP 白名单模板 | IP 白名单模板可关联多个实例，轻松维护多个实例的 IP 白名单。 | [设置](../user-guide/configure-a-whitelist-template.md) [IP](../user-guide/configure-a-whitelist-template.md) [白名单模板](../user-guide/configure-a-whitelist-template.md) |  |
| 支持 TLS/SSL | 支持 TLS 与 SSL 通讯加密。 | [开启](../user-guide/enable-tls-encryption.md) [TLS/SSL](../user-guide/enable-tls-encryption.md) [加密](../user-guide/enable-tls-encryption.md) |  |
| 实例回收站 | 支持实例回收站。 | [实例回收站](../user-guide/manage-instances-in-the-recycle-bin.md) |  |
| 可观测性 | 多监控项 | 支持 Memory、Stats、CPU、Keyspace 等多种监控项，便于您从多维度观察实例状态。 | [查看性能监控](../user-guide/view-monitoring-data.md) |
| 时延洞察 | 多维度精确展示 Redis 命令与特殊事件的时延统计，提高数据库排查的效率。 | [时延洞察](../user-guide/latency-insights.md) |  |
| 大、热 Key 分析 | 包括离线大 Key 全量分析和实时请求 Key 分析，快速定位大、热 Key。 | [大](../big-keys-and-hotkeys.md) [Key](../big-keys-and-hotkeys.md) [与热](../big-keys-and-hotkeys.md) [Key](../big-keys-and-hotkeys.md) |  |
| 慢日志分析 | 支持慢日志查看及分析，提供优化请求的线索。 | [查询慢日志](../user-guide/view-slow-logs.md) |  |
| 生命周期管理 | 生命周期管理 | 支持创建、释放、退订、付费模式转换、升级版本、重启实例等操作。 | [管理生命周期](../lifecycle-management.md) |
| 备份与恢复 | 支持手动备份 | 支持手动备份，一天最多允许保留 15 份备份数据。 | [手动备份](../user-guide/automatic-or-manual-backup.md) |
| 支持自动备份 | 根据设置的备份策略自动进行备份。 | [自动备份](../user-guide/automatic-or-manual-backup.md) |  |
| 支持全量恢复 | 通过备份数据恢复至一个新的实例。 | [从备份集恢复至新实例](../user-guide/restore-data-from-a-backup-set-to-a-new-instance.md) |  |
| 支持数据闪回 | 支持将实例整体或指定 Key 的数据恢复至某个秒级的时间点。 | [通过数据闪回按时间点恢复数据](../user-guide/use-data-flashback-to-restore-data-by-point-in-time.md) |  |
| 高可用 | 自动和手动执行主备切换 | 支持自动 HA 实现故障转移，支持手动执行主备切换（即切换节点角色），便于您进行实时容灾演练。 | [手动执行主备切换](../user-guide/manually-switch-workloads-from-a-master-node-to-a-replica-node.md) |
| 重启或重搭代理节点 | 支持手动重启或重新搭建代理节点，便于您进行实时容灾演练，也可以在服务异常、延迟较高时发起主动运维。 | [重启或重搭代理节点](../user-guide/restart-or-rebuild-a-proxy-node.md) |  |
| 连接管理 | 修改专有网络/交换机 | 支持修改专有网络或交换机。 | [修改专有网络](../user-guide/change-the-vpc-or-vswitch-of-an-instance.md) [VPC](../user-guide/change-the-vpc-or-vswitch-of-an-instance.md) [或交换机](../user-guide/change-the-vpc-or-vswitch-of-an-instance.md) |
| 申请/释放公网连接地址 | 默认情况下，云数据库 Redis 版仅提供专有网络连接地址，如需从本地通过公网连接 Redis 实例，可以申请 Redis 实例的公网连接地址。 | [申请公网连接地址](../user-guide/apply-for-a-public-endpoint-for-an-apsaradb-for-redis-instance.md) |  |
| 开通/释放直连地址 | 支持开通直连访问模式，兼容原生 Redis Cluster 协议。 | [开通直连访问](../user-guide/enable-the-direct-connection-mode.md) |  |
| 弹性能力 | 手动/自动开启带宽包 | 支持在不调整实例规格的情况下手动或动态增加实例的带宽，轻松应对流量高峰。 | [开启带宽弹性伸缩](../user-guide/enable-bandwidth-auto-scaling.md) |
| 开启/关闭自动扩容 | 当内存平均使用率达到阈值后会自动升级 Redis 实例的规格，帮助您快速弹性适配业务高峰，规避内存溢出的风险。 | [开启自动扩容](../user-guide/enable-automatic-scale-up.md) |  |
| 无感扩缩容 | 实例扩容过程可实现客户端无感知、不闪断、无只读状态，满足随时弹性资源伸缩需求。 | [Tair](imperceptible-scaling.md) [集群无感扩缩容介绍](imperceptible-scaling.md) |  |
| 性能优化 | 代理查询缓存 | 支持代理查询缓存（Proxy Query Cache）功能，启用后，代理节点会缓存热点 Key 对应的请求和查询结果。 | [通过](../user-guide/use-read-write-splitting-to-mitigate-issues-caused-by-hotkeys.md) [Proxy Query Cache](../user-guide/use-read-write-splitting-to-mitigate-issues-caused-by-hotkeys.md) [优化热点](../user-guide/use-read-write-splitting-to-mitigate-issues-caused-by-hotkeys.md) [Key](../user-guide/use-read-write-splitting-to-mitigate-issues-caused-by-hotkeys.md) [问题](../user-guide/use-read-write-splitting-to-mitigate-issues-caused-by-hotkeys.md) |
| 日志管理 | 审计日志 | 支持开通、查询、下载审计日志。 | [审计日志](../audit-logs.md) |
| 查询慢日志 | 支持查询数据节点、代理节点慢日志。 | [查询慢日志](../user-guide/view-slow-logs.md) |  |
| 查询运行日志 | 支持查询实例的运行日志。 | [查询运行日志](../user-guide/view-active-logs.md) |  |
| 事件管理 | 修改运维事件计划时间 | 支持在可运维时间执行运维计划，支持修改可运维时间点。 | [修改运维事件计划切换时间](../developer-reference/api-r-kvstore-2015-01-01-modifyactiveoperationtasks-redis.md) |
| 查询运维事件进度 | 支持查询运维任务的进度。 | [查询运维事件进度](../developer-reference/api-r-kvstore-2015-01-01-describeactiveoperationtasks-redis.md) |  |
| 参数管理 | 设置实例参数 | 支持设置实例参数。 | [设置参数](../user-guide/modify-the-values-of-parameters-for-an-instance.md) |
| 查看参数列表 | 支持查看参数列表。 | [查看参数列表](../user-guide/supported-parameters.md) |  |
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
