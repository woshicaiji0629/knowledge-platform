# 各场景数据采集方式选择指南-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/data-collection-overview

# 数据采集概述
日志服务的数据采集支持多种采集方式与数据类型。本文将介绍如何选择不同来源数据的采集方式。
## 数据采集方式
数据采集作为使用日志服务功能的第一步，目的是将目标数据传输并保存到日志服务中，以便后续使用日志服务的其他功能。例如对数据进行[查询与分析](quick-guide-to-query-and-analysis.md)，对数据格式与内容进行[数据加工处理](data-processing-new-version-quick-start.md)，将数据[消费](data-consumption-and-subscription.md)或[投递](data-shipping-overview.md)到第三方系统等。
重要
日志服务提供的采集方式仅支持采集增量数据，若需要历史数据请使用[数据导入](data-collection-overview.md)。
概念介绍：
[LoongCollector（原](loongcollector-collection.md)[Logtail）](loongcollector-collection.md)：Logtail是日志服务提供的日志采集Agent，用于采集阿里云ECS、自建IDC或其他云厂商等服务器上的日志。Logtail基于日志文件采集，无需修改应用程序代码，且采集日志不会影响应用程序运行。LoongCollector是日志服务推出的新一代采集Agent，是Logtail的升级版，兼容Logtail的同时性能更佳。
[SDK](use-sdks-to-collect-logs.md)[采集](use-sdks-to-collect-logs.md)：日志服务支持直接使用SDK/API等方式在代码中进行定制化开发，相比其他方式灵活性更高。
### Kubernetes环境下的采集方案
当企业应用部署在Kubernetes环境下，使用阿里云日志服务进行采集时请参考如下内容：
[Kubernetes](container-log-collection-in-a-kubernetes-cluster.md)[集群容器日志采集](container-log-collection-in-a-kubernetes-cluster.md)：对于应用日志采集有两种方式，支持标准输出与文本日志类型，采集前请阅读[Kubernetes](kubernetes-cluster-container-log-collection-instructions.md)[集群容器日志采集须知](kubernetes-cluster-container-log-collection-instructions.md)。
[通过控制台采集集群容器日志（标准输出/文件）](collect-kubernetes-cluster-text-logs-daemonset.md)：通过控制台手动可视化配置日志采集规则，适合少量集群及测试环境的使用场景。
[通过](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)[Kubernetes CRD](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)[采集集群容器日志（标准输出/文件）](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)：使用CRD自定义资源配置日志采集规则，方便模板化，生产集群优先选择，支持CI/CD自动化的场景。
[采集](use-prometheus-to-collect-kubernetes-metric-data.md)[Kubernetes](use-prometheus-to-collect-kubernetes-metric-data.md)[监控数据(Metric)](use-prometheus-to-collect-kubernetes-metric-data.md)：本文介绍如何在Kubernetes上部署Prometheus，将监控数据采集到日志服务MetricStore中，并将日志服务MetricStore对接到Grafana实现监控数据可视化展示。
[采集](collect-kubernetes-events.md)[Kubernetes](collect-kubernetes-events.md)[事件](collect-kubernetes-events.md)：日志服务支持使用eventer将Kubernetes中的事件采集到日志服务。
### 主机/服务器中数据采集方案
当企业应用部署在阿里云ECS，自建服务器或其他云服务器等主机环境下，使用阿里云日志服务进行采集时请参考如下内容：
[持续采集主机文本日志](host-text-log-collection-auto-install.md)：对于应用日志支持多种解析格式，如Nginx,JSON,Apache,IIS,分隔符等，需要重点注意不同服务器与日志服务Project的关系，会影响日志服务采集器的安装方式。
[采集主机监控数据(Metric)](collect-metric-data-from-hosts.md)：支持采集主机CPU、内存、负载、磁盘、网络等监控数据。
[采集](collect-windows-event-logs.md)[Windows](collect-windows-event-logs.md)[事件日志](collect-windows-event-logs.md)：Windows事件日志采用发布订阅的模式，应用程序或者内核将事件日志发布到指定的通道，日志服务调用Windows API订阅这些通道，从而持续获取相关事件日志。
### Docker数据采集方案
[采集](collect-docker-container-text-logs.md)[Docker](collect-docker-container-text-logs.md)[容器日志（标准输出/文件）](collect-docker-container-text-logs.md)：采集 Docker 容器的标准输出（stdout/stderr）和容器内文本日志文件。
[采集](collect-docker-events.md)[Docker](collect-docker-events.md)[事件](collect-docker-events.md)：采集Docker事件信息，其中包含容器、镜像、插件、网络、存储等交互事件。
### 阿里云云产品数据采集方案
[云产品日志采集](collection-of-alibaba-cloud-service-logs.md)：日志服务支持采集弹性计算、存储服务、安全、数据库等多种阿里云云产品的日志数据，包括云产品的操作信息、运行状况、业务动态等信息。
### 中间件数据采集方案
[采集](retrieving-sql-query-results.md)[SQL](retrieving-sql-query-results.md)[查询结果](retrieving-sql-query-results.md)：支持采集SQL Server，MySQL，PostgreSQL的查询结果。
[前端/Web](frontend-log-collection.md)[服务日志采集](frontend-log-collection.md)：
[使用](use-the-web-tracking-feature-to-collect-logs.md)[WebTracking](use-the-web-tracking-feature-to-collect-logs.md)[采集前端日志](use-the-web-tracking-feature-to-collect-logs.md)：WebTracking是一种通过向前端页面添加特定代码段，来跟踪用户行为的技术。能够在浏览器、小程序和移动端中采集用户行为数据。
[采集](collect-http-data.md)[HTTP](collect-http-data.md)[数据](collect-http-data.md)：定期请求指定的URL，将请求返回的Body内容作为数据源上传到日志服务。
[采集](collect-unity3d-logs.md)[Unity3D](collect-unity3d-logs.md)[日志](collect-unity3d-logs.md)：支持使用Web Tracking采集Unity3D日志。
### 与现有三方生态集成
[集成其他开源](collect-data-using-other-open-source-agents.md)[Agent](collect-data-using-other-open-source-agents.md)[与协议采集日志](collect-data-using-other-open-source-agents.md)：支持如下方式。
使用Loggie的Sink配置，将采集到的日志上传到日志服务。
使用Log4j2 Appender将日志采集到日志服务。
使用Syslog-ng采集日志并通过Syslog协议上传。
使用Kafka Producer SDK、Beats系列软件、Collectd、Fluentd、Logstash、Telegraf、Vector等采集工具采集日志，并通过Kafka协议上传到日志服务。
[接入](import-metrics-collected-by-telegraf.md)[Telegraf](import-metrics-collected-by-telegraf.md)[监控](import-metrics-collected-by-telegraf.md)：日志服务支持将Telegraf采集的监控数据（MySQL监控数据、Redis监控数据、Elasticsearch监控数据、Clickhouse监控数据、Kafka监控数据、Tomcat监控数据等）通过InfluxDB协议写入LoongCollector（原Logtail），再将监控数据上传到日志服务。
[采集](collect-metric-data-from-open-falcon.md)[Open-Falcon](collect-metric-data-from-open-falcon.md)[监控数据](collect-metric-data-from-open-falcon.md)：配置Transfer将Open-Falcon数据上传至日志服务,Open-Falcon版本需包含[Influxdb support](https://github.com/open-falcon/falcon-plus/commit/df7a2f80e27902a7e081c595bd1a24080cc624e7)功能。
[通过](collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[Remote Write](collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[协议接入](collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[Prometheus](collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[监控数据](collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)：日志服务支持Prometheus的Remote Write协议，只需要在Prometheus中启动Remote Write功能即可采集数据到日志服务。
### SDK采集
[SDK](developer-reference/overview-of-log-service-sdk.md)[采集](developer-reference/overview-of-log-service-sdk.md)：日志服务支持Java、Python、PHP、Node.js、C、Go、iOS、Android、C++等语言的SDK采集。不仅可以写入日志数据，也可以[通过](use-an-sdk-to-collect-metrics.md)[SDK](use-an-sdk-to-collect-metrics.md)[写入时序数据](use-an-sdk-to-collect-metrics.md)。
### 数据导入
支持将已有的其他数据导入到日志服务进行分析，包括其他应用数据与历史文件数据。
[导入](import-data-from-oss-to-log-service.md)[OSS Bucket](import-data-from-oss-to-log-service.md)[中的日志文件](import-data-from-oss-to-log-service.md)。
[导入](import-data-from-elasticsearch-to-log-service.md)[Elasticsearch/OpenSearch](import-data-from-elasticsearch-to-log-service.md)[数据](import-data-from-elasticsearch-to-log-service.md)。
[导入](importing-amazon-s3-data.md)[Amazon S3](importing-amazon-s3-data.md)[的日志文件](importing-amazon-s3-data.md)。
[导入](import-data-from-kafka-to-log-service.md)[Kafka](import-data-from-kafka-to-log-service.md)[数据](import-data-from-kafka-to-log-service.md)。
日志服务仅采集增量日志。采集历史日志需要[导入历史日志文件](import-historical-logs.md)。
## 数据脱敏/传输加密能力
[数据传输加密](data-encryption.md)：日志服务支持通过密钥管理服务KMS对数据进行加密存储，同时支持基于SSL/TLS的HTTPS加密传输。
[数据处理](data-processing-sls.md)：对日志数据进行格式化处理，根据数据传输流程阶段有以下三种数据处理方式。
[数据采集时处理（处理插件）](processing-plug-ins.md)：需要基于日志服务自研采集器LoongCollector（原Logtail），数据在从本地服务器往日志服务传输前脱敏，消耗本地服务器资源处理解析。
[数据写入时处理（写入处理器）](sls-write-processor.md)：在数据传输至日志服务但进行存储前处理，可进行脱敏规则的配置，消耗日志服务端资源，处理完成后进行数据存储。
[数据写入后处理（数据加工）](data-processing-new-version-quick-start.md)：对存储于日志服务的数据进行处理，可进行脱敏规则的配置，在往其他LogStore或第三方系统输出前脱敏。
## 采集相关文档
[跨地域采集日志](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)：应用部署在地域A，日志服务Project部署在地域B。该方案解决如何将地域A的ECS实例中的日志数据发送到地域B的Project中。
[跨阿里云账号采集日志](use-logtail-to-collect-logs-across-accounts.md)：应用A使用账号A的日志服务，应用B使用账号B的日志服务，现计划将应用A与B的日志集中采集到账号A下管理。
[采集-IoT/嵌入式日志](collect-iot-or-embedded-development-logs.md)：智能路由器、各种电视棒、天猫精灵、扫地机器人等IoT设备应用数目多、分布广，难以调试且硬件受限，该方案解决如何处理IoT设备日志的问题。
[采集客户端数据的高可用方案](high-availability-solutions-to-collect-data-from-clients.md)：针对单集群故障风险，提供双写方案和数据加工复制+写入切换方案两种异地多活的客户端数据采集方案。
[采集企业内网服务器日志](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)：服务器部署在企业内网中且没有公网访问权限，可通过代理模式将这些服务器的日志采集到日志服务。
更多方案可参考[数据采集最佳实践](data-collection-best-practices.md)。
## 常见问题
专线方式接入应如何选择网络？
请选择阿里云内网（经典网络或专有网络VPC）。
如何选择网络类型和接入点（Endpoint）？
网络类型：[LoongCollector](loongcollector-installation-linux.md)[网络传输类型](loongcollector-installation-linux.md)。
接入点：通过[地域](loongcollector-installation-linux.md)找到对应[服务接入点](developer-reference/api-sls-2020-12-30-endpoint.md)。
采集公网数据时能否采集公网IP地址？
[为日志自动添加公网](manage-a-logstore.md)[IP](manage-a-logstore.md)[与到达日志服务时间](manage-a-logstore.md)。
采集问题如何排查？
[LoongCollector](loongcollector-collection-exception-troubleshooting.md)[采集异常问题汇总排查](loongcollector-collection-exception-troubleshooting.md)。
更多问题可查看[数据采集常见问题](faq-18.md)。
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
