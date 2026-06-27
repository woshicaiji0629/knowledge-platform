# 配置IP黑白名单来拦截或仅允许特定IP的访问-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-an-ip-blacklist-or-whitelist

# 配置IP黑/白名单
当业务面临恶意IP盗刷或特定攻击时，可通过配置IP黑白名单，在CDN边缘节点根据访问来源对请求进行过滤。此功能允许您仅放行可信IP（白名单）或精准拦截已知恶意IP（黑名单），从而保护源站资源，降低安全风险。
## 使用场景
| 配置项 | 使用场景 |
| --- | --- |
| IP 白名单 | 保护内部敏感数据： 仅允许指定的 IP 访问敏感数据或资源，确保数据安全。 第三方服务对接： 确保只有可信的第三方服务 IP 能够访问 CDN 资源。 |
| IP 黑名单 | 防止恶意攻击： 检测到某 IP 频繁发起异常请求时，将其加入黑名单，禁止恶意的 IP 访问。 地域访问限制： 禁止高风险地区的 IP 访问（如某些政策限制的国家）， 封禁来自某些国家或地区的 IP 地址段。 |
## 计费说明
配置IP黑/白名单功能本身不收费，但被拦截的请求仍会产生少量费用。
计费原理：拦截发生在HTTP请求处理阶段（七层），此时CDN节点已经处理了请求，消耗了资源。
计费项：
流量费用：被拦截的请求会产生一次请求（包含HTTP头）和一次响应（403页面）的流量。这部分流量按标准CDN流量计费。
HTTPS请求数费用：如果域名使用HTTPS协议，由于TLS握手在IP拦截前已经完成，因此每次被拦截的HTTPS请求仍会计算一次HTTPS请求数费用。
## 注意事项
一个域名只能配置一条IP黑名单或IP白名单规则，且两者互斥，无法同时配置。
配置IP黑名单后，黑名单中的IP请求仍然可以到达CDN节点，但会被节点拒绝并返回403状态码。此时，CDN日志中会记录这些IP的请求信息，但这并不意味着IP黑名单未生效。
少数互联网服务提供商（ISP）在特定区域可能会分配私有IP地址给用户端，导致CDN节点接收到的是用户的私有IP地址。
说明
私有IP地址范围有以下三个：
A类私有IP地址：10.0.0.0～10.255.255.255，子网掩码：10.0.0.0/8
B类私有IP地址：172.16.0.0～172.31.255.255，子网掩码：172.16.0.0/12
C类私有IP地址：192.168.0.0~192.168.255.255，子网掩码：192.168.0.0/16
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击访问控制。
在IP黑/白名单区域，单击修改配置。
您可以根据下方示例，快速进行配置。您也可以参考[参数说明](configure-an-ip-blacklist-or-whitelist.md)，添加适用于自身业务的配置。
场景一：保护管理后台（白名单+规则引擎）
目标：仅允许公司办公室出口 IP203.x.x.10和203.x.x.11访问/admin/路径。
配置：
类型：选择白名单。
规则：填入203.x.x.10和203.x.x.11（换行分隔）。
高级配置-IP规则：选择使用真实建连IP作为判断依据。
高级配置-规则条件：在[规则引擎](rules-engine.md)页面配置一个规则，规则内容为URI包含/admin/*其中任意一个，忽略大小写。然后在规则条件选择此规则。
结果：只有来自这两个 IP 的请求才能访问/admin/目录，其他所有 IP 对该目录的访问都将被拒绝并返回 403 状态码。
场景二：允许合作伙伴的 IPv6 网段访问（白名单）
目标：仅允许合作伙伴的 IPv6 网段FC00:0AA3:0000:0000:0000:0000:0000:0000/48访问。
配置：
类型：选择白名单。
规则：填入FC00:0AA3:0000:0000:0000:0000:0000:0000/48。
高级配置-IP规则：选择使用真实建连IP作为判断依据。
结果：只有来自该 IPv6 地址范围的请求可以访问您的域名资源。
场景三：紧急封禁攻击源（黑名单）
目标：发现一个来自198.x.x.0/24网段的 CC 攻击，需紧急封禁。
配置：
类型：选择黑名单。
规则：填入198.x.x.0/24。
高级配置-IP规则：选择使用真实建连IP作为判断依据。
结果：所有来自198.x.x.0/24网段的 IP 请求都将被 CDN 节点拒绝。
## 参数说明
| 参数 | 说明 |
| --- | --- |
| 类型 | 选择 黑名单 或 白名单 。 黑名单 ：列表中的 IP 地址将被拒绝访问，返回 403 状态码。 白名单 ：仅允许列表中的 IP 地址访问，其他所有 IP 都将被拒绝。 |
| 规则 | 规则格式要求 支持输入 IP 地址或者 IP 地址段。 输入多个 IP 地址或者 IP 地址段时，使用换行符分隔。 支持 IPv4 类型的地址或者地址段： IPv4 地址示例： 192.168.0.1 。 IPv4 地址段示例： 192.168.0.0/24 。 不支持输入通配网络地址 0.0.0.0/0 ，如果需要表示全量 IPv4 地址，可以用以下两个子网来表示： 0.0.0.0/1 128.0.0.0/1 支持 IPv6 类型的地址或者地址段： IPv6 地址示例： FC00:AA3:0:23:3:300:300A:1234 。 IPv6 地址段示例：FC00:0AA3:0000:0000:0000:0000:0000:0000/48。 地址中的英文字母不区分大小写，即支持全大写、全小写或者大小写混合，例如： FC00:AA3:0:23:3:300:300A:1234 或 fc00:0aa3:0000:0023:0003:0300:300a:1234 。 不支持 : : 缩写格式，例如：不支持 FC00:0AA3::0023:0003:0300:300A:1234 。 不支持输入通配网络地址 0000:0000:0000:0000:0000:0000:0000:0000/0 ，如果需要表示全量 IPv6 地址，可以用以下两个子网来表示： 0000:0000:0000:0000:0000:0000:0000:0000/1 8000:0000:0000:0000:0000:0000:0000:0000/1 规则长度限制 规则输入框最大支持输入 30 KB 长度的字符，考虑到 IP 地址或者 IP 地址段的字符串长度有长有短，如果按平均长度来算，最多可配置大约 700 个 IPv6 地址/地址段或者 2000 个 IPv4 地址/地址段。如果您有更多的 IP 地址封禁需求，请开通 ESA 安全防护功能（支持海量 IP 封禁和按区域封禁服务），具体操作方法，请参见 [CDN、DCDN](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/how-to-upgrade-from-cdn-and-dcdn-to-esa/) [和](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/how-to-upgrade-from-cdn-and-dcdn-to-esa/) [ESA](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/how-to-upgrade-from-cdn-and-dcdn-to-esa/) [的功能对照](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/how-to-upgrade-from-cdn-and-dcdn-to-esa/) 和 [IP](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/ip-access-rules) [访问规则配置](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/ip-access-rules) 。 |
| IP 规则 | 支持选择以下三种规则： 使用用户的 x-forwarded-for 请求头作为判断依据 （默认规则） 当客户端均通过可信代理访问，且代理会正确设置 x-forwarded-for 头时，推荐使用该规则。 使用真实建连 IP 作为判断依据 当客户端直接连接 CDN，无中间代理服务器；或希望基于代理服务器 IP 进行访问控制时，推荐使用该规则。 同时使用 x-forwarded-for 和真实建连 IP 作为判断依据 当客户端为混合网络环境，部分用户直连，部分用户通过代理访问时，推荐使用该规则。 |
| 规则条件 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 重要 引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](rules-engine.md) 中进行管理。 |
## 拓展阅读：阿里云CDN如何识别客户端IP
CDN节点通过以下两种方式识别客户端IP，这两种方式各有优劣：
真实建连IP (TCP Connection IP)
定义：客户端与CDN边缘节点建立TCP连接时所使用的IP地址。
优点：无法被伪造，安全性最高。
缺点：当用户通过代理（如公司网络出口、NAT设备）访问时，此IP为代理服务器的IP，无法反映真实的客户端来源。
X-Forwarded-For(XFF) 请求头
定义：一个HTTP请求头字段，用于记录请求经过的每一个代理服务器的IP地址。CDN通常取其最左侧的IP作为客户端IP。
优点：能够穿透代理，获取到真实的客户端IP。
缺点：此请求头可由客户端任意伪造，存在严重安全风险。恶意用户可通过伪造XFF头来绕过基于此IP的访问控制。
当客户端直接访问 CDN 时，这两个 IP 通常是相同的。但如果客户端通过代理服务器访问 CDN，这两个 IP 将会不同。例如，客户端真实 IP 为10.10.10.10，代理服务器 IP 为192.168.0.1，则：
X-Forwarded-For请求头的值可能为10.10.10.10, 192.168.0.1。
客户端真实 IP 为10.10.10.10。
真实建连 IP 为192.168.0.1。
针对上述IP获取方式，CDN提供三种校验模式，以平衡安全性与业务灵活性。
| IP 地址校验模式 | 使用场景 | 工作原理 | 安全性评估 |
| --- | --- | --- | --- |
| 使用用户的 x-forwarded-for 请求头作为判断依据 （默认） | 客户端均通过可信代理访问，且代理会正确设置 XFF 头。 | 仅提取并匹配 x-forwarded-for 请求头中最左侧的 IP 地址。 | x-forwarded-for 请求头可被客户端伪造，恶意用户可轻易绕过黑名单限制。 |
| 使用真实建连 IP 作为判断依据 | 客户端直接连接 CDN，无中间代理服务器；或希望基于代理服务器 IP 进行访问控制。 | 仅使用客户端与 CDN 节点建立 TCP 连接的 IP 地址进行匹配。 | 建连 IP 无法伪造，提供最可靠的防护。 |
| 同时使用 x-forwarded-for 和真实建连 IP 作为判断依据 | 混合网络环境，部分用户直连，部分用户通过代理访问。 | 黑名单 ： x-forwarded-for 头中的 IP 或真实建连 IP，任意一个命中规则即拦截。 白名单 ： x-forwarded-for 头中的 IP 或真实建连 IP，任意一个命中规则即放行。 | 兼顾了识别真实客户端 IP 的灵活性与建连 IP 的安全性，是大多数场景下的最佳选择。 |
## 常见问题
[IP](access-control-faq.md)[黑白名单配置时有](access-control-faq.md)[IP](access-control-faq.md)[地址数量限制，配置](access-control-faq.md)[IP](access-control-faq.md)[地址段算](access-control-faq.md)[1](access-control-faq.md)[个还是多个](access-control-faq.md)[IP](access-control-faq.md)[地址数？](access-control-faq.md)
[需要在源站将](access-control-faq.md)[CDN](access-control-faq.md)[设置为访问白名单，能提供阿里云](access-control-faq.md)[CDN](access-control-faq.md)[访问源站的节点](access-control-faq.md)[IP](access-control-faq.md)[吗？](access-control-faq.md)
[为什么](access-control-faq.md)[IP](access-control-faq.md)[黑名单中的](access-control-faq.md)[IP](access-control-faq.md)[仍可访问资源？](access-control-faq.md)
[如何获取客户端真实](access-control-faq.md)[IP](access-control-faq.md)[地址？](access-control-faq.md)
## 相关API
添加IP黑/白名单配置
调用[BatchSetCdnDomainConfig](../developer-reference/api-cdn-2018-05-10-batchsetcdndomainconfig.md)接口配置IP黑/白名单，相关参数参考[配置](../developer-reference/parameters-for-configuring-features-for-domain-names.md)[IP](../developer-reference/parameters-for-configuring-features-for-domain-names.md)[白名单](../developer-reference/parameters-for-configuring-features-for-domain-names.md)和[配置](../developer-reference/parameters-for-configuring-features-for-domain-names.md)[IP](../developer-reference/parameters-for-configuring-features-for-domain-names.md)[黑名单](../developer-reference/parameters-for-configuring-features-for-domain-names.md)。
更新IP黑/白名单配置
调用[BatchSetCdnDomainConfig](../developer-reference/api-cdn-2018-05-10-batchsetcdndomainconfig.md)接口更新IP黑/白名单，相关参数参考[配置](../developer-reference/parameters-for-configuring-features-for-domain-names.md)[IP](../developer-reference/parameters-for-configuring-features-for-domain-names.md)[白名单](../developer-reference/parameters-for-configuring-features-for-domain-names.md)和[配置](../developer-reference/parameters-for-configuring-features-for-domain-names.md)[IP](../developer-reference/parameters-for-configuring-features-for-domain-names.md)[黑名单](../developer-reference/parameters-for-configuring-features-for-domain-names.md)。
重要
接口的更新逻辑为：仅更新传入的参数。例如，若在请求中传入了ip_list参数而未传入ip_acl_xfwd，则ip_acl_xfwd不会被更新。
该接口仅支持对IP列表、IP规则和规则条件进行更新，不允许更改配置类型。例如，无法通过该接口将IP黑名单配置更改为IP白名单配置。
如果您需要更改配置类型（例如，将IP黑名单配置更改为IP白名单配置），需按照以下步骤操作：
调用删除配置接口，移除现有的IP黑名单配置。
调用添加配置接口，重新添加IP白名单配置。
删除IP黑/白名单配置
步骤一：查询ConfigId
调用[查询域名配置](../developer-reference/api-cdn-2018-05-10-describecdndomainconfigs.md)接口，查询配置的ConfigId。如果您知道对应配置的ConfigId，请忽略此步骤，参考步骤二进行删除配置。
步骤二：删除配置
调用[DeleteSpecificConfig](../developer-reference/api-cdn-2018-05-10-deletespecificconfig.md)接口，使用ConfigId删除配置。
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
