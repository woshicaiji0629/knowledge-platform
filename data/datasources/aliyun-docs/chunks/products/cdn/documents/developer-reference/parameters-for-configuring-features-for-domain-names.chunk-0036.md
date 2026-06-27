## 缓存配置
filetype_based_ttl_set
功能说明：配置文件过期时间，该功能详细介绍请参见控制台配置说明[配置](../user-guide/configure-the-cdn-cache-expiration-time.md)[CDN](../user-guide/configure-the-cdn-cache-expiration-time.md)[缓存过期时间](../user-guide/configure-the-cdn-cache-expiration-time.md)。
功能ID（FunctionID/FuncId）：6。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| ttl | Integer | 是 | 缓存时间，单位为秒，取值范围是 1~99999999（3 年多一些）。 | 500000 |
| file_type | String | 是 | 文件类型，区分大小写。多个文件类型用半角逗号（,）分隔。例如 jpg,txt。 | jpg |
| weight | Integer | 否 | 权重。取值：1~99。 说明 默认为 1，数字越大优先级越高。 | 1 |
| swift_origin_cache_high | String | 否 | 源站响应缓存策略优先，当开启时，表示在源站响应缓存相关头（比如 Cache-Control、Pragma 等）的时候，源站的缓存策略优先生效。可以配置的值为： on：开启 off（默认）：关闭 | off |
| swift_no_cache_low | String | 否 | 忽略源站不缓存响应头，当开启时，表示忽略源站的以下响应头（均表示不缓存）。 Cache-Control: no-store Cache-Control: no-cache Cache-Control: max-age=0 Pragme: no-cache 可以配置的值为： on：开启 off（默认）：关闭 | off |
| swift_follow_cachetime | String | 否 | 客户端跟随 CDN 缓存策略，当开启时，表示将最终生效的 CDN 缓存策略响应给客户端。可以配置的值为： on：开启 off（默认）：关闭 | off |
| force_revalidate | String | 否 | 过期时间为 0 时强制内容验证，可以配置的值为： on：开启。 过期时间为 0 时，支持在 CDN 节点上缓存内容，并且每次请求都需要回源验证缓存内容。 off（默认）：关闭。 过期时间为 0 时，CDN 节点不缓存内容，每次请求都需要回源重新获取内容。 | off |
