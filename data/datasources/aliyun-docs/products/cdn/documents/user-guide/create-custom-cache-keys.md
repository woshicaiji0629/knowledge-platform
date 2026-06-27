# 自定义Cache Key-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/create-custom-cache-keys

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

# 自定义Cache Key

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

配置自定义缓存键（Cache Key），开发者可以根据HTTP请求的不同部分（例如URI、请求参数、HTTP请求头或自定义变量等）制定规则来生成Cache Key，将访问同一个文件的一类请求转化为统一的Cache Key，提高缓存命中率，降低回源率，减少请求的响应时间和带宽消耗。

## 功能对比与选择

- 

自定义Cache Key与[忽略参数](products/cdn/documents/user-guide/ignore-parameters.md)存在冲突：开启忽略参数后，节点会去除URL中?之后的参数，导致自定义Cache Key中的请求参数配置失效。使用自定义Cache Key前，请关闭忽略参数。

- 

自定义Cache Key功能更全面，可替代忽略参数缓存键配置，推荐优先使用。配置对比：

- 

- 

- 

- 

- 

- 

| 场景 | 忽略参数 | 自定义 Cache Key |
| --- | --- | --- |
| 在缓存键中忽略所有请求参数 | 忽略参数设置为是，保留指定参数留空 | 添加一条请求参数处理策略： 操作方式：保留 参数名：设为任意不存在的参数名，例如 example-argument |
| 在缓存键中仅保留请求参数 key1 | 忽略参数设置为是，保留指定参数设置为 key1 | 添加一条请求参数处理策略： 操作方式：保留 参数名：key1 |
| 在缓存键中仅删除请求参数 key1 | 删除指定参数设置为 key1 | 添加一条请求参数处理策略： 操作方式：删除 参数名：key1 |


- 

回源参数改写：自定义Cache Key功能不修改回源URL，仅修改请求的缓存标识，回源请求与客户端请求内容一致。如果需要改写回源URL携带的请求参数，请使用[重写回源参数](products/cdn/documents/user-guide/rewrite-url-parameters-in-back-to-origin-requests.md)。

- 

缓存刷新：配置自定义 Cache Key 后，[按](products/cdn/documents/user-guide/refresh-and-prefetch-resources.md)[URL](products/cdn/documents/user-guide/refresh-and-prefetch-resources.md)[提交刷新任务](products/cdn/documents/user-guide/refresh-and-prefetch-resources.md)可能无法正确匹配缓存内容，请提交经过自定义Cache Key功能处理后的缓存键作为刷新对象。

## 使用场景

重要

自定义Cache Key功能不会修改回源的URL，仅会修改请求的缓存标识，回源的请求和客户端发起的请求内容保持一致。

Cache Key是一个文件在CDN节点上缓存时唯一的身份ID，每个在CDN节点上缓存的文件都对应一个Cache Key。文件的Cache Key默认为客户端请求的URL（带参数）。

### 场景一

客户不同请求的URL中含有复杂的参数，因此即使多个请求访问的是同一个文件，但由于URL参数不同，CDN节点会视为请求不同文件而将不同请求缓存成多个文件，造成回源的请求增加。

可通过自定义Cache Key规则将同一类请求的Cache Key统一，降低回源率。

### 场景二

客户端请求的URL一样时，CDN将视为请求同一个文件。但实际上请求的Http Header中携带了client字段区分了客户端系统，希望请求不同文件。

此时可通过自定义Cache Key将client字段的值拼接至Cache Key，两个请求即可识别为2个不同的Cache Key。

重要

功能配置在引用规则引擎上的规则条件配置时，配置的执行顺序不是按照配置的优先级顺序执行，而是会按照配置关联的规则条件的优先级顺序来执行。

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

在自定义Cachekey页签下，单击配置，配置Cache Key。

- 

- 

- 

- 

- 

- 

- 

- 

