# 配置Prometheus监控数据为Grafana数据源-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/send-time-series-data-from-log-service-to-grafana

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

# 时序数据对接Grafana

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

日志服务MetricStore提供了兼容Prometheus的查询接口，您可以直接通过Prometheus数据源方式对接到Grafana进行可视化演示。本文介绍配置Prometheus监控数据为Grafana数据源的操作步骤。

## 操作视频

## 前提条件

- 

已安装Grafana。具体操作，请参见[安装](http://docs.grafana.org/installation/)[Grafana](http://docs.grafana.org/installation/)。

- 

已接入时序数据。具体操作，请参见[通过](products/sls/documents/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[Remote Write](products/sls/documents/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[协议接入](products/sls/documents/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[Prometheus](products/sls/documents/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[监控数据](products/sls/documents/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)。

## 对接Grafana

- 

登录Grafana。

- 

在左侧导航栏，选择Configuration>Data Sources。

- 

在Data Sources页签，单击Add data source。

- 

选择Prometheus，单击Select。

- 

在Settings页签中，请参考如下说明配置数据源。

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| Name | 请您自定义一个数据源的名称，例如 Prometheus-01。 |
| HTTP | URL ：日志服务 MetricStore 的 URL，格式为 https://{project}.{sls-endpoint}/prometheus/{project}/{metricstore} 。其中 {sls-endpoint} 为 Project 所在地域的 Endpoint，详情请参见 [服务入口](products/sls/documents/developer-reference/service-entrance.md) ， {project} 和 {metricstore} 为您已创建的日志服务的 Project 和 Metricstore，请根据实际值替换。例如： https://sls-prometheus-test.cn-hangzhou.log.aliyuncs.com/prometheus/sls-prometheus-test/prometheus 。 说明 为保证传输安全性，请务必设置为 https 。 Whitelisted Cookies ：添加访问白名单，可选。 |
| Auth | 打开 Basic auth 开关。 |
| Basic Auth Details | User 为阿里云账号 AccessKeyID。 Password 为阿里云账号 AccessKeySecret。 建议您使用仅具备指定 Project 只读权限的 RAM 用户账号，详情请参见 [指定](products/sls/documents/use-custom-policies-to-grant-permissions-to-a-ram-user.md) [Project](products/sls/documents/use-custom-policies-to-grant-permissions-to-a-ram-user.md) [只读授权策略](products/sls/documents/use-custom-policies-to-grant-permissions-to-a-ram-user.md) 。 |


- 

单击Save & Test。

## 导入日志服务Grafana模板

您可以在Grafana模板市场中查找日志服务提供的可视化模板并一键导入到您的Grafana中，进行可视化展示。

- 

复制Grafana模板ID。

- 

登录[Grafana](https://grafana.com/grafana/dashboards?search=SLS)[模板市场](https://grafana.com/grafana/dashboards?search=SLS)。

- 

单击您要导入的模板。

- 

在页面右侧，单击Copy ID to Clipboard。

- 

登录Grafana。

- 

在左侧导航栏中，选择Create>Import。

- 

在Grafana.com Dashboard文本框中输入您在[步骤](products/sls/documents/send-time-series-data-from-log-service-to-grafana.md)[1](products/sls/documents/send-time-series-data-from-log-service-to-grafana.md)中复制的Grafana模板ID。

配置完成后，单击空白处，即可进入配置页面，配置数据源。

- 

配置数据源。

此处需配置为您在[对接](products/sls/documents/send-time-series-data-from-log-service-to-grafana.md)[Grafana](products/sls/documents/send-time-series-data-from-log-service-to-grafana.md)中添加的数据源。不同仪表盘对应的数据源参数不同，可能为telegraf、host等。

- 

单击Import。

## Prometheus查询API

日志服务提供了兼容Prometheus的查询API，可直接配置日志服务作为Grafana的Prometheus数据源，同时也支持用各类Prometheus API直接访问。支持的API如下：

| API 名称 | 示例 |
| --- | --- |
| [Instant queries](https://prometheus.io/docs/prometheus/latest/querying/api/#instant-queries) | GET /api/v1/query POST /api/v1/query |
| [Range queries](https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries) | GET /api/v1/query_range POST /api/v1/query_range |
| [Getting label names](https://prometheus.io/docs/prometheus/latest/querying/api/#getting-label-names) | GET /api/v1/labels POST /api/v1/labels |
| [Querying label values](https://prometheus.io/docs/prometheus/latest/querying/api/#querying-label-values) | GET /api/v1/label/<label_name>/values |
| [Finding series by label matchers](https://prometheus.io/docs/prometheus/latest/querying/api/#finding-series-by-label-matchers) | GET /api/v1/series POST /api/v1/series |


[上一篇：可视化最佳实践](products/sls/documents/best-practices-11.md)[下一篇：添加变量类型的过滤器](products/sls/documents/add-a-filter-of-the-replace-variable-type.md)

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
