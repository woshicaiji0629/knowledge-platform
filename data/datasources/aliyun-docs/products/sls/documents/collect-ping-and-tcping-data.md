# 如何通过Logtail采集ping和tcping数据到日志服务-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/collect-ping-and-tcping-data

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

# 采集ping和tcping数据

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍通过Logtail采集ping和tcping数据到日志服务Metricstore的操作步骤。

## 前提条件

已创建Project和MetricStore。具体操作，请参见[管理](products/sls/documents/manage-a-project.md)[Project](products/sls/documents/manage-a-project.md)和[创建](products/sls/documents/manage-a-metricstore.md)[MetricStore](products/sls/documents/manage-a-metricstore.md)。

## 使用限制

只有Linux Logtail 1.0.31及以上版本的Logtail支持采集ping和tcping数据。如果您已在服务器上安装旧版本的Logtail，需先升级。具体操作，请参见[安装](products/sls/documents/install-logtail-on-a-linux-server.md)[Logtail（Linux](products/sls/documents/install-logtail-on-a-linux-server.md)[系统）](products/sls/documents/install-logtail-on-a-linux-server.md)。

## 操作步骤

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在时序存储>时序库页签中，在目标MetricStore下面选择数据接入>logtail配置，然后在右侧页面单击添加Logtail配置。

- 

在快速数据接入对话框中，单击Ping 监控。

- 

在创建机器组页签中。

- 

如果已有可用的机器组，请单击使用现有机器组。

- 

如果您还没有可用的机器组，请执行以下操作（以ECS为例）。

- 

在ECS机器页签中，通过手动选择实例方式选择目标ECS实例，单击创建。

具体操作，请参见[安装](products/sls/documents/install-logtail-on-ecs-instances.md)[Logtail（ECS](products/sls/documents/install-logtail-on-ecs-instances.md)[实例）](products/sls/documents/install-logtail-on-ecs-instances.md)。

重要

如果您的服务器是与日志服务属于不同账号的ECS、其他云厂商的服务器和自建IDC时，您需要手动安装Logtail。具体操作，请参见[安装](products/sls/documents/install-logtail-on-a-linux-server.md)[Logtail（Linux](products/sls/documents/install-logtail-on-a-linux-server.md)[系统）](products/sls/documents/install-logtail-on-a-linux-server.md)。手动安装Logtail后，您必须在该服务器上手动配置用户标识。具体操作，请参见[配置用户标识](products/sls/documents/configure-a-user-identifier.md)。

- 

安装完成后，单击确认安装完毕。

- 

在创建机器组页面，输入名称，单击下一步。

日志服务支持创建IP地址机器组和用户自定义标识机器组，具体操作，请参见[创建机器组](products/sls/documents/manage-machine-groups.md)。

- 

确认目标机器组已在应用机器组区域，单击下一步。

重要

创建机器组后立刻应用，可能因为连接未生效，导致心跳为FAIL，您可单击自动重试。如果还未解决，请参见[Logtail](products/sls/documents/troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组无心跳](products/sls/documents/troubleshoot-the-errors-related-to-logtail-machine-groups.md)进行排查。

- 

在数据源设置页签中，设置配置名称和插件配置，然后单击下一步。

重要

inputs为数据源配置，必选项。一个inputs中只允许配置一个类型的数据源。

