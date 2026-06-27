# 静态资源边缘缓存就近分发-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/product-overview/what-is-alibaba-cloud-cdn

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/cdn/documents/product-overview.md)

- [快速入门](products/cdn/documents/getting-started.md)

- [操作指南](products/cdn/documents/user-guide.md)

- [实践教程](products/cdn/documents/use-cases.md)

- [安全合规](products/cdn/documents/security-and-compliance.md)

- [开发参考](products/cdn/documents/developer-reference.md)

- [服务支持](products/cdn/documents/support.md)

- [视频专区](products/cdn/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 什么是阿里云CDN

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

阿里云内容分发网络CDN（Content Delivery Network）是由遍布全球的边缘节点服务器群组成的分布式网络，将源站资源缓存到阿里云遍布全球的加速节点，当终端用户请求访问和获取源站资源时无需回源，可就近获取CDN节点上已经缓存的资源，提高资源访问速度，同时分担源站压力。

阿里云在全球拥有3200+节点。中国内地拥有2300+节点，覆盖31个省级区域；海外、中国香港、中国澳门拥有900+节点，覆盖70多个国家和地区。全网带宽输出能力达180 Tbps。主要节点分布请参见[节点分布](products/cdn/documents/product-overview/pop-distribution.md)。

CDN接入快捷、简单，您不需要调整现有业务结构，也不需要进行复杂的配置，只需要在CDN控制台进行简单操作，即可将域名接入阿里云，享受全球链路加速服务。通过[快速入门](products/cdn/documents/getting-started/getting-started.md)，您可以轻松开启CDN加速服务。

## 为什么选择阿里云CDN

使用可以帮您实现静态资源的加速和分发，提高资源访问速度：

- 

丰富的资源节点：为用户提供就近接入的同运营商CDN节点，解决长距离接入和跨运营商访问带来的延迟高和速度慢的问题。

- 

资源可弹性扩展：基于全球3200+节点，资源可弹性扩展，实现业务[高可用](https://www.aliyun.com/getting-started/what-is/what-is-high-availability)。

- 

精准的调度系统：实时获取CDN节点的健康状况，并根据用户所在位置和运营商来分配最佳接入节点，以便取得最佳接入效果。

- 

智能的传输链路：通过协议优化、连接优化等措施来降低总体时延、提高传输速度，尤其是提高弱网环境下的传输速度。

- 

高效的缓存策略：能够带来更高的缓存命中率，命中就近节点上的远程资源，提供高效的访问速度。

- 

降低您的IT成本：可将您的业务算力、带宽、连接数转移到CDN边缘节点，降低您的IT成本。

- 

强大的带宽输出能力：全网带宽输出能力达180 Tbps。

- 

提供行业通用标准[API](https://www.aliyun.com/getting-started/what-is/what-is-api)：提高易用性和适用性。

更多选择理由，请参见[阿里云](products/cdn/documents/product-overview/competitive-advantages-of-alibaba-cloud-cdn.md)[CDN](products/cdn/documents/product-overview/competitive-advantages-of-alibaba-cloud-cdn.md)[的五大竞争力](products/cdn/documents/product-overview/competitive-advantages-of-alibaba-cloud-cdn.md)。

## 加速原理

CDN接管域名解析，将用户请求智能地引导至最近的CDN节点，如果该最佳节点已[缓存](https://www.aliyun.com/getting-started/what-is/what-is-cache)该资源，当终端用户请求访问和获取源站资源时无需回源，从而实现加速。

假设您的加速域名为www.aliyundoc.com，接入CDN开始加速服务后，当终端用户在北京发起HTTP请求时，处理流程如下图所示。

- 

用户发起请求：当终端用户向www.aliyundoc.com下的指定资源发起请求时，首先向Local DNS（本地DNS）发起请求域名www.aliyundoc.com对应的IP。

- 

解析请求转发：Local DNS检查缓存中是否有www.aliyundoc.com的IP地址记录。如果有，则直接返回给终端用户；如果没有，则向网站授权DNS请求域名www.aliyundoc.com的解析记录。

- 

CNAME配置生效：当网站授权DNS解析www.aliyundoc.com后，返回域名的CNAMEwww.aliyundoc.com.example.com。

- 

智能调度：Local DNS向阿里云CDN的DNS调度系统请求域名www.aliyundoc.com.example.com的解析记录，阿里云CDN的DNS调度系统将为其分配最佳节点IP地址。

- 

返回最佳节点IP：Local DNS获取阿里云CDN的DNS调度系统返回的最佳节点IP地址。

- 

用户访问节点：Local DNS将最佳节点IP地址返回给用户，用户获取到最佳节点IP地址，向最佳节点IP地址发起对该资源的访问请求。

- 

节点响应：

- 

缓存命中：如果该最佳节点已缓存该资源，则会将请求的资源直接返回给用户（步骤8），此时请求结束。

- 

缓存未命中：如果该最佳节点未缓存该资源或者缓存的资源已经失效，则节点将会向源站发起对该资源的请求。获取源站资源后结合用户自定义配置的缓存策略，将资源缓存到CDN节点并返回给用户（步骤8），此时请求结束。配置缓存策略的操作方法，请参见[配置缓存过期时间](products/cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)。

## 产品架构

以下为阿里云CDN的产品架构图，由调度系统、链路质量系统、缓存系统和支撑系统这四大系统组成。

- 

链路质量系统

链路质量探测系统会实时监测缓存系统中的所有节点和链路的实时负载以及健康状况，并将结果反馈给调度系统，调度系统根据用户请求中携带的IP地址解析用户的运营商和区域归属，然后综合链路质量信息为用户分配一个最佳接入节点。

- 

调度系统

支持策略中心、[DNS](https://www.aliyun.com/getting-started/what-is/what-is-dns)、DNS-over-HTTPS (DoH)和302调度模式。当终端用户发起访问请求时，用户的访问请求会先进行域名DNS解析，然后通过阿里云CDN的调度系统处理用户的解析请求。

- 

缓存系统

用户通过收到的最佳接入节点访问对应的缓存节点，如果节点已经缓存了用户请求的资源，会直接将资源返回给用户；如果L1（边缘节点）和L2（汇聚节点）节点都没有缓存用户请求的资源，此时会返回源站去获取资源并缓存到缓存系统，供后续用户访问，避免重复回源。分级缓存的部署架构可提高内容分发效率、降低回源带宽以及提升用户体验。

- 

支撑服务系统

支撑服务系统包括天眼、数据智能和配置管理系统，分别具备了资源监测、数据分析和配置管理能力。

- 

资源监测：天眼可以对缓存系统上用户业务运行的状态进行监测。例如对CDN加速域名的QPS、带宽、HTTP状态码等常见指标的监控。

- 

数据分析：用户可以分析CDN加速域名的Top URL、PV、UV等数据。

- 

配置管理：通过配置管理系统，用户可以配置缓存文件类型、缓存时忽略查询参数等缓存规则，以提升缓存系统的运作效率。

## CDN计费

CDN的计费方式分为基础服务计费和增值服务计费：

- 

基础服务计费：包括按流量计费和按带宽峰值计费这两种计费模式，默认采用按流量计费模式。详细信息，请参见[基础服务计费](products/cdn/documents/product-overview/billing-rules-of-basic-services.md)。

- 

增值服务计费：增值服务计费项包括静态HTTPS请求数、静态QUIC请求数、实时日志推送数量等。详细信息，请参见[增值服务计费](products/cdn/documents/product-overview/billing-of-value-added-services.md)。

CDN计费详情，请参见[CDN](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.10.1b444ee22Dxy8y#/cdn/detail)[产品定价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.10.1b444ee22Dxy8y#/cdn/detail)。

了解CDN的计费方式后，您可以快速开通CDN服务。具体操作，请参见[开通](products/cdn/documents/activate-alibaba-cloud-cdn.md)[CDN](products/cdn/documents/activate-alibaba-cloud-cdn.md)[服务](products/cdn/documents/activate-alibaba-cloud-cdn.md)。

## CDN、DCDN、ESA的区别

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

- 

| 对比项 | CDN | 全站加速 DCDN | 边缘安全加速 ESA |
| --- | --- | --- | --- |
| 典型应用场景 | 手机 App 更新、游戏包更新、视频点播（长视频、短视频）、图文网站。 | 在线商城、在线支付、聊天互动、在线教育、全球对战游戏、金融理财。 | 包括但不限于游戏、电商、金融、零售行业等。 |
| 覆盖范围 | 仅中国内地 全球 全球（不包含中国内地） | 仅中国内地 全球 全球（不包含中国内地） | 仅中国内地 全球 全球（不包含中国内地） |
| 加速方式 | 以静态内容加速为主，适用于高带宽大流量场景，动态资源直接回源。 通过全球 3200+边缘节点，基于缓存策略存储您的业务内容。 基于源站 [负载均衡](https://www.aliyun.com/getting-started/what-is/what-is-load-balance) 、回源权重管理、回源流量卸载等技术控制回源流量，保护源站同时降低源站成本。 将服务器上的图片、视频等静态资源缓存在 CDN 边缘节点，供用户从最近的节点获取静态资源。 | 支持纯动态加速和动静态混合加速。 纯动态加速 针对 POST 请求等不能在边缘缓存的业务，基于智能选路技术，从众多回源线路中择优选择一条线路进行传输。 动静态混合加速 智能识别动态和静态资源，静态资源缓存在边缘节点，供用户就近访问；动态资源基于智能选路技术，从众多回源线路中择优选择一条线路进行传输。 | 支持动态和静态资源缓存加速。同时，多方面的升级也给用户带来更极速的访问体验。 缓存加速 支持缓存定时预热、冷资源缓存保持和缓存资源分析的能力，提高缓存命中率，减少回源流量。 集成 DNS 通过集成 Anycast DNS，实现全球各站点平均 DNS 解析速度小于 30ms。 四层代理 支持复杂场景下的加速，支持多端口和多协议能力 |
| 协议支持 | 应用层：支持 HTTP、HTTPS、QUIC 协议。 网络层：支持 IPv4、IPv6 协议。 | 应用层：支持 HTTP、HTTPS、WebSocket 协议。 传输层：支持 TCP、UDP 协议。 网络层：支持 IPv4、IPv6 协议。 | 应用层：支持 HTTP、HTTPS、WebSocket 协议。 传输层：支持 TCP、UDP 协议。 网络层：支持 IPv4、IPv6 协议。 |
| 调度模式 | DNS 调度 DNS-over-HTTPS 调度 302 调度 | DNS 调度 DNS-over-HTTPS 调度 302 调度 | 高性能、更安全的 DNS 调度 DNS-over-HTTPS 调度 302 调度 |
| 边缘计算 | 通过 EdgeScript 边缘脚本，实现可编程 CDN 的业务逻辑。 图片处理。 | 支持在边缘节点使用 EdgeRoutine 构建边缘程序，例如 A/B Test、预热等。 通过 EdgeScript 边缘脚本，实现可编程 CDN 的业务逻辑。 图片处理。 | 边缘函数 支持在边缘节点上直接部署 JavaScript 代码，用户可以从边缘节点得到响应，显著减少延迟。 边缘存储 边缘节点提供的 Key-Value 型边缘存储服务，结合边缘函数可以部署轻量型 BaaS 服务、API 网关服务等。 边缘容器 边缘节点提供以容器为核心的高弹性、易运维的计算资源，无需购买服务器资源，可以更专注于应用的开发。 |
| 安全策略 | Referer 防盗链 URL 鉴权 IP 黑白名单 | 基础 WAF 防御 DDoS 防御 基础的 Bot 防御 | 集成原生 WAF，支持自定义防护规则。 企业版最高支持 Tbps 级别的 DDoS 防护。 支持 H5 页面的 SDK 集成和原生安卓、iOS 的 SDK 集成的 Bot 防护。 AI 防护 支持源站防护。 |
| 日志分析 | 离线日志 实时日志投递 | 离线日志 实时日志投递 | 流量分析 离线日志 实时日志投递 即时日志监控 |


说明

- 

静态内容是指在不同请求中访问到的数据都相同的静态文件。例如：图片、视频、网站中的文件（html、css、js）、软件安装包、apk文件、压缩包等。

- 

动态内容是指在不同请求中访问到的数据不相同的动态内容。例如：网站中的文件（asp、jsp、php、perl、cgi）、API接口、[数据库](https://www.aliyun.com/getting-started/what-is/what-is-cloud-database)交互请求等。

关于动态和静态资源的详细介绍，请参见[什么是静态内容和动态内容？](products/cdn/documents/support/what-are-static-content-and-dynamic-content.md)。

## 管理工具

通过注册并登录阿里云账号，您可以在任何地方，通过以下方式管理CDN产品：

- 

通过CDN控制台管理

管理控制台是具有交互式操作的Web服务页面，更容易上手。关于管理控制台的操作，请参见[操作指南](products/cdn/documents/user-guide.md)。

- 

调用CDN API进行管理

支持GET和POST请求的RPC风格API。关于API说明，请参见[API](products/cdn/documents/developer-reference/api-cdn-2018-05-10-overview.md)[参考](products/cdn/documents/developer-reference/api-cdn-2018-05-10-overview.md)。

- 

通过阿里云App管理

支持阿里云App管理加速资源，更加快捷方便。关于阿里云App常见场景操作，请参见[在阿里云](products/cdn/documents/user-guide/use-alibaba-cloud-cdn-on-the-alibaba-cloud-app.md)[App](products/cdn/documents/user-guide/use-alibaba-cloud-cdn-on-the-alibaba-cloud-app.md)[上使用](products/cdn/documents/user-guide/use-alibaba-cloud-cdn-on-the-alibaba-cloud-app.md)[CDN](products/cdn/documents/user-guide/use-alibaba-cloud-cdn-on-the-alibaba-cloud-app.md)。

## 相关产品

了解CDN相关产品，便于您更深刻地理解CDN产品在阿里云产品中所处的位置和用途。

| 相关产品 | 用途 |
| --- | --- |
| [全站加速](https://help.aliyun.com/zh/edge-security-acceleration/dcdn/product-overview/what-is-dcdn#concept-hdt-3t2-xdb) | 全站加速可以区分动态和静态资源，实现动静态资源分别加速，并且同时兼顾加速与安全。 |
| [对象存储](products/oss/documents/user-guide/what-is-oss.md) [OSS](products/oss/documents/user-guide/what-is-oss.md) | 对象存储 OSS 结合 CDN 使用，可以提高网站访问速度，有效降低 OSS 的外网流量费用。 |
| [视频直播](https://help.aliyun.com/zh/live/product-overview/what-is-apsaravideo-live#topic-20605) | 在视频直播中应用 CDN，可实现媒资存储、切片转码、访问鉴权、内容分发加速一体化解决方案。 |
| [视频点播](https://help.aliyun.com/zh/vod/product-overview/what-is-apsaravideo-vod#concept-2526011) | 在视频点播中应用 CDN，可减少缓冲时间，实现高流畅度的播放体验。 |
| [云解析](https://help.aliyun.com/zh/dns/alibaba-cloud-dns#0dd736c066uij) [DNS](https://help.aliyun.com/zh/dns/alibaba-cloud-dns#0dd736c066uij) | 借助阿里云云解析 DNS 提供的强大且稳定的解析调度入口，确保顺畅的访问体验。 |
| [云服务器](products/ecs/documents/user-guide/what-is-ecs.md) [ECS](products/ecs/documents/user-guide/what-is-ecs.md) | 借助云服务器 ECS 提高网站可用性，保护服务器源站信息，降低带宽使用成本。 |
| [负载均衡](https://help.aliyun.com/product/27537.html) | 您可以将负载均衡服务器的 IP 地址设置为回源地址，降低回源带宽压力。 |


## 最佳实践

如果您想了解关于CDN的具体实践，请参见以下文档：

- 

[CDN](products/cdn/documents/use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)[加速](products/cdn/documents/use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)[OSS](products/cdn/documents/use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)[资源](products/cdn/documents/use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)

- 

[CDN](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md)[加速](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md)[ECS](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md)[资源](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md)

- 

[提高](products/cdn/documents/use-cases/increase-the-cache-hit-ratios-of-alibaba-cloud-cdn.md)[CDN](products/cdn/documents/use-cases/increase-the-cache-hit-ratios-of-alibaba-cloud-cdn.md)[缓存命中率](products/cdn/documents/use-cases/increase-the-cache-hit-ratios-of-alibaba-cloud-cdn.md)

## 扩展阅读

如何使用CDN来加速OSS上存储的文件资源分发？如何使用dcdn助力企业灰度上云？来这里看看达人们玩转CDN产品：[直达实战派](https://help.aliyun.com/contentpioneer/)

[上一篇：产品简介](products/cdn/documents/product-overview/product-introduction.md)[下一篇：阿里云CDN的五大竞争力](products/cdn/documents/product-overview/competitive-advantages-of-alibaba-cloud-cdn.md)

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
