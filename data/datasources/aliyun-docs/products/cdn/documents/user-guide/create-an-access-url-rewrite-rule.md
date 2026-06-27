# 配置访问URL重写与重定向-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/create-an-access-url-rewrite-rule

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

# 重写访问URL

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

如果源站资源路径变化，CDN节点资源路径也会变化。用户请求的URL路径不变时，CDN节点需要重写请求的URL，将其重定向到目标路径，以减少回源并提升客户端访问性能。

## 背景信息

HTTP 302状态码（302 Found）表示资源临时改变位置。配置访问URL重写后，CDN节点会在HTTP Location头部放置新的URL，客户端收到302响应后会请求新的URL。

配置访问URL重写规则后，CDN节点默认发送302状态码，同时也支持303和307状态码，如果您需要修改状态码，可以通过[填写信息](https://page.aliyun.com/form/act2017566026/index.htm)申请。

| 编码 | 含义 | 处理方法 | 典型应用场景 |
| --- | --- | --- | --- |
| 302 | Found | GET 方法不会发生变更，其他方法有可能会变更为 GET 方法。 | 由于不可预见的原因该页面暂不可用。在这种情况下，搜索引擎不会更新它们的链接。 |
| 303 | See Other | GET 方法不会发生变更，其他方法会变更为 GET 方法（消息主体会丢失）。 | 用于 PUT 或 POST 请求完成之后进行页面跳转，防止由于页面刷新导致的操作的重复触发。 |
| 307 | Temporary Redirect | 方法和消息主体都不发生变化。 | 由于不可预见的原因该页面暂不可用。在这种情况下，搜索引擎不会更新它们的链接。当站点支持非 GET 方法的链接或操作的时候，该状态码优于 302 状态码。 |


重要

单个域名最多可以配置50条重写规则。配置多条规则时，按照CDN控制台访问URL重写列表由上而下的顺序执行。

## 重写访问URL和重写回源路径的区别

- 

- 

| 功能 | 作用对象 | 客户端体验 | 应用场景 |
| --- | --- | --- | --- |
| [重写访问](products/cdn/documents/user-guide/create-an-access-url-rewrite-rule.md) [URL](products/cdn/documents/user-guide/create-an-access-url-rewrite-rule.md) | 影响的是客户端访问的 URL，同时也会改变 CDN 节点回源的 URL。 | 执行规则为 redirect 的情况下，客户端将会使用重定向以后的 URL 重新发起访问请求。 执行规则为 break 的情况下，客户端看到的 URL 与实际访问的 URL 一致，没有变化。 | 常用于将旧域名的 URL 迁移、映射到新域名；或者为移动端和 PC 端提供不同的 URL。 示例 ：访问 old.example.com/hello 时，重写访问 URL 为 new.example.com/hello 。 |
| [重写回源路径](products/cdn/documents/user-guide/rewrite-urls-in-back-to-origin-requests.md) | 影响的是 CDN 节点回源时访问的 URL，而客户端访问的 URL 不变。 | 客户端看到的 URL 与实际访问的 URL 一致，没有变化。 | 常用于隐藏源站的真实 URL 结构，保护源站信息；或者通过 URL 映射，让 CDN 节点回源到不同的源站目录。 示例 ：访问 cdn.example.com/hello 时重写回源 URL 为 origin.example.com/source/hello 。 |


### 重写访问URL示意图

- 

客户端向CDN发起请求，请求的URL为old.example.com/hello。

- 

CDN接收到请求后，根据重写访问URL规则，CDN节点会在给客户端发送的302状态码响应信息的HTTP Location头部中放置新的URL地址信息，将请求的URL重写为new.example.com/hello。

- 

客户端收到302状态码响应之后，将会向新的URL地址发起请求。

- 

CDN节点检查缓存，如果缓存中有重写后URL的内容，直接返回给客户端；如果没有，则CDN节点向源站发起请求，请求的URL为重写后的new.example.com/hello。

- 

源站接收到请求，返回响应内容给CDN节点。

- 

CDN节点将响应内容缓存，并返回给客户端。

### 重写回源路径示意图

- 

客户端向CDN发起请求，请求的URL为cdn.example.com/files/hello.txt。

- 

CDN接收到请求后，检查缓存，如果缓存中有请求URL的内容，直接返回给客户端；如果没有，则CDN节点根据重写回源URL规则，将回源URL重写为origin.example.com/secret/files/hello.txt，向源站发起请求。

- 

源站接收到请求后，向CDN节点返回响应内容。

- 

CDN节点将响应内容缓存，并返回给客户端。

## 操作步骤

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

在域名管理页面，找到目标域名，单击操作列的管理。

- 

在指定域名的左侧导航栏，单击缓存配置。

- 

单击重写访问URL页签。

- 

单击添加，根据您的实际需求，配置访问URL重写参数。

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

| 参数 | 说明 |
| --- | --- |
| 待重写的 Path | 仅支持以 / 开头的 Path，不含协议头和域名；支持 PCRE 正则表达式，如 ^/hello$ 。 URL 中 # 号后的内容属于客户端片段标识符（Fragment Identifier），浏览器不会将其发送到服务端，因此 CDN 重写规则无法匹配 # 后的路径。如需对含 # 片段的 URL 配置跳转，应精确匹配 # 前的路径部分，并为每个目标地址分别配置独立的重写规则。 |
| 目标 Path | 执行规则设置为 break 的情况下，仅支持以 / 开头的 Path，不含协议头和域名。 执行规则设置为 Redirect 的情况下，可以包含协议头和域名。支持 PCRE 正则表达式，例如：常用 $1 、 $2 来捕获待改写 Path 中圆括号内的字符串。 |
| 执行规则 | 默认支持 Redirect 和 break 这两种规则。 Redirect ：如果请求 URL 匹配了某条规则，该请求将会被 302 重定向到目标 URL， 节点返回给客户端的 Location 信息为目标 URL（不修改原始 URL 中的参数）。执行完当前规则后，当存在其他配置规则时，会继续匹配剩余规则。 break ：如果请求 URL 匹配了某条规则，该请求将会被重写为目标 URL（不修改原始 URL 中的参数）。执行完当前规则后，当存在其他配置规则时，将不再匹配剩余规则。 同时支持 空 、 enhance-break 和 enhance_redirect 三种规则，这三种规则需要 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex.htm) 申请后台配置。 空 : 配置了多条规则的情况下，如果请求 URL 匹配了某条规则，执行完当前规则以后，还会继续匹配后续规则。 enhance_break : 和 break 类似，但是会修改包含参数在内的整个 URL。 enhance_redirect : 和 redirect 类似，但是会修改包含参数在内的整个 URL。 说明 不同的执行规则使用的重写方式不同，重写后的 URL 是否支持其他域名、其他协议也存在差异： 空 、 Break 、 enhance_break 采用直接重写用户请求 URL 的方式，不支持重写为其他域名，也不支持重写为其他协议（例如从 HTTP 协议重写为 HTTPS 协议）。 Redirect 、 enhance_redirect 采用 302 跳转方式实现 URL 重写，支持重写为其他域名，也支持重写为其他协议： 302 Location 地址除了可以设置为当前的加速域名，还支持设置为其他域名，可以实现这样的效果：原始 URL 使用的域名是 example.com ，重写后的 URL 使用新的域名 aliyundoc.com 。 302 Location 地址支持使用其他协议，可以实现这样的效果：原始 URL 使用 HTTP 协议，重写后的 URL 使用 HTTPS 协议。 |
| 规则条件 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 重要 引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](products/cdn/documents/user-guide/rules-engine.md) 中进行管理。 |
| Nginx Var | 默认为不勾选，勾选后可以在目标 URL 中使用 Nginx 内置变量。配置示例如下： 待重写的 Path： ^/test.jpg$ 目标 Path： /test.${arg_type} 开启 Nginx 变量计算以后实现的效果是会把${nginx_var}值计算出来，${arg_type}表示原始 URL 中参数 type 的值。 说明 该参数需 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex.htm) 申请后台配置。 |