| 参数类型 | 操作说明 |
| --- | --- |
| 规则条件 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 重要 引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](products/cdn/documents/user-guide/rules-engine.md) 中进行管理。 |
| URI | 当客户端请求的 URI 与配置中的 源 URI 相匹配时，系统会用配置中的 目标 URI 替换 源 URI ，来生成 Cache Key。则使用配置中的 目标 URI 替换 源 URI 来拼接 Cache Key。 支持配置多个 URI 替换策略。若存在多条策略，则按照从上到下的顺序依次进行匹配。一旦匹配到某个 源 URI ，系统将使用该策略对应的 目标 URI 执行替换操作，并停止与后续策略的匹配。 源 URI ：以正斜线（/）开头的 URI， 不含 http://头及域名 。支持 PCRE 正则表达式。 目标 URI ：以正斜线（/）开头的 URI， 不含 http://头及域名 。 |
| 请求参数 | 操作的对象是用户发起的原始请求 URL 中携带的参数，可以对参数进行 新增 、 删除 、 修改 、 保留 操作，操作后的结果将会拼接到 Cache Key 中。支持设置多个操作，存在多个操作的情况下，将会从上到下按顺序逐个执行。 新增 ：将新增的请求参数拼接到 Cache Key 中。例如：原始 URL 为 http://image.example.com/cat.jpg ，新增一个请求参数 type=jpg ，则 Cache Key 为 http://image.example.com/cat.jpg?type=jpg 。 删除 ：在生成 Cache Key 的时候删除原始请求 URL 中的指定参数。例如：原始 URL 为 http://image.example.com/cat.jpg?type=jpg ，删除参数 type ，则 Cache Key 为 http://image.example.com/cat.jpg 。 修改 ：在生成 Cache Key 的时候修改原始请求 URL 中的指定参数。例如：原始 URL 为 http://image.example.com/cat.jpg?type=jpg ，修改参数 type=png ，则 Cache Key 为。 保留 ：在生成 Cache Key 的时候仅保留原始请求 URL 中的指定参数。例如：原始 URL 为 http://image.example.com/cat.jpg?type=jpg&path=image ，保留参数 type ，则 Cache Key 为 http://image.example.com/cat.jpg?type=jpg 。 |
| HTTP Header | 将客户端原始请求中携带的指定 HTTP Header 的值拼接到 Cache Key 中。支持配置多个 HTTP Header 名称（多个 HTTP Header 名称之间用空格分隔），效果是每个 HTTP Header 的值将会按顺序拼接到 Cache Key 中。 例如：原始 URL 为 http://image.example.com/cat.jpg ，客户端请求携带了一个 HTTP Header（path:image） ；如果 HTTP Header 中设置了 path 这个请求头，则 Cache Key 为 http://image.example.com/cat.jpgimage 。 |
| 自定义变量 | 可以使用正则表达式来匹配客户端原始请求中携带的指定请求参数的值、指定 HTTP Header 的值、指定 Cookie 参数的值、指定的 URI，正则表达式匹配命中时，将对应的值拼接到 Cache Key 中。具体使用请参见 [配置示例](products/cdn/documents/user-guide/create-custom-cache-keys.md) 。 |


- 

单击确定。

## 配置示例

### URI

客户端的请求http://aliyundoc.com/a/b/image.jpg和http://aliyundoc.com/a/b/c/image.jpg将视为请求同一个文件，该文件的Cache Key为http://aliyundoc.com/c/image.jpg。URI改写规则配置示例：将源URI/a/b改写为目标URI/c，将源URI/a/b/c改写为目标URI/c。单击+ 添加源URI可新增改写规则，单击删除可移除已有规则。

### 请求参数

客户端的请求http://aliyundoc.com/a/b/image.jpg?delete_par=1&modify_par=1将按规则添加add_par=1，删除delete_par，将modify_par的值修改为2，最终转化为http://aliyundoc.com/a/b/image.jpg?modify_par=2&add_par=1。

重要

请求参数中，如对同一个变量同时进行了多个操作，则各种操作的生效优先级：新增>删除>保留>修改。

删除操作仅支持输入单个参数名，如需删除多个参数，可单击添加参数操作增补多条删除操作。

### HTTP Header

客户端请求的HTTP Header的User-Agent和Accept-Language的值将被拼接到Cache Key中。例如请求http://aliyundoc.com/a/b/image.jpg中的User-Agent=Mozilla/5.0 (Linux; X11)，Accept-Language=en，则该请求的Cache Key为：http://aliyundoc.com/a/b/image.jpgMozilla/5.0(Linux;X11)en。在HTTP HEADER输入框中填写需要采集的请求头字段，例如User-Agent和Accept-Language。

### 自定义变量

示例一

变量名为language，来源为Request Header，来源字段名为Accept-Language，匹配规则为([%w]+),([%w]+)，变量表达式为$1aa。自定义变量配置示例：变量名设置为language，来源选择Request Header，来源字段名填写Accept-Language，匹配规则填写([%w]+),([%w]+)，变量表达式填写$1aa。

客户端的请求http://aliyundoc.com/a/b/image.jpg且携带HTTP请求头Accept-Language=en,ch，则匹配规则将匹配到en赋值给变量表达式中的$1。变量表达式还将在末尾拼接上aa，得到enaa的变量并取别名为language，拼接在URL后方形成最终的Cache Key：http://aliyundoc.com/a/b/image.jpgenaa。

说明

变量表达式中的$n的含义是匹配规则中第n个括号所匹配到的内容。例如示例一中Accept-Language=en,ch，匹配规则为([%w]+),([%w]+)，则$1=en，$2=ch。

示例二

变量名为expired，来源为Request Cookie，来源字段名为a，匹配规则为[%w]+:(.*)，变量表达式为$1。自定义变量配置示例： -变量名：expired-来源：Request Cookie-来源字段名：a-匹配规则：[%w]+:(.*)-变量表达式：$1

客户端的请求http://aliyundoc.com/a/b/image.jpg且携带Cookie a=expired_time:12635187，则匹配规则将匹配到12635187赋值给变量表达式中的$1并取别名为expired，拼接在URL后方形成最终的Cache Key：http://aliyundoc.com/a/b/image.jpg12635187。

