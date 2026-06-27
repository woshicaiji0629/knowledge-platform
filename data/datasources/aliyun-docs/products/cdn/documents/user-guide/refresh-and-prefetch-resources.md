# 刷新和预热CDN节点的缓存资源-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/refresh-and-prefetch-resources

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

# 刷新和预热资源

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

通过刷新功能可删除CDN边缘节点上已缓存的资源，并强制边缘节点回源站获取最新资源，适用于源站资源更新和发布、违规资源清理、域名配置变更等场景；通过预热功能可在业务高峰前预先将热门资源缓存到边缘节点，降低源站压力。

## 功能介绍

### 资源刷新

刷新操作的本质是向边缘节点下发缓存失效指令，而非直接删除文件。边缘节点收到指令后，会将匹配的缓存资源标记为"失效"或"过期"。当用户再次请求该资源时，边缘节点发现缓存已失效，便会回源获取最新资源，并在返回给用户的同时重新缓存。

控制台默认刷新方式说明：在CDN控制台执行目录刷新或正则刷新时，默认采用标记刷新方式。标记刷新仅标记缓存过期，当边缘节点回源时，会携带If-Modified-Since或If-None-Match请求头。若源站返回304 Not Modified，边缘节点将保留旧缓存副本。这种方式可节省回源流量，但在某些场景下（如源站同名更新、违规内容清理、配置变更后）可能导致用户仍访问到旧内容。若需彻底清除缓存，建议使用API调用[刷新缓存](products/cdn/documents/developer-reference/api-cdn-2018-05-10-refreshobjectcaches.md)接口，并将Force参数设置为true进行强制刷新。

适用场景

- 

资源更新和发布：源站的旧资源更新或升级后，为避免用户仍访问到旧的缓存资源，可提交对应资源的URL或目录进行刷新，确保用户访问到最新的资源并缓存至边缘节点。

- 

违规资源清理：源站存在不合规内容时，删除源站资源后，由于边缘节点仍可能存在缓存，资源仍可能被访问到。此时可通过URL刷新功能更新缓存资源，确保违规内容及时清除。

### 资源预热

预热操作由边缘节点根据提交的URL列表，主动向源站发起请求，将资源缓存到边缘节点上，而非源站主动推送。预热可提升新资源或活动页面的首次访问速度，同时减少活动上线时的回源压力，保护源站。

预热机制说明：预热操作默认将资源缓存至L2回源节点（二级缓存层），而非直接分发至所有L1边缘节点。当用户首次访问某资源时，L1边缘节点会从L2回源节点或源站拉取内容并缓存。因此，预热操作主要解决的是降低源站压力的问题，L1边缘节点的全面缓存覆盖依赖于用户的实际访问分布。只有当用户实际访问某L1节点后，该节点完成本地缓存，后续同区域用户才能直接从L1命中缓存获得加速。

适用场景

- 

首次接入CDN：首次接入CDN后，可将热点静态资源提前预热至边缘节点。用户访问时可直接由边缘节点响应，避免初次访问速度慢的问题，提升用户体验。

- 

运营活动：运营大型活动时，提前将活动页涉及的静态资源预热至边缘节点。活动开始后，用户访问的所有静态资源均已缓存至边缘节点，由边缘节点直接响应，确保活动页面快速加载。

- 

安装包或其他大文件发布：新版本安装包或升级包发布前，提前将资源预热至边缘节点。产品正式上线后，用户的下载请求将直接由边缘节点响应，提升下载速度，降低源站压力。

缓存层级与效果

预热操作主要将资源缓存至 L2 汇聚节点，而非所有 L1 边缘节点。用户首次访问时，L1 边缘节点会从 L2 节点或源站拉取资源。因此，预热的主要目的是降低源站压力，而非保证所有 L1 边缘节点立即命中缓存。

- 

