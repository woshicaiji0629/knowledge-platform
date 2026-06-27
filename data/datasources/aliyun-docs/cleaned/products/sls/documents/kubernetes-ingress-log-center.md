# Kubernetes Ingress日志分析监控-Kubernetes Ingress日志中心-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/kubernetes-ingress-log-center

# Kubernetes Ingress日志中心
阿里云Kubernetes Ingress组件除了提供外部可访问的URL、负载均衡、SSL、基于名称的虚拟主机外，还支持将所有您的HTTP请求日志记录到标准输出中。日志服务推出Ingress日志中心功能，用于分析和监控Ingress后端对接的服务状态。本文介绍Ingress日志中心相关的功能说明、功能优势、资产说明、费用说明、使用限制等信息。
## 产品试用
SLSPlayground中的Ingress日志中心Demo，内置了演示数据、可视化图表等资源，提供了完整的演示环境，便于您快速了解及体验功能。
您可以单击[Ingress](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/app/ingress_metrics/setting)[日志中心](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/app/ingress_metrics/setting)，进行试用。
重要
SLS Playground中的数据为演示数据，请勿用于生产环境。
## 功能说明
Ingress日志中心基于实时访问日志进行自动聚合，并提供智能巡检、实时告警等功能，详细功能如下：
实时访问日志的采集、存储、查询、分析。
基于原始访问日志实时提取出各类指标信息，包括PV、请求成功率、平均延迟、P50/P99/P9999延迟、出入流量等。并支持多个维度组合，包括host和status。
丰富可视化报表，包括监控大盘、异常事件、运营大盘等，支持报表邮件、钉钉群订阅。
提供智能巡检功能，支持全局以及Service粒度巡检，并支持可视化报表中直接标注异常点。
自定义告警配置，告警通知直接对接消息中心、邮件、短信、语音（电话）、钉钉，并支持对接自定义WebHook。
## 功能优势
简单：一站式开通、中心化使用，无需关心日志收集、存储、计算、可视化等问题，将开发、运维人员从日志处理的繁琐耗时中解放出来，将更多的精力集中到业务开发和技术探索上去。
海量：访问日志与Ingress请求PV成正比，数据规模很大，处理访问日志需要考虑性能和成本问题。日志中心可自定配置预聚和功能，实时计算聚合指标，计算后的聚合结果可降低几个数量级，使查询速度大大提升。
实时：DevOps、监控、报警等场景要求日志数据的实时性。结合日志服务强大的大数据计算能力，秒级分析处理实时产生的日志。
弹性：可任意设置日志存储周期。Logstore容量可动态伸缩满足业务增长需求。
智能：基于达摩院智能AIOps算法，提供各类指标自动巡检功能，有助于更快、更准确地发现并定位问题。
## 资产说明
所有资产都在您选择的Project下，Project内的资产如下：
Logstore
访问日志Logstore用于存储Kubernetes Ingress访问日志，该Logstore为您自定义创建的Logstore。
该Logstore默认开启索引，并配置部分字段的索引。您可以增加索引字段，修改索引后只对新数据生效。您还可以对历史数据重建索引。具体操作，请参见[重建索引](reindex-logs-for-a-logstore.md)。
您可以自定义修改日志存储时间。具体操作，请参见[修改](manage-a-logstore.md)[Logstore](manage-a-logstore.md)[配置](manage-a-logstore.md)。
巡检结果Logstore用于存储巡检结果。开通日志中心功能后，自动生成该专属Logstore，其名称为访问日志Logstore名称-metrics-result。
重要
请勿删除Kubernetes Ingress访问日志相关的Logstore，否则将无法正常采集日志到日志服务。
请勿删除访问日志Logstore中的部分字段的索引，否则指标转换会失败。
Metricstore
监控指标Metricstore用于存储聚合后的指标信息。开通日志中心功能后，自动生成该专属Metricstore，其名称为访问日志Logstore名称-metrics。
说明
监控指标Metricstore存储的是聚合后的指标，数据量相比原始访问日志大大降低，非常适用于长期存储。
聚合规则
| 规则名称 | 聚合时间粒度 | 聚合维度 | 生成指标名 |
| --- | --- | --- | --- |
| total | 10 秒 | total | pv body_bytes_sent_avg body_bytes_sent_sum request_length_avg request_length_sum upstream_response_time_avg upstream_response_time_p50 upstream_response_time_p90 upstream_response_time_p99 upstream_response_time_p9999 request_time_avg request_time_p50 request_time_p90 request_time_p99 request_time_p9999 |
| host | 10 秒 | host | pv:host body_bytes_sent_avg:host body_bytes_sent_sum:host request_length_avg:host request_length_sum:host upstream_response_time_avg:host upstream_response_time_p50:host upstream_response_time_p90:host upstream_response_time_p99:host upstream_response_time_p9999:host request_time_avg:host request_time_p50:host request_time_p90:host request_time_p99:host request_time_p9999:host |
| host_status | 10 秒 | host+status | pv:host:status body_bytes_sent_avg:host:status body_bytes_sent_sum:host:status request_length_avg:host:status request_length_sum:host:status upstream_response_time_avg:host:status upstream_response_time_p50:host:status upstream_response_time_p90:host:status upstream_response_time_p99:host:status upstream_response_time_p9999:host:status request_time_avg:host:status request_time_p50:host:status request_time_p90:host:status request_time_p99:host:status request_time_p9999:host:status |
巡检规则
| 规则名称 | 开启状态 | 巡检算法 | 巡检指标 |
| --- | --- | --- | --- |
| total | 默认开启 | Time2Graph | pv body_bytes_sent_avg body_bytes_sent_sum request_length_avg request_length_sum upstream_response_time_avg request_time_avg |
| host | 默认开启 | Time2Graph | pv:host body_bytes_sent_avg:host body_bytes_sent_sum:host request_length_avg:host request_length_sum:host upstream_response_time_avg:host request_time_avg:host |
| host_status | 默认关闭 | Time2Graph | pv:host:status body_bytes_sent_avg:host:status body_bytes_sent_sum:host:status request_length_avg:host:status request_length_sum:host:status upstream_response_time_avg:host:status request_time_avg:host:status |
专属仪表盘
| 仪表盘名称 | 关联的 Logstore、Metricstore | 说明 |
| --- | --- | --- |
| 运营大盘 | 访问日志 Logstore 名称 | 展示用户请求相关的信息，包括 PV、UV、移动端分布、国家/省/市分布等。 说明 此部分信息基于原始访问日志全量计算，数据量超大的情况下会有一定延迟。 |
| 概览 | 访问日志 Logstore 名称 -metrics | 展示 Kubernetes 总体的监控信息，包括 PV、失败率、5XX 比例、状态码分布、流量等。 |
| 监控大盘 | 访问日志 Logstore 名称 -metrics | 支持以 host、status 等维度过滤出实例详细的监控信息。 |
| 异常事件 | 访问日志 Logstore 名称 -metrics 访问日志 Logstore 名称 -metrics-result | 展示流式巡检算法检测出的 Service 粒度异常信息，包括异常统计以及具体指标上异常的实时显示。 |
## 费用说明
日志服务根据存储空间、读取流量、请求数量、数据加工、数据投递等进行收费。更多信息，请参见[按使用功能计费模式计费项](billable-items.md)。
## 使用限制
必须成功解析Ingress日志后才能进行时序转换规则配置和巡检配置。对于自定义日志格式的Ingress访问日志，需手动配置解析规则解析日志，对应的日志字段名称需要符合默认的字段命名规则。
日志中心配置完成后只对新产生的日志生效，存量日志并不会转换成指标信息。
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
