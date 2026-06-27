## 常见问题
配了白名单，任意IP仍能访问
原因：策略组未关联到监听；或策略组中没有添加任何IP条目（空策略组等同于全部放通）。
解决方案：进入ALB实例的监听页签，确认目标监听的访问控制列显示已开启，并确认关联的策略组中包含IP条目。
想临时全放通，添加0.0.0.0/0到白名单不生效
原因：访问控制策略组不支持添加0.0.0.0/0，控制台会提示格式错误。
解决方案：正确做法是直接[关闭访问控制](network-acls.md)，需要时再开启。
配了黑名单，目标IP仍能访问
原因：请求经CDN/WAF转发到ALB，ALB看到的源IP是CDN/WAF的回源IP，而非客户端真实IP。
解决方案：ALB访问控制在四层生效，匹配的是请求报文的源IP地址。当请求经CDN/WAF转发时，源IP是CDN/WAF的回源IP，因此ALB层的黑名单无法拦截客户端IP。需要在WAF或CDN层配置黑名单。
黑名单无法拦截X-Forwarded-For中的IP
原因：ALB访问控制在四层生效，仅匹配请求报文的源IP地址，不解析七层HTTP头部中的X-Forwarded-For字段。
解决方案：可在 WAF 中通过[自定义规则](../../../../waf/documents/web-application-firewall-3-0/user-guide/configure-custom-rules-to-defend-against-specific-requests.md)实现：将匹配字段设为 X-Forwarded-For、逻辑符设为包含、匹配内容填写目标IP，规则动作设为拦截。参考[配置自定义规则中的匹配条件说明](../../../../waf/documents/web-application-firewall-3-0/user-guide/match-conditions.md)。
在后端Nginx配了allow/deny不生效
原因：经过ALB代理后，后端服务器收到的请求来源IP是ALB的Local IP（从ALB实例所在交换机分配的私网地址），Nginx的allow/deny基于来源IP判断，因此无法匹配客户端IP。
解决方案：
（推荐）改用ALB访问控制功能，在ALB层直接配置IP黑白名单。
在Nginx中通过X-Forwarded-For请求头[获取客户端真实](../use-cases/preserve-client-ip-addresses.md)[IP](../use-cases/preserve-client-ip-addresses.md)，再基于真实IP配置allow/deny规则。
想对单个域名或URL路径做访问限制
说明：访问控制ACL作用于监听级别，无法按域名或路径区分。开启后该监听下所有域名均受影响。
替代方案：标准版或WAF增强版
