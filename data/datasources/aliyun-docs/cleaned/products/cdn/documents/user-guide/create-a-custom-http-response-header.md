# 配置缓存出站响应头-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/create-a-custom-http-response-header

# 修改出站响应头
出站响应头是HTTP响应消息头的组成部分之一，可携带特定响应参数并传递给客户端，用来控制缓存行为。通过修改出站响应头，当用户请求加速域名下的资源时，CDN返回的响应消息会携带您配置的响应头，从而实现跨域访问等特定功能。
## 背景信息
出站响应头是HTTP协议中用于控制缓存的机制。当客户端请求资源时，CDN节点返回的HTTP响应头允许在特定条件下缓存内容。
说明
HTTP响应头的配置属于域名维度的配置，一旦配置生效，便会对域名下所有资源的响应消息生效。
配置HTTP响应头仅影响客户端（例如浏览器）的响应行为，不影响CDN节点的缓存行为。泛域名暂不支持修改出站响应头。
## 适用场景
告知客户端CDN响应文件的资源类型：添加响应头Content-Type: text/html告知客户端CDN响应文件的格式是HTML格式。
实现跨域资源访问：当用户请求CDN上某个域名的资源时，您可以在CDN返回的响应消息中配置响应头Access-Control-Allow-Origin，以实现跨域访问，您可以参考[配置跨域资源共享](configure-cors.md)来了解详细信息。阿里云CDN还支持按照已配置CORS规则对接收到的用户的跨域请求进行校验，以实现更灵活的跨域资源访问控制。
自定义响应行为：根据业务需求添加或修改自定义头部信息，调整客户端接收的响应内容和格式。
## 注意事项
在添加了多条配置的情况下，执行顺序按配置列表从上到下，因此需要注意多个配置操作将会叠加，最终结果可能会与预期不符。以下例子中配置2最终生效：
配置1：增加HTTP响应头：cache-control: max-age=3600
配置2：增加HTTP响应头：cache-control: no-cache
引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。
CDN不支持删除或修改Via、EagleId等系统保留响应头。这些Header用于CDN节点信息记录，即使配置删除或修改也无效，系统仍会保留最后一个节点的信息。
出站响应头配置修改后一般在5分钟内生效，无需重新预热（预热不会改变已缓存资源的响应头）。若需确保客户端获取最新的响应头信息，请在控制台对受影响的URL执行[操作步骤](create-a-custom-http-response-header.md)（清除缓存）操作后测试验证。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击缓存配置。
单击修改出站响应头页签。
单击添加，修改出站响应头。
下面以增加出站响应头为例，为您介绍配置方法。
| 参数 | 说明 |
| --- | --- |
| 响应头操作 | 增加、删除、变更和替换指定的响应头。 |
| 自定义响应头参数 | 选择自定义响应头参数。详细信息，请参见 [响应头参数](create-a-custom-http-response-header.md) 。 |
| 自定义响应头名称 | 当自定义响应头参数选择为 自定义 时，需要配置自定义响应头名称。自定义响应头名称要求如下： 由大小写字母、短划线和数字组成。 长度为 1~100 个字符。 |
| 响应头值 | 输入您要设置的响应头值。详细信息，请参见 [响应头参数](create-a-custom-http-response-header.md) 。 |
| 是否允许重复 | 允许 ：保留源站返回的头，同时会加上一个同名的头。 不允许 ：源站返回的头会被新配置的同名头覆盖。 |
| 跨域验证 | 跨域校验默认为关闭状态，只有在 响应头操作 为“增加”且 自定义响应头参数 为“Access-Control-Allow-Origin”的时候才可以配置。 开启 ：开启状态下 CDN 节点将按以下规则对用户做跨域校验，并根据校验结果响应“Access-Control-Allow-Origin”的值。 关闭 ：关闭状态下 CDN 节点不会校验用户请求中携带的 Origin 头，只会固定响应已配置的 Access-Control-Allow-Origin 值。 跨域校验规则请参见 [跨域校验规则](create-a-custom-http-response-header.md) 。 |
| 规则条件 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 重要 引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](rules-engine.md) 中进行管理。 |
单击确定，完成配置。
成功修改出站响应头后，您可以在出站响应头节点HTTP响应头列表中，对当前的配置进行修改或删除操作。
## 配置示例：为PDF文件配置 Cache-Control:no-cache
如果希望客户端对PDF文件进行协商缓存（每次请求都向CDN节点验证文件是否更新），可以通过规则引擎实现：
在添加出站响应头配置时，选择使用规则条件。
设置匹配条件为「文件扩展名」包含.pdf。
配置动作为修改出站响应头，添加cache-control:no-cache。
重要
此配置仅影响CDN返回给客户端的响应头，使客户端进行协商缓存，但不影响CDN节点本身对该PDF文件的缓存策略。
## 跨域校验规则
重要
是否允许重复和跨域校验这两个配置项之间存在互斥，是否允许重复配置为允许的情况下，跨域校验将会失效。
任意匹配：自定义响应头参数Access-Control-Allow-Origin的值设置为*不论用户请求里面是否携带Origin参数，也不论携带的Origin参数为何值，都固定返回Access-Control-Allow-Origin:*。
精确匹配：自定义响应头参数Access-Control-Allow-Origin的值设置了单个或者多个值（多个值之间用,分隔）。
如果用户请求头里携带的Origin参数值与被设置的任意一个值精确匹配，就会响应对应的跨域头。
如果都没有精确匹配上，则不响应跨域头。
泛域名匹配：自定义响应头参数Access-Control-Allow-Origin的值设置了泛域名，则会校验请求头中Origin值是否能匹配上Access-Control-Allow-Origin的泛域名。
您可以参考[配置跨域资源共享](configure-cors.md)来了解如何配置。
## 响应头参数
| 响应头参数 | 说明 | 示例 |
| --- | --- | --- |
| 自定义 | 支持添加自定义响应头。自定义响应头名称要求如下： 由大小写字母、短划线和数字组成。 长度为 1~100 个字符。 | Test-Header |
| Cache-Control | 指定客户端程序请求和响应遵循的缓存机制。 | no-cache |
| Content-Disposition | 指定客户端程序把请求所得的内容存为一个文件时提供的默认的文件名。 | examplefile.txt |
| Content-Type | 指定客户端程序响应对象的内容类型。 | text/plain |
| Pragma | Pragma 是一个在 HTTP/1.0 中规定的通用首部，这个首部通常用于在服务器的响应中定义客户端对文件的缓存行为。 | no-cache |
| Access-Control-Allow-Origin | Access-Control-Allow-Origin 是 HTTP 响应头，用于指示哪些源可以访问资源。它是跨域资源共享（CORS, Cross-Origin Resource Sharing）机制的一部分，该机制允许服务器声明其资源是否可以被某个指定的源（域名）访问。该响应头的值支持以下类型： 通配符 * ：使用通配符表示允许任何源访问资源。这种方式非常宽松，适用于那些公开无需认证或授权即可访问的资源。不过，在生产环境中使用通配符时需要谨慎，因为它可能带来安全风险，比如跨站请求伪造攻击。 单个指定源 ：你可以指定一个具体的源（域名），表示仅允许该特定源访问资源。例如， http://example.com 或 https://api.example.com 。这要求请求必须来自指定的源，否则将被拒绝。 | * http://www.aliyun.com |
| Access-Control-Allow-Methods | 指定允许的跨域请求方法。多个方法用英文逗号 , 分隔。 | POST,GET |
| Access-Control-Allow-Headers | 指定允许的跨域请求字段。 | X-Custom-Header |
| Access-Control-Expose-Headers | 指定允许访问的自定义头信息。 | Content-Length |
| Access-Control-Allow-Credentials | 该响应头表示是否可以将对请求的响应暴露给页面。 返回 true：表示可以暴露。 返回其他值：表示不可以暴露。 | true |
| Access-Control-Max-Age | 指定客户端程序对特定资源的预请求返回结果的缓存时间，单位为秒。 | 600 |
| Content-Security-Policy | 配置内容安全策略（CSP），用于控制页面可以加载哪些资源，防范 XSS 攻击和数据注入等安全威胁。CDN 不对 CSP 策略内容做语义校验，仅校验 HTTP 响应头基本格式。策略内容需为单行字符串，不能包含换行符、非法控制字符或未转义的引号，且不要包含外层双引号。建议先在浏览器开发者工具中验证策略正确性后再填入，或在源站配置 CSP 由 CDN 透传。 | default-src 'self'; script-src 'self' 'unsafe-inline' |
| Permissions-Policy | 配置权限策略，用于控制浏览器特定功能（如摄像头、麦克风、地理位置等）的访问权限。 | camera=(), microphone=() |
说明
响应头值支持配置为“*”，表示任意来源。
响应头值非“*”的情况下，支持配置单个或者多个IP、域名、或者IP和域名混合。相互间用英文（,）分隔。
响应头值非“*”的情况下，必须包含协议头“http:// ”或者“https://”。
响应头值支持携带端口。
响应头值支持泛域名。
说明
CDN支持通过自定义响应头配置 Content-Security-Policy（CSP）和 Permissions-Policy 安全响应头。ALB（应用型负载均衡）本身不支持直接添加这两个安全响应头，如需配置，建议通过CDN或WAF等产品实现。
CSP响应头值不要包含外层双引号，这是常见的配置报错原因。正确格式示例：default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:
浏览器F12开发者工具中的CSP语法提示属于浏览器自身的限制，与实际请求无关，不影响响应头的实际生效，请通过实际请求验证。
## 常见问题
[为什么已经配置了响应头](cache-related-faq.md)[Access-Control-Allow-Origin，但是访问资源仍提示跨域问题，response header](cache-related-faq.md)[中没有配置的响应头？](cache-related-faq.md)
[出站响应头和入站响应头有什么区别？](cache-related-faq.md)
配置自定义响应头后未生效，如何排查？
DNS解析问题：确认域名DNS解析仅保留了CDN的CNAME记录，删除了OSS等源站的直接解析记录，确保流量经过CDN节点。如果流量直接到达源站，CDN配置的响应头不会生效。
源站未返回该响应头：CDN默认透传源站响应头，若源站未返回该Header则CDN也不会返回。请确保源站配置正确并返回该响应头；或在CDN控制台「修改出站响应头」中强制添加该响应头，CDN会在出站时自动添加。
Content-Type等响应头未生效：CDN配置自定义出站响应头仅在请求经过CDN时生效。若源站（如OSS、OBS）在上传文件时未指定正确的Content-Type，可能导致回源获取的元数据与预期不符。建议检查源站上传文件时的Content-Type设置，并提供具体URL进行测试验证。
修改入站响应头配置后未生效，是什么原因？
入站响应头：仅作用于源站返回给CDN节点之间的通信，不影响最终用户收到的响应。
出站响应头：影响CDN返回给最终用户的响应。
如果配置的是「修改入站响应头」（如修改Set-Cookie的domain字段），该配置只会影响源站到CDN节点之间的通信，终端用户不会感知到变化。如需影响终端用户收到的响应，请配置「修改出站响应头」。如仍无效，建议直接在源站修改响应头。
出站响应头配置生效时间及状态一直显示「配置中」，如何处理？
配置一般在5分钟内生效。若长时间显示「配置中」或未生效，请检查：
配置格式是否正确（如响应头值是否符合规范，是否为单行字符串）。
是否已单击确定完成保存。
尝试刷新页面或稍后再次查看状态。
是否支持将出站响应头配置批量添加到多个域名？
支持。可以使用CDN API接口BatchSetCdnDomainConfig进行批量域名配置，通过该接口的功能参数设置响应头添加规则。
前端JavaScript代码中拿不到后端返回的自定义响应头（如filename），如何处理？
清除CDN缓存，确保未缓存旧响应头。
确认源站实际返回的响应头中包含该字段。
在CDN控制台「修改出站响应头」中，显式添加Access-Control-Expose-Headers: <header-name>配置，以覆盖源站的CORS设置，确保前端JavaScript能获取该字段。例如，需要获取filename响应头时，添加Access-Control-Expose-Headers: filename。
使用浏览器无痕模式重新请求，确认问题是否解决。
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