效果评估：预热有助于提升缓存命中率，但对于小文件或非热点文件，建议合理评估预热成本。预热会产生回源流量，大致等于单个文件大小乘以 L2 节点数量。

## 前提条件

- 

权限要求：使用 RAM 用户调用刷新预热 API（如cdn:RefreshObjectCaches、cdn:PushObjectCache）或操作控制台时，须授予cdn:RefreshObjectCaches（刷新）和cdn:PushObjectCache（预热）权限。建议遵循最小权限原则，仅授予业务所需的操作权限。详情请参见[CDN](products/cdn/documents/security-and-compliance/custom-policies-for-dcdn.md)[自定义权限策略参考](products/cdn/documents/security-and-compliance/custom-policies-for-dcdn.md)。

- 

URL 格式：提交的 URL 中若包含非 ASCII 字符（如中文、空格等），必须先进行UTF-8百分号编码（Percent-encoding），否则刷新或预热任务可能无法生效。

示例：如https://www.example.com/文档/说明.pdf，须编码为https://www.example.com/%E6%96%87%E6%A1%A3/%E8%AF%B4%E6%98%8E.pdf。

## 刷新与预热注意事项

- 

操作时机：缓存刷新和预热任务都会产生回源流量，建议在业务流量低峰期执行大批量的缓存刷新和缓存预热任务。

- 

[配置共享缓存](products/cdn/documents/user-guide/configure-shared-cache.md)：

- 

使用主域名或任意关联域名提交刷新任务，均可使所有关联域名的缓存失效。

- 

使用主域名提交预热任务，只会预热主域名的回源节点组。需要同时预热关联域名的回源节点组时，需要[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)确认主域名和关联域名的回源节点组是否一致，若一致，预热主域名即可覆盖。

- 

重写访问URL：如果域名配置了[重写访问](products/cdn/documents/user-guide/create-an-access-url-rewrite-rule.md)[URL](products/cdn/documents/user-guide/create-an-access-url-rewrite-rule.md)，节点将使用重写后的 URL 来生成 Cachekey，因此需要提交重写后的 URL 进行刷新预热操作。

- 

刷新与缓存规则的关系：URL 刷新仅使 CDN 边缘节点上的具体资源缓存失效，不会删除或修改您在控制台中配置的目录类型缓存规则。

- 

源站无关性：刷新操作针对 CDN 边缘节点缓存执行，不支持指定只刷新某个源站的缓存。CDN 屏蔽了多源站的差异，刷新会统一作用于所有节点上的匹配资源。

- 

忽略参数场景的刷新：若域名配置了忽略参数缓存规则，URL 刷新时应确保提交的刷新 URL 与实际缓存 Key 匹配，或使用目录刷新。灰度发布期间新旧版本共存时，可通过刷新带版本参数的 URL 获取最新内容。

## 费用说明

刷新和预热功能本身不收取任何操作费用。

但这两种操作都会触发边缘节点回源拉取资源，由此产生的回源流量和回源请求次数将会产生费用。计费标准遵循所使用的源站类型：

- 

源站为阿里云 OSS 时，将按 OSS 的计费规则收取[回源流量费用](products/oss/documents/traffic-fees.md)和[回源请求次数费用](products/oss/documents/api-operation-calling-fees.md)。

- 

源站为 ECS 或其他服务器时，将按其网络带宽或流量计费。

大规模刷新或预热操作（尤其短时间内集中执行）可能导致回源成本增加。

## 操作步骤

### 刷新资源

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击刷新预热。

- 

在刷新缓存/预热缓存页签，选择操作类型为刷新。

- 

根据需求选择刷新方式并提交任务。

