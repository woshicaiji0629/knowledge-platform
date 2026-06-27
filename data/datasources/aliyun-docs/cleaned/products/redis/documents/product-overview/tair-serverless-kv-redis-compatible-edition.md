# Tair Serverless KV实例,Redis Serverless KV-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/product-overview/tair-serverless-kv-redis-compatible-edition

# Redis兼容版
云数据库 Tair（兼容 Redis）推出的Serverless KV Redis兼容版实例具备自动扩缩容以及按实际访问量计费的能力。高峰时自动扩容保障业务平稳业务无感知，能够显著降低运维的复杂度。使用期间仅按实际访问量计费，有效降低使用成本。
## 架构介绍
Tair Serverless KVRedis兼容版实例为分布式集群架构，兼容Redis开源版6.0，更多信息请参见[Redis](commands-supported-by-tair-serverless-kv-instances.md)[兼容版命令支持](commands-supported-by-tair-serverless-kv-instances.md)。以下为架构图和组件说明。
| 组件 | 说明 |
| --- | --- |
| 数据分片（Partition） | 一个实例由多分片构成，分片间的数据分布与 Redis Cluster 兼容（SLOT）。每个数据分片均为一主多备（分别部署在不同机器上）的高可用架构。备节点的数量至少为 1。 |
| 高可用服务（HA） | 主节点（Master）发生故障后，系统会自动在 30 秒内切换至备节点（Replica），以保证服务高可用和数据高可靠。 |
### Serverless能力
创建和使用Tair Serverless KVRedis兼容版实例时，您无需为实例规格配置而感到困扰。实例会自动适应应用程序的RCU（读操作）、WCU（写操作）以及存储用量需求，根据工作负载自动进行扩缩容。以下为概念说明：
存储空间：用于数据的存储，实例的存储空间范围为0 ~ 25 TB，存储空间能够根据用量自动扩、缩容，无需预设资源大小。
RCU（读操作）：最小读操作单位，每个RCU表示单个客户端访问4 KB的数据。若单次读操作不足4 KB，则按1 RCU计算；超过时，按4KB为单位向上取整，即RCU = ⌈单次读取数据量 / 4 KB⌉。
WCU（写操作）：最小写操作单位，每个WCU表示单个客户端写入512 B的数据。单次写操作不足512 B时，则按1 WCU计算；超过时，按512 B为单位向上取整，即WCU = ⌈单次写入数据量 / 512 B⌉。
### 初始性能和弹性扩容
Tair Serverless KVRedis兼容版实例初始性能峰值（限流阈值）为30,000 RCU/s和20,000 WCU/s。当流量超过性能峰值的60%时，实例开始扩容，扩容期间超过原峰值部分流量发生限流。扩容结束后，新峰值为原先的2倍，若流量仍超过新峰值的60%，则会再次自动扩容。
说明
Tair Serverless KV实例保证可以在30分钟内完成一次扩容任务。
当实例流量超出限流阈值时，超出部分将被限流，限流行为默认为排队等待（与传统Redis行为一致），可选返回错误，更多信息请参考[客户端限流处理](best-practices-in-client-side-throttling.md)。
### 实例限制
最大容量：25TB。
最大带宽：最大出、入带宽均为16Gbit/s（即2GB/s），且二者独立计量。
最大连接数：400,000个。
最大吞吐：访问性能上限为7,680,000 RCU/s和5,120,000 WCU/s。
热点吞吐：热点 Key 的请求上限为30,000 RCU/s和20,000 WCU/s.
## 计费
Tair Serverless KV的费用主要包含两部分：计算资源费用 (RCU/WCU)和存储空间费用。[Tair Serverless KV](billing-for-tair-serverless-kv.md)[计费说明](billing-for-tair-serverless-kv.md)
## 开始使用Tair Serverless KVRedis兼容版
### 创建与释放Tair Serverless KVRedis兼容版实例
操作步骤
访问[Tair Serverless KV](https://kvstorenext.console.aliyun.com/Redis/serverless)[实例列表](https://kvstorenext.console.aliyun.com/Redis/serverless)。
单击创建实例。
选择地域、专有网络以及虚拟交换机。
设置实例参数（可选，也可以保持默认）：
设置实例名称。
选择密码设置为立即设置，并输入密码。
后续，您可以在控制台中重置或修改密码。
配置资源组和标签，也可以保持默认选项。
阅读并选中服务协议，单击开通。
在Serverless KV实例列表中，实例的运行状态为运行中时，表示实例创建完成。
说明
如需释放实例，请在实例右侧单击释放。
后续步骤：
[设置白名单](../getting-started/step-2-configure-whitelists.md)
[连接](connect-to-a-tair-serverless-kv-instance.md)[Redis](connect-to-a-tair-serverless-kv-instance.md)[兼容版实例](connect-to-a-tair-serverless-kv-instance.md)
### 性能监控
Tair Serverless KV实例的性能监控提供了用量、流量、时延、请求数、Key统计、命中率等性能监控指标。您可以查询实例在过去一个月内指定时间段的监控数据，掌握实例的性能与运行状况，排查性能问题。
操作步骤
访问[Tair Serverless KV](https://kvstorenext.console.aliyun.com/Redis/serverless)[实例列表](https://kvstorenext.console.aliyun.com/Redis/serverless)。
在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击性能监控。
### 备份与恢复
Tair Serverless KV实例支持以下备份与恢复方案。
| 类别 | 实施方案 | 说明 |
| --- | --- | --- |
| 数据备份 | [自动或手动备份](../user-guide/automatic-or-manual-backup.md) | 实例会按照默认的策略自动备份数据，您可以根据业务需求修改自动备份策略，也可以手动发起备份。 |
| 数据恢复 | [从备份集恢复至新实例](../user-guide/restore-data-from-a-backup-set-to-a-new-instance.md) | 支持从指定的备份集创建新实例，新实例中的数据将和该备份集中的数据一致，可用于数据恢复、快速部署业务或数据验证等场景。 |
## 常见问题
Q：实例扩容后，我的业务访问量快速回落，此时我需要为扩容上来的性能付费吗？
A：不需要，费用只与CU、存储的使用量相关，与后台实际资源无关。如当前实例性能上限为 30,000 RCU/s，访问量为 200 RCU/s，此时只按 200 RCU/ s 和当前的存储容量进行计费。在请求负载处于低水位一段时间后实例会自动缩容。
Q：Tair Serverless KV中的数据是持久化的吗？
A：是的，Tair Serverless KV中的数据是实时持久化的（落盘），相比传统Redis，Tair Serverless KV更适合作为持久化的数据库使用。
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
