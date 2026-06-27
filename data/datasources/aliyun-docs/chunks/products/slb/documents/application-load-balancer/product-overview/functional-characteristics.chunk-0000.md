# 功能特性
ALB功能版本：
基础版：提供应用型负载均衡的基本功能，可支持基于域名、URL、HTTP Header等路由转发。
标准版：在基础版之上，支持更多功能特性，增强了转发、安全、监控和连接管理等能力。
WAF增强版：在标准版之上，集成Web应用防火墙（[WAF 3.0](../../../../waf/documents/web-application-firewall-3-0/product-overview/what-is-waf.md)），为Web业务提供应用层安全防护。
扩展版：基于灵活的“服务扩展”能力，提供身份认证、基于内容的路由等核心流量治理功能，并新增多模型代理、负载感知路由、Token限速等AI原生特性，打造面向AI及传统应用的一体化智能流量入口。
ALB的[实例性能指标](what-is-alb.md)与功能版本无关。[ALB](../../product-overview/alb.md)[升级实例](../../product-overview/alb.md)支持通过[安全组](../user-guide/add-an-alb-instance-to-a-security-group.md)或[访问控制策略组（ACL）](../user-guide/network-acls.md)管理流量，而升级前的实例仅支持ACL。如需使用安全组，请[新建实例](../user-guide/create-and-manage-alb-instances.md)或联系商务经理对存量实例进行升级。