| 刷新方式 | 操作说明 |
| --- | --- |
| URL 刷新 | 目的： 精确失效一个或多个具体文件的缓存。 操作： 在 URL 输入框中输入完整的 URL（包含 http:// 或 https:// ），每行一个。一个账号每日最多可提交 10,000 条 URL 刷新。例如： https://www.example.com/static/image.jpg 。 |
| 目录刷新 | 目的： 失效指定 URL 目录下所有文件和子目录的缓存。 操作： 输入完整的目录 URL，须以 / 结尾。例如： https://www.example.com/static/ 。 说明： 此方式为标记刷新。若需强制刷新整个目录，请使用刷新缓存 API 并设置 Force=true 。每次最多可提交 100 条目录刷新，单个域名每分钟最多可提交 100 条目录刷新。 |
| 正则刷新 | 目的： 按正则表达式匹配 URL 路径，批量失效符合规则的资源缓存。适用于精确到路径的刷新场景，例如按版本号、文件类型或路径段批量刷新资源。 操作： 输入带有正则表达式的 URL。例如： https://www.example.com/static/[0-9][a-z].*.jpg 。目前仅支持以下四种正则模式： [0-9] ：匹配任意单个数字（0~9）。示例： img[0-9].jpg 匹配 img0.jpg ~ img9.jpg 。 [a-z] ：匹配任意单个小写字母（a~z）。示例： file[a-z].txt 匹配 filea.txt ~ filez.txt 。 [^/]* ：匹配单个路径段（不包含 / 的任意字符序列）。示例： cdn.aliyun.com/[^/]*.js 匹配根目录下所有 JS 文件。 .* ：匹配任意路径段（包含 / 的任意字符序列）。示例： cdn.aliyun.com/.* 匹配该域名下所有资源。 说明： 此方式为标记刷新。若需强制刷新整个目录，请使用刷新缓存 API 并设置 Force=true 。建议尽量使用更精确的匹配规则，避免非预期的大范围缓存失效。一个账号每日最多可提交 20 条包含正则表达式的 URL。 |


如何实现全站刷新（全局/根目录刷新）

CDN 不支持一键全站刷新，但您可以通过以下方式实现全站刷新：

- 

目录刷新：在操作方式中选择目录，输入域名根目录 URL（如https://www.example.com/）。URL 必须以/结尾。

- 

强制刷新（API）：若目录刷新后部分节点仍返回旧缓存，建议调用[刷新缓存 API](products/cdn/documents/developer-reference/api-cdn-2018-05-10-refreshobjectcaches.md)（RefreshObjectCaches），将Force参数设置为true进行强制刷新。强制刷新将无条件删除节点上的缓存资源，确保下次访问回源获取最新内容。

说明

控制台的刷新表单不支持设置Force参数，如需使用强制刷新，请通过 API 或 SDK 调用。

- 

单击提交，系统开始执行刷新任务。

- 

刷新任务一旦提交成功，无法中止。

- 

刷新任务通常需要 5~6 分钟在全网生效。如果缓存过期时间小于此值，则无需手动刷新。

- 

如果在OSS控制台开启了[CDN](products/oss/documents/user-guide/cdn-acceleration.md)[缓存自动刷新](products/oss/documents/user-guide/cdn-acceleration.md)，则无法通过 CDN 控制台查看 OSS 的缓存自动刷新任务。

### 预热资源

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击刷新预热。

- 

在刷新缓存/预热缓存页签，选择操作类型为预热。

- 

在URL输入框中输入需要预热的完整文件 URL，每行一个。不支持预热目录。例如：https://www.example.com/install/package.zip。

- 

单击提交，系统开始执行预热任务。

- 

预热任务一旦提交成功，无法中止。

- 

预热任务的完成时间取决于文件大小、数量和源站性能，通常需要 5~30 分钟。

预热 OSS 文件注意事项

当源站为 OSS 时，预热 URL 须注意以下规范：

- 

URL 格式：必须填写 CDN 加速域名的完整 URL（如https://cdn.example.com/path/file.zip），不能填写源站 OSS 的内网或外网地址（如https://examplebucket.oss-cn-hangzhou.aliyuncs.com/...）。

- 

