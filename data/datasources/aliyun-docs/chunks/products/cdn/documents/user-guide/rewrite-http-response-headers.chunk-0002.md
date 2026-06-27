## 适用场景
以下是一些常见的场景和示例：
内容类型不正确：如果源站返回的内容类型（Content-Type）与实际内容不符，客户端可能会无法正确解析。例如，一个HTML文件被错误地标记为纯文本。这时可以通过配置回源响应头来修正。
示例：将Content-Type: text/plain更改为Content-Type: text/html。
缓存策略控制：如果您需要对CDN缓存策略进行更精细的控制，可以调整源站的回源响应头中的Cache-Control或Expires字段。这有助于优化内容的更新频率和缓存命中率。
示例：将Cache-Control: max-age=3600更改为Cache-Control: max-age=86400，以延长缓存有效期。CDN的默认缓存规则具体请参见[阿里云](configure-the-cdn-cache-expiration-time.md)[CDN](configure-the-cdn-cache-expiration-time.md)[默认缓存规则及优先级](configure-the-cdn-cache-expiration-time.md)。
跨域资源共享（CORS）：如果您希望允许其他域名的Web应用访问CDN上托管的资源，则需要在源站设置Access-Control-Allow-Origin和其他相关的CORS头。这些设置确保在浏览器执行跨域请求时，CDN能够提供适当的响应头给客户端，避免CORS错误。关于跨域访问问题，您可以参见[配置跨域资源共享](configure-cors.md)。
示例：
Access-Control-Allow-Origin: *：允许所有域名进行跨域资源请求。
Access-Control-Allow-Methods: GET, POST, OPTIONS：指定允许跨域请求的HTTP方法。
压缩传输：如果源站支持压缩传输但没有启用，或者使用的压缩算法不是最有效的，可以通过设置回源响应头中的Accept-Encoding来让源站使用最优的压缩方式。
示例：将Accept-Encoding: gzip, deflate更改为Accept-Encoding: br，以优先使用Brotli压缩。关于Brotli压缩相关内容具体请参见[Brotli](configure-brotli-compression.md)[压缩](configure-brotli-compression.md)。
重定向：当源站需要重定向用户到另一个URL时，回源响应头可以设置正确的重定向响应头。关于重定向具体请参见[配置回源](configure-301-or-302-redirection.md)[301/302](configure-301-or-302-redirection.md)[跟随](conf
