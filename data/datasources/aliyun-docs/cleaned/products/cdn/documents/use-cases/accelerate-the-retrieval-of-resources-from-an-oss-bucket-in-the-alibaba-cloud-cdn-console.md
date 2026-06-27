# 本文档详细说明了如何通过阿里云CDN加速OSS静态资源访问，包括技术架构、配置流程及优化建议，帮助用户提升访问速度并降低源站负载。-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console

# CDN 加速 OSS 资源
将 OSS 作为 CDN 源站，利用全球边缘节点缓存静态内容，实现用户就近访问。该方案通过 CDN 分发 OSS 中存储的图片、视频、脚本等静态资源，显著提升访问速度并降低源站负载。
使用 OSS 默认域名的用户请注意：若当前使用 OSS 默认域名（如{bucket}.oss-cn-hangzhou.aliyuncs.com）访问资源，无法在不改变 URL 链接的情况下直接转变为 CDN 加速链接。必须使用自定义域名进行 CDN 加速，并使用该自定义域名进行访问，这意味着业务侧需要修改原有的 URL 链接。
## 业务场景
阿里云 OSS 提供低成本的对象存储，CDN 实现静态资源加速分发。使用 OSS 作为 CDN 的源站，具备以下优势：
用户访问资源全部经过 CDN，降低源站压力。
CDN 下行流量单价低于直接访问 OSS 产生的外网流出流量。
从距离客户端最近的 CDN 节点获取资源，减少网络传输距离，降低访问延迟。
少量视频场景：OSS 提供低成本存储，CDN 就近分发降低延迟，方案简单经济。如需转码、加密、播放器集成等高级功能，则适合使用音视频点播服务。
静态图片场景：CDN 下行流量单价低于OSS 外网流出流量单价。若用户均为中国内地访问，CDN+OSS 与直连 OSS 的速度差距不大，但 CDN 通过边缘节点缓存使物理距离更近，体验略优。OSS 传输加速域名更适合跨地域场景，或作为 CDN 回源地址优化跨境访问。
## 技术架构
该方案的核心架构是利用 CDN 作为 OSS 的缓存层。用户请求资源时，请求首先到达距离最近的 CDN 边缘节点：
缓存命中：节点已缓存该资源，直接从缓存返回给用户，实现最快响应。
缓存未命中：节点向源站（OSS Bucket）发起请求获取资源，返回给用户的同时在节点创建缓存副本，以备后续请求使用。
## 实施步骤
### 步骤一：注册域名和 ICP 备案
选择域名。
新注册域名：[域名注册](https://help.aliyun.com/zh/dws/user-guide/how-to-register-a-domain-name)
完成实名认证：域名注册时需根据指引提交所有权人（个人或企业）的身份证明材料以完成实名认证。
域名信息模板的审核过程通常需要 1～3 个工作日。
域名实名认证资料的审核通常需要 1 个工作日。
关于认证流程的详细说明，请参考[实名认证](https://account.console.aliyun.com/#/auth/home)。
完成 ICP 备案：根据工信部规定，托管在中国内地提供服务的网站都必须先完成[ICP](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)[备案流程](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)。
提交备案申请：阿里云提供自助备案（免费）、备案管家服务（付费）和备案智能助理（付费）等备案服务。
备案流程与耗时：阿里云初审需要 1～2 个工作日；初审通过后，申请人需在 24 小时内完成工信部短信核验；各地区通信管理局的最终审核需要 1～20 个工作日。在等待管局审核期间，可并行进行网站内容部署。
为保护品牌资产，可在注册域名的同时，通过[申请商标专用权](https://help.aliyun.com/zh/trademark/user-guide/trademark-registration-application/)获得法律保护。
### 步骤二：添加加速域名并关联 OSS 源站
此步骤在 CDN 控制台注册加速域名，并将其与作为源站的 OSS Bucket 关联。
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
点击添加域名，配置加速域名的基本信息：
加速域名：输入自定义域名（如www.example.com），支持泛域名（如*.example.com）。此处填写的不是 OSS 默认域名，而是希望用于 CDN 加速的对外服务域名。
加速区域：根据主要用户群体所在的地理位置选择。
业务类型：根据资源类型选择，例如，对于小于 20MB 的图片和网页小文件，选择“图片小文件”。
首次添加某域名时，需验证域名归属权，提供文件验证或 DNS 验证两种方式。
选择中国内地或全球时，加速域名必须已完成 ICP 备案，否则将触发备案校验拦截。
若提示 DNS 验证失败，请检查：域名是否已完成 ICP 备案（针对中国内地加速场景）；DNS 解析是否存在冲突。
点击新增源站信息，填写 OSS 的信息：
源站信息：选择OSS 域名作为源站类型。
域名：源站类型为 OSS 域名时，可从下拉列表中选择当前账号下已有的 OSS Bucket 外网域名。
配置多源站时，可设置以下参数：
| 参数 | 说明 |
| --- | --- |
| 优先级 | 主（20）或备（30）。 |
| 权重 | 允许范围为 1～100。。单源站场景保持默认值即可。 |
| 端口 | HTTP 默认 80，HTTPS 默认 443，支持自定义 1～65535。源站类型为函数计算时自动设为 80。 |
单击确定。域名添加后会进入推荐配置页签。
### 步骤三：配置核心加速策略（推荐配置）
按照推荐配置的引导流程来添加缓存过期时间、Range 回源、忽略参数等基础配置，这些配置可以提升 CDN 的缓存命中率、访问性能以及安全性。
配置缓存过期时间
合理的缓存规则能最大化 CDN 性能，减少不必要的回源请求。缓存规则按顺序匹配，首个命中的规则生效。进入 CDN 控制台指定域名的管理配置页面，选择缓存配置功能。以下为参考的推荐配置：
| 文件类型 | 文件后缀名 | 过期时间 | 说明 |
| --- | --- | --- | --- |
| 图片/音视频 | jpg,png,gif,mp3,mp4 | 30 天 | 资源内容不经常变更 |
| 静态脚本 | js,css | 1 小时 | 可能随版本发布而频繁变更 |
| 网站首页 | html | 不缓存（0 秒） | 确保用户始终获取最新页面结构 |
混合大视频与 MP3 小文件时，建议按文件类型分别配置缓存策略：MP4 等大视频文件设置较长缓存时间（如 30 天），同时建议开启 Range 回源以支持大文件分片回源、提升首播速度；MP3 等小文件同样设置较长缓存时间，由于文件较小，无需额外开启 Range 回源。可分别为.mp4和.mp3后缀添加对应缓存规则。
配置忽略参数
进入 CDN 控制台指定域名的管理配置页面，选择性能优化中的忽略参数功能。开启[忽略参数](../user-guide/ignore-parameters.md)功能后，CDN 节点生成缓存 hashkey 时会去除 URL 中?之后的参数，使客户端携带不同参数访问同一资源时都能命中同一个缓存文件，有助于提高缓存命中率、减少回源流量。
开启 Range 回源
开启 Range 回源功能后，CDN 节点请求源站 OSS 上的大文件时，OSS 按照 CDN 请求的 Range 范围返回分片内容，可减少回源流量消耗、减少资源响应时间。该功能适用于音视频等较大文件的内容分发，不适用于图片小文件等业务，图片业务加速时无需配置。
配置 OSS 文件自动刷新缓存
为确保 OSS 中的内容更新能及时同步到 CDN，可以在 OSS 控制台的Bucket 配置>域名管理页面开启目标域名的OSS 目标域名绑定和CDN 缓存自动刷新，选择需要自动刷新的操作。当 OSS 内容发生更新时，OSS 会自动触发 CDN 刷新任务。
此功能为事件触发，不保证 100% 的送达率和实时性。在 OSS 侧高并发写入或网络抖动等极端情况下，刷新事件可能丢失。对时效性要求极高的场景，建议直接使用 CDN的[刷新和预热](../user-guide/refresh-and-prefetch-resources.md)。
### 步骤四：配置 DNS 解析并验证生效
前往CDN 控制台的域名管理列表，找到之前添加的域名，复制域名对应的 CNAME 值（如果此处值为空，请稍等五秒之后刷新重试）。
使用加速域名所在的阿里云账号，登录[云解析 DNS 控制台](https://dnsnext.console.aliyun.com/overview?spm=5176.11785003.console-base_search-panel.dtab-product_dns.e7e4142fCBguns)，在公网权威解析页面找到目标域名并点击解析设置。
单击添加记录，创建一条 CNAME 记录：
记录类型：选择CNAME。
主机记录：填写子域名的前缀（例如www）。
记录值：粘贴从 CDN 控制台复制的 CNAME 值。
其他参数保持默认，然后单击 确认。
验证流量是否已切换至 CDN
配置 DNS 解析后，可通过以下方式确认流量已正确切换至 CDN：
使用curl -I检查响应头：在终端执行curl -I https://your-domain.com/file，观察响应头中的X-Cache字段。若返回X-Cache: HIT或X-Cache: MISS均表示请求经过 CDN；若未出现X-Cache字段，说明请求可能直接到达 OSS。
查看 CDN 控制台监控数据：登录 CDN 控制台，进入页面，检查该域名是否有流量数据。若配置生效后监控页面有数据，说明流量已通过 CDN。
检查 CNAME 状态：在 CDN 控制台，查看目标域名的 CNAME 状态是否为已配置。CNAME 状态有三种：已配置（绿色）、等待配置（黄色）、检测超时。
若域名同时解析到 OSS 和 CDN，请求可能绕过 CDN 直接访问 OSS，导致加速失效。请确保 DNS 解析中仅保留指向 CDN CNAME 的记录，删除任何直接指向 OSS 域名的 A 记录或 CNAME 记录。
### 步骤五：安全配置
启用 HTTPS 加密传输
如果应用在配置阿里云 CDN 之前已支持 HTTPS 访问，务必进行 HTTPS 证书的配置，否则域名将不再支持 HTTPS 访问。
说明
开启HTTPS将产生HTTPS请求数，静态HTTPS请求数每月前500万次免费，超过500万次后，开始计费。HTTPS请求数计费不能使用CDN流量包抵扣，请确保您的账户余额充足，或购买HTTPS请求包，避免欠费导致CDN停止服务。详情敬请参见[静态](../product-overview/billing-of-https-requests-for-static-content.md)[HTTPS](../product-overview/billing-of-https-requests-for-static-content.md)[请求数](../product-overview/billing-of-https-requests-for-static-content.md)。
HTTPS 请求数计费不能使用 CDN 流量包抵扣，请确保账户余额充足，或购买 HTTPS 请求包，避免欠费导致 CDN 停止服务。
前往阿里云 CDN 控制台的域名管理列表，找到之前添加的域名，点击，进入域名配置页面。
选择HTTPS配置页签中的HTTPS证书，点击修改配置。
在HTTPS设置界面，打开HTTPS安全加速开关，并选择证书：
| 证书类型 | 说明 |
| --- | --- |
| 云盾（SSL）证书中心 | 从阿里云 SSL 证书产品中选择已有证书。需在中搜索选择。 |
| 自定义上传（证书+私钥） | 手动上传 PEM 格式的证书内容和私钥。需设置证书名称、上传和。 |
|  | 阿里云 Digicert 免费 DV 证书，有效期一年，自动续签。不支持泛域名。需勾选授权同意复选框。 |
| CSR 证书 | 提交 CSR 证书签名请求后使用。 |
如果已在阿里云数字证书管理服务购买了证书，选择云盾（SSL）证书中心中选择已购买的证书。
如果无法选择已购买的证书，请检查已购买证书绑定的域名和加速域名是否相同。如果使用的是第三方服务商签发的证书，选择自定义上传（证书+私钥）后，上传证书（公钥），该证书将保存至阿里云数字证书管理服务。可前往我的证书查看。
授权 CDN 访问私有 Bucket
如果 OSS Bucket 为私有权限，则必须完成以下授权，否则所有回源请求都将因无权限而失败。
前往阿里云 CDN 控制台的域名管理列表，点击之前添加的域名，进入域名配置页面。
在回源配置中打开阿里云OSS私有Bucket回源，然后选择同账号回源。如果涉及到跨账号回源，请参考[OSS](../user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[私有](../user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[Bucket](../user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[回源](../user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)进行配置。
配置 URL 鉴权
URL 鉴权（也称时间戳防盗链）通过为访问 URL 添加签名和过期时间，防止资源被恶意盗用。
前往阿里云 CDN 控制台的域名管理列表，点击之前添加的域名，进入域名配置页面。
在访问控制页签中，选择URL鉴权，点击修改配置。
在配置页中，选择A方式，设置一个主KEY和一个备KEY（主、备KEY至少要填写一个），并妥善保管。这些密钥将用于在服务端验证带有签名的 URL，使用示例请参考[鉴权方式](../user-guide/type-a-signing.md)[A](../user-guide/type-a-signing.md)[说明](../user-guide/type-a-signing.md)。
根据业务需求设置鉴权 URL 的有效时间，例如 1800 秒。
配置用量封顶
为防止域名被攻击或盗刷产生突发高带宽导致高额账单，可通过用量封顶控制用户访问该域名的带宽、流量、HTTPS 请求数上限值，减少因突发流量导致的损失。
在往阿里云 CDN 控制台域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击流量限制。
在用量封顶页签中，参考[功能介绍](../user-guide/configure-usage-cap.md)，配置适合自身业务的用量封顶策略。
点击修改配置，可以根据自身业务选择合适的统计周期、阈值和解封时间。具体参数配置请参考[功能介绍](../user-guide/configure-usage-cap.md)。
单击确定，封顶规则即可创建成功并生效。
监控与告警
设置实时监控：对 CDN 产品下指定域名的带宽峰值设置监控，达到设定的带宽峰值后将会给管理员发送告警，便于及时发现潜在风险。
设置费用预警：在控制台上方选择费用与成本，通过以下功能控制账户消费额度：
可用额度预警：设置账户余额低于一定金额时向报警联系人的联系方式发送告警信息。
启用延停额度：可选择关闭该功能，这样在账号欠费时会立即关闭业务，以避免产生更多消费。
## 计费说明
将 OSS 作为 CDN 源站时，可能产生以下费用：
CDN 下行流量费用：用户通过 CDN 访问资源产生的下行流量。建议购买 CDN 流量包以降低成本，CDN 下行流量单价通常低于 OSS 外网流出流量单价。购买 CDN 资源包后无需额外配置，系统自动抵扣产生的 CDN 下行流量费用。
OSS 流出到 CDN 的流量费用：CDN 回源到 OSS 时产生的 OSS 流出流量。
静态 HTTPS 请求数费用：开启 HTTPS 安全加速后产生。
中国站每月前 500 万次免费。
HTTPS 请求数计费不能使用 CDN 流量包抵扣，需单独购买 HTTPS 请求数资源包或确保账户余额充足。
## 常见问题
[CDN](cdn-acceleration-oss-faq.md)[加速](cdn-acceleration-oss-faq.md)[OSS](cdn-acceleration-oss-faq.md)[常见问题](cdn-acceleration-oss-faq.md)
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
