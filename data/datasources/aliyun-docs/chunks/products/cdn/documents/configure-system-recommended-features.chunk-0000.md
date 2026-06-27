## 提高缓存命中率与访问速度
访问速度慢通常与缓存命中率低有强关联性，推荐您配置缓存过期时间、过滤参数功能提升缓存命中率。

| 场景 | 说明 | 配置 |
| --- | --- | --- |
| 缓存命中率低、访问速度慢 | 设置的缓存时间过短或未设置缓存规则，导致频繁回源站获取资源。合理配置缓存过期时间，可有效提升资源的缓存命中率，提升访问性能。 缓存时间设置建议如下： 不常更新的静态文件：例如图片、应用下载类型等，缓存时间建议设置 1 个月以上。 频繁更新的静态文件：例如 JS、CSS 等，根据实际业务情况设置。 | [配置缓存过期时间](user-guide/configure-the-cdn-cache-expiration-time.md) |
| 默认客户端回源获取资源时需精确匹配 URL 中 ? 之后的参数。开启忽略参数功能后，客户端回源获取资源时会去除 URL 请求中 ? 之后的参数，有效提高文件缓存命中率，减少回源次数。 | [忽略参数](user-guide/ignore-parameters.md) |  |

如果您想了解缓存命中率低的原因，请参见[CDN](alibaba-cloud-content-delivery-network-cache-hit-rate-is-low.md)[缓存命中率低](alibaba-cloud-content-delivery-network-cache-hit-rate-is-low.md)。
