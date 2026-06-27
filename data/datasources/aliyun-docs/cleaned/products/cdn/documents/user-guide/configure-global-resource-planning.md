# 配置全球资源计划-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-global-resource-planning

# 配置全球资源计划
全球资源计划是一种资源服务计划，同时使用阿里云自建节点和全球合作伙伴节点为域名提供加速服务。开启后，您的域名可以享受更丰富的节点资源，更好地覆盖非中国内地区域，提升域名的访问体验。
## 节点分布
全球资源计划在全球覆盖200+节点，具体节点分布如下表所示：
| 计费区域 | 节点分布 |
| --- | --- |
| 北美 | 美国、加拿大、墨西哥 |
| 南美 | 巴西、阿根廷、哥伦比亚、智利、秘鲁 |
| 欧洲 | 英国、德国、意大利、荷兰、法国、瑞典、奥地利、西班牙、波兰、比利时、瑞士、葡萄牙、保加利亚、克罗地亚、捷克、丹麦、芬兰、希腊、匈牙利、爱尔兰、挪威、罗马尼亚 |
| 亚太 1 区 | 中国香港、中国台湾、日本、新加坡、菲律宾、马来西亚、泰国 |
| 亚太 2 区 | 韩国、印度、越南、印度尼西亚 |
| 亚太 3 区 | 澳大利亚、新西兰 |
| 中东/非洲 | 以色列、阿拉伯联合酋长国、南非、阿曼、尼日利亚、巴林、肯尼亚 |
说明
全球资源计划开启前后[计费规则](../product-overview/billing-overview.md)不变。
## 注意事项
该功能正在分阶段开放中，如果您暂时还未看到该功能，请耐心等待。
仅支持加速区域为全球（不包含中国内地）的域名。
全球资源计划开启后支持部分功能。具体范围请参考[开启全球资源计划后支持的配置功能](configure-global-resource-planning.md)。
全球资源计划开启后无法直接关闭。关闭该功能需要删除后重新添加域名至阿里云 CDN。
## 开启全球资源计划后支持的配置功能
说明
暂不支持POST请求。
开启全球资源计划之后，您的域名可以享受更丰富的节点资源，但是支持的功能会受到限制，请谨慎评估之后使用。以下为全球资源计划支持的功能列表：
| 功能大类 | 功能集 | 功能介绍 | 全球资源计划支持情况 |
| --- | --- | --- | --- |
|  | 基本配置 | [加速区域修改](change-the-accelerated-region.md) | 不支持 |
| [源站配置](configure-an-origin-server.md) | 支持 |  |  |
| [配置条件源站](configure-a-conditional-origin.md) | 不支持 |  |  |
| [IPv6](configure-ipv6.md) [配置](configure-ipv6.md) | 支持 |  |  |
| 回源配置 说明 默认支持 Range 回源功能，控制台暂不支持关闭。如果需要关闭，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 。 | [配置默认回源](configure-the-default-origin-host.md) [HOST](configure-the-default-origin-host.md) | 支持 |  |
| [指定源站回源](specify-an-origin-host-for-each-origin.md) [HOST](specify-an-origin-host-for-each-origin.md) | 支持 |  |  |
| [配置回源协议](configure-the-origin-protocol-policy.md) | 支持 |  |  |
| [OSS](grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md) [私有](grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md) [Bucket](grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md) [回源](grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md) | 支持 |  |  |
| [配置默认回源](configure-sni.md) [SNI](configure-sni.md) | 不支持 |  |  |
| [指定回源](specify-origin-sni.md) [SNI](specify-origin-sni.md) | 不支持 |  |  |
| [配置回源请求超时时间](configure-a-timeout-period-for-back-to-origin-http-requests.md) | 支持 |  |  |
| [修改出站请求头](configure-custom-request-headers.md) | 支持 |  |  |
| [修改入站响应头](rewrite-http-response-headers.md) | 支持 |  |  |
| [Common Name](common-name-whitelist.md) [白名单](common-name-whitelist.md) | 不支持 |  |  |
| [高级回源](configure-advanced-origin-settings.md) | 不支持 |  |  |
| [配置回源](configure-301-or-302-redirection.md) [301/302](configure-301-or-302-redirection.md) [跟随](configure-301-or-302-redirection.md) | 不支持 |  |  |
| [重写回源路径](rewrite-urls-in-back-to-origin-requests.md) | 支持 |  |  |
| [重写回源参数](rewrite-url-parameters-in-back-to-origin-requests.md) | 支持 |  |  |
| 缓存配置 | [配置缓存过期时间](configure-the-cdn-cache-expiration-time.md) | 支持 |  |
| [配置状态码过期时间](create-a-cache-rule-for-http-status-codes.md) | 不支持 |  |  |
| [修改出站响应头](create-a-custom-http-response-header.md) | 不支持 |  |  |
| [配置自定义页面](create-a-custom-error-page.md) | 不支持 |  |  |
| [配置访问](create-an-access-url-rewrite-rule.md) [URL](create-an-access-url-rewrite-rule.md) [改写规则](create-an-access-url-rewrite-rule.md) | 不支持 |  |  |
| [自定义](create-custom-cache-keys.md) [Cache Key](create-custom-cache-keys.md) | 不支持 |  |  |
| [配置共享缓存](configure-shared-cache.md) | 不支持 |  |  |
| [响应过期缓存](serve-stale-content.md) | 不支持 |  |  |
| HTTPS 配置 说明 默认支持 TLS v1.2 版本，暂不支持修改配置。如果需要兼容 TLS v1.0 和 v1.1 版本，您可以 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 申请。 | [配置](configure-an-ssl-certificate.md) [HTTPS](configure-an-ssl-certificate.md) [证书](configure-an-ssl-certificate.md) 说明 仅支持 2048 和 3072 位的 RSA 密钥。 | 支持 |  |
| [配置](enable-http-or-2.md) [HTTP/2](enable-http-or-2.md) | 支持 |  |  |
| [配置协议重定向](configure-url-redirection.md) 说明 仅支持默认和 HTTP 跳转至 HTTPS 方式。 | 支持 |  |  |
| [配置](configure-tls-version-control.md) [TLS](configure-tls-version-control.md) [版本控制与加密套件](configure-tls-version-control.md) | 不支持 |  |  |
| [配置](configure-hsts.md) [HSTS](configure-hsts.md) | 不支持 |  |  |
| [配置](configure-ocsp-stapling.md) [OCSP Stapling](configure-ocsp-stapling.md) | 不支持 |  |  |
| [客户端认证证书](client-authentication-certificate.md) | 不支持 |  |  |
| 访问控制 | [配置](configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md) [Referer](configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md) [防盗链](configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md) | 不支持 |  |
| [URL](url-signing.md) [鉴权](url-signing.md) | 不支持 |  |  |
| [IP](configure-an-ip-blacklist-or-whitelist.md) [黑/白名单](configure-an-ip-blacklist-or-whitelist.md) | 不支持 |  |  |
| [配置](configure-a-user-agent-blacklist-or-whitelist.md) [UA](configure-a-user-agent-blacklist-or-whitelist.md) [黑白名单](configure-a-user-agent-blacklist-or-whitelist.md) | 不支持 |  |  |
| [配置远程鉴权](configure-remote-authentication.md) | 不支持 |  |  |
| 性能优化 | [页面优化](enable-html-optimization.md) | 不支持 |  |
| [Gzip](use-the-gzip-compression-feature.md) [压缩](use-the-gzip-compression-feature.md) | 不支持 |  |  |
| [Brotli](configure-brotli-compression.md) [压缩](configure-brotli-compression.md) | 不支持 |  |  |
| [忽略参数](ignore-parameters.md) | 不支持 |  |  |
| [图像处理](image-editing.md) | 不支持 |  |  |
| 视频相关 | [配置](object-chunking.md) [Range](object-chunking.md) [回源](object-chunking.md) | 不支持 |  |
| [配置拖拽播放](video-seeking.md) | 不支持 |  |  |
| [配置听视频](audio-extraction.md) | 不支持 |  |  |
| [配置音视频试看](audio-and-video-preview.md) | 不支持 |  |  |
| [配置](m3u8-encryption-and-rewrite.md) [M3U8](m3u8-encryption-and-rewrite.md) [标准加密改写](m3u8-encryption-and-rewrite.md) | 不支持 |  |  |
| 流量限制 | [配置用量封顶](configure-usage-cap.md) | 不支持 |  |
| [配置单请求限速](configuration-order-request-speed-limit.md) | 不支持 |  |  |
| 边缘脚本 | [边缘脚本](edgescript-overview.md) [EdgeScript](edgescript-overview.md) | 不支持 |  |
| 规则引擎 | [规则引擎](rules-engine.md) | 不支持 |  |
| Quic 协议 | [配置](what-is-the-quic-protocol.md) [QUIC](what-is-the-quic-protocol.md) [协议](what-is-the-quic-protocol.md) | 不支持 |  |
| 资源监控 | 资源监控 | [资源监控](resource-monitoring.md) | 不支持 |
| 实时监控 | [实时监控](real-time-monitoring.md) | 不支持 |  |
| 边缘脚本监控 | [边缘脚本监控](es-monitoring.md) | 不支持 |  |
| 刷新和预热 | 刷新资源 | [刷新和预热资源](refresh-and-prefetch-resources.md) | 支持 |
| 预热资源 | [刷新和预热资源](refresh-and-prefetch-resources.md) | 不支持 |  |
| 工具服务 | 检测 IP 地址 | [检测](does-the-ip-belong-to-cdn-pops.md) [IP](does-the-ip-belong-to-cdn-pops.md) [地址](does-the-ip-belong-to-cdn-pops.md) | 支持 |
| 自助诊断工具 | [自助诊断工具](self-diagnostic-tools.md) | 不支持 |  |
| 安全防护 | 证书服务 | [批量配置](configure-an-ssl-certificate-for-multiple-domain-names.md) [HTTPS](configure-an-ssl-certificate-for-multiple-domain-names.md) [证书](configure-an-ssl-certificate-for-multiple-domain-names.md) | 支持 |
| [查询域名证书](query-ssl-certificates-of-domain-names.md) | 支持 |  |  |
| 沙箱 | [沙箱说明](introduction-to-sandboxes.md) | 不支持 |  |
| 用量查询 | 用量查询 | [用量查询](query-resource-usage-1.md) | 支持 |
| 资源包管理 | [资源包管理](query-the-details-of-resource-plans.md) | 支持 |  |
## 配置入口
[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)
在左侧导航栏，单击域名管理。
单击添加域名，在域名信息页面，配置加速区域，选择全球（不包含中国内地）。
开启全球资源计划。
在业务信息配置页面，设置加速区域（如全球（不包含中国内地））、加速域名、业务类型（如图片小文件）和标签等参数。
## 查看域名是否开启全球资源计划
全球资源计划开启后仅支持部分配置功能，不支持的功能入口将不可见。如果需要确认某个加速域名当前的全球资源计划状态，可通过以下方法查看：
[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)
在左侧导航栏，单击域名管理。
单击目标域名，在域名信息页面的基础信息在页签查看：
显示全球资源计划：已开启：该域名已开启全球资源计划。
未显示该项：该域名未开启全球资源计划。
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
