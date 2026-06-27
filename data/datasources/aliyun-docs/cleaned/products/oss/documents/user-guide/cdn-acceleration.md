# 通过CDN加速访问OSS提升静态资源分发速度-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/cdn-acceleration

# 通过CDN加速访问OSS
一键部署
我的部署
CDN加速为OSS提供全球分布式缓存能力。当网站或应用需要向全球用户分发存储在OSS中的静态资源（如图片、音视频、文档）时，通过配置CDN加速，可以显著提升访问速度、降低网络延迟，并削减流量成本。
## 工作原理
CDN加速OSS采用分布式缓存架构，将存储在OSS Bucket（源站）中的静态内容主动分发并缓存到遍布全球的CDN边缘节点上，通过就近访问机制实现加速效果。
请求路由：用户首次请求资源时，请求通过智能DNS解析被路由到地理位置最近且网络状况最优的CDN节点。
回源获取：该CDN节点检测到本地无此资源缓存，随即向OSS源站发起回源请求获取资源内容。
缓存存储：OSS响应资源内容后，CDN节点根据预设缓存规则将资源存储在本地，同时向用户返回资源内容。
缓存命中：后续用户请求相同资源时，CDN节点直接从本地缓存响应，无需回源获取。这一机制大幅缩短访问路径，降低网络延迟，实现访问加速的同时减少源站负载。
## 快速使用
### 前提条件
拥有一个已注册的域名，或[购买一个新域名](https://wanwang.aliyun.com/domain)（支持绑定非阿里云注册的域名）。
如果加速区域包含中国内地，域名必须完成[ICP](https://beian.aliyun.com/)[备案](https://beian.aliyun.com/)。
### 步骤一：添加CDN加速域名并配置源站
前往[CDN](https://cdnnext.console.aliyun.com/domain/list)[控制台](https://cdnnext.console.aliyun.com/domain/list)，单击添加域名。
选择加速区域和业务类型，填写加速域名。加速域名支持主域名（如example.com）或自定义的子域名（如oss.example.com），建议使用子域名以便于管理和扩展。
单击新增源站信息，选择源站信息为OSS域名，并选择目标Bucket域名，单击确定，添加OSS源站。
单击下一步，完成CDN加速域名添加。
CDN加速域名添加完成后，可按照推荐配置的引导流程来添加缓存过期时间、Range回源、HTTPS证书等基础配置，或单击跳过，暂不配置，直接进入CNAME配置。
### 步骤二：配置CNAME解析规则
通过DNS CNAME记录将加速域名指向CDN分配的CNAME地址，实现域名解析到CDN节点的路由功能。以阿里云DNS解析为例进行介绍：
前往[DNS](https://dns.console.aliyun.com/)[控制台](https://dns.console.aliyun.com/)，在目标域名操作列单击解析设置。
单击添加记录，填写以下记录信息，其余配置项可保持默认设置。
| 配置项 | 说明 |
| --- | --- |
| 记录类型 | 选择 CNAME 。 |
| 主机记录 | 填写 @ （主域名）或子域名前缀（如 oss ），根据 CDN 加速域名填写。 |
| 记录值 | 填写向导页或加速域名列表页的 CNAME 值，如 oss.example.com.w.cdngslb.com 。 |
单击确定，按页面提示完成解析记录添加。
说明
DNS解析的生效时间取决于记录的TTL（生存时间）设置，完全生效通常需要几分钟到几小时。配置后立即访问无效属于正常现象，请耐心等待或尝试清除本地DNS缓存。
### 步骤三：设置私有Bucket回源
默认情况下，新创建的Bucket读写权限为私有，通过CDN访问时需要开启私有Bucket回源功能，授权CDN节点访问私有资源。如果Bucket读写权限设为公共读，CDN可直接访问，无需开启此功能。
在[CDN](https://cdnnext.console.aliyun.com/domain/list)[控制台](https://cdnnext.console.aliyun.com/domain/list)单击目标域名，然后在左侧导航栏单击回源配置。
在阿里云OSS私有Bucket回源部分开启私有Bucket回源，回源类型选择同账号回源。
重要
开启私有Bucket回源后，CDN将获得访问私有Bucket的授权，并自动在回源请求中添加签名信息。因此，客户端必须使用不包含签名参数的URL（如http://example.com/example.jpg）进行访问。若URL中仍携带Expires、Signature等签名参数，将导致OSS鉴权失败，返回403错误。
### 步骤四：验证加速效果
配置完成后，通过对比测试验证CDN加速域名的性能提升效果。
获取文件访问URL：
| URL 类型 | 获取方式 |
| --- | --- |
| OSS 默认访问 URL | 前往 [Bucket](https://oss.console.aliyun.com/bucket) [列表](https://oss.console.aliyun.com/bucket) ，单击目标 Bucket，在目标文件操作列单击 详情 ，然后单击 复制文件 URL 。 |
| CDN 加速访问 URL | 使用 CDN 加速域名和文件名构造 URL，如 http://example.com/example.jpg （ 不包含签名信息 ）。 |
验证加速效果：使用专业的测速平台或工具（如[云监控一次性拨测工具](https://cloudmonitornext.console.aliyun.com/disposableTest)），对比两个URL访问同一文件的加载时间。
说明
首次检测时，因CDN节点无缓存需回源获取资源，加速效果可能不明显。请于首次检测后，待CDN缓存生效后再次测试。
检查缓存命中状态：通过浏览器的开发者工具（F12），查看资源请求的响应头中X-Cache字段的值：
| 字段值 | 含义 |
| --- | --- |
| 以 HIT 开头 | 成功命中 CDN 缓存，实现了加速效果。 |
| 以 MISS 开头 | 未命中 CDN 缓存，请求已回源至 OSS 获取资源。 |
## 场景示例
### 视频和大文件加速
对于视频点播、大文件下载等场景，需要特殊配置以确保良好的用户体验。
必要配置
开启Range回源：为加速域名[开启](../../../cdn/documents/user-guide/object-chunking.md)[Range](../../../cdn/documents/user-guide/object-chunking.md)[回源](../../../cdn/documents/user-guide/object-chunking.md)，允许CDN节点按需分片请求大文件，支持视频拖拽播放和断点续传。
配置合理的缓存时间：视频文件通常不频繁更新，建议设置较长的缓存时间（如30天以上），避免频繁回源。
使用资源预热：在视频发布前，使用CDN的[刷新和预热资源](../../../cdn/documents/user-guide/refresh-and-prefetch-resources.md)功能将视频提前分发至边缘节点。
视频码率建议
视频加载速度与码率密切相关。如果用户反馈视频播放卡顿，请检查视频码率：
| 码率范围 | 适用场景 | 说明 |
| --- | --- | --- |
| 500kbps~2000kbps | 移动端、普通画质 | 推荐范围，加载流畅。 |
| 2000kbps~4000kbps | PC 端、高清画质 | 需确保用户带宽充足。 |
| >6000kbps | 超高清/4K | 可能导致加载缓慢，建议提供多码率版本。 |
说明
如果视频码率过高（>10Mbps），即使开启CDN加速也可能出现加载缓慢的问题。建议使用[视频转码](video-transcoding.md)服务降低码率，或提供多码率自适应播放。
### 多Bucket回源配置
当业务架构依赖于多个OSS Bucket存储不同类型或归属的资源时，可通过以下两种方案配置多源回源。
方式一：独立子域名架构
为不同功能或资源类型的Bucket分配独立的、语义化的子域名，并为每个子域名配置单独的CDN加速。
| 资源类型 | 子域名示例 | 配置建议 |
| --- | --- | --- |
| 图片资源 | img.example.com | 配置长期缓存策略以提升访问速度 |
| 音视频资源 | video.example.com | 启用 Range 回源支持断点续传 |
| 敏感文档 | docs.example.com | 单独启用 URL 鉴权保障安全 |
使用独立子域名架构具备以下优势：
语义化子域名便于开发团队识别和维护。
在DNS层面实现流量分流，避免单一域名的并发连接限制。
各Bucket的缓存策略、安全配置、监控告警可独立设置。
独立的监控体系能够精确定位性能瓶颈和异常流量。
方式二：统一域名路径路由
当多个Bucket分属不同业务或应用，却希望对外提供统一访问入口时，可配置单一CDN加速域名，利用[规则引擎](../../../cdn/documents/user-guide/rules-engine.md)将不同访问路径的请求回源至指定Bucket。以加速域名oss.example.com回源两个Bucket（cdn-bucket1、cdn-bucket2）为例：
添加源站信息：将cdn-bucket1和cdn-bucket2添加到加速域名的源站信息中，并为域名[配置](cdn-acceleration.md)[CNAME](cdn-acceleration.md)[解析规则](cdn-acceleration.md)。
添加路径规则：在加速域名的添加规则中，添加两条URL路径规则，分别匹配http://oss.example.com/bucket1/*和http://oss.example.com/bucket2/*。
| 规则名称 | 类型 | 匹配运算符 | 匹配值 |
| --- | --- | --- | --- |
| bucket1（可自定义） | URI | 包含其中任意一个 | /bucket1/* |
| bucket2（可自定义） | URI | 包含其中任意一个 | /bucket2/* |
添加条件源站：在加速域名的基本配置中新增条件源站，按路径规则匹配源站。
| 规则条件 | 源站地址 |
| --- | --- |
| bucket1 | cdn-bucket1.oss-<region-id>.aliyuncs.com |
| bucket2 | cdn-bucket2.oss-<region-id>.aliyuncs.com |
指定源站回源HOST：在加速域名的回源配置中添加指定源站回源HOST，确保回源请求正确到达目标Bucket。
| 源站类型 | 源站地址 | 回源 HOST 类型 | 回源 HOST | 规则条件 |
| --- | --- | --- | --- | --- |
| 基础源站地址 | cdn-bucket1.oss-<region-id>.aliyuncs.com | 基础源站域名 | cdn-bucket1.oss-<region-id>.aliyuncs.com | bucket1 |
| 基础源站地址 | cdn-bucket2.oss-<region-id>.aliyuncs.com | 基础源站域名 | cdn-bucket2.oss-<region-id>.aliyuncs.com | bucket2 |
重写回源URL：在加速域名的回源配置中添加重写回源路径，在回源时自动剥离虚拟路径（如/bucket1），使回源请求路径与Bucket内对象的实际存储路径一致。
| 待重写的 Path | 目标 Path | 执行规则 |
| --- | --- | --- |
| ^/bucket1/(.*)$ | /$1 | break |
| ^/bucket2/(.*)$ | /$1 | break |
效果验证：配置完成后，即可使用单一CDN加速域名根据不同路径访问不同的OSS Bucket资源。如访问http://oss.example.com/bucket1/example.jpg，将回源到cdn-bucket1根目录下的example.jpg文件。
### 跨账号私有回源配置
当业务需要跨账号回源私有Bucket时，如使用A账号的CDN加速域名回源B账号的Bucket，可在CDN加速域名中开启阿里云OSS私有Bucket回源时选择跨账号回源实现。
添加跨账号Bucket源站：新建CDN加速域名添加源站信息时，域名选择OSS自定义源站，并输入需要回源的Bucket域名。
开启跨账号私有Bucket回源：在CDN加速域名的回源配置中，开启阿里云OSS私有Bucket回源，回源类型选择跨账号回源或同账号回源，并输入具有目标Bucket访问权限的AccessKey ID和AccessKey Secret。
## 应用于生产环境
### 最佳实践
安全传输：启用HTTPS
为加速域名[配置](access-oss-by-https-protocol.md)[HTTPS](access-oss-by-https-protocol.md)[证书](access-oss-by-https-protocol.md)，并启用强制HTTPS跳转，实现客户端到CDN节点间的数据加密传输。HTTPS不仅能有效防止数据在传输过程中被窃取或篡改，还能避免浏览器地址栏出现不安全警告，提升用户信任度与品牌形象。
证书配置位置说明
| 访问方式 | 证书配置位置 | 说明 |
| --- | --- | --- |
| 直接访问 OSS 域名 | OSS 控制台 | 在 Bucket 的 Bucket 配置 > 域名管理 中配置 |
| 通过 CDN 加速域名访问 | CDN 控制台 | 在加速域名的 HTTPS 配置 中配置 |
说明
泛域名证书（如*.example.com）只能匹配二级域名，三级域名（如img.cdn.example.com）需要单独申请证书。
OSS不支持HTTP/2协议，如需使用HTTP/2，请通过CDN加速访问。
性能优化：配置综合缓存策略
缓存策略是CDN性能的核心要素，应包含缓存有效期和参数处理两个维度。
设置缓存有效期
通过[配置](../../../cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)[CDN](../../../cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)[缓存过期时间](../../../cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)，最大化缓存命中率：
| 文件类型 | 建议缓存时间 | 说明 |
| --- | --- | --- |
| 不常更新的静态文件（图片、音视频、安装包） | 1 个月以上 | 减少不必要的回源请求 |
| 频繁更新的静态文件（JS、CSS） | 数小时~数天 | 配合版本号（如 style.v1.1.css ）管理 |
| 动态文件或 API（PHP、JSP） | 0 秒（不缓存） | 确保每次请求获取最新内容 |
配置参数处理以启用图片处理
OSS的图片处理（如缩放、裁剪、水印）是高频使用功能。默认情况下，CDN为最大化缓存命中率会过滤全部参数，这会导致?x-oss-process类的图片处理指令失效。为正常使用此功能，需在CDN控制台加速域名的性能优化中修改[忽略参数](../../../cdn/documents/user-guide/ignore-parameters.md)配置。
| 业务场景 | 忽略参数配置 | 说明 |
| --- | --- | --- |
| 纯静态资源分发 | 过滤全部参数 | 最大化缓存命中率 |
| 使用 OSS 图片处理 | 保留全部参数或保留指定参数 x-oss-process | 确保图片处理指令生效 |
| 带版本号的资源 | 保留指定参数 v 或 version | 支持版本号更新缓存 |
可用性保障：使用资源预热与自动刷新
启用缓存后，源站文件的更新将无法立即同步到CDN边缘节点。建议采用以下策略：
资源预热：在版本发布或运营活动前，使用CDN的[刷新和预热资源](../../../cdn/documents/user-guide/refresh-and-prefetch-resources.md)功能将热点资源提前分发至全球节点，避免上线瞬间大量回源请求冲击源站。
缓存自动刷新：在Bucket的Bucket 配置>域名管理中为绑定的域名开启CDN缓存自动刷新。当通过API更新OSS文件时，OSS会自动触发CDN刷新任务。
说明
缓存自动刷新仅在CDN加速与OSS Bucket归属同一阿里云账号时有效，且不保证绝对的及时性。对于时效性要求极高的场景，建议在更新文件后主动使用CDN的刷新功能。
跨域访问：配置CORS策略
当前端应用需要跨域访问CDN加速的OSS资源时，仅在OSS Bucket上配置CORS规则可能因CDN缓存机制而失效。最佳实践是在CDN层面直接配置CORS相关响应头：
在[CDN](https://cdnnext.console.aliyun.com/domain/list)[控制台](https://cdnnext.console.aliyun.com/domain/list)单击加速域名或操作列的管理。
在缓存配置>修改出站响应头中配置响应头参数和响应头值。
| 自定义响应头参数 | 响应头值 | 跨域验证 |
| --- | --- | --- |
| Access-Control-Allow-Origin | * | 开启 |
| Access-Control-Allow-Methods | POST,GET, HEAD, PUT, DELETE | 不涉及 |
| Access-Control-Max-Age | 3600 | 不涉及 |
说明
参数设置仅供参考，请结合实际业务场景进行调整。
性能优化：提升大文件与数据传输效率
开启Range回源：对于音视频点播、大文件分发等场景，[配置](../../../cdn/documents/user-guide/object-chunking.md)[Range](../../../cdn/documents/user-guide/object-chunking.md)[回源](../../../cdn/documents/user-guide/object-chunking.md)功能至关重要。它允许CDN节点按需分片请求大文件，可实现视频拖动播放等高级功能，并显著减少回源流量和首屏等待时间。
优化数据传输：为减小JS、CSS、HTML等文本文件的传输体积，可在CDN控制台开启[Gzip](../../../cdn/documents/user-guide/use-the-gzip-compression-feature.md)[压缩](../../../cdn/documents/user-guide/use-the-gzip-compression-feature.md)或[页面优化](../../../cdn/documents/user-guide/enable-html-optimization.md)功能。
说明
开启页面优化或Gzip压缩功能会改变文件的Content-Length和Content-MD5值。如果业务逻辑依赖这些值进行校验，请谨慎开启。
若同时开启页面优化和Gzip压缩功能，页面优化功能将失效，CDN只会对文件进行Gzip压缩。
平滑上线：零停机域名切换
在将现有业务从OSS Bucket域名切换至CDN加速域名时，应采用分阶段切换策略：
准备阶段：完成CDN加速域名的所有配置，并在测试环境中充分验证其功能和性能表现。
灰度发布阶段（建议在业务低峰期）：采用灰度发布的方式将部分业务流量切换至CDN加速域名，通过逐步放量降低切换风险。
验证阶段：密切监控业务访问日志和错误率，分析响应时间、成功率等关键指标，确保服务正常。
全量发布阶段：经过充分验证后，将全量业务流量切换至CDN加速域名。
回滚预案：如遇问题，立即回滚至Bucket域名，并详细分析问题根因后重新部署。
### 风险防范
流量盗用防护：配置Referer防盗链与URL鉴权
为防止资源被非法站点盗用，产生不必要的流量费用和带宽消耗，必须配置安全防护策略：
Referer防盗链：[配置](../../../cdn/documents/user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[Referer](../../../cdn/documents/user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[黑/白名单](../../../cdn/documents/user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)，通过校验HTTP请求头中的Referer字段，仅允许来自指定域名的访问。
URL鉴权：针对私有权限的OSS Bucket，开启CDN的私有Bucket回源后，CDN节点即获得访问授权，这使得原本需要签名的私有资源能通过CDN域名被公开访问。为恢复对私有资源的安全控制，建议在CDN层面启用[配置](../../../cdn/documents/user-guide/configure-url-signing.md)[URL](../../../cdn/documents/user-guide/configure-url-signing.md)[鉴权](../../../cdn/documents/user-guide/configure-url-signing.md)。
说明
配置CDN加速后，盗链请求可能直接命中CDN缓存而不回源到OSS，从而绕过OSS的防盗链验证。为确保防护有效，必须在CDN层面也配置防盗链规则。
流量异常监控与告警
建议在云监控中为CDN加速域名[设置报警规则](../../../cdn/documents/user-guide/set-an-alert-rule.md)，当CDN流量异常增长时及时发现。
回源链路保障：配置回源SNI与回源HOST
确保CDN与OSS之间的回源通信稳定且安全，是服务可用性的关键保障。
配置回源SNI
为避免不带SNI（Server Name Indication）的CDN回源请求导致OSS访问异常，需在CDN中[配置默认回源](../../../cdn/documents/user-guide/configure-sni.md)[SNI](../../../cdn/documents/user-guide/configure-sni.md)，并设置其与回源HOST相同（回源HOST默认为加速域名）。当回源请求携带SNI时，OSS能够在TLS握手阶段精准识别业务域名，从而返回匹配的证书。若OSS接收到不携带SNI的请求，将无法进行业务域名的精准识别，可能触发更严格的流量限制。
隐藏源站信息
默认情况下，CDN使用Bucket域名回源。当回源出错时（如文件不存在），错误信息中可能暴露OSS Bucket域名，存在安全风险。为隐藏源站信息，可按以下步骤将回源HOST修改为CDN加速域名：
在[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)页面单击目标Bucket名称，然后在Bucket 配置>域名管理中将CDN加速域名绑定到Bucket。
在CDN控制台单击目标加速域名，然后在回源配置>默认回源HOST中单击修改配置，将域名类型修改为加速域名。
行为审计与排障：启用访问日志
生产环境必须具备完善的日志记录能力，以便进行安全审计、性能分析和故障排查。建议在CDN控制台[配置实时日志推送](../../../cdn/documents/user-guide/configure-real-time-log-delivery.md)，将访问日志投递到日志服务SLS。通过SLS，可以对访问行为、流量分布、热门资源、错误请求等进行深度分析和监控告警。
## 计费说明
| 费用类型 | 说明 |
| --- | --- |
| CDN 费用 | 配置 CDN 加速访问 OSS 会产生 CDN 流量费用，详见 [CDN](../../../cdn/documents/product-overview/billing-overview.md) [计费概述](../../../cdn/documents/product-overview/billing-overview.md) 。 |
| OSS 费用 | CDN 节点缓存未命中时回源到 OSS 获取资源，会产生 CDN 回源流出流量费用，详见 [CDN](../traffic-fees.md) [回源流出流量](../traffic-fees.md) 。 |
## 常见问题
为什么CDN回源时出现5xx报错？
5xx错误表示CDN无法成功从OSS源站获取资源，需要从以下方面排查：
| 排查方向 | 检查内容 |
| --- | --- |
| 源站配置 | 检查 CDN 控制台配置的 OSS 源站地址是否正确。 |
| 回源协议 | 如果 CDN 配置了 HTTPS 回源或 [协议跟随回源](../../../cdn/documents/user-guide/configure-the-origin-protocol-policy.md) ，请确保源站支持 HTTPS 访问且 SSL 证书配置正确。 |
| 网络链路 | 测试 CDN 节点或本地到 OSS 源站的网络连通性。CDN 节点是公网节点，源站必须连通公网。 |
| 源站压力 | 在 [CDN](https://cdnnext.console.aliyun.com/monitor/realTime) [实时监控](https://cdnnext.console.aliyun.com/monitor/realTime) 页面观察是否存在突增的带宽和流量。对于热点资源，应进行 [预热资源](../../../cdn/documents/user-guide/refresh-and-prefetch-resources.md) 并 [设置合理的缓存周期](../../../cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md) 。 |
为什么配置静态页面后通过CDN加速访问报错403 Forbidden或You are forbidden to list buckets？
原因分析：此问题通常发生在为配置了[静态网站托管](hosting-static-websites.md)的私有Bucket开启CDN加速后。根本原因在于两种访问机制的冲突：
CDN私有回源时会携带签名信息进行身份验证。
OSS静态网站托管的默认首页功能（如访问/时自动返回index.html）要求访问请求必须是匿名的。
当用户访问加速域名的根目录时，CDN发起带签名的请求访问Bucket根目录。OSS收到签名请求后不会触发静态网站托管逻辑，转而尝试执行ListObjects操作，最终导致403错误。
解决方案：绕过OSS的静态网站托管机制，直接在CDN层面通过[重写访问](../../../cdn/documents/user-guide/create-an-access-url-rewrite-rule.md)[URL](../../../cdn/documents/user-guide/create-an-access-url-rewrite-rule.md)实现同样效果：
| 参数 | 配置值 |
| --- | --- |
| 待重写的 Path | ^/$ （匹配根目录访问） |
| 目标 Path | /index.html （或实际首页文件名） |
| 执行规则 | Redirect |
是否可以通过CDN域名上传文件到OSS？
出于安全考虑，不建议通过CDN域名上传文件到OSS。如果CDN被设置为公共写入，任何人无需身份验证即可通过CDN上传文件到OSS，容易受到恶意上传和数据篡改的攻击。建议在限制最小权限的前提下，使用OSS域名上传文件。
使用CDN加速后OSS下行流量是否会变少？
如果CDN缓存的文件被频繁命中，OSS的公网流出流量会显著降低，从而减少OSS流量成本。
CDN缓存文件被频繁命中的前提是，业务场景中的部分数据在某段时间内被频繁访问，例如网站访问、图片文件下载、游戏发行等场景。缓存命中率越高，回源流量越少，成本节省效果越明显。
如何统计文件的真实访问次数？
启用CDN加速后，OSS的访问日志将无法记录由CDN缓存直接响应的终端用户访问请求，可通过以下方式统计：
| 数据范围 | 获取方式 |
| --- | --- |
| 30 天内的日志数据 | 通过下载 CDN 的 [离线日志](../../../cdn/documents/user-guide/offline-logs-quick-start.md) 进行查看和分析。 |
| 超过 30 天的日志数据 | 在 CDN 中 [配置实时日志推送](../../../cdn/documents/user-guide/configure-real-time-log-delivery.md) 后，在 [CDN](https://cdnnext.console.aliyun.com/log/realtime/pushData) [实时日志数据统计](https://cdnnext.console.aliyun.com/log/realtime/pushData) 页面查看和分析。 |
访问报错403 Forbidden如何排查？
403错误可能来自OSS或CDN的权限拦截，建议直接访问OSS默认域名观察是否正常。
正常：问题在CDN侧，需排查CDN的Referer防盗链、URL鉴权、私有Bucket回源是否开启等配置。
也报403错误：问题在OSS侧，需要排查OSS的Bucket ACL、Referer防盗链、Bucket Policy等配置。
为什么业务切换到CDN后OSS仍产生下行流量费用？
可能原因：
存在直接访问OSS的请求：检查业务代码或第三方系统集成中是否有未替换为CDN加速域名的OSS域名。
CDN缓存未命中导致回源：回源会产生OSS的CDN回源流出流量。检查CDN缓存命中率，如果较低请优化缓存配置。
Bucket为公共读被恶意访问：如果Bucket权限为公共读，可能被恶意访问。建议在业务允许的情况下将Bucket设为私有并开启CDN私有回源。
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
