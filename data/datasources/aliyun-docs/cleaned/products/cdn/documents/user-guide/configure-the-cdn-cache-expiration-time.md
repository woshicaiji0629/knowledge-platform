# 了解CDN默认缓存时间并配置缓存过期时间-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-the-cdn-cache-expiration-time

# 配置CDN缓存过期时间
通过配置缓存过期时间规则，可以精细化控制CDN节点的资源缓存时长，以平衡内容更新、访问性能与回源成本。此文档介绍缓存规则的工作原理、配置方法、验证、排障流程及最佳实践。
## 工作原理
请求到达CDN节点时，系统遵循以下决策流程（序号越小，优先级越高）决定是响应缓存副本，还是回源获取最新内容。
不缓存资源：源站响应pragma:no-cache、cache-control:no-cache（或者no-store，或者max-age=0）时，CDN遵循源站的策略，完全不缓存资源。
遵循控制台缓存规则：CDN控制台为指定目录或文件后缀名设置规则，且源站未配置上述不缓存规则，此时控制台缓存规则为最高优先级策略。
多条控制台缓存规则匹配时的优先级逻辑：
| 场景 | 优先级逻辑 | 示例 |
| --- | --- | --- |
| 权重不同 | 权重值（1-99）大的规则优先生效。 | 规则 A（目录 /image/ ，权重 50）和规则 B（后缀 .jpg ，权重 90）都匹配 image/a.jpg ，则规则 B 生效。 |
| 权重相同 | 先创建的规则优先生效。 | 为域名配置权重同为 60 的目录规则（ /static/ ）和后缀规则（ .js ），若目录规则创建时间早于后缀规则，则 /static/app.js 命中目录规则。 |
请求命中某条缓存规则后，不再继续匹配其他规则。
默认情况下，若源站响应Pragma: no-cache或Cache-Control: no-cache/no-store/max-age=0，CDN节点不缓存该资源。如果需要强制缓存资源，可以在控制台配置缓存过期时间时勾选忽略源站不缓存标头。
CDN遵循源站缓存策略：若请求未命中任何CDN控制台规则，或命中的规则开启了优选遵循源站缓存策略，此时CDN将遵循源站的HTTP响应标头。响应头的优先级由高至低为：cache-control>expires>last-modified>ETag。
| 响应头 | CDN 如何处理 | 注意事项与示例 |
| --- | --- | --- |
| Cache-Control | 优先用 s-maxage （ CDN 缓存时长），其次 max-age 。 | 示例： s-maxage=86400, max-age=3600 |
| Expires | 过期时间，仅当无 Cache-Control 时生效。 | 示例： Expires: Wed, 21 Oct 2025 07:28:00 GMT |
| Last-Modified | Last-Modified 是一个时间戳，表示资源最后被修改的时间。 缓存时间计算规则如下： （当前时间- last-modified ）* 0.1，计算结果在 10 秒~3600 秒及之间的，取计算结果时间；小于 10 秒的，按照 10 秒处理；大于 3600 秒的，按照 3600 秒处理。 | 示例： Last-Modified: Wed, 21 Oct 2023 07:28:00 GMT |
| ETag | ETag 是服务器为每个资源生成的一个唯一标识符，通常是一个哈希值或版本号。 ETag 默认缓存 10 秒。 | 示例： ETag: "abc123" |
CDN不缓存策略：若没有命中CDN控制台的缓存规则，并且源站也没有返回Cache-Control等缓存响应头，则CDN执行不缓存策略。
说明
CDN仅对源站响应200, 203, 206, 300, 301, 308, 410状态码的请求执行缓存策略。如需缓存其他状态码的请求（例如404），需在缓存配置>状态码过期时间页面设置。
## 操作步骤
## 控制台（推荐）
CDN控制台的[域名管理](https://cdn.console.aliyun.com/domain/list)页，单击目标域名右侧的管理。
在缓存配置>缓存过期时间页面单击添加，配置缓存规则。
| 参数名 | 说明 | 默认值/示例 |
| --- | --- | --- |
| 类型 | 支持按目录或文件后缀名指定资源范围。 • 目录：为路径下所有资源统一设置缓存规则。 • 文件后缀名：为指定类型的文件统一设置缓存规则。 | 目录、文件后缀名 |
| 地址 | 根据所选类型填写： • 目录：以 / 开头（如 /static/ ）， / 可匹配所有路径，每次仅支持添加一条。 • 文件后缀名：输入一个或多个后缀，用英文逗号分隔（如 jpg,png,css ），区分大小写，不支持竖线（|）或其他符号。 | /static/ 、 jpg,png,css |
| 过期时间 | 资源在 CDN 节点的缓存时长，最长 3 年。 • 不常更新的静态资源（如图片、安装包）：建议 ≥ 1 个月。 • 频繁更新的静态资源（如 JS/CSS）：建议设置为较短时间（如 1～7 天）。 • 动态内容（如 PHP/JSP）：建议设为 0 秒（不缓存）。 | 0 秒～3 年 |
| 优先遵循源站缓存策略 | 默认关闭。开启后，优先采用源站缓存策略，覆盖本规则配置。 | 关闭 |
| 忽略源站不缓存标头 | 开启后，CDN 将忽略源站返回的以下不缓存指令： Cache-Control: no-store 、 no-cache 、 max-age=0 ，以及 Pragma: no-cache，仍按 CDN 控制台规则缓存。 | 关闭 |
| 客户端跟随 CDN 缓存策略 | 开启后，CDN 会将自身生效的缓存策略（如 max-age=3600 ）通过响应头返回给客户端。 | 关闭 |
| 强制内容重新验证 | 仅在过期时间设为 0 秒时生效。 • 关闭（默认，等同于缓存策略 no-store ）：CDN 节点不缓存文件，每次请求都需要回源获取内容。 • 开启（等同于缓存策略 no-cache ）：CDN 节点会缓存文件，但每次请求都需要回源验证缓存内容（304 机制）。适用于需要实时验证但希望减少源站带宽压力的场景。 | 关闭 |
| 权重 | 规则优先级，取值 1～99，数值越大优先级越高。当多条规则匹配同一资源时，权重值大的规则优先生效；若权重相同，先创建的规则优先生效。建议为具体路径或后缀设置高权重，为根目录 / 设置低权重，以实现精细化控制。 | 1～99 |
| 规则条件 | 可基于请求中的参数（如 Header、URL 参数等）进一步限定规则生效范围。默认不使用；如需配置，请通过规则引擎管理。引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。 | 不使用 |
### 缓存规则匹配逻辑
CDN 缓存过期时间支持两种规则类型，匹配行为有所不同：
目录：使用路径前缀匹配。配置/static/将匹配该目录下所有资源（如/static/image/1.jpg、/static/css/style.css）；配置/将匹配所有路径。目录路径须以正斜线（/）开头，每条规则仅支持添加一个目录。
文件后缀名：使用后缀名精确匹配。输入的后缀名不带点（.），多个后缀名以半角逗号分隔（如jpg,css,js）。后缀名仅允许字母和数字组合，无特定后缀限制——以下类型均可配置：
常见静态资源后缀：jpg、png、gif、css、js、html
字体文件后缀：ttf、otf、woff、woff2、eot
动态页面后缀：php、aspx、jsp
其他任意字母数字组合的后缀
说明
如果同时配置了多条缓存规则（如一条目录规则和一条后缀名规则），当同一请求匹配多条规则时，以权重更高的规则为准。权重相同时，先创建的规则优先生效。具体优先级逻辑请参见上方「工作原理」章节。
如果为缓存规则关联了规则条件（通过规则引擎配置），多个条件之间为"且"（AND）关系，即请求需同时满足所有条件才会命中该规则。
若将全站动态后缀（如aspx）设为不缓存，需确保不影响需要缓存的同类型静态资源。若需缓存字体文件，需单独添加包含对应后缀（如ttf,otf,woff,woff2,eot）的规则。
## API
调用[BatchSetCdnDomainConfig](../developer-reference/api-cdn-2018-05-10-batchsetcdndomainconfig.md)接口，可以批量配置域名。更多功能参数的配置方法，敬请参考[域名配置功能函数](../developer-reference/parameters-for-configuring-features-for-domain-names.md)。
## 使规则变更立即生效
配置变更或新增规则，仅对新缓存的资源生效。变更前已缓存的资源，将继续沿用旧的缓存策略直至过期。
要使新规则立即对全网生效，必须手动清理已有缓存。如果是规则变更，通过[刷新和预热资源](refresh-and-prefetch-resources.md)功能执行刷新操作；如果是新增规则，通过[预热资源](refresh-and-prefetch-resources.md)功能执行预热操作。
## 生效验证
配置完成后，可通过curl命令或浏览器开发者工具查看资源的HTTP响应标头，以判断缓存是否按预期工作。
1. 执行验证命令
在终端上执行以下命令进行测试。
curl -I "https://your.domain.com/path/to/file.jpg"
2. 解读关键响应头
| 响应标头 | 常见值与解读 |
| --- | --- |
| X-Cache | 指示请求是否命中 CDN 缓存。 - HIT ：命中缓存。 - MISS ：未命中缓存，请求已回源获取资源。 |
| Cache-Control | 开启"客户端跟随 CDN 缓存策略"后，此标头会显示 CDN 传递给浏览器的缓存指令，如 max-age=3600 。 |
| X-Swift-CacheTime | 资源在 CDN 节点上配置的缓存总时长，单位为秒。 |
## 应用于生产环境注意事项
版本化文件名（推荐）：更新静态资源（如style.css）时，使用带版本或哈希值的新文件名（如style-v2.css或style-a1b2c3d.css），并更新HTML中的引用。此方式无需手动刷新缓存，可确保用户立即获取最新内容，是推荐的缓存更新方式。
动静分离：为动态和静态资源使用不同域名或目录路径，并配置独立的、高权重的缓存规则，以避免策略混淆。例如，为/static/目录下的所有资源设置长缓存，为/api/目录下的资源设置不缓存。
善用浏览器缓存：开启"客户端跟随缓存策略"，可减少对CDN的重复请求，提升加载速度并节省CDN流量。
避免缓存时间过短：过短的缓存时间会导致CDN频繁回源，无法起到加速效果，反而增加源站的流量消耗和成本。
注意缓存时间过长：过长的缓存时间会导致客户端获取数据更新不及时。对于需频繁更新的内容，务必配合刷新缓存操作或使用版本化文件名。
游戏行业及小文件场景：对于游戏行业的小文件资源（如配置文件、素材包），若更新频率较低（例如每周或每两周更新一次），建议将缓存过期时间设置为 15 天或与资源实际更新周期保持一致，以平衡更新速度与加速效果。过短的缓存时间会导致频繁回源，影响加速效果；过长则可能导致用户获取到旧版本资源。建议结合[刷新预热](refresh-and-prefetch-resources.md)功能，在版本更新时主动刷新缓存。
## HTTP协议缓存控制机制说明
在HTTP协议中定义了三种不同类型的协议头部来实现缓存控制相关的机制：
过期时间校验机制
客户端在向服务端请求资源的过程中，双方将为资源约定一个过期时间，在该过期时间之前，该资源（缓存副本）就是有效的，过了过期时间后，该资源（缓存副本）就会失效。
在HTTP协议中，控制缓存过期时间的Header常见的有下面这些：
| 头部名称 | 协议版本 | 作用 | 示例值 | 类型 |
| --- | --- | --- | --- | --- |
| Pragma | HTTP/1.0 | Pragma 用于表示内容是否为不缓存，通常取值 no-cache，表示文件不缓存，常被用来兼容只支持 HTTP1.0 协议的 Server。 | Pragma:no-cache | 请求/响应 |
| Expires | HTTP/1.0 | Expires 响应头包含日期/时间，表示在此时间之后，缓存内容将会过期。 如果使用了无效的日期，比如 0，则代表该资源已经过期。 | Expires: Wed, 21 Oct 2022 07:28:00 GMT | 响应 |
| Cache-Control | HTTP/1.1 | Cache-Control 响应头可以设置不同的指令来实现灵活的缓存控制，是目前主流客户端（如浏览器等）用于控制缓存的重要头部。 | 以下三个示例表示文件不缓存： Cache-Control:no-cache Cache-Control:no-store Cache-Control:max-age=0 表示缓存有效期 1 小时的示例：Cache-Control:max-age=3600 | 请求/响应 |
资源标签验证机制
客户端在首次向服务端请求资源的过程中，服务端将在响应头中带上资源标签，资源标签可以作为客户端再次请求同一资源时的校验标识。客户端再次请求同一资源时，请求头中将会携带资源标签，若服务端校验后认为该资源没有更新，则响应HTTP状态码304，告诉客户端该资源没有更新，客户端可以继续使用本地缓存；若服务端校验后发现资源标签不匹配，则告诉客户端该资源已经被修改或者已经过期，客户端需要重新获取资源内容。
在HTTP协议中，控制缓存版本的Header常见的有下面这些：
| 头部名称 | 协议版本 | 作用 | 示例值 | 类型 |
| --- | --- | --- | --- | --- |
| Last-Modified | HTTP/1.0 | Last-Modified 表示资源的最后修改时间。 | Last-Modified: Wed, 21 Oct 2015 07:28:00 GMT | 响应 |
| ETag | HTTP/1.1 | ETag 表示当前资源特定版本的唯一标识符。 对比 ETag 能判断资源是否变化，如果没有改变，源站服务器不需要发送完整的响应。 | ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4" | 响应 |
多副本协商机制
缓存软件使用关键字索引在磁盘中缓存的对象，在HTTP/1.0中使用资源的URL作为关键字，但可能存在不同的资源基于同一个URL的情况，要区别它们还需要客户端提供更多的信息，例如：Accept-Language、Accept-Charset等头部，为了支持这种内容协商机制（content negotiation mechanism），HTTP/1.1在响应消息中引入了Vary头部，该头部列出了请求消息中需要包含哪些头部用于内容协商。
多副本协商机制通常使用HTTP协议的Vary头部来区分不同的缓存副本，实现不同的客户端请求同一个资源的时候可以拿到不同缓存副本：
| 头部名称 | 协议版本 | 说明 | 示例值 | 类型 |
| --- | --- | --- | --- | --- |
| Vary | HTTP/1.1 | 常用示例： 服务端指定 Vary: Accept-Encoding ，告知接收端（例如： CDN 节点）对于该资源需缓存两个版本（压缩和未压缩）。客户端向 CDN 请求同一个资源时，老版本浏览器获取未压缩资源（避免兼容性问题），新版本浏览器获取压缩资源（减少数据传输流量）。 服务端指定 Vary: User-Agent ，用来识别发送请求的浏览器类型，告知接收端（例如： CDN 节点），根据不同的浏览器类型缓存对应版本的资源。 | Vary: Accept-Encoding Vary: Accept-Encoding,User-Agent | 响应 |
## 常见问题
[缓存相关常见问题](cache-related-faq.md)
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
