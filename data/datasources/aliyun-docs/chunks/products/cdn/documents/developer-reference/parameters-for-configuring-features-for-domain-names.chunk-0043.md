evalidate | String | 否 | 过期时间为 0 时强制内容验证，可以配置的值为： on：开启。 过期时间为 0 时，支持在 CDN 节点上缓存内容，并且每次请求都需要回源验证缓存内容。 off（默认）：关闭。 过期时间为 0 时，CDN 节点不缓存内容，每次请求都需要回源重新获取内容。 | off |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "path", "argValue": "/example/demo" }, { "argName": "code_string", "argValue": "403=10,404=15" }, { "argName": "swift_code_origin_cache_high", "argValue": "off" }, { "argName": "swift_code_no_cache_low", "argValue": "off" }, { "argName": "swift_code_follow_cachetime", "argValue": "off" }, { "argName": "force_revalidate", "argValue": "off" }], "functionName": "path_force_ttl_code" }], "DomainNames": "example.com" }
default_ttl_code
功能说明：配置状态码过期时间（源站优先），该功能详细介绍请参见控制台配置说明[配置状态码过期时间（源站优先）](../create-a-status-code-expiration-rule-that-honors-origin.md)。
功能ID（FunctionID/FuncId）：207。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| default_ttl_code | String | 是 | 状态码及其缓存时间，单位为秒，取值范围是 1~99999999（3 年多一些），多个状态码之间用半角逗号（,）分隔。 | 4xx=3,200=3600,5xx=1 |