示例三

同时设置URI规则和自定义变量。

URI：

将所有URI符合/abc/.*/abc的请求都合并成/abc。源URI为/abc/.*/abc，目标URI为/abc。

自定义变量：

变量名为testname，来源为Path，匹配规则为/abc/xyz/(.*)，变量表达式为$1。变量名：testname；来源：Path；匹配规则：/abc/xyz/(.*)；变量表达式：$1

客户端的请求URLhttp://aliyundoc.com/abc/xyz/abc/image.jpg，按URI的配置Cache Key将被合并成http://aliyundoc.com/abc/image.jpg， 然后根据自定义变量的配置该URL将会命中/abc/xyz/(.*)，此时$1将被赋值为abc并拼接到Cache Key中，形成最终的Cache Key：http://aliyundoc.com/abc/image.jpgabc，从而达到两个规则组合使用，实现更复杂的缓存逻辑。

如果没有匹配到Cache Key的自定义变量，则变量表达式$1就不会被拼接到Cache Key中。

示例四

同时设置规则条件和自定义变量，使来自Mobile端和PC端的请求生成不同的Cache Key。

Mobile规则条件：

User-Agent包含*Mobile*,*Android*,*iPhone*,*ipad*其中任意一个

PC规则条件：

User-Agent不包含*Mobile*,*Android*,*iPhone*,*ipad*其中任意一个

Mobile自定义Cache Key：

规则条件选择Mobile，自定义变量的变量名为Mobile，来源为Path，匹配规则为/，变量表达式为+mobile。

PC自定义Cache Key：

规则条件选择PC，自定义变量的变量名为PC，来源为Path，匹配规则为/，变量表达式为+pc。

客户端的请求URLhttp://aliyundoc.com/image.jpg，根据User-Agent的值，请求分别命中Mobile端和PC端的自定义Cache Key规则。Mobile端最终生成的Cache Key为：http://aliyundoc.com/image.jpg+mobile；PC端最终生成的Cache Key为：http://aliyundoc.com/image.jpg+pc。

## 常见问题

### 配置自定义 Cache Key 区分不同 Token 请求后仍命中缓存且未回源怎么办？

配置自定义 Cache Key 区分不同 Token 的请求后，仍出现命中缓存且请求未回源的情况，请按以下步骤排查：

- 

检查配置：确认已将携带 Token 的 HTTP Header 加入自定义 Cache Key，或者将缓存时间设置为 0 秒。

- 

刷新缓存：配置修改后，需提交目录刷新以清除旧缓存。URL 刷新不支持通配符*，建议使用目录刷新。

- 

客户端验证：清除浏览器缓存或重启浏览器后重试，检查响应头中的缓存标识是否为MISS，确认未命中 CDN 缓存。

- 

后端排查：若响应头显示MISS但后端仍无日志，需检查后端负载均衡配置及网关日志，确认请求是否到达源站。

- 

权限核查：若无法查询详细日志，需确认当前账号是否有该 CDN 域名的管理权限，或通过主账号申请AliyunSupportFullAccess权限，提供 EagleID 由拥有域名的账号协助排查。

### 配置自定义 Cache Key 区分移动端和 PC 端缓存后测试未生效怎么办？

配置自定义 Cache Key 区分 Mobile 和 PC 端缓存后测试未生效，请按以下步骤排查：

- 

检查配置冲突：确认未开启忽略参数功能。忽略参数会与自定义 Cache Key 冲突，导致配置不生效。

- 

检查配置完整性：确保 Mobile 和 PC 分别配置了自定义变量。Mobile 规则的变量表达式应设为+mobile，PC 规则的变量表达式应设为+pc。配置示例见本文「示例四」。

- 

等待生效：配置提交后需等待 5～10 分钟全网同步。

- 

进一步排查：如以上步骤确认无误仍未生效，建议提供测试返回的 EagleID 以便查询 CDN 日志进一步排查。

### 未开启 ESA 时是否可以使用自定义 Cache Key？

可以。自定义 Cache Key 是 CDN 的基础缓存配置功能，无需开启 ESA 即可使用。

配置路径：登录[CDN 控制台](https://cdn.console.aliyun.com)>域名管理> 单击目标域名的管理> 左侧导航栏选择缓存配置> 在自定义 Cache Key 页签下单击配置。

重要

若已开启忽略参数功能，需先关闭，否则会导致自定义 Cache Key 中的请求参数配置失效。

### CDN 自定义 Cache Key 能否实现动态接口的缓存效果？

不能。CDN 主要用于静态资源加速，无法实现动态接口的加速效果。自定义 Cache Key 用于优化静态资源的缓存策略（如统一 URL 参数、区分客户端等），不适用于动态接口缓存场景。如需动态内容加速，可使用。

[上一篇：重写访问URL](products/cdn/documents/user-guide/create-an-access-url-rewrite-rule.md)[下一篇：配置共享缓存](products/cdn/documents/user-guide/configure-shared-cache.md)

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
