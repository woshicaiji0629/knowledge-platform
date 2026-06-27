# etcd组件监控指标及大盘使用说明-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/monitor-etcd

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-managed-and-ack-dedicated/product-overview.md)

- [快速入门](products/ack/documents/ack-managed-and-ack-dedicated/getting-started.md)

- [操作指南](products/ack/documents/ack-managed-and-ack-dedicated/user-guide.md)

- [实践教程](products/ack/documents/ack-managed-and-ack-dedicated/use-cases.md)

- [安全合规](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference.md)

- [服务支持](products/ack/documents/ack-managed-and-ack-dedicated/support.md)

[首页](https://help.aliyun.com/zh)

# etcd组件监控指标及大盘使用说明

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Kubernetes集群使用etcd作为持久存储设备，用于保存集群的状态和元数据信息。作为一个分布式键值存储，etcd保证了集群数据的强一致性和高可用性。本文介绍etcd组件的监控指标清单、大盘使用指导以及常见指标异常解析。

## 使用前须知

### 操作入口

请参见[查看集群控制面组件监控大盘](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/view-control-plane-component-dashboards-in-ack-pro-clusters.md)。

### 指标清单

指标是组件对外透出状态和参数的方式之一，etcd组件使用的指标清单如下。

- 

- 

- 

- 

- 

- 

- 

| 指标 | 类型 | 说明 |
| --- | --- | --- |
| cpu_utilization_core | Gauge | CPU 使用量。单位：核（Core）。 |
| etcd_server_has_leader | Gauge | etcd 基于 Raft 实现一致性算法。在 Raft 中，etcd 会将集群中的某个成员（Member）选举为“Leader”，即主节点，而其他成员则作为“Follower”，即从节点。Leader 会定期向所有 Member 发送心跳，以保持集群稳定。 此指标表示 etcd Member 中是否存在 Leader。 1：有主节点。 0：没有主节点。 |
| etcd_server_is_leader | Gauge | etcd Member 是否是 Leader。 1：是。 0：不是。 |
| etcd_server_leader_changes_seen_total | Counter | 过去一段时间内，etcd Member 的切主次数，即 Leader 更换的次数。 |
| etcd_mvcc_db_total_size_in_bytes | Gauge | etcd Member Database（数据库）的总大小。 |
| etcd_mvcc_db_total_size_in_use_in_bytes | Gauge | etcd Member Database 的实际使用大小。 |
| etcd_disk_backend_commit_duration_seconds_bucket | Histogram | etcd 后端 commit 延时，即在 etcd 中，数据变更写入到存储后端并成功提交（commit）所花费的时间。 Bucket 阈值为 [0.001, 0.002, 0.004, 0.008, 0.016, 0.032, 0.064, 0.128, 0.256, 0.512, 1.024, 2.048, 4.096, 8.192] 。 |
| etcd_debugging_mvcc_keys_total | Gauge | etcd 中存储的所有键（Key）的数量 |
| etcd_server_proposals_committed_total | Gauge | etcd 基于 Raft 实现一致性算法。在 Raft 中，任何试图更改系统状态的动作都以提案（Proposal）的形式被提出。 此指标指在 etcd 中，成功提交到 Raft 日志中的 Proposal 数量。 |
| etcd_server_proposals_applied_total | Gauge | 成功应用或执行（Apply）的 Proposal 数量。 |
| etcd_server_proposals_pending | Gauge | 正在等待处理的 Proposal 数量。 |
| etcd_server_proposals_failed_total | Counter | 处理失败的 Proposal 数量。 |
| memory_utilization_byte | Gauge | 内存使用量。单位：字节（Byte）。 |
| resource_utilization_level | Gauge | 资源使用水位。 resource：资源类型，包括 cpu 和 memory。 utilization_level：水位等级，high（使用率 ≥80%）或 normal（使用率 <80%）。 container：目标容器。包括 kube-apiserver、kube-scheduler、kube-controller-manager、cloud-controller-manager 和 etcd。 |


说明

如下资源使用率指标已废弃，请及时去除依赖该指标的告警和监控。

- 

cpu_utilization_ratio：CPU使用率。

- 

memory_utilization_ratio：内存使用率。

请使用resource_utilization_level指标做资源使用水位相关的告警和监控，该指标在灰度开放中。如果内存和CPU资源水位相关看板不可见，请先[升级监控组件](products/arms/documents/prometheus-monitoring/update-monitoring-components.md)再[升级托管探针](products/arms/documents/prometheus-monitoring/update-monitoring-components.md)。

## 大盘使用指导

大盘基于组件指标和相关PromQL绘制，大盘可观测性展示和功能解析如下。

### 可观测性展示

### 功能解析

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

| 名称 | PromQL | 说明 |
| --- | --- | --- |
| etcd 存活状态 | etcd_server_has_leader etcd_server_is_leader == 1 | etcd Member 是否存活。正常值为 3。 etcd Member 是否是主节点。正常情况下，必须有一个 Member 为主节点。 |
| 过去一天切主次数 | changes(etcd_server_leader_changes_seen_total{job="etcd"}[1d]) | 过去一天内 etcd 集群切主次数，即 Leader 更换的次数。 |
| 内存使用量 | memory_utilization_byte{container="etcd"} | 内存使用量。单位：字节。 |
| CPU 使用量 | cpu_utilization_core{container="etcd"}*1000 | CPU 使用量。单位：毫核。 |
| 内存资源水位 | resource_utilization_level{resource="memory",container="etcd",utilization_level="high"} resource_utilization_level{resource="memory",container="etcd",utilization_level="normal"} | 当 resource_utilization_level{utilization_level="high",...} == 1，表明容器资源利用率（水位）>= 80%。 当 resource_utilization_level{utilization_level="normal",...} == 1，表明容器资源利用率（水位）< 80%。 |
| CPU 资源水位 | resource_utilization_level{resource="cpu",container="etcd",utilization_level="high"} resource_utilization_level{resource="cpu",container="etcd",utilization_level="normal"} |  |
| 磁盘大小 | etcd_mvcc_db_total_size_in_bytes | etcd Backend DB 总大小，即 etcd 后端数据库总大小。 |
| etcd_mvcc_db_total_size_in_use_in_bytes | etcd Backend DB 实际使用大小，即 etcd 后端数据库实际使用大小。 |  |
| kv 总数 | etcd_debugging_mvcc_keys_total | etcd 集群 KV 对（键对）总数。 |
| backend commit 延迟 | histogram_quantile(0.99, sum(rate(etcd_disk_backend_commit_duration_seconds_bucket{job="etcd"}[5m])) by (instance, le)) | 后端 Commit 时延，即 Proposal 在 etcd 数据库完成持久化存储所需要的时间。 |
| raft proposal 情况 | rate(etcd_server_proposals_failed_total{job="etcd"}[1m]) | Raft Proposal 提交失败的速率（分钟）。 |
| etcd_server_proposals_pending{job="etcd"} | Pending 的 Raft Proposal 总数。 |  |
| etcd_server_proposals_committed_total{job="etcd"} - etcd_server_proposals_applied_total{job="etcd"} | Raft Proposal 中，Committed 和 Applied 的数量差值，即已提交但尚未执行的 Proposal 数量。 |  |


## 常见指标异常

### etcd存活状态

| 正常情况 | 异常情况 | 异常说明 |
| --- | --- | --- |
| 3 个 etcd Member 都有 Leader，且其中之一必须为 Leader，即 sum(etcd_server_has_leader)=3 ，且仅有一个 member etcd_server_is_leader == 1 。 | 单个 Member 异常。 | 对应的 member etcd_server_has_leader!=1 ，不影响整体 etcd 集群对外提供服务。 |
| 大于 1 个 Member 异常。 | 多个 member etcd_server_has_leader!=1 ，Member 异常大于 1，此时 etcd 集群无法对外提供服务。 同时，请观察是否存在 Member 的 etcd_server_is_leader == 1 。如果没有，etcd 则处于无主状态，无法对外提供服务。 |  |


### Backend Commit时延

| 正常情况 | 异常情况 | 异常说明 |
| --- | --- | --- |
| 指标处于几 ms 到几十 ms。 | 长时间出现几百 ms 甚至秒级别的延迟。 | 磁盘读写存在异常。 |


### Raft Proposal异常

| 正常情况 | 异常情况 | 异常说明 |
| --- | --- | --- |
| Raft Proposal Failed 速率为 0。 | raft proposal failed 大于 0。 | 有 Raft Proposal 提交失败。如果此值较大，需进一步排查。 |
| Pending 的 Raft Proposal 总数为 0。 | Pending 的 Raft Proposal 总数大于 0。 | 提交的 Raft Proposal 有积压，一般是由于 Apply 速度较慢，可结合后端 Commit 时延进行分析。 |
| Raft Proposal 的 Committed 和 Applied 数量差值为 0。 | Committed 和 Applied 数量差值大于 0。 | 客户端请求过多，etcd 压力较大。 若此值大于 5000，etcd 会拒绝接后续的请求，并返回 too many requests ，直至积压的 Proposal 全部处理完毕。 |


## 相关文档

关于其他集群控制面组件监控的指标详情、大盘使用指引和常见指标异常说明，请参见[kube-apiserver](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-kube-apiserver.md)[组件监控指标说明](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-kube-apiserver.md)、[组件监控指标说明](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-kube-scheduler.md)、[组件监控指标说明](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-kube-controller-manager.md)、[cloud-controller-manager](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-cloud-controller-manager.md)[组件监控指标说明](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-cloud-controller-manager.md)。

[上一篇：kube-apiserver组件监控指标说明](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-kube-apiserver.md)[下一篇：kube-scheduler组件监控指标说明](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-kube-scheduler.md)

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
