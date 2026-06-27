evalidate | String | 否 | 过期时间为 0 时强制内容验证，可以配置的值为： on：开启。 过期时间为 0 时，支持在 CDN 节点上缓存内容，并且每次请求都需要回源验证缓存内容。 off（默认）：关闭。 过期时间为 0 时，CDN 节点不缓存内容，每次请求都需要回源重新获取内容。 | off |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "file_type", "argValue": "jpg" }, { "argName": "code_string", "argValue": "403=10" }, { "argName": "swift_code_origin_cache_high", "argValue": "off" }, { "argName": "swift_code_no_cache_low", "argValue": "off" }, { "argName": "swift_code_follow_cachetime", "argValue": "off" }, { "argName": "force_revalidate", "argValue": "off" }], "functionName": "filetype_force_ttl_code" }], "DomainNames": "example.com" }
path_force_ttl_code
功能说明：配置路径状态码过期时间，该功能详细介绍请参见控制台配置说明[配置状态码过期时间](../user-guide/create-a-cache-rule-for-http-status-codes.md)。
功能ID（FunctionID/FuncId）：65。
参数说明：
