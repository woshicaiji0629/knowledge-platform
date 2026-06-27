# 如何配置条件源站-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-a-conditional-origin

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

# 配置条件源站

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

条件源站功能可以与规则引擎功能实现配置联动，根据指定规则（如 request header、query string parameter、path、client IP 等）来过滤用户请求，并将符合条件的请求回源到指定的源站地址。可以添加多个配置，实现不同规则条件下回源到不同的源站。

## 前提条件

在添加条件源站配置之前，需要先在[规则引擎](products/cdn/documents/user-guide/rules-engine.md)中创建规则条件。

## 注意事项

- 

功能冲突：条件源站与[高级回源](products/cdn/documents/user-guide/configure-advanced-origin-settings.md)互斥，只能二选一配置。

- 

通配符支持：在规则引擎中，URI匹配值支持通配符*（匹配任意多个字符）和?（匹配任意单个字符）。高级回源功能中的 Path 匹配仅支持精确值，不支持通配符。

- 

规则优先级与匹配顺序：条件源站按所关联规则条件的优先级依次匹配，而非按功能自身的配置顺序。命中某一条规则后不再继续匹配。规则引擎中的规则条件优先级由创建顺序决定，越早创建的规则优先级越高。若需调整匹配优先级，需在规则引擎中删除现有规则后，按期望的优先顺序重新添加。

- 

多路径配置技巧：在创建"包含"或"不包含"某路径的规则时，可以在单条规则的匹配值中填写多个路径（支持多行或多值输入），简化配置。

- 

规则数量限制：条件源站可引用的规则条件数量受规则引擎全局限制。单个域名下所有功能（包括条件源站、高级回源、Referer 防盗链等）对规则条件的总引用次数最大不超过 5 次。在多源站复杂场景下，若超出该限制会导致配置失败。建议合理规划规则数量，或在源站过多时考虑使用独立域名分别加速。

## 源站为OSS时的注意事项

- 

若源站为OSS，需要添加该源站地址到域名管理>基本配置>源站信息中，并且将源站类型设置为OSS域名，以便CDN与OSS正常鉴权。

- 

多 OSS 源站场景：当配置多个 OSS 源站时，必须为每个源站配置[指定源站回源](products/cdn/documents/user-guide/specify-an-origin-host-for-each-origin.md)[HOST](products/cdn/documents/user-guide/specify-an-origin-host-for-each-origin.md)，且 Host 值需与对应的 OSS Bucket 域名完全一致（例如dev-3mir.oss-cn-guangzhou.aliyuncs.com）。

若未正确配置或依赖默认回源 Host，请求可能随机回源至错误的 Bucket，导致 403 SignatureDoesNotMatch（签名验证失败）或 404 Not Found 错误。每条条件回源规则（包括匹配规则和不匹配/兜底规则）都需要明确绑定对应的源站和回源 Host。建议在配置多个源站时，将基础源站的权重设置为一致，并为每个条件源站配置独立的规则条件，以确保回源路径可控。

## 条件源站与基础源站、高级回源的区别

条件源站和高级回源均可引用规则引擎中配置的规则条件，从而实现更灵活的回源策略。CDN 根据请求是否命中规则条件，自动选择对应的源站：

| 源站类型 | 触发条件 |
| --- | --- |
| 条件源站 | 请求命中条件源站引用的规则条件 |
| 高级回源 | 请求命中高级回源引用的规则条件 |
| 基础源站 | 请求 未命中 任何条件源站 / 高级回源规则（默认兜底） |


## 操作步骤

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

在域名管理页面，找到目标域名，单击操作列的管理。

- 

在源站信息区域，单击条件源站后的展开配置条件源站。

- 

单击新增条件源站。

- 

设置规则条件。

- 

如果是首次添加配置或需要修改已有的规则条件，可以在条件源站对话框中单击规则引擎，在规则引擎中添加或修改配置，具体请参见[规则引擎](products/cdn/documents/user-guide/rules-engine.md)。