{{ "inputs": [ { "detail": { "tcp": [ { "port": 80, "src": "192.XX.XX.103", "count": 3, "target": "www.aliyun.com" } ], "interval_seconds": 60, "icmp": [ { "src": "192.XX.XX.103", "count": 3, "target": "www.aliyun.com" } ], "http": [ { "src": "192.XX.XX.103", "expect_code": 200, "target": "www.aliyun.com" } ] }, "type": "metric_input_netping" } ] }

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

| 参数 | 类型 | 是否必选 | 参数说明 |
| --- | --- | --- | --- |
| tcp | array | 是 | 采集 TCP ping 数据。详细参数说明如下，参数值需根据实际值替换。 port ：端口号。 src ：执行 ping 命令的服务器的 IP 地址。即由 src 字段决定在机器组的哪台机器中执行 ping 命令。 count ：限制执行一次 ping 命令发送的数据包数量。建议使用默认值 3，取值范围为(0,10)。 target ：目标主机名或 IP 地址。即由 target 字段决定 ping 的目标主机名或 IP 地址。 name ：名称，默认为{src}->{target}。 labels ：标签，支持增加指标标签。 支持添加多个 IP 地址，示例如下： "tcp": [ { "port": 80, "src": "192.XX.XX.103", "count": 3, "target": "www.aliyun.com" }, { "port": 80, "src": "192.XX.XX.104", "count": 3, "target": "www.aliyun.com" } ] |
| icmp | array | 是 | 采集 ICMP ping 数据。详细参数说明如下，参数值需根据实际值替换。 src ：执行 ping 命令的服务器的 IP 地址。即由 src 字段决定在机器组的哪台机器中执行 ping 命令。 count ：限制执行一次 ping 命令发送的数据包数量。建议使用默认值 3，取值范围为(0,10)。 target ：目标的主机名或 IP 地址。即由 target 字段决定 ping 的目标主机名或 IP 地址。 name ：名称，默认为{src}->{target}。 labels ：标签，支持增加指标标签。 支持添加多个 IP 地址，示例如下： "icmp": [ { "src": "192.XX.XX.103", "count": 3, "target": "www.aliyun.com" }, { "src": "192.XX.XX.104", "count": 3, "target": "www.aliyun.com" } ] |
| http | array | 是 | 采集 HTTP ping 数据。详细参数说明如下，参数值需根据实际值替换。 src ：执行 ping 命令的服务器的 IP 地址。即由 src 字段决定在机器组的哪台机器中执行 ping 命令。 method ：执行请求的 http method，默认 get。 expect_response_contains ： 预期结果包含内容。 expect_code ：预期状态码。 target ：目的地址，支持 https。 name ：名称，默认为{src}->{target}。 labels ：标签，支持增加指标标签。 "http": [ { "src": "192.XX.XX.103", "expect_code": 200, "target": "www.aliyun.com" } ] |
| interval_seconds | int | 是 | 执行 ping 命令的时间间隔，单位：秒。 默认值：60。 取值范围：[10, 86400) |
| type | string | 是 | 数据源类型，固定为 metric_input_netping。 |


## 后续步骤

采集ping数据后，您可以在Metricstore中进行查询分析。具体操作，请参见[查询和分析时序数据](products/sls/documents/query-and-analyze-metric-data.md)。在日志服务SLS的查询分析页面中，可通过PromQL查询相关指标，并以折线图形式展示ping延迟数据的变化趋势。

相关指标说明如下表所示。

| 分类 | 指标名 | 说明 |
| --- | --- | --- |
| ICMP ping | ping_failed | 单次执行 icmp ping 命令，发送失败的数据包数量。 |
| ping_rtt_avg_ms | 单次执行 icmp ping 命令的平均响应时间，单位：毫秒。 |  |
| ping_rtt_max_ms | 单次执行 icmp ping 命令的最大响应时间，单位：毫秒。 |  |
| ping_rtt_min_ms | 单次执行 icmp ping 命令的最小响应时间，单位：毫秒。 |  |
| ping_rtt_stddev_ms | 单次执行 icmp ping 命令的标准差时间，单位：毫秒。 |  |
| ping_rtt_total_ms | 单次执行 icmp ping 命令的总响应时间，单位：毫秒。 |  |
| ping_succcess | 单次执行 icmp ping 命令，发送成功的数据包数量。 |  |
| ping_total | 单次执行 icmp ping 命令，发送的数据包总数。 |  |
| TCP ping | tcping_failed | 单次执行 tcp ping 命令，发送失败的数据包数量。 |
| tcping_rtt_avg_ms | 单次执行 tcp ping 命令的平均响应时间，单位：毫秒。 |  |
| tcping_rtt_max_ms | 单次执行 tcp ping 命令的最大响应时间，单位：毫秒。 |  |
| tcping_rtt_min_ms | 单次执行 tcp ping 命令的最小响应时间，单位：毫秒。 |  |
| tcpping_rtt_stddev_ms | 单次执行 tcp ping 命令的标准差时间，单位：毫秒。 |  |
| tcping_rtt_total_ms | 单次执行 tcp ping 命令的总响应时间，单位：毫秒。 |  |
| tcping_succcess | 单次执行 tcp ping 命令，发送成功的数据包数量。 |  |
| tcping_total | 单次执行 tcp ping 命令，发送的数据包总数。 |  |
| HTTP ping | httping_failed | 单次执行 http ping 命令，发送失败的数量。 |
| httping_succcess | 单次执行 http ping 命令，发送成功的数量。 |  |
| httping_total | 单次执行 http ping 命令，发送的总数。 |  |
| httping_rt_ms | 单次执行 http ping 命令延迟，单位：毫秒。 |  |
| httping_response_bytes | 单次执行 http ping 命令响应值大小，单位：Byte。 |  |
| httping_cert_ttl_days | 单次执行 http ping 命令证书过期时间，单位：Day。 |  |


[上一篇：采集Open-Falcon数据](products/sls/documents/collect-metric-data-from-open-falcon.md)[下一篇：使用Prometheus采集Kubernetes监控数据](products/sls/documents/use-prometheus-to-collect-kubernetes-metric-data.md)

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
