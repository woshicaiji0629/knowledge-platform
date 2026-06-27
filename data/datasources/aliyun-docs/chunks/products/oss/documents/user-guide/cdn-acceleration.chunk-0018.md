## 常见问题
为什么CDN回源时出现5xx报错？
5xx错误表示CDN无法成功从OSS源站获取资源，需要从以下方面排查：

| 排查方向 | 检查内容 |
| --- | --- |
| 源站配置 | 检查 CDN 控制台配置的 OSS 源站地址是否正确。 |
| 回源协议 | 如果 CDN 配置了 HTTPS 回源或 [协议跟随回源](../../../cdn/documents/user-guide/configure-the-origin-protocol-policy.md) ，请确保源站支持 HTTPS 访问且 SSL 证书配置正确。 |
| 网络链路 | 测试 CDN 节点或本地到 OSS 源站的网络连通性。CDN 节点是公网节点，源站必须连通公网。 |
| 源站压力 | 在 [CDN](https://cdnnext.console.aliyun.com/monitor/realTime) [实时监控](https://cdnnext.console.aliyun.com/monitor/realTime) 页面观察是否存在突增的带宽和流量。对于热点资源，应进行 [预热资源](../../../cdn/documents/user-guide/refresh-and-prefetch-resources.md) 并 [设置合理的缓存周期](../../../cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md) 。 |

为什么配置静态页面后通过CDN加速访问报错403 Forbidden或You are forbidden to list buckets？
原因分析：此问题通常发生在为配置了[静态网站托管](hosting-static-websites.md)的私有Bucket开启CDN加速后。根本原因在于两种访问机制的冲突：
CDN私有回源时会携带签名信息进行身份验证。
OSS静态网站托管的默认首页功能（如访问/时自动返回index.html）要求访问请求必须是匿名的。
当用户访问加速域名的根目录时，CDN发起带签名的请求访问Bucket根目录。OSS收到签名请求后不会触发静态网站托管逻辑，转而尝试执行ListObjects操作，最终导致403错误。
解决方案：绕过OSS的静态网站托管机制，直接在CDN层面通过[重写访问](../../../cdn/documents/user-guide/create-an-access-url-rewrite-rule.md)[URL](../../../cdn/documents/user-guide/create-an-access-url-rewrite-rule.md)实现同样效果：