- 

如果已有规则条件，从规则条件下拉列表中选择需要引用的规则条件。

- 

在源站地址输入框中，输入源站地址（支持IP源站、域名源站、OSS源站、函数计算源站）。

- 

单击确定，完成配置。

## 示例：/api/* 地址访问 FC 服务，其他地址访问 OSS 服务

高级回源仅支持精确值匹配，不支持通配符或正则表达式。要实现的路径级回源，可以使用条件源站与规则引擎。通过条件源站功能结合规则引擎和 URL 重写，可以实现将/api/*路径的请求路由到函数计算（FC）源站，其他请求默认回源到 OSS 源站。

创建规则引擎规则

- 

登录域名管理，在域名管理页面找到目标域名，进入规则引擎。

- 

单击添加规则，按下表配置规则条件：

| 配置项 | 值 |
| --- | --- |
| 规则名称 | 自定义名称，如 api-to-fc ，便于后续识别 |
| 匹配类型 | URI |
| 匹配运算符 | 包含其中任意一个 |
| 匹配值 | */api/* |
| 大小写敏感 | 忽略大小写 （默认） |


重要

不要添加 hostname 条件。hostname 匹配的是请求域名而非源站，添加 hostname 条件可能导致规则无法匹配 URL 重写后的路径。

- 

单击提交，保存规则。

配置条件源站

- 

在域名管理页面左侧导航栏，进入域名管理>基本配置，在源站信息区域，单击条件源站后的展开图标。

- 

单击新增条件源站，在对话框中按下表配置：

| 配置项 | 值 |
| --- | --- |
| 规则条件 | 在下拉列表中选择步骤一创建的规则（如 api-to-fc ） |
| 源站地址 | 输入函数计算（FC）的源站地址 |


- 

单击确定，完成配置。

配置回源 HOST

在回源配置中，为该规则指定回源 HOST 为 FC 的域名，确保回源请求使用正确的 Host 头。

配置 URL 重写（可选）

如果业务需要将/api/路径重写为 FC 上的/print/api/路径，需配合 CDN 的 URL 重写功能进行配置：

- 

在规则引擎中配置 URL 重写规则，将/api/重写为/print/api/。

- 

确保步骤一中规则引擎的 URI 匹配条件能覆盖重写后的路径（如使用*/api/*或具体匹配/print/api/*）。

完成以上配置后，前端请求/api/*时将路由至 FC 服务，其他请求默认回源至 OSS。

## 示例：基于 Referer 的条件回源

以下示例将根据访问来源（Referer）将请求路由到不同的源站，适用于图片防盗链或来源控制的场景。

### 创建 Referer 规则条件

- 

登录 CDN 控制台，选择目标域名，进入域名管理>规则引擎。

- 

单击添加规则，按下表配置：

| 配置项 | 值 |
| --- | --- |
| 规则名称 | referer-routing （自定义，便于识别） |
| 匹配类型 | Referer |
| 匹配运算符 | 包含其中任意一个 |
| 匹配值 | example.com 目标来源域名。支持配置多个来源域名。 |
| 大小写敏感 | 忽略大小写 |


- 

单击提交，保存规则。

### 配置条件源站

- 

在域名管理页面左侧导航栏，进入基本配置，在源站信息区域单击条件源站后的展开图标。

- 

单击新增条件源站，在对话框中按下表配置：

| 配置项 | 值 |
| --- | --- |
| 规则条件 | 在下拉列表中选择 referer-routing |
| 源站地址 | 输入 Referer 来源对应的专用源站地址 |


- 

单击确定，完成配置。

## 示例：基于 Cookie 的条件回源

以下示例将根据请求携带的 Cookie 值将请求路由到不同的源站，适用于 A/B 测试或灰度发布场景。

### 创建 Cookie 规则条件

- 

登录 CDN 控制台，进入规则引擎页面，单击添加规则。

| 配置项 | 值 |
| --- | --- |
| 规则名称 | cookie-routing （自定义，便于识别） |
| 匹配类型 | Cookie |
| 匹配运算符 | 包含其中任意一个 |
| 匹配值 | ab_test=new_version Cookie 键值对，用于标识灰度用户 |


- 

单击提交，保存规则。

### 配置条件源站

- 

在条件源站配置中，选择cookie-routing规则，关联灰度版本的源站地址。

- 

同时配置一条兜底规则（不匹配cookie-routing的请求），关联默认源站地址。

## 常见问题

### 配置条件源站后，访问资源仍回源到基础源站或出现 404/403 错误，如何排查？

请按以下步骤逐一排查：

- 

检查规则匹配条件：确认请求的 URI、Header 等参数是否命中了您配置的条件规则。注意 URI 路径匹配需使用通配符（如/api/*），通配符*匹配零个或多个字符，?匹配任意单个字符。如果匹配值未加通配符，可能导致无法匹配。

- 

检查回源 Host 配置：如果您的源站是 OSS，确认是否为每个条件源站配置了指定回源 Host，且 Host 值与对应 OSS Bucket 域名完全一致。未正确配置回源 Host 会导致 OSS 签名验证失败，返回 403 错误。

- 

检查源站地址：确认源站地址填写正确且源站服务正常运行。可以通过直接访问 OSS Bucket 域名验证源站是否可达。

- 

检查缓存状态：配置修改后，CDN 边缘节点可能仍保留旧配置下的缓存内容。建议执行[缓存刷新](products/cdn/documents/user-guide/rules-engine.md)操作，以确保新配置立即生效。特别是基于 Cookie 的条件回源规则，若测试时账号未登录（请求不携带 Cookie）或缓存未清理，可能导致规则看似未生效。建议在测试时使用curl -v -H "Cookie: key=value"命令模拟携带 Cookie 的请求，验证规则是否正确匹配。

- 

检查 OSS 权限：若回源 OSS 时返回 403 且错误信息包含 "You have no right to access this object"，检查 OSS Bucket 的 ACL 权限。若 Bucket 为私有权限，需将其设置为公共读或在 CDN 配置回源鉴权。

- 

检查规则条件引用次数：确认单个域名下规则条件的总引用次数未超过 5 次的上限。超限会导致新配置无法生效。

### 如何实现中国内地和非中国内地用户访问不同的源站（流量分流）？

您可以通过条件源站结合规则引擎实现地域分流。具体配置如下：

- 

创建地域规则条件：登录 CDN 控制台，选择目标域名，进入域名管理>规则引擎，单击添加规则。

- 

配置中国内地规则：匹配类型选择用户地理位置，匹配值选择中国内地，关联规则逻辑关系选择或者，保存规则。

- 

配置海外规则（兜底）：匹配类型选择用户地理位置，匹配值选择不包含中国内地，保存规则。

- 

配置条件源站：在源站信息区域，分别为两个规则关联对应的源站：

- 

中国内地规则关联国内源站（如国内 OSS Bucket 或国内服务器）

- 

非中国内地（海外）规则关联海外源站（如海外 OSS Bucket 或海外服务器）

- 

配置回源 Host：为每个源站分别配置指定回源 Host，确保 Host 值与对应源站域名一致。

跨境优化建议

针对非中国内地用户访问中国内地源站延迟高或连接不稳定的场景，建议结合 OSS 传输加速优化跨境回源链路。配置方式如下：

- 

中国内地用户的条件源站回源至 OSS 普通公网域名（如bucket.oss-cn-hangzhou.aliyuncs.com）。

- 

非中国内地用户的条件源站回源至 OSS 传输加速域名（如bucket.oss-accelerate.aliyuncs.com）。

OSS 传输加速利用全球分布的加速节点优化跨境传输链路，可有效降低回源延迟。关于 OSS 传输加速的详细说明，请参见[通过传输加速访问](products/oss/documents/user-guide/transfer-acceleration.md)[OSS](products/oss/documents/user-guide/transfer-acceleration.md)。

### 配置条件源站后，多久生效？是否需要刷新缓存？

生效时间：条件源站配置修改后，通常在 5~10 分钟内全局生效。CDN 配置会逐步推送到各边缘节点，在此期间可能出现新旧配置并存的情况。

缓存刷新建议：

- 

配置生效后，如果CDN 边缘节点已缓存了旧配置下回源获取的内容，建议执行缓存刷新操作，以确保用户访问到最新内容。您可以通过 CDN 控制台手动刷新缓存，或调用RefreshObjectCachesAPI 进行批量刷新。

- 

如果配置修改仅涉及回源规则（不涉及已缓存内容本身），通常不需要刷新缓存，因为回源规则由 CDN 边缘节点实时判断。

说明

对于首次配置条件源站的用户，建议配置完成后使用curl -I命令测试不同路径的回源结果，确认配置已生效。

### CDN 回源私有 OSS 时，如何配合条件源站实现鉴权？

当您的 OSS Bucket 为私有权限时，CDN 回源需要正确的鉴权配置才能正常获取资源。请通过服务关联角色授权 CDN 访问私有 OSS，授权 CDN 服务访问您的私有 OSS Bucket，详细操作参见[OSS](products/cdn/documents/user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[私有](products/cdn/documents/user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[Bucket](products/cdn/documents/user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[回源](products/cdn/documents/user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)。CDN 会通过服务关联角色获取 OSS 访问权限。授权后，CDN 回源私有 Bucket 时自动携带鉴权信息，无需手动配置。

### CDN 与全球加速 GA 联用时出现 502 错误，如何排查？

若 CDN 与全球加速（GA）联动，且配置条件源站后出现 502 错误，请按以下方向排查：

- 

检查回源 Host 配置：使用条件源站时，需删除默认的回源 Host，改为配置指定回源 Host。建议配置两条规则分别处理中国内地和非中国内地流量：一条匹配中国内地流量，源站为中国内地服务器 IP，指定回源 Host 设置为 CDN 加速域名；另一条匹配非中国内地流量，源站为 GA 源站域名，指定回源 Host 设置为 GA 源站域名。

- 

检查协议与端口一致性：确保 GA 监听端口与 CDN 回源端口一致。若 GA 使用 HTTPS 443 端口，建议 CDN 也通过 443 端口回源。若源站未配置 HTTPS 证书，可在 GA 中创建监听 HTTP 80 端口的实例，使 CDN 通过 HTTP 80 端口回源至 GA，避免因协议或端口不匹配导致的 502 错误。

- 

替代方案：若上述配置过于复杂，可考虑迁移至 ESA（边缘安全加速），ESA 支持更灵活的条件源站配置及独立回源端口配置。

### 配置条件源站是否影响防盗链功能？

不影响。防盗链策略（包括 Referer 防盗链、URL 鉴权等）对整个 CDN 域名全局生效，与条件源站配置互不干扰。配置条件源站后，防盗链功能仍按原有策略正常工作。

### CDN 配置条件源站时，源站中是否需要添加对应的 URL 路径？

不需要。源站侧只需配置域名，无需添加 URL 路径规则。CDN 根据请求的完整 URL 进行回源判断：

- 

若请求满足条件源站规则，则回源至对应规则关联的源站。

- 

若不满足任何条件源站规则且存在基础源站，则回源至基础源站。

只需在 CDN 控制台添加对应的源站域名，并为每个条件源站配置指定回源 Host（即源站域名）。无需在源站侧额外配置 URI 匹配规则。

[上一篇：配置源站](products/cdn/documents/user-guide/configure-an-origin-server.md)[下一篇：IPv6配置](products/cdn/documents/user-guide/configure-ipv6.md)

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
