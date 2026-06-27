### 忽略参数

| 作用 | 适用场景 |
| --- | --- |
| 去除请求 URL 参数（ ? 之后的部分），使携带不同参数的请求命中同一缓存文件，提高缓存命中率、减少回源次数。 | 当 URL 参数与资源内容无关（如用户 UID、渠道来源、推荐码等），建议开启忽略参数。例如，以下两个请求访问同一资源但携带不同 UID： A 用户： http://example.com/1.jpg?uid=123*** B 用户： http://example.com/1.jpg?uid=654*** 未开启忽略参数时，CDN 节点会将 A、B 用户的 URL 视为不同资源，无法命中同一缓存，每次都需回源。开启忽略参数后，CDN 节点会去除 URL 参数，统一使用 http://example.com/1.jpg 匹配缓存。 |

说明
[配置](configure-url-signing.md)[URL](configure-url-signing.md)[鉴权](configure-url-signing.md)的优先级高于忽略参数。鉴权方式A的鉴权信息包含URL参数部分，CDN会先完成鉴权判断，通过后再缓存副本。
