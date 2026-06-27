# 忽略参数-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/ignore-parameters

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

# 忽略参数

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

开启忽略参数后，CDN 节点会去除请求 URL 参数（? 之后的部分），使不同参数的请求命中同一缓存，从而提高缓存命中率。本文介绍忽略参数的配置方法、功能对比以及常见问题排查。

## 功能对比与选择

- 

[自定义](products/cdn/documents/user-guide/create-custom-cache-keys.md)[Cache Key](products/cdn/documents/user-guide/create-custom-cache-keys.md)与忽略参数存在冲突：开启忽略参数后，节点会去除URL中?之后的参数，导致自定义Cache Key中的请求参数配置失效。使用自定义Cache Key前，请关闭忽略参数。

- 

自定义Cache Key可替代忽略参数的缓存键配置，且功能更全面，推荐优先使用。配置对比：

- 

- 

- 

- 

- 

- 

| 场景 | 忽略参数配置 | 自定义 Cache Key 配置 |
| --- | --- | --- |
| 在缓存键中忽略所有请求参数 | 忽略参数设置为是，保留指定参数留空 | 添加一条请求参数处理策略： 操作方式：保留 参数名：设为任意不存在的参数名，例如 example-argument |
| 在缓存键中仅保留请求参数 key1 | 忽略参数设置为是，保留指定参数设置为 key1 | 添加一条请求参数处理策略： 操作方式：保留 参数名：key1 |
| 在缓存键中仅删除请求参数 key1 | 删除指定参数设置为 key1 | 添加一条请求参数处理策略： 操作方式：删除 参数名：key1 |


- 

[重写回源参数](products/cdn/documents/user-guide/rewrite-url-parameters-in-back-to-origin-requests.md)可替代忽略参数的回源参数重写，且功能更全面，推荐优先使用。

## 功能介绍

### 忽略参数

| 作用 | 适用场景 |
| --- | --- |
| 去除请求 URL 参数（ ? 之后的部分），使携带不同参数的请求命中同一缓存文件，提高缓存命中率、减少回源次数。 | 当 URL 参数与资源内容无关（如用户 UID、渠道来源、推荐码等），建议开启忽略参数。例如，以下两个请求访问同一资源但携带不同 UID： A 用户： http://example.com/1.jpg?uid=123*** B 用户： http://example.com/1.jpg?uid=654*** 未开启忽略参数时，CDN 节点会将 A、B 用户的 URL 视为不同资源，无法命中同一缓存，每次都需回源。开启忽略参数后，CDN 节点会去除 URL 参数，统一使用 http://example.com/1.jpg 匹配缓存。 |


说明

[配置](products/cdn/documents/user-guide/configure-url-signing.md)[URL](products/cdn/documents/user-guide/configure-url-signing.md)[鉴权](products/cdn/documents/user-guide/configure-url-signing.md)的优先级高于忽略参数。鉴权方式A的鉴权信息包含URL参数部分，CDN会先完成鉴权判断，通过后再缓存副本。

### 保留回源参数

| 作用 | 适用场景 |
| --- | --- |
| 回源时保留原始 URL 全部参数，确保源站能接收到用户的关键信息。 | 开启忽略参数后，CDN 节点默认使用去除参数后的 URL 回源。以上述示例为例，A、B 用户的回源请求都使用 http://example.com/1.jpg ，UID 等关键信息会丢失。开启保留回源参数后，CDN 节点将使用原始 URL 回源，确保 UID 等参数传递给源站。 |


## 操作步骤

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

在域名列表单击目标域名，在左侧导航栏，单击性能优化，进入性能优化配置页面。

- 

单击忽略参数区域的修改配置，根据实际需求选择模式并完成配置。

- 

配置完成后，单击确定保存。

重要

- 

切换模式后，原有配置将被清除。

- 

修改忽略参数配置后，边缘节点上已缓存的文件不会自动更新。必须通过控制台执行[URL 刷新](products/cdn/documents/user-guide/refresh-and-prefetch-resources.md)或[目录刷新](products/cdn/documents/user-guide/refresh-and-prefetch-resources.md)，才能使新配置生效并清除旧缓存。否则，用户可能仍会访问到使用旧缓存策略缓存的内容，导致访问异常。

