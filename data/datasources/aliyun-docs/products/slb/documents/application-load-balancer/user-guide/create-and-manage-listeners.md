# 创建和管理ALB监听-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/user-guide/create-and-manage-listeners

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/slb/documents/application-load-balancer/product-overview.md)

- [快速入门](products/slb/documents/application-load-balancer/getting-started.md)

- [操作指南](products/slb/documents/application-load-balancer/user-guide.md)

- [实践教程](products/slb/documents/application-load-balancer/use-cases.md)

- [开发参考](products/slb/documents/application-load-balancer/developer-reference.md)

- [服务支持](products/slb/documents/application-load-balancer/support.md)

[首页](https://help.aliyun.com/zh)

# 创建和管理监听

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/slb)

[我的收藏](https://help.aliyun.com/my_favorites.html)

监听是用于检查连接请求的过程。用户可以根据业务需求为ALB实例创建监听来转发客户端请求，并对监听进行修改、启停、删除等管理操作。

## 监听协议选型

创建监听前，建议根据业务需求选择合适的监听协议。ALB支持HTTP、HTTPS和QUIC三种七层监听协议，不同协议的适用场景和配置要求如下表所示。

| 协议 | 适用场景 | 是否需要 SSL 证书 | 支持的后端协议 | 特性 |
| --- | --- | --- | --- | --- |
| HTTP | 需要对数据内容进行识别的应用，如 Web 应用、手机小游戏等。 | 否 | HTTP、HTTPS | 默认支持 WebSocket 协议。 |
| HTTPS | 需要加密传输的应用。支持在 ALB 实例与客户端之间建立 SSL/TLS 加密会话。 | 是（服务器证书必选，CA 证书双向认证时必选） | HTTP、HTTPS、gRPC（需开启 HTTP 2.0） | 支持 HTTP 2.0、双向认证（CA 证书）、TLS 安全策略、QUIC 协议升级。默认支持 WebSocket Secure（WSS）协议。 |
| QUIC | 网络信号较弱、频繁切换 Wi-Fi 和移动网络等场景。可有效解决网络、视频卡顿问题，提升音视频资源访问效率，同时保障数据传输安全性。 | 是（服务器证书必选） | HTTP | 基于 UDP 传输，连接建立更快，支持连接迁移（网络切换不断连）。可单独使用或与 HTTPS 监听联合使用。 |


了解QUIC协议

QUIC协议介绍

QUIC协议又被称为快速UDP互联网连接协议，提供与SSL相同的安全性，同时具备多路复用等多种优势，具有较好的弱网性能，在丢包和网络延迟严重的情况下仍可提供可用的服务。QUIC协议在应用程序层面可以实现不同的拥塞控制算法，不需要操作系统和内核支持，相比于传统的TCP协议，拥有了更高的改造灵活性，适合用于在TCP协议优化遇到瓶颈的业务。

随着短视频、直播等新兴业务的飞速发展，流媒体传输对于带宽和延迟提出了双重要求，QUIC协议可以有效解决网络、视频卡顿的问题，提升音视频资源的访问效率，同时保障数据传输的安全性。

支持的QUIC协议类型

ALB支持gQUIC和iQUIC。HTTP/3协议是以iQUIC协议为基础构建的应用层协议，它主要依赖iQUIC来实现多路复用、拥塞控制、损失检测和重新传输等功能。HTTP/3协议可以更快地启动客户端连接，消除了多路复用流中的队头阻塞，并且支持客户端IP地址更改时的连接迁移。

- 

ALB支持的gQUIC协议版本有Q46、Q43、Q39，对应的Chrome浏览器版本为Chrome 74-81。

- 

ALB支持的HTTP/3协议版本为h3，对应的Chrome浏览器版本为Chrome 87及以上。

QUIC监听使用场景

| 场景 | 说明 |
| --- | --- |
| QUIC 监听单独使用 | 要求客户端都支持 HTTP/3 协议 |
| QUIC 监听与 HTTPS 监听联合使用 | 客户端暂未全量支持 HTTP/3 协议时，ALB 会根据客户端情况自动协商，优先使用 HTTP/3。协商不成功时，会回退为使用 HTTPS 或 HTTP/2。 |


## 前提条件

- 

已[创建](products/slb/documents/application-load-balancer/user-guide/create-and-manage-alb-instances.md)[ALB](products/slb/documents/application-load-balancer/user-guide/create-and-manage-alb-instances.md)[实例](products/slb/documents/application-load-balancer/user-guide/create-and-manage-alb-instances.md)和[服务器组](products/slb/documents/application-load-balancer/user-guide/create-and-manage-a-server-group.md)。

- 

如需创建HTTPS或QUIC监听，请确保已在证书中心购买或上传服务器证书。更多信息，请参见[管理证书](products/slb/documents/application-load-balancer/user-guide/manage-certificates.md)。

## 创建监听

ALB支持以下两种方式创建监听：

- 

创建监听：通过配置向导逐步完成，支持自定义高级配置。

- 

快速创建监听：只需配置监听协议、监听端口和服务器组（HTTPS/QUIC还需配置服务器证书，HTTPS还需选择TLS安全策略）。

### 控制台

步骤一：配置监听

- 

前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击目标实例ID，在监听页签下单击创建监听。

- 

在配置监听配置向导，完成以下配置，然后单击下一步。

- 

选择监听协议：HTTP、HTTPS或QUIC。

- 

监听端口：端口范围为1~65535。通常HTTP使用80端口，HTTPS使用443端口。

同一个ALB实例内，相同协议的监听端口不能重复。此外，HTTP和HTTPS监听也不能使用相同端口。

- 

监听名称：输入监听的自定义名称。

- 

标签：以键值对形式标记监听。

- 

高级配置：单击修改展开。

- 

启用HTTP2.0：仅HTTPS监听支持。

- 

连接空闲超时时间：取值范围1~600秒，默认15秒。超时后连接将被断开。如需提升最大超时时间，请前往[配额中心](https://quotas.console.aliyun.com/products/alb/quotas?query=alb_quota_max_idle_timeout)申请。

当监听协议为HTTP时，连接空闲超时时间对HTTP 2.0请求暂不生效。

- 

连接请求超时时间：取值范围1~600秒，默认60秒。超时后返回HTTP 504错误码。如需提升最大超时时间，请前往[配额中心](https://quotas.console.aliyun.com/products/alb/quotas?query=alb_quota_max_request_timeout)申请。

- 

数据压缩：开启后对响应内容进行压缩，仅当Content-Length超过1024字节时触发。支持Brotli（所有类型）和Gzip（压缩级别为 Level 4），客户端同时支持时优先使用Brotli。

Gzip支持的类型：text/xml、text/plain、text/css、application/javascript、application/x-javascript、application/rss+xml、application/atom+xml、application/xml、application/json。

- 

查找真实客户端源IP：开启后，ALB从X-Forwarded-For头字段中提取真实客户端IP。需设置可信IP列表：

- 

0.0.0.0/0：取X-Forwarded-For中最左边的地址。

- 

proxy1 IP;proxy2 IP;..：从右往左取第一个不在列表中的值。

开启后，转发规则中基于SourceIp匹配和QPS(基于客户端源IP限速)将使用真实客户端IP。

QUIC监听不支持此配置项。仅标准版、WAF增强版实例支持，基础版不支持。

- 

附加HTTP头字段：选择要添加的HTTP头字段，用于获取客户端IP、监听协议、端口等信息。各头字段的详细说明，请参见[HTTP](products/slb/documents/application-load-balancer/user-guide/http-headers.md)[头字段](products/slb/documents/application-load-balancer/user-guide/http-headers.md)。

- 

开启QUIC升级：适用于HTTPS监听与QUIC监听联合使用的场景。在关联的QUIC监听中选择已创建的QUIC监听。开启后，ALB会向客户端通告HTTP/3协议，支持HTTP/3的客户端将优先通过QUIC监听访问，不支持时自动回退为HTTPS。

仅HTTPS监听支持此配置项。

步骤二：配置SSL证书（仅HTTPS/QUIC监听）

| 证书 | 说明 | 单向认证是否需要 | 双向认证是否需要 |
| --- | --- | --- | --- |
| 服务器证书 | 证明服务器身份，由客户端校验是否受信。更多信息，请参见 [什么是](https://help.aliyun.com/zh/ssl-certificate/what-is-an-ssl-certificate#concept-yz4-v2p-ydb) [SSL](https://help.aliyun.com/zh/ssl-certificate/what-is-an-ssl-certificate#concept-yz4-v2p-ydb) [证书](https://help.aliyun.com/zh/ssl-certificate/what-is-an-ssl-certificate#concept-yz4-v2p-ydb) 。 | 是 | 是 |
| CA 证书 | 服务器用 CA 证书验证客户端证书的签名，未通过则拒绝连接。 | 否 | 是 |


- 

新证书应用后通常一到三分钟生效。

- 

QUIC监听仅需配置服务器证书，不支持双向认证。

- 

如需多域名访问或挂载多个服务器证书，可为监听[添加扩展证书](products/slb/documents/application-load-balancer/use-cases/configure-an-alb-instance-to-serve-multiple-domain-names-over-https.md)。

- 

在配置SSL证书配置向导，选择服务器证书。

如果没有可选的服务器证书，可单击创建SSL证书进入证书中心，在证书中心[购买](https://help.aliyun.com/zh/ssl-certificate/purchase-an-ssl-certificate#task-q3j-zfp-ydb)或[上传](https://help.aliyun.com/zh/ssl-certificate/upload-an-ssl-certificate)服务器证书。

- 

仅HTTPS监听：选择TLS安全策略。

系统提供多种预定义策略可直接选用。如需自定义TLS协议版本和加密算法套件，可单击创建 TLS 安全策略并创建自定义策略。更多信息，请参见[TLS](products/slb/documents/application-load-balancer/user-guide/tls-security-policies.md)[安全策略](products/slb/documents/application-load-balancer/user-guide/tls-security-policies.md)。

- 

仅HTTPS监听（可选）：打开启用双向认证，选择CA证书来源并选择CA证书。

- 

选择CA证书来源为阿里云签发，在选择默认CA证书下拉框中选择CA证书。如果没有可选的CA证书，可单击购买CA证书以[创建新](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468)[CA](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468)[证书](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468)。

- 

选择CA证书来源为非阿里云签发，在选择默认CA证书下拉框中选择CA证书。如果没有可选的CA证书，可单击上传自签CA证书，通过证书应用仓库[上传自签名](https://help.aliyun.com/zh/ssl-certificate/create-and-manage-a-certificate-application-repository)[CA](https://help.aliyun.com/zh/ssl-certificate/create-and-manage-a-certificate-application-repository)[证书](https://help.aliyun.com/zh/ssl-certificate/create-and-manage-a-certificate-application-repository)。

仅标准版和WAF增强版实例支持双向认证，基础版不支持。

步骤三：选择服务器组

在选择服务器组配置向导，选择服务器组，并查看后端服务器信息，然后单击下一步。

步骤四：配置审核

在配置审核页面，确认配置信息，单击提交。

快速创建监听

- 

前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击目标实例ID，在监听页签下单击快速创建监听。

- 

在快速创建监听对话框中，完成以下参数的配置，然后单击确定。

- 

选择监听协议：HTTP、HTTPS或QUIC。

- 

监听端口：端口范围为1~65535。通常HTTP使用80端口，HTTPS使用443端口。

- 

选择服务器证书（仅HTTPS和QUIC监听）：选择服务器证书。如果没有可选的服务器证书，可单击创建SSL证书进入证书中心，在证书中心[购买](https://help.aliyun.com/zh/ssl-certificate/purchase-an-ssl-certificate#task-q3j-zfp-ydb)或[上传](https://help.aliyun.com/zh/ssl-certificate/upload-an-ssl-certificate)服务器证书。

- 

TLS安全策略（仅HTTPS监听）：选择TLS安全策略。如需自定义TLS协议版本和加密算法套件，可单击创建 TLS 安全策略并创建自定义策略。更多信息，请参见[TLS](products/slb/documents/application-load-balancer/user-guide/tls-security-policies.md)[安全策略](products/slb/documents/application-load-balancer/user-guide/tls-security-policies.md)。

- 

转发的后端服务器组：选择后端服务器组类型和后端服务器。

### API

调用[CreateListener](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-createlistener.md)创建监听。

## 修改监听

监听协议和监听端口创建后不支持修改。如需更改，请删除监听后重新创建。

### 控制台

- 

前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击目标实例ID。

- 

单击监听页签，找到目标监听，选择以下一种方法，修改监听基本信息。

- 

单击目标监听ID或在操作列单击查看详情，进入监听详情页签，在监听基本信息区域单击编辑监听。

- 

在操作列选择>编辑监听。

- 

在编辑监听对话框中，修改监听名称或高级配置，然后单击保存。

### API

调用[UpdateListenerAttribute](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-updatelistenerattribute.md)更新监听的配置。

## 启动或停止监听

启动或停止监听时，监听会短暂进入配置中状态，在此期间无法对监听进行删除、编辑或更换服务器组等操作。

警告

停止监听会使访问中断，请谨慎操作。

### 控制台

- 

前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击目标实例ID。

- 

单击监听页签，找到目标监听，通过以下任一方式启动或停止监听：

- 

在操作列选择>启动或停止，在弹出的对话框中单击确定。

- 

单击目标监听ID，在监听详情页签右上角单击启动或停止。

### API

- 

调用[StartListener](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-startlistener.md)启动监听。

- 

调用[StopListener](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-stoplistener.md)停止监听。

## 更换服务器组

### 控制台

- 

前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击目标实例ID。

- 

单击监听页签，找到目标监听，选择以下一种方式更换服务器组。

- 

在操作列选择>更换服务器组（监听默认转发）。

- 

单击目标监听ID，在监听详情页签的服务器组（监听默认转发）区域，单击更换服务器组（监听默认转发）。

- 

在弹出的对话框中，选择需要更换的服务器组或在下拉框中单击创建服务器组以[创建新的服务器组](products/slb/documents/application-load-balancer/user-guide/create-and-manage-a-server-group.md)并选择，然后单击保存。

### API

调用[UpdateListenerAttribute](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-updatelistenerattribute.md)更新监听的配置（含更换服务器组）。

## 管理证书

### 控制台

- 

前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击目标实例ID，在监听页签找到目标HTTPS或QUIC监听，在操作列单击管理证书。

- 

在监听证书页面，可以更换服务器证书、添加或移除扩展证书等。具体操作，请参见[管理证书](products/slb/documents/application-load-balancer/user-guide/manage-certificates.md)。

### API

- 

调用[UpdateListenerAttribute](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-updatelistenerattribute.md)更新监听的证书配置。

- 

调用[AssociateAdditionalCertificatesWithListener](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-associateadditionalcertificateswithlistener.md)为监听添加扩展证书。

- 

调用[DissociateAdditionalCertificatesFromListener](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-dissociateadditionalcertificatesfromlistener.md)从监听移除扩展证书。

## 修改TLS安全策略（仅HTTPS监听）

### 控制台

- 

前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击目标实例ID，在监听页签找到目标HTTPS监听，单击监听ID进入监听详情页。

- 

在监听详情页签，找到SSL 证书区域，在TLS 安全策略右侧单击图标。

- 

在弹出的编辑 TLS 安全策略对话框中，选择TLS安全策略，然后单击保存。

系统提供多种预定义策略可直接选用。如需自定义TLS协议版本和加密算法套件，可单击创建 TLS 安全策略并创建自定义策略。更多信息，请参见[TLS](products/slb/documents/network-load-balancer/user-guide/tls-security-policy.md)[安全策略](products/slb/documents/network-load-balancer/user-guide/tls-security-policy.md)。

### API

调用[UpdateListenerAttribute](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-updatelistenerattribute.md)更新监听的配置，通过SecurityPolicyId参数指定TLS安全策略。

## 管理链路追踪

仅标准版和WAF增强版的ALB实例支持链路追踪。链路追踪的详细说明和开启指导，请参见[通过](products/slb/documents/application-load-balancer/use-cases/untitled-document-1698045154408.md)[ALB](products/slb/documents/application-load-balancer/use-cases/untitled-document-1698045154408.md)[链路追踪实现业务全链路分析](products/slb/documents/application-load-balancer/use-cases/untitled-document-1698045154408.md)。

开启链路追踪后，会产生可观测链路 OpenTelemetry 版和日志服务相关费用。

- 

前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击目标实例ID，在监听页签找到目标监听，单击监听ID。

- 

在监听详情页签的链路追踪区域，根据需要进行如下操作。

| 操作 | 说明 |
| --- | --- |
| 开启链路追踪 | 开启 链路追踪 开关，在 开启链路追踪 对话框中配置参数后单击 保存 。 |
| 编辑链路追踪 | 单击 编辑链路追踪 ，在对话框中修改 采样率 后单击 保存 。 |
| 关闭链路追踪 | 关闭 链路追踪 开关，在 关闭链路追踪 对话框中单击 确定 。 |
| 查看链路追踪 | 在 调用链分析 右侧单击 查看 ，前往可观测链路 OpenTelemetry 版控制台查看请求数据。更多信息，请参见 [调用链分析](https://help.aliyun.com/zh/opentelemetry/user-guide/analyze-traces) 。 |


## 删除监听

### 控制台

- 

前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击目标实例ID，在监听页签找到目标监听，在操作列选择>删除。

- 

在弹出的对话框中，单击确定。

### API

调用[DeleteListener](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-deletelistener.md)删除监听。

## 计费

监听没有独立的计费项，但监听的流量和规则配置会影响LCU费用。ALB实例的计费规则请参见[ALB](products/slb/documents/application-load-balancer/product-overview/alb-billing-rules.md)[计费说明](products/slb/documents/application-load-balancer/product-overview/alb-billing-rules.md)。

## 配额

| 配额名称 | 描述 | 默认值 | 最大支持提升至 | 是否支持申请 |
| --- | --- | --- | --- | --- |
| alb_quota_loadbalancer_listeners_num_basic_edition | 一个基础版 ALB 实例可添加的监听数 | 50 个 | 80 个 | [是](https://quotas.console.aliyun.com/products/alb/quotas?query=alb_quota_loadbalancer_listeners_num) |
| alb_quota_loadbalancer_listeners_num_standard_edition | 一个标准版 ALB 实例可添加的监听数 | 50 个 | 100 个 |  |
| alb_quota_loadbalancer_listeners_num_standardwithwaf_edition | 一个 WAF 增强版 ALB 实例可添加的监听数 | 50 个 | 100 个 |  |
| alb_quota_max_idle_timeout | 创建监听时连接空闲最大超时时间 | 600 秒 | 3600 秒 |  |
| alb_quota_max_request_timeout | 创建监听时连接请求最大超时时间 | 600 秒 | 3600 秒 |  |


仅[ALB](products/slb/documents/product-overview/alb.md)[升级实例](products/slb/documents/product-overview/alb.md)支持将alb_quota_max_request_timeout和alb_quota_max_idle_timeout配额提升至最大3600秒；未升级实例仅支持提升至最大900秒。

[上一篇：ALB监听](products/slb/documents/application-load-balancer/user-guide/listeners-1.md)[下一篇：配置监听转发规则](products/slb/documents/application-load-balancer/user-guide/manage-forwarding-rules-for-a-listener.md)

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
