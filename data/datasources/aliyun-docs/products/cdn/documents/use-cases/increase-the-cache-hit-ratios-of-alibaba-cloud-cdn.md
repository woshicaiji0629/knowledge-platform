# 如何提高CDN缓存命中率-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/use-cases/increase-the-cache-hit-ratios-of-alibaba-cloud-cdn

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

# 提高CDN缓存命中率

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

CDN缓存命中率低会导致源站压力大，静态资源访问效率低。您可以根据导致CDN缓存命中率低的具体原因，选择对应的优化策略来提高CDN的缓存命中率。

## 背景信息

CDN通过将静态资源缓存在CDN节点上实现资源访问加速。当客户端访问某资源时，如果CDN节点上已经缓存了该资源，用户请求会命中CDN节点上的缓存，直接从缓存中获取资源返回给用户，可避免通过较长的链路回源，提高资源的响应速度和降低源站的带宽压力。如果CDN缓存命中率低，会影响用户体验和增加源站的带宽压力。

CDN缓存字节命中率：

- 

字节命中率=（L1的边缘节点响应流量-回源的边缘节点响应流量）/L1的边缘节点响应流量

说明

字节命中率越低，回源流量越大，源站的流出流量越大，源站的带宽资源以及其他的负载越大，因此回源流量代表了源站服务器接收到的负载压力，在业务使用中主要关心字节命中率。

- 

请求命中率=CDN缓存命中的请求数÷CDN所有的请求数

重要

range分片回源情况下，命中率指标建议参考字节命中率。

## 查看CDN缓存命中率

### 方式一：通过控制台查看

CDN控制台提供的缓存命中率监控为字节命中率，详细信息如下：

- 

通过资源监控功能查询

可查询数据的时间范围较大，适合查看较长周期（例如30天）内的命中率情况。时间粒度为5分钟的情况下，数据延迟15分钟左右。详细信息，请参见[资源监控](products/cdn/documents/user-guide/resource-monitoring.md)。

- 

通过实时监控功能查询

可查询数据的时间范围较小，适合查看较短周期（例如1小时）内的实时命中率情况。时间粒度为1分钟的情况下，数据延迟3分钟左右。详细信息，请参见[实时监控](products/cdn/documents/user-guide/real-time-monitoring.md)。

### 方式二：调用API查看

- 

资源监控功能对应的API

| API | 描述 |
| --- | --- |
| [DescribeDomainHitRateData](products/cdn/documents/api-describedomainhitratedata.md) | 获取加速域名的字节命中率数据，支持获取最近 90 天的数据。 |
| [DescribeDomainReqHitRateData](products/cdn/documents/api-describedomainreqhitratedata.md) | 获取加速域名的请求命中率数据，支持获取最近 90 天的数据。 |


- 

实时监控功能对应的API

| API | 描述 |
| --- | --- |
| [DescribeDomainRealTimeByteHitRateData](products/cdn/documents/api-describedomainrealtimebytehitratedata.md) | 获取加速域名 1 分钟粒度的字节命中率数据，支持查询 7 天内的数据。 |
| [DescribeDomainRealTimeReqHitRateData](products/cdn/documents/api-describedomainrealtimereqhitratedata.md) | 获取加速域名 1 分钟粒度的请求命中率数据，支持查询 7 天内的数据。 |


## 提高CDN缓存命中率

下表列出了影响CDN缓存命中率的因素和提高CDN缓存命中率的方法。

- 

- 

- 

- 

- 

- 

- 