### 模式：保留指定参数

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

| 参数 | 说明 | 示例 |
| --- | --- | --- |
| 忽略参数 | 是 ：开启忽略参数，去除 URL 中 ? 之后的参数。 说明 仅开启 忽略参数 而未设置 保留指定参数 时，将去除 ? 之后的所有参数。 否 ：关闭忽略参数，保留所有 URL 参数。 | 假设原始 URL 为 http://example.com/1.jpg?key1=1&key2=2&key3=3 ，各配置的处理结果如下： 示例一， 忽略所有参数，不保留回源参数 ： 配置： 忽略参数 = 是 ， 保留指定参数 留空， 保留回源参数 = 否 。 缓存 key： http://example.com/1.jpg 回源 URL： http://example.com/1.jpg 示例二， 保留指定参数，不保留回源参数 ： 配置： 忽略参数 = 是 ， 保留指定参数 = key1 ， 保留回源参数 = 否 。 缓存 key： http://example.com/1.jpg?key1=1 回源 URL： http://example.com/1.jpg?key1=1 示例三， 忽略所有参数，保留回源参数 ： 配置： 忽略参数 = 是 ， 保留指定参数 留空， 保留回源参数 = 是 。 缓存 key： http://example.com/1.jpg 回源 URL： http://example.com/1.jpg?key1=1&key2=2&key3=3 示例四， 保留指定参数，保留回源参数 ： 配置： 忽略参数 = 是 ， 保留指定参数 = key1 ， 保留回源参数 = 是 。 缓存 key： http://example.com/1.jpg?key1=1 回源 URL： http://example.com/1.jpg?key1=1&key2=2&key3=3 |
| 保留指定参数 | 配置需要保留的参数名，最多 10 个，多个参数用英文逗号（,）分隔。 |  |
| 保留回源参数 | 是：回源时保留原始 URL 中的所有参数。 否：回源时仅携带与缓存 hashkey 一致的参数（即保留指定的参数）。 |  |
| 规则条件 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 重要 引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](products/cdn/documents/user-guide/rules-engine.md) 中进行管理。 |  |


### 模式：删除指定参数

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

| 参数 | 说明 | 示例 |
| --- | --- | --- |
| 删除指定参数 | 配置需要删除的参数名，最多 10 个，多个参数用空格分隔。 | 假设原始 URL 为 http://example.com/1.jpg?key1=1&key2=2&key3=3 ，各配置的处理结果如下： 示例一， 删除指定参数，不保留回源参数 ： 配置： 删除指定参数 = key1 ， 保留回源参数 = 否 。 缓存 key： http://example.com/1.jpg?key2=2&key3=3 回源 URL： http://example.com/1.jpg?key2=2&key3=3 示例二， 删除指定参数，保留回源参数 ： 配置： 删除指定参数 = key1 ， 保留回源参数 = 是 。 缓存 key： http://example.com/1.jpg?key2=2&key3=3 回源 URL： http://example.com/1.jpg?key1=1&key2=2&key3=3 |
| 保留回源参数 | 是：回源时保留原始 URL 中的所有参数。 否：回源时仅携带与缓存 hashkey 一致的参数（即删除指定参数后的结果）。 |  |
| 规则条件 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 重要 引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](products/cdn/documents/user-guide/rules-engine.md) 中进行管理。 |  |


## 常见问题

### 开启忽略参数后出现业务异常，如何排查？

开启忽略参数后，CDN 会将带不同参数的请求视为同一资源进行缓存。如果 URL 参数涉及以下类型，不应全局忽略：

- 

用户身份标识（如 UID、Token、Session ID）：忽略后会导致鉴权失败或不同用户数据串号。

- 

动态内容区分（如版本号?v=1、分页页码?page=2）：忽略后会导致返回错误的缓存内容。

- 

源站处理指令（如 OSS 图片处理参数x-oss-process）：忽略后会导致处理参数失效，返回未处理的原始资源。

排查与解决方法：

- 

删除或关闭忽略参数的配置。

- 

配置修改后，执行缓存刷新操作（URL 刷新或目录刷新），清除边缘节点的旧缓存。

- 

