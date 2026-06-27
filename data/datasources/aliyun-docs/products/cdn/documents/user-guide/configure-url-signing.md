# 配置URL鉴权-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-url-signing

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

# 配置URL鉴权

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在CDN分发的内容默认为公开资源，用户拿到URL后均可访问，为防止站点资源被恶意下载盗用，除了通过Referer防盗链、IP黑白名单等防控方式，您还可以采用URL鉴权，自行配置校验鉴权URL中的加密串和时间戳，更安全有效地保护源站资源。

## 鉴权逻辑

URL鉴权功能通过阿里云CDN节点与客户资源站点配合，形成了更为安全可靠的源站资源防盗方法。主要由以下几个部分配合：

- 

源站应用服务器：根据鉴权URL生成规则（包括鉴权算法、密钥）生成鉴权URL返回给客户端。

- 

客户端：发起资源请求，并发送鉴权URL给CDN节点进行验证。

- 

CDN节点：对鉴权URL中的鉴权信息（鉴权字符串、时间戳等）进行验证。

- 

CDN客户在源站应用服务器配置鉴权URL的生成规则（包括鉴权算法和密钥）。

假设鉴权URL为：http://DomainName/timestamp/md5hash/FileName。

- 

客户端访问源站应用的页面时，源站应用服务器将会按照鉴权URL的生成规则生成鉴权URL，并且把鉴权URL包含在应用页面上返回给客户端。

- 

客户端使用鉴权URL向CDN节点发起资源请求。

- 

CDN节点对鉴权URL中的鉴权信息（包括鉴权字符串、时间戳等）进行验证，判断请求的合法性。

- 

鉴权失败，拒绝访问请求。

- 

鉴权通过，正常响应合法请求。

说明

- 

若CDN节点没有缓存资源，CDN节点回源前，会去掉鉴权URL中的鉴权参数，将鉴权URL还原为原始URL（例如：http://DomainName/FileName），再使用原始URL生成缓存key或者发起回源请求。

- 

您的请求URL经过CDN鉴权后，URL中的特殊字符，例如中文（或其他非 ASCII 字符）会被编码（encode）处理。

## 注意事项

- 

配置URL鉴权后，鉴权失败请求仍可访问到CDN节点，但会被CDN节点拒绝并返回403状态码，CDN日志中仍会记录鉴权失败的请求记录。

- 

由于URL鉴权功能采用的是自行配置校验鉴权URL中的加密串和时间戳，因此在恶意请求被CDN节点拦截的同时，会产生少量的流量费用，如果客户端使用HTTPS协议访问，还会产生HTTPS请求数费用（因为拦截恶意请求的时候，也同时消耗了CDN节点的处理资源）。

## 配置鉴权URL并开启鉴权

重要

- 

请确保您已经在您的源站应用服务器配置了鉴权URL的生成规则（包括鉴权算法、密钥）。

- 

CDN配置的URL鉴权逻辑必须与您的源站应用服务器的URL鉴权逻辑保持一致。

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

在域名管理页面，找到目标域名，单击操作列的管理。

- 

在指定域名的左侧导航栏，单击访问控制。

- 

单击URL鉴权页签。

- 

在鉴权URL设置区域，单击修改配置。

- 

打开URL鉴权开关，配置URL鉴权信息。

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