| 策略 | 影响因素与应用场景 | 配置方法 |
| --- | --- | --- |
| 业务高峰前预热热门资源 | 影响因素：运营大型活动或新版本安装包发布前，没有提前将资源预热到 CDN 节点，大量资源需要从源站获取，导致 CDN 缓存命中率低。 应用场景： 运营活动 运营一个大型活动时，提前将活动页涉及到的静态资源预热至 CDN 节点，活动开始后用户访问的所有静态资源均已缓存至 CDN 加速节点，由加速节点直接响应。 安装包发布 新版本安装包或升级包发布前，提前将资源预热至 CDN 加速节点，产品正式上线后，海量用户的下载请求将直接由 CDN 加速节点响应，提升下载速度，大幅度降低源站压力，提升用户体验。 | [刷新和预热资源](products/cdn/documents/user-guide/refresh-and-prefetch-resources.md) |
| 合理配置缓存过期时间： 不常更新的静态文件（例如，图片类型、应用下载类型等），建议设置 1 个月以上。 频繁更新的静态文件（例如，JS、CSS 等），根据实际业务情况设置。 动态文件（例如，PHP、JSP、ASP 等），建议设置为 0s，即不缓存。 | 影响因素： CDN 上未配置缓存策略，所有用户请求都需要回源站。 CDN 上配置的缓存过期时间过短，缓存资源频繁过期，导致缓存命中率低。 应用场景：用户在源站发布了静态资源，CDN 节点没有将资源缓存下来，或者 CDN 节点上缓存的资源很快就失效了。 | [配置](products/cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md) [CDN](products/cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md) [缓存过期时间](products/cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md) |
| 去除 URL 中问号后的参数缓存 | 影响因素：当 URL 请求中带有 queryString 或其他可变参数时，访问同一个资源的不同 URL（URL 携带的参数不同）会重新回源，导致 CDN 缓存命中率低。 应用场景：希望通过不同的 URL（URL 携带的参数不同），可以访问到同一个资源。 | [忽略参数](products/cdn/documents/user-guide/ignore-parameters.md) |
| 大文件设置分片回源策略 | 影响因素：用户下载安装包可能下载一半就停止下载，或者观看视频只看了一部分就停止观看，即用户只需要访问资源文件指定范围内的部分内容，但是 CDN 节点会向源站请求整个文件，从而使得 CDN 节点从源站下载的内容大于响应给用户的内容，导致缓存命中率低。 应用场景：用户下载应用安装包或者观看视频资源。 | [配置](products/cdn/documents/user-guide/object-chunking.md) [Range](products/cdn/documents/user-guide/object-chunking.md) [回源](products/cdn/documents/user-guide/object-chunking.md) |
| 处理源站不缓存标头 | 影响因素：源站返回了不缓存的响应头（如 Cache-Control: max-age=0、Cache-Control: no-cache、Cache-Control: private 等），CDN 会遵循源站指示不对该资源进行缓存，导致所有请求都回源到源站，缓存命中率降低。典型场景：源站为静态文件（图片、JS、CSS 等）配置了 Cache-Control: max-age=0 或 Cache-Control: no-cache 响应头，导致 CDN 节点无法缓存这些静态资源。 | 方法一（推荐）：修改源站服务器配置，去掉静态资源响应头中的 Cache-Control: max-age=0 或 Cache-Control: no-cache 等不缓存标头，为静态资源配置合理的缓存时长（如 Cache-Control: max-age=2592000）。 方法二：在 **域名管理** 页面，单击目标加速域名，进入 **缓存配置** 页签，在 **缓存过期时间** 中 **添加** 缓存规则，开启 **忽略源站不缓存标头** 选项。开启后，CDN 将忽略源站返回的不缓存标头，按照 CDN 自身配置的缓存策略进行缓存。 说明 「忽略源站不缓存标头」功能开启后，CDN 将会忽略源站响应的不缓存标头（例如 Cache-Control: no-cache 等），按照您在 CDN 控制台配置的缓存过期时间规则进行缓存。该选项在缓存过期时间配置弹窗中与「优选遵循源站缓存策略」「客户端跟随 CDN 缓存策略」「强制内容重新验证」等选项并列。过期时间最多可设置为 3 年。 说明 为进一步提升缓存命中率，建议在 **回源配置** 中将 Range 回源设置为「跟随客户端 Range 请求」，避免全量回源影响命中率。 |
| 其他命中率优化策略 | 除了以上几种常用的命中率优化措施以外，阿里云 CDN 还有其他的优化措施，这些措施可以根据不同的业务场景来配置，例如：中心 302 调度、边缘 302 调度、合并回源、共享缓存等。其中，**共享缓存**功能允许同账号下的多个加速域名共用 CDN 节点上的缓存资源。当您有多个域名需要同名的 JS/CSS 文件且各源站内容完全一致时，可通过共享缓存功能让这些域名共用同一份缓存，从而提升缓存命中率。新增网站时，只需确保其资源路径与现有加速域名的资源结构对齐，无需重复配置 CDN 缓存规则，即可实现多源站文件的统一加速和缓存共享。 | 中心 302 调度、边缘 302 调度、合并回源由阿里云售后工程师在后台配置。**共享缓存**：在 **域名管理** 页面，单击目标加速域名，进入 **缓存配置** 页签，切换到 **共享缓存** 子页签，单击 **修改配置** ，从当前账号下已在线的加速域名列表中选择要共享缓存的目标域名（支持搜索过滤），确认后即可生效。选择后，当前加速域名与所选加速域名共享缓存，同时合并到所选加速域名回源。如需删除配置，单击 **删除配置** 并确认即可。 说明 共享缓存配置中，可从当前账号下已在线的加速域名中单选一个目标域名（自动排除当前域名本身）。配置生效后，当前域名将使用所选域名的缓存资源，并合并到所选域名的回源路径中。 |


## 查看缓存命中状态日志

在CDN的请求日志中，记录了所有CDN请求的缓存命中状态。详细日志格式，请参见[快速入门](products/cdn/documents/user-guide/offline-logs-quick-start.md)。

缓存命中状态字段说明：

- 

HIT：表示命中缓存。

- 

MISS：表示未命中缓存。

说明

命中状态仅表示CDN L1节点的命中状态。例如，CDN L1节点未命中缓存，L2节点命中缓存，日志中仍显示MISS。

日志示例：

26/Jun/2019:10:38:19 +0800] 192.168.53.146 - 1542 "-" "GET http://example.aliyundoc.com/index.html" 200 191 2830 MISS "Mozilla/5.0 (compatible; AhrefsBot/5.0; +http://example.com/robot/)" "text/html"

您也可以调用[查询离线日志下载地址](products/cdn/documents/developer-reference/api-cdn-2018-05-10-describecdndomainlogs.md)接口，获取加速域名的日志信息。

[上一篇：CDN加速门户网站](products/cdn/documents/use-cases/accelerate-content-delivery-for-infographic-and-video-websites.md)[下一篇：投递CDN实时日志到SLS来分析用户访问数据](products/cdn/documents/use-cases/ship-and-analyze-alibaba-cloud-cdn-real-time-logs-in-log-service.md)

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
