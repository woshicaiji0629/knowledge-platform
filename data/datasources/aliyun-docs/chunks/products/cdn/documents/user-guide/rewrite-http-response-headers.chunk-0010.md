## 默认预设响应头
阿里云CDN默认预设了Cache-Control、Content-Type、Expires、Last-Modified四个修改入站响应头，这四个响应头是HTTP协议中的重要组成部分，它们分别用于控制缓存、定义内容类型、设置过期时间以及记录资源的最后修改时间。

| CDN 默认预设响应头 | 说明 | 示例 |
| --- | --- | --- |
| Cache-Control | 用于控制资源在 CDN 缓存中的行为和时间周期的头信息。它为 CDN 节点和客户端浏览器提供了缓存指示，例如何时缓存内容、缓存多久，以及缓存的内容何时被认为是过时的。优先级高于旧的 Expires 头部。 | Cache-Control: no-cache 强制在使用缓存的资源之前总是向源站进行验证。 Cache-Control: max-age=3600 指示资源在 3600 秒（1 小时）内是新鲜的，可以从 CDN 缓存中提供，无需回源。 |
| Content-Type | 描述了返回给客户端的资源的数据类型。它帮助客户端正确地解释和显示接收到的数据。CDN 使用这个头信息来处理对应的数据类型以及如何传输它们。 | Content-Type: text/html 表示发送的内容是 HTML 格式。 Content-Type: image/jpeg 表示资源是 JPEG 图像格式。 |
| Expires | 提供了一个具体的日期/时间，这个时间点之后资源被认为是过期的。CDN 使用这个头来确定资源是否仍然有效，如果过期，CDN 将回源请求新的资源。 Expires 响应头是一个相对古老的头部，在 HTTP/1.1 中， Cache-Control 头部提供了更细粒度的控制，因此 Expires 的使用已经逐渐减少。 | Expires: Thu, 01 Dec 2023 16:00:00 GMT 指出在指定的 GMT 时间后，内容过期。 |
| Last-Modified | 表示资源最后一次被修改的时间。CDN 和浏览器使用这个响应头来判断自从该资源上次被缓存后是否有被修改过。 | Last-Modified: Wed, 21 Oct 2023 07:28:00 GMT 显示资源最后修改的时间。 |