| 参数 | 说明 |
| --- | --- |
| 鉴权类型 | 阿里云 CDN 提供了 4 种鉴权签名计算方式。您可以根据访问加密 URL 格式，选择合适的鉴权方式，实现对源站资源的有效保护。URL 鉴权类型如下： [鉴权方式](products/cdn/documents/user-guide/type-a-signing.md) [A](products/cdn/documents/user-guide/type-a-signing.md) [说明](products/cdn/documents/user-guide/type-a-signing.md) [鉴权方式](products/cdn/documents/user-guide/type-b-signing.md) [B](products/cdn/documents/user-guide/type-b-signing.md) [说明](products/cdn/documents/user-guide/type-b-signing.md) [鉴权方式](products/cdn/documents/user-guide/type-c-signing.md) [C](products/cdn/documents/user-guide/type-c-signing.md) [说明](products/cdn/documents/user-guide/type-c-signing.md) [鉴权方式](products/cdn/documents/user-guide/authentication-method-f-description.md) [F](products/cdn/documents/user-guide/authentication-method-f-description.md) [说明](products/cdn/documents/user-guide/authentication-method-f-description.md) 说明 URL 鉴权错误会返回 403 报错： MD5 计算类错误 例如： X-Tengine-Error:denied by req auth: invalid md5hash=de7bfdc915ced05e17380a149bd760be 时间类报错 例如： X-Tengine-Error:denied by req auth: expired timestamp=1439469547 |
| 主 KEY | 输入鉴权方式对应的主用密码。由 6~128 个字符组成，支持大写字母、小写字母、数字。 |
| 备 KEY | 输入鉴权方式对应的备用密码。由 6~128 个字符组成，支持大写字母、小写字母、数字。主、备 KEY 至少要填写一个。 |
| 鉴权 URL 有效时长 | CDN 配置的鉴权 URL 有效时长，用户可在（timestamp+CDN 上鉴权 URL 有效时长）时间区间内访问 CDN，超出该区间，鉴权失效。 单位：秒 取值范围：1~31536000 默认值：1800（30 分钟） 示例： 例如签算服务器生成鉴权 URL 的时间（timestamp）为 2020-08-15 15:00:00（UTC+8），CDN 上鉴权 URL 有效时长为 1800 秒，则鉴权 URL 失效时间为 2020-08-15 15:30:00（UTC+8）。 |
| 签名参数 | 通过设置签名参数，可以自定义签名参数名称。仅在鉴权类型设置为 F 方式的时候有效。 |
| 时间戳参数 | 通过设置时间戳参数，可以自定义时间戳参数名称。仅在鉴权类型设置为 F 方式的时候有效。 |
| 时间戳格式 | 设置时间戳格式，支持十进制（Unix 时间戳）和十六进制（Unix 时间戳）。仅在鉴权类型设置为 F 方式的时候有效。 |
| URL 编码 | URL 编码开关，默认关闭，开启的情况下将会对用户请求 URL 做 URL 编码处理。仅在鉴权类型设置为 F 方式的时候有效。 |
| 规则条件 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 重要 引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](products/cdn/documents/user-guide/rules-engine.md) 中进行管理。 |


- 

单击确定。

## 验证鉴权URL正确性

为保证服务器正确实现了鉴权逻辑，配置鉴权URL后，建议您在CDN控制台生成对应的鉴权URL，校验鉴权URL的正确性。

- 

在鉴权URL生成工具区域，配置原始URL（未编码）和鉴权信息。

| 参数 | 说明 |
| --- | --- |
| 原始 URL（未编码） | 输入完整的原始 URL 地址，例如： https://www.aliyun.com 。生成鉴权 URL 时，工具将自动编码原始 URL。 |
| 鉴权类型 | 按照您在 [配置鉴权](products/cdn/documents/user-guide/configure-url-signing.md) [URL](products/cdn/documents/user-guide/configure-url-signing.md) [并开启鉴权](products/cdn/documents/user-guide/configure-url-signing.md) 的配置，选择 URL 鉴权类型。 |
| 鉴权 KEY | 按照您在 [配置鉴权](products/cdn/documents/user-guide/configure-url-signing.md) [URL](products/cdn/documents/user-guide/configure-url-signing.md) [并开启鉴权](products/cdn/documents/user-guide/configure-url-signing.md) 的配置，输入您配置的 主 KEY 或 备 KEY 。 |
| 鉴权 URL 有效时长 | 按照您在 [配置鉴权](products/cdn/documents/user-guide/configure-url-signing.md) [URL](products/cdn/documents/user-guide/configure-url-signing.md) [并开启鉴权](products/cdn/documents/user-guide/configure-url-signing.md) 的配置，输入 URL 鉴权的有效时长，单位为秒。 |


- 

单击开始生成，即可获得鉴权URL和Timestamp。

## 关闭URL鉴权

重要

如果CDN的URL鉴权功能已经关闭，但是客户端发起的请求URL依然携带鉴权参数，将导致CDN无法把客户端发起的请求URL（带鉴权参数）还原为原始URL，最终所有请求都无法命中缓存，均会透传回源站，导致源站的流量大涨，同时也会增加源站的流量费用。因此，如果您需要停止使用URL鉴权，需同时关闭应用服务器和CDN的URL鉴权功能。

- 

在[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)的鉴权URL设置区域，单击修改配置，关闭URL鉴权开关。

- 

在您的应用服务器中去掉请求URL的鉴权参数。

## 相关API

- 

[查询域名配置](products/cdn/documents/developer-reference/api-cdn-2018-05-10-describecdndomainconfigs.md)

- 

[域名配置功能函数](products/cdn/documents/developer-reference/parameters-for-configuring-features-for-domain-names.md)

[上一篇：URL鉴权配置](products/cdn/documents/user-guide/url-signing.md)[下一篇：鉴权方式A说明](products/cdn/documents/user-guide/type-a-signing.md)

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
