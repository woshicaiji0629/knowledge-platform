# 云原生与经典实例差异与选型-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/comparison-between-tair-instances-that-cloud-native-and-classic

# 云原生实例和经典实例对比
在购买Tair实例时，推荐您选择云原生版实例。本文列出云原生版与经典版实例的主要区别，为您提供选型参考。
## 特性对比
| 对比项 | 云原生实例（推荐） | 经典实例 |
| --- | --- | --- |
| 架构与扩容 | 基于新一代管控架构，更灵活、扩容能力更强。支持在原本地资源充足的情况下快速扩容（无需迁移至新实例），扩容速度更快，对业务影响更小。更多信息请参见 [变更实例配置](../user-guide/change-the-configurations-of-an-instance.md) 。 | 基于传统管控架构。集群架构实例为预设固定规格，不支持自定义。扩容耗时较长。 |
| [标准架构](standard-master-replica-instances.md) | 标准架构支持创建多副本实例，最多可创建 1 主节点、9 个备节点。 | 最多仅支持一个备节点。 |
| [集群架构](cluster-master-replica-instances.md) | 扩容时能够有效消除原生 Redis 集群可能会产生的 -ASK 、 -TRYAGAIN 错误，实现无感扩缩容。 集群架构实例支持自由调整 2~256 个分片节点数量（支持最小粒度为 1 个分片），同时支持调整分片节点的规格，能够更好地应对不同性能、容量的需求场景。 集群架构支持创建多副本实例，每个分片节点最多可创建 1 主节点、4 个备节点。 | 扩容时会闪断。 集群架构实例的分片节点的扩展数固定，例如 2 分片、4 分片、8 分片等。 |
| [读写分离功能](read-or-write-splitting-instances-1.md) | 标准版（读写分离）实例支持自由调整 1~9 个只读节点数量。 在多可用区开启读写分离时支持就近访问。 集群架构（代理模式）支持开启读写分离模式，每个分片节点最多可以创建 1 主节点、4 个只读节点。 | 读写分离架构（已停售）的只读节点固定为 1、3、5 个。 |
| 容灾能力 | 若实例为多可用区部署，支持在主可用区内进行 HA 切换。可避免因 HA 切换到备可用区而导致的业务访问时延增加的问题，更多信息请参见 [通过自定义节点数规避跨可用区切换](../use-cases/prevent-cross-zone-switchover-by-specifying-the-number-of-nodes.md) 。 | 多可用区实例仅能 HA 切换到备可用区，之后再 [手动切换](../user-guide/manually-switch-workloads-from-a-master-node-to-a-replica-node.md) 至主可用区。 |
## 功能支持度对比
云原生版实例为云原生基础架构，其中云原生版集群架构支持无感扩缩容，未来Tair会以该架构为主要演进方向。
详细的功能支持度对比如下表所示，为便于阅读，约定✔️表示支持该功能，❌表示不支持该功能，➖表示无此概念。
## 仅查看不同功能点
| 类别 | 功能 | 云原生实例 | 经典实例 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 标准架构 | 集群架构 | 读写分离架构 | 标准架构 | 集群架构 | 读写分离架构 |  |  |
| 变更实例配置 | [快速扩容](../user-guide/change-the-instance-specification.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ | ❌ |
| [集群无感扩缩容](imperceptible-scaling.md) | ➖ | ✔️ | ➖ | ➖ | ❌ | ➖ |  |
| [自定义分片数](../user-guide/adjust-the-number-of-cluster-shards.md) | ➖ | ✔️ | ➖ | ➖ | ❌ | ➖ |  |
| [增删备节点](../user-guide/node-management.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ | ❌ |  |
| [自定义读写分离只读节点数量](../user-guide/enable-read-write-splitting.md) | ➖ | ➖ | ✔️ | ➖ | ➖ | ❌ |  |
| [多可用区就近访问](read-or-write-splitting-instances-1.md) | ➖ | ➖ | ✔️ | ➖ | ➖ | ❌ |  |
| 备份与恢复 | [手动备份支持自定义备份策略](../user-guide/automatic-or-manual-backup.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ | ❌ |
| [删除手动备份](../user-guide/automatic-or-manual-backup.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ | ❌ |  |
| 扩展功能 | [半同步模式](../user-guide/modify-the-synchronization-mode-of-a-persistent-memory-optimized-instance.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ | ❌ |
## 查看所有功能点
| 类别 | 功能 | 云原生实例 | 经典实例 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 标准架构 | 集群架构 | 读写分离架构 | 标准架构 | 集群架构 | 读写分离架构 |  |  |
| 管理生命周期 | [重启实例](../user-guide/restart-one-or-more-apsaradb-for-redis-instances.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [转包年包月](change-the-billing-method-to-subscription.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [转按量付费](change-the-billing-method-to-pay-as-you-go.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [续费实例](renewal.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [升级大版本](../user-guide/upgrade-the-major-version-1.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [升级小版本与代理版本](../user-guide/update-the-minor-version.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [释放按量付费实例](../user-guide/release-pay-as-you-go-instances.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [退订包年包月实例](../user-guide/unsubscribe-from-subscription-instances.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [实例回收站](../user-guide/manage-instances-in-the-recycle-bin.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| 变更实例配置 | [变更实例配置](../user-guide/change-the-configurations-of-an-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [快速扩容](../user-guide/change-the-instance-specification.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ | ❌ |  |
| [集群无感扩缩容](imperceptible-scaling.md) | ➖ | ✔️ | ➖ | ➖ | ❌ | ➖ |  |
| [自定义分片数](../user-guide/adjust-the-number-of-cluster-shards.md) | ➖ | ✔️ | ➖ | ➖ | ❌ | ➖ |  |
| [增删备节点](../user-guide/node-management.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ | ❌ |  |
| [自定义读写分离只读节点数量](../user-guide/enable-read-write-splitting.md) | ➖ | ➖ | ✔️ | ➖ | ➖ | ❌ |  |
| [读写分离架构多可用区就近访问](read-or-write-splitting-instances-1.md) | ➖ | ➖ | ✔️ | ➖ | ➖ | ❌ |  |
| 管理网络连接 | [变更专有网络](../user-guide/change-the-vpc-or-vswitch-of-an-instance.md) [VPC](../user-guide/change-the-vpc-or-vswitch-of-an-instance.md) [或交换机](../user-guide/change-the-vpc-or-vswitch-of-an-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [申请公网连接地址](../user-guide/apply-for-a-public-endpoint-for-an-apsaradb-for-redis-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [集群架构支持直连访问模式](../user-guide/enable-the-direct-connection-mode.md) | ➖ | ✔️ | ➖ | ➖ | ✔️ | ➖ |  |
| [修改连接地址或端口](../user-guide/change-the-endpoint-or-port-number-of-an-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| 管理带宽 | [开启带宽弹性伸缩](../user-guide/enable-bandwidth-auto-scaling.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [手动增加实例带宽](../user-guide/adjust-the-bandwidth-of-an-apsaradb-for-redis-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| 管理高可用 | [手动执行主备切换](../user-guide/manually-switch-workloads-from-a-master-node-to-a-replica-node.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [重启或重搭代理节点](../user-guide/restart-or-rebuild-a-proxy-node.md) | ➖ | ✔️ | ✔️ | ➖ | ✔️ | ✔️ |  |
| [升级代理节点](../user-guide/upgrade-proxy-nodes.md) | ➖ | ✔️ | ✔️ | ➖ | ✔️ | ✔️ |  |
| 管理参数 | [设置参数](../user-guide/modify-the-values-of-parameters-for-an-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| 管理标签 | [管理标签](../create-tags.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| 其他管理功能 | [设置可维护时段](../user-guide/set-a-maintenance-window.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [更换实例所属的可用区](../user-guide/migrate-an-instance-across-zones.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [导出实例列表](../user-guide/export-the-instance-list.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| 账号与安全 | [创建与管理账号](../user-guide/create-and-manage-database-accounts.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [修改或重置密码](../user-guide/change-or-reset-the-password.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [设置](../getting-started/step-2-configure-whitelists.md) [IP](../getting-started/step-2-configure-whitelists.md) [白名单](../getting-started/step-2-configure-whitelists.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [设置](../user-guide/configure-a-whitelist-template.md) [IP](../user-guide/configure-a-whitelist-template.md) [白名单模板](../user-guide/configure-a-whitelist-template.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [开启](../user-guide/enable-tls-encryption.md) [TLS](../user-guide/enable-tls-encryption.md) [加密](../user-guide/enable-tls-encryption.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [开启专有网络免密访问](../user-guide/enable-password-free-access.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [开启实例释放保护](../user-guide/enable-the-release-protection-feature.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| 性能与监控 | [查看监控数据](../user-guide/view-monitoring-data.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [报警设置](../user-guide/alert-settings.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [性能趋势](../user-guide/performance-trends.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [实时性能](../user-guide/view-performance-metrics-in-real-time.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [实例会话](../user-guide/instance-sessions.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [慢请求](../user-guide/slow-queries.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [时延洞察](../user-guide/latency-insights.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [离线全量](../user-guide/offline-key-analysis.md) [Key](../user-guide/offline-key-analysis.md) [分析](../user-guide/offline-key-analysis.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [Top Key](../user-guide/use-the-real-time-key-statistics-feature.md) [统计](../user-guide/use-the-real-time-key-statistics-feature.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [诊断实例](../user-guide/create-a-diagnostic-report.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| 审计与日志 | [审计日志](../user-guide/enable-the-new-audit-log-feature.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [查询慢日志](../user-guide/view-slow-logs.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [查询运行日志](../user-guide/view-active-logs.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| 备份与恢复 | [自动或手动备份](../user-guide/automatic-or-manual-backup.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [手动备份支持自定义备份策略](../user-guide/automatic-or-manual-backup.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ | ❌ |  |
| [删除手动备份](../user-guide/automatic-or-manual-backup.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ | ❌ |  |
| [下载备份集](../user-guide/download-a-backup-file.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [按时间点恢复](../user-guide/use-data-flashback-to-restore-data-by-point-in-time.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [从备份集恢复至新实例](../user-guide/restore-data-from-a-backup-set-to-a-new-instance.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️️️️ | ✔️ |  |
| 扩展功能 | [全球多活](../user-guide/overview-of-global-distributed-cache-for-tair.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| [半同步模式](../user-guide/modify-the-synchronization-mode-of-a-persistent-memory-optimized-instance.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ | ❌ |  |
| 代理查询缓存 | ➖ | ✔️ | ✔️ | ➖ | ✔️ | ✔️ |  |
| [Tair](../developer-reference/extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md) [扩展数据结构概览](../developer-reference/extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [多线程](dram-based-instances.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
## 产品支持度
| 实例及其创建方法 | 支持的实例类型 | 支持的引擎版本 | 支持的架构 |
| --- | --- | --- | --- |
| 云原生 版实例 [步骤](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md) [1：创建实例](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md) | Redis 开源版 | 7.0 6.0 5.0 | 标准架构 集群架构 读写分离架构 |
| Redis [倚天版](cost-efficient-instances.md) | 7.0 6.0 5.0 | 标准架构 |  |
| Tair（企业版） [内存型](dram-based-instances.md) | 兼容 Redis 7.0 兼容 Redis 6.0 兼容 Redis 5.0 | 标准架构 集群架构 读写分离架构 |  |
| Tair（企业版） [持久内存型](persistent-memory-optimized-instances-1.md) | 兼容 Redis 6.0 | 标准架构 集群架构 读写分离架构 |  |
| Tair（企业版） [磁盘型](essd-based-instances-1.md) | 兼容 Redis 6.0 | 标准架构 集群架构 |  |
| 经典 版实例 [步骤](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md) [1：创建实例](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md) | Redis 开源版 | 5.0 | 集群架构 标准架构 读写分离架构 |
| Tair（企业版） [内存型](dram-based-instances.md) | 5.0 | 集群架构 标准架构 读写分离架构 |  |
## 常见问题
Q：如何将经典版实例转为云原生版实例？
A：在控制台的实例详情页中，单击转云原生，更多信息请参见[转为云原生部署模式](../user-guide/change-to-the-cloud-native-deployment-mode.md)。
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
