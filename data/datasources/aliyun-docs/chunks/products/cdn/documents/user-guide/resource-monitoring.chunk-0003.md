| 监控项 | 监控指标 | 相关 API |
| --- | --- | --- |
| 访问流量/带宽 | 展示加速域名的带宽和流量。 支持按区域、运营商和协议（HTTP、HTTPS、QUIC、IPv4 和 IPv6）查询。 | [查询带宽-按协议](../api-describedomainbpsdatabylayer.md) [查询用量-按天](../api-describedomainsusagebyday.md) |
| 回源流量/带宽 | 展示加速域名的回源带宽和回源流量。 说明 回源宽带：指当用户请求的资源在 CDN 节点未命中时，CDN 节点向源站请求资源所消耗的网络带宽。 回源流量：指当 CDN 节点无法从本地缓存中获取用户请求的内容时，需要向源服务器请求数据的流量。 | [查询回源带宽](../api-describedomainsrcbpsdata-2.md) [查询回源流量](../api-describedomainsrctrafficdata.md) |
| 访问请求数 | 展示加速域名的请求次数和 QPS。 支持按区域、运营商和协议（HTTP、HTTPS、QUIC、IPv4 和 IPv6）查询。 说明 加速域名的请求次数指最小时间粒度内的请求数总和（例如最小时间粒度为 5 分钟，那么展示的加速域名请求次数指 5 分钟内的请求数总和）。 QPS 指的是每秒的请求次数。 | [查询](../api-describedomainqpsdatabylayer.md) [QPS-按协议](../api-describedomainqpsdatabylayer.md) |
| 命中率 | 展示加速域名的字节命中率和请求命中率。 说明 字节命中率：单位时间内 CDN 节点响应用户的总字节数中，CDN 节点直接响应（非回源）的字节数占比。计算公式为：（CDN 节点响应用户的总字节数 - 源站响应 CDN 节点的总字节数）÷ CDN 节点响应用户的总字节数。 命中率：单位时间内所有请求（包含 HTTP 协议和 HTTPS 协议）的字节命中率。 HTTPS 命中率：单位时间内 HTTPS 请求的字节命中率。 | [查询字节命中率](../api-describedomainhitratedata.md) [查询请求命中率](../api-describedomainreqhitratedata.md) |
| HTTPCODE | 展示加速域名的 HTTP 状态码信息，支持按照 2xx、3xx、4xx 和 5xx 维度查询。参考 [HTTP](../developer-reference/http-status-code-description.md) [状态码](../developer-reference/http-status-code-d
