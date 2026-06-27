# 防范流量盗刷最佳实践-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/use-cases/best-practices-for-preventing-traffic-theft

# 防范流量盗刷最佳实践
当您的域名因被恶意攻击或流量被恶意盗刷，产生了突发高带宽或者大流量消耗，导致产生高于日常消费金额的高额账单。因恶意攻击或流量盗刷产生的高额账单无法免除/退款，为尽量避免此类风险，本文为您介绍这一类情况的应对办法。
## 及时止损
当您已经发现域名因被恶意攻击或流量被恶意盗刷，并且产生了高额账单，请先设置带宽上限和单请求限速，以此来减少进一步的损失，设置完成后再进一步分析日志做出针对性的安全设置。
### 控制带宽用量
通过设置带宽上限，来控制带宽用量。当指定加速域名在统计周期（1分钟）内产生的平均带宽超出预设上限，CDN将停止为该域名提供加速服务，且该域名会被解析到无效地址offline.***.com，无法继续访问。因此设置带宽封顶带宽值时，可根据日常业务峰值预留适当带宽空间。具体操作请参见[配置带宽封顶](../user-guide/configure-bandwidth-caps.md)。
### 限制下行速率
通过配置单请求限速，对用户访问到CDN节点的所有请求进行下行速率限速，以此来压制加速域名的全网带宽峰值。具体操作请参见[配置单请求限速](../user-guide/configuration-order-request-speed-limit.md)。
## 分析原因
### 查询账单明细，确认流量异常的时间段
您可以在费用与成本[明细账单](https://billing-cost.console.aliyun.com/finance/expense-report/expense-detail-by-instance)页面查看云产品相关的消费明细。根据实际需求选择统计维度和统计周期，查看不同维度的报表。详细操作请参见[明细账单](https://help.aliyun.com/zh/user-center/billing-details-1)。
统计周期选择明细，产品选择CDN，仔细审查账单，注意流量和带宽的异常增加，以及流量异常的时间段。具体请参见[账单查询](../product-overview/query-bills.md)。
### 检查日志文件，识别异常流量
基础查询：离线日志
通过下载离线日志，查看相关时间段的访问日志，分析HTTP请求的详细信息，识别可疑的IP地址、User-Agent等。离线日志字段数据相对较少，如果您想查看更多数据，可使用实时日志功能。
获得离线日志文件后，您可以使用命令行工具来快速解析日志文件，提取访问量TOP10的IP地址或User-Agent等信息，详情请参见[CDN](../analysis-method-of-alibaba-cloud-content-delivery-network-access-log.md)[访问日志的分析方法](../analysis-method-of-alibaba-cloud-content-delivery-network-access-log.md)。
进阶查询：运营报表和实时日志
重要
运营报表需定制后才会进行生产统计分析，如果您之前已配置过实时日志推送或订阅运营报表，您可以查看到过去的日志信息。运营报表为CDN自带免费功能，无需额外付费。
实时日志需要开通日志服务（SLS）并成功投递日志后，才会生成实时日志。实时日志为付费功能，具体计费请参见[计费详情](../user-guide/overview-1.md)。
实时日志和运营报表均需要提前配置，如果您在产生高额账单之前未配置过这两项功能，只能通过离线日志进行历史数据分析。
运营报表
定制运营报表后，您可以看到用户访问的PV/UV、地区和运营商、域名排行、热门referer、热门URL、回源热门URL和Top客户端IP等报表内容。具体操作请参见[定制和订阅运营报表](../user-guide/customize-an-operations-report-template-and-create-a-tracking-task.md)。
实时日志
如果您想查询更多日志信息，例如Referer和URI等信息，需要开通[日志服务](https://sls.console.aliyun.com)[SLS](https://sls.console.aliyun.com)，将采集到的实时日志实时推送至日志服务。开启实时日志，并成功投递日志后，根据日志投递条数产生计费。
参考[配置实时日志推送](../user-guide/configure-real-time-log-delivery.md)为需要分析用户访问数据的CDN加速域名配置实时日志推送。
在实时日志功能页面找到需要分析日志的Project名称，单击日志分析。
进入日志分析页面，在右上角过滤时间段，单击左侧原始日志页签，找到refer_domain字段，您可以看到由高到低排列的Referer信息。
## 解决问题
当您获取到了日志或报表数据后，您可以通过数据特征来分析攻击类型。通常您可以分析Top信息（Top IP、Top User-Agent、Top Referer等）提取特征。
### 限制可疑IP访问
通过配置IP黑名单，限制访问源IP。分析日志后，筛选出一些可疑的攻击IP，您需要将这些可疑的IP地址列入黑名单。具体操作请参见[配置](../user-guide/configure-an-ip-blacklist-or-whitelist.md)[IP](../user-guide/configure-an-ip-blacklist-or-whitelist.md)[黑/白名单](../user-guide/configure-an-ip-blacklist-or-whitelist.md)。
### 过滤可疑User-Agent
攻击者通过伪造User-Agent字段发送大量请求，试图绕过安全检查。伪造的User-Agent可能是空值、随机字符串或常见浏览器的伪造字符串。您可以配置User-Agent白名单或黑名单，拒绝非正常的User-Agent请求。例如，拒绝空User-Agent或不符合规范的随机字符串，您可以使用参数this-is-empty-ua和RandomString分别来表示空User-Agent和随机字符串。具体操作请参见[配置](../user-guide/configure-a-user-agent-blacklist-or-whitelist.md)[UA](../user-guide/configure-a-user-agent-blacklist-or-whitelist.md)[黑白名单](../user-guide/configure-a-user-agent-blacklist-or-whitelist.md)。
### 添加可疑Referer至黑名单
攻击者在请求头中伪造Referer字段，以假冒合法的引用来源，进行恶意请求。配置Referer黑白名单，允许合法的Referer访问，防止未经授权的第三方网站链接到资源，拒绝带有恶意Referer的请求。在规则输入框中填写日志中查询出的异常Referer，建议勾选忽略Scheme。具体操作请参见[配置](../user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[Referer](../user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[黑/白名单](../user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)。
### 升级至ESA并接入WAF、Bots防护
建议您将域名迁移至[ESA](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/what-is-esa)产品，ESA提供丰富的防护功能，不仅可以保护数据安全，同时也提升了访问速度和用户体验。您可以根据[CDN、DCDN](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/how-to-upgrade-from-cdn-and-dcdn-to-esa/)[和](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/how-to-upgrade-from-cdn-and-dcdn-to-esa/)[ESA](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/how-to-upgrade-from-cdn-and-dcdn-to-esa/)[的功能对照](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/how-to-upgrade-from-cdn-and-dcdn-to-esa/)的指引，快速完成域名的迁移。然后根据下方引导，快速接入ESA的安全防护功能。
## WAF
ESA的[WAF](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/waf-overview/)提供了IP访问规则、白名单规则、自定义规则等丰富的规则匹配拦截能力，避免网站服务器被恶意入侵，保障业务的核心数据安全。
### 配置IP访问规则
在ESA控制台，选择[站点管理](https://esa.console.aliyun.com/siteManage/list)，在站点列单击目标站点。
在站点详情页面，选择安全防护>WAF>IP访问规则。
选择并填写需要防护的IP/IP段、[ASN](https://help.aliyun.com/zh/edge-security-acceleration/esa/support/what-is-asn)、区域信息，并设置执行动作，单击添加规则。执行动作详情参考[执行动作说明](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/ip-access-rules#56609e4e27ghb)。
可选：创建的规则默认对站点下所有HTTP（7层）请求生效。如需在TCP/UDP（4层代理）请求中生效需在站点详情页面，选择四层代理>配置，在配置页面点击创建应用，在创建应用页面中开启IP访问控制。
### 配置白名单规则
在ESA控制台，选择[站点管理](https://esa.console.aliyun.com/siteManage/list)，单击目标站点操作列的配置WAF。
在站点详情页面，选择安全防护>WAF>白名单规则。
在白名单规则页签，单击新增规则，配置以下参数。
填写规则名称，建议使用能描述放行目的的名称，例如"内部扫描工具放行"。
在如果请求匹配以下规则...区域配置匹配条件，设置识别可信请求的特征，例如客户端IP、URL路径、请求头等。请求匹配规则的详细配置方法，请参见[运算符和分组符号](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/work-with-rules-engine/)。
在则跳过…区域选择该请求需要跳过的防护规则范围。
全部规则：跳过所有WAF和Bots管理规则。适用于完全可信、需要无拦截通过的请求来源。
部分规则种类或ID：选择要跳过的规则类型和[具体规则](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/whitelist-rules#29362fb0b3ojr)[ID](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/whitelist-rules#29362fb0b3ojr)（例如Bot管理、智能限频、频次控制），推荐使用此模式，在放行可信流量的同时保留其他防护能力。
### 配置自定义规则
在ESA控制台选择[站点管理](https://esa.console.aliyun.com/siteManage/list)，在站点列单击目标站点。
在左侧导航栏，选择安全防护>WAF。
单击自定义规则页签，进入自定义规则页签，单击新增规则。
填写规则名称。
在如果请求匹配以下规则...区域设置要匹配的用户请求特征，请求匹配规则参见[运算符和分组符号](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/work-with-rules-engine/)。
在则执行…区域设置当请求命中该规则时，要执行的防护动作，详细信息请参见[执行动作说明](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/waf-custom-rules#ed19696507a84)。
单击确定。
## Bots防护
ESA的[快速上手](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/bots)支持简易模式和高级模式的配置。通过简易模式您可以快速的为当前站点配置爬虫管理，而高级模式提供了更为精准的爬虫规则，方便您针对性的对网站或APP作出调整。
### 使用简易模式
简易模式是面向安全入门级用户的机器流量、爬虫管理功能，适用于所有套餐版本的用户，但是对于部分功能使用会有一些套餐限制。相比于需要专业配置能力配置复杂规则的高级模式，简易模式默认将流量划分为了3类，您只需要快速选择对某类爬虫的处置动作即可实现对爬虫的管理。
配置全局策略
在ESA控制台，选择[站点管理](https://esa.console.aliyun.com/siteManage/list)，在站点列单击目标站点。
在左侧导航栏，选择安全防护>Bots。
在Bots页面，选择简易模式，根据下列说明选择合适的配置项进行配置。
绝对是Bot：包含大量恶意爬虫请求。通常建议您配置拦截或滑块挑战。
可能是Bot：这类的请求风险较绝对是Bot相对较低，有可能包含恶意爬虫以及其他流量。通常建议您配置观察或在风险较高时期做滑块挑战。
已通过验证的Bot：这类通常是各类搜索引擎的爬虫，有利于您网站的SEO优化。一般建议放行，如您不希望任何搜索引擎爬虫访问您的站点时可做拦截操作。
为静态资源请求配置Bots检测
若您购买了企业版套餐，可以[配置静态资源免受恶意 Bots 的攻击](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/protect-static-resources)。
重要
如果您启用静态资源保护，可能会阻止定期获取静态资源的正常Bots（例如邮件客户端）。启用此功能之前，请确保您了解现有的基础架构。
启用JavaScript检测
若您购买了企业版套餐，可以使用轻量隐性的[JavaScript](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/javascript-detection)[检测](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/javascript-detection)采集浏览器指纹以提升Bots识别结果。
### 使用高级模式
通过高级模式，您可以为站点配置针对特定请求的防护规则集，并对不同的防护行为单独设置生效时间。高级模式还支持防护移动应用，也可以将规则集跨域配置到您账户下的其他站点中。您可以参考下面的步骤配置 Bots 规则集：
在ESA控制台，选择[站点管理](https://esa.console.aliyun.com/siteManage/list)，在站点列单击目标站点。
在左侧导航栏，选择安全防护>Bots。
在Bots页面，选择高级模式，单击创建规则集。
填写规则集名称，选择防护目标类型为网页/浏览器，选择SDK集成方式为自动集成（推荐）。
根据您需要过滤的请求条件在如果请求匹配以下规则...中配置规则表达式，例如针对来自中国内地的请求进行Bots防护，可配置为：(ip.geoip.country in {"CN"})。更多支持的字段可参考[Bots](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/rules-match-fields-available-for-bots)[可用的规则匹配字段](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/rules-match-fields-available-for-bots)。
选择需要添加的防护执行动作。
针对搜索引擎的Bots：
[合法](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#458e1fa445hit)[Bot](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#458e1fa445hit)[管理](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#458e1fa445hit)：建议您可以配置您信赖的指定搜索引擎Bots直接放行。
伪造爬虫拦截：用于快速拦截所有搜索引擎的Bots，可结合[合法](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#458e1fa445hit)[Bot](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#458e1fa445hit)[管理](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#458e1fa445hit)控制仅放行执行搜索引擎Bots。
针对已知Bots库：
[爬虫威胁情报库](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#8da0dac6f4aod)：来自阿里云针对已识别到的恶意 Bots 建立的攻击源 IP 地址库，建议您开启滑块校验应对它们。
[IDC](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#8da0dac6f4aod)[黑名单封禁](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#8da0dac6f4aod)：如果您的用户客户端不会来自公有云或 IDC 的机房，可以在IDC黑名单封禁中直接设置阻断 IDC的请求。
针对需要判别的请求：
[Bot](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#c3e848838dn9g)[特征识别](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#c3e848838dn9g)：对比真实的用户浏览器访问特征来识别非浏览器类 Bots。
[Bot](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#e796719ffexvg)[行为识别](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#e796719ffexvg)：ESA对客户端传入的流量进行分析后自动训练机器学习模型，并且生成防护规则或黑名单。您可以根据实际拦截情况配置应对措施。
[自定义限速](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#4ed90b96f85xh)：当您想要放行一些 Bots 请求但是又不想它们访问太过频繁，您可以对来自同一IP或同一特定的会话请求进行频次控制——对访问频次超过指定阈值的请求执行防护动作。
在生效时间区域，单击对应规则右侧的编辑，设置生效时间后单击确定。
完成配置后单击确定。
## 安全分析
[安全分析](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/security-analysis)用于展示WAF和Bot管理的拦截、观察和总访问量等数据，以便您根据数据动态调整您的防护规则。
### 分析维度
筛选器：支持按照Host、HTTP版本、客户端IP等维度筛选过滤。选择筛选条件后，仅显示与筛选条件匹配的数据结果。
查询时间：默认展示过去24小时的请求特征信息，支持自定义查询时间，最多可查询至过去30天的数据。
### 查看安全分析报表
在Web应用遭遇突发性流量峰值或检测到异常攻击行为时，应通过安全分析模块对HTTP/S请求流量进行实时特征解析，核验其与预设的合法请求特征基线（包括但不限于Header结构、载荷模式、访问频率）的合规性。针对偏离基线的非预期流量（如SQL注入特征、CC攻击特征），可联动WAF引擎动态加载预定义或自定义防护规则集（如正则表达式匹配、速率限制策略），实施精准的请求阻断与攻击溯源，实现纵深防御体系下的主动式威胁处置。
说明
安全分析获取的数据信息存在约5分钟的延迟。
账号维度
安全分析提供针对当前账户下所有接入站点的报表入口，用于分析所有站点的防护信息。
登录[ESA](https://esa.console.aliyun.com/siteManage/list)[控制台](https://esa.console.aliyun.com/siteManage/list)，在左侧导航栏选择分析和日志>安全分析。
在安全分析页面，查看防护信息，通过筛选器选出您需要的数据信息。可以点击图标打印页面报告或点击图标将数据以CSV格式下载保存到本地进行分析。
站点维度
安全分析提供特定接入站点的报表入口，用于分析该站点的防护信息。
在ESA控制台选择[站点管理](https://esa.console.aliyun.com/siteManage/list)，在站点列单击目标站点。
在左侧导航栏，选择安全防护>安全分析。
在安全分析页面，查看防护信息，通过筛选器选出您需要的数据信息。可以点击图标打印页面报告或点击图标将数据以CSV格式下载保存到本地进行分析。
说明
可以参考[根据异常流量进行特定防护](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/get-started-with-security#33cfddfc9bzqb)在安全防护页面单击以筛选条件创建 WAF 自定义规则或以筛选条件创建 Bot 规则来对异常流量进行统一防护管理。
## 后续防护
### 设置实时监控
设置对CDN产品下指定域名的带宽峰值监控，达到设定的带宽峰值后将会给管理员发送告警（短信、邮件和钉钉），便于更加及时地发现潜在风险。详情请参见[设置报警](../user-guide/set-an-alert-rule.md)。
### 设置费用预警
您可以在控制台右上方菜单栏费用选择费用与成本，通过设置以下这几个功能来更好地控制账户的消费额度，避免产生过高的账单。
可用额度预警：您可以设置账户余额低于一定金额时即向您发送短信告警。
启用延停额度：您可以选择关闭该功能，这样在账号欠费时会立即关闭业务，以避免产生更多消费。更多信息，请参见[延期免停权益](https://help.aliyun.com/zh/user-center/exemption-of-suspension-after-delinquency)。
说明
为了保证计量数据统计的完整性，确保账单的准确性，CDN产品需要在记账周期结束后大约3个小时才能生成实际的账单，因此实际扣款时间与对应的资源消费时间存在一定的时延，无法通过账单来实时反馈资源消耗情况，这是由CDN产品自身的分布式节点特性决定的，每个CDN服务商都采用类似的处理办法。
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
