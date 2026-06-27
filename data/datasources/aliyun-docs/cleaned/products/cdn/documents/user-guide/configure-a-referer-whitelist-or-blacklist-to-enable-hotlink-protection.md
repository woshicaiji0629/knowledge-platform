# 通过设置Referer黑白名单规则来避免网站被恶意盗刷-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection

# 配置Referer黑/白名单
Referer黑/白名单基于HTTP请求头中的Referer字段，通过设置黑名单/白名单来控制访问，防止资源被非法盗用。配置后，CDN会根据Referer信息，允许或拒绝访问请求。
重要
阿里云CDN的Referer黑/白名单功能默认不启用，即任何网站均可访问您的资源。
Referer黑/白名单只是防止CDN流量盗刷的一种方式，更多防护方式参见[防范流量盗刷最佳实践](../use-cases/best-practices-for-preventing-traffic-theft.md)。
将域名添加到Referer黑名单或白名单后，CDN会将该域名的泛域名加入规则名单。例如，填写aliyundoc.com，最终生效的是*.aliyundoc.com，即所有子域名都会生效。
## Referer图解
Referer是用户从一个网站跳转到另一个网站时，记录的第一个网站的URL信息，即表示当前页面是通过哪个页面跳转过来的。具体由协议、域名、路径、查询参数组成，如下图所示。
说明
Referer本质上就是一个URL，即请求链接。
阿里云支持仅域名形式的Referer配置，通过勾选忽略Scheme实现。
## 使用场景
Referer黑/白名单主要用于保护网站的资源不被其他网站直接引用或盗用，常见的使用场景包括：
版权保护：某些网站的内容受版权保护，Referer黑/白名单可以限制只有授权网站访问这些内容，保护版权。
防止热链盗用：Referer黑/白名单确保资源只能在特定网站上使用，防止其他网站直接引用，减少热链盗用。
提高网站安全性：Referer黑/白名单只允许特定网站访问资源，防止恶意盗链、恶意访问或盗取敏感信息。
控制流量来源：Referer黑/白名单限制特定网站的流量访问，有效控制流量来源，提高网站稳定性和安全性。
综上所述，您可以根据需求，在不同场景中使用Referer黑/白名单功能，保护资源、提高安全性和控制流量。
## 工作原理
服务器端检查每个请求的Referer字段，如果Referer字段不是来自白名单配置，就拒绝提供服务，从而节省带宽和服务器资源。CDN的Referer请求规则如下：
如果浏览器携带的Referer与黑名单Referer匹配，或与白名单Referer不匹配，则CDN将拒绝该请求的访问。
如果浏览器携带的Referer与白名单Referer匹配，则CDN将允许该请求的访问。
## 注意事项
配置Referer黑/白名单后，黑名单请求仍可访问CDN节点，但会被拒绝并返回403状态码，CDN日志中也会记录该请求。
Referer黑/白名单功能基于HTTP请求头中的Referer字段设置访问控制规则。黑名单请求被拦截时会产生少量流量费用，使用HTTPS协议访问还会产生HTTPS请求数费用。
由于CDN流量盗刷来自公网访问，所以Referer规则仅限于公网域名匹配。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击访问控制。
在Referer黑/白名单页签，单击修改配置。
根据业务需求，[填写](configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[Referer](configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[配置项](configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)。
单击确定，完成配置。
## Referer配置项说明
| 参数 | 说明 |  |
| --- | --- | --- |
| Referer 类型 | 黑名单 携带黑名单 Referer 的请求均无法访问当前资源。 白名单 只有携带白名单 Referer 的请求才能访问当前资源。 说明 黑名单和白名单互斥，只能选择一种。 |  |
| 规则 | 支持添加多个 Referer 名单，使用回车符分隔。 支持星号（*）作为通配符，匹配所有子域名。如 *.example.com 匹配 example.com 的所有子域名。 支持通配符（*）缺省，匹配自身及其所有子域名。如 example.com 匹配 example.com 和 *.example.com 结果集。 说明 Referer 黑/白名单规则的总长度最长不超过 60 KB。 配置规则不需要填写协议头。 |  |
| 重定向 URL | 请求被拦截后返回 302+Location 头，该项为 Location 头的值，必须以 http:// 或者 https:// 开头，例如： http://www.example.com 。 |  |
| 高级配置 | 允许通过浏览器地址栏直接访问资源 URL | 默认未勾选。勾选后，无论配置的是 Referer 黑名单还是白名单，系统不拦截空 Referer 请求，CDN 节点允许用户访问当前资源。 空 Referer 包括： 用户请求中不携带 Referer 头。 Referer 头值为空。 |
| 精确匹配 | 默认未勾选。勾选后，不再支持通配符（*）缺省。若未使用通配符， example.com 仅匹配 example.com 。 |  |
| 忽略 Scheme | 未勾选 忽略 Scheme 时，请求头中 Referer 必须携带 HTTP 或 HTTPS 协议头。 勾选 忽略 Scheme 后，请求头中 Referer 可不携带 HTTP 或 HTTPS 协议头。 |  |
| 规则条件 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 重要 引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](rules-engine.md) 中进行管理。 |  |
## Referer验证
这里使用curl命令测试，-e后面接referer值，-I后接CDN加速域名。该命令结果返回响应头信息。这里以白名单为例进行验证。
### 场景一：仅设置Referer规则
说明
该场景仅设置Referer规则为aliyun.com，重定向URL、高级配置、规则条件均不配置。
将匹配携带形如http(s)://aliyun.com及其子域名的请求，其他非白名单Referer将被拒绝。
携带主域名的Referer访问测试，命令curl -e http://aliyun.com -I CDN加速域名。
[root@xxx ~]# curl -e http://aliyun.com -I http://referer.n p HTTP/1.1 200 OK Server: Tengine
携带子域名的Referer访问测试，命令curl -e http://sub.aliyun.com -I CDN加速域名。
[root@xxx ~]# curl -e http://sub.aliyun.com -I http://referer.xxx HTTP/1.1 200 OK Server: Tengine
携带其他域名的Referer访问测试，命令curl -e http://aIiyun.com -I CDN加速域名。
[root@xxx ~]# curl -e http://aIiyun.com -I http://referer.xxx HTTP/1.1 403 Forbidden Server: Tengine
空Referer的测试，命令curl -e " " -I CDN加速域名。
[root@ixxxxx ~]# curl -e " " -I http://referer.nxxxxx p HTTP/1.1 403 Forbidden Server: Tengine
仅域名的Referer访问测试，命令curl -e aliyun.com -I CDN加速域名。
[root@i-xxx ~]# curl -e aliyun.com -I http://referer.mxxx HTTP/1.1 403 Forbidden Server: Tengine
### 场景二：设置Referer规则并勾选允许通过浏览器地址栏直接访问资源URL
说明
该场景设置Referer规则为aliyun.com并勾选允许通过浏览器地址栏直接访问资源URL。高级配置其他选项不勾选，重定向URL、规则条件均不配置。
相比场景一中多匹配出空Referer的情形，即携带空Referer和直接访问也将被允许。
不携带Referer的访问测试，命令curl -I CDN加速域名。
[root@ixxxxxxxxxx ~]# curl -I http://referer.mxxxxxxxp HTTP/1.1 200 OK Server: Tengine
携带" "Referer的访问测试，命令curl -e " " -I CDN加速域名。
[root@ixxxxx7 ~]# curl -e " " -I http://referer.mxxxp HTTP/1.1 200 OK Server: Tengine
### 场景三：设置Referer规则并勾选忽略Scheme
说明
该场景设置Referer规则为aliyun.com并勾选忽略scheme。高级配置其他选项不勾选，重定向URL、规则条件均不配置。
同场景一的情形，但允许出现不携带协议头，如仅域名aliyun.com的Referer请求。
不带协议头的Referer访问测试，命令curl -e aliyun.com -I CDN加速域名。
[root@i-xxx z ~]# curl -e aliyun.com -I http://referer.xxx HTTP/1.1 200 OK Server: Tengine
## 常见问题
### 请求中的Referer字段不是应该默认自带HTTP或HTTPS协议头部吗，为什么还会出现没有带上HTTP或HTTPS协议头部的情况？
一般情况下，用户请求中的Referer应该是带有HTTP或HTTPS协议头部的。然而，在某些情况下，可能会出现没有带上HTTP或HTTPS协议头部的Referer的情况。
一种常见的情况是当用户从一个不安全的网站（即未使用HTTP加密）跳转到一个使用HTTPS协议的网站时，浏览器可能会根据安全策略（如Referrer-Policy）修改或去除Referer字段，以保护用户数据的安全性。这种情况下，Referer字段只会包含域名部分，不包含协议头部。
另外，某些浏览器或代理服务器可能会在特定情况下自动去除Referer字段，例如在隐私保护模式下或通过匿名代理访问网站时。
因此，在实际应用中，需要注意处理请求中Referer字段可能没有带上HTTP或HTTPS协议头部的情况，以确保正确判断和使用Referer信息。如果请求中Referer字段没有携带HTTP或HTTPS协议头部，但又想匹配命中该请求，您需要勾选忽略Scheme选项。
### 为什么会出现空Referer，对于此类请求应该怎么处理？
空Referer（也称为Referer头为空）是指在HTTP请求中缺失了Referer请求头部的情况。请求中的Referer头通常包含完整的URI，其中包括协议（如http或https）、主机名，可能还包括路径和查询字符串等。空Referer可能出现的原因：
直接访问：用户直接通过浏览器地址栏输入网址、或通过书签访问、或打开一个新的空白标签页时，都没有来源网页，因此Referer头为空。
用户隐私：用户或用户使用的软件（比如浏览器扩展或隐私模式）可能出于隐私保护考虑故意去除Referer头。
安全协议：从HTTPS页面跳转到HTTP页面的时候，为了安全起见，避免敏感信息泄露，浏览器通常不会发送Referer头。
客户端策略：一些网站或应用程序可能出于安全考虑，通过设置<meta>标签或者HTTP头（如Referrer-Policy）控制Referer的发送。
跨域请求：某些跨域请求可能因浏览器的安全策略而不携带Referer头。
对于带有空Referer的请求，处理方式取决于具体应用场景和安全要求。以下是一些处理建议：
默认策略：如果您的服务不需要依赖Referer信息来作出决策，那么可以允许带有空Referer的请求。
允许访问：对于特定的URL或源，您可以勾选允许通过浏览器地址栏直接访问资源URL选项，只允许来自这些来源的请求，即使Referer为空，CDN节点都将允许用户访问当前的资源。
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
