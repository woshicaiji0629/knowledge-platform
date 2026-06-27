# 各类监控指标数据的采集方案汇总-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/data-collection

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 指标数据采集（Metric）

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

日志服务支持通过Logtail采集主机CPU、内存、负载、磁盘、网络等监控数据。也支持通过Telegraf+Logtail采集其他产品监控数据。本文列举常见的采集方案。

| 方案 | 说明 |
| --- | --- |
| [采集主机监控数据](products/sls/documents/collect-metric-data-from-hosts.md) | 日志服务 Logtail 支持采集主机 CPU、内存、负载、磁盘、网络等监控数据。 |
| [采集](products/sls/documents/collect-metric-data-from-open-falcon.md) [Open-Falcon](products/sls/documents/collect-metric-data-from-open-falcon.md) [数据](products/sls/documents/collect-metric-data-from-open-falcon.md) | Open-Falcon 是一款企业级、高可用、可扩展的开源监控解决方案，用于监控服务器的状态，例如磁盘空间、端口存活、网络流量等。 |
| [采集](products/sls/documents/collect-ping-and-tcping-data.md) [ping](products/sls/documents/collect-ping-and-tcping-data.md) [和](products/sls/documents/collect-ping-and-tcping-data.md) [tcping](products/sls/documents/collect-ping-and-tcping-data.md) [数据](products/sls/documents/collect-ping-and-tcping-data.md) | 介绍通过 Logtail 采集 ping 和 tcping 数据到日志服务 Metricstore 的操作步骤。 |
| [通过](products/sls/documents/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md) [Remote Write](products/sls/documents/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md) [协议接入](products/sls/documents/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md) [Prometheus](products/sls/documents/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md) [监控数据](products/sls/documents/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md) | 日志服务支持 Prometheus 的 Remote Write 协议，只需要在 Prometheus 中启动 Remote Write 功能即可采集数据到日志服务。 |
| [通过](products/sls/documents/collect-metric-data-from-prometheus-by-using-a-logtail-plug-in.md) [Logtail](products/sls/documents/collect-metric-data-from-prometheus-by-using-a-logtail-plug-in.md) [插件接入](products/sls/documents/collect-metric-data-from-prometheus-by-using-a-logtail-plug-in.md) [Prometheus](products/sls/documents/collect-metric-data-from-prometheus-by-using-a-logtail-plug-in.md) [监控数据](products/sls/documents/collect-metric-data-from-prometheus-by-using-a-logtail-plug-in.md) | 日志服务 Logtail 插件支持采集 Prometheus 格式的各类指标数据，例如 Node Exporter、Kafka Exporter 及应用所涉及的 Prometheus 指标等。 |
| [接入](products/sls/documents/collect-metric-data-from-elasticsearch-servers.md) [Elasticsearch](products/sls/documents/collect-metric-data-from-elasticsearch-servers.md) [监控数据](products/sls/documents/collect-metric-data-from-elasticsearch-servers.md) | 介绍如何通过日志服务来完成 Elasticsearch 监控数据的采集和可视化。 |
| [接入](products/sls/documents/collect-metric-data-from-mysql-servers.md) [MySQL](products/sls/documents/collect-metric-data-from-mysql-servers.md) [监控数据](products/sls/documents/collect-metric-data-from-mysql-servers.md) | 介绍如何通过日志服务来完成 MySQL 监控数据的采集和可视化。 |
| [接入](products/sls/documents/collect-metric-data-from-redis-servers.md) [Redis](products/sls/documents/collect-metric-data-from-redis-servers.md) [监控数据](products/sls/documents/collect-metric-data-from-redis-servers.md) | 介绍如何通过日志服务来完成 Redis 监控数据的采集和可视化。 |
| [接入](products/sls/documents/collect-metric-data-from-mongodb-databases.md) [MongoDB](products/sls/documents/collect-metric-data-from-mongodb-databases.md) [监控数据](products/sls/documents/collect-metric-data-from-mongodb-databases.md) | 介绍如何通过日志服务来完成 MongoDB 监控数据的采集和可视化。 |
| [接入](products/sls/documents/collect-metric-data-from-clickhouse-servers.md) [Clickhouse](products/sls/documents/collect-metric-data-from-clickhouse-servers.md) [监控数据](products/sls/documents/collect-metric-data-from-clickhouse-servers.md) | 介绍如何通过日志服务来完成 ClickHouse 监控数据的采集和可视化。 |
| [接入](products/sls/documents/collect-metric-data-from-kafka-servers.md) [Kafka](products/sls/documents/collect-metric-data-from-kafka-servers.md) [监控数据](products/sls/documents/collect-metric-data-from-kafka-servers.md) | 介绍如何通过日志服务来完成 Kafka 监控数据的采集和可视化。 |
| [接入](products/sls/documents/collect-metric-data-from-java-applications-or-tomcat-servers.md) [Java](products/sls/documents/collect-metric-data-from-java-applications-or-tomcat-servers.md) [应用或](products/sls/documents/collect-metric-data-from-java-applications-or-tomcat-servers.md) [Tomcat](products/sls/documents/collect-metric-data-from-java-applications-or-tomcat-servers.md) [的监控数据](products/sls/documents/collect-metric-data-from-java-applications-or-tomcat-servers.md) | 以 Java 应用监控数据为例，介绍如何通过日志服务来完成 Java 应用数据的采集和可视化。 |
| [接入](products/sls/documents/collect-metric-data-from-nginx-servers.md) [Nginx](products/sls/documents/collect-metric-data-from-nginx-servers.md) [监控数据](products/sls/documents/collect-metric-data-from-nginx-servers.md) | 介绍如何通过日志服务来完成 Nginx 监控数据的采集和可视化。 |
| [接入](products/sls/documents/collect-metric-data-from-nvidia-gpus.md) [NVIDIA GPU](products/sls/documents/collect-metric-data-from-nvidia-gpus.md) [监控数据](products/sls/documents/collect-metric-data-from-nvidia-gpus.md) | 介绍如何通过日志服务来完成 NVIDIA GPU 监控数据的采集和可视化。 |
| [通过](products/sls/documents/use-an-sdk-to-collect-metrics.md) [SDK](products/sls/documents/use-an-sdk-to-collect-metrics.md) [写入时序数据](products/sls/documents/use-an-sdk-to-collect-metrics.md) | 日志服务支持通过 SDK 写入时序数据，本文列举了 Java、Golang 和 Python 语言的 SDK demo。 |


[上一篇：采集Beats和Logstash数据源](products/sls/documents/collect-data-from-beats-and-logstash.md)[下一篇：采集主机监控数据](products/sls/documents/collect-metric-data-from-hosts.md)

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
