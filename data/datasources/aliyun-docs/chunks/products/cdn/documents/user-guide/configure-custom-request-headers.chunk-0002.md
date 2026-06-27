## 注意事项
出站请求指用户请求中通过CDN回源的HTTP消息。修改出站请求头配置只会影响通过CDN回源的HTTP消息，对于CDN节点直接响应给用户的HTTP消息不做修改。
不支持对泛域名修改出站请求头。
功能配置在引用规则引擎上的规则条件配置时，配置的执行顺序不是按照配置的优先级顺序执行，而是会按照配置关联的规则条件的优先级顺序来执行。
阿里云CDN默认支持携带以下HTTP请求头回源，您无需额外配置。

| 回源 HTTP Header | 说明 | 示例 |
| --- | --- | --- |
| Ali-Cdn-Real-Ip | 客户端与 CDN 节点建连时使用的真实 IP。 | Ali-Cdn-Real-Ip:192.168.0.1 |
| X-Forwarded-For | 客户端请求经过 CDN 节点回源的整个链路上，包括客户端和 CDN 节点的 IP 信息。 | X-Forwarded-For:192.168.0.1, 172.16.0.1 |
| X-Client-Scheme | 客户端发送到 CDN 节点的应用层请求使用的协议，例如：HTTP、HTTPS。 | X-Client-Scheme:http |
| Host | 客户端请求在回源时实际访问的源站 Web 站点域名。 | Host:example.com |
| Via | 客户端请求经过的所有 CDN 节点的名称。 | Via:cn2546-10.l1, cache1.cn2546-10, l2cn2547-7.l2, cache1.l2cn2547-7 |

修改出站请求头的值如果配置的是某个变量，那么实际使用的时候会被设置为具体的变量值，以下为可以使用的变量。

| 名称 | 回源 HTTP Header | 说明 | 示例 |
| --- | --- | --- | --- |
| Ali-Cdn-Real-Port | $http_Ali_Cdn_Real_Port | 在回源头里面添加客户端真实端口信息，向源站传递客户端端口信息。 | Ali-Cdn-Real-Port:80 |
| Ali_Cdn_Real_Ip | $http_Ali_Cdn_Real_Ip | 在回源头里面添加客户端真实 IP 信息，向源站传递客户端 IP 地址信息。 | Ali-Cdn-Real-Ip:192.168.0.1 |
| x_forwarded_for | $proxy_add_x_forwarded_for | 在回源头里面添加 X-Forwarded-For 信息，向源站传递客户端 IP 和中间的代理服务器 IP。 | X-Forwarded-For:192.168.0.1, 172.16.0.1 |
