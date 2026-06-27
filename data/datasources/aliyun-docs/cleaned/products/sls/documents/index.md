# 数据观测与分析的平台化-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/

# 日志服务
日志服务SLS是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。
[免费试用](https://free.aliyun.com/?product=9672268&crowd=personal&spm=a2c4g.31815.0.0.405dde53qNeCGT)[控制台](https://sls.console.aliyun.com/lognext/profile)[存储家族](https://www.aliyun.com/storage/storage)[常见问题](https://help.aliyun.com/document_detail/254665.html)[相关技术圈](https://developer.aliyun.com/group/sls/)
日志服务产品简介
## 学习路径
由浅入深，带您玩转SLS！
### 了解
产品介绍
- [什么是日志服务](product-overview/what-is-log-service.md)
- [核心概念与选型](sls-core-concept-and-selection.md)
- [产品计费](product-overview/billing-overview.md)
- [客户案例](customer-use-cases.md)
### 上手
快速入门
- [快速入门：使用Logtail采集ECS文本日志并分析](getting-started.md)
- [快速入门：使用日志服务SDK采集日志并分析](developer-reference/get-started-with-log-service-sdk-for-python.md)
### 使用
资源管理
- [管理Project](manage-a-project.md)
- [管理Logstore](manage-a-logstore.md)
- [管理MetricStore](manage-a-metricstore.md)
- [管理EventStore](manage-an-eventstore.md)
- [管理Shard](manage-shards.md)
- [资源流控及解决方案](expansion-of-resources.md)
数据采集
- [Logtail安装与管理](sls-logtail-management.md)
- [日志数据采集（Log）](sls-log-collection.md)
- [指标数据采集（Metric）](data-collection.md)
- [链路数据采集（Trace）](call-chain-trace-collection.md)
- [事件数据采集（Event）](acquisition-events-sls.md)
- [数据传输加密](data-encryption.md)
- [数据采集常见问题](faq-18.md)
- [最佳实践](best-practices-2.md)
数据处理
- [数据采集时处理（处理插件）](processing-plug-ins.md)
- [数据写入时处理（写入处理器）](sls-write-processor.md)
- [数据写入后处理（数据加工）](sls-data-processing.md)
- [SPL语法](spl-overview.md)
数据存储
- [管理智能存储分层](data-tiered-storage-overview.md)
- [存储冗余](storage-redundancy.md)
- [数据防篡改](data-tamper-proof.md)
- [数据可靠性](data-reliability.md)
查询与分析
- [查询与分析快速指引](quick-guide-to-query-and-analysis.md)
- [通过AI智能生成查询与分析语句（Copilot）](copilot-automatic-generation-of-ai-assisted-sql-statements.md)
- [索引模式查询与分析](query-and-analyze-logs-in-index-mode.md)
- [扫描模式查询与分析（Scan）](query-and-analyze-logs-in-scan-mode.md)
- [高性能完全精确查询与分析（SQL独享版）](dedicated-sql.md)
- [时序数据查询与分析](time-series-data-query-and-analysis.md)
- [定时查询与分析（定时SQL）](scheduled-sql.md)
- [关联外部数据源查询与分析](associate-external-data-sources.md)
- [跨域查询与分析（数据集Storeview）](cross-domain-query-and-analysis-dataset-storeview.md)
- [使用第三方工具查询与分析](use-third-party-tools-to-query-and-analyze-log-service-data.md)
数据监控
- [可视化概述](overview-of-visualization.md)
- [仪表盘](dashboard.md)
- [统计图表](statistical-charts.md)
- [告警](sls-alerting.md)
数据输出与集成
- [下载日志](download-logs.md)
- [数据消费与订阅](data-consumption-and-subscription.md)
- [数据投递](data-shipping.md)
### 实践
数据采集
- [采集IoT/嵌入式日志](user-guide/collect-iot-or-embedded-development-logs.md)
- [采集通过WebTracking采集日志](user-guide/use-web-tracking-to-collect-logs.md)
- [采集搭建移动端日志直传服务](user-guide/build-a-service-to-upload-logs-from-mobile-apps-to-log-service.md)
- [采集公网数据](user-guide/collect-data-over-the-internet.md)
- [采集多渠道数据](user-guide/collect-data-from-multiple-channels.md)
查询与分析
- [关联Logstore与MySQL数据库进行查询分析](user-guide/associate-a-logstore-with-a-mysql-database-to-perform-query-and-analysis.md)
- [关联Logstore与OSS外表进行查询和分析](user-guide/associate-a-logstore-with-an-oss-external-table-to-perform-query-and-analysis.md)
- [查询MNS日志](user-guide/query-mns-logs.md)
- [分析网站日志](user-guide/analyze-website-logs.md)
- [分析Nginx访问日志](user-guide/collect-and-analyze-nginx-access-logs.md)
可视化
- [添加变量类型的过滤器](user-guide/add-a-filter-of-the-replace-variable-type.md)
- [添加过滤器类型的过滤器](user-guide/add-a-filter-of-the-filter-type.md)
消费与投递
- [搭建监控系统](user-guide/build-a-monitoring-system.md)
- [计量计费日志](user-guide/consume-metering-logs-to-generate-bills.md)
- [通过Consumer Library实现高可靠消费](user-guide/use-a-consumer-group-to-consume-logs-in-high-reliability-mode.md)
### 开发
开发者文档
- [API参考](developer-reference/api-reference-overview.md)
- [SDK参考](developer-reference/overview-of-log-service-sdk.md)
- [CLI参考](developer-reference/overview-of-log-service-cli.md)
- [访问控制](developer-reference/overview-8.md)
- [可视化开发](developer-reference/embed-console-pages-and-share-log-data.md)
- [监控日志服务](user-guide/overview-7.md)
- [使用GetLogs接口查询日志](developer-reference/use-getlogs-to-query-logs.md)
## 体验教程
免费云资源，真实云环境，丰富实践场景
### [使用Nginx模式采集日志](https://developer.aliyun.com/adc/scenario/5e1aca8e9cd14965a6e84ca5cf2fefd0)
[本教程介绍如何通过日志服务控制台创建Nginx模式的Logtail配置快速采集Nginx日志并进行多维度分析。](https://developer.aliyun.com/adc/scenario/5e1aca8e9cd14965a6e84ca5cf2fefd0)
### [日志服务之敏感信息脱敏与审计](https://developer.aliyun.com/adc/scenario/904ff702016d4663a041a27ec3fac835?spm=a2c6h.26976794.J_6470440060.3.297c190cnN5ar1)
[本教程介绍如何使用日志服务创建模拟数据任务（NGINX访问日志），并对数据进行脱敏和审计。](https://developer.aliyun.com/adc/scenario/904ff702016d4663a041a27ec3fac835?spm=a2c6h.26976794.J_6470440060.3.297c190cnN5ar1)
### [日志服务之数据清洗与入湖](https://developer.aliyun.com/adc/scenario/10c085942f0e4b2d83ba08bf077b41cf?spm=a2c6h.26976794.J_6470440060.4.297c190cnN5ar1)
[本教程介绍如何使用日志服务接入NGINX模拟数据，通过数据加工对数据进行清洗并归档至OSS中进行存储。](https://developer.aliyun.com/adc/scenario/10c085942f0e4b2d83ba08bf077b41cf?spm=a2c6h.26976794.J_6470440060.4.297c190cnN5ar1)
### [日志服务之告警接入与管理](https://developer.aliyun.com/adc/scenario/12c6146ddc4343cdbd9c644b2e584ecb?spm=a2c6h.26976794.J_6470440060.5.297c190cnN5ar1)
[本教程介绍如何使用日志服务接入NGINX模拟数据，并配置告警规则来对NGINX访问错误进行监控。](https://developer.aliyun.com/adc/scenario/12c6146ddc4343cdbd9c644b2e584ecb?spm=a2c6h.26976794.J_6470440060.5.297c190cnN5ar1)
### [日志服务之分析用户访问行为](https://developer.aliyun.com/adc/scenario/cad002a5fb954ffcb82aba985e881ae6?spm=a2c6h.26976794.J_6470440060.6.297c190cnN5ar1)
[本教程介绍如何使用日志服务采集NGINX日志，创建仪表盘分析用户访问行为。](https://developer.aliyun.com/adc/scenario/cad002a5fb954ffcb82aba985e881ae6?spm=a2c6h.26976794.J_6470440060.6.297c190cnN5ar1)
### [日志服务数据导入](https://developer.aliyun.com/adc/scenario/a721f0acedc64460b83572997be0683f?spm=a2c6h.26976794.J_6470440060.7.297c190cnN5ar1)
[本教程介绍如何通过日志服务数据导入方式，将OSS数据导入到日志服务。](https://developer.aliyun.com/adc/scenario/a721f0acedc64460b83572997be0683f?spm=a2c6h.26976794.J_6470440060.7.297c190cnN5ar1)
## 热门视频
数据加工
快速入门
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
