evalidate | String | 否 | 过期时间为 0 时强制内容验证，可以配置的值为： on：开启。 过期时间为 0 时，支持在 CDN 节点上缓存内容，并且每次请求都需要回源验证缓存内容。 off（默认）：关闭。 过期时间为 0 时，CDN 节点不缓存内容，每次请求都需要回源重新获取内容。 | off |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "path", "argValue": "/example/demo" }, { "argName": "weight", "argValue": "1" }, { "argName": "ttl", "argValue": "500000" }, { "argName": "swift_origin_cache_high", "argValue": "off" }, { "argName": "swift_no_cache_low", "argValue": "off" }, { "argName": "swift_follow_cachetime", "argValue": "off" }, { "argName": "force_revalidate", "argValue": "off" }], "functionName": "path_based_ttl_set" }], "DomainNames": "example.com" }
filetype_force_ttl_code
功能说明：配置文件状态码过期时间，该功能详细介绍请参见控制台配置说明[配置状态码过期时间](../user-guide/create-a-cache-rule-for-http-status-codes.md)。
功能ID（FunctionID/FuncId）：63。
参数说明：
