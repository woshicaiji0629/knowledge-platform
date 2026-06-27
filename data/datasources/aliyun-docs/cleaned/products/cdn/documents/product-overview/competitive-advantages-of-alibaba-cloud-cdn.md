# 产品核心竞争优势全面介绍-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/product-overview/competitive-advantages-of-alibaba-cloud-cdn

# 阿里云CDN的五大竞争力
本文主要从五个方面全面介绍阿里云CDN的产品能力，帮助您更好地理解阿里云CDN产品。
阿里云CDN产品主要有以下五大竞争力：
[产品竞争力](competitive-advantages-of-alibaba-cloud-cdn.md)
[技术竞争力](competitive-advantages-of-alibaba-cloud-cdn.md)
[价格竞争力](competitive-advantages-of-alibaba-cloud-cdn.md)
[生态竞争力](competitive-advantages-of-alibaba-cloud-cdn.md)
[服务竞争力](competitive-advantages-of-alibaba-cloud-cdn.md)
## 产品竞争力
广泛的节点覆盖
阿里云在全球拥有3200+节点。中国内地拥有2300+节点，覆盖31个省级区域；中国香港、中国澳门、其他国家和地区拥有900+节点，覆盖70多个国家和地区。全网带宽输出能力达180 Tbps。阿里云CDN产品通过广泛的地域覆盖和深厚的带宽储备，在全球范围为用户提供安全、稳定、可靠的内容分发服务。
权威的业界认证
公安部认证CDN内容分发系统等级保护三级。
国际PCI-DSS认证。
Gartner评估的全球级CDN服务供应商。
全球IPv6 Enabled CDN Logo认证。
丰富的产品功能
阿里云CDN提供控制台和OpenAPI，支持对内容加速业务进行配置和管理。主要的产品能力如下：
| 产品能力 | 主要功能模块 |
| --- | --- |
| 域名管理 | 添加域名、基本配置、回源配置、缓存配置、HTTPS 配置、访问控制、性能优化、视频相关、安全配置、流量限制、QUIC 协议、边缘脚本、IPv6 配置等。 |
| 监控查询 | 资源监控、实时监控、用量查询、边缘脚本监控、安全监控。 |
| 日志管理 | 离线日志下载、离线日志转存、实时日志推送、运营报表定制、运营报表订阅。 |
| 刷新预热 | URL 刷新、目录刷新、URL 预热。 |
灵活的可编程CDN配置
阿里云CDN是一个可编程CDN，既支持简单的一站式配置，又可以通过EdgeScript（[边缘脚本](../user-guide/edgescript-overview.md)，简称ES）实现自定义配置。当CDN控制台上的标准配置无法满足您的业务需求时，可通过ES编写简单脚本来快速实现定制化业务需求，解决定制化需求发布周期长、业务变更不敏捷等问题。
开放丰富的API接口
支持通过API实现CDN控制台上的所有功能。详细操作，请参见[API](../developer-reference/api-cdn-2018-05-10-overview.md)[概览](../developer-reference/api-cdn-2018-05-10-overview.md)。
## 技术竞争力
精准的调度系统
持续更新的精准IP数据库：IP数据库的作用是在用户的DNS解析请求转发到了CDN调度系统时，调度系统会判断用户的地区和运营商归属，以此来为用户分配就近接入的同运营商CDN节点。为了确保IP数据库的数据处于最新的状态，数据库一直在持续地更新。
HTTPDNS服务：采用HTTPDNS这项技术使得用户终端可以绕开运营商的Local DNS，直接采用HTTP协议去访问调度系统，请求所需要访问的域名的最优接入节点，这样可以避免DNS劫持所带来的业务安全问题。该功能需要客户端兼容。
节点状态分析：CDN调度系统通过链路状态系统实时分析整个缓存系统中的所有节点和链路的健康状况，为用户选择最优的接入节点，避免因为接入节点质量不佳而影响到用户访问体验。
基于内容的调度：在大文件下载和视频点播等场景下，采用302调度技术。用户请求会先访问中心调度系统，系统解析请求内容后，通过302重定向将用户分配至最佳接入节点，以提高缓存命中率。
智能的缓存系统
分层缓存：利用智能对象热度算法，多级、分层缓存热点资源，实现资源精准加速。
高性能缓存：高性能的缓存Cache系统设计，均衡使用CPU多核处理能力，高效合理使用和控制内存，最大化SSD IOPS和吞吐。
高速读写存储：各节点具备高速读写固态硬盘SSD存储，配合SSD加速能力，大幅减少用户访问等待时间，提高可用性。
高效回源：提供Failover重试机制，保证高效回源和信息同步。
高效的传输协议
支持QUIC协议：QUIC是一种基于UDP的新一代互联网传输层协议，且融合了TCP、TLS、HTTP/2等协议的特性，能有效应对当前传输层与应用层的需求，降低延迟和提高连接并发处理能力。
自研TCP协议栈算法：通过调整拥塞算法、丢包探测算法，对TCP协议的性能做了大幅度提升，传输性能显著提升。
可靠的安全防护能力
阿里云CDN通过可靠的安全防护措施，帮助您规避业务上的安全风险。
防盗链：用户可以选择通用的Referer、UA、URL、IP等通用鉴权方式，也可以用EdgeScript来定制鉴权方式，以防止源站资源被盗用；支持远程鉴权功能实现二次鉴权。
DNS防劫持：支持HTTPDNS，通过HTTP协议直接获取域名解析结果，以绕过运营商Local DNS，避免域名劫持。
HTTPS传输加密：支持采用TLS协议来加密HTTP协议内容，防止明文数据暴露在互联网上，并且可以设置TLS1.3、HSTS等高级功能。
源站保护：阿里云CDN产品自身具备一定的安全防护能力，也可以配置SCDN产品来提供更强的安全防护能力。
源站可靠性：可以配置主备源站，阿里云CDN能够持续监测主备源站的状态，在主站出现故障的时候能够及时切换到备站。
## 价格竞争力
性能和技术强大的同时，阿里云CDN的价格同样很有竞争力：
计费方式灵活多样，详细信息，请参见[计费概述](billing-overview.md)。
预付费套餐包价格常年优惠，详细信息，请参见[加速资源包](https://common-buy.aliyun.com/?spm=5176.7933777.1398157.2.2fef56f5Tev9PO&commodityCode=dcdnpaybag&aly_as=L0rjD3H0#/buy)。
阿里云CDN精心为您打造了多款计费方式和资源包，适合您多种不同的业务场景或场景组合。您可以根据您的业务场景，选择合理的计费方式。
| 如果您的业务场景是... | 我们建议您选择... |
| --- | --- |
| 您的源站内容日常访问流量较少，或某个时段内占用带宽资源较大。 | 按流量计费方式。 说明 推荐您购买更划算的 [预付费资源包](https://common-buy.aliyun.com/?spm=5176.8064714.323101.1.720cSlWXSlWXoT&commodityCode=dcdnpaybag#/buy) 。我们为您提供多个加速区域、多种规格的套餐。您可以根据实际需求，购买 100GB~50PB 的套餐包。 |
| 如果您满足近 30 天内的带宽峰值超过 5 Gbps，并且流量曲线比较平稳，全天带宽利用率大于 30%。 | [按带宽峰值计费](billing-rules-of-basic-services.md) 。按照每日的带宽峰值计费。每 5 分钟统计一个带宽数据，每日得到 288 个值，取其中的最大值。 |
| 当您开通 HTTPS 功能，且终端用户以 HTTPS 协议访问您的源站内容。 | [动静态请求数套餐包](https://common-buy.aliyun.com/?spm=5176.8064714.323101.1.720cSlWXSlWXoT&commodityCode=dcdnpaybag#/buy) 。动静态 HTTPS 请求数优先抵用资源包，超出后按量付费。 |
| 如果您的月消费金额大于 10 万。 | 阿里云 CDN 为您提供月结 95 带宽峰值计费方式，您可以联系阿里云商务洽谈。 |
关于阿里云CDN全部的计费方式，请参见[CDN](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.10.1b444ee22Dxy8y#/cdn/detail)[详细价格信息](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.10.1b444ee22Dxy8y#/cdn/detail)。
## 生态竞争力
阿里云拥有强大的产品功能体系：
如果您已经使用了其他阿里云的产品，那么借助生态优势，接入CDN服务会使您的实际业务更加流畅，提升您的业务运营效能。
| 如果您已经购买了... | 推荐您... | 原因 |
| --- | --- | --- |
| [云服务器](../../../ecs/documents/user-guide/what-is-ecs.md) [ECS](../../../ecs/documents/user-guide/what-is-ecs.md) | 开通阿里云 CDN | 云服务器 ECS 作为 CDN 源站，使用 CDN 可以帮助您有效提高网站访问速度。 |
| [对象存储](../../../oss/documents/user-guide/what-is-oss.md) [OSS](../../../oss/documents/user-guide/what-is-oss.md) | 对象存储 OSS 作为 CDN 源站，使用 CDN 可以提高您网站的访问速度，有效降低 OSS 的外网流量费用。 |  |
| [函数计算](https://help.aliyun.com/zh/functioncompute/fc-2-0/product-overview/what-is-function-compute#concept-2259850) | 函数计算作为 CDN 源站，使用 CDN 可以帮助您有效提高网站访问速度。 |  |
CDN对静态内容有超强的加速能力，针对动静态混合加速场景和更加关注安全的场景，均有对应的产品提供给您。
| 如果您的业务或需求是... | 推荐您使用... | 说明 |
| --- | --- | --- |
| 动静态混合内容加速 | [边缘安全加速](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/what-is-esa) [ESA](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/what-is-esa) | ESA 对图片、音视频、CSS 文件等静态资源在边缘节点上进行缓存；对 API 接口、数据库交互请求等服务器动态生成实时的数据进行路由和传输优化。从而显著提高访问速度和用户体验。 |
| 需要更关注安全，兼顾安全和加速 | [边缘安全加速](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/what-is-esa) [ESA](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/what-is-esa) | ESA 使用原生 DDoS 防护、原生 Web 应用防火墙搭配阿里云自研机器学习算法，对每一次请求进行威胁检测，全球有超过 20Tbps 的边缘 DDoS 攻击防护资源储备。 |
如果您已经开通了阿里云CDN服务，还可以了解其他交叉产品，帮助您更好地实现业务需求。
| 如果您的业务或需求是... | 我们推荐您使用... | 说明 |
| --- | --- | --- |
| 加速音视频点播内容 | [视频点播](https://help.aliyun.com/zh/vod/product-overview/what-is-apsaravideo-vod) | 阿里云视频点播（VOD）是集音视频上传、自动化转码处理、媒体资源管理、分发加速于一体的全链路音视频点播服务。 |
| 加速直播流媒体 | [视频直播](https://help.aliyun.com/zh/live/product-overview/what-is-apsaravideo-live#topic-20605) | 视频直播服务（ApsaraVideo Live）是基于内容接入、分发网络和大规模分布式实时转码技术打造的音视频直播平台，提供便捷接入、高清流畅、低延迟、高并发的音视频直播服务。 |
| 使用 CDN 服务前还没有域名 | [阿里云域名服务](https://help.aliyun.com/zh/dws/product-overview/what-is-domains#concept-t42-dlv-12b) | 阿里云域名服务是集域名注册、交易、监控和保护为一体的综合域名管理平台，联合阿里云备案、云解析 DNS 服务，为您提供全方位域名服务。 |
| 在使用阿里云 CDN 前，域名还未完成 ICP 备案 | [阿里云备案](https://help.aliyun.com/zh/icp-filing/basic-icp-service/product-overview/what-is-an-icp-filing#concept-nx4-hql-zdb) | 根据 《互联网信息服务管理办法》 以及 《非经营性互联网信息服务备案管理办法》 ，国家对非经营性互联网信息服务实行备案制度，对经营性互联网信息服务实行许可制度。未取得许可或者未履行备案手续的，不得从事互联网信息服务。即所有对中国内地提供服务的网站都必须先进行 ICP 备案，才可开通服务。阿里云 ICP 代备案系统为您提供申请备案、修改注销备案信息、认领备案等服务。 |
| 实现全站 HTTPS 化，配置 HTTPS 证书 | [SSL](https://help.aliyun.com/zh/ssl-certificate/product-overview/what-is-certificate-management-service#concept-xn2-52p-ydb) [证书服务](https://help.aliyun.com/zh/ssl-certificate/product-overview/what-is-certificate-management-service#concept-xn2-52p-ydb) | SSL 证书服务由阿里云联合中国及中国以外地域多家数字证书管理和颁发的权威机构，在阿里云平台上直接提供的服务器数字证书。可在阿里云平台上直接购买，或者免费获取所需类型的数字证书，并一键部署在阿里云产品中，以非常方便快捷的方式将您的服务从 HTTP 转换成 HTTPS，实现网站的身份验证和数据加密传输。 |
| 将易于管理识别的域名转换为计算机用于互连通信的数字 IP 地址 | [云解析](https://help.aliyun.com/zh/dns/alibaba-cloud-dns) [DNS](https://help.aliyun.com/zh/dns/alibaba-cloud-dns) | 云解析 DNS（Alibaba Cloud DNS）是一种安全、快速、稳定、可扩展的权威 DNS 服务，云解析 DNS 为企业和开发者将易于管理识别的域名转换为计算机用于互连通信的数字 IP 地址，从而将用户的访问路由到相应的网站或应用服务器。 |
| 帮助您提升运维、运营效率，建立 DT 时代海量日志处理能力。 | [日志服务](../../../sls/documents/what-is-log-service.md) | 日志服务（简称 SLS）是针对日志类数据的一站式服务，在阿里巴巴集团经历大量大数据场景锤炼而成。您无需开发就能快捷完成日志数据采集、消费、投递以及查询分析等功能，提升运维、运营效率，建立 DT 时代海量日志处理能力。 |
| 对阿里云资源和互联网应用进行监控的服务。 | [云监控](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/what-is-cloudmonitor#concept-2452587) | 云监控（CloudMonitor） 是一项针对阿里云资源和互联网应用进行监控的服务。云监控服务可用于收集获取阿里云资源的监控指标，探测互联网服务可用性，以及针对指标设置警报。 |
## 服务竞争力
阿里云CDN拥有多种服务体系，包括：
完善的服务体系：7*24小时全网监控和服务。
完善的资料体系：
学习产品知识：[什么是阿里云](what-is-alibaba-cloud-cdn.md)[CDN](what-is-alibaba-cloud-cdn.md)。
学习基础课程：[阿里云大学](https://edu.aliyun.com/course/explore?title=CDN)。
浏览和讨论相关话题：[开发者社区](https://developer.aliyun.com/?spm=5176.12825654.h2v3icoap.940.2fed2c4aiuQBu4&aly_as=xIPi0tJy)。
完善的问题解决体系：您可以提交反馈建议，进行售前和售后问题咨询。
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
