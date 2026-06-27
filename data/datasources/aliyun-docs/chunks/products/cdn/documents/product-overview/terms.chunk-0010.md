## 回源协议
回源协议，指CDN节点回源时使用的协议，有可能与客户端访问资源时使用的协议相同，也有可能不相同。例如，当客户端使用HTTPS方式请求未缓存在CDN节点上的资源时，可以配置CDN节点使用HTTPS协议回源站获取资源，也可以配置使用HTTP协议回源（源站不支持HTTPS协议的情况下）。具体配置，可参见[配置回源协议](../user-guide/configure-the-origin-protocol-policy.md)。
