path_force_ttl_code
功能说明：配置路径状态码过期时间，该功能详细介绍请参见控制台配置说明[配置状态码过期时间](../user-guide/create-a-cache-rule-for-http-status-codes.md)。
功能ID（FunctionID/FuncId）：65。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| path | String | 是 | 目录，必须以正斜线（/）开头，例如：/image。 | /example/demo |
| code_string | String | 是 | 状态码及其缓存时间，单位为秒，取值范围是 1~99999999（3 年多一些），多个用半角逗号（,）分隔。例如：302=0,301=0,4xx=2。 | 403=10,404=15 |
| swift_code_origin_cache_high | String | 否 | 源站响应缓存策略优先，当开启时，表示在源站响应缓存相关头（比如 Cache-Control、Pragma 等）的时候，源站的缓存策略优先生效。可以配置的值为： on：开启 off（默认）：关闭 | off |
| swift_code_no_cache_low | String | 否 | 忽略源站不缓存响应头，当开启时，表示忽略源站的以下响应头（均表示不缓存）。 Cache-Control: no-store Cache-Control: no-cache Cache-Control: max-age=0 Pragme: no-cache 可以配置的值为： on：开启 off（默认）：关闭 | off |
| swift_code_follow_cachetime | String | 否 | 客户端跟随 CDN 缓存策略，当开启时，表示将最终生效的 CDN 缓存策略响应给客户端。可以配置的值为： on：开启 off（默认）：关闭 | off |
| force_revalidate | String | 否 | 过期时间为 0 时强制内容验证，可以配置的值为： on：开启。 过期时间为 0 时，支持在 CDN 节点上缓存内容，并且每次请求都需要回源验证缓存内容。 off（默认）：关闭。 过期时间为 0 时，CDN 节点不缓存内容，每次请求都需要回源重新获取内容。 | off |