签名参数：预热 URL 中不得包含 OSS 的临时签名参数（如Expires、OSSAccessKeyId、Signature等）。这些是临时授权参数，会导致预热失败。请使用不含签名的永久可访问 URL。

- 

源站响应状态码：预热要求源站返回200状态码。若源站返回308重定向或其他非200状态码，预热任务将失败。例如，URL 末尾缺少斜杠导致 OSS 返回重定向时，应补全斜杠后重新提交。

| 参数 | 说明 |
| --- | --- |
| 预热类型 | 仅支持 URL 预热，不支持目录预热。 |
| URL | 输入的 URL 须带有 http:// 或 https:// ，预热 URL 须为精确的资源文件路径，不支持输入以 / 结尾的目录。预热多个 URL 时，请按一行一个 URL 输入。 URL 预热配额（每日）： 默认情况下，一个账号每日最多可提交 1000 条 URL 预热任务，如账号日带宽峰值大于 200Mbps，可申请提升每日配额，阿里云将根据实际业务需求进行评估和配置。每次最多可提交 100 条 URL 预热任务。 预热队列规则： 每个账号的预热队列最大为 100,000 条 URL，按 URL 提交先后顺序进行预热；当预热队列中待预热的 URL 达到 100,000 条时，将拒绝接收新的预热任务。 预热速度： 预热任务的执行速度与需要预热资源的文件平均大小有关，文件平均大小越小，预热速度越快。 |


### 自动化刷新或预热

存在以下情况时，建议[使用自动化脚本刷新和预热](products/cdn/documents/user-guide/run-scripts-to-refresh-and-prefetch-content.md)：

- 

无开发人员，需手动提交刷新预热任务，运维成本高。

- 

刷新或预热URL过多，分批提交导致效率低。

- 

需要人工或程序判断刷新预热任务是否正常进行。

## 验证结果

手动查询

操作记录页签可查看资源刷新或预热的详细记录和进度。进度为100%表示任务执行完成。刷新或预热的数量过多会影响任务的完成进度，请耐心等待。

接口查询

调用[查询刷新预热任务-按](products/cdn/documents/developer-reference/api-cdn-2018-05-10-describerefreshtaskbyid.md)[ID](products/cdn/documents/developer-reference/api-cdn-2018-05-10-describerefreshtaskbyid.md)接口，查询刷新或预热任务是否完成。

命令行验证

执行命令curl -I <资源链接>，系统显示结果如下：

存在X-Cache的情况：

- 

X-Cache为HIT，说明此次请求命中缓存，预热成功。

- 

X-Cache为MISS，说明此次请求未命中缓存，预热任务未完成或预热失败，请重新预热。

不存在X-Cache的情况：

如果不存在X-Cache，说明该资源未接入CDN，请参照[快速接入阿里云](products/cdn/documents/getting-started/quick-access-to-alibaba-cloud-cdn.md)[CDN](products/cdn/documents/getting-started/quick-access-to-alibaba-cloud-cdn.md)，先将该URL的域名接入阿里云CDN，再进行资源的预热。

## 使用限制

刷新和预热功能存在配额限制，超出限制后任务将被拒绝。如需提升配额，可前往配额管理申请：

| 操作类型 | 方式 | 配额限制 | 管理额度 |
| --- | --- | --- | --- |
| 刷新 | URL 刷新 | 每个账号每日最多 10000 条 | 配额提升申请或特殊场景审批，审批通常需要 1 个工作日： [配额管理](products/cdn/documents/user-guide/quota-management.md) |
| 目录刷新 | 每次最多提交 100 条；每个域名每分钟最多 100 条 |  |  |
| 正则刷新 | 每个账号每日最多 20 条 |  |  |
| 预热 | URL 预热 | 每次最多提交 100 条；每个账号每日最多 1000 条 |  |


大量文件预热的最佳实践

- 

不支持目录预热：预热仅支持提交具体文件的 URL，不支持输入以/结尾的目录路径。

