# 配置回源HOST以访问源站虚拟站点-CDN-阿里云-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-the-default-origin-host

# 配置默认回源HOST
在发起回源请求时携带的 Host 请求头默认为加速域名，可通过本功能自定义回源 Host 请求头。
## 背景介绍
当存在多个加速域名、每个域名负责加速不同静态资源时，常见的做法是搭建多个源站，以支持不同加速域名的回源请求。若加速域名数量较多而回源流量较少，重复建站会造成资源浪费，可通过虚拟站点技术解决该问题。
### 虚拟站点技术
虚拟站点技术是一种在单个 Web 服务器上提供多个网站服务的技术。服务器使用不同的域名或主机名区分和隔离不同的网站。当用户请求访问某个特定的域名或主机名时，服务器会根据请求中的域名或主机名，将请求定向到相应的虚拟站点，从而提供对应的网站内容。
Nginx 相关实现
Nginx 支持通过server区块配置多个虚拟站点，示例如下：
server { listen 80; server_name example.org www.example.org; ... } server { listen 80; server_name example.net www.example.net; ... } server { listen 80; server_name example.com www.example.com; ... }
上述配置了 3 个虚拟站点，分别为example.org、example.net、example.com。Nginx 使用server_name匹配 HTTP 请求头中的Host字段选择虚拟站点；如果未匹配到任何一个虚拟站点，Nginx 会使用默认的虚拟站点提供服务（若未配置，默认为第一个server配置的默认站点）。
### 默认回源HOST
访问 URL 链接时，如果不指定Host字段，该请求的Host字段默认为访问 URL 链接的主机加端口部分。默认将Host字段设置为加速域名，也可根据源站的虚拟站点配置自定义Host字段的默认值。
源站服务器需支持通过Host请求头匹配不同的虚拟站点，否则该功能配置无法达到预期效果。
重要
当源站使用 HTTPS 协议时，除了配置默认回源HOST，通常还需配置默认回源SNI。若回源HOST与回源SNI配置不一致（例如 HOST 为源站域名、SNI 为加速域名），可能导致 SSL 握手失败或源站返回错误。建议将回源HOST和回源SNI设置为相同的域名（通常为源站域名或加速域名，需与源站证书及虚拟主机配置匹配）。控制台的回源配置页面，"默认回源HOST"和"默认回源SNI"是两个独立的配置项，需分别单击修改配置进行设置。
## 操作步骤
登录[阿里云](https://www.aliyun.com/product/cdn)[CDN](https://www.aliyun.com/product/cdn)[平台](https://www.aliyun.com/product/cdn)。
在左侧导航栏单击域名管理。
在域名列表中选择目标域名。
单击回源配置Tab。
回源HOST区域，单击修改配置。
打开回源HOST开关，选择域名类型。
| 域名类型 | 说明 |
| --- | --- |
| 加速域名 | 以终端用户访问的加速域名作为回源 HOST。 |
| 源站域名 | 以源站服务器的域名作为回源 HOST。源站信息为 IP 地址类型时，选项置灰，不可选择。源站信息为 OSS 域名时，将会同步开启默认回源 HOST 功能，并且设置域名类型为源站域名。 |
| 自定义域名 | 以用户指定的域名作为回源 HOST。自定义域名需确保为已绑定的域名，否则回源失败。适用于源站绑定了多个域名，且希望用户从指定域名获取资源的场景。 |
重要
当源站使用 HTTPS 协议时，除了配置回源HOST外，还需要在同一回源配置页面配置默认回源SNI。建议将回源HOST和默认回源SNI设置为相同的域名（通常为源站域名），以避免因两者不一致导致 SSL 握手失败或源站拒绝服务。例如，如果回源HOST设置为源站域名，而默认回源SNI设置为加速域名，可能导致源站证书校验失败。在控制台中，回源HOST和默认回源SNI是同一回源配置页面上的两个独立配置项，分别通过修改配置按钮进行配置。
单击确定。
## 配置示例
### 示例一：源站类型为域名
| 域名 | 说明 |
| --- | --- |
| 加速域名： image.example.com 源站地址： source.example.com | 功能默认关闭，可主动开启默认回源 HOST 功能。 回源域名类型说明： • 加速域名 ：当回源时，会到 source.example.com 源站上的 image.example.com 虚拟站点获取资源。 • 源站域名 ：当回源时，会到源站 source.example.com 获取资源。 • 自定义域名 ：回源 HOST 为用户输入的自定义域名。 |
### 示例二：源站类型为IP地址
| 域名 | 说明 |
| --- | --- |
| 加速域名： example.com 源站地址： 10.10.10.10 | 功能默认关闭，可主动开启默认回源 HOST 功能。 回源域名类型说明： • 加速域名 ：当回源时，会到 10.10.10.10 这台主机上的 example.com 虚拟站点获取资源。 • 源站域名 ：源站信息为 IP 地址类型时，选项置灰，不可选择。 • 自定义域名 ：当回源时，会到 10.10.10.10 这台主机上自定义域名的虚拟主机获取资源。 |
### 示例三：源站类型为OSS域名
当源站信息为 OSS 域名时，将会同步开启默认回源HOST功能，并且设置域名类型为源站域名。
| 域名 | 说明 |
| --- | --- |
| 加速域名： example.com 源站地址： example.oss-cn-hangzhou.aliyuncs.com | 回源域名类型说明： • 加速域名 ：当回源时，会到 example.oss-cn-hangzhou.aliyuncs.com OSS 域名上的 example.com 站点获取资源。 • 源站域名 ：当回源时，会到 OSS 域名 example.oss-cn-hangzhou.aliyuncs.com 获取资源。 • 自定义域名 ：当回源时，会到 example.oss-cn-hangzhou.aliyuncs.com 站点上自定义域名的虚拟站点获取资源。 |
## 常见问题
### 配置默认回源HOST后，访问加速域名返回 404、500、502 或 403 错误怎么办？
请按以下步骤排查：
检查回源HOST配置是否与源站虚拟主机配置匹配。如果源站通过Host请求头区分虚拟站点（如 Nginx 的server_name），请确保 CDN 控制台中配置的回源HOST与源站期望的域名一致。操作路径：域名管理>域名列表> 选择目标域名 >回源配置> 在回源HOST区域单击修改配置，将域名类型设为源站域名或加速域名。
检查源站是否拦截了 CDN 节点 IP。如果回源HOST配置正确但仍有错误，请检查源站的安全策略是否拦截了 CDN 节点 IP，或源站防火墙、安全组是否拒绝了来自 CDN 的请求。
检查 IIS 源站主机头（Host Header）配置。若源站为 IIS 服务器且设置了特定主机头，CDN 回源请求中的 Host 字段必须与该主机头一致，否则可能返回 403 或 404 错误。若 IIS 未设置特定主机头（允许 IP 直接访问），则无需特殊配置，但建议配置正确的主机头以匹配 CDN 回源HOST。
刷新 CDN 缓存。如果源站之前返回的错误响应（如 404）被 CDN 边缘节点缓存，修改回源HOST配置后需要刷新 CDN 缓存以清除缓存的错误响应。
### 配置回源HOST和 SNI 后出现 ERR_TOO_MANY_REDIRECTS（重定向过多）或 502 错误怎么办？
出现 ERR_TOO_MANY_REDIRECTS 通常是 CDN 与源站同时开启了 HTTPS 强制跳转导致循环重定向；出现 502 错误通常是回源协议或端口配置不当（如源站监听非标准端口）。请按以下步骤排查：
关闭源站上的 HTTPS 强制跳转功能。登录源站管理面板（如宝塔面板），找到 HTTPS 设置，关闭"强制HTTPS"或"HTTP到HTTPS跳转"选项。
确认回源HOST和回源 SNI 配置一致且正确。在 CDN 控制台的回源配置页面，确保回源HOST和默认回源SNI设置为正确的域名（通常为源站域名），且两者值保持一致，使回源请求符合源站的预期。
检查并调整 CDN 回源协议和端口。确保 CDN 的回源协议（HTTP 或 HTTPS）和回源端口与源站实际监听配置匹配。如果源站仅监听特定端口（如 HTTP 的 8080 端口），需要在 CDN 源站配置中设置对应的回源端口。
刷新 CDN 缓存。调整配置后，刷新 CDN 缓存以清除已缓存的重定向或错误响应。
### 访问返回 403 Forbidden 错误怎么办？
当源站使用 Cloudflare、WAF 等安全服务时，403 Forbidden 错误常因回源HOST与源站期望的 Host 头不一致，导致源站安全策略拦截请求。请按以下步骤排查：
将默认回源HOST设置为源站实际绑定的域名。在 CDN 控制台将回源HOST设置为源站实际绑定的域名（而非加速域名），确保与源站证书及虚拟主机配置匹配。
确认 WAF 配置中的域名一致性。若源站为 WAF，需确保 CDN 回源请求中的 Host 头与 WAF 配置的防护域名一致，否则 WAF 会因域名不匹配而拦截请求。
检查源站访问日志。登录源站或安全服务管理面板，查看访问日志，确认是否有来自 CDN 节点 IP 的请求被拦截，并查看拦截原因。
刷新 CDN 缓存。修改配置后，刷新 CDN 缓存以清除已缓存的 403 错误响应。
### CDN 加速后页面跳转失败或部分资源无法访问怎么办？
可能原因是源站依赖 URL 参数或特定的 Host 头进行逻辑判断，而 CDN 默认行为可能导致参数丢失或 Host 头不匹配。请按以下步骤排查：
检查缓存规则中的 URL 参数配置。在 CDN 控制台的缓存配置中，检查是否启用了"忽略 URL 参数"功能。若源站依赖 URL 参数进行跳转或逻辑判断，启用此功能可能导致参数丢失。建议取消"忽略 URL 参数"或选择"保留指定参数"以保留源站所需的参数。
将回源HOST配置为源站期望的域名。将回源HOST配置为加速域名或源站期望的域名，确保源站能正确识别请求主机头从而处理跳转逻辑。
执行目录或 URL 刷新。修改配置后，在 CDN 控制台的刷新预热页面执行目录刷新或 URL 刷新以使新配置生效。
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
