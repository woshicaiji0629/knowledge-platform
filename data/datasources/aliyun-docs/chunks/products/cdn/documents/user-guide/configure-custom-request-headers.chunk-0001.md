## 背景信息
HTTP请求头是HTTP的请求消息头的组成部分之一，可携带特定的请求参数信息并传递给服务器。
当CDN节点请求回源站拉取资源时，源站可获取到回源请求头中携带的信息。您可以通过该功能，改写用户回源请求中的HTTP Header信息，携带特定的参数信息给源站，实现特定业务需求。例如，通过X-Forwarded-For头部携带真实客户端IP至源站。
源站服务器通过用户回源请求中携带的X-Forwarded-For头部获取客户端真实IP的方式，请参见[获取客户端真实](../../../waf/documents/web-application-firewall-2-0/user-guide/retrieve-the-originating-ip-addresses-of-clients.md)[IP](../../../waf/documents/web-application-firewall-2-0/user-guide/retrieve-the-originating-ip-addresses-of-clients.md)。
