](../support/faq-about-alb.md)[类型](../support/faq-about-alb.md)需保持一致。
协议版本：如需支持IPv6访问，选择[双栈](alb-instance-overview.md)；否则选择IPv4。
购买双栈ALB实例前，请为实例所在交换机[开启](../../../../vpc/documents/vpc-and-vswitch.md)[IPv6](../../../../vpc/documents/vpc-and-vswitch.md)。仅支持新建双栈实例，不支持升级已有IPv4实例为双栈。
[功能版本](../product-overview/functional-characteristics.md)（实例费）：
基础版：提供应用型负载均衡的基本功能，可支持基于域名、URL、HTTP Header等路由转发。
标准版：在基础版之上，还支持自定义TLS安全策略、链路追踪等特性，以及重定向、重写等高级路由功能。
WAF增强版：在标准版之上，集成Web应用防火墙（WAF 3.0），为Web业务提供应用层安全防护。
若账号未开通WAF实例，购买WAF增强版ALB实例将自动开通WAF 3.0按量付费实例。若账号已开通WAF 3.0包年包月实例，购买WAF增强版ALB实例后，不会额外产生WAF费用。若账号下已开通WAF 2.0实例，需先[释放](../../../../waf/documents/web-application-firewall-2-0/user-guide/terminate-the-waf-service.md)[WAF 2.0](../../../../waf/documents/web-application-firewall-2-0/user-guide/terminate-the-waf-service.md)[实例](../../../../waf/documents/web-application-firewall-2-0/user-guide/terminate-the-waf-service.md)或者[迁移至](../../../../waf/documents/product-overview/migrate-a-waf-instance-to-waf-3.md)[WAF 3.0](../../../../waf/documents/product-overview/migrate-a-waf-instance-to-waf-3.md)。ALB 默认不开启 X-Forwarded-Proto 头字段。释放 WAF 2.0 实例后，直接访问 ALB 可能会因后端服务无法正确识别协议（HTTP/HTTPS）而导致业务异常（例如，无限重定向）。为避免此问题，务必在 ALB