- 

单击确定，完成配置。

成功配置重写功能后，您可以在重写列表中，对当前的配置进行修改或删除操作。

## 配置示例

### 示例1

客户端请求http://example.aliyundoc.com/hello时，请求中包含/hello，CDN节点会在302状态码的Location信息里写入新的URL地址http://example.aliyundoc.com/index.html，并返回给客户端，客户端对http://example.aliyundoc.com/index.html发起请求。

该规则配置中，待重写的Path为^/hello$，目标Path为/index.html，执行规则选择redirect。

说明

客户端在302重定向的时候，如果Location中不包含协议头和域名，那么会默认使用原始请求的协议头和域名。

### 示例2

客户端请求http://example.aliyundoc.com/hello时，请求中包含/hello，匹配上了正则表达式^/hello$，CDN节点会给客户端响应302状态码，并且在Location信息里写入目标URLhttps://test.aliyundoc.com/index.html，客户端收到响应之后，将会对https://test.aliyundoc.com/index.html发起请求。

配置规则：待重写的Path设置为^/hello$，目标Path设置为https://test.aliyundoc.com/index.html，执行规则设置为redirect。

### 示例3

客户端请求http://www.example.com/cdn/url/http://image.example.com/image/cat.jpg时，请求中包含/cdn/url/http://，匹配上了正则表达式^/cdn/url/http://(.*)，CDN节点会给客户端响应302状态码，并且在Location信息里写入目标URLhttp://image.example.com/image/cat.jpg，客户端收到响应之后，将会对http://image.example.com/image/cat.jpg发起请求。

配置规则：目标Path设置为http://$1，执行规则设置为redirect。

### 示例4

客户端请求http://example.aliyundoc.com/stories/index.html#/voice/318时，URL中#/voice/318属于客户端片段标识符（Fragment Identifier），浏览器不会将该部分发送到服务端。CDN节点收到的实际请求路径仅为/stories/index.html。因此，配置重写规则时，待重写的Path应设置为^/stories/index\.html$来精确匹配#前的路径部分，目标Path设置为目标URL，执行规则设置为Redirect。

如果多个含不同#片段的旧URL需要跳转到不同的目标地址，由于服务端无法区分#后的不同内容，需要为每个不同的源路径分别配置独立的重写规则。

[上一篇：配置自定义页面](products/cdn/documents/user-guide/create-a-custom-error-page.md)[下一篇：自定义Cache Key](products/cdn/documents/user-guide/create-custom-cache-keys.md)

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
