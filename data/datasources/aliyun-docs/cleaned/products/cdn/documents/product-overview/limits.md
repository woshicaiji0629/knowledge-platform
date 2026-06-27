# 使用限制-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/product-overview/limits

# 使用限制
域名接入阿里云CDN之前，您需要了解阿里云CDN加速域名的接入条件和限制，避免因域名涉及违规内容而造成损失。
## 安全限制
| 限制项 | 说明 |
| --- | --- |
| 安全违规行为 | 所有接入 CDN 的域名都要经过内容审核， CDN 目前不支持接入的域名包括但不限于： 无法正常访问或内容不包含任何实质信息 游戏私服类 传奇类游戏和纸牌类游戏 盗版软件、盗版小说、盗版视频、盗版漫画等无内容版权的网站 P2P 类金融网站 彩票类网站 违规医院和药品类网站 涉黄、涉毒、涉赌等 如果您想了解更多违规行为以及违规信息，请参见 [安全违规行为类型说明](https://help.aliyun.com/zh/document_detail/469814.html) 和 [安全违规信息类型说明](https://help.aliyun.com/zh/document_detail/469816.html) 。 说明 含有以上违规内容的加速域名，由您自行承担任何可能的风险。阿里云 CDN 系统也将定期复审域名内容，如果发现以上任何违规行为，则系统会立即下线或封禁域名。情节严重的将封禁整个账号下域名服务，且永不恢复。 如果您在阿里云 CDN 接入了一个泛域名（例如 *.example.com ）进行加速，该泛域名包含的某个精确域名（例如 a.example.com ）出现了以上违规内容，阿里云 CDN 将下线该泛域名（ *.example.com ）。 如果您的域名审核被拒绝，请在控制台的域名列表查看拒绝原因，请自行整改后重新提交域名审核。 详细说明，请参见 [CDN](../alibaba-cloud-content-delivery-network-dynamic-route-for-content-delivery-network-add-accelerated-domain-name-audit-failed.md) [加速域名审核失败](../alibaba-cloud-content-delivery-network-dynamic-route-for-content-delivery-network-add-accelerated-domain-name-audit-failed.md) 。 |
| URL 屏蔽的解除办法 | 通过 [阿里云安全管控申诉](https://page.aliyun.com/form/act1555286298/index.htm) 自助申诉。 |
| 域名违规导致的加速域名清退申诉方案 | 可以通过下边的三步申请加速域名解封： 需要对违规网站进行彻底整改，例如删除违法内容、文件或链接，整改涉诈信息等。 准备相关的申诉材料。 营业执照（必须和域名的备案信息一致）。 域名的业务说明。 通过 [智能在线](https://ia.aliyun.com/) 反馈给阿里云售后，申请解封。 |
| 突发带宽/QPS 限流规则 | 根据您与阿里云签订的 [《CDN](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud201802111644_54364.html?spm=a2c4g.11186623.2.2.35fa3be7Szv8A7) [服务协议》](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud201802111644_54364.html?spm=a2c4g.11186623.2.2.35fa3be7Szv8A7) ，如果您对 CDN 服务有突发带宽/QPS 使用需求（包括但不限于带宽容量压测、QPS 性能压测、促销活动、重大发布等），您需要至少提前 3 个工作日（重大节日的突发，包括但不限于春晚，双十一等，需要提前至少 1 个月）联系阿里云客户经理或通过阿里云 [其它渠道](https://help.aliyun.com/zh/document_detail/464625.html#task-2155749) 申请突发带宽用量。 若申请成功，在双方约定的突发量级内，可确保您的服务不受影响。 若申请不成功或未申请，则对于突发带宽，阿里云有权采取限流等措施（不会 100%触发限流，阿里云会根据域名业务情况、突发带宽量级等因素综合判断）来保障全网用户的稳定性，由此导致的可用性问题，阿里云不承担责任。 未提前申请突发用量或申请不成功，有可能会出现以下问题： 带宽突增有可能会触发阿里云 CDN 的限流规则。 详细信息，请参见 [突发带宽说明](billing-rules-of-basic-services.md) 。 QPS 突增有可能会触发阿里云 CDN 的 CC 防护规则，导致域名被切入 [沙箱](../user-guide/introduction-to-sandboxes.md) 。 |
| 域名被攻击或盗刷的潜在风险 | 阿里云 CDN 产品默认并不提供访问控制或者安全防护能力，如果您的域名因被恶意攻击或流量被恶意盗刷，产生了突发高带宽或者大流量消耗，很可能会产生高于日常消费金额的高额账单。 因恶意攻击或流量盗刷产生的高额账单无法免除/退款，为尽量避免此类风险，您可以通过 [高额账单风险警示](configure-high-bill-alerts.md) 了解这一类情况的应对办法。 |
| 域名沙箱模式 | 沙箱说明 ：当您的域名遭受攻击（例如 DDoS 或 CC 攻击）或者未向阿里云提前报备业务突增情况，而出现带宽或者 QPS 大幅度上涨时，CDN 系统有权将您的域名切入 [沙箱说明](../user-guide/introduction-to-sandboxes.md) （不会 100%将域名切入沙箱，阿里云会根据域名业务情况、攻击影响程度等因素综合判断），防止影响其他正常用户的加速服务。在攻击较严重的情况下，同账户下的其他域名也会被切入沙箱，同时还会限制账号下的新域名接入。 |
## 加速域名限制
| 限制项 | 说明 |
| --- | --- |
| 域名格式要求 | 域名（例如： image.example.com ）总长度不超过 100 字符。 域名去掉根域名之后的子域名部分（例如：域名 image.example.com 去掉根域名 example.com 之后的子域名是 image ）的长度不超过 64 字符。 支持：小写英文字母（a~z）、数字（0~9）和短划线（-），例如 example.com。 不支持：中文、英文大写字母（A~Z）和除了短划线（-）以外的其他符号，且短划线（-）不能连续出现、不能单独使用、不能出现在开头和结尾。如果域名包含中文（例如：阿里云.网址），请以中文形式进行相关备案，再通过第三方工具 punycode 将中文域名转换成为英文域名（例如：xn--fiq****.xn--eq****）后填入。 |
| 泛域名要求 | CDN 支持泛域名加速，关于泛域名的添加规则， 请参见 [CDN](../does-alibaba-cloud-cdn-support-wildcard-domain-names.md) [支持泛域名加速吗？](../does-alibaba-cloud-cdn-support-wildcard-domain-names.md) 。 泛域名和子域名必须在同一个账号下，否则添加域名时系统会报错。 如果泛域名未被添加到任何 CDN 账号下，则支持在多个账号下添加不同的子域名。 当您将 .aliyundoc.com 形式的泛域名和 example.aliyundoc.com 形式的精确域名一起添加到 CDN 时，精确域名的数量上限为 500 个，超过 500 个后新增的精确域名将无法生效，即无法使用 CDN 加速服务。 说明 未超出 500 个之前匹配到的精确域名使用不受影响。 如果您的加速域名为泛域名 *.example.com ，那么二级子域名 www.example.com 可以被加速，但是二级根域名 example.com 无法被加速。您可以为二级根域名 example.com 单独配置一个加速域名。 说明 添加加速域名时应选择主域名还是泛域名？ CDN 添加加速域名时支持泛域名（如 *.example.com ）和具体域名（如 example.com ）。若要覆盖所有子域名，应添加泛域名 *.example.com ；若仅加速二级根域名，则添加 example.com 即可。注意，泛域名不包含二级根域名（如 example.com ）。 |
| 域名备案要求 | 备案 ：如果您的加速区域为 全球 或 仅中国内地 ，无论源站在哪里域名都必须备案，推荐您进入 [阿里云](https://beian.aliyun.com/?spm=5176.8142029.388261.3.a0SCC3) [ICP](https://beian.aliyun.com/?spm=5176.8142029.388261.3.a0SCC3) [代备案管理系统](https://beian.aliyun.com/?spm=5176.8142029.388261.3.a0SCC3) 进行备案。ICP 备案接入前请参考 [备案服务器检查](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-server-access-information-check#concept-m5j-vrl-zdb) 完成相关准备与检查。 开启 CDN 加速后，用户的访问请求会被调度至就近的 CDN 节点，因此用户实际访问的 IP 地址会随节点分配而变化，这是 CDN 的正常工作机制。CDN 节点 IP 的变化不会影响源站 IP，也不会影响域名的 ICP 备案状态。ICP 备案是针对源站进行的，与 CDN 节点 IP 无关，您无需因 CDN 节点 IP 变化而担心备案被取消。 |
| 域名数量限制 | 每个阿里云账号最多可以添加 50 个加速域名 。 说明 如果您域名的总带宽日均峰值大于 50 Mbps，且业务无风险，可参见 [配额管理](../user-guide/quota-management.md) 申请增加域名个数。 加速域名不允许重复添加 ：如果需要将 CDN 域名跨账号迁移到另一个阿里云账号上， 请参考 [跨账号迁移](../user-guide/domain-name-transfer.md) [CDN](../user-guide/domain-name-transfer.md) [域名](../user-guide/domain-name-transfer.md) 验证域名归属权后 ，将目标域名迁移到当前账号。如果出现目标域名已被添加到其他云产品（例如视频点播、DCDN 等）的提示，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 处理。 |
| 域名回收/下线限制 | 回收规则 ：如果您的域名处于停用状态超过 120 天（包含审核未通过状态），阿里云 CDN 会自动删除该域名的相关记录。如果您需要继续使用，需前往阿里云 [CDN](https://cdn.console.aliyun.com/) [控制台](https://cdn.console.aliyun.com/) 重新添加域名。 下线（offline）规则 ：详细信息，请参见 [关于域名下线（Offline）规则调整的公告](rules-for-disabling-accelerated-domain-names.md) 。 |
## 源站限制
| 限制项 | 说明 |
| --- | --- |
| 源站地址长度 | 最长不超过 67 个字符。 |
| 源站数量 | 每个加速域名的源站数量最多可以设置 20 个。 |
| OSS 域名 | 在下拉列表中选择同一账号下 OSS 的外网域名作为源站。 手动输入阿里云 OSS 的外网域名作为源站（不支持 OSS 内网域名作为源站），例如： ***.oss-cn-hangzhou.aliyuncs.com ，OSS 外网域名可前往 [OSS](https://oss.console.aliyun.com/) [控制台](https://oss.console.aliyun.com/) 查看。 说明 关于加速 OSS 资源的实践，请参见 [CDN](../use-cases/use-alibaba-cloud-cdn-to-accelerate-the-delivery-of-resources-from-oss-buckets.md) [加速](../use-cases/use-alibaba-cloud-cdn-to-accelerate-the-delivery-of-resources-from-oss-buckets.md) [OSS](../use-cases/use-alibaba-cloud-cdn-to-accelerate-the-delivery-of-resources-from-oss-buckets.md) [资源](../use-cases/use-alibaba-cloud-cdn-to-accelerate-the-delivery-of-resources-from-oss-buckets.md) 。 阿里云 CDN 回源阿里云 OSS 的流量优惠说明： 用户需要在 CDN 控制台上把源站类型设置为“OSS 域名”，这样阿里云 OSS 产品会将来自阿里云 CDN 产品的回源流量识别为“ CDN 回源流出流量”，从而享受到更优惠的价格。 如果用户在 CDN 控制台上把源站类型误设为“源站域名”，阿里云 OSS 产品会将来自阿里云 CDN 产品的回源流量识别为“外网流出流量”，这种情况下就享受不到优惠价格。 详细的费用说明，请参见 [CDN](billing-of-oss-content-acceleration.md) [加速](billing-of-oss-content-acceleration.md) [OSS](billing-of-oss-content-acceleration.md) [计费说明](billing-of-oss-content-acceleration.md) 。 采用阿里云 OSS 作为源站时，必须要 [配置默认回源](../user-guide/configure-the-default-origin-host.md) [HOST](../user-guide/configure-the-default-origin-host.md) ，并且默认回源 HOST 的值为 OSS Bucket 的公网地址域名，否则会无法访问源站。 采用阿里云 OSS 作为源站时，建议 [配置默认回源](../user-guide/configure-sni.md) [SNI](../user-guide/configure-sni.md) ，并且默认回源 SNI 的值为 OSS Bucket 的公网地址域名，否则可能会被 OSS 限流。 |
| IP | 支持配置单个或者多个 IP 作为源站地址，不支持内网 IP，支持 IPv4 地址和 IPv6 地址，不能全部配置 IPv6 地址，必须至少配置一个 IPv4 地址，使用阿里云 ECS 的外网 IP 作为源站地址可免审核。如果要配置 IPv6 源站地址，您需要提前开启 IPv6 回源功能，如果没有提前开启，那么配置的 IPv6 源站地址将无法生效，这会导致回源失败。详细信息，请参见 [配置](../user-guide/configure-back-to-origin-routing-over-ipv6.md) [IPv6](../user-guide/configure-back-to-origin-routing-over-ipv6.md) [回源](../user-guide/configure-back-to-origin-routing-over-ipv6.md) 。 关于源站类型为 IP 的配置实践，敬请参见 [CDN](../use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) [加速](../use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) [ECS](../use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) [资源](../use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) 。 |
| 源站域名 | 支持配置域名作为源站地址，可配置多个域名。 说明 关于源站类型为域名的配置实践，敬请参见 [CDN](../use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) [加速](../use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) [ECS](../use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) [资源](../use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) 。 源站域名不能与加速域名相同。若加速域名和源站域名一致，会导致请求反复解析到 CDN 节点上，造成循环解析，使得 CDN 节点无法回源。 阿里云 CDN 当前支持直接将阿里云 ALB 产品的实例地址（例如： example.hangzhou.alb.aliyuncs.com ）添加为 CDN 的源站。 源站域名格式： 域名长度为 1~67 个字符。 支持：小写英文字母（a~z）、数字（0~9）和短划线（-），例如 example.com 。 不支持：中文、英文大写字母（A~Z）和除了短划线（-）以外的其他符号，且短划线（-）不能连续出现、不能单独使用、不能出现在开头和结尾。如果域名包含中文（例如：阿里云.网址），请以中文形式进行相关备案，再通过第三方工具 punycode 将中文域名转换成为英文域名（例如：xn--fiq****.xn--eq****）后填入。 |
| 函数计算域名 | 函数计算域名 ：支持将您在同一账号下的函数计算产品上配置的函数计算域名，配置为源站地址。您需要选择函数计算 区域 和 域名 。操作方法，请参见 [配置自定义域名](https://help.aliyun.com/zh/functioncompute/fc-2-0/user-guide/configure-a-custom-domain-name#multiTask145) 。 |
## 回源限制
| 限制项 | 说明 |
| --- | --- |
| 回源请求头最大长度 | 最大不能超过 300 Bytes。 |
| 回源请求超时时间 | TCP 层默认为 10 秒，HTTP 层默认为 30 秒。 |
| 回源的 Content-Type | 如果源站不响应 Content-Type ， CDN 会自动添加 Content-Type:application/octet-stream 。 |
| Head 请求默认转换为 Get 请求方式回源 | 默认情况下，用户的 Head 请求经过阿里云 CDN 节点之后再访问源站，会被自动转换为 Get 请求方式，如果您希望保持 Head 请求回源的方式， 请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) ，联系客服为您处理。 |
| 回源请求头默认的字符串格式转化 | 使用 回源 HTTP 请求头 功能添加的回源请求头，在实际回源的时候，字符串的大小写格式会被自动转换成驼峰式，例如： 示例 1：回源请求头 ALI-CDN 在实际回源的时候会被改写为 Ali-Cdn 。 示例 2：回源请求头 ALICDN 在实际回源的时候会被改写为 Alicdn 。 如果您需要关闭默认改写，可以通过 回源 HTTP 请求头 功能添加以下回源请求头： 自定义参数： Ali-Swift-Header-Capitalize 取值：off |
## 缓存刷新限制
| 限制项 | 说明 |
| --- | --- |
| 缓存刷新 | URL 刷新：10000 条/日/每账号。 目录刷新：100 条/日/每账号。 如果您账号的日带宽峰值大于 200 Mbps，可参考 [配额管理](../user-guide/quota-management.md) 申请提升每日配额，阿里云将根据您业务的实际需求进行评估和配置。 |
| 文件预热 | 仅支持 URL 预热，配额限制为 1000 条/日/每账号。 如果您账号的日带宽峰值大于 200 Mbps，可参考 [配额管理](../user-guide/quota-management.md) 申请提升每日配额，阿里云将根据您业务的实际需求进行评估和配置。 |
## 访问限制
| 限制项 | 说明 |
| --- | --- |
| 访问区域“全球（不包含中国内地）”的限制 | 加速域名 的 加速区域 选择为 全球（不包含中国内地） 的情况下，阿里云 CDN 禁止用户请求访问中国内地的节点，此时用户的请求被调度至邻近境外节点（如中国香港、日本、新加坡）。 |
| 访问区域“全球”和“全球（不包含中国内地）”的区别 | 覆盖范围 全球 ：覆盖全球所有 CDN 节点（含中国内地），服务范围最广。 全球（不包含中国内地） ：仅覆盖中国内地以外的全球节点（含中国香港、中国澳门和中国台湾）。 节点调度策略 全球 ：用户就近访问最优节点（含中国内地节点），中国内地用户可能直连本地节点，延迟更低。 全球（不包含中国内地） ：强制排除中国内地节点，中国内地用户会被调度至邻近境外节点（如中国香港、日本、新加坡），可能增加延迟。 访问路径与速度 全球 ：全球用户（含中国内地）均享受本地化加速，访问速度更均衡。 全球（不包含中国内地） ：海外及中国香港、中国澳门和中国台湾用户优先优化，中国内地用户需跨境访问，速度可能受影响。 适用场景 全球 ：需兼顾中国内地与海外用户的业务（如跨国企业官网、全球化应用）。 全球（不包含中国内地） ：目标用户集中在海外或需规避中国内地网络环境（如纯海外业务、国际媒体内容分发）。 |
| 源站 HTTP 响应头总大小限制 | 在源站返回 CDN 节点的信息里面，HTTP 响应头的总大小不能超过 32 KB，否则会返回 502 错误状态码。 |
| URL 长度限制、HTTP 请求头长度限制、URL＋所有 HTTP 请求头的总长度限制 | HTTP2.0 场景下： 默认 Nginx 参数 http2_max_field_size=32 KB ，即单个 HTTP 请求头和单个请求 URL 的长度，均不能超过 32 KB，否则返回 414 错误码。 默认 Nginx 参数 http2_max_header_size=128 KB ，表示所有 HTTP 请求头长度+URL 的长度之和，不能超过 128 KB，否则返回 400 错误码。 HTTP1.1 场景下：目前 CDN 的 large_client_header_buffers 值配置的是 number=4、size=64 KB ，即单个 HTTP 请求头和单个请求 URL 的长度，均不能超过 64 KB，否则返回 414 错误码；并且所有 HTTP 请求头长度+URL 的长度之和，不能超过 256 KB，否则返回 400 错误码。 |
| 请求方式 | 常见的 HTTP 请求方式里面， CDN 支持 GET 、 PUT 、 POST 、 HEAD 和 OPTIONS 这几种请求方式。 说明 如果需要支持 DELETE 和 PATCH 请求方式，请使用 DCDN 全站加速产品，并且开启动态加速功能。 PUT 请求方式支持带有请求体（BODY）或者不带请求体（ Content-Length=0 ）的 HTTP 请求。 POST 请求方式支持 chunk 编码，支持带有请求体（BODY）或者不带请求体（ Content-Length=0 ）的 HTTP 请求。 对于访问静态缓存资源的场景，默认情况下，CDN 节点会将用户的 HEAD 请求转换为 GET 请求方式回源，如果您希望保持 HEAD 请求方式回源， 请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) ，联系客服为您处理。 |
| 物联网卡访问限制 | 根据中华人民共和国工业和信息化部（简称：工信部）的相关规定（《关于印发〈物联网卡安全分类管理实施指引（试行）〉的通知》（工网安函[2020]1173 号）），阿里云 CDN 产品在中国内地无法为使用物联网卡的终端提供加速服务，终端设备使用物联网卡来访问阿里云 CDN 节点的情况下，很可能会无法连接到节点 IP。 |
| HTTPS 访问限制 | 如果客户端在发起与 CDN 节点的 SSL 握手时没有传递 SNI 信息，则 CDN 节点无法保证能够握手成功。 |
## API限制
| 限制项 | 说明 |
| --- | --- |
| 单用户可调用 API 接口频率限制 | 针对阿里云 CDN 产品上所有 API 接口，单用户可调用频率为 1000 次/秒。超过阈值上限时，会返回下述提示信息： ErrorCode:Throttling ErrorMessage:Request was denied due to flow control. |
## 其他限制
| 限制项 | 说明 |
| --- | --- |
| CNAME 域名 | 阿里云 CDN、DCDN、直播以及点播产品的 CNAME 域名仅可以作为阿里云 CDN 的调度解析使用，对于恶意使用 CNAME 域名的行为，阿里云有权清退对应的域名和账号。 |
| 文件 | 文件缓存 源站响应了可以缓存的响应头： CDN 节点可以缓存的文件最大为 500 GB。 文件上传 通过阿里云 CDN 产品向源站上传文件，上传文件的大小限制为单个文件最大不超过 300 MB。 |
| 边缘脚本规则数量限制 | 默认 1 个域名仅支持配置 2 条 EdgeScript 规则，如果需要配置多条规则， 修改出站请求头 。 |
| 功能配置数量限制 | 添加的配置项数量最多为 50 条，包括但不限于以下功能： 修改出站请求头 、 修改入站响应头 、 重写回源路径 、 重写回源参数 、 缓存过期时间 。 |
| Gzip 压缩、Brotli 压缩 | 当源站文件的大小在 1 KB~10 MB 及之间时，才可以使用 Gzip 压缩或 Brotli 压缩，对 1 KB 以下和 10 MB 以上大小的文件不做压缩。 |
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
