# 规则引擎介绍-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/rules-engine

# 规则引擎
规则引擎功能使用图形化方式配置条件规则。条件规则支持识别用户请求中的各种参数信息，以决定某个配置是否对该请求生效，可用于灵活、精确地控制CDN的配置策略执行效果。
## 背景说明
阿里云CDN产品控制台提供了配置缓存过期时间、回源参数改写等基础功能，满足大部分通用需求。但对于一些特殊需求，如将包含路径/example的请求回源到指定源站地址，则需要结合规则引擎实现自定义配置。此外，阿里云CDN还提供了[边缘脚本](edgescript-overview.md)功能，支持高度灵活的用户定制需求，配置类似第三方 CDN 服务商（如 Fastly、CloudFront）的精细化策略。
| 配置能力 | 基础功能 | 基础功能+规则引擎 | 边缘脚本 |
| --- | --- | --- | --- |
| 功能实现 | 常见的通用功能配置 | 通过图形化配置界面实现各种条件过滤目的的规则，支持 URI、Header、Cookie、Query String 等多种匹配类型，以及 AND/OR 逻辑组合。 | 支持高度灵活的用户定制需求，适合需要编写自定义脚本的高级场景。 |
| 使用场景 | 常见的通用需求 | 部分自定义高级配置需求 | 定制化的用户需求 |
| 上手难度 （对用户技术要求） | 低 | 中 | 高 |
| 配置灵活性 | 低 | 中 | 高 |
## 复杂逻辑配置与边缘脚本替代方案
规则引擎支持基础的 AND/OR 逻辑组合，适用于大部分条件过滤场景。但以下场景建议使用[边缘脚本（EdgeScript）](edgescript-overview.md)替代：
复杂正则匹配：规则引擎的正则运算符默认禁用，需[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请开启。对于需要频繁使用正则表达式的场景，边缘脚本原生支持正则匹配，更加便捷。
多维度精确组合：若需同时匹配客户端 IP 和 User-Agent 并使用正则表达式进行复杂判断（例如拦截特定 IP 段且 UA 包含特定关键词的请求），规则引擎的配置可能较为繁琐。边缘脚本支持通过脚本逻辑灵活组合多种条件。
指定 URI 的精确访问控制：若仅需针对指定 URI 设置 Referer 或 IP 白名单拦截，可直接在规则引擎中配置 URI 匹配条件，无需使用边缘脚本。
## 注意事项
单个域名下最多支持创建50个规则条件。
单个规则条件中的子条件数量最多不超过20个。
通过控制台或者OpenAPI来配置时，无法使用正则相关的匹配运算符（包括正则匹配和正则不匹配），但是可以查看已有配置。如果要使用正则相关的匹配运算符，推荐使用[边缘安全加速](https://www.aliyun.com/product/esa?spm=5176.28536895.J_kUfM_yzYYqU72woCZLHoY.3.11cf586c1lhOVC)。
通过控制台或者OpenAPI配置时，单个域名下所有功能对规则条件的总引用次数最大不超过5次。
规则条件支持嵌套，嵌套层次最多为3层，不同层级支持独立的逻辑关系设置。
缓存过期时间、修改出站请求头等其他功能引用规则条件后，按所关联规则条件的优先级执行，而非按功能自身的配置顺序执行。
上述数量限制（50 个规则条件、20 个子条件、3 层嵌套、5 次引用）均为系统硬性上限，无法通过后台申请调整。
每个条件的匹配值最多支持 32 个（适用于客户端 IP、URI、文件扩展名、文件名、User-Agent 等匹配类型）。若客户端 IP 白名单数量较多，建议将多个 IP 地址转换为 IP 段（CIDR 格式，例如120.209.XXX.X/24）进行配置，以节省匹配值配额。
User-Agent 匹配值最多支持配置 32 个，超过该数量的配置不生效。若需匹配大量 User-Agent，建议使用通配符（*）合并相似的 UA 值（例如*Chrome*可覆盖所有 Chrome 浏览器版本），或改用[边缘脚本](edgescript-overview.md)实现更灵活的匹配逻辑。
## 功能优先级与执行逻辑
配置规则引擎时，需注意以下功能优先级和执行逻辑：
Referer 防盗链优先级高于规则引擎：当请求携带 Referer 时，系统先执行 Referer 黑白名单校验。若命中 Referer 白名单，请求直接放行，不再执行规则引擎中的其他条件判断；若未命中白名单，请求直接被拦截。只有当请求的 Referer 为空时，才不会触发 Referer 黑白名单的放行或拦截逻辑，请求会继续匹配规则引擎中配置的条件。
规则条件引用功能的执行顺序：缓存过期时间、修改出站请求头等功能引用规则条件后，按所关联规则条件的优先级执行，而非按功能自身的配置顺序执行。例如，若缓存过期时间和回源参数改写分别引用了优先级不同的规则条件，系统会按规则条件的优先级从高到低依次执行。
鉴权与缓存配置冲突排查：若配置 URL 鉴权后出现非预期行为（如不携带鉴权参数仍可正常访问、或合法链接被误拦截），请按以下顺序排查：
检查是否配置了 WAF 白名单，WAF 白名单可能绕过CDN的鉴权逻辑导致请求直接放行。
检查忽略 URL 参数配置是否将鉴权参数（如auth_key）过滤掉，导致缓存命中时跳过鉴权校验。
确认鉴权参数未被缓存 Key 规则忽略，避免不同鉴权参数的请求命中同一缓存。
## 规则条件的语法说明
一个规则条件由“逻辑判断运算符”与“条件表达式”构成，具体见下方说明。
### 逻辑判断（Logic）
对同一个层级内的条件（包括被嵌套的条件集合）进行逻辑判断，支持and和or。
and（并且）：逻辑与运算符，所有条件都为真才会匹配成功。
or（或者）：逻辑或运算符，其中一个条件为真即可匹配成功。例如为同一个响应头配置多个规则条件，可实现不同条件下添加相同响应头的效果。示例：当 URI 包含/path-a或URI 包含/path-b时，执行添加响应头的操作。
### 条件表达式包含的参数
最小粒度的条件表达式包含以下参数：
| 参数名称 | 域名配置功能函数 [condition](../developer-reference/parameters-for-configuring-features-for-domain-names.md) 中对应的配置参数 | 参数说明 | 是否必填 |
| --- | --- | --- | --- |
| 条件匹配 | match | 表示条件匹配表达式。 | 是 |
| 逻辑判断 | logic | 表示条件匹配表达式的逻辑判断参数，取值为 and 和 or 。 | 是 |
| 条件判断内容 | criteria | 表示条件表达式的判断内容。 | 是 |
| 匹配类型 | MatchType | 表示对用户请求中携带的某一类型信息进行匹配。 | 是 |
| 匹配对象 | MatchObject | 表示对匹配类型进行进一步的细分，例如：客户端 IP 可以细分为“建联 IP”和“XFF IP”。 | 否 |
| 匹配运算符 | MatchOperator | 表示匹配操作执行的具体动作。 | 是 |
| 匹配值 | MatchValue | 表示预先设定的匹配值，将会与用户请求中携带的信息进行匹配。 | 是 |
| 条件判断值取反 | negate | 表示是否对条件表达式的结果取反，取值为 true 和 false。 | 是 |
| 大小写敏感 | caseSensitive | 表示对匹配值中的字符是否大小写敏感。 | 否 |
| 规则条件名称 | name | 表示规则条件的名称。 | 是 |
| 生效状态 | status | 表示规则条件的生效状态。 | 是 |
### 条件表达式的配置方法
| 匹配类型名称 | 域名配置功能函数 [condition](../developer-reference/parameters-for-configuring-features-for-domain-names.md) 中对应的配置参数 | 匹配类型含义 | 匹配对象 | 匹配运算符 | 匹配值 | 大小写敏感 | 对应 nginx/tengine |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 协议类型 | scheme | 客户端请求使用的协议类型，例如：HTTP、HTTPS。 | 不涉及 | 等于 不等于 | http https | 不涉及 | $scheme |
| 请求方法 | method | 客户端请求使用的请求方法，例如：GET、PUT。 | 不涉及 | 等于 不等于 | get put post delete head | 不涉及 | $request_method |
| URI（路径） | uri | 客户端请求 URL 中的路径，不含请求参数，例如： /favicon.ico 。 | 不涉及 | 包含其中任意一个 不包含其中任意一个 | 支持通配符 ? 和 * , 例如：填写 /*/my_path/* ，支持输入多个值。 | 区分大小写 忽略大小写 | $raw_uri 或$uri |
| 文件名 | basename | 客户端请求的文件的名称，例如：name1。 | 不涉及 | 包含其中任意一个 不包含其中任意一个 | 支持通配符 ? 和 * ，支持输入多个值。 | 区分大小写 忽略大小写 | - |
| 文件扩展名 | extension | 客户端请求的文件的后缀名，从右向左识别，识别到第一个"."，例如： .mp4 。 | 不涉及 | 包含其中任意一个 不包含其中任意一个 | 支持通配符 ? 和 * ，支持输入多个值。 | 区分大小写 忽略大小写 | - |
| Hostname | hostname | 客户端请求携带的 hostname，匹配顺序：请求 URL 中的 host>请求头 HOST 中的 host。 | 不涉及 | 包含其中任意一个 不包含其中任意一个 | 用户请求的 host，支持输入多个值。 | 区分大小写 忽略大小写 | $host 或$http_host |
| 客户端 IP | clientip | 客户端的 IP。 支持 IPv4（例如 1.1.X.X ）、IPv6（例如 240e:95c:3004:2:3:0:0:XXX ）、支持网段（例如 20.209.XXX.XXX/31 ）。 | 建联 IP XFF IP 说明 建联 IP、XFF IP 详细说明，请参见 [IP](rules-engine.md) [地址校验模式](rules-engine.md) 。 | 包含其中任意一个 不包含其中任意一个 | 支持填写 IPv6 格式 IP，例如：240e:XXX:3004:2:3:0:0:3f7，支持网段方式填写，例如：120.209.XXX.XXX/31，支持输入多个值。 | 不涉及 | $remote_addr |
| 客户端 IP 版本 | clientipVer | IPv4 或 IPv6。 | 建联 IP XFF IP 说明 建联 IP、XFF IP 详细说明，请参见 [IP](rules-engine.md) [地址校验模式](rules-engine.md) 。 | 等于 不等于 | v4 v6 | 不涉及 | - |
| 用户网络运营商 | geolocation | 客户端 IP 归属的运营商。 | 建联 IP XFF IP 说明 建联 IP、XFF IP 详细说明，请参见 [IP](rules-engine.md) [地址校验模式](rules-engine.md) 。 | 包含其中任意一个 不包含其中任意一个 | 可以通过下拉列表来选择，可以输入字符来过滤选项，支持输入 ID 或名称来模糊匹配查询，支持输入多个值。 | 不涉及 | $ip_isp_id |
| 用户 IP 地理位置 | geolocation | 客户端 IP 所处的地理位置。 | 建联 IP XFF IP 说明 建联 IP、XFF IP 详细说明，请参见 [IP](rules-engine.md) [地址校验模式](rules-engine.md) 。 | 包含其中任意一个 不包含其中任意一个 | 可以通过下拉列表来选择，可以输入字符来过滤选项，支持输入 ID 或名称来模糊匹配查询，支持输入多个值。 | 不涉及 | $ip_country_id |
| 请求参数 | querystring | 用户请求 URL 中携带的请求参数。 | 输入参数名称。 | 存在 不存在 包含其中任意一个 不包含其中任意一个 大于 大于等于 小于 小于等于 | 支持通配符 ? 和 * ，支持输入多个值。 | 区分大小写 忽略大小写 | $arg_{name} |
| 请求头 | header | 用户请求中携带的请求头。 | 支持输入参数名称，也支持通过下拉列表来选择参数。 | 存在 不存在 包含其中任意一个 不包含其中任意一个 大于 大于等于 小于 小于等于 | 支持输入多个值。 | 区分大小写 忽略大小写 | $http_{name} |
| Cookie | cookie | 请求携带的 Cookie。 | 输入 Cookie 名称。 | 存在 不存在 包含其中任意一个 不包含其中任意一个 大于 大于等于 小于 小于等于 | 支持通配符 ? 和 * ，支持输入多个值。 | 区分大小写 忽略大小写 | $cookie_{name} |
| User-Agent | useragent | 请求头里的 User-Agent。 | 不涉及 | 包含其中任意一个 不包含其中任意一个 | 可以选择下拉列表中的值，或者直接输入 UA 值，例如： *Chrome/25* ，支持通配符 ? 和 * ，支持输入多个值（最多仅支持配置 32 个 UA，超过这个数量后，配置的 UA 不生效）。 | 区分大小写 忽略大小写 | $http_user_agent |
| Range 分桶 | range | 将客户端请求分桶，按百分比执行。 | 不涉及 | 等于 不等于 | 输入百分比的数值。 | 不涉及 | - |
| 时间 | time | 客户端请求发生的时间，时区为东八区（北京时间），例如：09:10~14:22。 | 不涉及 | 包含其中任意一个 不包含其中任意一个 | 直接输入时间段，例如 09:10~14:22 ，表示 9 点 10 分至 14 点 22 分。 | 不涉及 | - |
| Nginx Var | ngxvar | 当上方所有的变量均无法满足需求时，支持使用 Nginx 变量来配置，支持的变量详见 Nginx 官网： [Nginx](http://nginx.org/en/docs/varindex.html) [变量](http://nginx.org/en/docs/varindex.html) 。 | 可以通过下拉列表来选择或直接输入变量名，支持 $region:$isp 这种拼接方式。 | 存在 不存在 包含其中任意一个 不包含其中任意一个 大于 大于等于 小于 小于等于 | 支持输入多个值。 | 不涉及 | ${name} |
条件表达式常见配置说明
URI（路径）匹配起始位置：URI 匹配的值为域名后第一个/开始的路径部分，不包含域名和请求参数。例如，对于请求https://example.com/path/file.html?key=value，实际匹配的 URI 值为/path/file.html。配置匹配值时需以/开头。
文件扩展名匹配格式：配置文件扩展名匹配时，匹配值必须包含点号（.）。例如，要匹配.txt文件，应填写.txt而非txt，否则可能导致匹配失败。
通配符使用示例：URI 和文件扩展名均支持通配符?（匹配任意 1 个字符）和*（匹配任意多个字符）。常用示例：
/*.pdf：匹配根目录下所有 PDF 文件。
/api/*/data：匹配/api/下任意子路径中的data路径。
.??：匹配所有两个字符的文件扩展名（如.js、.ts）。
### IP地址校验模式
规则引擎功能的“IP地址校验模式”分为两种，使用不同的“IP地址校验模式”会影响到CDN节点对客户端IP的判断：
建联 IP：该模式匹配客户端与CDN节点之间建连使用的IP，如果客户端与CDN节点之间有经过代理服务器，那么建联IP=代理服务器IP。
XFF IP：该模式匹配用户请求中x-forwarded-for请求头携带的左边第一个IP，不论客户端与CDN节点之间是否有经过代理服务器，XFF IP都=客户端真实IP。
选择使用哪一种“IP地址校验模式”主要取决于用户请求在经过CDN节点时，中间是否有经过代理服务器。
需注意，引用规则条件的功能在CDN节点上的生效位置也会影响到对“IP地址校验模式”的选择（对于在L2节点上生效的回源配置相关功能而言，用户请求经过的L1节点就相当于中间经过了代理服务器）。
示例：假设客户端真实IP为10.10.10.10，代理服务器IP为192.168.0.1。
没有经过代理服务器：
用户请求中x-forwarded-for请求头值：10.10.10.10。
客户端真实IP（即x-forwarded-for请求头携带的左边第一个IP）=客户端与CDN节点建连IP=10.10.10.10。
经过代理服务器：
用户请求中x-forwarded-for请求头值：10.10.10.10,192.168.0.1。
客户端真实IP（即x-forwarded-for请求头携带的左边第一个IP）=10.10.10.10。
客户端与CDN节点建连IP=代理服务器IP=192.168.0.1。
客户端真实IP（即x-forwarded-for请求头携带的左边第一个IP）≠客户端与CDN节点建连IP。
少数ISP在特定区域可能会分配私有IP地址给用户端，导致CDN节点接收到的是用户的私有IP地址。
说明
私有IP地址范围有以下三个：
A类私有IP地址：10.0.0.0～10.255.255.255，子网掩码：10.0.0.0/8
B类私有IP地址：172.16.0.0～172.31.255.255，子网掩码：172.16.0.0/12
C类私有IP地址：192.168.0.0~192.168.255.255，子网掩码：192.168.0.0/16
### 匹配运算符（matchOperator）
| 名称 | 域名配置功能函数 [condition](../developer-reference/parameters-for-configuring-features-for-domain-names.md) 中对应的配置参数 | 含义 |
| --- | --- | --- |
| 等于 | matchOperator 为 equals。 | 变量完全等于匹配值或者完全不等于匹配值的时候，条件才成立。 |
| 不等于 | matchOperator 为 equals，并且参数 negate 的值为 true。 |  |
| 存在 | matchOperator 为 exists。 | 变量存在或者不存在时，条件即成立。 |
| 不存在 | matchOperator 为 exists，并且参数 negate 的值为 true。 |  |
| 包含其中任意一个 | matchOperator 为 contains。 | 变量包含（不包含） 任意一个 匹配值的时候，条件即成立。最多支持 32 个匹配值。 包含匹配的情况有两种： 精确匹配：直接输入匹配对象，包含：a，必须=a 才能匹配上。 通配符匹配：可以加入 * 作为通配符，可以支持配置 a* 、 *a 、 *a* ，可以对应 abc、bca、bcabc。 |
| 不包含其中任意一个 | matchOperator 为 contains，并且参数 negate 的值为 true。 |  |
| 大于 | matchOperator 为 gt。 | 即 > |
| 小于 | matchOperator 为 lt。 | 即 < |
| 大于等于 | matchOperator 为 ge。 | 即 >= |
| 小于等于 | matchOperator 为 le | 即 <= |
| 正则匹配 | matchOperator 为 regex。 | 匹配值可以填写正则表达式，实现对变量的正则匹配。 说明 通过控制台或者 OpenAPI 来配置的情况下，无法使用正则相关的匹配运算符（包括正则匹配和正则不匹配），但是可以查看已经存在的配置，如果要使用正则相关的匹配运算符，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 申请，或者使用 [边缘安全加速产品](https://www.aliyun.com/product/esa?spm=5176.28536895.J_kUfM_yzYYqU72woCZLHoY.3.11cf586c1lhOVC) 。 |
| 正则不匹配 | matchOperator 为 regex，并且参数 negate 的值为 true。 |  |
### 通配符
| 通配符号 | 含义 | 路径匹配示例 |
| --- | --- | --- |
| ? | 表示匹配任意 1 个字符。 | /img/?.png 匹配 /img/a.png 、 /img/b.png 等单字符文件名的资源。 |
| * | 表示匹配任意多个字符。 | /api/* 匹配 /api/ 下的所有路径（如 /api/v1/users 、 /api/v2/products ）； /static/*.css 匹配 /static/ 目录下所有 CSS 文件。 |
## 当前支持引用规则条件的功能
| 功能分类 | 功能名称 |
| --- | --- |
| 基本配置 | [条件源站](configure-a-conditional-origin.md) |
| 缓存配置 | [缓存过期时间](configure-the-cdn-cache-expiration-time.md) |
| [修改出站响应头](create-a-custom-http-response-header.md) |  |
| [访问](create-an-access-url-rewrite-rule.md) [URL](create-an-access-url-rewrite-rule.md) [改写规则](create-an-access-url-rewrite-rule.md) |  |
| [自定义](create-custom-cache-keys.md) [Cache Key](create-custom-cache-keys.md) |  |
| 回源配置 | [修改出站请求头](configure-custom-request-headers.md) |
| [修改入站响应头](rewrite-http-response-headers.md) |  |
| [重写回源参数](rewrite-url-parameters-in-back-to-origin-requests.md) |  |
| [指定源站回源](specify-an-origin-host-for-each-origin.md) [HOST](specify-an-origin-host-for-each-origin.md) |  |
| 访问控制 | [配置](configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md) [Referer](configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md) [黑/白名单](configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md) |
| [配置](configure-url-signing.md) [URL](configure-url-signing.md) [鉴权](configure-url-signing.md) |  |
| [配置](configure-an-ip-blacklist-or-whitelist.md) [IP](configure-an-ip-blacklist-or-whitelist.md) [黑/白名单](configure-an-ip-blacklist-or-whitelist.md) |  |
| [配置](configure-a-user-agent-blacklist-or-whitelist.md) [UA](configure-a-user-agent-blacklist-or-whitelist.md) [黑白名单](configure-a-user-agent-blacklist-or-whitelist.md) |  |
| 性能优化 | [忽略参数](ignore-parameters.md) |
| 视频相关 | [配置](object-chunking.md) [Range](object-chunking.md) [回源](object-chunking.md) |
| 流量限制 | [单请求限速](configuration-order-request-speed-limit.md) |
### 配置查看与管理说明
执行动作查看位置：规则引擎页面仅定义规则条件，不直接配置执行动作。具体的执行动作（如缓存过期时间、URL 改写、限速等）需在引用了该规则的对应功能页面查看和管理。例如，若某个缓存过期时间配置引用了规则条件，需在「缓存配置」>「缓存过期时间」中查看和修改。
远程鉴权不支持绑定规则引擎：远程鉴权功能目前不支持引用规则条件，无法通过规则引擎控制远程鉴权的生效范围。
鉴权超时限制：远程鉴权的鉴权超时时长最高可设置为 3000 毫秒（3 秒），默认值为 500 毫秒，这是系统支持的极限值。
### 高级用法
以下为结合规则引擎实现高级配置的典型场景：
差异化限速策略：若需对部分请求限速、部分不限速（例如对携带鉴权参数的地址限速，对其他地址不限速），或配置兜底限速策略，可在规则引擎中创建区分请求特征的规则条件，然后在「单请求限速」中分别引用不同规则条件并设置不同的限速值。
基于 IP 的灰度回源：若需实现基于客户端 IP 的灰度发布或特定 IP 回源到不同源站，可在规则引擎中创建 IP 匹配条件，然后在「条件源站」中引用该规则条件，指定不同的回源地址。
混合源站架构建议：若需同时使用 WAF 和 OSS 作为源站，不建议直接配置多个主源站。应使用规则引擎根据 URL 路径创建匹配条件，然后通过「条件源站」动态指定不同路径的回源地址，避免多源站回源冲突。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击规则引擎。
单击添加规则。
在添加规则页面，设置规则名称和规则内容。
单击提交，完成配置。
## 典型配置场景
以下列举两个高频配置场景的实现思路。
### 场景一：IP 白名单访问控制与非白名单跳转
需求：仅允许特定 IP 访问站点，其他 IP 自动跳转至维护页面。
配置思路：
在规则引擎中创建规则条件，设置匹配类型为「客户端 IP」，匹配运算符为「不包含其中任意一个」，匹配值填写白名单 IP 地址。
在「缓存配置」>「访问 URL 改写」中引用该规则条件，将匹配到的请求（即非白名单 IP）重定向至指定的维护页面 URL（例如 OSS 上托管的 HTML 页面）。
注意事项：
若非白名单 IP 返回 403 而非预期跳转，需检查是否配置了多个 OSS 源站导致回源冲突。建议一个CDN域名只对应一个主 OSS 源站。
确保目标维护页面 URL 可公开访问，且未被其他访问控制规则拦截。
### 场景二：Referer 防盗链与文件扩展名组合控制
需求：限制特定扩展名文件的 Referer 访问，但允许空 Referer 访问特定扩展名的文件。
配置思路：
在规则引擎中创建规则条件，设置匹配类型为「文件扩展名」，匹配运算符为「不包含其中任意一个」，匹配值填写需要豁免的扩展名（如.pdf）。
在「访问控制」>「Referer 防盗链」中引用该规则条件。这样，非指定扩展名的请求受 Referer 黑白名单限制，而指定扩展名的空 Referer 请求可通过规则豁免。
## 常见问题
### 指定源站回源 HOST 设置的规则是否会计入高级条件规则数量限制？
是的。域名下对应功能只要使用过对应的规则，都会被计入高级条件规则数量限制中。请注意单个域名下最多支持创建 50 个规则条件，单个规则条件中的子条件数量最多不超过 20 个。
### 配置规则引擎后，执行动作在哪里？
规则引擎本身用于定义条件，需与其他功能（如缓存过期时间、回源参数改写、URL 重写等）联动生效。执行动作体现在所关联的具体功能配置中，可在对应功能配置处查看或管理已引用的规则。例如，可以先创建一个规则条件定义匹配逻辑，然后在缓存过期时间功能中引用该规则，使缓存策略仅对匹配该规则的请求生效。
### 开启 URL 鉴权时，如何通过规则引擎匹配请求参数控制视频下载？
在开启 URL 鉴权（A 鉴权）的情况下，可以通过规则引擎匹配请求参数来控制行为。建议在规则引擎中配置「URL 包含」条件，匹配特定的业务参数名或值（如download=1）。
说明
鉴权参数本身不建议作为匹配依据，以免影响鉴权的正常校验。但其他业务参数（如download）可以正常匹配。
确保最终生成的 URL 中包含与规则一致的参数（例如http://.../video.mp4?auth_key=...&download=1），即可触发对应的响应头配置实现下载控制。
### 如何配置 301 跳转规则？
可以通过创建访问 URL 重写规则来实现域名跳转。在规则引擎中配置 URI 匹配条件，配合 URL 重写功能，即可实现如将www.example.com跳转至shop.example.com的效果。
### 如何配置子域名 301 强制跳转到顶级域名？
可以在 CDN 侧配置 URL 重写实现此需求。具体配置如下：
在规则引擎中配置 URI 匹配条件，匹配类型选择「URI（路径）」，匹配运算符选择「正则匹配」（需通过工单申请开通正则匹配权限，或使用边缘安全加速），匹配值设置为^/(.*)$。
在 URL 重写功能中，将目标路径设置为https://顶级域名/$1，其中$1为正则表达式捕获的路径部分。
例如，将sub.wetqt.com/any/path强制跳转至https://wetqt.com/any/path。
### 如何配置规则引擎实现匹配指定路径后不缓存？
针对不同的匹配需求，可采用以下两种配置方式：
针对文件后缀：在缓存配置中，对不需要缓存的文件后缀设置缓存过期时间为 0；对需要缓存的文件后缀设置合适的缓存时间（如 4 小时），并在缓存配置中设置「不忽略源站」、「不缓存头部」、「不遵循源站缓存时间」。
针对路径匹配：由于 CDN 控制台不支持完整 URL 的正则表达式匹配，需通过规则引擎配置 URI 路径匹配来实现。匹配类型选择「URI（路径）」，匹配运算符选择「包含其中任意一个」或「不包含其中任意一个」，匹配值中可使用通配符?和*。例如，填写/*/no-cache/*可匹配/api/no-cache/data等路径。
### 路径匹配的起始位置是否从域名后的第一个/开始？
是的。规则引擎中若使用路径匹配（非正则），匹配内容是从域名后的第一个/开始的路径部分。例如对于https://example.com/a.html，实际匹配的路径为/a.html。
CDN 原生不支持如^https?://([^/]+)/path这类包含协议和域名的完整 URL 正则表达式匹配。
### 配置文件名匹配时，为什么首次响应头没有生效？
在规则引擎中配置文件名匹配时，请注意「文件名（basename）」和「文件扩展名（extension）」是两个独立的匹配类型：
文件名（basename）：匹配不包含文件后缀的文件名部分。例如script（不包含.js）。
文件扩展名（extension）：匹配文件的后缀名。例如.js、.css。
如果在文件名匹配中包含了文件后缀（如script.js），将无法正确匹配。请将文件后缀去除，仅填写文件名部分（如script）即可生效。
### 如何配置匹配所有静态资源（如 js 和 css 文件）？
在规则引擎中按照文件扩展名进行匹配，可匹配对应的静态资源。具体操作：
匹配类型选择「文件扩展名」。
匹配运算符选择「包含其中任意一个」。
匹配值填写.js,.css（多个扩展名用英文逗号分隔）。
这样即可匹配所有.js和.css扩展名的请求。也可以添加更多扩展名，如.js,.css,.png,.jpg。
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
