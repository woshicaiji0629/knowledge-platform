| 功能 | 说明 |
| --- | --- |
| [配置](configure-the-cdn-cache-expiration-time.md) [CDN](configure-the-cdn-cache-expiration-time.md) [缓存过期时间](configure-the-cdn-cache-expiration-time.md) | 通过配置缓存过期时间规则，可以精细化控制 CDN 节点的资源缓存时长，以平衡内容更新、访问性能与回源成本。此文档介绍缓存规则的工作原理、配置方法、验证、排障流程及最佳实践。 |
| [配置状态码过期时间](create-a-cache-rule-for-http-status-codes.md) | CDN 节点从源站获取资源时，源站会返回响应状态码，您可以在阿里云 CDN 上配置状态码缓存时间，当客户端再次请求相同资源时，由 CDN 直接响应状态码，不会触发回源，减轻源站压力。当状态码超过设置的缓存时间，会重新触发回源。 |
| [配置状态码过期时间（源站优先）](../create-a-status-code-expiration-rule-that-honors-origin.md) | 如果您需要根据源站响应的不同状态码，设置静态资源在 CDN 节点上的缓存过期时间，则可以配置状态码过期时间（源站优先）功能。 |
| [修改出站响应头](create-a-custom-http-response-header.md) | 出站响应头是 HTTP 响应消息头的组成部分之一，可携带特定响应参数并传递给客户端，用来控制缓存行为。通过修改出站响应头，当用户请求加速域名下的资源时， CDN 返回的响应消息会携带您配置的响应头，从而实现跨域访问等特定功能。 |
| [配置自定义页面](create-a-custom-error-page.md) | 配置自定义错误页面后，当用户请求的内容不存在或出现错误时，CDN 节点会返回自定义的错误页面，而不是默认的错误页面。自定义错误页面可以提高用户体验，让用户看到更友好的错误提示。 |
| [重写访问](create-an-access-url-rewrite-rule.md) [URL](create-an-access-url-rewrite-rule.md) | 如果源站资源路径变化， CDN 节点资源路径也会变化。用户请求的 URL 路径不变时， CDN 节点需要重写请求的 URL，将其重定向到目标路径，以减少回源并提升客户端访问性能。 |
| [自定义](create-custom-cache-keys.md) [Cache Key](create-custom-cache-keys.md) | 您可以将访问同一个文件的一类请求转化为统一的 Cachek
