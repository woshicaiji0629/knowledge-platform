# 监控项指标数据查询详情-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/user-guide/resource-monitoring

# 资源监控
资源监控基于客户端IP地址的归属区域或运营商，统计流量带宽、访问请求数、缓存命中率以及HTTP状态码等数据。通过对CDN资源的监控，您可以全面了解带宽使用情况以及缓存命中率等关键指标，从而进行优化和调整。
## 功能介绍
资源监控和实时监控相比，资源监控的单次查询最大时间和可查询历史数据时间范围更大，详情请参见下方报表。
### 支持查询的时间粒度
通过控制台查询数据和调用相关API接口查询时，单次查询的最大时间跨度和可查询历史数据时间范围存在区别。不同时间粒度对应的单次查询的最大时间跨度、可查询的历史数据时间范围和数据延迟关系如下：
通过控制台查询：
| 时间粒度 | 单次查询的最大时间跨度 | 可查询历史数据时间范围 | 数据延迟 |
| --- | --- | --- | --- |
| 5 分钟 | 3 天 | 90 天 | 15 分钟 |
| 1 小时 | 31 天 | 90 天 | 4 小时 |
| 1 天 | 90 天 | 90 天 | 次日凌晨 4 点 |
调用相关API接口查询：
| 时间粒度 | 单次查询的最大时间跨度 | 可查询历史数据时间范围 | 数据延迟 |
| --- | --- | --- | --- |
| 5 分钟 | 3 天 | 93 天 | 15 分钟 |
| 1 小时 | 31 天 | 186 天 | 4 小时 |
| 1 天 | 366 天 | 366 天 | 次日凌晨 4 点 |
### 监控项和监控指标
资源监控功能包含了下表中的六个监控项，您可以选择需要监控的域名、区域、运营商等，在线查看各监控项和监控指标的具体情况，也可以将查询结果下载到本地查看及分析。
说明
资源监控以客户端IP地址所在地区或者运营商归属来统计数据，计量计费以统计各个计费大区的CDN节点上产生的流量、带宽数据和请求数来统计数据。由于统计方式不同，两者结果会有一定的差异。资源监控的曲线图主要用于带宽趋势的展示，如果您需要查询计费账单对应的计量数据，可通过[用量概述](resource-usage-overview.md)查看。
数据计算和统计源于API，如需查看更详细的信息，请参见下表中对应的API文档。
| 监控项 | 监控指标 | 相关 API |
| --- | --- | --- |
| 访问流量/带宽 | 展示加速域名的带宽和流量。 支持按区域、运营商和协议（HTTP、HTTPS、QUIC、IPv4 和 IPv6）查询。 | [查询带宽-按协议](../api-describedomainbpsdatabylayer.md) [查询用量-按天](../api-describedomainsusagebyday.md) |
| 回源流量/带宽 | 展示加速域名的回源带宽和回源流量。 说明 回源宽带：指当用户请求的资源在 CDN 节点未命中时，CDN 节点向源站请求资源所消耗的网络带宽。 回源流量：指当 CDN 节点无法从本地缓存中获取用户请求的内容时，需要向源服务器请求数据的流量。 | [查询回源带宽](../api-describedomainsrcbpsdata-2.md) [查询回源流量](../api-describedomainsrctrafficdata.md) |
| 访问请求数 | 展示加速域名的请求次数和 QPS。 支持按区域、运营商和协议（HTTP、HTTPS、QUIC、IPv4 和 IPv6）查询。 说明 加速域名的请求次数指最小时间粒度内的请求数总和（例如最小时间粒度为 5 分钟，那么展示的加速域名请求次数指 5 分钟内的请求数总和）。 QPS 指的是每秒的请求次数。 | [查询](../api-describedomainqpsdatabylayer.md) [QPS-按协议](../api-describedomainqpsdatabylayer.md) |
| 命中率 | 展示加速域名的字节命中率和请求命中率。 说明 字节命中率：单位时间内 CDN 节点响应用户的总字节数中，CDN 节点直接响应（非回源）的字节数占比。计算公式为：（CDN 节点响应用户的总字节数 - 源站响应 CDN 节点的总字节数）÷ CDN 节点响应用户的总字节数。 命中率：单位时间内所有请求（包含 HTTP 协议和 HTTPS 协议）的字节命中率。 HTTPS 命中率：单位时间内 HTTPS 请求的字节命中率。 | [查询字节命中率](../api-describedomainhitratedata.md) [查询请求命中率](../api-describedomainreqhitratedata.md) |
| HTTPCODE | 展示加速域名的 HTTP 状态码信息，支持按照 2xx、3xx、4xx 和 5xx 维度查询。参考 [HTTP](../developer-reference/http-status-code-description.md) [状态码](../developer-reference/http-status-code-description.md) 查看状态码详细说明和解决措施。 2xx 成功 - 边缘响应 ：表示客户端访问阿里云 CDN 节点时，请求已被服务器成功处理，并返回了相应的资源或确认信息。 4xx 客户端错误 - 边缘响应 ：表示客户端访问阿里云 CDN 节点时，由于客户端发送的请求有问题（例如，权限不足），阿里云 CDN 节点无法处理，请修改客户端请求内容后重新发送。 5xx 服务器错误 - 边缘响应 ：表示客户端访问阿里云 CDN 节点时，阿里云 CDN 节点的服务器出现了内部错误（例如，阿里云 CDN 节点负载过高），请检查源站配置（例如，源站的网络设置）。 | [查询](../api-describedomainhttpcodedatabylayer.md) [HTTP](../api-describedomainhttpcodedatabylayer.md) [状态码-按协议](../api-describedomainhttpcodedatabylayer.md) |
| 回源 HTTPCODE | 展示加速域名的回源 HTTP 状态码信息，支持按照 2xx、3xx、4xx 和 5xx 维度查询。参考 [HTTP](../developer-reference/http-status-code-description.md) [状态码](../developer-reference/http-status-code-description.md) 查看状态码详细说明和解决措施。 4xx 客户端错误 - 回源响应 ：表示阿里云 CDN 节点访问源站时，由于阿里云 CDN 节点发送的请求有问题（例如，请求的资源不存在），源站服务器无法处理，请修改客户端请求内容或调整 CDN 域名配置后重新发送。 5xx 服务器错误 - 回源响应 ：表示阿里云 CDN 节点访问源站时，源站服务器出现了内部错误（例如：源站服务器负载过高），请检查源站配置（例如，源站的服务器负载）。 | [查询回源](../api-describedomainsrchttpcodedata.md) [HTTP](../api-describedomainsrchttpcodedata.md) [状态码](../api-describedomainsrchttpcodedata.md) |
## 注意事项
通过CDN/DCDN控制台（或者OpenAPI）的监控查询、用量查询（实际计费流量）功能查到的加速域名使用的流量数据与通过日志统计的流量数据有差异。通常来说，通过监控查询、用量查询功能查到的加速域名使用的流量数据是通过日志统计的流量数据的1.1倍，详细请参见[为什么监控查询流量、用量查询流量与日志统计流量有差异](../product-overview/traffic-amount-in-the-monitoring-and-usage-analytics-or-in-the-usage-statistics-feature-different-from-the-logged-traffic-amount.md)。
## 用量查询、资源监控、实时监控在数据统计维度上的区别
用量查询：按CDN节点维度来统计用量数据，每个CDN节点都唯一归属于某个计费大区，因此用量查询只能按计费大区来查询用量数据，例如，中国内地、亚太1区、北美区等。具体内容请参见[用量查询](query-resource-usage-1.md)。
资源监控和实时监控：按客户端IP维度来统计监控数据，每个客户端IP都唯一归属于某个区域或者某个运营商，因此资源监控和实时监控只能按区域或者运营商（可以使用区域+运营商的组合）来查询监控数据。具体内容请参见[资源监控](resource-monitoring.md)和[实时监控](real-time-monitoring.md)。
## 资源监控和实时监控的区别
最低数据延迟：实时监控可以查询到延迟更低的数据。在实时监控下，当数据查询粒度为1分钟时，数据延迟约为5分钟；而资源监控只能在数据查询粒度为5分钟的情况下，将数据延迟控制在约15分钟左右。
最小数据粒度：实时监控可以查询到更小颗粒度的数据。实时监控可以查询的最小数据颗粒度为1分钟，而资源监控支持查询的最小数据颗粒度为5分钟。
可查询协议层：资源监控可以按更多的细分协议层来查询数据。资源监控支持按HTTP、HTTPS、QUIC、IPv4、IPv6这五种协议层来查询数据，而实时监控不支持。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，选择监控查询>资源监控。
在资源监控页面，选择您要查看的监控项和查询条件，单击查询。
系统会根据您选择的监控项和查询条件，显示查询结果。您可以在线分析查询结果，也可以将查询结果下载到本地进行分析。
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
