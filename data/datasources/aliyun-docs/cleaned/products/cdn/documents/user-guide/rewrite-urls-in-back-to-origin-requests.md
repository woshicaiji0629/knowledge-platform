# 重写回源URI工作原理、注意事项及配置示例-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/rewrite-urls-in-back-to-origin-requests

# 重写回源路径
阿里云CDN支持URL重写，重写不影响CDN内部链路和缓存key，仅在回源请求时使用重写后的URL。
## 工作原理
通过重写回源URL规则，使请求URL与源站URL匹配，准确获取源站的资源，或者传递指定的参数给源站。
执行规则设置为“空”或者“break”的情况下，仅重写URL中的资源路径部分。
执行规则设置为“enhance_break”的情况下，能够同时重写资源路径和请求参数。
## 注意事项
单个域名可以配置的重写回源路径规则数量上限是50个。
规则重写按照规则列表从上到下顺序依次执行，因此顺序可能会影响您的重写结果。
配置重写回源路径规则时，可能与域名管理>性能优化页签下的[忽略参数](ignore-parameters.md)功能冲突，配置时要需注意避免冲突。
如果同时配置了重写回源路径和条件回源规则，重写回源路径规则可能改写回源URL路径，导致源站收到的请求路径与预期不一致，返回404错误。排查方法：先临时关闭重写回源路径规则，验证请求是否恢复正常；如需同时使用两个功能，调整规则的优先级和匹配条件，确保回源路径不被意外改写。
## 重写访问URL和重写回源路径的区别
| 功能 | 作用对象 | 客户端体验 | 应用场景 |
| --- | --- | --- | --- |
| [重写访问](create-an-access-url-rewrite-rule.md) [URL](create-an-access-url-rewrite-rule.md) | 影响的是客户端访问的 URL，同时也会改变 CDN 节点回源的 URL。 | 执行规则为 redirect 的情况下，客户端将会使用重定向以后的 URL 重新发起访问请求。 执行规则为 break 的情况下，客户端看到的 URL 与实际访问的 URL 一致，没有变化。 | 常用于将旧域名的 URL 迁移、映射到新域名；或者为移动端和 PC 端提供不同的 URL。 示例 ：访问 old.example.com/hello 时，重写访问 URL 为 new.example.com/hello 。 |
| [重写回源路径](rewrite-urls-in-back-to-origin-requests.md) | 影响的是 CDN 节点回源时访问的 URL，而客户端访问的 URL 不变。 | 客户端看到的 URL 与实际访问的 URL 一致，没有变化。 | 常用于隐藏源站的真实 URL 结构，保护源站信息；或者通过 URL 映射，让 CDN 节点回源到不同的源站目录。 示例 ：访问 cdn.example.com/hello 时重写回源 URL 为 origin.example.com/source/hello 。 |
### 重写访问URL示意图
客户端向CDN发起请求，请求的URL为old.example.com/hello。
CDN接收到请求后，根据重写访问URL规则，CDN节点会在给客户端发送的302状态码响应信息的HTTP Location头部中放置新的URL地址信息，将请求的URL重写为new.example.com/hello。
客户端收到302状态码响应之后，将会向新的URL地址发起请求。
CDN节点检查缓存，如果缓存中有重写后URL的内容，直接返回给客户端；如果没有，则CDN节点向源站发起请求，请求的URL为重写后的new.example.com/hello。
源站接收到请求，返回响应内容给CDN节点。
CDN节点将响应内容缓存，并返回给客户端。
### 重写回源路径示意图
客户端向CDN发起请求，请求的URL为cdn.example.com/files/hello.txt。
CDN接收到请求后，检查缓存，如果缓存中有请求URL的内容，直接返回给客户端；如果没有，则CDN节点根据重写回源URL规则，将回源URL重写为origin.example.com/secret/files/hello.txt，向源站发起请求。
源站接收到请求后，向CDN节点返回响应内容。
CDN节点将响应内容缓存，并返回给客户端。
## 配置回源路径
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击回源配置。
单击重写回源路径页签。
单击添加。根据您的需求，配置待重写的Path、目标Path和执行规则。
| 参数 | 示例 | 说明 |
| --- | --- | --- |
| 待重写的 Path | ^/hello$ | 以正斜线（/）开头的 URL，不含 http://头及域名。必须使用 PCRE 正则表达式。 |
| 目标 Path | /hello/test | 以正斜线（/）开头的 URL，不含 http://头及域名。支持使用 PCRE 正则表达式。 |
| 执行规则 | 空 | 如果配置了多条规则，在匹配执行当前规则后，将按照从上到下的顺序依次执行所有可以匹配的规则。 |
| break | 如果配置了多条规则，若请求的 URL 匹配了当前规则，匹配执行完当前规则后，剩余规则将不再匹配。 只修改 URL 中的资源路径部分，不修改 URL 的参数，因此不会影响 重写回源路径 功能对 URL 中参数的重写。 |  |
| enhance break | 如果配置了多条规则，若请求的 URL 匹配了当前规则，匹配执行完当前规则后，剩余规则将不再匹配。 与 break 相似，但是增加了对 URL 中参数部分的重写能力，对 URL 中参数的重写可能会与 [回源参数重写](rewrite-url-parameters-in-back-to-origin-requests.md) 功能产生冲突，因此在同时配置这两个功能时，需要注意避免配置冲突。 |  |
单击确定，使重写规则开始执行和生效。
您也可以在重写回源路径页面的规则列表中，单击修改或删除，对当前配置的规则进行相应操作。
## 配置示例
### 示例一：执行空规则。
| 待重写的 Path | ^/hello$ |
| --- | --- |
| 目标 Path | /index.html |
| 执行规则 | 空 |
| 结果说明 | 原始请求： http://example.com/hello 重写后的回源请求： http://example.com/index.html 该请求将会继续匹配 重写回源路径 规则列表中其余的规则。 |
### 示例二：执行break规则。
| 待重写的 Path | ^/hello.jpg$ |
| --- | --- |
| 目标 Path | /image/hello.jpg |
| 执行规则 | break |
| 结果说明 | 原始请求： http://example.com/hello.jpg 重写后的回源请求： http://example.com/image/hello.jpg 该请求将不再继续匹配 重写回源路径 规则列表中其余的规则。 |
### 示例三：执行enhance break规则。
| 待重写的 Path | ^/hello.jpg?code=123$ |
| --- | --- |
| 目标 Path | /image/hello.jpg?code=321 |
| 执行规则 | enhance break |
| 结果说明 | 原始请求： http://example.com/hello.jpg?code=123 重写后的回源请求： http://example.com/image/hello.jpg?code=321 该请求将不再继续匹配 重写回源路径 规则列表中其余的规则。 |
### 示例四：在文件名是变量的情况下对根目录添加URL前缀。
例如：将包含/xxx的URL（xxx代表任意文件名称，例如：/hello.jpg、/hello.html等等）重写为/image/xxx，即对根目录下的任意文件的URL都插入路径/image。
| 待重写的 Path | ^(.*)$ 说明 ^ 表示匹配字符串的开始位置； (.*) 是一个分组，其中 . 表示匹配任意单个字符（除了换行符）， * 表示匹配前面的字符或分组零次或多次，可以在目标 Path 中通过$1 来调用分组的变量内容； $ 表示匹配字符串的结束位置。所以， ^(.*)$ 的意思是：匹配整个字符串，从开始到结束，中间可以包含任意字符（除了换行符），并将匹配到的内容捕获到一个分组中。例如，对于字符串 "hello world" 来说， ^(.*)$ 会匹配整个字符串，并将 "hello world" 捕获到第一个分组中。 |
| --- | --- |
| 目标 Path | /image$1 说明 /image 表示匹配字符串 "/image" ； $1 表示引用第一个捕获分组的内容， $2 表示引用第二个捕获分组的内容，依此类推。所以， /image$1 的意思是：匹配字符串 "/image" 后面紧跟着第一个捕获分组的内容。例如，如果第一个捕获分组的内容是 "abc" ，那么 /image$1 将匹配字符串 "/imageabc" 。需要注意的是， $1 引用的是捕获分组的内容，而不是字面量 "$1" 。如果想要匹配字面量 "$1" ，需要使用转义字符 "\$1" 。 |
| 执行规则 | break |
| 结果说明 | 原始请求： http://example.com/hello.jpg 重写后的回源请求： http://example.com/image/hello.jpg 原始请求： http://example.com/hello.html 重写后的回源请求： http://example.com/image/hello.html 该请求将不再继续匹配 回源 URL 重写 规则列表中其余的规则。 |
### 示例五：在文件名是变量的情况下对指定目录添加URL前缀。
例如：将包含/live/xxx的URL（xxx代表任意文件名称，例如：/live/hello.jpg、/live/hello.html 等等）重写为/image/live/xxx，即对目录/live下的任意文件的URL都插入路径/image。
| 待重写的 Path | ^/live/(.*)$ |
| --- | --- |
| 目标 Path | /image/live/$1 |
| 执行规则 | break |
| 结果说明 | 原始请求： http://example.com/live/hello.jpg 重写后的回源请求： http://example.com/image/live/hello.jpg 原始请求： http://example.com/live/hello.html 重写后的回源请求： http://example.com/image/live/hello.html 该请求将不再继续匹配 回源 URL 重写 规则列表中其余的规则。 |
### 示例六：匹配多条规则时，执行空规则。
在回源URL重写配置中添加两条规则：第一条将待重写Path^/image_01.png$重写为目标Path/image_02.png，执行规则为空；第二条将待重写Path^(.*)$重写为目标Path/image$1，执行规则为空。两条规则状态均为已生效。
结果说明：
原始请求：http://example.com/image_01.png
重写后的回源请求：http://example.com/image/image_02.png
说明
先匹配第一条规则，重写为http://example.com/image_02.png，继续匹配第二条规则，最终重写为http://example.com/image/image_02.png。
### 示例七：匹配多条规则时，执行break规则。
在回源URL重写配置中添加两条重写规则：第一条待重写Path为^/image_01.png$，目标Path为/image_02.png，执行规则为break，状态为已生效；第二条待重写Path为^(.*)$，目标Path为/image$1，执行规则为空，状态为已生效。当请求URI匹配到第一条规则且执行规则为break时，将不再继续匹配后续规则。
结果说明：
原始请求：http://example.com/image_01.png
重写后的回源请求：http://example.com/image_02.png
说明
先匹配第一条规则，重写为http://example.com/image_02.png，由于第一条规则设置为break，所以不再匹配后续规则。
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