- 

大文件优先：若您的源站（如 OSS）有大量文件需要预热，建议仅对大文件（如安装包、视频等）进行预热。小文件通常无需预热，可在用户首次访问时自动缓存到边缘节点。

- 

配额与队列：每个账号每日默认 1000 条 URL 预热配额，预热队列最大容量为 100,000 条 URL。

- 

回源流量：预热会触发所有 L2 汇聚节点向源站回源拉取资源，可能产生较高的回源流量（大致等于文件大小 × L2 节点数）。建议仅在业务高峰前对关键资源进行预热。对于视频类业务，建议配合 Range 回源优化，避免全量预热导致回源流量过高。

## 参考：CDN的缓存刷新机制

CDN 针对目录刷新和正则刷新提供两种缓存刷新机制：标记刷新和强制刷新，适用于不同场景，帮助灵活高效地管理缓存内容。

### 标记刷新（CDN默认策略）

- 

适用场景：常规内容更新，如发布新版静态文件。

- 

机制：这是目录刷新和正则刷新在控制台上的默认行为。CDN 边缘节点在回源时，会携带If-Modified-Since或If-None-Match请求头。源站会根据这些头信息判断资源是否已更新。

- 

效果：如果源站资源未变更，源站将返回304 Not Modified状态码，CDN 边缘节点会继续使用旧的缓存副本，不会消耗回源流量。这是一种节省成本和源站资源的优化方式。若需彻底清除缓存（如违规清理、配置变更、同名文件更新），标记刷新可能无法满足需求，请使用强制刷新。

### 强制刷新

- 

适用场景：紧急清理违规或错误资源、修复错误的Cache-Control响应头配置后需要强制全网更新、源站文件同名更新等场景。

- 

机制：通过[刷新缓存](products/cdn/documents/developer-reference/api-cdn-2018-05-10-refreshobjectcaches.md)提交刷新任务时，将参数Force设置为true来触发。此模式下，CDN 边缘节点会无条件地将缓存资源标记为失效，不再进行304校验。

- 

效果：下次访问该资源时，CDN 边缘节点将必须回源获取新版本，即使源站上的文件并未改变。

强制刷新的典型应用场景

以下场景建议使用强制刷新（通过[刷新缓存 API](products/cdn/documents/developer-reference/api-cdn-2018-05-10-refreshobjectcaches.md)设置Force=true）：

- 

违规内容或木马清理：源站删除恶意文件后，必须使用强制刷新，或确保源站对该 URL 返回正确的 HTTP 状态码（如404）。否则边缘节点可能因标记刷新回源校验后仍保留旧缓存，继续提供违规内容。

- 

同名文件更新（配置变更）：若源站文件同名替换但内容不同，标记刷新可能因源站返回304 Not Modified状态码而继续使用旧缓存。此时应使用强制刷新确保全网更新到最新内容。

- 

页面显示异常或首页循环：若访问网站其他页面时一直显示首页，或图片显示异常，且 URL 刷新无效，建议使用目录刷新并通过 API 设置Force=true进行强制刷新。

API 强制刷新参数示例：

{ "ObjectType": "Directory", "ObjectPath": "https://www.example.com/static/", "Force": true }

关键参数说明：

- 

ObjectType：填写Directory（目录）或File（文件）。

- 

ObjectPath：填写以/结尾的完整目录路径，或具体的文件URL。

- 

Force：设置为true开启强制刷新，忽略源站的If-Modified-Since/If-None-Match校验，直接清除缓存。

## 常见问题

[刷新和预热相关常见问题](products/cdn/documents/user-guide/refresh-and-warm-up-related-faq.md)

[上一篇：刷新和预热](products/cdn/documents/user-guide/refresh-and-prefetch.md)[下一篇：使用自动化脚本刷新和预热](products/cdn/documents/user-guide/run-scripts-to-refresh-and-prefetch-content.md)

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
