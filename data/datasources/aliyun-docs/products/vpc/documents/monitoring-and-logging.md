# 网络监控审计与诊断排查-专有网络VPC-阿里云

Source: https://help.aliyun.com/zh/vpc/monitoring-and-logging

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/vpc/documents/vpc-user-guide.md)

- [开发参考](products/vpc/documents/developer-reference.md)

- [产品计费](products/vpc/documents/product-billing.md)

- [常见问题](products/vpc/documents/troubleshooting.md)

- [动态与公告](products/vpc/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 监控与日志

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

阿里云提供了各种监控与日志审计相关的服务，例如云监控、配置审计等，帮助实时监控专有网络VPC中资源的使用情况和业务运行状况，并在收到异常报警时及时响应，有效保障专有网络VPC的可用性、业务的正常运行和健康度。

## 问题诊断排查

### 自助问题排查

VPC的[自助排查功能](https://vpc.console.aliyun.com/troubleshooting?product=VPC)可以排查VPC实例网络连通性问题、VPC与外部网络连接、费用问题及资源配额不足等问题，并提供解决建议。实例排查期间可能会对实例探测并进行诊断分析，但不会对实例配置和正常业务造成影响。

## 基础云监控

VPC 已接入阿里云基础云监控服务，可以免费使用，对各项指标进行实时监控。

### 监控指标阈值报警

使用云监控为VPC相关指标[创建阈值报警规则](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/create-an-alert-rule)。通过对监控项报警阈值进行监控，可以迅速得知监控数据异常并解决异常。

### 订阅阈值事件

当监控指标达到阈值报警条件时，云监控自动发送原始报警通知给报警联系人。订阅阈值事件，可以对报警通知进行定制化处理：

- 

合并降噪：从阈值事件的订阅范围对报警进行合并，通过条件降噪来控制报警的有效性，避免大量重复报警造成报警风暴。

- 

合并降噪后的有效报警通知：云监控可以直接发送给报警联系人，如果报警在预定时间内未恢复，云监控自动将报警通知发送给下一个报警联系人组。

- 

自定义通知方式：可以按照习惯定义通知渠道的级别和模板，还可以通过推送与集成，直接将所有报警数据推送到轻量消息队列（原 MNS）、日志服务SLS、函数计算FC和Webhook。

可监控指标

| 产品 | 指标类型 | 可监控指标 |
| --- | --- | --- |
| [VPC 对等连接](https://cms.console.aliyun.com/metric-meta/acs_vpcpeer/vpcpeer) | 实例维度 | 周期内入方向流量、周期内出方向流量、网络限速丢包速率、入方向带宽、出方向带宽 |
| [IPAM 作用范围](https://cms.console.aliyun.com/metric-meta/acs_vpcipam/vpcipam_scope) | 实例维度 | 作用范围内合规 CIDR 数量、不合规 CIDR 数量、已忽略 CIDR 数量、托管 CIDR 数量、未托管 CIDR 数量、不重叠 CIDR 数量、重叠 CIDR 数量、子网 CIDR 数量、VPC CIDR 数量 |
| [IPAM 地址池](https://cms.console.aliyun.com/metric-meta/acs_vpcipam/vpcipam_pool) | 实例维度 | 池整体利用率、池分配子池利用率、池分配资源利用率，地址池内合规 CIDR 数量、不合规 CIDR 数量、重叠 CIDR 数量、不重叠 CIDR 数量 |
| [IPAM](https://cms.console.aliyun.com/metric-meta/acs_vpcipam/vpcipam_resource_vpc) [资源(VPC)](https://cms.console.aliyun.com/metric-meta/acs_vpcipam/vpcipam_resource_vpc) | 实例维度 | VPC 利用率、VPC IPv4 网段利用率、VPC IPv6 网段利用率 |
| [IPAM](https://cms.console.aliyun.com/metric-meta/acs_vpcipam/vpcipam_resource_vswitch) [资源(VSwitch)](https://cms.console.aliyun.com/metric-meta/acs_vpcipam/vpcipam_resource_vswitch) | 实例维度 | 子网利用率、子网 IPv4 网段利用率、子网 IPv6 网段利用率 |


## 健康状态监控

查看[阿里云健康看板](https://status.aliyun.com/)。实时了解云资源的健康状态，查看阿里云每个地域下云服务的状态是否有异常，以及该服务异常状态的RSS订阅方式，便于可及时处理异常情况。

## 云资源配置审计

VPC已接入阿里云配置审计供免费试用，提供统一的云资源配置历史追踪、配置合规审计，可以实现对云上资源合规性的自主监控，确保基础设施的持续合规性。

- 

资源配置检测：检测当前阿里云账号和所有RAM用户的操作记录，且默认每隔10分钟记录资源配置的变更。

- 

开启等保2.0云上预检功能：配置审计解读等保2.0法规条例，并对应实现为云上资源配置的检测。一键开启等保2.0云上预检功能，配置审计将持续监控资源的合规性。还可以下载预检报告，呈递检测机构报备。

- 

审计数据实时查询与分析：将云资源的配置变更历史和不合规事件数据[投递到日志服务](https://help.aliyun.com/zh/document_detail/179275.html)[SLS](https://help.aliyun.com/zh/document_detail/179275.html)[的指定日志库中](https://help.aliyun.com/zh/document_detail/179275.html)，实现通过日志服务SLS统一查询和分析日志数据。

## 云资源操作审计

VPC已接入阿里云操作审计，可提供统一的云资源操作日志管理，记录云账号下用户登录及资源访问操作，实现安全分析、入侵检测、资源变更追踪以及合规性审计。

- 

操作审计可记录通过阿里云控制台、OpenAPI、开发者工具访问和使用云上产品和服务的[日志数据](https://help.aliyun.com/zh/actiontrail/product-overview/audit-events-of-vpc)。

- 

默认追踪并记录最近90天的事件。如需保存更长时间的日志，则需要[创建跟踪](https://help.aliyun.com/zh/actiontrail/use-advanced-event-query-feature-to-query-events#section-uxh-m43-tqk)，将产生的时间记录到日志服务或对象存储OSS。

- 

将事件投递到SLS或OSS后，可以[通过](https://help.aliyun.com/zh/actiontrail/user-guide/query-events-in-the-log-service-or-oss-console)[SLS](https://help.aliyun.com/zh/actiontrail/user-guide/query-events-in-the-log-service-or-oss-console)[或](https://help.aliyun.com/zh/actiontrail/user-guide/query-events-in-the-log-service-or-oss-console)[OSS](https://help.aliyun.com/zh/actiontrail/user-guide/query-events-in-the-log-service-or-oss-console)[控制台查询事件](https://help.aliyun.com/zh/actiontrail/user-guide/query-events-in-the-log-service-or-oss-console)。

- 

[创建数据回补投递任务](https://help.aliyun.com/zh/actiontrail/user-guide/create-a-historical-event-delivery-task)可以跟踪历史事件，将跟踪历史投递到日志服务SLS。

## 流日志与流量镜像

[VPC](products/vpc/documents/vpc-flow-logs.md)[流日志](products/vpc/documents/vpc-flow-logs.md)采集并记录弹性网卡的进出流量信息，可以监控网络性能、排查网络故障或优化流量成本。

当需要监控网络流量时，传统方式为登录实例抓包或在实例部署监控Agent，占用实例的系统资源，影响业务性能。[VPC](products/vpc/documents/traffic-mirroring-overview.md)[流量镜像](products/vpc/documents/traffic-mirroring-overview.md)提供旁路监控方案，在不影响业务流量的前提下，将符合筛选条件的出入指定弹性网卡的流量复制并转发到安全分析设备，实现实时检测。

[上一篇：数据安全](products/vpc/documents/data-security.md)[下一篇：使用 PrivateLink 私网访问 VPC OpenAPI](products/vpc/documents/use-privatelink-to-access-vpc-openapi-over-private-network.md)

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
