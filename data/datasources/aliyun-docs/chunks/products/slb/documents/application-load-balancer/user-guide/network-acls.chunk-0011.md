识别客户端真实IP，需在正确的层级配置访问控制。以CNAME接入WAF的场景为例（客户端 → CDN → WAF → ALB → ECS），各层的源IP和访问控制建议如下。
WAF增强版ALB通过SDK集成实现防护，WAF不参与流量转发，因此不存在WAF回源环节。如果ALB前无CDN等七层代理，则不存在本节描述的问题。

| 层级 | 看到的源 IP | 访问控制建议 |
| --- | --- | --- |
| WAF | 无 CDN 时为客户端真实 IP。 有 CDN 时为 CDN 回源 IP，需在 WAF 接入配置中设置 [客户端](../../../../waf/documents/web-application-firewall-3-0/user-guide/add-a-domain-name-to-waf-in-cname-record-mode.md) [IP](../../../../waf/documents/web-application-firewall-3-0/user-guide/add-a-domain-name-to-waf-in-cname-record-mode.md) [判定方式](../../../../waf/documents/web-application-firewall-3-0/user-guide/add-a-domain-name-to-waf-in-cname-record-mode.md) 以获取真实客户端 IP。 | 推荐在此层做 IP 黑白名单 。WAF 正确配置后可基于客户端真实 IP 进行拦截，同时支持地域封禁功能。 |
| ALB | WAF 的回源 IP。 | 在 ALB 配置白名单，仅允许 WAF 的回源 IP 段访问，防止攻击者绕过 WAF 直接访问 ALB 公网 IP。 [WAF](../../../../waf/documents/web-application-firewall-3-0/user-guide/faq-about-the-cloud-native-mode.md) [回源](../../../../waf/documents/web-application-firewall-3-0/user-guide/faq-about-the-cloud-native-mode.md) [IP](../../../../waf/documents/web-application-firewall-3-0/user-guide/faq-about-the-cloud-native-mode.md) [段](../../../../waf/documents/web-application-firewall-3-0/user-guide/faq-about-the-cloud-native-mode.md) 可在 WAF 控制台的 接入管理 页面查看。 |
| 后端 ECS | ALB 的 Local IP（从 ALB 实例所在交换机分配的私网地址）。 | 请确保后端 ECS 的 iptables 或其他第三方安全软件未屏蔽 ALB 的 Local IP 网段，否则健康检查和请求转发会失败。 |
