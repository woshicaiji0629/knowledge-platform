# 修改出站请求头-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-custom-request-headers

# 修改出站请求头
阿里云CDN默认支持携带一些例如客户端IP地址的请求头，也支持自定义配置。如果您需要改写用户回源请求中的HTTP Header，可以通过修改出站请求头实现，支持增加、删除、变更或替换回源HTTP请求头，满足更多实际业务需求。
## 背景信息
HTTP请求头是HTTP的请求消息头的组成部分之一，可携带特定的请求参数信息并传递给服务器。
当CDN节点请求回源站拉取资源时，源站可获取到回源请求头中携带的信息。您可以通过该功能，改写用户回源请求中的HTTP Header信息，携带特定的参数信息给源站，实现特定业务需求。例如，通过X-Forwarded-For头部携带真实客户端IP至源站。
源站服务器通过用户回源请求中携带的X-Forwarded-For头部获取客户端真实IP的方式，请参见[获取客户端真实](../../../waf/documents/web-application-firewall-2-0/user-guide/retrieve-the-originating-ip-addresses-of-clients.md)[IP](../../../waf/documents/web-application-firewall-2-0/user-guide/retrieve-the-originating-ip-addresses-of-clients.md)。
## 注意事项
出站请求指用户请求中通过CDN回源的HTTP消息。修改出站请求头配置只会影响通过CDN回源的HTTP消息，对于CDN节点直接响应给用户的HTTP消息不做修改。
不支持对泛域名修改出站请求头。
功能配置在引用规则引擎上的规则条件配置时，配置的执行顺序不是按照配置的优先级顺序执行，而是会按照配置关联的规则条件的优先级顺序来执行。
阿里云CDN默认支持携带以下HTTP请求头回源，您无需额外配置。
| 回源 HTTP Header | 说明 | 示例 |
| --- | --- | --- |
| Ali-Cdn-Real-Ip | 客户端与 CDN 节点建连时使用的真实 IP。 | Ali-Cdn-Real-Ip:192.168.0.1 |
| X-Forwarded-For | 客户端请求经过 CDN 节点回源的整个链路上，包括客户端和 CDN 节点的 IP 信息。 | X-Forwarded-For:192.168.0.1, 172.16.0.1 |
| X-Client-Scheme | 客户端发送到 CDN 节点的应用层请求使用的协议，例如：HTTP、HTTPS。 | X-Client-Scheme:http |
| Host | 客户端请求在回源时实际访问的源站 Web 站点域名。 | Host:example.com |
| Via | 客户端请求经过的所有 CDN 节点的名称。 | Via:cn2546-10.l1, cache1.cn2546-10, l2cn2547-7.l2, cache1.l2cn2547-7 |
修改出站请求头的值如果配置的是某个变量，那么实际使用的时候会被设置为具体的变量值，以下为可以使用的变量。
| 名称 | 回源 HTTP Header | 说明 | 示例 |
| --- | --- | --- | --- |
| Ali-Cdn-Real-Port | $http_Ali_Cdn_Real_Port | 在回源头里面添加客户端真实端口信息，向源站传递客户端端口信息。 | Ali-Cdn-Real-Port:80 |
| Ali_Cdn_Real_Ip | $http_Ali_Cdn_Real_Ip | 在回源头里面添加客户端真实 IP 信息，向源站传递客户端 IP 地址信息。 | Ali-Cdn-Real-Ip:192.168.0.1 |
| x_forwarded_for | $proxy_add_x_forwarded_for | 在回源头里面添加 X-Forwarded-For 信息，向源站传递客户端 IP 和中间的代理服务器 IP。 | X-Forwarded-For:192.168.0.1, 172.16.0.1 |
## 常见问题
### 安全扫描发现缺失 Required HTTP Header Fields，如何在 CDN 侧直接配置修复该漏洞？
CDN 作为中间代理，无法直接在响应中插入缺失的 HTTP 响应头（如 Cache-Control 等）来修复安全扫描漏洞，只能配置修改回源请求头。
建议通过 CDN 控制台配置自定义回源请求头，将所需参数透传至源站（如 CLB），由源站接收并处理。若源站不支持或无法修改，CDN 侧无其他直接添加响应头的方式。
说明
如果您需要在 CDN 返回给客户端的响应中添加 HTTP 响应头，请参见[修改出站响应头](create-a-custom-http-response-header.md)。
### CDN 添加自定义 HTTP 头字段是否会影响访问速度？
在 CDN 侧添加自定义 HTTP 头字段（即配置回源请求头）不会影响访问速度。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击回源配置。
单击修改出站请求头页签。
单击添加。
修改出站请求头信息。
重要
当不同的操作方式同时作用于同一个回源请求头参数时，会存在操作冲突。此时按照操作类型的优先级来执行，优先级顺序为替换＞增加＞变更和删除。例如，当增加和删除操作同时作用于同一个参数时，会先增加再删除。
### 增加请求头参数
| 配置项 | 示例 | 说明 |
| --- | --- | --- |
| 请求头操作 | 增加 | 在回源 HTTP 请求中增加指定的请求头参数。 |
| 自定义请求头参数 | 自定义回源请求头 | 选择 自定义回源请求头 或选择已经预设好的请求头参数。 |
| 自定义请求头名称 | x-code | 自定义请求头名称为 x-code。 |
| 请求头值 | key1, key2 | 一个请求头参数中可以配置多个值，多个值用英文逗号（,）分隔。 |
| 是否允许重复 | 允许 | 允许 ：可以添加重复的请求头参数。例如 x-code:key1 ， x-code:key2 。 不允许 ：添加同一个请求头参数，新值将覆盖旧值。例如先添加 x-code:key1 ，再添加 x-code:key2 ，最终的值为 x-code:key2 。 |
| 规则条件 | 不使用 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 重要 引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](rules-engine.md) 中进行管理。 |
### 删除请求头参数
| 配置项 | 示例 | 说明 |
| --- | --- | --- |
| 请求头操作 | 删除 | 删除所有与请求头参数名称匹配的参数值，无论是否有重复的请求头参数。 |
| 自定义请求头参数 | 自定义回源请求头 | 选择 自定义回源请求头 或选择已经预设好的请求头参数。 |
| 自定义请求头名称 | x-code | 自定义请求头名称为 x-code。 |
| 规则条件 | 不使用 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](rules-engine.md) 中进行管理。 |
### 变更请求头参数
| 配置项 | 示例 | 说明 |
| --- | --- | --- |
| 请求头操作 | 变更 | 当请求头参数不存在重复时，可以正常变更参数，如果有多个重复的请求头参数，则不允许变更。 |
| 自定义请求头参数 | 自定义回源请求头 | 选择 自定义回源请求头 或选择已经预设好的请求头参数。 |
| 自定义请求头名称 | x-code | 自定义请求头名称为 x-code。 |
| 请求头变更为 | key1, key3 | 一个请求头参数中可以配置多个值，多个值用英文逗号（,）分隔。 |
| 规则条件 | 不使用 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](rules-engine.md) 中进行管理。 |
### 替换请求头参数
| 配置项 | 示例 | 说明 |
| --- | --- | --- |
| 请求头操作 | 替换 | 当请求头参数不存在重复时，可以正常替换参数，如果有多个重复的请求头参数，则不允许替换。 |
| 自定义请求头参数 | 自定义回源请求头 | 选择 自定义回源请求头 或选择已经预设好的请求头参数。 |
| 自定义请求头名称 | x-code | 自定义请求头名称为 x-code。 |
| 查找 | key | 正则表达式查找需要替换的参数值。 |
| 替换为 | abc | 正则表达式替换需要替换的参数值。 |
| 匹配 | 匹配所有 | 匹配所有 ：所有匹配上的值都会被替换。例如 x-code:key1,key2,key3 ，正则匹配值 key 替换为 abc，替换后的结果为 x-code:abc1,abc2,abc3 。 仅匹配第一个 ：只有第一个匹配上的值会被替换。例如 x-code:key1,key2,key3 ，正则匹配值 key 替换为 abc，替换后的结果为 x-code:abc1,key2,key3 。 |
| 规则条件 | 不使用 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](rules-engine.md) 中进行管理。 |
单击确定。
## 相关API
[批量配置域名](../developer-reference/api-cdn-2018-05-10-batchsetcdndomainconfig.md)
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
