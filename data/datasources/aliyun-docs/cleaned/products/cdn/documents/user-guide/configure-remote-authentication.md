# 配置远程鉴权-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-remote-authentication

# 配置远程鉴权
如果您有自己的鉴权服务器，可以通过配置远程鉴权，将用户请求转发至您指定的鉴权服务器，由鉴权服务器对用户请求进行校验。
## 功能介绍
远程鉴权和URL鉴权的作用一样，都用于保护资源，让资源只被授权成功的用户访问，非授权用户将无法访问。这两个功能在技术实现方案上有如下差异：
URL鉴权：用户把域名的鉴权规则下发给CDN节点，由CDN节点完成鉴权的整个数据交互流程。
远程鉴权：用户有自己单独设置的鉴权服务器，CDN节点收到用户请求后，需要把用户请求转发给鉴权服务器完成鉴权，鉴权服务器由用户自主管理。
远程鉴权功能的数据交互流程如下：
| 序号 | 交互说明 |
| --- | --- |
| ① | 用户发起的资源访问请求到达 CDN 节点，请求中携带了鉴权参数。例如： 原始请求 URL： https://example.com/123/test.txt?key=xxxxxxxxxx 原始请求中携带 Header： test=123 |
| ② | CDN 节点收到用户请求，将用户请求直接转发（或者经过指定的规则处理后转发）给鉴权服务器。例如： 鉴权服务器地址： https://192.0.2.1/auth CDN 控制台上的远程鉴权功能设置为： 保留所有请求参数 、 保留所有请求 header CDN 转发给鉴权服务器的请求 URL 为： https://192.0.2.1/auth?key=xxxxxxxxxx CDN 转发给鉴权服务器的请求包含 header： test=123 |
| ③ | 鉴权服务器根据用户请求中携带的鉴权参数给出鉴权结果，并返回给 CDN 节点。 |
| ④ | CDN 节点根据鉴权服务器返回的鉴权结果执行对应的动作，并返回对应的数据给用户。 鉴权结果举例说明如下： 举例 1：鉴权成功， CDN 节点与用户开始正常的缓存数据访问交互。 举例 2：鉴权失败， CDN 节点返回 403 状态码给用户。 举例 3：鉴权失败， CDN 节点对用户访问进行限速。 举例 4：鉴权超时， CDN 节点执行鉴权超时的默认动作，即放行或者拒绝用户请求。 |
## 注意事项
配置远程鉴权后，鉴权失败的请求仍可访问到CDN节点，但会被CDN节点拒绝并返回403状态码，CDN日志中仍会记录客户端的请求记录。
由于远程鉴权，将用户请求转发至您指定的鉴权服务器，由鉴权服务器对用户请求进行校验，因此在恶意请求被CDN节点拦截的同时，会产生少量的流量费用，如果客户端使用HTTPS协议访问，还会产生HTTPS请求数费用（因为拦截恶意请求的时候，也同时消耗了CDN节点的处理资源）。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击访问控制。
单击远程鉴权页签。
打开远程鉴权开关，根据界面提示，配置远程鉴权信息。
说明
开启远程鉴权功能后，用户的每次请求都要转发给鉴权服务器处理，当请求访问量大时，需考虑鉴权服务器的压力和性能。
| 参数 | 说明 |  |
| --- | --- | --- |
| 鉴权服务器地址 | 鉴权服务器对外可以访问的地址。系统会对您输入的鉴权服务器地址进行校验，包括格式校验和值校验。 格式要求 鉴权地址支持 HTTP 协议和 HTTPS 协议，格式请参考以下几种类型： http://example.com/auth https://example.com/auth http://192.0.2.1/auth https://192.0.2.1/auth 值要求 值不能包含 127.0.0.1 和 localhost，因为这类本地地址属于无效地址。 |  |
| 请求方法 | 鉴权服务器支持的请求方法。支持 GET 、 HEAD 和 POST 这三种请求方法，默认使用 GET 方法请求。 |  |
| 鉴权文件类型 | 所有文件类型 ：所有的文件类型都参与鉴权。 指定文件类型 ：仅指定的文件类型参与鉴权。 指定文件类型时，如果您输入多个文件类型，多个文件类型用竖线（|）分隔，例如：mp4|flv。 文件类型区分大小写，即.jpg 和 JPG 是两种不同的文件类型。 |  |
| URL 鉴权参数 | 保留参数设置 | 用于控制用户请求 URL 中需要参与鉴权的参数。可以选择 保留所有参数 、 保留指定参数 和 删除所有 URL 参数 。 保留指定参数时，多个参数用竖线（|）分隔，例如：user|token。 参数区分大小写，即 key 和 KEY 是两种不同的参数。 |
| 添加自定义参数 | 为 CDN 节点转发给鉴权服务器的请求 URL 添加自定义参数。您可以自定义设置参数和取值，也可以直接使用 CDN 控制台上预设的变量。 自定义设置参数和取值时，要求如下： 多个参数用竖线（|）分隔，例如： token=$arg_token|vendor=ali_cdn 。 参数值区分大小写，即 key 和 KEY 是两种不同的参数值。 使用预设变量时，您可以提取变量的值添加到 CDN 转发给鉴权服务器的请求上。 例如，选择提取变量$http_host，则用户请求的 URL 地址会加上 host=$http_host，此处的 host 表示用户请求头中的 host 值。变量名称与变量含义的介绍，请参见 [变量名称](configure-remote-authentication.md) 。 |  |
| 请求头鉴权参数 | 保留请求头设置 | 用于控制用户请求头中需要参与鉴权的参数。可以选择 保留所有参数 、 保留指定参数 和 删除所有 URL 参数 。 保留指定参数时，多个请求头用竖线（|）分隔，例如：user_agent|referer|cookies。 参数不区分大小写，即 http_remote_addr 和 HTTP_Remote_Addr 一样。 说明 选择“保留所有参数”时， CDN 节点默认会删除 HOST 头，如果您需要保留 HOST 头，可通过“保留指定参数”或者“添加自定义参数”来保留。 CDN 节点默认删除 HOST 头的原因是 CDN 节点转发给鉴权服务器的鉴权请求中携带的 HOST 头是加速域名，这可能会导致鉴权服务器无法识别鉴权请求，从而导致访问时返回 404 状态码，导致鉴权失败。 |
| 添加自定义参数 | 用于 CDN 节点转发给鉴权服务器的请求头添加自定义参数。您可以自定义设置参数和取值，也可以直接使用 CDN 控制台上预设的变量。 自定义设置参数和取值时，要求如下： 多个请求头用竖线（|）分隔，例如： User-Agent=$http_user_agent|vendor=ali_cdn 。 参数不区分大小写，即 http_remote_addr 和 HTTP_Remote_Addr 一样。 使用预设变量时，您可以提取变量的值添加到 CDN 转发给鉴权服务器的请求上。 例如，选择提取变量$http_host，则用户请求的 URL 地址会加上 host=$http_host，此处的 host 表示用户请求头中的 host 值。变量名称与变量含义的介绍，请参见 [变量名称](configure-remote-authentication.md) 。 |  |
| 鉴权结果对应状态码 | 鉴权成功状态码 | 说明 鉴权服务器在鉴权成功时，会向 CDN 返回特定的 HTTP 状态码。您可以配置多个状态码，多个状态码之间需用英文逗号分隔。 示例 若将鉴权成功状态码设置为 200,206 ，则当鉴权服务器返回 200 或 206 时，表示鉴权成功。 异常处理机制 为避免因异常情况导致所有用户请求被阻断，如果鉴权服务器返回的状态码既不属于成功状态码，也不属于失败状态码， CDN 节点将默认放过该请求。 |
| 鉴权失败状态码 | 说明 鉴权服务器在鉴权失败时，会向 CDN 返回特定的 HTTP 状态码。您可以配置多个状态码，多个状态码之间需用英文逗号分隔。 示例 若将鉴权失败状态码设置为 400,403 ，则当鉴权服务器返回 400 或 403 时，表示鉴权失败。 异常处理机制 为避免因异常情况导致所有用户请求被阻断，如果鉴权服务器返回的状态码既不属于成功状态码，也不属于失败状态码， CDN 节点将默认放过该请求。 |  |
| 其他状态码是否放行 | 是 ：为避免因为一些异常情况阻断所有的用户请求，如果鉴权服务器返回的状态码既不是成功状态码，也不是失败状态码， CDN 节点默认放过用户请求。 说明 例如： 鉴权成功状态码设置为 200，鉴权服务器返回 201 时，结果为放过用户请求。 鉴权失败状态码设置为 403，鉴权服务器返回 404 时，结果为放过用户请求。 否 ：表示在鉴权服务器返回的状态码既不是成功状态码，也不是失败状态码的情况下， CDN 节点将会拒绝用户请求。 |  |
| 鉴权失败之后 CDN 执行的操作 | 响应自定义状态码 | 用户请求鉴权失败时， CDN 节点返回给用户的状态码。 例如，将响应自定义状态码设置为 403，当用户请求鉴权失败时， CDN 节点会返回 403 给用户。 |
| 鉴权超时配置 | 鉴权超时时长 | 统计的是从 CDN 节点发起鉴权请求开始，到 CDN 节点收到鉴权服务器返回的结果为止的时间。单位为毫秒，鉴权超时时长最长可以设置为 3000。 |
| 鉴权超时之后的动作 | CDN 与鉴权服务器之间的数据交互超时后， CDN 对用户请求的处理。支持 通过 和 拒绝 这两种动作，区别如下： 通过 ：鉴权超时， CDN 将直接允许用户请求。 拒绝 ：鉴权超时， CDN 拒绝用户请求，返回上面配置的 响应自定义状态码 给用户。 |  |
单击确定，完成配置。
成功配置远程鉴权功能后，您可以在远程鉴权页签下，对当前的配置进行修改或关闭远程鉴权功能。
## 变量名称
添加自定义参数时，您可以选择直接使用CDN控制台上预设的变量。变量名称与变量含义见下表。
| 变量名称 | 变量含义 |
| --- | --- |
| $http_host | 请求头中的 Host 值。 |
| $http_user_agent | 请求头中的 User-Agent 值。 |
| $http_referer | 请求头中的 Referer 值。 |
| $http_content_type | 请求头中的 Content-Type 值。 |
| $http_x_forward_for | 请求头中的 X-Forwarded-For 值。 |
| $remote_addr | 请求的 Client IP 信息。 |
| $scheme | 请求的协议类型。 |
| $server_protocol | 请求的协议版本。 |
| $uri | 请求的原始 URI。 |
| $args | 请求的 Query String，不包含问号（?）。 |
| $request_method | 请求方法。 |
| $request_uri | uri+'?'+args 的内容。 |
## 常见问题
[阿里云](access-control-faq.md)[CDN URL](access-control-faq.md)[鉴权和远程鉴权可以同时开启吗？](access-control-faq.md)
[远程鉴权中鉴权服务器支持配置为内网地址吗？](access-control-faq.md)
[鉴权服务器返回的状态码既不是成功状态码，也不是失败状态码，CDN](access-control-faq.md)[为什么会直接放行？](access-control-faq.md)
[远程鉴权服务器发生故障或宕机时，CDN](access-control-faq.md)[会直接放行所有请求吗？](access-control-faq.md)
## 相关API
[BatchSetCdnDomainConfig](../api-batchsetcdndomainconfig.md)
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
