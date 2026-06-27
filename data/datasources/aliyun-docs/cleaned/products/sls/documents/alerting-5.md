# 告警功能竞品分析与选型对比-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/alerting-5

# 可观测告警运维系统对比
日志服务新版告警是一站式的告警监控、降噪、事务管理、通知分派的智能运维平台。本文介绍日志服务新版告警与各个开源告警系统的对比信息。
## 日志服务告警
日志服务新版告警支持监控日志、时序等各类数据，支持接收三方告警，支持对告警进行降噪、事件管理、通知管理等，新增40+功能场景，充分考虑研发、运维、安全以及运营人员的告警监控运维需求。更多信息，请参见[什么是日志服务告警](user-guide/the-alerting-feature-of-log-service.md)。
新版告警具备如下五大优势：
## 与ELK X-Pack告警（Elasticsearch Watcher、Kibana 7.x+Alert）对比
自建ELK使用开源的Elasticsearch+Logstash+Kibana组合，其不包括告警功能。如果您要为自建ELK配置告警，需额外购买X-Pack商业包，其包含两个告警功能（Elasticsearch Watcher和Kibana 7.x+Alert）。这两个告警功能互相独立，不能协同与关联。
| 类别 | 对比项 | 日志服务告警 | ELK X-Pack 告警 |
| --- | --- | --- | --- |
| 持久性 | 告警服务可用性 | 服务可用性>99.9%、存储持久性>99.99999999%。 | 商业版采用分布式，存储数据需要手动配置。 |
| 成本 | 费用 | 无订阅费用、免运维、监控与告警管理免费、通知渠道仅短信和语音按照条数收取少量费用。 | 商业订阅费用、人工运维费用、自购的机器费用、三方短信和语音费用。 |
| 告警监控 | 监控日志和时序数据的规模 | PB 级别。 | TB 级别。 |
| 监控查询分析语法 | 支持 SQL92 语法（含扩展）、PromQL 语法、告警语法扩展。 | Elasticsearch Watcher：支持 ES DSL。 Kibana 7.x+Alert：支持有限的过滤聚集操作。 |  |
| 机器学习能力 | 支持十多种预测、异常检测、根因分析等 AI 算法。 | 支持 X-Pack ML 算法。 |  |
| 数据协同能力 | 支持跨存储库、跨 Project、跨地域、跨账号协同监控。 | 支持同一集群下的同构索引合并分析。 |  |
| 无数据告警 | 支持。 | 不支持。 |  |
| 告警恢复 | 支持。 | 不支持。 |  |
| 标签与标注 | 支持。 | Kibana 7.x+Alert 支持自定义标签。 |  |
| 动态严重度 | 支持。 | 不支持。 |  |
| 分组评估 | 支持，可自定义配置。 | Elasticsearch Watcher：固定不分组。 Kibana 7.x+Alert：固定自动分组。 |  |
| 监控侧控制 | 支持配置持续触发阈值。 支持暂停和自动恢复（基于时间）监控。 | Elasticsearch Watcher 支持暂停和自动恢复（基于 ACK）。 |  |
| 告警管理 | 告警管理 | 支持告警去重、合并、抑制、静默。 支持事务管理、责任人设置。 | 不支持。 |
| 通知管理 | 通知管理 | 支持通知渠道动态分派、告警级别提升、接收组管理、渠道日历设置、值班表设置、渠道额度控制。 | 不支持。 |
| 常用渠道 | 支持短信、语音、钉钉、邮件、WebHook、阿里云消息中心等通知渠道。 其中通过 WebHook，还支持企业微信、飞书、Slack 等渠道。 | 支持邮件、WebHook 等通知渠道，不支持短信和语音。 Watcher 支持 PagerDuty、JIRA、Slack。 Kibana Alert 支持 IBM Resilient、MS Teams、Service Now。 |  |
## 与Prometheus&Loki（含AlertManager）告警对比
自建Prometheus&Loki使用开源的Prometheus+Loki+AlertManager组合搭建告警监控系统，其中Prometheus Alert对时序数据进行告警监控，Loki对日志进行告警监控，两者共同将告警发送给Alert Manager进行告警管理。
| 类别 | 对比项 | 日志服务告警 | Prometheus+Loki 2.0 告警 |
| --- | --- | --- | --- |
| 持久性 | 告警服务可用性 | 服务可用性>99.9%、存储持久性>99.99999999%。 | 部分服务采用分布式、部分服务采用单机可用性；存储采用单机可用性。 |
| 成本 | 费用 | 无订阅费用、免运维、监控与告警管理免费、通知渠道仅短信和语音按照条数收取少量费用。 | 人工运维费用、自购的机器费用、三方短信和语音费用。 |
| 告警监控 | 监控日志和时序数据的规模 | PB 级别。 | 日志：百 GB 级别。 时序数据：TB 级别。 |
| 监控查询分析语法 | 支持 SQL92 语法（含扩展）、PromQL 语法、告警语法。 | 日志：LogQL 语法。 时序数据：PromQL 语法。 |  |
| 机器学习能力 | 支持十多种预测、异常检测、根因分析等 AI 算法。 | 不支持。 |  |
| 数据协同能力 | 支持跨存储库、跨 Project、跨地域、跨账号协同监控。 | 支持同一集群下跨指标 PromQL Join。 |  |
| 无数据告警 | 支持。 | 不支持。 |  |
| 告警恢复 | 支持。 | 支持。 |  |
| 标签与标注 | 支持。 | 支持。 |  |
| 动态严重度 | 支持。 | 不支持。 |  |
| 分组评估 | 支持，可自定义配置。 | 支持按标签固定分组。 |  |
| 监控侧控制 | 支持配置持续触发阈值。 支持暂停和自动恢复（基于时间）监控。 | 支持设置持续触发阈值，不支持暂停与恢复监控。 |  |
| 告警管理 | 告警管理 | 支持告警去重、合并、抑制、静默。 支持事务管理、责任人设置。 | 支持告警去重、合并、抑制、静默，不支持事务管理、责任人管理。 |
| 通知管理 | 通知管理 | 支持通知渠道动态分派、告警级别提升、接收组管理、渠道日历设置、值班表设置、渠道额度控制。 | 仅支持渠道动态分派，其他不支持。 |
| 常用渠道 | 支持短信、语音、钉钉、邮件、WebHook、阿里云消息中心等通知渠道。 其中通过 WebHook，还支持企业微信、飞书、Slack 等渠道。 | 支持邮件、企业微信、WebHook（不支持自定义 Body）、PagerDuty、PushOver、Slack、OpsGenie、VictorOps。不支持短信、语音服务。 通过三方插件，也可以支持钉钉、飞书、Slack 等渠道。 |  |
## 与InfluxDB 2.0告警（含Kapacitor）告警对比
自建InfluxDB使用开源的InfluxDB OSS 2.0+Kapacitor组合搭建告警监控系统。如果您需要集群部署功能，还需要购买InfluxDB商业版。该方案仅适用于时序数据的告警监控。
| 类别 | 对比项 | 日志服务告警 | InfluxDB 2.0 告警（含 Kapacitor） |
| --- | --- | --- | --- |
| 持久性 | 告警服务可用性 | 服务可用性>99.9%、存储持久性>99.99999999%。 | 商业版采用分布式，支持存储配置。开源采用单机版。 |
| 成本 | 费用 | 无订阅费用、免运维、监控与告警管理免费、通知渠道仅短信和语音按照条数收取少量费用。 | 商业版订阅费用、人工运维费用、自购的机器费用、三方短信和语音费用。 |
| 告警监控 | 监控日志和时序数据的规模 | PB 级别。 | 日志：不支持。 时序数据：TB 级别。 |
| 监控查询分析语法 | 支持 SQL92 语法（含扩展）、PromQL 语法、告警语法扩展。 | 支持 Flux 语法。 |  |
| 机器学习能力 | 支持十多种预测、异常检测、根因分析等 AI 算法。 | 支持 Loud ML 算法。 |  |
| 数据协同能力 | 支持跨存储库、跨 Project、跨地域、跨账号协同监控。 | 支持单集群下跨 Bucket Flux Join。 |  |
| 无数据告警 | 支持。 | 不支持。 |  |
| 告警恢复 | 支持。 | 不支持。 |  |
| 标签与标注 | 支持。 | 支持设置简单的标签。 |  |
| 动态严重度 | 支持。 | 支持。 |  |
| 分组评估 | 支持，可自定义配置。 | 不支持。 |  |
| 监控侧控制 | 支持配置持续触发阈值。 支持暂停和自动恢复（基于时间）监控。 | 不支持。 |  |
| 告警管理 | 告警管理 | 支持告警去重、合并、抑制、静默。 支持事务管理、责任人设置。 | 仅支持告警抑制，其他不支持。 |
| 通知管理 | 通知管理 | 支持通知渠道动态分派、告警级别提升、接收组管理、渠道日历设置、值班表设置、渠道额度控制。 | 仅支持通知渠道动态分派，其他不支持。 |
| 常用渠道 | 支持短信、语音、钉钉、邮件、WebHook、阿里云消息中心等通知渠道。 其中通过 WebHook，还支持企业微信、飞书、Slack 等渠道。 | 支持邮件、WebHook（不支持灵活自定义 Body）、exec、PagerDuty、PushOver、Slack、OpsGenie、VictorOps、HipChat 等通知渠道。不支持短信、语音服务。 |  |
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
