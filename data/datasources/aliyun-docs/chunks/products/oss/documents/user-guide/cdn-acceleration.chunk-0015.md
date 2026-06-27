### 风险防范
流量盗用防护：配置Referer防盗链与URL鉴权
为防止资源被非法站点盗用，产生不必要的流量费用和带宽消耗，必须配置安全防护策略：
Referer防盗链：[配置](../../../cdn/documents/user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[Referer](../../../cdn/documents/user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[黑/白名单](../../../cdn/documents/user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)，通过校验HTTP请求头中的Referer字段，仅允许来自指定域名的访问。
URL鉴权：针对私有权限的OSS Bucket，开启CDN的私有Bucket回源后，CDN节点即获得访问授权，这使得原本需要签名的私有资源能通过CDN域名被公开访问。为恢复对私有资源的安全控制，建议在CDN层面启用[配置](../../../cdn/documents/user-guide/configure-url-signing.md)[URL](../../../cdn/documents/user-guide/configure-url-signing.md)[鉴权](../../../cdn/documents/user-guide/configure-url-signing.md)。
说明
配置CDN加速后，盗链请求可能直接命中CDN缓存而不回源到OSS，从而绕过OSS的防盗链验证。为确保防护有效，必须在CDN层面也配置防盗链规则。
流量异常监控与告警
建议在云监控中为CDN加速域名[设置报警规则](../../../cdn/documents/user-guide/set-an-alert-rule.md)，当CDN流量异常增长时及时发现。
回源链路保障：配置回源SNI与回源HOST
确保CDN与OSS之间的回源通信稳定且安全，是服务可用性的关键保障。
配置回源SNI
为避免不带SNI（Server Name Indication）的CDN回源请求导致OSS访问异常，需在CDN中[配置默认回源](../../../cdn/documents/user-guide/configure-sni.md)[SNI](../../../cdn/documents/user-guide/configure-sni.md)，并
