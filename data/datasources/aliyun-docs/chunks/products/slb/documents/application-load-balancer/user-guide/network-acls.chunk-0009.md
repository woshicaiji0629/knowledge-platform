ses.md)[IP](../use-cases/preserve-client-ip-addresses.md)，再基于真实IP配置allow/deny规则。
想对单个域名或URL路径做访问限制
说明：访问控制ACL作用于监听级别，无法按域名或路径区分。开启后该监听下所有域名均受影响。
替代方案：标准版或WAF增强版ALB可通过转发规则实现——在转发条件中同时配置域名/路径和SourceIp条件，对匹配的请求返回固定响应（如403）。单条转发规则的SourceIp条件最多支持5个IP/CIDR段，且不支持0.0.0.0/x格式。如IP数量较多或使用基础版ALB，建议接入WAF，通过[自定义规则](../../../../waf/documents/web-application-firewall-3-0/user-guide/configure-custom-rules-to-defend-against-specific-requests.md)实现域名/路径与IP组合的访问控制。
想封禁国外IP
说明：ALB访问控制不提供地域封禁功能，无法自动识别IP所属国家。
替代方案：可以手动将已知国外IP段加入黑名单，但无法自动更新且条目数有上限。建议使用WAF的[区域封禁](../../../../waf/documents/web-application-firewall-3-0/user-guide/configure-region-blacklist-rules-to-block-requests-from-specific-regions.md)功能实现。