如果部分参数需要保留，可使用保留指定参数模式，将关键参数（如x-oss-process、token等）设置为保留。

### 修改忽略参数配置后，为什么功能未生效？

修改忽略参数配置后，边缘节点上已缓存的文件不会自动更新。如果配置后仍出现访问异常或回源流量未降低，请按以下步骤排查：

- 

确认配置已保存：登录 CDN 控制台，重新进入忽略参数配置页面，确认当前配置状态与预期一致。

- 

检查是否与自定义 Cache Key 冲突：忽略参数与自定义 Cache Key 功能不可共存。开启忽略参数后，自定义 Cache Key 的请求参数配置将失效。请确认两者未同时启用。

- 

执行缓存刷新：配置修改后立即生效，但已缓存的旧文件仍使用旧策略。必须在[刷新和预热资源](products/cdn/documents/user-guide/refresh-and-prefetch-resources.md)页面执行 URL 刷新或目录刷新，清除旧缓存后新配置才能完全生效。

- 

验证配置生效：使用curl -I "完整URL"命令检查响应头X-Cache字段，确认缓存命中状态是否符合预期。

### 使用 OSS 图片处理或视频截帧时，如何配置忽略参数？

当使用 OSS 图片处理（如x-oss-process=image/resize,w_200）或视频截帧功能时，如果 CDN 域名开启了忽略参数，原图/原视频链接与带处理参数的链接会被缓存为同一份资源，导致访问内容错误。

解决方案：在 CDN 控制台忽略参数配置，将x-oss-process参数设置为保留指定参数模式，使带有图片处理参数的 URL 能够单独缓存，避免与原图/原视频缓存冲突。

### 如何利用忽略参数应对通过 URL 参数绕过缓存的请求？

当攻击者或爬虫通过添加随机无意义参数（如?timestamp=xxx、?random=xxx）请求同一资源时，CDN 会将每个带不同参数的请求视为独立资源，导致缓存命中率降低和回源流量激增。

此时应开启忽略参数功能（或配置忽略所有参数），使携带不同随机参数的请求命中同一缓存，从而有效降低回源压力。例如，配置忽略参数后，以下请求将命中同一缓存：

- 

http://example.com/page.html?t=123456

- 

http://example.com/page.html?t=789012

- 

http://example.com/page.html?random=abc

上述请求在开启忽略参数后，统一使用http://example.com/page.html匹配缓存，有效防御通过 URL 参数绕过缓存的攻击行为。

### 为什么开启了忽略参数，但不同客户端的缓存命中状态不一致（X-Cache 显示 MISS）？

可能原因：

- 

URL 携带未忽略的动态鉴权参数：如 URL 带有auth_key等鉴权参数，每次请求的鉴权值不同，即使开启了忽略参数但未将其保留，CDN 仍会识别为不同资源。

- 

首次访问节点无缓存：资源尚未缓存到特定边缘节点，首次访问必然显示 MISS。

- 

客户端请求头差异：如Accept-Encoding、User-Agent不同可能触发多副本缓存（如 Gzip 版本和非 Gzip 版本分别缓存）。

- 

与自定义Cache Key冲突，配置未生效。

排查方法：在客户端执行curl -I "完整URL"，对比响应头X-Cache和X-Swift-CacheTime确认缓存状态。

解决方案：确认忽略参数配置正确（已开启且关键参数已设置为保留），并确保客户端请求头策略一致。

### 灰度发布或版本更新时，如何通过 URL 参数控制 CDN 获取最新资源？

若开启了忽略参数，CDN 将无法通过 URL 参数（如?v=1、?v=2）区分不同版本。建议采用以下方案：

- 

方案一（推荐）：采用文件版本化命名（如style.v2.css、app.v2.js）而非仅依赖查询参数，以确保用户获取最新内容。

- 

方案二：在发布新版本时，主动调用 CDN[刷新接口](products/cdn/documents/user-guide/refresh-and-prefetch-resources.md)清除旧缓存。

[上一篇：获取信息](products/cdn/documents/user-guide/query-image-information.md)[下一篇：使用阿里云CDN加速后网站访问速度较慢](products/cdn/documents/user-guide/website-access-speed-is-slow-after-using-alibaba-cloud-cdn-1.md)

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
